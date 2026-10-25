# RESULT — 用户点名补盯 @bitcointapes

- **time**: 2026-10-25 12:38 CST
- **type**: user-named补盯（卡已在库，非新 admit）
- **notify**: false（父代理自行回用户；本子代理不发消息）
- **newIds**: []
- **alreadyInRadar**: true → `bitcointapes`（R486）
- **le2h**: []（FREE MINT「即将开放」，无精确开窗）
- **xReads**: 2（get_users_by_username + get_users_posts）
- **dsFallback**: false
- **discordPeekDeferred**: true（本补盯未 Peek）
- **blocker**: none

## 结论
- 官号存在：显示名 **BTape**，≈118粉，bio「Programmable TapeOut Circuits on Bitcoin | FREE MINT | Native UTXO Machines」，地点 BTC；无站外 URL；建号 2026-02-08。
- 近帖（2026-10-24）：主网免费公平铸造即将开放；可执行电路图写进 Ordinals（UCO/@BruceBlue，感谢 @Blonskr / TapeOut）。
- **已收录**：R486 `bitcointapes`（打新·Bitcoin·TapeOut 电路 FREE MINT；tags 已进 Tape/电路栏）。
- **为何仍像“没盯”**：卡在库，但 `tapeWatch`/`tapeOutWatch.accounts` 未含 `@bitcointapes`，例行不会专刷该号。

## 动作
- 不重 admit、不标 `focus:true`
- 软刷卡：粉 26→118；ecosystem→Tape；signal 更新为 FREE MINT soon 帖
- `meta.tapeWatch.accounts` += `@bitcointapes`；`candidateIds` += `bitcointapes`
- `meta.tapeOutWatch.accounts` += `@bitcointapes`；`candidateIds` += `bitcointapes`
- HANDOFF 追加补盯说明

## 建议例行关键词（父代理 UpdateRoutine）
- `@bitcointapes` / `bitcointapes` / `BTape` / `Bitcoin Tapes` / `UCO` / `Ordinals circuit` / `TapeOut Bitcoin`
