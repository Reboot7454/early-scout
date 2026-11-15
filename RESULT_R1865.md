# 早期打新雷达 R1865

- 时间：2026-11-15 19:17 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 oreva、questfun、hooded-legends、filobook、bamboo-ronin；均非已核验免费 LIVE、非首次 ≤2h，但属真新。bamboo-ronin 仅观察，不得当成免费 LIVE）
- 新收录：oreva（@OrevaPoW）、questfun（@questfunsol）、hooded-legends（@HoodedLegends）、filobook（@filobookrun）、bamboo-ronin（@BambooRonin）
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 3c39199 R1864）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 431 → remaining 406（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 431≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。本轮 thin official 与 UF 分片无重叠，THIN official 5 批全读，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 382 / 1-based 383 pitpadfun 起，kept 48，真实 NF_skip 0，walkScanned 48，无绕回。last kept 0-based 429 / 1-based 430 Agenthashapes，next 0-based 430 / 1-based 431 SwarmHiveBNB。收录后已把 @OrevaPoW、@questfunsol、@HoodedLegends、@filobookrun、@BambooRonin 追加进 UF。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun（thinSkipDedup 仅 ozero_fun 已在 MUST1，未在 THIN 重读）。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=Tape/电路（1865%11=6）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=37，sentToReview=0，admitted=0，skipped=37（too_many_posts 35，already_in_library 2）。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T10:06:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T09:06:00Z（约 2h）。silent start=2026-11-14T11:06:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 0、UF2 0、MUST1 12、MUST2 0、THIN1 5、THIN2 4、THIN3 0、THIN4 0、THIN5 0、KW_LZ 3、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 10、KW_SN 11、KW_MINT 25、KW_MINE 1、KW_PAD 25、KW_GO 6、KW_ELY 25、MEN_LZ 14、MEN_ELY 25、MEN_MINE 0、MEN_BN 1、SILENT_MEN 25。
- 首读 UF1 后快照 430 / 1000，故 remainingBefore=431；末次 SILENT_MEN 快照 406 / 1000。
- THIN official 本轮 5 批。thinSkipDedup 仅 ozero_fun。watchLeaks 0。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 新收录

- **oreva**（@OrevaPoW，id=oreva）：本轮 KW_MINE 盲捞发现。官号 2026-11-13 07:30 CST 建立（xUserId 2121022773980004352），蓝标，1 粉、1 帖、following=0。官网 https://oreva.work/ HTTP 200，站点 JS 回链 https://x.com/OrevaPoW，资料栏回链官网，互链成立。官帖 19:04 CST https://x.com/OrevaPoW/status/2121922247858266383 宣布 Agent 挖矿农场：BNB Chain / Flap 单币 $ORE，登记每台需 Agent 钱包持 50,000 ORE，2% 交易税以 BTCB 结算（80% 矿工奖池 / 20% 储备）。站点 /oreva-deployment.json（chainId=56）公布 token `0xDcDc1aBaD15895EF31fDA384731eA4f65F317777`、registry `0x244eC7F365EDafB0a8F8aBf7e8C43e6d113CbeeB`、vault `0x9aB0003d48d1F9Efbb16B310684bcb7388E29A7E`、factory `0x5b2A1224fD01E61770584eE0aeBbCa1fA9c4CcCe`；本轮未做链上独立核验，caUnverified=true。DeepSeek-flash（思考开）admit=true，overall 63（early 93 / actionable 52 / novelty 80 / risk 78），category=挖矿，status=live，focus=false。已进 userFollowWatch + miningWatch + agentMiningWatch。非免费 mint、非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。
- **questfun**（@questfunsol，id=questfun）：本轮 KW_PAD 盲捞发现。官号 2026-11-15 03:35 CST 建立（xUserId 2121687958441103360），蓝标，4 粉、2 帖。官网 https://questfun.xyz/ HTTP 200，站点回链 https://x.com/questfunsol，互链成立。官帖 19:09 CST https://x.com/questfunsol/status/2121923591088504905 称 mission-powered launchpad，$QUEST coming to pump.fun，给出 CA `9h9oJPr4yPgZgJE1rzevJmgqjWBiYnmp6TfVL2EHpump`，同时写 Token not live yet。站点自称 v0.1-BETA。DeepSeek-flash admit=true，overall 57（early 92 / actionable 40 / novelty 58 / risk 72），category=台子/Meme，status=announced，focus=false。已进 userFollowWatch。非免费 mint、非 ≤2h，但属真新。本号不自动 mint。
- **hooded-legends**（@HoodedLegends，id=hooded-legends）：本轮信号见到。官号 2026-11-08 03:24 CST 建立（xUserId 2119148397634441216），蓝标，1230 粉、57 帖。官网 https://hoodedlegends.xyz/ HTTP 200，站点回链 https://x.com/HoodedLegends，互链成立。888 张 1/1 手绘角色，Robinhood Chain，mint 时间与价格 TBA，WL 入口在置顶帖。本窗无该号自己的开窗帖，未见 CA。DeepSeek-flash admit=true，overall 56（early 66 / actionable 38 / novelty 56 / risk 58），category=打新，status=announced，focus=false。已进 userFollowWatch。非免费 LIVE、非 ≤2h，但属真新。本号不自动 mint。
- **filobook**（@filobookrun，id=filobook）：本轮信号见到。官号 2026-11-13 19:16 CST 建立（xUserId 2121199761566912512），蓝标，42 粉、21 帖。官网 https://filobook.run/ HTTP 200，站点回链 https://x.com/filobookrun，互链成立。产品是 agent 经济实时订单簿；官网写 $FILO is live on Robinhood Chain，购买入口 Pons，公布代币合约 `0x6dfcdbfc63015cf4ac4ba4fa69ce9e68603a05cf`（本轮未做深度链上核验，caUnverified=true）。DeepSeek-flash admit=true，overall 80（early 92 / actionable 82 / novelty 74 / risk 45），category=台子/Meme，status=live，focus=false。已进 userFollowWatch。非免费 mint、非 ≤2h，但属真新。本号不自动 mint。
- **bamboo-ronin**（@BambooRonin，id=bamboo-ronin）：本轮在他人帖 includes 中见到，未额外重读时间线。官号 2026-11-10 22:08 CST 建立（xUserId 2120156276189528064），蓝标，554 粉、6 帖。资料栏无网站，本轮未找到官网。bio 仅写 555 free pandas on @Robinhoodapp。本窗无该号自己的开窗帖，未见 CA。DeepSeek-flash admit=true，overall 50（early 88 / actionable 40 / novelty 55 / risk 35），category=打新，status=watching，focus=false。已进 userFollowWatch。免费是否 LIVE 无法核验，**不得写成免费 LIVE**。属真新观察卡，按 notify 规则推送。本号不自动 mint。

## 在库窗口 / 可操作变化

- **DualForge**（@DualForgeBSC）：原定开铸 2026-11-15 19:00 CST 已过。本轮约 19:17 CST 复查，MUST1 本 1h 官方窗无该号新帖，仍无官网/新 CA/开闸确认，status 保持 announced，不是已确认开铸。首次进入 ≤2h 已在 R1861 推送，本轮不重推。le2h 已关（开铸时刻已过且未确认 LIVE）。仅限 Binance Agent ID。
- **osk-agent**（@AIAgent_OSK）：官号 19:04 CST https://x.com/AIAgent_OSK/status/2121922370932019402 再述 0.008 BNB、95% OSK/WBNB LP / 5% inviters、免费席已尽、下一席开池；与 R1863 已推送的池已开窗口同一口径，不是新的可操作变化，不重推。付费只告警，本号不自动 mint。
- **hokiseries**：Base Bots 公售仍至 2026-11-15 20:00 CST（约 0.7h），仍在结束窗 ≤2h。该公售已在 R1815 按开窗 ≤2h 通知且当时已写明结束时间，本轮无该号新帖，不重推。价格 0.0001 ETH，不是免费。
- **POLYROB**（@tmachinroBot）：官帖 https://x.com/tmachinroBot/status/2121921345948705009 写关闭时间为 Sun 17:12 UTC = 2026-11-16 01:12 CST，约 6h，已按此前窗口通知，不重推。
- **pillowbook-rh**（@pillowbookRH）：官帖 https://x.com/pillowbookRH/status/2121921165199290586 写 T-6h，Sun 15 Nov 17:00 UTC = 2026-11-16 01:00 CST，尚未进入 ≤2h，不重推。
- **qtronlaptops**：仍为 Today 5pm UTC = 2026-11-16 01:00 CST 第二批窗口（R1864 已记录 18:34 CST 帖），距开铸约 6h，尚未 ≤2h，不重推。
- **jacketagent**：免费仍 LIVE 至 2026-11-16 00:00 CST（约 5h），尚未进入 ≤2h，不重推。
- **MicroFrens**：本窗仅感谢类回复，对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送），无新的对公窗口或份额规则变化，不重推。
- HoodTurtle / DeadHood_nft / Gloopix / infamousScratch 本窗无新帖。hood-turtle mint 仍是 11-17 22:15 CST。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 TAPE/GIWA/DOGE 与核心栏 KW_MINT/PAD/ELY 打满 25 条硬顶；KW_SN 11；KW_BTC 10；KW_GO 6；KW_LZ 3；KW_MINE 1。mentions：LayerZero 14、Elysium+kinetiq 25、mining-squeek+Nutshell 0、BN Agent pads+STARX 1。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞独立发现 @OrevaPoW（1 粉新建号）与 @questfunsol（4 粉新建号），不是靠关注表。
- 未送审（不收录）：**kinetiq-toons**（@KToonsNFT，官网 kinetiqtoons.xyz 互链成立，Elysium NFT，WL 已关、mint TBA、非当前免费 LIVE）DeepSeek admit=false overall 50，暂不列入；**social-gruff**（@SocialGruff，官网 gruff.family，DogeOS 工具，账号约 32 天、近 2k 粉，站点未见回链官推）DeepSeek admit=false overall 46。另跳过 Nekointhehood（0 帖、无站点、仅 bio 写免费，按 yums 类暂缓）、billtobillion（meme 币）、maicaem27（持币号）以及 KOL/giveaway 噪音。numencash、PlunderPort、BitMinersonRH、FungoLabs 已在库。

## Watch 漏挂修复

- 本轮 0。oreva 写入 userFollowWatch + miningWatch + agentMiningWatch；questfun / hooded-legends / filobook / bamboo-ronin 写入 userFollowWatch。在库且本轮新卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1865.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 oreva、questfun、hooded-legends、filobook、bamboo-ronin（仅观察）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 430 SwarmHiveBNB 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- DualForge 原定 19:00 CST 开铸已过但本窗仍无开闸/CA 确认，不要把「到点」写成已开铸；首次 ≤2h 已在 R1861 推送，后续不要重复提醒，除非出现新 CA、官方开闸确认、改期或其他可操作变化。
- osk-agent 池已开事件已在 R1863 推送并写入已核验 CA，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复客服回复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售至 20:00 CST，已进入结束窗但因 R1815 已写明结束时间不重推；结束后如有新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 免费 LIVE 至 11-16 00:00 CST，进入 ≤2h 后再判断。
- bamboo-ronin 不得在后续轮次仅凭 bio 写成免费 LIVE；需官网、官方开窗帖或 CA 之一确认。
- kinetiq-toons 本轮 DS skip（WL 已关、mint TBA）；若后续官宣开铸/免费 LIVE 再核收录。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
