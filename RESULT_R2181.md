# RESULT R2181

- 轮次：R2181（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 13:37–13:52 CST（Asia/Shanghai）。apply dry-run lastScout=2026-11-25 13:52:41 CST。
- mode=ample；softCap=28；minSpend=20；silentCap=2（silent 不计 softCap）
- xReads=26（main 25 + silent 1），未超 softCap，不低于 minSpend
- remainingBefore=694 / 1000（第一笔 X 工具结果 remainingToday=693，+1）；remainingAfter=668（live 最小值，来自 KW_STARK_24 remainingToday=668；并行完成使 SILENT_GO 报 671，不以之为 after）
- Judgment / admit / score：DeepSeek（deepseek-flash，thinking on）本轮无需送审，未调用；dsFallback=false
- 本号不自动 mint。未 commit / push，未改 /workspace/early-scout/data.json。dry-run 写在 /tmp/r2181/data.json。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=1，KW_TAPE=25，KW_GIWA=25，KW_DOGE=13，KW_BTC=1，KW_STARK=1
  - KW_MINT=25，KW_MINE=1，KW_PAD=25，KW_GO=25，KW_ELY=7，KW_GAPS=20
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=21、KW_BTC_24=25、KW_STARK_24=25
- 未把厚栏改成 24h：TAPE/GIWA/DOGE 30m 已 ≥5（25/25/13）；MINT/PAD/GO 已触顶或为厚栏，不转 24h。MINE=1 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2（无 UF3），cursor 1111 @BitRushBTCB 起 50 号至 @megalith_agent，next 1161 @digent_coin，wrap=false，total=2384。ufOnlyFrom=49，mustOverlap=0，skippedNF=[Haltercard]。UF1=0 帖，UF2=3 帖（均为已在库 @qHooks_ 产品更新）。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF，未连刷）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=0。
- Mentions 24h 本轮：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest。
  - MEN_PADS=3
  - MEN_GIWA=25 触顶
  - MEN_TAPE=19
  - MEN_LZ=25 触顶
  - MEN_ELY=24
- mentionsNext：DogeEVM / BTC / Starknet / squeek / STARX
- 无额外探索性 X 读取。规划搜索各跑一次，无同查询重试。

## 静号

- silentAccounts.ran=true；lane=GO盘；next=LayerZero
- search_users 不可用；fallback 一次 SILENT_GO（不占 softCap）
- hits=0；seen=0；sentToReview=[]；admitted=[]；skipped=[]

## 新收录

无。newThisRound=[]，未建新卡，无新 Watch 挂钩。未向 DeepSeek 送审（未见真实早期/可行动新项目）。

## 库内动态（不重推）

- 真实 LE2H=0。The Jacket 仍 2026-11-25 18:00 CST（10:00 UTC），约 16:00 CST 才进 2h，尚未进入。ORIPA 首包仍 20:00 CST（本轮仍可见「10 hours left」旧官帖，与既定窗口一致）。Ugly Puggies 公开仍 21:00 CST（13:00 UTC），不是改期/开铸。2hour.fun Reservations are OPEN，第一场窗口仍是 Today at 21:00 UTC = 2026-11-26 05:00 CST，不要按今天 21:00 CST 告警。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。公共 BSC RPC（https://bsc-dataseed.binance.org/，约 2026-11-25 13:38:23 CST）322/3333（R2180 为 309/3333），nftMintPaused=false。官帖 13:21 CST（https://x.com/TriForgeAgent/status/2125459910116987261 ）报 311/3333，随后链上继续小幅增加。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=1；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。本号不自动 mint。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，付费阶梯未开，未见 CA，不重推。
- AtlasPad：官号继续密集更新文档、图表、持有人分成、$ATLASPAD / LayerZero OFT 桥、Buyback and Burn 与 Agentic Hook / perpetual 设想（如 13:06 CST https://x.com/useatlaspad/status/2125456162258849961 ，13:23 CST https://x.com/useatlaspad/status/2125460405392973875 ）。资料栏 CA 仍是 0xa7145870a49036a485696315ba071bbae17c33b8。未见已真正开盘或免费铸，不重推。
- Basket：从既有官帖 12:39 CST 长文（https://x.com/Basketdotxyz/status/2125449223801811336 ）补到完整 token mint CA 3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f。官号继续发配对/分红说明并重复锁仓 67,642,871 $BASKET（Streamflow CYQBAXkp2mCDonYqHanbxqrFcyoUkEwy2g6HHBPUEMM）。这是同一则已在 R2179/R2180 跟踪的 live 官帖补全 CA，不是新开盘或免费铸，不重推。卡片已写入该 CA。
- Sparecycle 称已在 @HeyResearch 列为 Verified Builder、合约已验证，不是免费 mint，不重推。
- Shit Capital Genesis 付费公售仍 LIVE（官帖称已超募、还剩约 44 小时），不重推。DAEMONS 仍是 waitlist / 主网约圣诞节前，免费铸仅对成员，不是已开铸 LIVE。Agent Cards 第三方帖称「TODAY IS THE DAY / 10 hours before mint」（约 13:37 CST），官方窗口仍 23:00 CST，本轮尚未进入 2 小时，不按第三方改期或提前告警。

## 看见但未收录

- @ninedragons_rtc / https://9dragons.pages.dev（跳转 https://9dragons.shop）：建号约 10.08 天，37 粉 / 1 帖。官帖（2121824860494242285）称 3,333 份动画交易卡将于 Nov 20 在 Robinhood Chain 铸造，仅限 Agent ID 持有人，GTD Phase 1 白名单，$RTC。铸造日已是 2026-11-20（约 5 天前）。本轮未见新官帖（仅见该旧公告的转帖）。官网为大型内联 SPA/图片页，静态 HTML 未能核到剩余供应或是否仍 LIVE，故不按免费 mint LIVE 收录，亦未送审。
- @ponsbot_ai：2026-11-25 12:57 CST 新建号，0 粉 / 1 帖，资料栏无官网。推文截断为 “Live on the web now: Launch a token on Pons…”。t.co 链接只回到推文本身，未核到独立官网。证据过薄，未送审，不收录。
- @anvoraapp / https://anvora.vercel.app：简介与帖文明确写 testnet，由 @kriptokolik58 用 Ammora SDK 搭建，不收。
- @OUTLAWSxNFT：旧号（2022-12-19 建号，约 4979 粉），简介写 Free Mint on OpenSea • Nov 27 | 1:30 PM UTC（即 2026-11-27 21:30 CST），不是早期新号，不收。
- @tinylegendsfun：约 439 天、5024 粉，本轮仅为第三方 Nativ3 日历转述，不是早期官宣，不收。
- @aripintujg、@szymansk68、@abdo_mahmoud_7：GIWA Sepolia / Ammora SDK 演示（@aripintujg 已在 R2180 静号跳过），不收。
- @NoctiqAI：API 产品，不是 mint。
- @tailtradesxyz：交易台，CA 已上线，不是免费 mint。
- @CadaCasoxLayer：R2180 已见，TapeOut / X Layer 工具，不是 mint。
- @Pax_Gothamista：旧号，第三方白名单转述，不收。
- Pixel Puddings（@PixelPuddingsRH）：本轮无实质新证据（R2180 DeepSeek admit=false overall=43），不重收、未再送审。

## Discord Peek

- 父进程并行 computerUse 已写出 /tmp/r2181/discord_peek.json（attemptedAt=2026-11-25 13:37:59 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道后被重定向到 Discord 登录墙（Welcome back / Email or Phone Number / Password / Log In / QR / passkey / Register）。未输入凭据、未登录。四频道均未翻，lastSeen 仍约 2026-11-23 22:19–22:56 CST，积压仍在。
- apply dry-run 已按该 JSON 写入 discordPeekDeferred=true。若父进程还有更新，可再合并。

## 失败 / 备注

- dsFallback=false。X 搜索 26/26 无解析错误（ingest errors=[]）。
- 薄栏 24h 与 SILENT_GO 因并行完成，remainingToday 不是严格按 ORDER 递减，但首笔+1 与全部 live remaining 的最小值已用于 remainingBefore/After。
- 部分大体量搜索结果被写入 local preview / asset 文件；MUST_WIN / MUST_WIN2 / KW_DOGE / KW_ELY / KW_MINE / MEN_PADS / KW_LZ_24 等未落盘的 inline 结果已重建到 /tmp/r2181/x_local_previews/，未重查同一 query。
- apply_r2181.py：默认拒绝写 /workspace/early-scout/data.json；APPLY_DRY_RUN=1 + EARLY_SCOUT_DATA=/tmp/r2181/data.json.src + APPLY_DRY_OUT=/tmp/r2181/data.json 通过。workspace data.json sha256 未变（62e8e049f02943d27c342545de6bd3747a210454d7d8e480feab29d0d5a22787），git 工作区无本轮改动（仍仅有既有未跟踪文件 r2148_discord_peek.json）。
- notify=false：无新收录，没有需要点名的免费 LIVE / 免费 mint / 免费登记；库内变化未达重推门槛。
