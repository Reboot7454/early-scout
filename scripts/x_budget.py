#!/usr/bin/env python3
"""Early-scout X day-budget pacing helper (Asia/Shanghai).

Does NOT change hard rules (UF first, no lane-cut when quota OK, zero-X when
exhausted, full scan on first post-reset round). Prints a soft per-round cap
so 1000/day lasts toward next 08:00 CST reset.

As of 2026-11-11 the user required equal-effort coverage (不要偏科):
thin lanes must get dedicated keyword / mentions slots and must not be merged
into high-volume Elysium / BNB / Robinhood queries.

Usage:
  python3 scripts/x_budget.py              # remaining from meta.xQuota or env
  python3 scripts/x_budget.py 1000         # explicit remaining
  X_REMAINING=850 python3 scripts/x_budget.py
"""
from __future__ import annotations
import json, os, sys
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
        "alloc": alloc,
        "thinLanes": THIN_LANES,
        "coreLanes": CORE_LANES,
        "kwThinQueries": KW_THIN,
        "kwCoreQueries": KW_CORE,
        "fatWatches": FAT_WATCHES,
        "thinWatches": THIN_WATCHES,
        "priority": "UF分片→必盯/≤2h（薄栏 Watch 每轮全读，厚表分片且不得与薄栏合并）→薄栏独立KW→核心栏KW→薄栏 mentions→其余 mentions",
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
            "RESULT 必写 xReads/remainingBefore/remaining/mode/softCap/minSpend/ufCursor/laneReads（每薄栏独立 KW 是否跑到）",
        ],
    }


def main() -> None:
    explicit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    out = plan(load_remaining(explicit))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
