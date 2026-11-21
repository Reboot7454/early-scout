# RESULT R2073

- time: 2026-11-21 08:43:52 CST（Asia/Shanghai）
- lastScout: 2026-11-21 08:43:52 CST
- notify: true
- newAdmits: sleeperdragons（@SleeperDragons，无官网）
- notifyReason: Kismo Seekers Whitelist Phase II 报名页已关闭（关闭事件，R2067 已报截止临近，本轮报关窗而非重复同一截止提醒）；新收录 SleeperDragons（真新，但不是免费 mint LIVE / 免费登记）。
- panel: https://reboot7454.github.io/early-scout/
- prev: 写盘前远程已是 R2072（2a6ca4d，post-reset-full，新收 TCG Miner）；本轮为重置后例行 ample，升为 R2073

## alert
【早期打新雷达 R2073】Kismo Seekers（@Kismonft / https://kismonft.com）Whitelist Phase II 报名页已关闭（页文 “The Whitelist Applications are closed for now.”；接口仍返回 open=true，以页面为准）。官网 Genesis 仍写 Mint opens · date coming soon，开铸与合约仍 TBA，不是免费 mint LIVE。

新收录 SleeperDragons（@SleeperDragons）：官号 11-18 建、仅 6 粉，资料栏自称比特币上 1,024 颗蛋、Wake the Hoard · Jan 20；无官网无合约，未见开铸或登记官帖，不是免费 mint LIVE，只宜观察。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/

## X 额度
- remainingBefore: 966
- xReads: 29
- remainingAfter: 937
- mode: ample（`python3 scripts/x_budget.py 966`；softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50；非 post-reset-full，lastFullAfterReset 保持 R2072）
- breakdown: UF 4（UF1+UF2+UF3+UF1ex）+ MUST 1 + KW_THIN 30m 6 + KW_CORE 5 + KW_GAPS 1 + KW_THIN_24h 4 + MEN 3 + SILENT 1 + MUST_TAPEAI 1 + getUsersByUsernames 2 + 误读 getUsersPosts 1（占位 id，无有效数据）= 29
- 略高于 softCap 28、高于 minSpend 20。同一 handle 本轮只拉一次（UF1ex 是错误过滤重试，仍命中已在分片内的 @anipalsonsol，未再追加读取）。
- search_users 仍不可用；silent 只跑 Tape/电路 mention 1 读（在 softCap 外）。
- 额外读取说明：MUST_TAPEAI 为核验 TAI 是否在 11-21 官宣开窗（0 帖，时间仍 TBA，不重推）；getUsers 用于短名单未入库号核验；误读 1 次不重复补刷。

## 覆盖
- userFollow: 是。cursor 1183 @CrossEyed_APP → next 1233 @KyrosElysium。walk 50 kept 50；firstKept @CrossEyed_APP，lastKept @TheUnseenAnons。skip_already=0，wrap=false，NF_skip=0。
  - UF1 视觉上几乎只有已在分片内的 @anipalsonsol（AniPals/AURA 已 LIVE，不新建卡）；UF2 见 @wiseguyzRH / @globemkts / @kairo_market（均已在库）；UF3=0。本片无真新官号。
- 十栏关键词: 是。核心栏（打新 / 挖矿 / 台子/Meme / GO盘 / Elysium）近 30 分钟 + KW_GAPS 专名补漏；瘦栏 6 组先跑 30 分钟。
- 瘦栏 24h 补搜: 是（仅 LayerZero=0、GIWA=1、BTC=2、Starknet=2 各多 1 次 24h）。Tape 30m=6、DogeEVM 30m=7（≥5）未拉长。未把全部关键词改成 24h。挖矿 30m=0 但属肥/核心栏，未改 24h。
- MUST 官号：@mobster_meme @machinedotfun @bscaidrop @PulseLaunchpad @localbottomcom @NutshellMarkets @starx_xlayer + 窗口号 @KToonsNFT @RobinYieldRH @Hooddrivee @Kismonft @mercesdotlive @RuninAI_com @kangozro 等。本窗仅 @RuninAI_com 仍预热「mine is coming」与 @kangozro 同一已报免费 WL 号召。MUST 有 next_token 但仅 12 帖（RuninAI 11 + kangozro 1），未额外翻页。
- MUST_TAPEAI：本轮另核 from:TapeAIAgent OR from:tapeupio 近 16h = 0。TAI 仍称 11-21 经 TapeUP PoB 上线、开窗时刻 TBA（R2022 已提醒），未见新的官方开盘时刻，不重推。
- mentions: 轮换子集 24h：squeek+Nutshell（0）、BN Agent pads+STARX（17）、LayerZero（25 触顶，未翻页）。下轮 Tape / GIWA。
- silentAccounts.ran: true（lane=Tape/电路，search_users 不可用，仅 SILENT_MEN 1 读=7，未见未入库可收录官号）。silentNext: GIWA（Tape/电路已跑完，勿按轮次取模跳步）。
- thinOfficial: 否（为给瘦栏 24h KW 留额度而延期，RESULT 标明 deferred）。
- Discord Peek: deferred=true。computerUse 08:37 CST 遇登录墙（Welcome back / Email or Phone Number / Log In / QR / passkey），landed `https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302`。loginOk=false，未填凭据。4 频道均未打开，cards=0。lastSeen 未改：alpha-3 07:59 / backup 06:59 / smart 08:00 / alpha-1 07:45 CST。11/15–11/18 积压仍未清，不在增量范围。须父代理同一轮补增量 Peek。

## 新收录
- **SleeperDragons**（@SleeperDragons，无官网），来源 KW_THIN_BTC，DeepSeek admit=true、overall=37（early 88 / actionable 20 / novelty 58 / risk 82）。官号 2026-11-18 13:37 CST 建，本轮 6 粉、82 帖（xUserId 2122926872547766272）。资料栏自称 1,024 eggs sleeping on Bitcoin，Hatch when you choose; a future block picks your dragon. Not even we can peek。Wake the Hoard · Jan 20。供应与 Jan 20 写在官号资料栏，不只是第三方转述；@EDKbtc_ 亦称 incoming on bitcoin、supply 1024、mint probably Jan 20。无官网无合约，置顶帖已 404。本轮只见到一条回复（08:21:33 CST，https://x.com/SleeperDragons/status/2123934808351113293，讨论 ShieldedNaka 类 public art / private owner），未见自己的开铸或登记官帖。不是免费 mint LIVE，只宜观察。已进 btcPrivacyWatch + userFollowWatch，focus=false。本号不自动 mint。

## 看见但未新收（不重推）
- @drachenfly / DRACHEN：已在库 whitelist-open，本窗仅见第三方 RT「APPLICATION IS LIVE」（供应 2026、ETH、Mint TBA、GTD Free），不是新卡。
- @anipalsonsol：已在 UF 分片，AniPals/AURA 已 LIVE，不新建卡。
- @kangozro：同已提醒的免费 WL 号召，不是新开铸 LIVE。
- @RuninAI_com：仍在预热 mine / one-click launch coming，未宣布已开窗。
- @PandalZero、@soomdotfun、@silicube、@rezofun、@layerfee、@t0dotfun、@ammorahq、@vorda、@plunderport、@hypesium、@tapeai / @tapeupio、@ptah-trade、@buzzchain、@mmix-districts、@lawoftheabyss、@hooja-fun、@tribe3tech、@quoted-xyz、@spike-wtf、@escape_hub 等短名单均为库内续更，无新的首次可操作窗口。
- @FarmerUnionXRPL：2025-04 建号、约 2660 粉，XRPL 社区「PROOF OF HAIR」持仓免费 mint，非极早期，未送审、未建卡。
- @wormwtf：2024 年已验证 Solana 杠杆预测市场（约 2.2 万粉），非早期，未建卡。
- @watzenweb3：个人 builder 在 GIWA 上提交 Ammora SDK 任务（Moralume），不是新官号项目，未建卡。
- Buzzchain 测试网：仅见第三方教程，未见本轮官号宣布，不改已收录卡状态、不重推。
- TapeAI TAI：近 16h 官号 0 帖，开窗时刻仍 TBA，R2022 已提醒，不重推。

## 窗口刷新
- Kismo Seekers：Whitelist Phase II 报名页已关闭（页文 “The Whitelist Applications are closed for now.”）。/api/gen-wl 仍返回 open=true、phase=2，与页面不一致，以页面为准。Genesis 仍写 Mint opens · date coming soon，开铸与合约仍 TBA，不是免费 mint LIVE。此为关闭事件，需提醒；不再把 08:31:58 CST 当作仍开放的 le2h。
- Kinetiq Toons：OpenSea 合集供应仍 584、持有 449、地板 0.0087 HYPE。MUST 未见第二则关窗确认官帖。不重推。
- Robin Yield：公售仍 LIVE。OpenSea 供应 404、持有 151、地板 0.00005 ETH。R2045 已提醒，不重推。
- Hood Drive：官网仍 WL Closed，开铸仍 2026-11-22 01:00 CST（约 16.27h，le2h=false），OpenSea hood-drive 供应 0。不重推。
- Merces / RuninAI / Soneium Punks：无新开窗，不重推。

## Watch / 漏挂
- 新卡 sleeperdragons 入库同时挂 btcPrivacyWatch + userFollowWatch。
- 本轮未做历史旧卡整库补挂。
- 软债：cantonWatch / cantonPadWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch lastChecked 已刷新为本轮时间。

## 下轮
- UF 从 1233 @KyrosElysium 继续。
- mentions: 轮换子集 Tape / GIWA。
- silent: GIWA（Tape/电路本轮已跑完，勿按轮次取模跳步）。
- thinOfficial 本轮延期，额度仍 ample 时可补。
- Discord：本路 deferred=true，须同一轮由父代理补增量 Peek（cutoff 仍为 alpha-3 07:59 / backup 06:59 / smart 08:00 / alpha-1 07:45 CST）。11/15–11/18 积压仍待专门清理，不在增量范围。
