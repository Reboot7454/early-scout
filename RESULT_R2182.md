# RESULT R2182

- 轮次：R2182（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 14:02–14:15 CST（Asia/Shanghai）。apply dry-run lastScout=2026-11-25 14:15:09 CST。
- mode=ample；softCap=28；minSpend=20；silentCap=2（silent 不计 softCap）
- xReads=27（main 26 + silent 1），未超 softCap，不低于 minSpend
- remainingBefore=668 / 1000（第一笔 X 工具结果 remainingToday=667，+1）；remainingAfter=641（SILENT_LZ 之后又跑 3 次薄栏 24h，末笔 KW_STARK_24 remainingToday=641；668−27=641，与 live 一致）
- Judgment / admit / score：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score，送审 2 项，均 admit；dsFallback=false
- 本号不自动 mint。未 commit / push，未改 /workspace/early-scout/data.json。dry-run 写在 /tmp/r2182/data.json。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=0，KW_TAPE=25，KW_GIWA=15，KW_DOGE=5，KW_BTC=0，KW_STARK=0
  - KW_MINT=25，KW_MINE=3，KW_PAD=25，KW_GO=23，KW_ELY=9，KW_GAPS=17
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=21、KW_BTC_24=25、KW_STARK_24=25
- 未把厚栏改成 24h：TAPE/GIWA/DOGE 30m 已 ≥5（25/15/5）；MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=3 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1161 @digent_coin 起 50 号至 @ironshotgame，next 1211 @kairo_market，wrap=false，total 写盘后=2386（原 2384 + 本轮 2 个新收录挂入 UF）。ufOnlyFrom=50，mustOverlap=0，skippedNF=[]。UF1=0 帖，UF2=1 帖（已在 UF 名单的 @PairMineAI 产品回复），UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷；mentions of @starx_xlayer 在本轮 MEN_STARX）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=1。
- Mentions 24h 本轮：DogeEVM / BTC / Starknet / squeek / STARX。
  - MEN_DOGE=4
  - MEN_BTC=25 触顶
  - MEN_STARK=0
  - MEN_SQUEEK=0
  - MEN_STARX=0
- mentionsNext：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_LZ）各跑一次，另加 3 次正当薄栏 24h，无同查询重试。

## 静号

- silentAccounts.ran=true；lane=LayerZero；next=Elysium
- search_users 不可用；fallback 一次 SILENT_LZ（不占 softCap）
- hits=9；seen=9；sentToReview=[]；admitted=[]；skipped=[jackqwe88800, globemkts, perptools]（第三方/策展，未见需新收录的早期官号）

## 新收录

2 项，已同时挂 Watch（focus=false）。

1. **SYMPHONY（$OPUS）** @symphonyopus / https://symphony-opus.pages.dev  
   - 建号 2026-11-22 14:33 CST，本轮 5 粉 / 31 帖。官网与官推互证。  
   - 面向 Binance Agent ID 持有人的社区公平发射（BNB Chain）。Prelude 免费登记（仅 gas）已链上 LIVE，至 2026-12-12 20:00 CST（12 Dec 2026 12:00 UTC）。Soundcheck 每日免费签到合约已部署。付费 Pass 销售计划 2026-12-12 至 2026-12-30（1/1.5/2 USDT），本轮未见 Sale 合约。  
   - 官帖 13:54 CST：https://x.com/symphonyopus/status/2125468121989521454 、https://x.com/symphonyopus/status/2125468051562975373  
   - 公共 BSC RPC（https://bsc-dataseed.binance.org/）核到：PreludeRegistry `0xeA2FC84d8B87cB8CbCd27bda65761625BB7dB678` 有代码，count()=234，registrationEnd=2026-12-12 20:00 CST，MIN_REGISTRANTS=500，name=SYMPHONY Prelude Pass，registry=`0x60B9262456dE011F7d15a54CdD8c48bAaa8B022F`；Soundcheck `0xf29BB5C9266e4bD829be23cC9878e241fb85DD71`；TreasuryVault `0x4d32E4a76C7389445F9CB76f7098E4D50E0503A7`。config.js 仍留过时 “PHASE 1 — NOT DEPLOYED YET” 注释，以链上有代码和 count=234 为准。  
   - DeepSeek overall=78，admit=true。**免费登记 LIVE，须点名。不是已开铸的免费 mint LIVE。** 已挂 userFollowWatch + bnAgentWatch + freeMintWatch。本号不自动 mint。

2. **Azuke Pad** @AzukePad / https://azuke.xyz/  
   - 建号 2026-11-18 14:39 CST，本轮 46 粉 / 7 帖。官网与官推互证。  
   - 官帖 13:57 CST（https://x.com/AzukePad/status/2125468832328487147 ）称 pump.fun 发射台已 LIVE（持有越久、每 10 分钟 SOL 手续费分成倍率越高，最高 10x；DEX at 30k）。自有代币 $AZUKE 资料栏与官网均写 CA `GQVZsQToSWPgkjtgLyGZoQiCLkYjvr2ieFr6g4nLpump`（本轮未另做链上核验）。官网当时显示约 4 个已上浪潮的币、约 55 持有人、已返还约 0.541 SOL（页面数字可能变动）。  
   - DeepSeek overall=60，admit=true。**不是免费 mint / 免费登记。** 已挂 userFollowWatch + agentPadWatch。本号不自动 mint。

## 库内动态（不重推）

- 真实 LE2H=0。The Jacket 仍 2026-11-25 18:00 CST（10:00 UTC），约 16:00 CST 才进 2h，尚未进入。ORIPA 首包仍 20:00 CST（本轮仍可见「10 hours left」旧官帖，与既定窗口一致，约 18:00 CST 才进 2h）。Ugly Puggies 公开仍 21:00 CST（13:00 UTC），本轮仍只有 first wl batch 已添加的旧官帖，不是改期/开铸。2hour.fun 本轮仍可见同一则 Reservations are OPEN 官帖（https://x.com/2hourfun/status/2125409666502930693 ），第一场窗口仍是 Today at 21:00 UTC = 2026-11-26 05:00 CST，不要按今天 21:00 CST 告警。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。公共 BSC RPC（https://bsc-dataseed.binance.org/，约 2026-11-25 14:06:15 CST）330/3333（R2181 为 322/3333，R2180 为 309/3333），nftMintPaused=false。本轮 MUST 仍可见 13:21 CST 报 311/3333 的旧官帖（https://x.com/TriForgeAgent/status/2125459910116987261 ）。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=1；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。本号不自动 mint。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，付费阶梯未开，未见 CA，不重推。
- AtlasPad：继续密集更新产品，另有回复 “we go live on the 30th”（https://x.com/useatlaspad/status/2125467224815317111 ），只是对询问的简短回复，不是已开盘或免费铸官宣，不按改期重推。
- Basket：继续介绍配对/分红，完整 CA 仍是 R2181 已补的 `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f`，不是新开盘或免费铸，不重推。
- SPCX / Amend / NoPvP / Sparecycle 等有产品更新，均非免费 mint，无实质开铸/改期，不重推。
- Thinkers Club / Shit Capital / Flame-BTC：付费公开仍 LIVE，不重推。Shit Capital 官帖称 Genesis sale 约 44 小时后关闭，不是免费铸。
- DAEMONS：waitlist 仍开、免费 mint 仅 members、主网约圣诞，不是已开铸 LIVE。ANKOU / Z3RO Terminal 无新日期或主网开铸。

## 看见但未收

- @LongyuNetwork（https://longyu.network）：建号 2026-11-21 14:12 CST，1407 粉 / 仅 3 帖（粉帖比异常），自称可挖矿的 BNB Chain L2 已 mainnet。本轮只有第三方提及，未见官帖，未送审、不收。
- @BitnetMoney：11 日号，1 粉 / 228 帖，自称 GPU 可挖的 Ethash L1，更像刷量号，不收。
- @CadaCasoxLayer：R2180 已见，TapeOut / X Layer 工具，不是 mint，不重收。
- @ninedragons_rtc、@anvoraapp：R2181 已见未收，本轮无实质新证据，不重收、未再送审。
- Pixel Puddings（@PixelPuddingsRH）：本轮无实质新证据（R2180 DeepSeek admit=false overall=43），不重收。
- @ponsbot_ai、@OUTLAWSxNFT、@tinylegendsfun：无足以改判的新证据，不重收。

## Discord Peek

- 父进程并行 computerUse 已写出 /tmp/r2182/discord_peek.json（attemptedAt=2026-11-25 14:03:54 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone Number / Password / Log In / QR / passkey / Register）。未输入凭据、未登录。四频道均未翻，lastSeen 仍约 2026-11-23 22:19–22:56 CST，积压仍在。
- apply dry-run 已按该 JSON 写入 discordPeekDeferred=true。若父进程还有更新，可再合并。

## 失败 / 备注

- dsFallback=false。X 搜索 27/27 无解析错误（ingest errors=[]）。部分大体量搜索结果先落到 preview/asset 文件，已用 Full text 路径还原后写入 /tmp/r2182/x_raw/{id}.json，未重查同一 query。
- apply_r2182.py：默认拒绝写 /workspace/early-scout/data.json；APPLY_DRY_RUN=1 + EARLY_SCOUT_DATA=/tmp/r2182/data.json.src + APPLY_DRY_OUT=/tmp/r2182/data.json 通过。workspace data.json sha256 未变（82f7dc39b02643c3ca48f19e8b8f0f34eb27a80db11ad959fa9d4612da6e7c5d）。
- notify=true：新收录须提醒，并点名 SYMPHONY（免费登记 LIVE，不是免费 mint LIVE）与 Azuke Pad（发射台 LIVE，非免费 mint）。库内 TRIFORGE 小幅进度及其他窗口未达重推门槛。

