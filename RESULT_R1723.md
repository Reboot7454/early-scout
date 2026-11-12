# RESULT R1723

- round: 1723
- completedAt: 2026-11-13 02:11:06 CST
- docsSynced: true
- notify: true
- notifyReason: clover-rh 仍在约 04:00 CST 前的 ≤2h，且本轮官方刚发 LIVE 帖并公布新 CA，必须 notify=true；farm-filch 窗口已过且仍无开铸确认。
- newThisRound: []
- candidates: 4063
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- userOrderedFull: R1715
- panel: https://reboot7454.github.io/early-scout/
- pushSha: ca2b491 (ca2b49103bb4b89437778e2b8c2f32803d4a3180)
- pushPending: false

## 新收录
- 无。meta.newThisRound=[]。candidateCount=4063。

## xQuota
- xReads: 10（主路径 10；静号 0 次，不占 softCap）
- remainingBefore: 105
- remaining: 91
- mode: tight
- softCap: 10
- minSpend: 10
- silentCap: 1
- ufCursor: 290→342（kept 40, skip 12, considered 52）
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 无
- kwCoreDeferred: 打新, 挖矿, 台子/Meme, GO盘, Elysium（tight softCap=10 裁掉，未砍薄栏 KW 或 UF）
- mentionsThin: 无（UF1 + le2h/必盯优先 1 次 + 薄栏 Watch 因 query 长度拆 2 次 + 6 条薄栏 KW=10，mentions 延后；薄栏拆分占用了 mentionsThin 槽）
- mentionsRest: 无
- fatShards: 本轮未推进（nextStart 保持 R1717/R1718：agentPad 276、freeMint 40、bnAgent 103、elysium 61）
- le2hSupplement: false（把 FarmFilch / bloodstockRH / cloverdotfamily 等放进独立优先 from: 查询，无需额外补搜）
- lastFullAfterReset: 仍为 R1692（本轮是 tight，不是 08:00 重置首轮，也不是用户点名全量）
- userOrderedFull: 仍为 R1715
- 注：开跑 footer remainingBefore=105（R1722 收工为 122，间隔内其它任务消耗了额度）。收工 remaining=91。无探索性重试、无翻页。UF skip=12 均为已知 NF_skip，未连刷。

## silentAccounts
- ran: true
- seen: 0
- sentToReview: 0
- admitted: 0
- skipped: 0
- lane: GIWA
- index: 7
- userQuery: GIWA launch
- search_users_unavailable: true
- deferredHandles: []
- 注：silentCap=1，计划仅 search_users（query=GIWA launch，全栏轮换第 7 栏）。该工具不可用，未用 mention 搜索顶替，也未伪造该槽；本路径 0 次 X 读。

## 本轮结论
R1723 例行 tight：0 张新卡。clover-rh 于 01:51:13 / 01:51:42 CST 发官方 LIVE 帖，宣布 Clover + $CLV/Token 已在 Robinhood Chain 上线，官帖 CA 为 0x500908d166d9adfb76ea226e6c1619ab25a6da07；此前卡片 CA 为 0x1ead1942232dae5a296eea527b7feb871941d960，已保留在 links.caPrev。DexScreener 本轮对官帖 CA 返回 0 个交易对，仍只索引到旧地址的 Clover/CLOVER 池（其中一池约显示流动性 3948.53 USD），不能据此断定哪条才是唯一正确代币。窗口至约 04:00 CST，扫描完成于 2026-11-13 02:11:06 CST，仍 ≤2h，status 保持 live。farm-filch 原定 00:00 CST 的 222 免费 mint 至约 02:00 CST 的窗口已过，本轮无官帖、无 mint CA，status 保持 announced，le2h 改为 false。bloodstockrh 本轮无官帖，le2h 保持 false。lil-giraffies / enter-elysium 仅刷 lastChecked 与粉丝。2hourfun 23:52:29 CST 官帖称 “Big update coming today regarding current market conditions.”，无开盘时刻或 CA，不标 le2h。Canton/Glaze/TokenWorks lastChecked 已刷。notify=true。discordPeekDeferred=true。

## 粉丝上调（仅升不降）
lil-giraffies 24490->24493、enter-elysium 47419->47422、globemkts 763->765、shoutoutloudio 3->39、2hourfun 12->32、stillwater-play 0->86、vaubanworks 0->218 共 7 项；下降项一律保持原卡片数字（clover-rh 3994 读数 3755 KEEP 3994、runeclaw 1458 读数 1170 KEEP 1458、gamapad 2438 读数 2219 KEEP 2438、jumak-sanjeok 1245 读数 1181 KEEP 1245、giwahook 37 读数 36 KEEP 37）。

## dsNote
deepseek-flash thinking-on：max_tokens=16000，第一次调用即完整可解析 JSON。admits=[]。clover-rh 官方 LIVE + 新公布 CA，窗口仍 ≤2h；farm-filch 窗口已过未确认开铸。粉丝只上调。search_users 不可用且 silentCap=1，未顶替 mention。本轮 tight 未触发 full，厚表分片未推进。未走 dsFallback。

## alertMessage
🔔 R1723：Clover 官方 LIVE 帖公布 CA 0x500908d166d9adfb76ea226e6c1619ab25a6da07，该地址与卡片旧 CA 0x1ead1942232dae5a296eea527b7feb871941d960 不一致，DexScreener 目前只索引到旧地址的池。请到面板 https://reboot7454.github.io/early-scout/ 与官方帖核对，不要把未核验的新地址或旧地址当成唯一确定交易标的。farm-filch 窗口已过且仍无官方开铸确认。
