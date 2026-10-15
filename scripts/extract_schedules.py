#!/usr/bin/env python3
"""One-shot / reusable backfill for schedule + onchain fields on early-scout data.json.
Only fills when evidence exists in whyWatch/background/links. Does not invent exact times.
"""
from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data.json"
TZ = ZoneInfo("Asia/Shanghai")

# Explicit evidence-based backfill map (id -> schedule and/or onchain).
# Only include clear datetimes from text; otherwise tentative + note.
BACKFILL: dict[str, dict] = {
    "afterflow": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-26T11:00:00-04:00",  # AL 11:00 EDT
            "endsAt": None,
            "phases": [
                {"name": "AL", "startsAt": "2026-10-26T11:00:00-04:00", "note": "11:00 EDT"},
                {"name": "Public", "startsAt": "2026-10-26T13:00:00-04:00", "note": "13:00 EDT"},
            ],
            "source": "inferred",
            "note": "免费 mint；AL 11:00 EDT / Public 13:00 EDT；供给约 1 万",
        }
    },
    "motif": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-20T17:00:00Z",
            "endsAt": None,
            "phases": [
                {"name": "First Chair 抽签", "startsAt": "2026-10-17T22:00:00Z", "note": "抽 100 席"},
                {"name": "First Chair", "startsAt": "2026-10-20T17:00:00Z"},
                {"name": "Public", "startsAt": "2026-10-20T19:00:00Z"},
            ],
            "source": "inferred",
            "note": "上限 2048；0.03 ETH；Ensemble 已封",
        }
    },
    "computers-rh": {
        "schedule": {
            "status": "live",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-16T19:00:00Z",  # holders FCFS next
            "endsAt": None,
            "phases": [
                {"name": "GTD", "startsAt": "2026-10-16T00:00:00Z", "note": "已开"},
                {"name": "Holders FCFS", "startsAt": "2026-10-16T19:00:00Z", "note": "约 7PM UTC"},
                {"name": "Public", "startsAt": "2026-10-16T22:00:00Z", "note": "约 10PM UTC · max 2"},
            ],
            "source": "inferred",
            "note": "免费 3333；GTD 已开，公售约今晚 UTC",
        },
        "onchain": {
            "chainId": "robinhood",
            "rpcHint": None,
            "contract": None,
            "standard": "erc721",
            "mintStatus": "open",
            "totalSupply": None,
            "maxSupply": 3333,
            "minted": None,
            "lastCheckedAt": None,
            "explorer": "https://opensea.io/collection/computersrh-nft",
            "note": "OpenSea collection 已开，精确合约待核对",
        },
    },
    "ink-terminal": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-16T10:00:00Z",
            "endsAt": None,
            "phases": [
                {"name": "Public", "startsAt": "2026-10-16T10:00:00Z", "note": "北京 18:00"},
            ],
            "source": "inferred",
            "note": "Ink free public · 供应 2000 · 北京 18:00 开",
        },
        "onchain": {
            "chainId": "ink",
            "rpcHint": None,
            "contract": "0x40aca2e71150a1b7d5212643f247ba25a4fa7fbe",
            "standard": "erc721",
            "mintStatus": "not_open",
            "totalSupply": None,
            "maxSupply": 2000,
            "minted": None,
            "lastCheckedAt": None,
            "explorer": "https://explorer.inkonchain.com/address/0x40aca2e71150a1b7d5212643f247ba25a4fa7fbe",
            "note": "OpenSea collection/inkterminal",
        },
    },
    "mutual-fun": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-22T19:00:00Z",
            "endsAt": None,
            "phases": [
                {"name": "Seat / $TMF mint", "startsAt": "2026-10-22T19:00:00Z", "note": "美东 3PM"},
            ],
            "source": "inferred",
            "note": "Pass 治理已结束；$TMF + Seat",
        }
    },
    "units-xreign": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-16T23:59:00+08:00",
            "endsAt": None,
            "phases": [
                {"name": "名单截止", "startsAt": "2026-10-16T23:59:00+08:00", "note": "约 Oct 16"},
            ],
            "source": "inferred",
            "note": "名单约 Oct 16 截止；正式 mint 时间未锁",
        }
    },
    "esccap": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-16T07:30:00Z",
            "endsAt": None,
            "phases": [
                {"name": "GTD WL 截止", "startsAt": "2026-10-16T07:30:00Z", "note": "字谜/referral"},
            ],
            "source": "inferred",
            "note": "Genesis mint 路线图 Q4；当前盯 WL 截止",
        }
    },
    "ghosts-among-us": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-31T00:00:00+08:00",
            "endsAt": None,
            "phases": [{"name": "Mint", "startsAt": "2026-10-31T00:00:00+08:00", "note": "日期点名，无精确时刻"}],
            "source": "inferred",
            "note": "团队点名 Oct 31 mint；精确时刻未公告",
        },
        "onchain": {
            "chainId": "ethereum",
            "rpcHint": "ethereum-publicnode",
            "contract": None,
            "standard": "erc721",
            "mintStatus": "not_open",
            "totalSupply": None,
            "maxSupply": 444,
            "minted": None,
            "lastCheckedAt": None,
            "explorer": "https://opensea.io/collection/ghosts-among-us",
            "note": "OpenSea 已开合集，合约地址待补",
        },
    },
    "tickertapes": {
        "schedule": {
            "status": "live",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-16T00:01:00Z",
            "endsAt": "2026-10-19T23:59:00Z",
            "phases": [
                {"name": "WL 免费", "startsAt": "2026-10-15T00:00:00Z", "note": "至 10-16 00:01 UTC"},
                {"name": "Public 免费", "startsAt": "2026-10-16T00:01:00Z", "note": "至约 10-19"},
            ],
            "source": "inferred",
            "note": "Signal Worlds 4444；WL→公售免费窗",
        },
        "onchain": {
            "chainId": "robinhood",
            "rpcHint": None,
            "contract": "0xa72d8d054a7b6e1033fcb4b2b8718e7d8166ba86",
            "standard": "erc721",
            "mintStatus": "open",
            "totalSupply": None,
            "maxSupply": 4444,
            "minted": None,
            "lastCheckedAt": None,
            "explorer": "https://opensea.io/collection/tickertapes-signal-worlds",
            "note": "Signal Worlds 合约",
        },
    },
    "glocks-onchain": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-15T22:20:00Z",
            "endsAt": None,
            "phases": [
                {"name": "Team", "startsAt": "2026-10-15T22:20:00Z"},
                {"name": "WL", "startsAt": "2026-10-15T22:30:00Z", "note": "至次日 04:30 UTC · ~0.00003 ETH"},
                {"name": "Public", "startsAt": "2026-10-16T04:30:00Z", "note": "约 WL 结束后"},
            ],
            "source": "inferred",
            "note": "供应 666；窗口今晚起",
        },
        "onchain": {
            "chainId": "robinhood",
            "rpcHint": None,
            "contract": "0x2ecfd6d8443d959f85e76065d7fa9fb35b86772b",
            "standard": "erc721",
            "mintStatus": "unknown",
            "totalSupply": None,
            "maxSupply": 666,
            "minted": None,
            "lastCheckedAt": None,
            "explorer": "https://opensea.io/collection/glocks-onchain",
            "note": "",
        },
    },
    "hoodpoker": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-15T21:00:00Z",
            "endsAt": None,
            "phases": [
                {"name": "Team", "startsAt": "2026-10-15T21:00:00Z"},
                {"name": "CCFF00 / WL / HoodFI", "startsAt": "2026-10-15T21:30:00Z", "note": "分阶段免费"},
                {"name": "Public", "startsAt": "2026-10-16T03:30:00Z", "note": "0.001777 ETH"},
            ],
            "source": "inferred",
            "note": "House Pass 7777；今晚起分阶段",
        },
        "onchain": {
            "chainId": "robinhood",
            "rpcHint": None,
            "contract": "0x8bea43c58da13587fef26bb7344660d6c5909336",
            "standard": "erc721",
            "mintStatus": "unknown",
            "totalSupply": None,
            "maxSupply": 7777,
            "minted": None,
            "lastCheckedAt": None,
            "explorer": "https://opensea.io/collection/hoodpoker",
            "note": "",
        },
    },
    "ethernal-cubs": {
        "schedule": {
            "status": "confirmed",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-29T14:00:00Z",
            "endsAt": None,
            "phases": [
                {"name": "Free mint", "startsAt": "2026-10-29T14:00:00Z", "note": "仅 gas"},
            ],
            "source": "inferred",
            "note": "3333 Orbs；WL/GTD 仍开放",
        }
    },
    "enter-the-anime": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-15T00:00:00+08:00",
            "endsAt": "2026-10-22T23:59:00+08:00",
            "phases": [],
            "source": "inferred",
            "note": "日历窗口约 10/15–10/22；精确开售时刻未锁",
        }
    },
    "orcs-on-ink": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-15T00:00:00+08:00",
            "endsAt": None,
            "phases": [
                {"name": "WL→Public", "startsAt": "2026-10-15T00:00:00+08:00", "note": "约 Oct 15"},
            ],
            "source": "inferred",
            "note": "约 Oct 15 WL→Public；精确时刻未锁",
        }
    },
    "donk": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-11-01T00:00:00+08:00",
            "endsAt": None,
            "phases": [{"name": "Pump.fun 公平发射", "startsAt": "2026-11-01T00:00:00+08:00"}],
            "source": "inferred",
            "note": "自称 2026-11-01 发射；CA 未开、时刻未锁",
        }
    },
    "bakeru": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "Free Mint / NFT / TGE 均为 Solana，日期 TBA",
        }
    },
    "cool-punks": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "FREE MINT on RH；mint 日 TBA",
        }
    },
    "the-squad": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "FCFS 申请开；mint 时间仍 TBA",
        }
    },
    "rorschach-ink": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "mint TBA",
        }
    },
    "unpaid-nft": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "Free Mint. Soon. 时间未官宣",
        }
    },
    "ink-pirates": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "mint 日 TBA",
        }
    },
    "ink-daddy": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "mint 日 TBA；GTD 抽奖中",
        }
    },
    "streamoors": {
        "schedule": {
            "status": "live",
            "timezone": "Asia/Shanghai",
            "startsAt": "2026-10-15T16:05:00Z",
            "endsAt": None,
            "phases": [{"name": "Platform live", "startsAt": "2026-10-15T16:05:00Z"}],
            "source": "inferred",
            "note": "发射台已 live；$STREAM CA 已出",
        }
    },
    "topfloor-fun": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "guest list 已关；mint 合约/时间未官宣",
        }
    },
    "grimveil": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "WL 申请中；mint 日未锁",
        }
    },
    "vaultstreet": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "1000 枚免费 mint 尚未开",
        }
    },
    "cabal": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "WL 0.1 ETH / 公开荷兰拍；精确时间未锁",
        }
    },
    "inkbots": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "GTD 名额开放中；正式 mint 时刻未锁",
        }
    },
    "fomies": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "免费 mint waitlist；链+时间未官宣",
        }
    },
    "farming-season": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "waitlist / Season 1 预热；CA Soon",
        }
    },
    "minehood": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "尚未开 mint",
        }
    },
    "liquid-orion": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "testnet soon；主网 mint 未锁",
        }
    },
    "ink-bubble-cats": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "GTD/FCFS 抽奖中；合约 Coming Soon",
        }
    },
    "ink-sigil": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "FREE GTD 协作窗；正式 mint 未锁",
        }
    },
    "ordfellaz": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "GTD/FCFS WL 抽奖中；mint 前窗口",
        }
    },
    "onchain-tendies": {
        "schedule": {
            "status": "tentative",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "AL 快照完成（约 Oct 13）；mint 时刻未锁",
        }
    },
    "beacon-genesis": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "专属 mint 细节未开",
        }
    },
    "torpor": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "allowlist 申请中；正式 mint 未锁",
        }
    },
    "playonmint": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "Bear mint / WL 信息混杂；时间未锁",
        }
    },
    "embervale": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "白名单可申请；正式 mint 未锁",
        }
    },
    "fungolabs": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "WL 申请中；mint 前才绑钱包",
        }
    },
    "liquid-apes": {
        "schedule": {
            "status": "tba",
            "timezone": "Asia/Shanghai",
            "startsAt": None,
            "endsAt": None,
            "phases": [],
            "source": "inferred",
            "note": "引流 WL；正式 mint 未锁（高域名风险）",
        }
    },
}


def now_meta() -> tuple[str, str]:
    now = datetime.now(TZ)
    return now.strftime("%Y-%m-%d %H:%M CST"), now.isoformat()


def apply_backfill(data: dict) -> dict:
    updated_s, updated_iso = now_meta()
    data = deepcopy(data)
    meta = data.setdefault("meta", {})
    meta["updated"] = updated_s
    meta["lastScout"] = updated_iso
    meta["features"] = ["schedule", "onchain"]
    meta["timezone"] = "Asia/Shanghai"

    n_sched = 0
    n_onchain = 0
    for c in data.get("candidates", []):
        patch = BACKFILL.get(c["id"])
        if not patch:
            continue
        if "schedule" in patch and "schedule" not in c:
            c["schedule"] = deepcopy(patch["schedule"])
            n_sched += 1
        elif "schedule" in patch:
            # refresh with evidence map (idempotent overwrite of schedule block only)
            c["schedule"] = deepcopy(patch["schedule"])
            n_sched += 1
        if "onchain" in patch:
            c["onchain"] = deepcopy(patch["onchain"])
            n_onchain += 1
    return data, n_sched, n_onchain


def main() -> None:
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    data, n_sched, n_onchain = apply_backfill(raw)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "scheduleFilled": n_sched, "onchainFilled": n_onchain, "updated": data["meta"]["updated"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
