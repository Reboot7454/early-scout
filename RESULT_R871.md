# R871 RESULT (full-radar · X exhausted)

- **notify**: false（无新收录；无有效≤2h；R870已告警额度满+$HASP；勿重复刷）
- **at**: 2026-10-29 23:59 CST
- **newIds**: (none — X daily exhausted; Discord Peek deferred)
- **le2h**: 无（keyhasp/blindfloor ≤2h 窗已过期已清）
- **xReads**: 0 (0/1000 remaining; reset 2026-10-30 08:00 CST；probe 确认日额已尽)
- **keywordsTenCols**: false (X blocked)
- **userFollowDone**: false (X blocked)
- **mentions**: **X blocked** — planned equal-effort: Elysium/kinetiq, Tape, GIWA, Zero, DogeEVM, Starknet, BTC/ShieldedNaka, squeek/Nutshell, starx/X Layer, BN Agent, flap/Irys/Full.fun/Arc
- **coverage**: 打新/挖矿/台子/GO/LZ/Elysium/Tape/GIWA/DogeEVM/BN Agent +BTC +Starknet +X Layer/STARX +squeek/Nutshell — 仓内 soft lastChecked；关键词/mentions/UF 待 X reset 08:00 CST 后首轮全量补扫
- **watchBugs**: dual-write links.x↔twitter hygiene ×790（无新「在库不在Watch」漏挂；R870×9 已补挂）
- **discordPeekDeferred**: true（本执行器无 Discord Peek；最新 DISCORD_ALPHA cards 2130 已于 R869 处理；无新 invent admits）
- **dsFallback**: false（无新候选需 DS）
- **soft**: keyhasp/blindfloor ≤2h 清出；soft-debt *Watch lastChecked → 23:59 CST；deferred 全量补扫至 08:00 CST 后首轮
- **skipped**: 全部 X soft-brush / keyword 十栏 / mentions（日额耗尽至 2026-10-30 08:00 CST）
- **push**: (pending)
- **panel**: https://reboot7454.github.io/early-scout/

```json
{
  "round": 871,
  "mode": "full-radar",
  "notify": false,
  "notifyReason": "quiet-x-exhausted-no-le2h",
  "alertMessage": "",
  "newIds": [],
  "newOneLiners": {},
  "le2h": [],
  "xReads": 0,
  "xReadsRemaining": 0,
  "xResetAt": "2026-10-30T00:00:00.000Z",
  "xResetAtCST": "2026-10-30 08:00 CST",
  "keywordsTenCols": false,
  "userFollowDone": false,
  "mentions": [
    "X blocked — planned equal: Elysium/kinetiq",
    "Tape",
    "GIWA",
    "Zero/LayerZero",
    "DogeEVM",
    "Starknet",
    "BTC/ShieldedNaka",
    "squeek/Nutshell",
    "starx/X Layer",
    "BN Agent pads",
    "flap/Irys/Full.fun/Arc"
  ],
  "mentionsCovered": [],
  "mentionsPlanned": [
    "Elysium/kinetiq",
    "Tape",
    "GIWA",
    "Zero",
    "DogeEVM",
    "Starknet",
    "BTC",
    "squeek/Nutshell",
    "starx/X Layer",
    "BN Agent",
    "flap/Irys/Full.fun/Arc"
  ],
  "coverage": {
    "打新": "soft-debt only (X blocked)",
    "挖矿": "soft-debt only (X blocked)",
    "台子/Meme": "soft-debt only (X blocked)",
    "GO盘": "soft-debt only (X blocked)",
    "LayerZero": "soft-debt only (X blocked)",
    "Elysium": "soft-debt only (X blocked)",
    "Tape/电路": "soft-debt only (X blocked)",
    "GIWA": "soft-debt only (X blocked)",
    "DogeEVM": "soft-debt only (X blocked)",
    "BN Agent 钱包": "soft-debt only (X blocked)",
    "BTC": "soft-debt only (X blocked)",
    "Starknet": "soft-debt only (X blocked)",
    "X Layer/STARX": "soft-debt only (X blocked)",
    "squeek/Nutshell": "soft-debt only (X blocked)"
  },
  "watchBugs": [
    "dual-write links.x↔twitter hygiene ×790"
  ],
  "discordPeekDeferred": true,
  "dsFallback": false,
  "soft": [
    "keyhasp ≤2h窗至00:00 CST已清；blindfloor 已过期清",
    "soft-debt *Watch lastChecked refreshed to 2026-10-29 23:59 CST",
    "deferred full rescan UF+ten-col keywords+all-chain mentions after 2026-10-30 08:00 CST"
  ],
  "skipped": [
    "X daily exhausted until 2026-10-30 08:00 CST — no search_posts/get_users/mentions",
    "keywordsTenCols blocked",
    "userFollow soft-brush blocked",
    "mentions all chains blocked",
    "Discord Peek deferred — no browser; latest DISCORD_ALPHA cards 2130 already processed in R869"
  ],
  "pushOk": false,
  "pushSha": "",
  "panel": "https://reboot7454.github.io/early-scout/",
  "at": "2026-10-29 23:59 CST",
  "blockers": [
    "X daily read limit 1000/1000 — reset 2026-10-30 08:00 CST",
    "Discord Peek needs user box / no invent admits"
  ]
}
```
