# RESULT R1904

- time: 2026-11-16 14:37 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 695 → 670 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: false
- newIds: （无）
- le2hIds: tapeai
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1903）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=695），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent 挖矿栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=695。25 次读取后 remaining=670。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 823 Elysiumgloom 起 packed 2 片 kept 48（24+24），wrap=false，walkScanned 63。NF_skip 15，其中 5 个为本轮新写入（PlayTycoonCity / PunksOnDrugs / baoracletrade / agentplacewall / LastCall4vx）；其余 10 个已在列（SENSEIAgent_ / Agentspunks / cryptosympbnb / BN_Big_Bang / LumenGenesisNFT / Estock_ / pixelboyzai / Panba_EmojiPack / AmberPoW_BSC / DigitalBombAI）。firstKept Elysiumgloom，lastKept elys_inscribe。next 886 ElyChestFun。
- MUST1：24 个 live/窗口号；MUST2：24 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + PlunderPort + PonkeAgent + KomaAgentID + pumptoksocial + pantheonperps + SYR0xyz + ZyroxRH + usePingPay + spiritsHOOD + UnicornGPrix + isomatricaaa + 7 个优先号）。为把本轮新收录的 3 个官号塞进 MUST 且不超过 2 批，计划时从 MUST 拿掉已过窗的 MicroFrens（mint 已完成）、DualForgeBSC（已开第二天）、SunfallWorld（季节宣传、无新 mint 窗）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 106 号 5 片全读（26+25+26+26+3）。UF1 / THIN1 / THIN3 / THIN5 / MEN_MINE 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T05:00:00Z（约 1.5h）；KW 与 mentions 自 2026-11-16T04:30:00Z（约 2h）；silent 自 2026-11-15T06:30:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 7 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 1。
- silent：1904%11=1 挖矿，SILENT_MEN 1 次 1 帖，未录取。下一轮 lane=台子/Meme。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 45；在库作者 17；新作者 166，短名单保留 93，跳过 73。

## 收录与在库

0 新收录。DeepSeek（deepseek-flash，思考开启）确认盲捞无可独立建卡的新官号，dsFallback=false。

在库刷新（均不重推）：

- tapeai：同一份已提醒的 BEM 预存窗口仍有效（2026-11-16 16:00 CST），现距窗口仍 ≤2h，预存尚未开始。R1903 已在进入 ≤2h 时提醒过；本轮未见新的官方时刻或「已开始」确认，不重推。le2h 保持 true。
- unicorn-grand-prix：复查官网 HTTP 200，Date 仍 to be announced；白名单页本轮 HTTP 200，但正文仍写 “The whitelist opens soon” / “not reachable right now”，不是首次可提交开放。14:02 CST 官帖已在 R1903 记入，只是重申门槛。
- isomatrica：仍是同一条 13:43 CST 官帖重申 Robinhood Chain + OpenSea，与官网 Ethereum 口径冲突未裁定；站内白名单 Now Open、Mint Not Yet Live。
- spiritsrh：仍是同一条 13:46 CST 白名单官帖，mint 未开窗；仅刷新 lastChecked。
- ozero：14:21 CST 官帖再发 Base Sepolia 测试网宣传，站点 HTTP 200，未见主网 mint。
- dotbots-ai / dotbots：13:02–13:03 CST 官帖宣布 The Arena Pioneer Cup is OPEN（Bot Battle testnet，Now → Nov 30 12:00 GMT+7）。这是已预告的测试网杯赛开赛，不是主网免费 mint，不按开铸通知。Round 2 销售 21:00 CST 尚未 ≤2h。

产品续更、同一已开闸入口不重推：PingPay / Zyro / PumpTok / Creedo / PaidTok / Vorda（GIWA Sepolia Missions）/ wrapped-eth。

尚未 ≤2h、无改期、不重推：Bombshell Cats AL 11-16 20:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；hooja-fun UNVAULT 仅有日期无时刻；MicroFrens reveal 11-17 01:00 CST（mint 已完成）。

## 跳过（要点）

- Mercatoragens：自称 launchpad，在招 trading bots / AI agents，不是本轮可操作打新窗口。
- Jennifer_Verse 等第三方转帖 @Mopesnft「Free Mint GTD + FCFS」：第三方拉新模板，不是官方确认开窗；mopesnft 已在库 watching。
- destroyer00bbb / BarivoleEvco：回复 Ammora Season 2，不是新官号。
- alexinsaan / Breezeofl 等空转或转帖号。
- Gebie_1（silent 挖矿栏）：第三方介绍 KleverChain 上的 KlyxSpace / KLVGoldMiner，不新建卡。
- 多个 DogeOS / Monko Mania 测试网积分截图号，以及 Elysium/Pad 评论向 KOL：不是新项目官号。
- AnFeng0858：仍是 TapeOut 布道者个人号。

## 覆盖与债

- 十栏关键词：跑全。
- userFollowWatch：本分片刷完，wrap=false，next 886 ElyChestFun。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

false。0 新收录；TapeAI 只是同一份已提醒的 ≤2h 预存窗口，无首次可操作变化；Unicorn 白名单仍不可提交；Isomatrica / SpiritsRH 无新入口；dotBots Pioneer Cup 是测试网杯赛；Ozero 仍是测试网。不在本聊天重复提醒。
