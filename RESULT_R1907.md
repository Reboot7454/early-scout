# RESULT R1907

- time: **2026-11-16 16:13 CST**
- mode: **ample**（独立例行，非第二次 post-reset-full）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: 无
- le2h: 无（TapeAI BEM 预存已开，本轮提醒后不再标 ≤2h）
- dsFallback: false
- xReads: **24**（main 23 + silent 1）
- remainingBefore: **620** → remaining: **596**
- softCap 28 / minSpend 20 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1906）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=620），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent LayerZero 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=620（首读 UF1 后 remaining 619，按 left_after_first+1 还原）。24 次读取后 remaining=596。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=23，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。本轮 THIN official 打成 4 片（103 号），比上轮少 1 次主读，仍 ≥ minSpend。

- UF1–UF2：0-based 994 velom33 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 55。NF_skip 5，其中 1 个新写入：MOIbitcoin；4 个已在列：UseZPadX/agenticsocial/dyorcash/404Naroba。404Naroba 已在 meta.NF_skip，本轮同步进 uf.NF_skip；MOIbitcoin 同时写入 meta.NF_skip 与 uf.NF_skip。firstKept velom33，lastKept getPOPAI。next 1049 Hypercellfun。
- MUST1：24 个 live/窗口号；MUST2：24 个。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。theoutcomers 为等待名单卡、无定时窗口，未自动加入 MUST。
- THIN official：去重后 103 号 4 片全读（26+25+27+25）。THIN1 / THIN4 / UF1 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T06:30:00Z（约 1.5h，与 R1906 06:00Z 重叠）；KW 与 mentions 自 2026-11-16T06:00:00Z（约 2h）；silent 自 2026-11-15T08:00:00Z（约 24h）。
- mentions 4 组轮换：Tape 21 / GIWA 4 / BTC 1 / Starknet+DogeEVM 1。
- silent：1907%11=4 LayerZero，SILENT_MEN 1 次 25 帖，未从该栏录取。下一轮 lane=Elysium。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 34；在库作者 18；新作者 180，短名单保留 112，跳过 68，very_new 6。8 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

## 收录与在库

新收录 0 张。

在库首次确认可操作窗口已开始（重推）：

- tapeai：@TapeAIAgent 16:00 CST 官帖（https://x.com/TapeAIAgent/status/2122238445347389449）称「TapeAI 预存正式上线，瓜分 630,000 枚 TAI 空投」，现支持 BEM / BNB / USDT 预存，BNB/USDT 按市价折算为 BEM；每预存 1 BEM 得 1 积分，直邀 20%、间邀 10%，按有效积分权重分享 TAI 总量 3%（630,000）。@tapeupio 16:03 CST（https://x.com/tapeupio/status/2122239142071542171）英文官帖确认 “TapeAI pre-deposits are now live on TapeUP”。站点 https://tapeup.io/ HTTP 200，前端有「预存 BEM / BNB / USDT，预购买 TAI」活动文案；https://app.tapeup.io/ 本轮 TLS unexpected eof（与近几轮相同），不据此判断站点下线；https://tapeai.net/ HTTP 200，首页未检出独立预存入口。R1903–R1906 已按即将开始的 ≤2h 窗口提醒过，当时预存尚未开始；本轮是首次「已开始」确认，notify=true 一次。提醒后 le2h=false，后续轮次不得对同一已开预存再推。非免费 mint。本号不自动存。

在库刷新（均不重推）：

- tapeup：同一条已开预存确认，主提醒放在 TapeAI 卡，本卡只补一句、不重复推。
- ephemeral-eth：16:04 CST 官帖（https://x.com/ephemeral_eth/status/2122239254386663472）重申代币今日 15:00 UTC / 23:00 CST 到 Ethereum 主网，并称合约已开放可读。同一份已提醒窗口，尚未 ≤2h，不重推。站点 ephemeral.money HTTP 200。
- zyro：16:39 CST 官帖为已上线产品界面更新，不重推。
- gloopix：15:02 CST 评论区 GTD 审核帖已在 R1906 记录，本窗重叠再见到，不重推。
- wrapped-eth / Creedo / PingPay / PaidTok / Bitsigil / inklegions / tapeupio Builder Camp：产品续更或同一已记录官帖，不重推。

尚未 ≤2h、无改期、不重推：Bombshell Cats AL 11-16 20:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；dotBots Round 2 销售 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；boxcars presale 11-17 21:00 CST。

## 跳过（要点）

- 无新官号可建卡。DeepSeek 未录取新卡（admits=[]）。
- @xykink（创建于 14:35 CST，4 粉）发 Pons V2 bonding-curve 可视化页 https://xy-k.ink/（HTTP 200），链向已有 https://ponsfamily.com/launchpad，本身不是新开铸或新台入口，不建卡。
- @PinkChainNet（约 11.2 天，19 粉）称 Pink One Live on Solana，站点 https://pinkone.base44.app/ 为 Base44 托管 SPA（仅标题，置信度低），bio 已有代币 CA，不是本轮新开窗，不建卡。
- @Flagellumly 称 FLGL 是 @Enter_Elysium 上的生物迷因且已有池，属已上线迷因，不是 testnet / Announced+部署，不建卡。
- @woblclub 仅一句 “something’s starting to sway on @Enter_Elysium”，Exploring 级预告，不建卡。
- Ammora/GIWA 评论宣传号、RGBHorse 第三方（已在库）、0xGigaChads 与已关注 zerodroidsio 的合作、LaikaSuperApp 转发（laika-doge 已在库）均不新建卡。

## 覆盖与债

- 十栏关键词：跑全。
- userFollowWatch：本分片刷完，wrap=false，next 1049 Hypercellfun。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。TapeAI / TapeUP 的 BEM 预存已正式开启（支持 BEM、BNB、USDT；BNB/USDT 按市价折算为 BEM；每预存 1 BEM 得 1 积分，直邀 20%、间邀 10%，按有效积分分享 3% TAI / 630,000 枚）。这是首次官方确认「已开始」，与此前「16:00 CST 即将开始」的 ≤2h 提醒不同，推一次。此后同一已开预存不再重推。详情看 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。

无新免费 LIVE / 免费 mint 卡。ephemeral-eth 仍是 23:00 CST，尚未 ≤2h。
