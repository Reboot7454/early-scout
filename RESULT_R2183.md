# RESULT R2183

- 轮次：R2183（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 14:37–14:48 CST（Asia/Shanghai）。apply dry-run lastScout=2026-11-25 14:47:55 CST。
- mode=ample；softCap=28；minSpend=20；silentCap=2（silent 不计 softCap）
- xReads=27（main 26 + silent 1），未超 softCap，不低于 minSpend
- remainingBefore=641 / 1000（第一笔 X 工具结果 remainingToday=640，+1）；remainingAfter=614（末笔 KW_STARK_24 remainingToday=614；641−27=614，与 live 一致）
- Judgment / admit / score：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score，送审 2 项（@dogstarterhq、@femeoraApp）；仅 Femeora 新收录。@dogstarterhq 与库内 R1828 Dogstarter 为同一站点，不重收。dsFallback=false
- 本号不自动 mint。未 commit / push，未改 /workspace/early-scout/data.json。dry-run 写在 /tmp/r2183/data.json。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=0，KW_TAPE=20，KW_GIWA=13，KW_DOGE=15，KW_BTC=0，KW_STARK=3
  - KW_MINT=25，KW_MINE=1，KW_PAD=25，KW_GO=25，KW_ELY=12，KW_GAPS=17
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=21、KW_BTC_24=25、KW_STARK_24=25
- 未把厚栏改成 24h：TAPE/GIWA/DOGE 30m 已 ≥5（20/13/15）；MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=1 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1211 @kairo_market 起 50 号至 @pfwafun，next 1261 @nouns_elysium，wrap=false，total 写盘后=2388（原 2386 + 本轮 1 个新收录 @femeoraApp + 库内 Dogstarter 新官号 @dogstarterhq）。ufOnlyFrom=50，mustOverlap=0（@shit_capital 只在本分片 UF from:），skippedNF=[]。UF1=1 帖（已在 UF 名单的 @District49xyz 产品介绍），UF2=0 帖，UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷；本轮 mentions 不含 @starx_xlayer）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=1（@Blonskr 介绍 TapeTape）。
- Mentions 24h 本轮：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest。
  - MEN_PADS=3
  - MEN_GIWA=25 触顶
  - MEN_TAPE=19
  - MEN_LZ=25 触顶
  - MEN_ELY=24
- mentionsNext：DogeEVM / BTC / Starknet / squeek / STARX
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_ELY）各跑一次，另加 3 次正当薄栏 24h，无同查询重试。

## 静号

- silentAccounts.ran=true；lane=Elysium；next=Tape/电路
- search_users 不可用；fallback 一次 SILENT_ELY（不占 softCap）
- hits=10；seen=8 个独立作者；sentToReview=[]；admitted=[]；skipped=[getleash_app, VoltaFamily, AtlasHL, DefiStark, CryptoDetonator, Audrey2ug, Meltonmy2, ChangchangL3]（前三者已在库；其余为已入库项目的第三方提及，未见需新收录的早期官号）

## 新收录

1 项，已同时挂 Watch（focus=false）。

1. **Femeora** @femeoraApp / https://femeora.tech/  
   - 建号 2026-11-23 01:09:30 CST，本轮 32 粉 / 20 帖。官网与官推互证。  
   - 官网自称 Robinhood Chain · mainnet 上的 DLMM/DAMM 流动性社交层（Every LP is a callout）。资料栏与官网均写 CA `0x6f6a3a9b30f783ef9f9f8651e49b797b8c2aa117`（本轮未另做链上核验）。  
   - 官帖 14:31 CST（https://x.com/femeoraApp/status/2125477457000378867 ）称 DLMM was step one，DAMM is coming，并写 “Then: launchpads that graduate into DAMM”。发射台毕业到 DAMM 仅见规划，不是已确认发射台 LIVE。  
   - DeepSeek overall=66，admit=true。**不是免费 mint / 免费登记。** 已挂 userFollowWatch + agentPadWatch。本号不自动 mint。

## 库内动态（不重推）

- 真实 LE2H=0。The Jacket 仍 2026-11-25 18:00 CST（10:00 UTC），约 16:00 CST 才进 2h，尚未进入；本轮 MUST 未见其新官帖。ORIPA 首包仍 20:00 CST（本轮仍可见「10 hours left」官帖 https://x.com/oripaxyz/status/2125409137127297404 ，与既定窗口一致，约 18:00 CST 才进 2h）。Ugly Puggies 公开仍 21:00 CST（13:00 UTC）；本轮 24h MUST 仍可见 09:35 CST first wl batch 已添加的官帖，另有 11:06 CST 回复 “see you there”，不是改期/开铸。2hour.fun 本轮仍可见同一则 Reservations are OPEN 官帖（https://x.com/2hourfun/status/2125409666502930693 ），另有 Streamflow 锁仓说明及 07:46 CST 回复 “Launching tomorrow”；第一场窗口仍是 Today at 21:00 UTC = 2026-11-26 05:00 CST，不要按今天 21:00 CST 告警。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。公共 BSC RPC（https://bsc-dataseed.binance.org/，约 2026-11-25 14:40:57 CST）332/3333（R2182 为 330/3333，R2181 为 322/3333），nftMintPaused=false。本轮 MUST 未见新的 TriForge 官帖。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=2（R2182 为 1）；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。本号不自动 mint。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，付费阶梯未开，未见 CA，不重推。
- Dogstarter（库内 R1828，status=testnet）：本轮 KW_DOGE 见到新官号 @dogstarterhq（建号 2026-11-23 00:14:42 CST，4 粉 / 5 帖）。官网 https://dogstarter.dog/ 页脚与 JSON-LD sameAs 现指向 https://x.com/dogstarterhq，与新官号互证；页脚仍写 DogeOS Chikyu Testnet。官帖 14:21 CST（https://x.com/dogstarterhq/status/2125474893743735081 ）介绍 DogLive。与旧官号 @dogstarter 为同一站点/同一项目，已更新卡片并挂入 @dogstarterhq 到 UF + dogeEvmWatch，**不重收、不重推**（仍是测试网，无主网开闸或免费 mint）。
- SYMPHONY @symphonyopus：R2182 已收录已通知。本轮继续回复宣传 Prelude 免费登记已开、付费 Sale 仍写 12 Dec，无实质变化，不重推、不重收。
- Azuke Pad @AzukePad：R2182 已收录已通知。本轮继续密集更新，称 payouts live、已向持有人发放约 0.543 SOL（R2182 页面曾显示约 0.541 SOL），并给出一笔 Solscan 凭证。仍不是免费 mint，无改期/新开铸，不重推。
- AtlasPad：本轮产品更新（Bridge 页 ZRO / $ATLASPAD 开关、宣称主网后持有人将获发射币空投、下一步 Agentic Hook Launch），不是已开盘或免费铸官宣，不按改期重推。
- Basket：官帖 14:06 CST（https://x.com/Basketdotxyz/status/2125471156215963928 ）介绍 1,000 份 Basket NFT（每份自带金库；铸造需烧掉 100,000 $BASKET + 0.5 SOL，页面 https://basketlaunch.xyz/mint ）。这是付费铸造，不是免费 mint。完整 token CA 仍是此前已补的 `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f`，不重推。
- SPCX / Amend / NoPvP / Sparecycle 等有产品更新，均非免费 mint，无实质开铸/改期，不重推。
- Thinkers Club / Flame-BTC：付费公开仍 LIVE（Flame-BTC 本轮仍可见 Public mint is open 旧帖），不重推。Shit Capital 在本分片 UF from: 中，本轮 30m 未见新帖。
- DAEMONS：waitlist 仍开、免费 mint 仅 members、主网约圣诞（本轮 09:00 CST 官帖重申 Before Christmas），不是已开铸 LIVE。ANKOU / Z3RO Terminal 无新日期或主网开铸。

## 看见但未收

- @eutoprotocol（https://eutoprotocol.xyz/）：建号约 6 日、67 粉 / 6 帖，资料栏自称 Solana launchpad + AI posts。本轮没有官帖，只在 KW_PAD 被 Larpcheckbot 第三方评述（称站点有钱包登录和发射流程，但 AI agent 未确认）。静态 HTML 未见回链官推（OG 图挂在 smash.battleagent.tech），未互证，未送审、不收。
- @tailtradesxyz（https://tailtrades.xyz/）：约 6 日号，自称 Hyperliquid / Elysium 上的 AI 交易台，资料栏已有 CA，不是 mint/发射台，不收。
- @OUTLAWSxNFT：2022 年旧号（4983 粉 / 16245 帖），资料栏写 Free Mint on OpenSea · Nov 27 | 1:30 PM UTC（即 2026-11-27 21:30 CST）。本轮未见官帖，R2180 前后已见未收，不重收。
- @PropsMintHQ（http://Propsmint.com）：体育博彩研究工具，不是加密 mint/发射台，不收。
- Pixel Puddings（@PixelPuddingsRH）：本轮无实质新证据（R2180 DeepSeek admit=false overall=43），不重收。
- @LongyuNetwork、@BitnetMoney、@CadaCasoxLayer、@ninedragons_rtc、@ponsbot_ai、@anvoraapp、@tinylegendsfun：本轮未见，无足以改判的新证据，不重收。

## Discord Peek

- 父进程并行 computerUse 已写出 /tmp/r2183/discord_peek.json（attemptedAt=2026-11-25 14:37:20 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone Number / Password / Log In / QR / passkey / Register）。未输入凭据、未登录。四频道均未翻，lastSeen 仍约 2026-11-23 22:19–22:56 CST，积压仍在。
- apply dry-run 已按该 JSON 写入 discordPeekDeferred=true。若父进程还有更新，可再合并。

## 失败 / 备注

- dsFallback=false。X 搜索 27/27 无解析错误（ingest errors=[]）。部分大体量搜索结果先落到 preview/asset 文件，已用 Full text 路径还原后写入 /tmp/r2183/x_raw/{id}.json，未重查同一 query。
- apply_r2183.py：默认拒绝写 /workspace/early-scout/data.json；APPLY_DRY_RUN=1 + EARLY_SCOUT_DATA=/tmp/r2183/data.json.src + APPLY_DRY_OUT=/tmp/r2183/data.json 通过。workspace data.json sha256 未变（519f81925adc79ec9c1198d448078bd94bc22872a84a97bce0e154afe1558311）。
- notify=true：因新收录 Femeora（须点名；不是免费 mint / 免费登记）。库内 Dogstarter 只更新新官号，不重推。

