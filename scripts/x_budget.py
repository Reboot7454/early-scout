#!/usr/bin/env python3
"""Early-scout X day-budget pacing helper (Asia/Shanghai).

Does NOT change hard rules (UF first, no lane-cut when quota OK, zero-X when
exhausted, full scan on first post-reset round). Prints a soft per-round cap
so 1000/day lasts toward next 08:00 CST reset.

As of 2026-11-11 the user required equal-effort coverage (不要偏科):
thin lanes must get dedicated keyword / mentions slots and must not be merged
into high-volume Elysium / BNB / Robinhood queries.

Silent-account discovery (search_users + one third-party mention or profile
batch) is alloc.silent / silentCap. It sits outside softCap and is dropped
before userFollowWatch or the six thin-lane keyword searches are cut.
The call list for that path is scripts/silent_accounts.py plan.

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

# Owned silent-account discovery. One lane per round, rotating through the
# full list so this 1-read slot cannot stick on Elysium / BNB / Robinhood.
# search_users queries are plain words: GET /2/users/search rejects operators
# and anything outside [A-Za-z0-9_' ]{1,50}. These are NOT the thin-lane
# keyword searches and must not replace them.
SILENT_USER_QUERIES = [
    {"lane": "打新", "query": "fair mint"},
    {"lane": "挖矿", "query": "GPU mine"},
    {"lane": "台子/Meme", "query": "launchpad"},
    {"lane": "GO盘", "query": "GO launch"},
    {"lane": "LayerZero", "query": "LayerZero OFT"},
    {"lane": "Elysium", "query": "Elysium mint"},
    {"lane": "Tape/电路", "query": "TapeOut"},
    {"lane": "GIWA", "query": "GIWA launch"},
    {"lane": "DogeEVM", "query": "DogeEVM"},
    {"lane": "BTC", "query": "Ordinals mint"},
    {"lane": "Starknet", "query": "Starknet mint"},
]

# Default second silent read: third-party tweets that @mention someone.
# has:mentions is the signal. This does not find a 0-post author, and it is
# not a thin-lane keyword search. scripts/silent_accounts.py plan swaps this
# for one get_users_by_usernames batch when the previous round queued handles.
SILENT_MENTION_QUERIES = [
    {"lane": "打新", "query": 'has:mentions has:links ("fair mint" OR "free mint" OR whitelist) -is:retweet'},
    {"lane": "挖矿", "query": 'has:mentions ("GPU mine" OR "NFT miner" OR "PoW mine") -is:retweet'},
    {"lane": "台子/Meme", "query": 'has:mentions (launchpad OR "bonding curve") -is:retweet'},
    {"lane": "GO盘", "query": 'has:mentions ("GO launch" OR "AR launch") -is:retweet'},
    {"lane": "LayerZero", "query": "has:mentions (LayerZero OR OFT) (mint OR launch OR launchpad) -is:retweet"},
    {"lane": "Elysium", "query": "has:mentions (Elysium OR Enter_Elysium) (mint OR launch) -is:retweet"},
    {"lane": "Tape/电路", "query": "has:mentions (TapeOut OR TapeAI OR bitcointapes) -is:retweet"},
    {"lane": "GIWA", "query": "has:mentions (GIWA OR GIWA_by_Upbit) (mint OR launch) -is:retweet"},
    {"lane": "DogeEVM", "query": "has:mentions (DogeEVM OR DogeOS) (mint OR launch) -is:retweet"},
    {"lane": "BTC", "query": "has:mentions (Ordinals OR CRC20 OR ShieldedNaka) (mint OR launch) -is:retweet"},
    {"lane": "Starknet", "query": "has:mentions (Starknet OR Bramble) (mint OR launchpad) -is:retweet"},
]

USER_QUERY_RE = re.compile(r"^[A-Za-z0-9_' ]{1,50}$")


def next_reset(now: datetime) -> datetime:
    local = now.astimezone(CST)
    reset = local.replace(hour=8, minute=0, second=0, microsecond=0)
    if local >= reset:
        reset += timedelta(days=1)
    return reset


def load_round() -> int:
    """Current meta.round. Read-only: this helper never increments it."""
    env = os.environ.get("SCOUT_ROUND")
    if env is not None and env.strip().isdigit():
        return int(env.strip())
    path = os.path.join(os.path.dirname(__file__), "..", "data.json")
    try:
        meta = json.load(open(path, encoding="utf-8")).get("meta", {})
        return max(0, int(meta.get("round") or 0))
    except Exception:
        return 0


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
    return plan


def silent_cap_for(mode: str, remaining: int, soft_cap: int) -> int:
    """Reads for the owned silent-account path. Outside softCap.

    Allowed only when `remaining` still covers this round's softCap, so the
    path cannot shrink userFollowWatch, must/≤2h, or the six thin-lane
    keyword searches. zero-x and near-exhausted record ran=false and spend 0.
    tight gets at most the user-search read; other live modes get that plus
    one mention-search or one profile batch.
    """
    if mode in ("zero-x", "near-exhausted") or soft_cap <= 0 or remaining <= 0:
        return 0
    want = 1 if mode == "tight" else 2
    headroom = remaining - soft_cap
    if headroom <= 0:
        return 0
    return min(want, headroom)


def silent_rotation(round_n: int) -> dict:
    n = len(SILENT_USER_QUERIES)
    i = int(round_n) % n
    user = SILENT_USER_QUERIES[i]
    mention = SILENT_MENTION_QUERIES[i]
    return {
        "round": int(round_n),
        "index": i,
        "lanes": n,
        "lane": user["lane"],
        "userQuery": user["query"],
        "mentionQuery": mention["query"],
        "note": "一条静号 query 轮换全栏；不是薄栏 KW，禁止只停在 Elysium/BNB/RH",
    }


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
    scout_round = load_round()
    silent_cap = silent_cap_for(mode, remaining, soft_cap)
    # Outside the softCap sum on purpose. Do not trim uf / kwThin to fund it.
    alloc["silent"] = silent_cap
    main_keys = ("uf", "mustLe2h", "kwThin", "kwCore", "mentionsThin", "mentionsRest")
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
        "silentCap": silent_cap,
        "silentOutsideSoftCap": True,
        "alloc": alloc,
        "allocMain": sum(alloc[k] for k in main_keys),
        "thinLanes": THIN_LANES,
        "coreLanes": CORE_LANES,
        "kwThinQueries": KW_THIN,
        "kwCoreQueries": KW_CORE,
        "silentRotation": silent_rotation(scout_round),
        "fatWatches": FAT_WATCHES,
        "thinWatches": THIN_WATCHES,
        "priority": "UF分片→必盯/≤2h（薄栏 Watch 每轮全读，厚表分片且不得与薄栏合并）→薄栏独立KW→静号补漏(silentCap，不占 softCap，不依赖 Discord)→核心栏KW→薄栏 mentions→其余 mentions→Discord Peek",
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
            "静号补漏走 alloc.silent / silentCap，不从 softCap 扣，不靠少跑 userFollowWatch 或六条薄栏 KW 来腾次数；silentCap=0 时本路径 ran=false，禁止改记到主扫上",
            "静号每轮只跑 silentRotation 的一条 search_users（全栏轮换）。第二读才是第三方 @提及或上一轮 deferred handle 的一次批量档案，调用清单以 scripts/silent_accounts.py plan 为准",
            "推文关键词搜不到 0 帖官号。search_users 无 bio:/url: 算子，也不能按帖数或注册时间过滤；url: 只命中帖子里的链接，不是资料栏网站",
            "0 帖且粉丝偏高且站点未确认存活、也无链上/发帖证据：defer，不送审不收录（R1623 @yumsdotfun）",
            "RESULT 必写 xReads/remainingBefore/remaining/mode/softCap/minSpend/ufCursor/laneReads（每薄栏独立 KW 是否跑到）以及 silentAccounts.ran/seen/sentToReview/admitted/skipped",
        ],
    }


def main() -> None:
    explicit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    out = plan(load_remaining(explicit))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
