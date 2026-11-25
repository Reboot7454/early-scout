# RESULT R2180

- 轮次：R2180（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 13:00–13:13 CST（Asia/Shanghai）。正式写盘 lastScout=2026-11-25 13:14:44 CST（dry-run 曾为 13:13:17 CST）。
- mode=ample；softCap=28；minSpend=20；silentCap=2（silent 不计 softCap）
- xReads=27（main 26 + silent 1），未超 softCap，不低于 minSpend
- remainingBefore=721 / 1000（第一笔 X 工具结果 remainingToday=720，+1）；remainingAfter=694（最后一笔 SILENT_PAD remainingToday=694）
- Judgment / admit / score：DeepSeek（deepseek-flash，thinking on）；dsFallback=false
- 本号不自动 mint。未 commit / push，未改 /workspace/early-scout/data.json。dry-run 写在 /tmp/r2180/data.json。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=2，KW_TAPE=25，KW_GIWA=6，KW_DOGE=6，KW_BTC=1，KW_STARK=1
  - KW_MINT=25，KW_MINE=1，KW_PAD=25，KW_GO=25，KW_ELY=5，KW_GAPS=13
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=20、KW_BTC_24=25、KW_STARK_24=25
- 未把厚栏改成 24h：TAPE/GIWA/DOGE 30m 已 ≥5；MINT/PAD/GO 已触顶，不转 24h。MINE=1 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1061 @Vigil_elysium 起 50 号至 @husherdotfun，next 1111 @BitRushBTCB，wrap=false，total=2384。ufOnlyFrom=50，mustOverlap=0（@PlatoUnseen 只放进 UF from:，未再进 MUST），skippedNF=[]。三批均为 0 帖。
- MUST_WIN 24h 两批（含 R2179 新收 @useatlaspad / @Basketdotxyz）+ MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=6。
- Mentions 24h 本轮：DogeEVM / BTC / Starknet / squeek / STARX（已去掉本轮已 from: 读过的官号；@starx_xlayer 仅做 mentions）。
  - MEN_DOGE=4（dropped from: @DogeOS）
  - MEN_BTC=25 触顶（dropped @ShieldedNaka / @ShieldedWizBTC / @crest_btc / @RGB_Stone）
  - MEN_STARK=0（dropped @Starknet）
  - MEN_SQUEEK=0（dropped @squeekchain / @NutshellMarkets）
  - MEN_STARX=0
- mentionsNext：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- 无额外探索性 X 读取。

## 静号

- silentAccounts.ran=true；lane=台子/Meme；next=GO盘
- search_users 不可用；fallback 一次 24h SILENT_PAD（has:mentions has:links + 该栏 mentionQuery 词，不占 softCap）
- hits=25 触顶；seen=24 作者（已知 1=@useatlaspad，未知 23）；sentToReview=[]；admitted=[]
- 看见但未送审：@velmarstocks（股票代币只读看板，R2178 DeepSeek admit=false overall=36，本轮官网仍写 $VELMAR Soon、无 CA，不重收）；@aripintujg（个人 Ammora/GIWA Sepolia 演示，链接 muse.ai 视频，不收）。其余多为新闻号/KOL/旧号或发射台无关转帖。

## 新收录

无。newThisRound=[]，未建新卡，无新 Watch 挂钩。

送审 1 项，DeepSeek admit=false：

- Pixel Puddings（@PixelPuddingsRH）：建号 2026-11-14 15:34:39 CST（约 10.9 天），130 粉 / 166 帖。简介自称 3000 Cute Pixel Puddings coming soon，Robinhood Chain。OpenSea https://opensea.io/collection/pixel-puddings 回链官推（siteXMutual=opensea-yes），本轮 Supply 0 / Owners 0。白名单页 https://pixel-puddings-whitelist-checker.pages.dev/ 只查询已上传名单（“A SWEET LITTLE MINT IS COMING”），不是开放免费登记，无价格、无开铸时间、无 CA。本轮仅见 12:43:08 CST Gm 帖，不是开铸公告。DeepSeek overall=43，actionable=20，admit=false。focus 未设。不收录。

## 库内动态（不重推）

- 真实 LE2H=0。The Jacket 仍 2026-11-25 18:00 CST（10:00 UTC），约 16:00 CST 才进 2h，尚未进入。ORIPA 首包仍 20:00 CST（官帖 10:00 CST 称还剩 10 hours，与既定窗口一致）。Ugly Puggies 公开仍 21:00 CST（13:00 UTC）；官帖称 first wl batch has been added，不是改期/开铸。2hour.fun 官帖确认 Reservations are OPEN，第一场窗口 Today at 21:00 UTC = 2026-11-26 05:00 CST，不要按今天 21:00 CST 告警。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。公共 BSC RPC（https://bsc-dataseed.binance.org/，约 2026-11-25 13:02:30 CST）309/3333（R2179 为 304/3333），nftMintPaused=false。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=1；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，付费阶梯未开，未见 CA，不重推。
- AtlasPad / Basket：刚在 R2179 收录。AtlasPad 本轮继续发文档/空投分成/Agentic Hook 设想，未见真正开盘或免费铸。Basket 12:43 CST 称用 Streamflow 锁定 67,642,871 $BASKET（锁仓合约 CYQBAXkp2mCDonYqHanbxqrFcyoUkEwy2g6HHBPUEMM，解锁 2027-06-07 13:00 CST），本轮仍未独立核到完整 token mint CA，官网仍写 CA soon，不是免费 mint，不重推。
- Sparecycle 称已在 @HeyResearch 列为 Verified Builder、合约已验证，不是免费 mint，不重推。
- Thinkers Club / Shit Capital / Flame-BTC：付费公开仍 LIVE，不重推。DAEMONS 仍是 waitlist / 主网约 12 月。ANKOU 日期仍 TBA。Z3RO 测试网。SPCX 发射台 beta 仍无代币发射。Vicehood 已在库，不按新登记重推。

## 看见但未收录

- @4omolife / https://4omo.life：BNB Chain Agent ID 叙事，官网仅 Hello World 占位；官帖明确写 Genesis Mint 界面是测试数据、不是 live launch。未送审。
- @CadaCasoxLayer：TapeOut / X Layer 法律电路工具（https://1-2-426.tapekit.org/），查询验证免费，不是 mint/发射台。未送审。
- @velmarstocks、@aripintujg：见静号。
- 已在库提及：@StinkyPenguinL0、@MMIX_io、@LawoftheAbyss、@PetroCraniums、@GAMA_GIWA 等，不重收。第三方转帖不作为 PetroCraniums 改期/开铸依据。

## Discord Peek

- 父进程并行 computerUse 已写出 /tmp/r2180/discord_peek.json（attemptedAt=2026-11-25 13:01:13 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道后被重定向到 Discord 登录墙（Welcome back / Email or Phone Number / Password / Log In / QR / passkey / Register）。未输入凭据、未登录。四频道均未翻，lastSeen 仍约 2026-11-23 22:19–22:56 CST，积压仍在。
- apply dry-run 已按该 JSON 写入 discordPeekDeferred=true。若父进程还有更新，可再合并。

## 失败 / 备注

- dsFallback=false。X 搜索 27/27 无解析错误。
- UF2/UF3 的 remainingToday 因并行完成顺序不是严格递减，但首笔+1 与末笔 live remaining 已用于 remainingBefore/After。
- apply_r2180.py：默认拒绝写 /workspace/early-scout/data.json；APPLY_DRY_RUN=1 + EARLY_SCOUT_DATA=/tmp/r2180/data.json.src + APPLY_DRY_OUT=/tmp/r2180/data.json 通过。workspace data.json sha256 未变，git 工作区无本轮改动。
- notify=false：无新收录，没有需要点名的免费 LIVE / 免费 mint / 免费登记；库内变化未达重推门槛。
