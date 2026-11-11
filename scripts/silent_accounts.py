#!/usr/bin/env python3
"""Owned silent-account discovery for early-scout. Discord is not an input.

Finds project accounts that have few or zero posts, a profile website or a
meaningful product bio, and are not already in data.json. Tweet keyword search
cannot see a 0-post official account. This path uses the X client the scout
already has:

  * search_users  — GET /2/users/search. Plain query, 1–50 chars of
    [A-Za-z0-9_' ]. Matches name / username / bio by relevance. No bio:, no
    url:, no tweet_count, no created_at operator. The user object can include
    description, the profile website (`url`), and public_metrics.
  * search_posts_all — full-archive tweet search. `url:` matches a URL that
    appears inside a tweet, not the profile website field. `has:mentions`
    is how a third party pointing at @someone becomes visible. A 0-post
    account is never the author of a hit.
  * get_users_by_usernames — one batched profile read for @handles a previous
    mention search already found.

The same client has no following-list tool. This script does not scrape
Discord and does not invent a follow-graph.

Reads come from x_budget.silentCap, which is outside softCap. When silentCap
is 0 the path records ran=false and does not borrow userFollowWatch or the
six thin-lane keyword searches.

R1623 gate: 0 posts + inflated followers + no confirmed live site and no
on-chain evidence stays deferred. Nothing here writes data.json or bumps
meta.round. New-card packets always carry links.x and focus false.

  python3 scripts/silent_accounts.py plan
  python3 scripts/silent_accounts.py filter --users /tmp/silent_users.json \\
      --mentions /tmp/silent_mentions.json --profiles /tmp/silent_profiles.json
  python3 scripts/silent_accounts.py result --ran true --seen N \\
      --sent-to-review N --admitted N --skipped N
  python3 scripts/silent_accounts.py selftest
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import socket
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import x_budget  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CST = timezone(timedelta(hours=8))

# R1623 deferred @yumsdotfun at 708 followers, 0 posts, site not live.
# TokenGuardian (644 followers, parked domain, 0 posts) was rejected the same morning.
INFLATED_FOLLOWERS = 500
MAX_POSTS = 3
NEW_ACCOUNT_DAYS = 120
MAX_DEFERRED = 10
MAX_SITE_CHECKS = 5
SITE_TIMEOUT = 4.0
BODY_LIMIT = 65536

RESIDUAL_GAP = (
    "推文搜索看不见 0 帖官号（没有帖可索引）。search_users 是名字/用户名/bio 的相关度匹配，"
    "query 只能是 [A-Za-z0-9_' ] 且最长 50，没有 bio:、url:、帖数或注册时间算子；"
    "资料栏网站要等用户对象返回后才能读。search_posts_all 的 url: 只命中帖子正文里的链接，"
    "不是资料栏网站。现有 X 客户端没有 following 列表工具，复刻不了 Discord 的关注监控。"
    "因此 yums 这类号（0 帖、资料网站为空、bio 不含网址也不含当轮 query、也没人发过该 @）"
    "在 Discord 挂掉时仍然发现不了，直到名字/bio 撞上轮换 query，或第三方帖子点名该 @"
)

PRODUCT_RE = re.compile(
    r"(fair\s*launch|launchpad|bonding(?:\s*curve)?|testnet|mainnet|whitelist|"
    r"airdrop|ordinals?|crc-?20|\bgpu\b|\bpow\b|\bminer\b|\bmint\b|\bnft\b|"
    r"layerzero|\boft\b|starknet|dogeevm|dogeos|elysium|giwa|tapeout|genesis)",
    re.I,
)
URL_RE = re.compile(
    r"https?://[^\s<>\"']+|(?<![\w.])(?:[a-z0-9-]+\.)+(?:fun|xyz|io|app|com|net|org|lol|world|gg)\b",
    re.I,
)
HANDLE_RE = re.compile(r"^[A-Za-z0-9_]{1,15}$")
MENTION_RE = re.compile(r"@([A-Za-z0-9_]{1,15})")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")
V1_CREATED = "%a %b %d %H:%M:%S %z %Y"

# Social hosts are not a product site. A parked or social-only link does not
# clear the R1623 shell gate.
SOCIAL_HOSTS = {
    "x.com",
    "twitter.com",
    "t.co",
    "t.me",
    "telegram.me",
    "telegram.org",
    "discord.gg",
    "discord.com",
    "youtube.com",
    "youtu.be",
    "medium.com",
}
PARKED_MARKERS = (
    "domain is for sale",
    "buy this domain",
    "this domain is parked",
    "domain parking",
    "godaddy",
    "hugedomains",
    "sedo.com",
    "afternic",
    "dan.com",
    "parkingcrew",
    "parkweb",
)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_created(value) -> datetime | None:
    if not value or not isinstance(value, str):
        return None
    text = value.strip()
    if ISO_RE.match(text):
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError:
            return None
    try:
        return datetime.strptime(text, V1_CREATED)
    except ValueError:
        return None


def host_of(url: str) -> str:
    m = re.match(r"^https?://([^/:?#]+)", url.strip(), re.I)
    if not m:
        return ""
    return m.group(1).lower().rstrip(".").removeprefix("www.")


def is_social_host(host: str) -> bool:
    host = host.lower().removeprefix("www.")
    return any(host == s or host.endswith("." + s) for s in SOCIAL_HOSTS)


def is_public_host(host: str) -> bool:
    if not host or host in {"localhost", "localhost.localdomain"} or host.endswith(".local"):
        return False
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        ip = None
    if ip is not None:
        return not (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast)
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False
    for info in infos:
        addr = info[4][0]
        try:
            ip = ipaddress.ip_address(addr)
        except ValueError:
            return False
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            return False
    return True


def normalize_url(raw: str) -> str:
    text = (raw or "").strip().rstrip(").,]}>\"'")
    if not text:
        return ""
    if text.startswith("//"):
        text = "https:" + text
    if not re.match(r"^https?://", text, re.I):
        if re.match(r"^(?:[a-z0-9-]+\.)+[a-z]{2,}\b", text, re.I):
            text = "https://" + text.split()[0]
        else:
            return ""
    if not text.lower().startswith(("http://", "https://")):
        return ""
    return text


def product_urls(*blobs: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for blob in blobs:
        if not blob:
            continue
        for match in URL_RE.findall(blob):
            url = normalize_url(match if isinstance(match, str) else match[0])
            if not url:
                continue
            host = host_of(url)
            if not host or is_social_host(host):
                continue
            key = url.lower()
            if key in seen:
                continue
            seen.add(key)
            found.append(url)
    return found


def metrics_of(user: dict) -> tuple[int | None, int | None]:
    public = user.get("public_metrics") or user.get("publicMetrics") or {}
    followers = _first_int(
        public.get("followers_count"),
        public.get("followers"),
        user.get("followers_count"),
        user.get("followers"),
    )
    posts = _first_int(
        public.get("tweet_count"),
        public.get("statuses_count"),
        user.get("tweet_count"),
        user.get("statuses_count"),
        user.get("posts"),
    )
    return followers, posts


def _first_int(*values) -> int | None:
    for value in values:
        if isinstance(value, bool) or value is None or value == "":
            continue
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.strip().isdigit():
            return int(value.strip())
    return None


def username_of(user: dict) -> str:
    raw = user.get("username") or user.get("screen_name") or user.get("handle") or ""
    return str(raw).lstrip("@").strip()


def bio_of(user: dict) -> str:
    return str(user.get("description") or user.get("bio") or "").strip()


def profile_website(user: dict) -> str:
    entities = user.get("entities") or {}
    url_entity = entities.get("url") or {}
    urls = url_entity.get("urls") if isinstance(url_entity, dict) else None
    if isinstance(urls, list):
        for item in urls:
            if isinstance(item, dict):
                expanded = item.get("expanded_url") or item.get("expandedUrl") or ""
                url = normalize_url(str(expanded))
                if url and not is_social_host(host_of(url)):
                    return url
    for key in ("url", "website", "profileUrl", "profile_url"):
        url = normalize_url(str(user.get(key) or ""))
        if url and not is_social_host(host_of(url)):
            return url
    return ""


def meaningful_bio(bio: str, urls: list[str]) -> bool:
    if not bio or not PRODUCT_RE.search(bio):
        return False
    if urls:
        return True
    return len(bio.strip()) >= 20


def load_json_arg(path: str | None):
    if not path:
        return None
    text = Path(path).read_text(encoding="utf-8")
    if not text.strip():
        return None
    return json.loads(text)


def as_user_list(payload) -> list[dict]:
    if payload is None:
        return []
    if isinstance(payload, list):
        return [u for u in payload if isinstance(u, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("data", "users", "profiles"):
        value = payload.get(key)
        if isinstance(value, list):
            return [u for u in value if isinstance(u, dict)]
        if isinstance(value, dict) and username_of(value):
            return [value]
    if username_of(payload):
        return [payload]
    return []


def as_tweet_list(payload) -> list[dict]:
    if payload is None:
        return []
    if isinstance(payload, list):
        return [t for t in payload if isinstance(t, dict)]
    if not isinstance(payload, dict):
        return []
    data = payload.get("data")
    if isinstance(data, list):
        return [t for t in data if isinstance(t, dict)]
    if isinstance(data, dict) and (data.get("text") or data.get("full_text")):
        return [data]
    return []


def author_usernames(payload) -> dict[str, str]:
    """Map author id → username from tweet expansions, when present."""
    out: dict[str, str] = {}
    if not isinstance(payload, dict):
        return out
    includes = payload.get("includes") or {}
    users = includes.get("users") if isinstance(includes, dict) else None
    if not isinstance(users, list):
        return out
    for user in users:
        if not isinstance(user, dict):
            continue
        uid = str(user.get("id") or "")
        name = username_of(user)
        if uid and name:
            out[uid] = name
    return out


def mention_handles(tweets: list[dict], authors_by_id: dict[str, str]) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for tweet in tweets:
        author = ""
        if tweet.get("author_id") is not None:
            author = authors_by_id.get(str(tweet.get("author_id")), "")
        author = author or str(tweet.get("author_username") or tweet.get("author") or "").lstrip("@")
        names: list[str] = []
        entities = tweet.get("entities") or {}
        mentions = entities.get("mentions") if isinstance(entities, dict) else None
        if isinstance(mentions, list):
            for item in mentions:
                if isinstance(item, dict) and item.get("username"):
                    names.append(str(item["username"]))
                elif isinstance(item, str):
                    names.append(item)
        text = str(tweet.get("text") or tweet.get("full_text") or "")
        names.extend(MENTION_RE.findall(text))
        for name in names:
            handle = name.lstrip("@")
            key = handle.lower()
            if not HANDLE_RE.match(handle) or key == author.lower() or key in seen:
                continue
            seen.add(key)
            found.append(handle)
    return found


def library_handles(data: dict) -> set[str]:
    found: set[str] = set()
    for card in data.get("candidates") or []:
        if not isinstance(card, dict):
            continue
        for key in ("handle", "twitter"):
            value = card.get(key)
            if value:
                found.add(str(value).lstrip("@").lower())
        links = card.get("links") or {}
        if isinstance(links, dict):
            for key in ("x", "twitter"):
                url = str(links.get(key) or "")
                match = re.search(r"(?:x|twitter)\.com/([^/?#]+)", url, re.I)
                if match:
                    found.add(match.group(1).lower())
    return found


def load_library(path: Path | None) -> set[str]:
    if path is None:
        return set()
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return {str(x).lstrip("@").lower() for x in data}
    if isinstance(data, dict) and "handles" in data and "candidates" not in data:
        return {str(x).lstrip("@").lower() for x in data.get("handles") or []}
    return library_handles(data)


class SiteResult:
    def __init__(self, live: bool, reason: str):
        self.live = live
        self.reason = reason


def _unsafe_redirect(url: str) -> bool:
    host = host_of(url)
    return (not host) or is_social_host(host) or (not is_public_host(host))


class _SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if _unsafe_redirect(newurl):
            raise urllib.error.URLError(f"blocked redirect {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def check_site(url: str, timeout: float = SITE_TIMEOUT) -> SiteResult:
    url = normalize_url(url)
    host = host_of(url)
    if not url or not host or is_social_host(host) or not is_public_host(host):
        return SiteResult(False, "url_rejected")
    opener = urllib.request.build_opener(_SafeRedirect)
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": "early-scout-silent/1.0"},
    )
    try:
        with opener.open(req, timeout=timeout) as resp:
            status = getattr(resp, "status", 0) or 0
            final = resp.geturl()
            if _unsafe_redirect(final):
                return SiteResult(False, "bad_final_host")
            body = resp.read(BODY_LIMIT).decode("utf-8", "replace").lower()
    except Exception as exc:
        return SiteResult(False, f"fetch_failed:{type(exc).__name__}")
    if status != 200:
        return SiteResult(False, f"status_{status}")
    if len(body.strip()) < 80:
        return SiteResult(False, "tiny_body")
    for marker in PARKED_MARKERS:
        if marker in body:
            return SiteResult(False, "parked")
    return SiteResult(True, "live")


def classify_user(
    user: dict,
    *,
    library: set[str],
    site_live: bool | None,
    now: datetime | None = None,
) -> dict:
    """Return a decision dict. kind is review | skip."""
    now = now or now_utc()
    handle = username_of(user)
    if not handle or not HANDLE_RE.match(handle):
        return {"kind": "skip", "handle": handle, "reason": "no_handle"}
    if handle.lower() in library:
        return {"kind": "skip", "handle": "@" + handle, "reason": "already_in_library"}
    if user.get("protected") is True:
        return {"kind": "skip", "handle": "@" + handle, "reason": "protected"}
    followers, posts = metrics_of(user)
    if posts is None:
        return {"kind": "skip", "handle": "@" + handle, "reason": "posts_unknown"}
    if posts > MAX_POSTS:
        return {"kind": "skip", "handle": "@" + handle, "reason": "too_many_posts", "posts": posts}
    created = parse_created(user.get("created_at") or user.get("createdAt"))
    if created is not None:
        age = now - created.astimezone(timezone.utc)
        if age > timedelta(days=NEW_ACCOUNT_DAYS):
            return {"kind": "skip", "handle": "@" + handle, "reason": "not_new", "createdAt": created.isoformat()}
    bio = bio_of(user)
    website = profile_website(user)
    urls = product_urls(website, bio)
    if not urls and not meaningful_bio(bio, urls):
        return {
            "kind": "skip",
            "handle": "@" + handle,
            "reason": "no_product_signal",
            "posts": posts,
            "followers": followers,
        }
    onchain = user.get("onchainConfirmed") is True or user.get("onchain_confirmed") is True
    inflated_shell = posts == 0 and (followers or 0) >= INFLATED_FOLLOWERS and not onchain
    if inflated_shell and site_live is not True:
        return {
            "kind": "skip",
            "handle": "@" + handle,
            "reason": "shell_deferred",
            "posts": posts,
            "followers": followers,
            "detail": "0 posts, inflated followers, live site not confirmed, no on-chain evidence (R1623)",
        }
    packet = {
        "kind": "review",
        "handle": "@" + handle,
        "name": user.get("name") or handle,
        "links": {"x": f"https://x.com/{handle}"},
        "focus": False,
        "posts": posts,
        "followers": followers,
        "createdAt": created.isoformat() if created else None,
        "bio": bio[:280],
        "website": website or (urls[0] if urls else ""),
        "siteLive": site_live,
        "onchainConfirmed": onchain,
        "why": "profile website" if website else "product bio",
    }
    return packet


def decide(
    users: list[dict],
    *,
    library: set[str],
    mention_handles_list: list[str] | None = None,
    carry_deferred: list[str] | None = None,
    check_sites: bool = True,
    site_checker=check_site,
    now: datetime | None = None,
) -> dict:
    """Filter one round of X payloads. Does not admit and does not touch data.json."""
    now = now or now_utc()
    by_handle: dict[str, dict] = {}
    for user in users:
        handle = username_of(user)
        if handle and HANDLE_RE.match(handle):
            by_handle.setdefault(handle.lower(), user)

    queued: list[str] = []
    queued_keys: set[str] = set()
    for raw in (mention_handles_list or []) + (carry_deferred or []):
        handle = raw.lstrip("@")
        key = handle.lower()
        if not HANDLE_RE.match(handle) or key in by_handle or key in queued_keys:
            continue
        if key in library:
            # Seen and skipped. A stub cannot fall through into a shell admit
            # because the library check runs before the shell gate.
            by_handle[key] = {"username": handle}
            continue
        queued.append(handle)
        queued_keys.add(key)

    checks_left = MAX_SITE_CHECKS if check_sites else 0
    site_cache: dict[str, SiteResult] = {}

    def live_for(user: dict) -> bool | None:
        nonlocal checks_left
        followers, posts = metrics_of(user)
        website = profile_website(user)
        urls = product_urls(website, bio_of(user))
        needs = posts == 0 and (followers or 0) >= INFLATED_FOLLOWERS and bool(urls)
        if not needs:
            return None
        if not check_sites or checks_left <= 0:
            return False
        for url in urls[:2]:
            if url not in site_cache:
                if checks_left <= 0:
                    return False
                checks_left -= 1
                site_cache[url] = site_checker(url)
            if site_cache[url].live:
                return True
        return False

    sent: list[dict] = []
    skipped: list[dict] = []
    for user in by_handle.values():
        decision = classify_user(user, library=library, site_live=live_for(user), now=now)
        if decision.get("kind") == "review":
            decision["focus"] = False
            if not (decision.get("links") or {}).get("x"):
                skipped.append({"handle": decision.get("handle"), "reason": "no_twitter"})
                continue
            sent.append({k: v for k, v in decision.items() if k != "kind"})
        else:
            skipped.append({k: v for k, v in decision.items() if k != "kind"})

    deferred: list[str] = []
    for handle in queued:
        if len(deferred) >= MAX_DEFERRED:
            skipped.append({"handle": "@" + handle, "reason": "deferred_overflow"})
            continue
        deferred.append(handle)
        skipped.append({
            "handle": "@" + handle,
            "reason": "profile_unresolved",
            "detail": "third-party @mention; resolve next round inside silentCap, not softCap",
        })

    seen = len(sent) + len(skipped)
    reasons: dict[str, int] = {}
    for row in skipped:
        reasons[row.get("reason") or "?"] = reasons.get(row.get("reason") or "?", 0) + 1
    field = {
        "ran": True,
        "seen": seen,
        "sentToReview": len(sent),
        "admitted": 0,
        "skipped": len(skipped),
        "deferredHandles": deferred,
        "skipReasons": reasons,
        "countRule": "seen = sentToReview + skipped; admitted is a subset of sentToReview and stays 0 until a card with links.x is written",
        "residualGap": RESIDUAL_GAP,
    }
    return {"silentAccounts": field, "sentToReview": sent, "skipped": skipped}


def validate_admit(card: dict) -> list[str]:
    """Ordinary silent admits need links.x and must not set focus."""
    errors = []
    links = card.get("links") or {}
    x = links.get("x") if isinstance(links, dict) else ""
    if not isinstance(x, str) or not re.search(r"(?:x|twitter)\.com/[A-Za-z0-9_]{1,15}", x):
        errors.append("links.x required")
    if card.get("focus") is True or "重点" in (card.get("tags") or []):
        errors.append("ordinary silent admit must not set focus")
    handle = str(card.get("handle") or "").lstrip("@")
    if not handle:
        errors.append("twitter handle required")
    return errors


def read_deferred(round_n: int) -> list[str]:
    """Pull deferredHandles from the last completed round's RESULT, if present."""
    for name in (f"RESULT_R{round_n}.md", f"RESULT_R{round_n}.json", f"ROUND{round_n}_RESULT.json"):
        path = ROOT / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        marker = text.find('"silentAccounts"')
        if marker < 0:
            continue
        start = text.rfind("{", 0, marker)
        if start < 0:
            continue
        try:
            obj, _ = json.JSONDecoder().raw_decode(text[start:])
        except json.JSONDecodeError:
            continue
        field = obj.get("silentAccounts") if isinstance(obj, dict) else None
        if isinstance(field, dict):
            handles = field.get("deferredHandles") or []
            if isinstance(handles, list):
                return [str(h).lstrip("@") for h in handles if HANDLE_RE.match(str(h).lstrip("@"))]
    return []


def build_plan(remaining: int | None, round_n: int | None, deferred: list[str] | None) -> dict:
    rem = x_budget.load_remaining(remaining)
    budget = x_budget.plan(rem)
    scout_round = x_budget.load_round() if round_n is None else int(round_n)
    rotation = x_budget.silent_rotation(scout_round)
    cap = int(budget["silentCap"])
    queued = deferred
    if queued is None:
        queued = read_deferred(scout_round)
    queued = [h.lstrip("@") for h in queued if HANDLE_RE.match(h.lstrip("@"))][:MAX_DEFERRED]
    start = (now_utc() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
    calls: list[dict] = []
    if cap >= 1:
        calls.append({
            "tool": "search_users",
            "query": rotation["userQuery"],
            "lane": rotation["lane"],
            "max_results": 20,
            "paginate": False,
            "user_fields": ["created_at", "description", "entities", "id", "name", "public_metrics", "url", "username", "protected"],
            "note": "one call, first page only; profiles come back on this read",
        })
    if cap >= 2 and queued:
        calls.append({
            "tool": "get_users_by_usernames",
            "usernames": queued,
            "user_fields": ["created_at", "description", "entities", "id", "name", "public_metrics", "url", "username", "protected"],
            "note": "resolve @handles a previous mention search queued; still inside silentCap",
        })
    elif cap >= 2:
        calls.append({
            "tool": "search_posts_all",
            "query": rotation["mentionQuery"],
            "lane": rotation["lane"],
            "start_time": start,
            "max_results": 20,
            "paginate": False,
            "tweet_fields": ["author_id", "created_at", "entities", "text"],
            "expansions": ["author_id"],
            "user_fields": ["created_at", "description", "public_metrics", "url", "username"],
            "note": "third-party @mentions only; do not count this as the lane's thin keyword search",
        })
    ran = cap > 0
    field = {
        "ran": ran,
        "seen": 0,
        "sentToReview": 0,
        "admitted": 0,
        "skipped": 0,
        "reason": None if ran else "silentCap=0",
        "reads": len(calls),
        "deferredHandles": [],
    }
    return {
        "silentCap": cap,
        "silentOutsideSoftCap": True,
        "softCap": budget["softCap"],
        "mode": budget["mode"],
        "remaining": budget["remaining"],
        "round": scout_round,
        "roundBumped": False,
        "rotation": rotation,
        "calls": calls,
        "doNot": [
            "do not count these reads against softCap",
            "do not skip userFollowWatch or any of the six thin-lane keyword searches to pay for them",
            "do not paginate search_users or search_posts_all",
            "do not call a following-list endpoint; this client does not have one, and Discord is not a substitute input",
            "do not admit 0-post inflated shells until a website or other evidence is confirmed",
            "do not set focus:true; do not write a card without links.x",
            "do not bump meta.round and do not rewrite data.json from this command",
        ],
        "residualGap": RESIDUAL_GAP,
        "silentAccountsIfSkipped": field if not ran else None,
        "savePayloadsTo": {
            "users": "/tmp/silent_users.json",
            "mentions": "/tmp/silent_mentions.json",
            "profiles": "/tmp/silent_profiles.json",
        },
        "next": "python3 scripts/silent_accounts.py filter --users /tmp/silent_users.json --mentions /tmp/silent_mentions.json --profiles /tmp/silent_profiles.json",
    }


def result_field(ran: bool, seen: int, sent: int, admitted: int, skipped: int, note: str) -> dict:
    if seen != sent + skipped:
        raise SystemExit(f"seen ({seen}) must equal sentToReview ({sent}) + skipped ({skipped})")
    if admitted < 0 or admitted > sent:
        raise SystemExit(f"admitted ({admitted}) must be between 0 and sentToReview ({sent})")
    if not ran and (seen or sent or admitted or skipped):
        raise SystemExit("ran=false requires all counts to be 0")
    field = {
        "ran": ran,
        "seen": seen,
        "sentToReview": sent,
        "admitted": admitted,
        "skipped": skipped,
        "countRule": "seen = sentToReview + skipped; admitted ⊆ sentToReview; filter skips are not DeepSeek rejects",
    }
    if note:
        field["note"] = note
    if not ran:
        field["reason"] = note or "silentCap=0"
    return {"silentAccounts": field}


def cmd_plan(args: argparse.Namespace) -> int:
    deferred = None
    if args.deferred:
        deferred = [p for p in args.deferred.split(",") if p.strip()]
    payload = build_plan(args.remaining, args.round, deferred)
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


def cmd_filter(args: argparse.Namespace) -> int:
    users = as_user_list(load_json_arg(args.users))
    users.extend(as_user_list(load_json_arg(args.profiles)))
    mention_payload = load_json_arg(args.mentions)
    tweets = as_tweet_list(mention_payload)
    mentions = mention_handles(tweets, author_usernames(mention_payload if isinstance(mention_payload, dict) else {}))
    # Authors expanded on the mention payload are profiles we already paid for
    # inside that one read. Run them through the same gate.
    if isinstance(mention_payload, dict):
        includes = (mention_payload.get("includes") or {}).get("users") or []
        if isinstance(includes, list):
            users.extend(u for u in includes if isinstance(u, dict))
    library_path = Path(args.library) if args.library else ROOT / "data.json"
    library = load_library(library_path)
    carry = [p.strip() for p in (args.carry_deferred or "").split(",") if p.strip()]
    out = decide(
        users,
        library=library,
        mention_handles_list=mentions,
        carry_deferred=carry,
        check_sites=not args.no_check_sites,
    )
    if args.admitted is not None:
        admitted = args.admitted
        sent = out["silentAccounts"]["sentToReview"]
        if admitted < 0 or admitted > sent:
            raise SystemExit(f"admitted ({admitted}) must be between 0 and sentToReview ({sent})")
        out["silentAccounts"]["admitted"] = admitted
    for packet in out["sentToReview"]:
        errors = validate_admit(packet)
        if errors:
            raise SystemExit("review packet failed admit shape: " + "; ".join(errors))
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


def cmd_result(args: argparse.Namespace) -> int:
    field = result_field(
        args.ran,
        args.seen,
        args.sent_to_review,
        args.admitted,
        args.skipped,
        args.note or "",
    )
    json.dump(field, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


def selftest() -> int:
    failures: list[str] = []

    def check(cond: bool, label: str) -> None:
        if not cond:
            failures.append(label)

    for row in x_budget.SILENT_USER_QUERIES:
        check(bool(x_budget.USER_QUERY_RE.match(row["query"])), f"user query charset: {row['query']}")
    lanes = [row["lane"] for row in x_budget.SILENT_USER_QUERIES]
    check(len(lanes) == len(set(lanes)), "silent user queries cover each lane once")
    check(len(x_budget.SILENT_MENTION_QUERIES) == len(lanes), "mention rotation matches user rotation")
    seen_lanes = {x_budget.silent_rotation(i)["lane"] for i in range(len(lanes))}
    check(seen_lanes == set(lanes), "rotation visits every lane")
    check(
        len({x_budget.silent_rotation(i)["lane"] for i in range(len(lanes))}) > 1,
        "rotation is not a single lane",
    )

    # Budget: silent never reduces thin-lane KW, and it is not inside the softCap sum.
    for remaining in (0, 8, 18, 19, 40, 100, 199, 200, 600, 800, 1000):
        out = x_budget.plan(remaining, now=datetime(2026, 11, 11, 22, 0, tzinfo=CST))
        alloc = out["alloc"]
        mode = out["mode"]
        if mode not in ("zero-x", "near-exhausted"):
            check(alloc["kwThin"] == len(x_budget.THIN_LANES), f"kwThin protected at remaining={remaining}")
            check(alloc["uf"] >= 1, f"uf protected at remaining={remaining}")
        main = alloc["uf"] + alloc["mustLe2h"] + alloc["kwThin"] + alloc["kwCore"] + alloc["mentionsThin"] + alloc["mentionsRest"]
        check(main <= out["softCap"], f"main alloc {main} exceeds softCap {out['softCap']} at remaining={remaining}")
        check(out["silentCap"] == alloc["silent"], f"silentCap mirrored remaining={remaining}")
        check(out["silentOutsideSoftCap"] is True, "flag")
        if mode in ("zero-x", "near-exhausted"):
            check(out["silentCap"] == 0, f"no silent reads in {mode}")
        else:
            check(out["silentCap"] <= max(0, remaining - out["softCap"]), f"silent within headroom remaining={remaining}")
            check(out["silentCap"] <= (1 if mode == "tight" else 2), f"silent want cap mode={mode}")

    # Exact headroom cases. 22:00 CST is after the evening reserve, so
    # remaining maps straight onto the documented mode bands.
    evening = datetime(2026, 11, 11, 22, 0, tzinfo=CST)
    check(x_budget.plan(0, now=evening)["silentCap"] == 0, "zero remaining")
    near = x_budget.plan(40, now=evening)  # <50 → near-exhausted, softCap ≤8
    check(near["mode"] == "near-exhausted" and near["silentCap"] == 0, f"near-exhausted drops silent: {near['mode']} {near['silentCap']}")
    tight = x_budget.plan(100, now=evening)
    check(tight["mode"] == "tight" and tight["silentCap"] == 1 and tight["alloc"]["kwThin"] == 6, f"tight silent={tight['silentCap']} mode={tight['mode']}")
    # Mode floors sit below the band's minimum remaining, so a live round
    # always has headroom. The cap function itself still refuses to spend
    # the softCap when the two numbers meet.
    check(x_budget.silent_cap_for("tight", 18, 18) == 0, "no headroom means no silent read")
    check(x_budget.silent_cap_for("tight", 19, 18) == 1, "one read of headroom, tight stays at 1")
    check(x_budget.silent_cap_for("ample", 40, 40) == 0, "ample does not borrow the softCap")
    check(x_budget.silent_cap_for("ample", 42, 40) == 2, "two reads only from headroom")
    check(x_budget.silent_cap_for("near-exhausted", 40, 8) == 0, "near-exhausted helper")
    check(x_budget.silent_cap_for("zero-x", 1000, 0) == 0, "zero-x helper")
    ample = x_budget.plan(800, now=evening)
    check(ample["mode"] == "ample" and ample["silentCap"] == 2 and ample["alloc"]["kwThin"] == 6, "ample keeps 6 thin KW plus 2 silent")

    fixed_now = datetime(2026, 11, 11, 8, 50, tzinfo=timezone.utc)
    library = {"enter_elysium"}

    yums = {
        "username": "yumsdotfun",
        "name": "Yums",
        "description": "creator fees routed by X handle",
        "url": "",
        "created_at": "2026-11-08T00:00:00.000Z",
        "public_metrics": {"followers_count": 708, "tweet_count": 0},
    }
    farm = {
        "username": "farmedshell",
        "name": "Farm",
        "description": "fair launch mint coming soon, join the whitelist",
        "created_at": "2026-11-10T00:00:00.000Z",
        "public_metrics": {"followers_count": 800, "tweet_count": 0},
    }
    quiet = {
        "username": "quietpad",
        "name": "Quiet Pad",
        "description": "gm",
        "url": "https://quietpad.fun",
        "created_at": "2026-11-09T00:00:00.000Z",
        "public_metrics": {"followers_count": 12, "tweet_count": 0},
    }
    old = {
        "username": "oldmint",
        "name": "Old",
        "description": "fair launch mint live https://oldmint.fun",
        "created_at": "Tue Mar 21 20:50:14 +0000 2006",
        "public_metrics": {"followers_count": 10, "tweet_count": 1},
    }
    loud = {
        "username": "loudpad",
        "name": "Loud",
        "description": "launchpad https://loudpad.fun",
        "created_at": "2026-11-01T00:00:00.000Z",
        "public_metrics": {"followers_count": 10, "tweet_count": 40},
    }

    def run(users, mentions=None, checker=None, carry=None):
        return decide(
            users,
            library=library,
            mention_handles_list=mentions or [],
            carry_deferred=carry,
            check_sites=checker is not None,
            site_checker=checker or (lambda url: SiteResult(False, "unchecked")),
            now=fixed_now,
        )

    yums_out = run([yums])
    check(yums_out["silentAccounts"]["sentToReview"] == 0, "yums 07:35 not sent")
    check(yums_out["skipped"][0]["reason"] == "no_product_signal", "yums without url/product bio is no_product_signal")
    check(yums_out["silentAccounts"]["admitted"] == 0, "filter does not admit")

    def dead(_url: str) -> SiteResult:
        return SiteResult(False, "parked")

    def live(url: str) -> SiteResult:
        return SiteResult(True, "live")

    farm_out = run([farm], checker=dead)
    check(farm_out["skipped"][0]["reason"] == "shell_deferred", "inflated 0-post slogan stays deferred")
    check(farm_out["silentAccounts"]["sentToReview"] == 0, "shell not reviewed")

    farm_live = dict(farm)
    farm_live["url"] = "https://farmed.fun"
    farm_ok = run([farm_live], checker=live)
    check(len(farm_ok["sentToReview"]) == 1, "confirmed live site clears the shell gate into review")
    packet = farm_ok["sentToReview"][0]
    check(packet["focus"] is False, "review packet focus false")
    check(packet["links"]["x"] == "https://x.com/farmedshell", "review packet links.x")
    check(validate_admit(packet) == [], "packet passes admit shape")
    check(farm_ok["silentAccounts"]["admitted"] == 0, "live site is review, not an admit")

    quiet_out = run([quiet])
    check(quiet_out["sentToReview"][0]["handle"] == "@quietpad", "low-follower profile website goes to review")
    check(quiet_out["sentToReview"][0]["focus"] is False, "quiet focus false")

    check(run([old])["skipped"][0]["reason"] == "not_new", "old account skipped")
    check(run([loud])["skipped"][0]["reason"] == "too_many_posts", "talkative account is not this path")
    known = {
        "username": "Enter_Elysium",
        "description": "launchpad https://elysium.example",
        "created_at": "2026-11-01T00:00:00.000Z",
        "public_metrics": {"followers_count": 10, "tweet_count": 1},
    }
    check(run([known])["skipped"][0]["reason"] == "already_in_library", "library skip")

    onchain = dict(farm)
    onchain["onchainConfirmed"] = True
    check(run([onchain], checker=dead)["silentAccounts"]["sentToReview"] == 1, "confirmed on-chain evidence can reach review")

    mentions_out = run(
        [],
        mentions=["yumsdotfun", "quietpad", "Enter_Elysium"],
    )
    # yumsdotfun and quietpad have no profile → deferred; Enter_Elysium is in the library.
    reasons = {row["reason"] for row in mentions_out["skipped"]}
    check("profile_unresolved" in reasons, "unprofiled mention is deferred not admitted")
    check("already_in_library" in reasons, "mentioned library handle skipped")
    check(mentions_out["silentAccounts"]["deferredHandles"] == ["yumsdotfun", "quietpad"], "deferred queue")
    check(mentions_out["silentAccounts"]["seen"] == mentions_out["silentAccounts"]["sentToReview"] + mentions_out["silentAccounts"]["skipped"], "count partition")

    tweet_payload = {
        "data": [{
            "text": "site is up follow @yumsdotfun",
            "author_id": "9",
            "entities": {"mentions": [{"username": "yumsdotfun"}]},
        }],
        "includes": {"users": [{
            "id": "9",
            "username": "someoneelse",
            "description": "launchpad https://someone.fun",
            "created_at": "2026-11-10T00:00:00.000Z",
            "public_metrics": {"followers_count": 4, "tweet_count": 2},
        }]},
    }
    extracted = mention_handles(as_tweet_list(tweet_payload), author_usernames(tweet_payload))
    check(extracted == ["yumsdotfun"], "mention extraction skips the author")
    # Author has 2 posts and a product URL → review. Mentioned yums has no profile → deferred.
    mixed = decide(
        tweet_payload["includes"]["users"],
        library=set(),
        mention_handles_list=extracted,
        check_sites=False,
        now=fixed_now,
    )
    handles_sent = [p["handle"] for p in mixed["sentToReview"]]
    check(handles_sent == ["@someoneelse"], f"author reviewed when silent: {handles_sent}")
    check(mixed["silentAccounts"]["deferredHandles"] == ["yumsdotfun"], "yums still needs a profile")

    bad_focus = dict(packet)
    bad_focus["focus"] = True
    check("ordinary silent admit must not set focus" in validate_admit(bad_focus), "focus true rejected")
    missing = dict(packet)
    missing["links"] = {}
    check("links.x required" in validate_admit(missing), "missing links.x rejected")

    # Private hosts are not fetched.
    check(check_site("http://127.0.0.1/mint").live is False, "loopback blocked")
    check(check_site("http://169.254.169.254/latest").live is False, "link-local blocked")
    check(is_social_host("discord.gg") and is_social_host("x.com"), "social hosts")

    try:
        result_field(False, 0, 0, 0, 0, "")
        result_ok = True
    except SystemExit:
        result_ok = False
    check(result_ok, "skipped-path result field")
    try:
        result_field(True, 3, 1, 1, 2, "")
        partition_ok = True
    except SystemExit:
        partition_ok = False
    check(partition_ok, "admitted subset")
    try:
        result_field(True, 3, 1, 2, 2, "")
        admitted_guard = False
    except SystemExit:
        admitted_guard = True
    check(admitted_guard, "admitted cannot exceed review")

    plan = build_plan(800, 1678, [])
    check(plan["roundBumped"] is False, "plan does not bump the round")
    check(plan["silentCap"] == 2, "plan cap")
    check(plan["calls"][0]["tool"] == "search_users", "first call is user search")
    check(plan["calls"][1]["tool"] == "search_posts_all", "second call is mentions when the queue is empty")
    check(plan["calls"][0]["paginate"] is False, "no pagination")
    queued_plan = build_plan(800, 1678, ["yumsdotfun"])
    check(queued_plan["calls"][1]["tool"] == "get_users_by_usernames", "queue spends the second read on profiles")
    check(queued_plan["calls"][1]["usernames"] == ["yumsdotfun"], "queued handle")
    check(len(queued_plan["calls"]) == 2, "queue does not add a third read")
    dry = build_plan(0, 1678, [])
    check(dry["calls"] == [] and dry["silentAccountsIfSkipped"]["ran"] is False, "no calls when the cap is zero")

    if failures:
        for label in failures:
            print("FAIL", label, file=sys.stderr)
        return 1
    print(f"selftest ok ({len(lanes)} lanes, inflated>={INFLATED_FOLLOWERS}, max_posts={MAX_POSTS})")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Silent-account discovery (Discord-independent)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    plan_p = sub.add_parser("plan", help="print this round's silentCap calls")
    plan_p.add_argument("--remaining", type=int, default=None)
    plan_p.add_argument("--round", type=int, default=None)
    plan_p.add_argument("--deferred", default="", help="comma-separated handles queued last round")
    plan_p.set_defaults(func=cmd_plan)

    filt = sub.add_parser("filter", help="gate search_users / mention payloads; does not admit")
    filt.add_argument("--users", help="search_users JSON")
    filt.add_argument("--mentions", help="search_posts_all JSON")
    filt.add_argument("--profiles", help="get_users_by_usernames JSON")
    filt.add_argument("--library", help="data.json or a handle list; default ./data.json")
    filt.add_argument("--carry-deferred", default="", help="handles still waiting on a profile read")
    filt.add_argument("--no-check-sites", action="store_true", help="do not HTTP-check sites; inflated 0-post shells stay deferred")
    filt.add_argument("--admitted", type=int, default=None, help="cards actually written; default 0")
    filt.set_defaults(func=cmd_filter)

    res = sub.add_parser("result", help="print the RESULT silentAccounts object")
    res.add_argument("--ran", required=True, choices=("true", "false"))
    res.add_argument("--seen", type=int, required=True)
    res.add_argument("--sent-to-review", type=int, required=True)
    res.add_argument("--admitted", type=int, required=True)
    res.add_argument("--skipped", type=int, required=True)
    res.add_argument("--note", default="")
    res.set_defaults(func=lambda a: cmd_result(argparse.Namespace(
        ran=a.ran == "true",
        seen=a.seen,
        sent_to_review=a.sent_to_review,
        admitted=a.admitted,
        skipped=a.skipped,
        note=a.note,
    )))

    sub.add_parser("selftest", help="run the local gate and budget checks").set_defaults(
        func=lambda _a: selftest()
    )

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
