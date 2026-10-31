#!/usr/bin/env python3
"""Early-scout X day-budget pacing helper (Asia/Shanghai).

Does NOT change hard rules (UF first, no lane-cut when quota OK, zero-X when
exhausted, full scan on first post-reset round). Prints a soft per-round cap
so 1000/day lasts toward next 08:00 CST reset.

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
        "priority": "UF→必盯/≤2h→合并关键词→mentions轮换",
        "rules": [
            "同一 handle 每轮只读 1 次（跨 UF+各 Watch 去重）",
            "禁探索性读：不闲逛、不重复确认、Not Found 不连刷",
            "UF 大表轮转软刷：≤2h/LIVE/点名优先，其余分片轮转，禁止整表全读",
            "额度紧(<200)：mentions 只轮换子集；近耗尽(<50)：只 UF+≤2h",
            "remaining=0→08:00：零 X；重置后仅首轮全量补扫",
            "额度够时仍不得偏科砍栏；softCap 是 pacing 不是砍栏借口",
        ],
    }


def main() -> None:
    explicit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    out = plan(load_remaining(explicit))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
