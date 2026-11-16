# RESULT R1908

- time: **2026-11-16 16:41 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **false**
- newThisRound: 无
- le2h: 无
- dsFallback: false
- xReads: **26**（main 25 + silent 1）
- remainingBefore: **596** → remaining: **570**
- softCap 18 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1907）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=596），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent Elysium 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=596（首读 UF1 后 remaining 595，按 left_after_first+1 还原）。26 次读取后 remaining=570。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，打满 minSpend 18，超过 softCap 18（+7）：MUST 优先号+窗口号在 2 片装不下，增加 MUST3；THIN official 去重后 107 号需要 5 片。silent 1 次在 softCap 外。

- UF1–UF2：0-based 1049 Hypercellfun 起 packed 2 片 kept 49（24+25），wrap=false，walkScanned 50。NF_skip 1，全部已在列：ePegsV4；新写入无。firstKept Hypercellfun，lastKept AgentCityrh。next 1099 Hood_Junkies。
- MUST1：24 个 live/窗口号；MUST2：25 个；MUST3：3 个（localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=['tmachinroBot', 'PlatoUnseen']（本 UF 分片已覆盖，未重复读）。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。theoutcomers 为等待名单卡、无定时窗口，未自动加入 MUST。MUST2 打满 25 条硬顶，多数为 @MicroFrens 回复，可能挤掉同片其他官号，未另开重复确认读。
- THIN official：去重后 107 号 5 片全读（26+25+26+26+4）。UF1 / MUST3 / THIN1 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T07:00:00Z（约 1.5h，与 R1907 06:30Z 重叠）；KW 与 mentions 自 2026-11-16T06:30:00Z（约 2h）；silent 自 2026-11-15T08:30:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 7 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 2。
- silent：1908%11=5 Elysium，SILENT_MEN 1 次 25 帖，送审 12、录取 0。下一轮 lane=Tape/电路。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 44；在库作者 19（official）/ 25（含关键词已在库作者）；新作者 171，短名单保留 97，跳过 74，very_new 8。9 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

栏 rc：UF1 0、UF2 1、MUST1 6、MUST2 25、MUST3 0、THIN1 0、THIN2 5、THIN3 3、THIN4 1、THIN5 0、KW_LZ 4、KW_TAPE 25、KW_GIWA 25、KW_DOGE 22、KW_BTC 12、KW_SN 1、KW_MINT 25、KW_MINE 1、KW_PAD 25、KW_GO 3、KW_ELY 25、MEN_LZ 7、MEN_ELY 25、MEN_MINE 0、MEN_BN 2、SILENT_MEN 25。parse_errors=[]。

## 收录与在库

新收录 0 张。

在库刷新（均不重推）：

- tapeai：@TapeAIAgent 16:27 CST 官帖（https://x.com/TapeAIAgent/status/2122245262802391289）称 BEM 预存量突破 10,000，预存持续进行中，规则与 R1907 已开窗口相同。R1907 已按首次「预存已开」提醒，本轮只记进度，不重推。本号不自动存。
- tapeup：@tapeupio 16:29 CST 转发同一进度帖（https://x.com/tapeupio/status/2122245682547577065），主记录在 TapeAI 卡，不重复推。
- inklegions：16:29 CST 官帖（https://x.com/inklegions/status/2122245573902504289）称今日 8:00 PM GMT+1 出征，对应已记录的免费 mint 2026-11-17 03:00 CST，尚未 ≤2h，不重推。
- spoxyfun：16:12 CST 官帖（https://x.com/SpoxyGang/status/2122241299797749962）预告 Marketplace，并重申免费已结束、付费 0.001 BNB 仍开。已在 R1870 按付费 LIVE 提醒，不重推。
- dualforge-bsc：16:02 CST 官帖（https://x.com/DualForgeBSC/status/2122238889738006585）称今日 fresh mint，属每日 opening tier，不是首次开窗，不重推。
- ephemeral-eth：本窗再见同一条 23:00 CST 到账说明（R1907 已记）及支付映射帖（https://x.com/ephemeral_eth/status/2122239266965381585）。尚未 ≤2h，不重推。
- microfrens：15:49 CST 称稀有特征约 12 小时后揭示（https://x.com/MicroFrens/status/2122235515118530743），对应已记录的 11-17 01:00 CST reveal，mint 已完成，不重推。
- gloopix：15:02 CST GTD 审核帖已在 R1906/R1907 记录，不重推。
- wrapped-eth / pingpay / zyro / unicorn-grand-prix / raeto / gamapad / ammora / tapemonkey：产品续更或社区帖，不重推。

尚未 ≤2h、无改期、不重推：Bombshell Cats AL 11-16 20:00 CST；dotBots Round 2 销售 21:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST。

## 跳过（要点）

- 无新官号可建卡。DeepSeek 评审后未录取（admits=[]）。思考输出未给出完整 JSON，但两次评审均明确不录取已上线代币/Elysium Exploring/纯转发；@lilypadprotocol 无官网、无 ETA、不可操作，不建卡。dsFallback=false。
- @BlotExaminer（今日建号，0 粉）称 Ten inkblots on @Enter_Elysium，资料栏无网站，t.co 只回到自己的推文，属 Exploring 级迷因，不建卡。
- @Flagellumly / @woblclub：与 R1907 相同，已上线迷因或 Exploring 预告，不建卡。
- @OMNIQPAD_SOL：站点 https://omniqpad.com/ 已开，bio 已有 pump CA，自称 LIVE on Solana，属已上线代币+展示站，不建卡。
- @Rhinovx：已在 Raydium bonding curve 交易，空投广告，不建卡。
- @lilypadprotocol：自称在测 Solana launchpad，无官网、明确没有 ETA，不可操作，不建卡。
- @chellynXrh / @0xpelzz 等纯转发：提到 @VitrumFalcons 11-18 OpenSea/RH 免费 mint（官号本窗未出现，未另开确认读）、@Mopesnft / @trippiart / @FeedTheFireRH 已在库；第三方时间相互矛盾，不以转发改期。
- @TenthOnElysium 只转发已在库的 PlunderPort；@Pumper_Liquid 称 $PUMPER 已在 Elysium/Montra 上线，属已上线迷因。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1099 Hood_Junkies。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

false。无新收录，无首次进入 ≤2h 的窗口，推送成功。TapeAI 10,000 BEM 是 R1907 已提醒的同一已开预存的进度，不重推。无新免费 LIVE / 免费 mint 卡。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
