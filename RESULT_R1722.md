# RESULT R1722

- round: 1722
- completedAt: 2026-11-13 01:45:00 CST
- docsSynced: true
- notify: true
- notifyReason: 无新收录；farm-filch 与 clover-rh 仍在 ≤2h。
- newThisRound: []
- candidates: 4063
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- userOrderedFull: R1715
- panel: https://reboot7454.github.io/early-scout/
- pushSha: 8b07f24 (8b07f24e25b68dfefbfdbf3ac4ce9caf8cd646e3)
- pushPending: false

## 新收录
- 无。meta.newThisRound=[]。candidateCount=4063。

## xQuota
- xReads: 10（主路径 10；静号 0 次，不占 softCap）
- remainingBefore: 132
- remaining: 122
- mode: tight
- softCap: 10
- minSpend: 10
- silentCap: 1
- ufCursor: 248→290（kept 40, skip 2, considered 42）
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 无
- kwCoreDeferred: 打新, 挖矿, 台子/Meme, GO盘, Elysium（tight softCap=10 裁掉，未砍薄栏 KW 或 UF）
- mentionsThin: 无（UF1 + le2h/必盯优先 1 次 + 薄栏 Watch 因 query 长度拆 2 次 + 6 条薄栏 KW=10，mentions 延后）
- mentionsRest: 无
- fatShards: 本轮未推进（nextStart 保持 R1717/R1718：agentPad 276、freeMint 40、bnAgent 103、elysium 61）
- le2hSupplement: false（把 FarmFilch / bloodstockRH / cloverdotfamily 等放进独立优先 from: 查询，未被高产号挤掉，无需额外补搜）
- lastFullAfterReset: 仍为 R1692（本轮是 tight，不是 08:00 重置首轮，也不是用户点名全量）
- userOrderedFull: 仍为 R1715
- 注：开跑 footer remainingBefore=132（与 R1721 收工一致）。收工 remaining=122。无探索性重试、无翻页。UF skip=2 为 NF_skip（huntfieldrh、ciowworld），未连刷。

## silentAccounts
- ran: true
- seen: 0
- sentToReview: 0
- admitted: 0
- skipped: 0
- lane: Tape/电路
- index: 6
- userQuery: TapeOut
- search_users_unavailable: true
- deferredHandles: []
- 注：silentCap=1，计划仅 search_users（query=TapeOut，全栏轮换第 6 栏）。该工具不可用，未用 mention 搜索顶替，也未伪造该槽；本路径 0 次 X 读。

## 本轮结论
R1722 例行 tight：0 张新卡。farm-filch 本轮无官帖，原定 00:00 CST 的 222 免费 mint 仍未获官方开铸确认、无 mint CA，status 保持 announced，窗口至约 02:00 CST，扫描完成于 01:45:00 CST，仍 ≤2h。clover-rh 代币+平台 02:00 CST 仍在 ≤2h（窗口至约 04:00 CST），本轮无新官帖，CA 仍 0x1ead1942232dae5a296eea527b7feb871941d960。bloodstockrh 窗口已在 R1721 关闭，本轮无官帖，le2h 保持 false。lil-giraffies 23:00 CST mint 为 R1721 已记录，本轮只刷 lastChecked 与粉丝（24478→24490），距开铸约 21 小时，le2h=false，CA 仍 0x20b25DA8785990CC89330AF56310024Bb199CD36。enter-elysium Rabby/Crossmint 基础设施更新已在 R1721 记录，粉 47410→47419。Canton/Glaze/TokenWorks lastChecked 已刷。notify=true。discordPeekDeferred=true。

## 粉丝上调（仅升不降）
lil-giraffies 24478->24490、enter-elysium 47410->47419、globemkts 753->763、giwaup 3925->3927 共 4 项；下降 4 项一律保持原卡片数字（runeclaw 1458->1170 KEEP 1458、gamapad 2438->2230 KEEP 2438、jumak-sanjeok 1245->1181 KEEP 1245、giwahook 37->36 KEEP 37）。

## dsNote
deepseek-flash thinking-on：max_tokens=16000，第一次调用即完整可解析 JSON。admits=[]。farm-filch/clover-rh 续 ≤2h；bloodstockrh 窗口保持已关；lil-giraffies / enter-elysium 仅刷 lastChecked 与粉丝。粉丝只上调。search_users 不可用且 silentCap=1，未顶替 mention。本轮 tight 未触发 full，厚表分片未推进。未走 dsFallback。

## alertMessage
🔔 R1722：farm-filch 仍在约 02:00 CST 前、clover-rh 仍在约 04:00 CST 窗口（≤2h）；请到面板 https://reboot7454.github.io/early-scout/ 核对官方 CA，未确认开铸/开盘不编造。
