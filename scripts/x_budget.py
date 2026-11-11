#!/usr/bin/env python3
"""Early-scout X day-budget pacing helper (Asia/Shanghai).

Does NOT change hard rules (UF first, no lane-cut when quota OK, zero-X when
exhausted, full scan on first post-reset round). Prints a soft per-round cap
so 1000/day lasts toward next 08:00 CST reset.

silentCap is a separate Discord-independent budget for 0-post / few-post
project accounts. It is not part of softCap and is not paid for by cutting
userFollowWatch or the six thin-lane keyword searches.

As of 2026-11-11 the user required equal-effort coverage (不要偏科):
thin lanes must get dedicated keyword / mentions slots and must not be merged
into high-volume Elysium / BNB / Robinhood queries.

Usage:
  python3 scripts/x_budget.py              # remaining from meta.xQuota or env
  python3 scripts/x_budget.py 1000         # explicit remaining
  X_REMAINING=850 python3 scripts/x_budget.py
"""
from __future__ import annotations
import json, os, re, sys
from datetime import datetime, timedelta, timezone

CST = timezone(timedelta(hours=8))
LIMIT = 1000

THIN_LANES = [
    "LayerZero",
    "Tape/电路",
    "GIWA",
    "DogeEVM",
    "BTC",
    "Starknet",
]
CORE_LANES = [
    "打新",
    "挖矿",
    "台子/Meme",
    "GO盘",
    "Elysium",
]

# Dedicated thin-lane searches. Do not fold these into a core/Elysium/BNB/RH query.
KW_THIN = {
    "LayerZero": 'LayerZero OFT OR "LayerZero launch" OR "LayerZero mint" OR "OFT launchpad"',
    "Tape/电路": "TapeOut OR TapeAI OR 电路NFT OR bitcointapes OR BTape OR Blonskr",
    "GIWA": 'GIWA mint OR GIWA launch OR "GIWA fair" OR GIWA_by_Upbit',
    "DogeEVM": 'DogeEVM OR DogeOS OR "Doge EVM" mint OR "DogeOS launch"',
    "BTC": 'Ordinals mint OR CRC20 OR "BTC launchpad" OR ShieldedNaka OR "Bitcoin fair launch"',
    "Starknet": "Starknet mint OR Starknet launchpad OR Starknet fairlaunch OR Bramble",
}

KW_CORE = {
    "打新": "fair mint OR WL mint OR free mint OR GTD mint",
    "挖矿": "GPU PoW mine OR NFT miner OR mint miner",
    "台子/Meme": "launchpad live OR bonding curve OR meme pad",
    "GO盘": "GO盘 OR GO launch OR AR launch",
    "Elysium": "Elysium mint OR Elysium launch OR Enter_Elysium",
}

FAT_WATCHES = [
    "userFollowWatch",
    "agentPadWatch",
    "bnAgentWatch",
    "elysiumWatch",
    "freeMintWatch",
]
THIN_WATCHES = [
    "starknetWatch",
    "layerZeroWatch",
    "btcPrivacyWatch",
    "btcCrc20Watch",
    "dogeEvmWatch",
    "tapeWatch",
    "tapeOutWatch",
    "giwaWatch",
]

# Silent-account fallback (Discord-independent). One lane per call — never OR
# these together and never fold them into a core / Elysium / BNB / RH query.
# `user` is a GET /2/users/search query: official grammar is
# ^[A-Za-z0-9_' ]{1,50}$ and the People index matches display name and handle,
# not bio and not the profile-website field. `url` is a recent-post query
# (search_posts_all / search recent). A 0-post official account is not an
# author of any post; it shows up only when someone else mentions it.
USER_QUERY_RE = re.compile(r"^[A-Za-z0-9_' ]{1,50}$")
SILENT_USER_FIELDS = "created_at,description,entities,name,pinned_tweet_id,public_metrics,url,username"
SILENT_GAP = (
    "推文搜索看不到 0 帖官号本身。GET /2/users/search 只允许字母数字空格"
    "（不能写 url:、bio: 或 yums.fun），索引是显示名和 handle，不是 bio；"
    "返回资料里的 description/url 只能本地筛。url: 最近帖只能碰到别人已经发出的链接或 @。"
    "没人提过、名字又不含本轮轮换词、主页网站还空着的 0 帖号"
    "（@yumsdotfun 在 2026-11-11 07:35 CST 被 Discord 看见时就是这种）X 这边仍然会漏。"
)
SILENT_LANES = [
    {
        "lane": "打新",
        "user": "fair mint",
        "url": '("free mint" OR "fair mint" OR whitelist) (url:xyz OR url:fun OR url:app) -is:retweet',
    },
    {
        "lane": "挖矿",
        "user": "NFT miner",
        "url": '("NFT miner" OR "GPU PoW" OR powminer) (url:xyz OR url:fun OR url:io) -is:retweet',
    },
    {
        "lane": "台子/Meme",
        "user": "launchpad",
        "url": '(launchpad OR "bonding curve") (url:fun OR url:xyz OR url:app) -is:retweet',
    },
    {
        "lane": "GO盘",
        "user": "GO launch",
        "url": '("GO launch" OR GOlaunch) (url:xyz OR url:fun) -is:retweet',
    },
    {
        "lane": "LayerZero",
        "user": "LayerZero",
        "url": '(LayerZero OR "OFT launch") (url:xyz OR url:io) -is:retweet',
    },
    {
        "lane": "Elysium",
        "user": "Elysium",
        "url": 'Elysium (mint OR launch OR testnet) (url:xyz OR url:fun) -is:retweet',
    },
    {
        "lane": "Tape/电路",
        "user": "TapeOut",
        "url": '(TapeOut OR bitcointapes OR Blonskr) (url:xyz OR url:io) -is:retweet',
    },
    {
        "lane": "GIWA",
        "user": "GIWA",
        "url": 'GIWA (mint OR launch) (url:xyz OR url:fun) -is:retweet',
    },
    {
        "lane": "DogeEVM",
        "user": "DogeEVM",
        "url": '(DogeEVM OR DogeOS) (mint OR launch) (url:xyz OR url:fun) -is:retweet',
    },
    {
        "lane": "BTC",
        "user": "Ordinals mint",
        "url": '(Ordinals OR CRC20) (mint OR launch) (url:xyz OR url:io) -is:retweet',
    },
    {
        "lane": "Starknet",
        "user": "Starknet",
        "url": 'Starknet (mint OR launchpad OR fairlaunch) (url:xyz OR url:fun OR url:app) -is:retweet',
    },
]
for _lane in SILENT_LANES:
    if not USER_QUERY_RE.match(_lane["user"]):
        raise RuntimeError(f"silent user query is not GET /2/users/search safe: {_lane['lane']}")


def silent_calls(mode: str) -> int:
    """Reads outside softCap. Zero when the day cannot fund UF."""
    if mode in ("zero-x", "near-exhausted"):
        return 0
    if mode in ("ample", "post-reset-full"):
        return 2
    return 1


def select_silent_queries(now: datetime, cap: int) -> list[dict]:
    """Rotate one lane per call. Cap 1 alternates user vs url; cap 2 does both on different lanes."""
    if cap <= 0:
        return []
    local = now.astimezone(CST)
    bucket = (local.hour * 60 + local.minute) // 35
    slot = local.timetuple().tm_yday * 48 + bucket
    n = len(SILENT_LANES)
    picks: list[tuple[str, int]] = []
    if cap == 1:
        kind = "user" if slot % 2 == 0 else "url"
        picks.append((kind, slot % n))
    else:
        picks.append(("user", slot % n))
        picks.append(("url", (slot + n // 2) % n))
    out = []
    for kind, idx in picks[:cap]:
        lane = SILENT_LANES[idx]
        if kind == "user":
            out.append({
                "lane": lane["lane"],
                "kind": "user",
                "query": lane["user"],
                "method": "GET /2/users/search",
                "existingClient": "no existing call searches unknown users; get_users_by_usernames only resolves handles you already have",
                "matches": "display name and handle only. Bio and profile URL are not in the index; filter them locally on the returned user object.",
                "maxResults": 20,
                "params": {
                    "query": lane["user"],
                    "max_results": "20",
                    "user.fields": SILENT_USER_FIELDS,
                },
                "countsAgainst": "silentCap",
                "doNot": "do not paginate, do not merge with another lane, do not charge this call to softCap",
            })
        else:
            out.append({
                "lane": lane["lane"],
                "kind": "url",
                "query": lane["url"],
                "method": "GET /2/tweets/search/recent",
                "existingClient": "search_posts_all / search recent — same post index as keyword search",
                "matches": "posts by other people. A 0-post official is included only via entities.mentions.username. A bare domain with no @handle is unresolved and must not be admitted.",
                "maxResults": 10,
                "params": {
                    "query": lane["url"],
                    "max_results": "10",
                    "tweet.fields": "created_at,entities,author_id",
                    "expansions": "author_id,entities.mentions.username",
                    "user.fields": SILENT_USER_FIELDS,
                },
                "countsAgainst": "silentCap",
                "doNot": "do not paginate, do not OR this into another lane, do not charge this call to softCap",
            })
    return out


def next_reset(now: datetime) -> datetime:
    local = now.astimezone(CST)
    reset = local.replace(hour=8, minute=0, second=0, microsecond=0)
    if local >= reset:
        reset += timedelta(days=1)
    return reset


def load_remaining(explicit: int | None) -> int:
    if explicit is not None:
        return max(0, explicit)
    env = os.environ.get("X_REMAINING")
    if env is not None and env.strip().isdigit():
        return max(0, int(env.strip()))
    path = os.path.join(os.path.dirname(__file__), "..", "data.json")
    try:
        meta = json.load(open(path, encoding="utf-8")).get("meta", {})
        xq = meta.get("xQuota") or {}
        if "remaining" in xq:
            return max(0, int(xq["remaining"]))
    except Exception:
        pass
    return LIMIT


def allocate(mode: str, soft_cap: int) -> dict:
    """API-call budget. Thin-lane KW is reserved first (except zero-x / near-exhausted)."""
    empty = {
        "uf": 0,
        "mustLe2h": 0,
        "kwThin": 0,
        "kwCore": 0,
        "mentionsThin": 0,
        "mentionsRest": 0,
        "minSpend": 0,
        "ufAccountShard": 0,
        "silent": 0,
    }
    if mode == "zero-x":
        return empty
    if mode == "near-exhausted":
        return {
            **empty,
            "uf": min(5, soft_cap),
            "mustLe2h": min(3, max(0, soft_cap - 5)),
            "minSpend": min(soft_cap, 6),
            "ufAccountShard": 24,
        }
    # tight / pace / ample / post-reset-full: always reserve 1 dedicated KW per thin lane
    kw_thin = len(THIN_LANES)  # 6
    if mode == "tight":
        plan = {
            "uf": 2,
            "mustLe2h": 2,
            "kwThin": kw_thin,
            "kwCore": 2,
            "mentionsThin": 2,
            "mentionsRest": 1,
            "minSpend": min(soft_cap, 14),
            "ufAccountShard": 40,
        }
    elif mode == "pace":
        plan = {
            "uf": 2,
            "mustLe2h": 2,
            "kwThin": kw_thin,
            "kwCore": 3,
            "mentionsThin": 3,
            "mentionsRest": 1,
            "minSpend": min(soft_cap, 18),
            "ufAccountShard": 48,
        }
    elif mode == "post-reset-full":
        plan = {
            "uf": 4,
            "mustLe2h": 3,
            "kwThin": kw_thin,
            "kwCore": 4,
            "mentionsThin": 4,
            "mentionsRest": 2,
            "minSpend": min(soft_cap, 24),
            "ufAccountShard": 80,
        }
    else:  # ample
        plan = {
            "uf": 2,
            "mustLe2h": 2,
            "kwThin": kw_thin,
            "kwCore": 4,
            "mentionsThin": 3,
            "mentionsRest": 1,
            "minSpend": min(soft_cap, 20),
            "ufAccountShard": 50,
        }
    used = (
        plan["uf"]
        + plan["mustLe2h"]
        + plan["kwThin"]
        + plan["kwCore"]
        + plan["mentionsThin"]
        + plan["mentionsRest"]
    )
    if used > soft_cap:
        # never cut kwThin first; trim UF/core mentions if the cap is tight
        overflow = used - soft_cap
        for key in ("mentionsRest", "kwCore", "uf", "mustLe2h", "mentionsThin"):
            take = min(overflow, max(0, plan[key] - (1 if key in ("uf", "mustLe2h") else 0)))
            plan[key] -= take
            overflow -= take
            if overflow <= 0:
                break
    plan["minSpend"] = min(soft_cap, max(plan["minSpend"], plan["kwThin"] + plan["uf"] + plan["mustLe2h"]))
    # Outside the softCap trim. Never steal uf / kwThin / mustLe2h to fund this.
    plan["silent"] = silent_calls(mode)
    return plan


def plan(remaining: int, now: datetime | None = None) -> dict:
    now = now or datetime.now(CST)
    reset = next_reset(now)
    hours_left = max(0.05, (reset - now.astimezone(CST)).total_seconds() / 3600)
    # Historical burn: ~1 X-using round every ~25–35m (often every tick).
    rounds_left = max(1, int(hours_left * 60 / 30))
    evening_reserve = 80 if now.astimezone(CST).hour < 20 else 0
    spendable = max(0, remaining - evening_reserve)
    raw_cap = spendable // rounds_left if rounds_left else spendable

    if remaining <= 0:
        mode, soft_cap = "zero-x", 0
    elif remaining < 50:
        mode, soft_cap = "near-exhausted", min(8, remaining)
    elif remaining < 200:
        mode, soft_cap = "tight", min(18, max(10, raw_cap))
    elif remaining < 600:
        mode, soft_cap = "pace", min(28, max(18, raw_cap))
    else:
        mode, soft_cap = "ample", min(40, max(28, raw_cap))

    # First hour after reset: allow one full catch-up round up to 50.
    local = now.astimezone(CST)
    post_reset = local.hour == 8 and local.minute < 25 and remaining >= 950
    if post_reset:
        mode, soft_cap = "post-reset-full", min(50, remaining)

    alloc = allocate(mode, soft_cap)
    # silentCap is extra quota, not a slice of softCap. Shrink it first if this
    # round's remaining cannot cover the lane cap plus the silent calls.
    room = max(0, remaining - soft_cap)
    if alloc["silent"] > room:
        alloc["silent"] = room
    lane_sum = (
        alloc["uf"]
        + alloc["mustLe2h"]
        + alloc["kwThin"]
        + alloc["kwCore"]
        + alloc["mentionsThin"]
        + alloc["mentionsRest"]
    )
    return {
        "remaining": remaining,
        "limit": LIMIT,
        "nowCST": local.strftime("%Y-%m-%d %H:%M CST"),
        "resetAtCST": reset.strftime("%Y-%m-%d %H:%M CST"),
        "hoursLeft": round(hours_left, 2),
        "roundsLeftEst": rounds_left,
        "eveningReserve": evening_reserve,
        "mode": mode,
        "softCap": soft_cap,
        "minSpend": alloc["minSpend"],
        "silentCap": alloc["silent"],
        "silentOutsideSoftCap": True,
        "silentCountsTowardMinSpend": False,
        "laneAllocSum": lane_sum,
        "alloc": alloc,
        "silentLanes": [lane["lane"] for lane in SILENT_LANES],
        "silentQueriesThisRound": select_silent_queries(now, alloc["silent"]),
        "silentGap": SILENT_GAP,
        "thinLanes": THIN_LANES,
        "coreLanes": CORE_LANES,
        "kwThinQueries": KW_THIN,
        "kwCoreQueries": KW_CORE,
        "fatWatches": FAT_WATCHES,
        "thinWatches": THIN_WATCHES,
        "priority": "UF分片→必盯/≤2h（薄栏 Watch 每轮全读，厚表分片且不得与薄栏合并）→薄栏独立KW→核心栏KW→薄栏 mentions→其余 mentions→静默号回退（silentCap，不占 softCap）→Discord Peek 只补漏",
        "rules": [
            "同一 handle 每轮只读 1 次（跨 UF+各 Watch 去重）",
            "禁探索性读：不闲逛、不重复确认、Not Found 不连刷",
            "UF 大表轮转软刷：≤2h/LIVE/点名优先，其余分片轮转，禁止整表全读",
            "禁止把 LayerZero / Tape / GIWA / DogeEVM / BTC / Starknet 的关键词或官号 mentions 并进 Elysium / BNB / Robinhood 的大搜索",
            "除 zero-x 与 near-exhausted 外，六个薄栏每轮各至少 1 次独立关键词搜索",
            "厚 Watch（agentPad/bnAgent/elysium/freeMint/UF）必须分片；薄 Watch 名单短，每轮全读，且不得与厚表并成一次 from:",
            "额度紧(<200) 仍保留薄栏独立 KW；仅近耗尽(<50) 才延后关键词/mentions",
            "remaining=0→08:00：零 X；重置后仅首轮全量补扫",
            "额度够时不得远低于 minSpend 收工；softCap 是 pacing 不是砍栏借口",
            "静默号回退用 alloc.silent / silentCap，不计入 softCap 与 minSpend；禁止从 uf 或六个薄栏 KW 扣额度来付这笔查询",
            "静默查询每次只打一条栏，user 与 url 两路错开轮换；禁止并进 Elysium / BNB / RH，也禁止把六个薄栏 OR 成一条",
            "0帖+高粉+站点未确认活+无链上/发帖证据不得送审（R1623）。脚本不自动收录、不写 data.json",
            "RESULT 必写 xReads/remainingBefore/remaining/mode/softCap/minSpend/ufCursor/laneReads（每薄栏独立 KW 是否跑到）/silentAccount{ran,seen,sentToReview,admitted,skipped}。静默读取计入 xReads 与 remaining，但不是少跑 laneReads 的理由",
        ],
    }


def main() -> None:
    explicit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    out = plan(load_remaining(explicit))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
