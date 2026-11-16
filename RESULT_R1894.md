# RESULT R1894

- time: 2026-11-16 09:36 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 24（main 23 + silent 1）
- remaining: 944 → 920 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: paidtok
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit 703f737 R1893）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫，R1893 已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=944），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent 台子/Meme 栏（仅 mentions；上轮 deferred 不再花档案额度）。DC 不登录，discordPeekDeferred=true。本号不自动 mint。

## X 额度与查询

remainingBefore=944（UF1 后页脚 943/1000）。24 次读取后 remaining=920。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=23（THIN 去重后 4 片而非典型 5 片），打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 177 hoodclub_rh 起 packed 2 片 kept 50（25+25；hint 50），wrap=false，walkScanned 59。NF_skip 9（AGENTICABOT / HashOre_BNB / usejackbay / DubbllePadX / SealzHood / BNBS_ai / keccaklings / ponzihooks / swiprdotxyz）。其中 7 个为本轮新写入 NF_skip（HashOre_BNB / usejackbay 已在列）。lastKept holovaprivacy。next 235 swiprdotxyz。
- MUST1：25 个 live/窗口号（含 @ciphersyndi / @Hood_Bitz / @inklegions / @hoojafun）；MUST2：7 个全部折入优先号。mustSkip=[DualForgeBSC]（已落入 UF2，未重读）。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 104 号打成 4 片全读（与本轮 UF+MUST 重叠后不足 5 片，不是漏跑薄栏官号）。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T00:00:00Z（约 1.5h，与 R1893 official 23:30Z 窗口重叠约 1h）；KW 与 mentions 自 2026-11-15T23:25:00Z（约 2h）；silent 自 2026-11-15T01:25:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 6 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 1。
- silent：1894%11=2 台子/Meme。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（25 帖），未再花 get_users_by_usernames（ZeroHoppersNFT 仍在 doNotSpendSilentOn）。sentToReview 1（@usePaidTok，同时出现在 KW_PAD），admitted 1。下一轮 lane=GO盘。
- 部分 KW/MUST/mentions 的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。

## 信号与结论

新录取 1：**paidtok**（@usePaidTok）。无 ≤2h 新窗口。watchLeaks=0（已把 @usePaidTok 写入 userFollowWatch）。判断/文案走 DeepSeek，dsFallback=false。

- **paidtok**（新收录，notify）：开号 2026-11-16 06:45 CST，粉 3、9 帖。09:22 CST 官宣 “We are live”，自称面向 TikTok 的发射台，可为任意 TikTok 账号发币、创作者费用自动归属。资料栏展开官网 https://usepaidtok.fun/ HTTP 200，有 Connect wallet / Launch for a creator，外链 pump.fun。站点 JS 声明 CA `ScqzaRCpW4vCze1wc9QCx553PYNC7w7G53b5CQ9pump`（站点声明，非官推/链上核验）。同号 09:21 CST 自述 payout 路径是对 Solana 主网的模拟、Nothing was signed or sent。不是免费 mint / 免费登记。paidtok.com 为无关 Watch & Earn 站，未当作官网。本号不自动 mint。
- **microfrens**（在库）：08:55–09:00 CST 官号预警 OpenSea 本集合被隐藏、出现仿盘（36h 前提工单未回复），并讨论若把份额收到 2222 则快照前买家未必人人拿到免费 mint；免费 mint 口径为买了 3 份及以上。属安全预警与份额讨论，非新的首次开窗，不重推。
- **cipher-syndicate**：08:31 CST 再发同一份时间表 Starts TONIGHT at 4:00 PM UTC（11:00 PM GMT+7）= 2026-11-17 00:00 CST；Stage 1 AL 免费 mint 444 cap；Stage 2/Public sub-0.0001 ETH。官帖仍写 10,000，继续以官网/OpenSea 1,234 为准。距今约 14.4h，非 ≤2h，非 LIVE。已在 R1892 按真新提醒，同一时间表不重推。
- **sunfall-world**：09:07 CST 官宣 Season 1 is done，冠军 Ganjathang Cloud Nine 获 0.5 HYPE 与 Sky Keep，First Keeper 任职至 Monday 23 Nov，并公布 weekly prize top 8。属赛季结算，非新 mint/登记窗口，不重推。
- **hood-bitz**：本窗仅 08:25 CST 回复 💚，仍无 BITBOTZ mint-live 时刻，不重推。
- **deadhood**：08:27 CST 再发 Mint Out，已是 sold-out，不重推。
- **tapemine**：08:35 CST 讲述 Behemoth #2755 设计溢价/算力，属二期进度，不重推。
- **inklegions / hoojafun**：MUST1 本窗无这两号新帖。Ink Legions 开铸仍 2026-11-17 03:00 CST 免费 mint，非 ≤2h（约 01:00 CST 11/17 才进入 ≤2h）。
- **banknotes_btc / zerolotl**：本窗帖与 R1893 已记录内容相同（this week / 主网将至），不重推。
- 预拒：Rezofun（无官网、coming、bio typo、曝光 5）；Unvault Mint Dates 仅第三方转帖且未写日期；priors_trade / _shadesol 已在库复述；anubislayer1 科普；shellytoken 已毕业 pump.fun 表情包。未把已在库项目再送 DeepSeek 当新卡。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 235 swiprdotxyz。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：已跑台子/Meme；下一轮 GO盘。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- PaidTok 本轮已按真新提醒；同一份 “We are live” + 未核验 CA 不重复推，除非官推公布并核验 CA、出现真实链上发射/结算，或出现免费窗口。
- hood-bitz 同一份 OpenSea 隐藏/仿盘预警与 2222 免费份额讨论不重推，除非公布 BITBOTZ 开窗时刻或确认 LIVE。
- MicroFrens 本轮同一份 OpenSea 隐藏/仿盘预警与 2222/“买 3 份以上才有免费 mint”讨论不重推，除非出现新的首次可操作窗口或确认新集合 LIVE。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- sunfall-world Season 1 已结束/冠军结算不重推，除非出现新 mint/登记窗口。
- 沿用 R1893/R1892：deadhood 售罄确认、hooja-fun “Not yet, soon”、shielded-wizards Ledgermaw raid、zerolotl 主网将至介绍、banknotes_btc “this week”、Hokori 燃烧已落地但官网无用户入口、wrapped-eth 会计示例且 /claim 仍 404。
- 其余已提醒窗口沿用：pillowbook 同一未开盘窗口、jacketagent 付费阶段无新变化、ozero 同一份 Base Sepolia 测试网宣传、TapeMine/Behemoth 二期进度、raccoonslimestd 仍在选择发射台、Elysium Portals 免费登记未见合约、boxcars 进度/箱子奖励刷新（除非预售开盘/改期、驾照售罄、改入口/改 CA）。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint。
