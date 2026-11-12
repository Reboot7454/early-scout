# RESULT R1721

- round: 1721
- completedAt: 2026-11-13 01:13:46 CST
- docsSynced: true
- notify: true
- notifyReason: 无新收录；farm-filch 与 clover-rh 仍在 ≤2h，bloodstockrh 窗口已关，且 lil-giraffies 新公布 23:00 CST mint。
- newThisRound: []
- candidates: 4063
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- userOrderedFull: R1715
- panel: https://reboot7454.github.io/early-scout/
- pushSha: 9863bb5 (9863bb587b3f1d3637ff973dea40f6d8b95319bd)
- pushPending: false

## 新收录
- 无。meta.newThisRound=[]。candidateCount=4063。

## xQuota
- xReads: 10（主路径 10；静号 0 次，不占 softCap）
- remainingBefore: 142
- remaining: 132
- mode: tight
- softCap: 10
- minSpend: 10
- silentCap: 1
- ufCursor: 208→248（kept 40, skip 0, considered 40）
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 无
- kwCoreDeferred: 打新, 挖矿, 台子/Meme, GO盘, Elysium（tight softCap=10 裁掉，未砍薄栏 KW 或 UF）
- mentionsThin: 无（UF1 + le2h/必盯优先 1 次 + 薄栏 Watch 因 query 长度拆 2 次 + 6 条薄栏 KW=10，mentions 延后）
- mentionsRest: 无
- fatShards: 本轮未推进（nextStart 保持 R1717/R1718：agentPad 276、freeMint 40、bnAgent 103、elysium 61）
- le2hSupplement: false（把 FarmFilch / bloodstockRH / cloverdotfamily 等放进独立优先 from: 查询，未被高产号挤掉，无需额外补搜）
- lastFullAfterReset: 仍为 R1692（本轮是 tight，不是 08:00 重置首轮，也不是用户点名全量）
- userOrderedFull: 仍为 R1715
- 注：开跑 footer remainingBefore=142（与 R1720 收工一致）。收工 remaining=132。无探索性重试、无翻页。

## silentAccounts
- ran: true
- seen: 0
- sentToReview: 0
- admitted: 0
- skipped: 0
- lane: Elysium
- index: 5
- userQuery: Elysium mint
- search_users_unavailable: true
- deferredHandles: []
- 注：silentCap=1，计划仅 search_users。该工具不可用，未用 mention 搜索顶替，也未伪造该槽；本路径 0 次 X 读。

## 本轮结论
R1721 例行 tight：0 张新卡。@giraffies_nft 于 00:52:20 CST 官宣 mint 为 2026-11-13 23:00 CST（13 Nov 3PM UTC），并称 OpenSea 已验证、Checker 数小时后上线；距开铸约 22 小时，le2h=false，代币 CA 仍 0x20b25DA8785990CC89330AF56310024Bb199CD36。farm-filch 00:00 CST 222 免费 mint 已过点，官方仍未确认开铸、无 mint CA，status 保持 announced，窗口至约 02:00 CST，仍 ≤2h。clover-rh 代币+平台 02:00 CST 仍在 ≤2h（窗口至约 04:00 CST），本轮无新官帖，CA 仍 0x1ead1942232dae5a296eea527b7feb871941d960。bloodstockrh $SIRE 窗口至约 01:00 CST 已关，le2h 转 false，代币 CA 仍未独立核出。enter-elysium 00:53 CST 官宣 Rabby 已上线 Elysium，属基础设施更新，非新 mint。trippi 23:12 CST 称 Robinhood 免费 mint「almost there」，仍无精确时刻与 CA。Canton/Glaze/TokenWorks lastChecked 已刷。notify=true。discordPeekDeferred=true。

## 粉丝上调（仅升不降）
lil-giraffies 24468->24478、enter-elysium 47409->47410、trippi 4811->5020、toll-xyz 131->133、shielded-wizards 690->691、packswap 66->68 共 6 项；下降 6 项一律保持原卡片数字（dualforge-bsc 93->89 KEEP 93、danta 66->65 KEEP 66、gamapad 2438->2224 KEEP 2438、jumak-sanjeok 1245->1181 KEEP 1245、runeclaw 1458->1170 KEEP 1458、giwahook 37->36 KEEP 37）。

## dsNote
deepseek-flash thinking-on：max_tokens=16000，第一次调用即完整可解析 JSON。admits=[]。lil-giraffies 新公布 23:00 CST mint；farm-filch/clover-rh 续 ≤2h；bloodstockrh 窗口关闭；enter-elysium Rabby 基础设施更新。粉丝只上调。search_users 不可用且 silentCap=1，未顶替 mention。本轮 tight 未触发 full，厚表分片未推进。未走 dsFallback。

## alertMessage
🔔 R1721：lil-giraffies 新公布 23:00 CST mint；farm-filch、clover-rh 仍约 ≤2h；bloodstockrh 窗口已过。面板 https://reboot7454.github.io/early-scout/ 请核对官方 CA。
