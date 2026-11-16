# RESULT R1905

- time: 2026-11-16 15:09 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 670 → 645 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: theoutcomers
- le2hIds: tapeai
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1904）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=670），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent 台子/Meme 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=670。25 次读取后 remaining=645。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 886 ElyChestFun 起 packed 2 片 kept 48（24+24），wrap=false，walkScanned 54。NF_skip 6，其中 1 个为本轮新写入（astropad_real）；其余 5 个已在列（ditherglyphs / exec_terminal / orivatbnb / spiderproject69 / useampad）。firstKept ElyChestFun，lastKept KnightsAgentTbl。next 940 Standssocial。
- MUST1：24 个 live/窗口号；MUST2：24 个。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 105 号 5 片全读（26+25+26+26+2）。UF1 / UF2 / THIN1 / THIN3 / THIN5 / MEN_BTC 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T05:30:00Z（约 1.5h，与 R1904 05:00Z 重叠）；KW 与 mentions 自 2026-11-16T05:00:00Z（约 2h）；silent 自 2026-11-15T07:00:00Z（约 24h）。
- mentions 4 组轮换：Tape 24 / GIWA 4 / BTC 0 / Starknet+DogeEVM 1。
- silent：1905%11=2 台子/Meme，SILENT_MEN 1 次 25 帖，未从该栏录取。下一轮 lane=GO盘。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 38；在库作者 17；新作者 176，短名单保留 113，跳过 63。10 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

## 收录与在库

新收录 1 张：theoutcomers（@theoutcomers，Outcomers）。已写入 userFollowWatch + freeMintWatch。

- 官推本轮 X 搜索已核验（id 2120804583387668480；2026-11-12 17:04:30 CST 开号；61 粉；218 条推）。官网 https://outcomers.trade/ HTTP 200。等待名单表单当前可提交（Email、X 用户名、引用置顶帖 URL、EVM 地址，无需连接钱包），属免费登记。
- 站点写 Join the community before the collection arrives，未见 mint 日期与合约；自述独立社区项目，Born on Hyperliquid。https://outcome.xyz/ 是 Hyperliquid 预测市场，与本 PFP 为不同产品。
- 本轮可见官帖仅 14:43 CST 一条自我挂 tag 回复（@Hyperliquid_Hub @Bitso @Enter_Elysium forgot @theoutcomers），不是开铸公告；@Enter_Elysium 不等于已部署 Elysium，卡片进打新栏而非 Elysium 栏。focus=false。
- 因新收录且等待名单为免费登记（即便 overall 58 < 70），notify=true。

在库刷新（均不重推）：

- tapeai：同一份已提醒的 BEM 预存窗口仍有效（2026-11-16 16:00 CST），现距窗口仍 ≤2h，预存尚未开始。R1903 已在进入 ≤2h 时提醒过；本轮未见新的官方时刻或「已开始」确认，不重推。le2h 保持 true。本轮 tapeai.io / app.tapeup.io 抓取超时，不据此写站点下线。
- unicorn-grand-prix：复查官网 HTTP 200，Date 仍 to be announced；白名单页本轮 HTTP 200，但正文仍写 “The whitelist opens soon” / “not reachable right now”，不是首次可提交开放。仍是同一条 14:02 CST 门槛重申。
- isomatrica：仍是同一条 13:43 CST 官帖重申 Robinhood Chain + OpenSea，与官网 Ethereum 口径冲突未裁定；站内白名单 Now Open、Mint Not Yet Live。
- spiritsrh：仍是同一条 13:46 CST 白名单官帖，mint 未开窗。本轮 spiritsrh.xyz / spiritsrh.com 未能打开，不另立官网。
- ozero：仍是同一条 14:21 CST Base Sepolia 测试网宣传，站点 HTTP 200，未见主网 mint。
- dotbots-ai / dotbots：本轮未见新官帖。Round 2 销售 21:00 CST 尚未 ≤2h；Arena Pioneer Cup 仍是已预告的测试网杯赛，不按开铸通知。

产品续更、同一已开闸入口不重推：Creedo（14:41 CST 称 Starting today 每周 20% 平台手续费回流 $CRD，是已上线产品分配更新，不是新 mint 窗）；PingPay / PaidTok / Zyro / PumpTok / Vorda（GIWA Sepolia Missions）/ wrapped-eth（14:50 CST 更正费率图）/ agentic_starter / Bitsigil（游戏上线日 coming soon，无日期；库内 sold-out）。inklegions 14:29 CST「Legions are marching today」不写成 mint 已开始，库内免费 mint 仍是 11-17 03:00 CST，尚未 ≤2h。

尚未 ≤2h、无改期、不重推：Bombshell Cats AL 11-16 20:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；hooja-fun UNVAULT 仅有日期无时刻；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；dotBots Round 2 销售 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；boxcars presale 11-17 21:00 CST。

## 跳过（要点）

- bitfoneapp / Bitfone Launchpad：仅第三方 @PottimiNR 截断转帖，本轮未拉到官方原帖全文；bitfone.app 为 JS 应用，无可核验 mint 说明，不新建卡。
- TSBdotfun / SHADOWBORN：第三方 @Emiola_gangan 转发 GTD 免费 mint 拉新模板；tsbdotfun 已在库 watching，不按官方 LIVE 通知。
- Jennifer_Verse / oceanEVM 等第三方转帖 @Mopesnft「Free Mint GTD + FCFS」：已在库 watching，不是官方确认开窗。
- rwadiasii GiwaPad：个人用 Ammora SDK 在 GIWA Sepolia 做的浏览器演示，不是新官方发射台。
- IDraGoDev 介绍 GANG / @gangdotfun：已在库 gang-fun（live）。
- AnFeng0858 / Hhhh3i2o：TapeOut 布道者/个人号。
- 多个 Ammora/GIWA 评论搬运号，以及 DogeOS / Monko Mania 测试网截图号、TapeOut/Elysium/Pad 评论向 KOL：不是新官号。
- Bhheennyy 自拟「TapeRules」概念帖，不是已上线官方产品。

## 覆盖与债

- 十栏关键词：跑全。
- userFollowWatch：本分片刷完，wrap=false，next 940 Standssocial。新收录 @theoutcomers 已补进该 Watch 与 freeMintWatch。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。新收录 Outcomers（@theoutcomers）：官网等待名单已开、可免费登记（引用置顶帖 + EVM 地址）；藏品尚未开铸、无 mint 日期与合约。详情 https://reboot7454.github.io/early-scout/

TapeAI 同一份已提醒的 ≤2h 预存窗口不重推。Unicorn 白名单仍不可提交；Isomatrica / SpiritsRH 无新入口；其余无首次可操作变化。
