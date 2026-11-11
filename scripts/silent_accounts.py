#!/usr/bin/env python3
"""Discord-independent discovery for silent project accounts.

A silent account has few or zero posts, so keyword / from: tweet search never
returns it as an author. Discord alpha Peek is still only a backfill. This
script is the fallback that does not touch that guild.

What the X API can actually do
------------------------------
- ``GET /2/tweets/search/recent`` (the repo's ``search_posts_all`` / recent
  search) indexes posts. A 0-post official account is not in that index.
  ``url:`` and ``@mentions`` only help when *someone else* has already posted
  the domain or the handle. Request
  ``expansions=author_id,entities.mentions.username`` so the mentioned
  profile (description, url, public_metrics) arrives in the same call.
- ``GET /2/users/search`` is a People lookup. The query grammar is
  ``^[A-Za-z0-9_' ]{1,50}$`` — no ``url:``, no ``bio:``, no dotted domain.
  The index matches display name and handle, not the bio. ``description``
  and ``url`` are returned on the user object and filtered locally. App-only
  bearer tokens often 403 this route (it is documented as user-context);
  ``run`` records that and still does the url search.
- ``get_users_by_usernames`` only resolves handles you already have. It is
  not a discovery call.

Residual gap (yums, 2026-11-11 07:35 CST): @yumsdotfun had 0 posts, an empty
profile-website field, and a bio that did not contain the product URL. No
rotating name/handle query contains "yums", and no X endpoint lists brand-new
accounts by themselves. Unless a third party has posted the handle or the
domain, this path cannot see that account. Discord follow-monitors can.
Confirming https://yums.fun later is an HTTP check, not an X read, and it
only helps after the handle is already known.

R1623 shell rule: 0 posts + inflated followers + no confirmed live site and
no on-chain/post evidence stays deferred. This script never writes
data.json, never admits, and never sets focus true.

Usage:
  python3 scripts/silent_accounts.py queries
  python3 scripts/silent_accounts.py queries --remaining 850
  python3 scripts/silent_accounts.py filter raw.json --library data.json
  python3 scripts/silent_accounts.py run --remaining 850
"""
from __future__ import annotations

import argparse
import json
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import x_budget  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.x.com/2"
MAX_POSTS = 3
MAX_AGE_DAYS = 30
FARM_FOLLOWERS = 400  # yums was deferred at ~708 with 0 posts and no live site
KOL_FOLLOWERS = 3000
REVIEW_CAP = 8
PROBE_CAP = 6
HANDLE_RE = re.compile(r"^[A-Za-z0-9_]{1,15}$")
HTTP_RE = re.compile(r"https?://[^\s)>\]\"']+", re.I)
BARE_HOST_RE = re.compile(
    r"(?<![\w./])((?:[a-z0-9-]+\.)+(?:fun|xyz|app|dev|finance))(?![\w])",
    re.I,
)
PRODUCT_RE = re.compile(
    r"(mint|launchpad|launch|whitelist|presale|airdrop|bonding|testnet|mainnet|"
    r"ordinals?|crc20|runes?|layerzero|\boft\b|elysium|tapeout|giwa|dogeevm|dogeos|"
    r"starknet|fair\s*launch|gpu|miner|\bpow\b|挖矿|发射|铸造|空投|电路|打新|白名单|"
    r"测试网|主网|公售)",
    re.I,
)
BUILDER_RE = re.compile(r"(building|official|protocol|\bapp\b|平台|工具|协议)", re.I)
SOCIAL_HOSTS = {
    "x.com",
    "twitter.com",
    "t.me",
    "telegram.me",
    "telegram.org",
    "discord.gg",
    "discord.com",
    "discordapp.com",
    "linktr.ee",
    "youtube.com",
    "youtu.be",
    "instagram.com",
    "tiktok.com",
    "medium.com",
}
BLOCKED_HOSTS = {
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "::1",
    "169.254.169.254",
    "metadata.google.internal",
}
PARKING = (
    "domain is for sale",
    "buy this domain",
    "this webpage is parked",
    "this domain is parked",
    "sedoparking",
    "parkweb",
    "hugedomains",
)


def slugify(handle: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", handle.lower()).strip("-")
    return text or "unknown"


def parse_time(value) -> datetime | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, timezone.utc)
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        dt = None
        for fmt in ("%a %b %d %H:%M:%S %z %Y", "%Y-%m-%d %H:%M:%S%z"):
            try:
                dt = datetime.strptime(str(value).strip(), fmt)
                break
            except ValueError:
                continue
        if dt is None:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def host_of(url: str) -> str:
    try:
        host = (urlparse(url).hostname or "").lower().rstrip(".")
    except Exception:
        return ""
    if host.startswith("www."):
        host = host[4:]
    return host


def is_social(url: str) -> bool:
    host = host_of(url)
    if not host:
        return False
    return any(host == item or host.endswith("." + item) for item in SOCIAL_HOSTS)


def is_blocked_host(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return True
    host = host_of(url)
    if host in BLOCKED_HOSTS or host.endswith(".local"):
        return True
    try:
        packed = socket.inet_aton(host)
    except OSError:
        return False
    # literal private / link-local / loopback
    if packed[0] in (10, 127) or packed[0] == 0:
        return True
    if packed[0] == 169 and packed[1] == 254:
        return True
    if packed[0] == 172 and 16 <= packed[1] <= 31:
        return True
    if packed[0] == 192 and packed[1] == 168:
        return True
    return False


def clean_url(url: str) -> str:
    text = (url or "").strip().rstrip(".,);")
    if not text:
        return ""
    if text.startswith("//"):
        text = "https:" + text
    if not re.match(r"https?://", text, re.I):
        if BARE_HOST_RE.fullmatch(text) or re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", text, re.I):
            text = "https://" + text
        else:
            return ""
    if is_social(text) or is_blocked_host(text):
        return ""
    return text


def urls_in_text(text: str) -> list[str]:
    found: list[str] = []
    for match in HTTP_RE.finditer(text or ""):
        cleaned = clean_url(match.group(0))
        if cleaned and cleaned not in found:
            found.append(cleaned)
    for match in BARE_HOST_RE.finditer(text or ""):
        cleaned = clean_url(match.group(1))
        if cleaned and cleaned not in found:
            found.append(cleaned)
    return found


def meaningful_product_bio(bio: str) -> bool:
    text = (bio or "").strip()
    if len(text) < 8:
        return False
    hits = {item.lower() for item in PRODUCT_RE.findall(text)}
    if urls_in_text(text) and hits:
        return True
    if len(hits) >= 2:
        return True
    if hits and BUILDER_RE.search(text):
        return True
    return False


def _first_int(*values):
    for value in values:
        if value is None or value == "":
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            continue
    return None


def profile_from_user(user: dict, evidence_url: str = "") -> dict | None:
    if not isinstance(user, dict):
        return None
    handle = user.get("username") or user.get("screen_name") or user.get("userName") or user.get("handle") or ""
    handle = str(handle).lstrip("@").strip()
    if not HANDLE_RE.match(handle):
        return None
    metrics = user.get("public_metrics") if isinstance(user.get("public_metrics"), dict) else {}
    entities = user.get("entities") if isinstance(user.get("entities"), dict) else {}
    url_entities = entities.get("url") if isinstance(entities.get("url"), dict) else {}
    expanded = ""
    for item in url_entities.get("urls") or []:
        if isinstance(item, dict):
            expanded = item.get("expanded_url") or item.get("expandedUrl") or ""
            if expanded:
                break
    website = clean_url(expanded) or clean_url(str(user.get("url") or user.get("website") or ""))
    bio = str(user.get("description") if user.get("description") is not None else user.get("bio") or "")
    created = user.get("created_at") or user.get("createdAt")
    return {
        "handle": handle,
        "name": str(user.get("name") or handle),
        "posts": _first_int(metrics.get("tweet_count"), user.get("statuses_count"), user.get("tweet_count"), user.get("posts")),
        "followers": _first_int(metrics.get("followers_count"), user.get("followers_count"), user.get("followers")) or 0,
        "bio": bio,
        "website": website,
        "evidence_url": clean_url(evidence_url),
        "created_at": created,
        "onchain": bool(user.get("onchainConfirmed") or user.get("onchain")),
        "protected": bool(user.get("protected")),
    }


def merge_profiles(left: dict, right: dict) -> dict:
    out = dict(left)
    if right.get("posts") is not None:
        out["posts"] = right["posts"]
    if (right.get("followers") or 0) > (out.get("followers") or 0):
        out["followers"] = right["followers"]
    if len(right.get("bio") or "") > len(out.get("bio") or ""):
        out["bio"] = right["bio"]
    if right.get("website"):
        out["website"] = right["website"]
    if right.get("evidence_url"):
        out["evidence_url"] = right["evidence_url"]
    if right.get("created_at") and not out.get("created_at"):
        out["created_at"] = right["created_at"]
    out["onchain"] = bool(out.get("onchain") or right.get("onchain"))
    out["name"] = right.get("name") or out.get("name")
    return out


def _tweet_urls(tweet: dict) -> list[str]:
    entities = tweet.get("entities") if isinstance(tweet.get("entities"), dict) else {}
    found: list[str] = []
    for item in entities.get("urls") or []:
        if not isinstance(item, dict):
            continue
        cleaned = clean_url(item.get("expanded_url") or item.get("expandedUrl") or item.get("unwound_url") or "")
        if cleaned and cleaned not in found:
            found.append(cleaned)
    for cleaned in urls_in_text(str(tweet.get("text") or "")):
        if cleaned not in found:
            found.append(cleaned)
    return found


def _mention_usernames(tweet: dict) -> list[str]:
    entities = tweet.get("entities") if isinstance(tweet.get("entities"), dict) else {}
    names = []
    for item in entities.get("mentions") or []:
        if isinstance(item, dict) and item.get("username"):
            names.append(str(item["username"]).lstrip("@"))
    return names


def _flatten_payload(payload) -> list:
    if isinstance(payload, list):
        out = []
        for item in payload:
            out.extend(_flatten_payload(item))
        return out
    if isinstance(payload, dict) and isinstance(payload.get("calls"), list):
        return _flatten_payload(payload["calls"])
    return [payload]


def harvest(payload) -> tuple[list[dict], list[dict]]:
    """Normalize user-search or tweet-search JSON into profiles plus URL-only leftovers."""
    profiles: dict[str, dict] = {}
    unresolved: list[dict] = []

    def add(profile: dict | None) -> None:
        if not profile:
            return
        key = profile["handle"].lower()
        profiles[key] = merge_profiles(profiles[key], profile) if key in profiles else profile

    blobs = _flatten_payload(payload)
    for blob in blobs:
        if not isinstance(blob, dict):
            continue
        if "text" in blob and "author_id" in blob and "data" not in blob:
            blob = {"data": [blob], "includes": blob.get("includes") or {}}
        users = []
        if blob.get("username") or blob.get("screen_name") or blob.get("userName"):
            users.append(blob)
        if isinstance(blob.get("users"), list):
            users.extend(blob["users"])
        data = blob.get("data")
        if isinstance(data, list) and data and isinstance(data[0], dict) and (
            data[0].get("username") or data[0].get("screen_name")
        ) and not data[0].get("text"):
            users.extend(data)
        elif isinstance(data, dict) and (data.get("username") or data.get("screen_name")):
            users.append(data)
        for user in users:
            add(profile_from_user(user))

        tweets = []
        if isinstance(data, list) and data and isinstance(data[0], dict) and "text" in data[0]:
            tweets = data
        includes = blob.get("includes") if isinstance(blob.get("includes"), dict) else {}
        by_id = {}
        by_name = {}
        for user in includes.get("users") or []:
            if not isinstance(user, dict):
                continue
            if user.get("id") is not None:
                by_id[str(user["id"])] = user
            uname = user.get("username") or user.get("screen_name")
            if uname:
                by_name[str(uname).lower()] = user
        for tweet in tweets:
            urls = _tweet_urls(tweet)
            evidence = urls[0] if urls else ""
            mentioned = []
            for uname in _mention_usernames(tweet):
                user = by_name.get(uname.lower())
                if user:
                    mentioned.append(user)
                    add(profile_from_user(user, evidence))
                else:
                    # Username only — metrics unknown, so it cannot be reviewed yet.
                    add({
                        "handle": uname,
                        "name": uname,
                        "posts": None,
                        "followers": 0,
                        "bio": "",
                        "website": "",
                        "evidence_url": evidence,
                        "created_at": None,
                        "onchain": False,
                        "protected": False,
                    } if HANDLE_RE.match(uname) else None)
            author = by_id.get(str(tweet.get("author_id") or ""))
            if author:
                add(profile_from_user(author, evidence))
            if urls and not mentioned and not author:
                unresolved.append({"urls": urls, "reason": "url_without_handle"})
            elif urls and not mentioned and author:
                # Author exists but was not an @mention of a project handle.
                # If the author themselves fails the silent gates, the domain
                # still has no separate official handle.
                author_profile = profile_from_user(author, evidence)
                author_silent = bool(
                    author_profile
                    and author_profile.get("posts") is not None
                    and author_profile["posts"] <= MAX_POSTS
                )
                if not author_silent:
                    unresolved.append({
                        "urls": urls,
                        "author": (author_profile or {}).get("handle"),
                        "reason": "url_without_mentioned_handle",
                    })
    return list(profiles.values()), unresolved


def candidate_url(profile: dict) -> str:
    for key in ("website", "evidence_url"):
        cleaned = clean_url(profile.get(key) or "")
        if cleaned:
            return cleaned
    for item in urls_in_text(profile.get("bio") or ""):
        return item
    return ""


def load_known(path: Path) -> set[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    known: set[str] = set()
    for card in data.get("candidates") or []:
        if not isinstance(card, dict):
            continue
        if card.get("id"):
            known.add(str(card["id"]).lower())
        for key in ("handle", "twitter"):
            value = card.get(key)
            if value:
                known.add(str(value).lstrip("@").lower())
        link = ((card.get("links") or {}).get("x")) or ""
        match = re.search(r"(?:x|twitter)\.com/([^/?#]+)", str(link), re.I)
        if match:
            known.add(match.group(1).lower())
    return known


def classify(profile: dict, *, now: datetime, known: set[str], site_live: bool | None) -> dict:
    handle = profile["handle"]
    key = handle.lower()
    if key in known or slugify(handle) in known:
        return {"action": "skip", "reason": "already_in_library", "deferred": False}
    if profile.get("protected"):
        return {"action": "skip", "reason": "protected", "deferred": False}
    posts = profile.get("posts")
    if posts is None:
        return {"action": "skip", "reason": "needs_profile", "deferred": False}
    if posts > MAX_POSTS:
        return {"action": "skip", "reason": "not_silent", "deferred": False}
    created = parse_time(profile.get("created_at"))
    if created is not None and created < now - timedelta(days=MAX_AGE_DAYS):
        return {"action": "skip", "reason": "account_too_old", "deferred": False}
    followers = int(profile.get("followers") or 0)
    if followers >= KOL_FOLLOWERS:
        return {"action": "skip", "reason": "high_followers", "deferred": False}
    bio = profile.get("bio") or ""
    product_bio = meaningful_product_bio(bio)
    url = candidate_url(profile)
    onchain = bool(profile.get("onchain"))
    if not url and not product_bio and not onchain:
        return {"action": "skip", "reason": "no_product_surface", "deferred": False}
    inflated = posts == 0 and followers >= FARM_FOLLOWERS
    needs_live = inflated or not product_bio
    if needs_live and not onchain:
        if site_live is True:
            pass
        elif site_live is False:
            reason = "shell_site_not_live" if inflated else "site_not_live"
            return {"action": "skip", "reason": reason, "deferred": True}
        else:
            reason = "shell_site_unconfirmed" if inflated else "site_unconfirmed"
            return {"action": "skip", "reason": reason, "deferred": True}
    web = url or None
    item = {
        "id": slugify(handle),
        "name": profile.get("name") or handle,
        "handle": "@" + handle,
        "followers": followers,
        "posts": posts,
        "bio": bio,
        "focus": False,
        "links": {"x": f"https://x.com/{handle}"},
        "siteLive": site_live,
        "onchain": onchain,
        "why": _why(posts, followers, product_bio, site_live, onchain),
        "admitHint": "送 DeepSeek admit。普通新卡 focus 必须 false，links.x 已写。本脚本不收录、不写 data.json。",
    }
    if web:
        item["links"]["web"] = web
    if item["focus"] is not False or "x.com/" not in item["links"]["x"]:
        raise RuntimeError("silent review item broke focus/links invariant")
    return {"action": "review", "reason": "review", "deferred": False, "item": item}


def _why(posts: int, followers: int, product_bio: bool, site_live: bool | None, onchain: bool) -> str:
    bits = [f"{posts} posts", f"{followers} followers"]
    if site_live is True:
        bits.append("site live")
    if product_bio:
        bits.append("product bio")
    if onchain:
        bits.append("on-chain evidence")
    return ", ".join(bits)


def screen(
    payload,
    *,
    known: set[str],
    now: datetime,
    site_probe: dict | None = None,
    probe=None,
    do_probe: bool = True,
    admitted: list[str] | None = None,
    queries: list | None = None,
    ran: bool = True,
    note: str = "",
) -> dict:
    profiles, unresolved = harvest(payload)
    site_probe = {str(k).rstrip("/"): v for k, v in (site_probe or {}).items()}
    decisions = []
    pending_probe: list[dict] = []
    for profile in profiles:
        url = candidate_url(profile)
        pre = classify(profile, now=now, known=known, site_live=None)
        if pre["reason"] in ("site_unconfirmed", "shell_site_unconfirmed") and url:
            pending_probe.append(profile)
        else:
            decisions.append((profile, pre))

    probed = 0
    for profile in pending_probe:
        url = candidate_url(profile)
        key = url.rstrip("/")
        live: bool | None
        if key in site_probe:
            live = bool(site_probe[key])
            decisions.append((profile, classify(profile, now=now, known=known, site_live=live)))
            continue
        if not do_probe:
            decisions.append((profile, classify(profile, now=now, known=known, site_live=None)))
            continue
        if probed >= PROBE_CAP:
            decided = classify(profile, now=now, known=known, site_live=None)
            decisions.append((profile, {**decided, "reason": "probe_cap", "deferred": True, "action": "skip"}))
            continue
        live = probe(url) if probe is not None else probe_site(url)
        probed += 1
        decisions.append((profile, classify(profile, now=now, known=known, site_live=live)))

    review = []
    skipped = []
    for profile, decision in decisions:
        if decision["action"] == "review":
            review.append(decision["item"])
        else:
            skipped.append({
                "handle": "@" + profile["handle"],
                "reason": decision["reason"],
                "deferred": bool(decision.get("deferred")),
                "posts": profile.get("posts"),
                "followers": profile.get("followers") or 0,
            })
    review.sort(key=lambda item: (item.get("siteLive") is not True, item.get("posts") or 0, item.get("followers") or 0))
    overflow = review[REVIEW_CAP:]
    review = review[:REVIEW_CAP]
    for item in overflow:
        skipped.append({"handle": item["handle"], "reason": "review_cap", "deferred": False})

    for row in unresolved:
        skipped.append({
            "handle": None,
            "urls": row.get("urls") or [],
            "reason": row.get("reason") or "url_without_handle",
            "deferred": False,
        })

    reasons: dict[str, int] = {}
    for row in skipped:
        reasons[row["reason"]] = reasons.get(row["reason"], 0) + 1
    admitted_norm = [item.lstrip("@").lower() for item in (admitted or [])]
    review_keys = set()
    for item in review:
        review_keys.add(item["handle"].lstrip("@").lower())
        review_keys.add(item["id"].lower())
    admitted_hits = [item for item in admitted_norm if item in review_keys]
    admitted_ignored = [item for item in admitted_norm if item not in review_keys]
    seen = len(profiles) + len(unresolved)
    deferred_rows = [row for row in skipped if row.get("deferred")]
    result = {
        "ran": ran,
        "seen": seen,
        "sentToReview": len(review),
        "admitted": len(admitted_hits),
        "skipped": len(skipped),
        "deferred": len(deferred_rows),
        "deferredHandles": [row["handle"] for row in deferred_rows if row.get("handle")],
        "skipReasons": reasons,
        "review": review,
        "residualGap": x_budget.SILENT_GAP,
        "queries": queries or [],
        "note": (
            (note + " ") if note else ""
        )
        + (
            "admitted 由 DeepSeek 收录之后再填；本字段不自动收录。"
            "延期号不写 data.json，同一轮用已保存的原始 JSON 重新 probe 即可，不必再读 X，也不要占下一轮 silentCap。"
        ),
    }
    if admitted_ignored:
        result["admittedIgnored"] = admitted_ignored
    errors = _api_errors(payload)
    if errors:
        result["apiErrors"] = errors
    return {"silentAccount": result, "review": review}


def _api_errors(payload) -> list[dict]:
    errors = []
    for blob in _flatten_payload(payload):
        if isinstance(blob, dict) and "error" in blob and "data" not in blob and "users" not in blob:
            errors.append({
                "error": blob.get("error"),
                "kind": blob.get("kind"),
                "lane": blob.get("lane"),
            })
    return errors


class _KeepStatus(urllib.request.HTTPErrorProcessor):
    """Let probe_site read 3xx/4xx bodies instead of raising."""

    def http_response(self, request, response):
        return response

    https_response = http_response


def probe_site(url: str, timeout: float = 6.0) -> bool | None:
    current = clean_url(url)
    if not current:
        return False
    opener = urllib.request.build_opener(_KeepStatus)
    for _ in range(4):
        req = urllib.request.Request(
            current,
            headers={"User-Agent": "early-scout-silent/1.0"},
            method="GET",
        )
        try:
            resp = opener.open(req, timeout=timeout)
        except TimeoutError:
            return None
        except urllib.error.URLError as exc:
            if isinstance(getattr(exc, "reason", None), (TimeoutError, socket.timeout)):
                return None
            return False
        except Exception:
            return False
        try:
            code = getattr(resp, "status", 200)
            if code in (301, 302, 303, 307, 308):
                loc = resp.headers.get("Location") or ""
                nxt = urllib.parse.urljoin(current, loc)
                if is_blocked_host(nxt) or is_social(nxt) or not clean_url(nxt):
                    return False
                current = nxt
                continue
            if code >= 500:
                return None
            if not (200 <= code < 300):
                return False
            body = resp.read(4096).decode("utf-8", "replace")
        finally:
            resp.close()
        low = body.lower()
        if any(phrase in low for phrase in PARKING):
            return False
        if len(body.strip()) < 40:
            return False
        return True
    return False


def _bearer() -> str:
    import os

    return (os.environ.get("X_BEARER_TOKEN") or os.environ.get("BEARER_TOKEN") or "").strip()


def fetch_query(spec: dict, token: str, timeout: float = 20.0) -> dict:
    kind = spec.get("kind")
    params = spec.get("params") or {}
    path = "/users/search" if kind == "user" else "/tweets/search/recent"
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(
        f"{API}{path}?{query}",
        headers={"Authorization": f"Bearer {token}", "User-Agent": "early-scout-silent/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:500]
        return {"error": exc.code, "detail": detail, "kind": kind, "lane": spec.get("lane")}
    except Exception as exc:
        return {"error": type(exc).__name__, "detail": str(exc)[:300], "kind": kind, "lane": spec.get("lane")}


def planned_account(now: datetime, remaining: int | None, reason: str) -> dict:
    budget = x_budget.plan(x_budget.load_remaining(remaining), now)
    return {
        "silentAccount": {
            "ran": False,
            "seen": 0,
            "sentToReview": 0,
            "admitted": 0,
            "skipped": 0,
            "reason": reason,
            "mode": budget["mode"],
            "softCap": budget["softCap"],
            "silentCap": budget["silentCap"],
            "queries": budget["silentQueriesThisRound"],
            "residualGap": x_budget.SILENT_GAP,
            "note": "queries 只是计划。跑完现有 X 客户端后把原始 JSON 交给 filter，ran 才会是 true。",
        }
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Silent-account fallback (no Discord)")
    parser.add_argument("command", nargs="?", default="queries", choices=("queries", "filter", "run"))
    parser.add_argument("raw", nargs="?", help="raw X JSON for filter")
    parser.add_argument("--remaining", type=int, default=None)
    parser.add_argument("--library", default=str(ROOT / "data.json"))
    parser.add_argument("--no-probe", action="store_true")
    parser.add_argument("--admitted", default="", help="comma-separated handles already admitted by DeepSeek")
    parser.add_argument("--site-probe", default="", help="JSON object of url -> true/false, skips HTTP for those urls")
    args = parser.parse_args(argv)
    now = datetime.now(x_budget.CST)
    admitted = [item.strip() for item in args.admitted.split(",") if item.strip()]

    if args.command == "queries":
        json.dump(planned_account(now, args.remaining, "planned"), sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    budget = x_budget.plan(x_budget.load_remaining(args.remaining), now)
    if args.command == "run":
        token = _bearer()
        if budget["silentCap"] <= 0:
            json.dump(planned_account(now, args.remaining, budget["mode"]), sys.stdout, ensure_ascii=False, indent=2)
            sys.stdout.write("\n")
            return 0
        if not token:
            planned = planned_account(now, args.remaining, "no_token")
            planned["silentAccount"]["note"] = (
                "未设置 X_BEARER_TOKEN / BEARER_TOKEN。用现有 X 客户端按 queries 打 silentCap 次调用，"
                "不要从 softCap 里扣，然后把原始 JSON 交给 filter。不要把 token 写进仓库。"
            )
            json.dump(planned, sys.stdout, ensure_ascii=False, indent=2)
            sys.stdout.write("\n")
            return 0
        payloads = [fetch_query(spec, token) for spec in budget["silentQueriesThisRound"]]
        payload = {"calls": payloads}
    else:
        if not args.raw or args.raw == "-":
            payload = json.load(sys.stdin)
        else:
            payload = json.loads(Path(args.raw).read_text(encoding="utf-8"))
        if budget["silentCap"] <= 0 and not payload:
            json.dump(planned_account(now, args.remaining, budget["mode"]), sys.stdout, ensure_ascii=False, indent=2)
            sys.stdout.write("\n")
            return 0

    library = Path(args.library)
    known: set[str] = set()
    note = ""
    if library.exists():
        known = load_known(library)
    else:
        note = f"library missing: {library}"
    site_probe = json.loads(args.site_probe) if args.site_probe else {}
    out = screen(
        payload,
        known=known,
        now=now,
        site_probe=site_probe,
        do_probe=not args.no_probe,
        admitted=admitted,
        queries=budget["silentQueriesThisRound"],
        ran=True,
        note=note,
    )
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
