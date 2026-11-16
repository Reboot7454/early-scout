# RESULT R1909

- time: **2026-11-16 17:09 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: 无
- le2h: 无
- dsFallback: false
- xReads: **26**（main 25 + silent 1）
- remainingBefore: **570** → remaining: **544**
- softCap 18 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1908）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=570），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent Tape/电路栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=570（首读 UF1 后 remaining 569，按 left_after_first+1 还原）。26 次读取后 remaining=544。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，打满 minSpend 18，超过 softCap 18（+7）：MUST 优先号+窗口号在 2 片装不下，增加 MUST3；THIN official 去重后 105 号需要 5 片。silent 1 次在 softCap 外。

- UF1–UF2：0-based 1099 Hood_Junkies 起 packed 2 片 kept 50（24+26），wrap=false，walkScanned 51。NF_skip 1，全部已在列（历史 uf.notFound / r1512.nf / r1683 known-bad）：Haltercard；已从 uf.notFound 同步进 meta.NF_skip 与 uf.NF_skip，无新写入，未连刷。firstKept Hood_Junkies，lastKept elysfinance。next 1150 MendlingsNFT。
- MUST1：24 个 live/窗口号；MUST2：25 个；MUST3：5 个（bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。theoutcomers 为等待名单卡、无定时窗口，未自动加入 MUST。MUST2 打满 25 条硬顶，多数为 @MicroFrens 与 @usePingPay 回复，可能挤掉同片其他官号，未另开重复确认读。
- THIN official：去重后 105 号 5 片全读（26+25+27+26+1）。UF2 / MUST3 / THIN1 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T07:30:00Z（约 1.5h，与 R1908 07:00Z 重叠）；KW 与 mentions 自 2026-11-16T07:00:00Z（约 2h）；silent 自 2026-11-15T09:00:00Z（约 24h）。
- mentions 4 组轮换：Tape 7 / GIWA 4 / BTC 1 / Starknet+DogeEVM 0。
- silent：1909%11=6 Tape/电路，SILENT_MEN 1 次 25 帖，送审 3、录取 0。下一轮 lane=GIWA。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 41；在库作者 25（含关键词已在库作者）；新作者 158，短名单保留 73，跳过 85，very_new 3。9 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

栏 rc：UF1 1、UF2 0、MUST1 2、MUST2 25、MUST3 0、THIN1 0、THIN2 9、THIN3 3、THIN4 1、THIN5 0、KW_LZ 3、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 19、KW_SN 2、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 2、KW_ELY 25、MEN_TAPE 7、MEN_GIWA 4、MEN_BTC 1、MEN_SN_DOGE 0、SILENT_MEN 25。parse_errors=[]。

## 收录与在库

新收录 0 张。

在库刷新：

- spiritsrh：@spiritsHOOD 16:53 CST 官帖（https://x.com/spiritsHOOD/status/2122251624248983944）首次给出免费 mint 时刻：11-19 23:00 WIB（即 11-20 00:00 CST）在 OpenSea，3,333 免费；白名单已开、11-18 截止。官网 https://spiritsrh.surge.sh/ 。此前 mint 为 TBA。属补公布具体时刻，本轮提醒。尚未 ≤2h。本号不自动 mint。
- bitmaxdog：@bitmaxdog 16:30 CST 官帖（https://x.com/bitmaxdog/status/2122246032545214737）称 PARTNERS PHASE IS LIVE，持 36 个 Ordinals 系列之一可在游戏内点地块 mint。官网 https://dogcity.space/（本轮 HTTP 200）。窗口约 45 小时（从 16:30 CST 起，大约到 11-18 13:30 CST；帖文只写 About 45 hours，不是已核验的精确截止）。此前卡为预热、入口未披露，属首次开铸窗口，本轮提醒。非公开无门槛免费 mint。尚未 ≤2h。
- tapeai / tapeup：本窗再见同一已开预存的进度与入口说明（https://x.com/TapeAIAgent/status/2122245262802391289 / https://x.com/tapeupio/status/2122239142071542171）。R1907 已按首次开窗提醒，R1908 已记 10,000 BEM 进度，不重推。本号不自动存。
- inklegions：16:29 CST 出征帖（https://x.com/inklegions/status/2122245573902504289）对应已记录的 11-17 03:00 CST 免费 mint，R1908 已记，尚未 ≤2h，不重推。
- spoxyfun：16:12 CST Marketplace/付费帖（https://x.com/SpoxyGang/status/2122241299797749962）已在 R1870/R1908 记录，不重推。
- dualforge-bsc：16:02 CST 每日 fresh mint（https://x.com/DualForgeBSC/status/2122238889738006585），非首次开窗，不重推。
- ephemeral-eth：16:04 CST 到账说明（https://x.com/ephemeral_eth/status/2122239254386663472）及支付映射（https://x.com/ephemeral_eth/status/2122239266965381585），R1907/R1908 已记，尚未 ≤2h，不重推。
- microfrens：本窗大量互动回复，无新时刻；11-17 01:00 CST reveal（mint 已完成）不重推。
- owlgatecli / packswap / btc-crc30 / pingpay / zyro / unicorn-grand-prix / gamapad / ammora 等：行情、产品续更或社区帖，不重推。

尚未 ≤2h、无改期、不重推：Bombshell Cats AL 11-16 20:00 CST；dotBots Round 2 销售 21:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST。SpiritsRH 免费 mint 11-20 00:00 CST 也尚未 ≤2h。

## 跳过（要点）

- 无新官号可建卡。DeepSeek 评审后未录取（admits=[]）。dsFallback=false。
- @woblclub：R1907/R1908 已因 Exploring 级 Elysium 预告跳过，本窗仍 0 粉、无官网。
- @ElysiumBusiness：1.3 天、0 粉，只点名 @Enter_Elysium / @BlobOnElysium，属 Exploring 级迷因，不建卡。
- @rea_fun：Vanar 上 GitHub→代币发射台，称 One week out，不属本雷达主链。
- @memecoinsoul：$MEMES 已在 Solana 发射，属已上线代币。
- @furbi59360：宣传 NEO Bitcoin Marketplace 已 LIVE，属市场推广。
- @0xGigaChads：只宣布与已在库 @zerodroidsio 联名，不是新官号。
- 其余短名单多为 Ammora/GIWA/DogeOS/Hypesium 第三方回复或任务贴；@foomeapp 已在库。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1150 MendlingsNFT。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。无新收录卡，无首次进入 ≤2h 的窗口。按 R1897「补公布具体时刻要提醒」：SpiritsRH 首次给出免费 mint 时刻；Bitmax $DOG CITY 合作方阶段开铸（有持仓门槛）。推送成功。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
