# RESULT R1730

时间：2026-11-13 03:54 CST（Asia/Shanghai）
仓库：Reboot7454/early-scout
面板：https://reboot7454.github.io/early-scout/
notify=true
discordPeekDeferred=true（本机未登录 Discord，Peek 跳过）

## 新收录（0）
本轮无新卡。

## skip
- LayerZero 关键词：几乎全是 Flare DVN/OFT 转发，不建卡。
- Tape/电路 关键词与 mentions：已在库 TapeOut/Blonskr 讨论，不标新卡。
- GIWA 关键词与 mentions：已在库 Ammora waitlist、GIWA 测试网互动，以及已在库 soom 同一条 02:54 CST testnet 帖，不建卡。
- DogeEVM：已在库 DogeOS/黑客松转发。
- BTC：已在库 ShieldedNaka 二级市场（OrdDropz）。
- Starknet：几乎全是动物/游戏 “Bramble” 误伤；一条 Variational/Extended 活动提及，不是新打新项目。
- UF 分片其余 24 个号本窗无帖。TradeOnRealm 01:51 CST 官帖讲启动前税率参数，已在库，非新 mint 窗。

## 更新
- hood-terminals：付费公售仍 LIVE 且 ≤2h（02:53 CST 开窗，至约 04:53 CST）。修正 R1729「03:17–03:18 仅互动、无新规则」：03:17:15 CST 与 03:34:47 CST 官帖明确将每钱包上限由 2 改为 20，并称公售提前开放、under 300 left。OpenSea total_supply 487→493/777（约余 284）；官价 0.0015 ETH，floor 0.00137899 ETH；官帖短链 301 到合集页。CA 0x1d742553740e23d1f3e2db98dd3f1d88a7280c92 来自 OS 索引（robinhood），未独立审计。官网本轮未重抓。粉丝 KEEP 1613（API 1612）。
- clover-rh：仍 ≤2h，窗口至约 04:00 CST（扫描时刻 03:52 CST，可能是窗前最后一轮提醒）。must 查询最新 20 条全是 hoodicorns（最早 01:58:53 CST），故 01:58 CST 后 clover / hoodgremlinrh / squeekchain 无新官帖；01:51 后仍无 clover 新官帖。官帖 CA 0x500908d166d9adfb76ea226e6c1619ab25a6da07 与旧 CA 0x1ead1942232dae5a296eea527b7feb871941d960 仍不一致；DexScreener 新 CA 0 池，旧 CA 最大 robinhood uniswap 池流动性仍约 3938.36 USD（另一池 3.55 USD）。粉丝 KEEP 3994。
- soom：再次看到同一条 02:54 CST testnet 帖，R1727 已写入，仅刷 lastChecked，粉仍 2。
- Canton/Glaze/TokenWorks：soft-touch lastChecked，无新 admit。

## 监控 / Watch
无新卡，无需新进 Watch。厚表分片因 tight 延后，nextStarts 保持 agentPad 376 / freeMint 140 / bnAgent 203 / elysium 161。薄栏 Watch 本轮延后。UF 下一轮从 667 续。

## xQuota
- xReads: 10（主路径 10；静号 0 次）
- remainingBefore: 66（官方 footer，开跑先核；不以 R1729 所写收工 890 为准）
- remaining: 56
- mode: tight
- softCap: 10
- minSpend: 10（已满足，实耗 10）
- silentCap: 1
- ufCursor: 632→667（kept 25：tight alloc.uf=1，单次 from: 装不下 ufAccountShard=40；skip 10 个已知坏号不重读；下一轮从 667 续）
- tenLanes: no（薄栏 6 条独立 KW 全跑；核心栏 KW 因 tight 延后）
- kwCoreRan: 无
- kwCoreDeferred: 打新, 挖矿, 台子/Meme, GO盘, Elysium
- mentionsThin: Tape/电路, GIWA
- mentionsRest: 无
- mentionsThinDeferred: LayerZero, DogeEVM, BTC, Starknet
- fatShardsDeferred: true（cursor 保持 R1729：agentPad 376 / freeMint 140 / bnAgent 203 / elysium 161）
- thinWatchesDeferred: true
- userFollow 软刷完成（本轮片，1 次查询）
- search_users_unavailable: true（未伪造用户搜索）
- 无探索性重试、无翻页、无同号重读（must 1 次合并查询；因最新 20 条全是 hoodicorns 且最早已到 01:58 CST，可判定其后 clover/gremlin/squeek 无新帖，未再补读）
- lastFullAfterReset: 仍为 R1692
- userOrderedFull: 仍为 R1715

## silentAccounts
- ran: false
- lane: GO盘（R1730 index 3，userQuery "GO launch"）
- search_users_unavailable: true；silentCap=1 无第二槽 mentions/profiles，故本路径未打 X
- seen: 0
- sentToReview: 0
- admitted: 0
- skipped: 0

## 本轮结论
R1730 tight。无新收录。Hood Terminals 付费公售仍 LIVE（≤2h），官帖将每钱包上限由 2 改为 20；OS 493/777，约余 284。clover-rh 窗口仍至约 04:00 CST，须提醒 CA 不一致与 Dex 只索引旧池。candidateCount 4071 不变。新卡规则遵守（本轮无新卡）。未自动 mint。docs/data.json 已同步并推送。

## dsNote
deepseek-flash thinking-on，max_tokens=16000，第一次调用即完整可解析 JSON，未走 dsFallback。admits=[]。alert 使用已核验的 20/钱包、OS 493/777、floor 0.00137899 ETH 与 Clover 旧池 3938.36 USD，未改分数、未新增事实。

## alertMessage
🔔 R1730：hood-terminals 付费公售仍 LIVE（02:53 CST 开窗，至约 04:53 CST，仍 ≤2h），官帖确认每钱包上限由 2 改为 20/钱包；OS 493/777（约余 284），官价 0.0015 ETH，floor 0.00137899 ETH；CA 0x1d742553740e23d1f3e2db98dd3f1d88a7280c92 来自 OS contracts（chain: robinhood），未独立审计。clover-rh 窗口至约 04:00 CST，扫描时仍 ≤2h；官帖 CA 与旧 CA 不一致，新 CA pairs=0，旧 CA 最大 robinhood uniswap 池流动性 3938.36 USD。面板：https://reboot7454.github.io/early-scout/

## 推送
pushSha=（待 git push 后回填）
