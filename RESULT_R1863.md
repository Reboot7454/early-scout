# 早期打新雷达 R1863

- 时间：2026-11-15 18:15 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 ozero；osk-agent 池已开，属新的可操作变化）
- 新收录：ozero（@ozero_fun）
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 9c9ac72 R1862）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 481 → remaining 456（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 481≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。本轮 thin official 与 UF 分片无重叠，必须再开第 5 批 THIN 才能全读薄表（仍全读，未与厚表合并），未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 286 / 1-based 287 oddoneout_fun 起，kept 48，真实 NF_skip 0（不沿用过期 NF 表），walkScanned 48，无绕回。last kept 0-based 333 / 1-based 334 BikeTysonPunk，next 0-based 334 / 1-based 335 mcnuggetsonline。收录后已把 @ozero_fun 追加进 UF。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=LayerZero（1863%11=4）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=56，sentToReview=0，admitted=0，skipped=56（too_many_posts 23 / already_in_library 17 / profile_unresolved 10 / deferred_overflow 5 / no_product_signal 1）。ozero 在主栏 MEN_LZ 发现并收录，不计入静号送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T09:08:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T08:08:00Z（约 2h）。silent start=2026-11-14T10:08:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包（KW_DOGE / KW_ELY / KW_GIWA / KW_MINT / KW_PAD / KW_TAPE / MEN_ELY / SILENT_MEN）被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 12、MUST2 0、THIN1 0、THIN2 3、THIN3 0、THIN4 2、THIN5 0、KW_LZ 3、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 6、KW_SN 7、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 6、KW_ELY 25、MEN_LZ 10、MEN_ELY 25、MEN_MINE 0、MEN_BN 3、SILENT_MEN 25。
- 首读 UF1 快照 480 / 1000，末次 SILENT_MEN 快照 456 / 1000。remainingBefore 取上轮结束 481，按 25 次递减记 remaining=456。
- THIN official 本轮 5 批。thinSkipDedup 无。watchLeaks 0。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 新收录

- **ozero**（@ozero_fun，id=ozero）：本轮 LayerZero mentions 盲捞发现。官号 2026-11-15 17:22 CST 建立（xUserId 2121896074465939456），未认证，0 粉、1 帖、following=6。官网 https://ozero.fun/ HTTP 200，标题写明 the coin launchpad built on Zero Chain，前端 JS 回链 https://x.com/ozero_fun，资料栏回链官网，互链成立。官帖 17:42 CST https://x.com/ozero_fun/status/2121901632447303838 称 coming to @LayerZero_Core，Base Sepolia 测试网 LIVE、任务开放。站点 last-modified 18:03 CST。JS 中有多组测试网地址，未当作已核实主网 CA。DeepSeek-flash（思考开）admit=true，overall 63（early 93 / actionable 45 / novelty 67 / risk 66），category=LayerZero，lzVerified=false，status=testnet，focus=false。已进 userFollowWatch + layerZeroWatch + zeroWatch。非免费主网 mint、非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。

## 在库窗口 / 可操作变化

- **osk-agent**（@AIAgent_OSK）：同一 18:00 CST 开池窗口此前已在 R1859 按首次 ≤2h 推送。本轮核验池已实际打开，属新的可操作变化，再次推送。官帖 18:04 CST https://x.com/AIAgent_OSK/status/2121907257369632893 称 18:00 UTC+8 已过、下一席开 OSK/WBNB 池，每 BSC .ai Agent ID 一席、0.008 BNB，888 免费席已尽。官网 https://oskagent.club/ config.js 给出已部署地址：token `0xF3DE5D50Ff0b21fDAB5f5ee7AcD3Cbf78C2b2e68`，sale `0x5aA04717BF9A86C421caECBaB33d4C2C73C4d156`，pair `0x0C1d8C5ec49A0075921922143e04ADF8240Bc8bB`（PancakeSwap V2），fund `0x1719808f04dd45af6eb099C47842c7F76f887dd4`，treasury `0x68377e18b14faaaa6e11248786f88daa7cdd4ca1`。链上核验：token0=WBNB `0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c`，token1=OSK；getReserves 约 3.60 BNB / 约 11.5365 亿 OSK，储备时间戳 2026-11-15 18:12:18 CST，LP totalSupply 非零；sale.progress() phase=2，seats=1646/3888，paid 约 758，时间戳 18:00:01 CST，开池标志为真；代币 totalSupply 约 15 万亿。DexScreener API 本轮 403，价格按储备估算约 3.12e-9 BNB/OSK（浅池，勿当成交深度；相对总量 FDV 很高）。库内卡此前 status=failed、ca 为空，本轮改为 live 并写入已核验 CA。le2h 现为 false（开池事件已发生）。付费只告警，本号不自动 mint。
- **DualForge**（@DualForgeBSC）：开铸仍 2026-11-15 19:00 CST。本窗官帖 17:51 CST 只讲 Flint/Quench 双钥匙机制，档期未改。https://x.com/DualForgeBSC/status/2121903800797602273 。本轮约 18:15 CST，距开铸约 0.8h，仍在 ≤2h，首次进入已在 R1861 推送，不重推。仅限 Binance Agent ID。未见新 CA。
- **MicroFrens**：对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送）。本窗客服约 17:54 CST 回复 updated, should be good to add more free mints now（https://x.com/MicroFrens/status/2121904597438767580），以及约 18:07 CST 感谢回复。仍是同一持有者/快照免费阶段，不是新的对公窗口或份额规则重开，不重推。
- **hokiseries**：Base Bots 公售仍至 2026-11-15 20:00 CST（约 1.8h），本轮首次进入结束窗 ≤2h。本窗无官帖。该公售已在 R1815 按开窗 ≤2h 通知且当时已写明结束时间，本轮不重推。价格 0.0001 ETH，不是免费。
- **POLYROB**（@tmachinroBot）：本窗无新官帖，公售仍至 2026-11-16 01:12 CST，已按此前窗口通知，不重推。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST），本窗无官帖，未进入 ≤2h；qtronlaptops / pillowbookRH 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/ELY 与薄栏 TAPE/GIWA/DOGE 打满 25 条硬顶；KW_MINE 0；MEN_MINE 0。MEN_ELY 打满 25。
- mentions：LayerZero 10（含本轮新收录 @ozero_fun）；Elysium+kinetiq 25（多为已在库/社区互动）；mining-squeek+Nutshell 0；BN Agent pads+STARX 3。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮 LayerZero mentions 盲捞独立发现 @ozero_fun（新建号、0 粉），不是靠关注表。
- 未送审（不收录）：@fufufafau7 仍是 @numencash 引流（R1862 已点名）；@launchonmorph 自称 Morph/Meteora Solana 发射台，无已确认官网；@LayerzeroEco 为侦察号而非可操作 mint；@BulwarkScore 为协议评分工具；@Galadomaiugb 空回复；@dorix_4cm 为已在库 0pad 的早期 ID 领取。其余为 giveaway/喊单噪音。

## Watch 漏挂修复

- 本轮 0。ozero 收录同时写入 userFollowWatch + layerZeroWatch + zeroWatch。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1863.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 ozero；osk-agent 池已开（新的可操作变化）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 334 mcnuggetsonline 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- DualForge 同一 19:00 CST 开铸窗口已在 R1861 按首次 ≤2h 推送，后续轮次不要重复提醒，除非档期改动、出现新 CA/开闸确认，或进入可操作变化。
- osk-agent 池已开事件已在本轮 R1863 推送并写入已核验 CA，后续不要重复「池已开」提醒，除非出现新的可操作变化（例如新阶段、停池、明显流动性变化或新规则）。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复客服回复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售至 20:00 CST，本轮已进入结束窗但因 R1815 已写明结束时间不重推；结束后如有新阶段再判断。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
