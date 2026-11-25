# RESULT R2184

- 轮次：R2184（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 15:08–15:18 CST（Asia/Shanghai）。apply dry-run lastScout=2026-11-25 15:18:36 CST。
- mode=ample；softCap=28；minSpend=20；silentCap=2（silent 不计 softCap）
- xReads=27（main 26 + silent 1），未超 softCap，不低于 minSpend
- remainingBefore=614 / 1000（第一笔 X 工具结果 remainingToday=613，+1）；remainingAfter=587（末笔 KW_STARK_24 remainingToday=587；614−27=587，与 live 一致）
- Judgment / admit / score：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score，送审 2 项（@gAntsbsc、@MergedSite），两项均新收录。dsFallback=false
- 本号不自动 mint。已把 dry-run 写盘到仓库 data.json（lastScout=2026-11-25 15:18:36 CST）并准备推送 data.json + RESULT_R2184.md。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=1，KW_TAPE=25，KW_GIWA=22，KW_DOGE=12，KW_BTC=0，KW_STARK=3
  - KW_MINT=25，KW_MINE=3，KW_PAD=25，KW_GO=25，KW_ELY=8，KW_GAPS=11
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=20、KW_BTC_24=25、KW_STARK_24=25
- 未把厚栏改成 24h：TAPE/GIWA/DOGE 30m 已 ≥5（25/22/12）；MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=3 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1261 @nouns_elysium 起 50 号至 @useproteus，next 1311 @candlebugely，wrap=false，total 写盘后=2390（原 2388 + 本轮 2 个新收录 @gAntsbsc、@MergedSite）。ufOnlyFrom=50，mustOverlap=0，skippedNF=[]。UF1=1 帖（已在 UF 名单的 @returntotimmy 回复 “Real”），UF2=0 帖，UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷；本轮 mentions 含 MEN_STARX，这是正确的，没有再 from: 读 @starx_xlayer）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=20。
- Mentions 24h 本轮：DogeEVM / BTC / Starknet / squeek / STARX。
  - MEN_DOGE=4
  - MEN_BTC=25 触顶
  - MEN_STARK=0
  - MEN_SQUEEK=0
  - MEN_STARX=0
- mentionsNext：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_TAPE）各跑一次，另加 3 次正当薄栏 24h，无同查询重试。

## 静号

- silentAccounts.ran=true；lane=Tape/电路；next=GIWA
- search_users 不可用；fallback 一次 SILENT_TAPE（不占 softCap）
- hits=0；seen=0；sentToReview=[]；admitted=[]；skipped=[]

## 新收录

2 项，已同时挂 Watch（focus=false）。均**不是免费 mint / 免费登记**。

1. **gAnts** @gAntsbsc / https://genius.fun/token/0x16c12e4c7ebbf09277013E90e7Fe820C93232709  
   - 建号 2026-11-25 15:02:36 CST，本轮 0 粉 / 2 帖。官帖 15:07:44 CST（https://x.com/gAntsbsc/status/2125486578881458323 ）称 The agent colony is opening on genius.fun，持 .ai Agent ID 且持 $gANTS 可自动孵化成工蚁（No form, no claim, no gas）。资料栏发帖时仍写 CA: TBA。  
   - 官网 token 页回链 @gAntsbsc 及该官帖，site-X 互证成立。约 15:15 CST 抓到的 token 页：Trading on curve，Progress 6.77%，Market cap (FDV) $3.8K，Price $0.000003800836736129，Supply 998.91M（另写 Tokens burned 1087781.267…），Holders 14，Reserved 285.71M，Total trading fee 2%（Creator 1.25% + Genius platform 0.5% + Meme buyback 0.25%）。Token CA `0x16c12e4c7ebbf09277013E90e7Fe820C93232709`，Curve `0x22a7d09a5880B29819C53Ec71f822D9018d9631F`，Creator `0x17cfE7b7Ba010F4396d6306e354bF32e7f61622e`。genius.fun 列表 JSON 写 launched_at=2026-11-25 15:08:27 CST，phase=NotGraduated，pair=GENIUS，verified=false。https://gants.fun/ 本轮 HTTP 410 Gone，不能当作可用官网。  
   - DeepSeek overall=62，admit=true。已挂 userFollowWatch + bnAgentWatch。本号不自动 mint。

2. **Merged** @MergedSite / https://merged.site/  
   - 建号 2026-11-25 13:46:35 CST，本轮 18 粉 / 5 帖。资料栏指向官网。本轮未直接搜到其 from: 原帖，但 KW_GO 见到引用官帖 https://x.com/MergedSite/status/2125480036014649452（约 14:41:44 CST）：paste any public GitHub repo and launch its coin on @Pumpfun, paired to $merged，并给出 CA `AMYpNGi5aGrKr1ZDsotUdWh7k1mMi569ygtaHJmErGEd`。  
   - 官网 HTTPS 200，页脚写 x.com/mergedsite 且公布同一 CA，site-X 互证成立。官网自称 launches are open，抓取时可见 2 repos with a coin（$BYOX codecrafters-io/build-your-own-x、$anchor otter-sec/anchor）；文案写 80% of creator fees to devs（示例拆分 55% maintainer / 25% contributors pool / 20% merged），并称 fee split locked on chain。CA 来自官网与被引用官帖，本轮未另做独立链上核验。与库内 R371 Merged Finance（@MergedFinance_）不是同一官号/站点。  
   - DeepSeek overall=74，admit=true。已挂 userFollowWatch + agentPadWatch。本号不自动 mint。

## 库内动态（不重推）

- 真实 LE2H=0。The Jacket 仍 2026-11-25 18:00 CST（10:00 UTC），约 16:00 CST 才进 2h，本轮开火时尚未进入；MUST 未见其新官帖。ORIPA 首包仍 20:00 CST（本轮 24h MUST 仍可见「10 hours left」官帖 https://x.com/oripaxyz/status/2125409137127297404 ，与既定窗口一致，约 18:00 CST 才进 2h）。Ugly Puggies 公开仍 21:00 CST（13:00 UTC）；24h MUST 仍可见 09:35 CST first wl batch 已添加的官帖及 11:06 CST 回复 “see you there”，不是改期/开铸。2hour.fun 24h MUST 仍可见同一则 Reservations are OPEN 官帖（https://x.com/2hourfun/status/2125409666502930693 ），另有 Streamflow 锁仓说明及 07:46 CST 回复 “Launching tomorrow”；第一场窗口仍是 Today at 21:00 UTC = 2026-11-26 05:00 CST，不要按今天 21:00 CST 告警。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。公共 BSC RPC（https://bsc-dataseed.binance.org/，约 2026-11-25 15:12:04 CST）337/3333（R2183 为 332/3333，R2182 为 330/3333），nftMintPaused=false。本轮 MUST 未见新的 TriForge 官帖。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=2；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。本号不自动 mint。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，付费阶梯未开，未见 CA，不重推。
- Femeora @femeoraApp：R2183 已收录已通知，本轮 MUST 未见新官帖，无实质变化，不重推、不重收。
- Dogstarter（库内 R1828，status=testnet）：R2183 已更新新官号 @dogstarterhq，本轮 MUST 未见新官帖，仍为 DogeOS Chikyu Testnet，不重收、不重推。
- SYMPHONY @symphonyopus：R2182 已收录已通知。本轮 14:00 / 14:23 CST 继续宣传 Prelude 免费登记已开、付费 Sale 仍写 12 Dec（Sale opens 12 Dec），无实质变化，不重推、不重收。
- Azuke Pad @AzukePad：R2182 已收录已通知。本轮继续称 payouts live、已向持有人发放约 0.543 SOL（与 R2183 所见同一量级），并继续给 Solscan 凭证。仍不是免费 mint，无改期/新开铸，不重推。
- AtlasPad：14:53 CST 称又做了一次 Buyback And Burn（https://x.com/useatlaspad/status/2125482975613878658 ，并给 robin.etherscan 交易），另有 Bridge 页 ZRO / $ATLASPAD 开关等产品更新，不是已开盘或免费铸官宣，不按改期重推。
- Basket：官帖 14:06 CST 介绍的付费 NFT 铸（烧 100,000 $BASKET + 0.5 SOL）已在 R2183 见过，不是免费 mint，不重推。
- Shit Capital：24h MUST 见到 11:09 CST 官帖称 300%+ oversubscribed、Genesis sale closes in 44 hours，仍是已知付费公开，不重推。
- SPCX / Amend / Sparecycle / Flame-BTC 等有产品更新或旧的 Public mint is open 帖，均非新的免费 mint / 改期，不重推。Sparecycle 本轮称可无钱包试用（free trial: 5 images an hour），这是产品试用不是代币/NFT 免费铸。
- Thinkers Club 仅见回复互动。DAEMONS：09:00 CST 官帖重申 Before Christmas、waitlist open、free mint for members，不是已开铸 LIVE。ANKOU / Z3RO Terminal / The Jacket / QQAI / Lamoryant / Plato 无新日期或主网开铸。

## 看见但未收

- @SocialGruff（https://gruff.family/）：建号约 43 日、2007 粉 / 58 帖，自称 DogeOS 上的 Social Gruff。本轮只作为 KW_DOGE 的 includes 用户出现，没有其本身帖文，不是 mint/发射台窗口，未送审、不收。
- @CallPutApp（https://callput.app）：2025-11-20 建号、562 粉，GIWA / Robinhood Chain / Base 上的期权产品；本轮 14:39 CST 发 GIWA GASOK NIGHT 回顾，不是早期 mint/发射台，不收。
- @networkparallax：约 315 日号、4 万+ 粉，本轮只在他人转推里出现 “Parallax Network: Global Launch / mobile mining”，与库内 R1606 @ParallaxLaunch 不是同一官号，也已过极早期，不收。
- @OUTLAWSxNFT、@eutoprotocol、@tailtradesxyz、@PropsMintHQ、Pixel Puddings（@PixelPuddingsRH）、@LongyuNetwork、@BitnetMoney、@CadaCasoxLayer、@ninedragons_rtc、@ponsbot_ai、@anvoraapp、@tinylegendsfun：本轮无足以改判的新证据，不重收。

## Discord Peek

- 父进程并行 computerUse 已写出 /tmp/r2184/discord_peek.json（attemptedAt=2026-11-25 15:08:35 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone Number / Password / Log In / QR / passkey / Register）。未输入凭据、未登录。四频道均未翻，lastSeen 仍约 2026-11-23 22:19–22:56 CST，积压仍在。
- apply dry-run 已按该 JSON 写入 discordPeekDeferred=true。若父进程还有更新，可再合并。

## 失败 / 备注

- dsFallback=false。X 搜索 27/27 无解析错误（ingest errors=[]）。部分大体量搜索结果先落到 preview/asset 文件，已用 Full text 路径还原后写入 /tmp/r2184/x_raw/{id}.json，未重查同一 query。ingest_direct.py 的 ORDER 初稿仍是上一轮 mentions/silent id，已在本轮改正后重跑，x_usage 与 live remaining 一致。
- apply_r2184.py：默认拒绝写 /workspace/early-scout/data.json；APPLY_DRY_RUN=1 + EARLY_SCOUT_DATA=/tmp/r2184/data.json.src + APPLY_DRY_OUT=/tmp/r2184/data.json 通过。workspace data.json sha256 未变（3d752194e5d8cad2b8194f59ec25926747a322a81cc9622104c2f5092be96631）。
- notify=true：因新收录 gAnts 与 Merged（须逐个点名；都不是免费 mint / 免费登记）。TRIFORGE 小幅进度与既定窗口项目不重推。
