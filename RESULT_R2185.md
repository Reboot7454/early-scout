# RESULT R2185

- 轮次：R2185（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 15:34–15:50 CST（Asia/Shanghai）。开火 2026-11-25T07:34:34Z。
- mode=ample；softCap=28；minSpend=20；silentCap=2（silent 不计 softCap）。x_budget.py 在 remaining=586 时曾建议 pace/18，因 remaining≫200 且用户禁止额度充足时砍栏，本轮仍按完整增量执行。
- xReads=28（main 27 + silent 1），未低于 minSpend
- remainingBefore=587 / 1000（第一笔 UF1 remainingToday=586，+1）；remainingAfter=559（末笔 KW_STARK_24 remainingToday=559；587−28=559，与 live 一致）
- Judgment / admit / score：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score，送审 2 项（@Fulcrumius、@useClassified），两项均新收录。dsFallback=false
- 本号不自动 mint。notify=true（真新收录，均非免费 mint / 免费登记）。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=2，KW_TAPE=25，KW_GIWA=25，KW_DOGE=3，KW_BTC=3，KW_STARK=2
  - KW_MINT=25，KW_MINE=3，KW_PAD=25，KW_GO=25，KW_ELY=8，KW_GAPS=11
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=20、KW_DOGE_24=25、KW_BTC_24=25、KW_STARK_24=25
- 未把厚栏改成 24h：TAPE/GIWA 30m 已 ≥5（25/25）；MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=3 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1311 @candlebugely 起 50 号至 @usemorf，next 1361 @HypeWaveDeFi，wrap=false，total 写盘后=2392（原 2390 + 本轮 2 个新收录 @Fulcrumius、@useClassified）。ufOnlyFrom=50，mustOverlap=0，skippedNF=[]。UF1=0 帖，UF2=0 帖，UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷 from:）。MUST_WIN=25 触顶，MUST_WIN2=24，MUST_OFF=20。must_win 含 symphonyopus、AzukePad、femeoraApp、dogstarterhq、gAntsbsc、MergedSite。
- Mentions 24h 本轮：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest。
  - MEN_PADS=3
  - MEN_GIWA=25 触顶
  - MEN_TAPE=17
  - MEN_LZ=25 触顶
  - MEN_ELY=24
- mentionsNext：DogeEVM / BTC / Starknet / squeek / STARX
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_GIWA）各跑一次，另加 4 次正当薄栏 24h，无同查询重试。errors=[]。

## 静号

- silentAccounts.ran=true；lane=GIWA；next=DogeEVM
- search_users 不可用；fallback 一次 SILENT_GIWA（不占 softCap）
- hits=22；seen=22；sentToReview=[]；admitted=[]；skipped=[]（多为已库 Ammora 等互动，未见需新收的静号官号）

## 新收录

2 项，已同时挂 Watch（focus=false）。均**不是免费 mint / 免费登记**。

1. **Fulcrumius** @Fulcrumius / https://fulcrumius.xyz/  
   - 建号 2026-11-22 17:57:30 CST，本轮 66 粉 / 52 帖。资料栏指向官网。本轮未直接搜到 from: 原帖，但 KW_PAD 见到转发 https://x.com/solcapone1/status/2125494797272027469 ，文案为 The Fulcrumius Private Launchpad is live. Launch, trade and hold coins without your wallet on any of it。  
   - 官网 HTTPS 200，回链 https://x.com/Fulcrumius 与开发者 https://x.com/Synxneuos，site-X 互证成立。官网自称 Solana mainnet · pump.fun 的 bundle launcher + dividend/private launchpad：Block 0 最多 17 钱包原子 Jito bundle 建币+dev buy，Back MEV 自称最多 20 钱包。收费文案普通路径 Fee 2.5% flat；Dividend and private launchpads: no launch fee。登录支持 Google / Phantom / MetaMask。页面 $NOVA 等 Live trades 看起来像演示，本轮未独立核到已发射币清单或 $FUL 合约。  
   - DeepSeek overall=62，admit=true。已挂 userFollowWatch + agentPadWatch。本号不自动 mint。

2. **Classified** @useClassified / https://useclassified.fun/  
   - 建号 2026-11-25 15:11:28 CST，本轮 3 粉 / 8 帖。官帖 15:40:19 CST（https://x.com/useClassified/status/2125494778682916910 ）仅写 Important. Read it please.。  
   - 官网 HTTPS 200，自称独立项目、建立在 Helius Privacy Rings 上，用全新钱包代付并代发射。FAQ 写并非由 Helius 制作。本轮 https://useclassified.fun/api/config：open=true、mock=false、hub=`G2LCRbDRjE8vpxkomM9E4WPP74gwLifKzLWzQCtDo7CL`、launchFeeSol=0.005、默认 venue=Raydium LaunchLab、ca=`EzoLmsunnsrZ7moxe4JF2uj3xrYYsRKBzybqrEhwpump`、x 为空字符串。X→站点已由资料栏确认，但站点未回链官号，site-X 互证不完整。coins 接口本轮为空列表。同 CA 在 pump.fun 币页（https://pump.fun/coin/EzoLmsunnsrZ7moxe4JF2uj3xrYYsRKBzybqrEhwpump ）标题 Classified，约 15:45 CST 可见 Market cap 约 $8.74K、24h vol 约 $27.1K、Holders 134、ATH 约 $9.81K、Supply 1B，配对 Helius Staked SOL，文案 Top 10 约 16.63%、Dev 0%、Bundlers 约 9.936%。  
   - DeepSeek overall=58，admit=true。已挂 userFollowWatch + agentPadWatch。本号不自动 mint。

## 库内动态（不重推）

- 真实 LE2H=0。The Jacket 仍 2026-11-25 18:00 CST（10:00 UTC），约 16:00 CST 才进 2h，本轮开火时尚未进入；MUST 未见其新官帖。ORIPA 首包仍 20:00 CST（与「10 hours left」官帖一致，约 18:00 CST 才进 2h）。Ugly Puggies 公开仍 21:00 CST（13:00 UTC），本轮可见 first WL batch 已添加及 “see you there”，不是改期/开铸。2hour.fun 首窗仍是 21:00 UTC = 2026-11-26 05:00 CST，不要按今天 21:00 CST 告警。Agent Cards 23:00 CST；Shielded Wizards 2026-11-26 05:10 CST；Lamoryant 2026-11-26 19:00 CST；QQAI 2026-11-26 18:00 CST。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。公共 BSC RPC（https://bsc-dataseed.binance.org/，约 2026-11-25 15:38:27 CST）340/3333（R2184 为 337/3333），nftMintPaused=false。本轮 MUST 未见新的 TriForge 官帖。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=3（R2184 为 2）；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。本号不自动 mint。官网 HTML 可能仍显示未水合的 “Contracts are not deployed yet”，以 RPC 为准。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，不重推。
- gAnts / Merged：R2184 已收录已通知。Merged 本轮 MUST 继续有产品/CA/锁仓说明帖，不是新的免费 mint，不重收、不重推。
- Femeora @femeoraApp：R2183 已通知；本轮可见 DAMM coming 等产品预告，无实质改期/开铸，不重推。
- SYMPHONY @symphonyopus：Sale 仍 12 Dec，Prelude 已知，本轮仅见 Pass 艺术图，不重推。
- Azuke Pad：本轮见 “holding even though we are very low”，不是改期/免费铸，不重推。
- AtlasPad：市场脉搏、6982 ZRO graduation、buyback/burn（与 R2184 所见同一 14:53 CST 帖）及 Bridge ZRO/$ATLASPAD 开关，不是已开盘或免费铸，不重推。
- Basket：本轮见前 3 小时 payouts / 90 NFTs minted / 9M $BASKET burned 等运营更新，仍是已知付费盘，不是免费 mint，不重推。
- Shit Capital Genesis 仍为已知付费公售；Ugly Puggies / ORIPA / 2hour.fun / DAEMONS / SPCX / Amend / Sparecycle / Flame-BTC / Z3RO Terminal / MSKD / Blonskr TapeTape / flapdotsh / dogstarterhq 等本轮均无新的免费 mint 或改期，不重推。Sparecycle “free trial: 5 images an hour” 是产品试用不是代币/NFT 免费铸。TapeTape（tapetape.org）是 @Blonskr 的加密通讯产品，无独立官号，不另建卡。

## 看见但未收

- @GeneraNetwork：约 4.6 日、155 粉 / 3 帖，无官网。本轮只作为他人 KW_GAPS 提及（称其用 AI agent 工作流出块，类比 squeekchain），没有其本身帖文，不收。
- @LedgerGank：建号约 0.12 日、1 粉，自称 XRP Ledger 社区 free mint，规则为关注+评论钱包+tag friends，无官网，像互动盘，不收。
- @axtapi：建号约 0.03 日，Claude API 聚合 + 注册送 $1 额度，不是加密 mint/发射台，不收。
- @tailtradesxyz：R2184 已见未收；本轮仍无足以改判的新证据，不重收。
- @furbi59360（Deadpool Ninja Turtle ordinals / fried_Chick）：约 594 日号、3575 粉，非早期官号，IP 交叉盘，不收。
- @LongyuNetwork、@BitnetMoney、@CadaCasoxLayer、@ninedragons_rtc、@anvoraapp、@ponsbot_ai、@OUTLAWSxNFT、@tinylegendsfun、@PixelPuddingsRH：本轮无足以改判的新证据，不重收。

## Discord Peek

- 本轮已同轮 computerUse Peek，写出 /tmp/r2185/discord_peek.json（约 2026-11-25 15:38:32 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone / Password / Log In / QR / passkey / Register）。未输入凭据、未登录。四频道均未翻，lastSeen 仍约 2026-11-23 22:19–22:56 CST，积压约 2 天。
- apply 已写 discordPeekDeferred=true。R2158 已请用户在盒子 Chrome 重新登录 Discord，本轮 nag=false，不单为登录墙再催。

## 失败 / 备注

- dsFallback=false。X 搜索 28/28 无解析错误（x_usage errors=[]）。
- 十栏关键词均已跑到；userFollow 本轮分片已刷完；mentions 本轮覆盖 pads-rest/GIWA/Tape/LayerZero-24h/Elysium-rest；瘦栏 LZ/DOGE/BTC/STARK 做了 24 小时补搜。
