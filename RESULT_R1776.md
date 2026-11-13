# RESULT R1776（例行 pace 合并进 Discord 已占轮）

- time: 2026-11-14 00:34:23 CST（Asia/Shanghai）。开跑前 `git pull`，远程已是 Discord R1776（00:26 CST 补收 sharpline / ophiris / bloomvale / covar-agent / loterry，已通知，不重推）。例行 pace 合并进同一轮，不另起 R1777。notify=false。未自动 mint。
- mode: tight merge（R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false。pace 本轮无新收录、无新确认免费 LIVE / 首次 ≤2h。lil-giraffies 本轮首次官宣售罄，铸造窗已过，不作为可打窗口重推；polyrob 公开销售改至 11-14 22:00 CST，非 ≤2h；oathbots / hooded-ape / ponke-agent 等已推 LIVE 仅进度刷新。Discord 五卡不重推。
- xReads: 12（main 11；silent 1；admitVerify 0）；remainingBefore 183 → remaining 171 / 1000；softCap 10，minSpend 10，silentCap 1；main 11 略超 softCap 1（UF×1 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + mentionsThin×2，未砍栏），高于 minSpend。官网 / 链上 / HTTP / OpenSea / GeckoTerminal 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。from: 官号窗 start_time=2026-11-13T16:00:00Z；关键词 / mentions start_time=2026-11-13T16:05:00Z。
- admitVerifyReads: 0。未为候选另耗 X 读。硬禁无官推核验：本窗无新收录候选。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑。核心栏因 tight / alloc.kwCore=0 本轮延后。BN Agent 靠已有卡 + 官网/RPC 刷新，不另烧 fat shard。不翻页 next_token。帖量 meta.result_count：LayerZero 3、Tape 17、GIWA 10、DogeEVM 18、BTC 7、Starknet 5。部分 write_to_file 回包在约 6.5KB 截断，已用 Full text 完整 asset 抽取完整帖，未为完整 JSON 重拉。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1；核心栏本轮未跑（kwCore=0）
- userFollow: 刷完本片 1318→1358，kept 40，skip 0，1 from: batch，本片 1 帖（@stockmonapp DNA 已在 Blockscout 完成 Robinhood Chain 代币资料验证，已在库，非新开铸）。下一轮从 1358 续（UF accounts=1671，含本轮补挂 5 个 Discord 官号；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 GIWA、DogeEVM（薄栏 mentionsThin；R1775 已覆盖 LayerZero+Tape）。kwCore=0、mentionsRest=0，本轮不跑核心栏 KW、不跑 rest mentions。GIWA 实际查询官号为 @GIWA_by_Upbit / @YeonPad / @Jumak_app / @AmmoraHQ / @ShortChall / @SuperWalk_ / @gamapadcom / @GIWAUP / @hanokreserve / @madang_fun / @deuslaunch / @BaekhoGiwa / @PunkOnGiwa / @Giwatron / @mimdotcash / @GiwaPumpPad / @GiwaGasok / @GIWAForge / @GenPad_Ai / @gazuaxyz / @JakduPump / @Writ_Fi / @GAMA_GIWA / @Flizyapp / @quadrixfinance / @narupay_com / @JoseonFun / @MulleProtocol / @gasokfun / @void_dex / @SealonGIWA / @Joayofundev / @GIWAHOOK / @GIWALAUNCHPAD / @giwapad_xyz / @soomdotfun / @VordaLaunch。DogeEVM 实际覆盖 @DogeOS / @LaikaSuperApp / @MonkoCoin / @gekkoai_agent / @RUNECLAW_AI / @cavdefi / @anoncoinit / @wowpadlol / @DogeOSExchange / @packswap_xyz。已与已知 NF（TapeFractal / FoundryTape）去重。均已跑，不翻页。帖量 MENT_GIWA 10、MENT_DogeEVM 9。
- fat shards: 本轮 tight 跳过厚表分片，光标不变：agentPad 154 / freeMint 242 / bnAgent 71 / elysium 168。未改 meta.fatNextStarts。
- thin official watches: 2 个 from: 批次（MUST 优先装进第一批）。去重后薄栏独立 handle 91，加 MUST 13，扣除已知 NF TapeFractal / FoundryTape 不连刷后查询 104。本窗 THIN1=12 帖 / THIN2=2 帖（含 @giraffies_nft 售罄官宣、@tmachinroBot 公开销售改期、@HoodedApeClubRH 1392/1500、@BoxcarsHQ 车型、@tapeupio Builder Camp、@Flizyapp / @Jumak_app GIWA 氛围帖）。无 @bagnotary / @boolish_rh / @Oathbots / @PonkeAgent 本窗官帖。
- silentAccounts: ran=true，lane=Elysium（round 1776 % 11 = 5；search_users unavailable，改跑 mentions `has:mentions (Elysium OR Enter_Elysium) (mint OR launch) -is:retweet`，softCap 外 1 读）；回包 1 帖。filter seen=1、sentToReview=0、admitted=0；@Leemah_luxe62 为个人祝贺 “launch Elysium Sounds” 语境，非项目官号。未做第二读。
- discordPeekDeferred: false（本例行默认不登录 DC；开跑前 Discord 已占用本轮并补收 5 卡，例行合并进 R1776。未尝试登录）。
- DS: 例行 pace 无新收录候选送审，未另开 DeepSeek 批次。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: lil-giraffies 首次官宣售罄，不重推。polyrob 公开销售改至 11-14 22:00 CST，非 ≤2h，不重推。oathbots 预售仍 OPEN，0.775→0.805 BNB / 25→27 钱包，不重推。HonestBull 已售仍 23/10000。boxcars 驾照 151→152/1000。ponke-agent 58→59/11055、免费 58→59/555。agx-402 unitsMinted 10325→10334，distributedAgx 4.1300 亿→4.1336 亿，mintUnitPriceU 0.2674→0.2656，genesisClaims 仍 OPEN，voting 仍 NOT_OPEN，migrationDeadline 2026-11-14 16:00:58 CST。hooded-ape-club 公铸仍 LIVE，OS 1392→1442/1500，不重推。bagnotary 池储备约 3212 USD，R1775 已推开盘，不重推。
- watch-bug: Discord 五张新卡在库不在任何 Watch，已补进 userFollowWatch（@SharplineMrktRh / @OphirisLoop / @bloomvaleRH / @CovarAgentxyz / @LoterryChainv2）。均为台子/Meme（RH 发币或 Polygon 彩票），未兼挂 agentPad/bnAgent/freeMint。历史漏挂仍约 1686 张；本轮未做整表回填。
- new cards: pace 无新卡。保留 Discord 本轮 newThisRound（sharpline / ophiris / bloomvale / covar-agent / loterry）。meta.newThisRound == 顶层 newThisRound == round1776Added。candidateCount 仍 4199。挂 Watch 后 UF accounts=1671。

## 仍在跟（刷新，不重推）

- lil-giraffies：官号于 2026-11-14 00:15:47 CST 官宣 Officially Sold Out，并引导进游戏。R1768 已推 ≤2h；本轮是售罄确认，不重推。卡内原 CA 0x20b25D… 公开 RPC 仍 hasCode false。OpenSea lil-giraffies-club 6245→6666，sales 7464→8271，owners 4397→4395，floor 约 4.1 USDG，合约 0x440c0d01…，与卡内原 CA 不同。
- polyrob：本窗官帖确认 allowlist 已于 13:00 UTC（21:00 CST）关闭；公开销售 Sat 14 Nov 14:00 UTC（11-14 22:00 CST）。此前卡内 21:52 CST 以本轮官帖为准。距公开销售仍约 21h，非 ≤2h。OpenSea 已铸仍 29。官网仍 SSL EOF。仍需 WL 才能打当前窗；公开销售尚未开始。
- oathbots：$OATH 付费预售仍 OPEN。链上 status=1，已存入 0.775→0.805 BNB / 25→27 钱包，finalized=False，50000000 枚 OATH 仍在预售合约内。窗口至 11-18 22:00 CST。非免费。R1773 已推。
- hooded-ape-club：公开铸造仍 LIVE。本窗 00:01 CST 官帖称 1,392 / 1,500，还剩 108。OpenSea 1392→1442/1500，sales 1389→1440，owners 540→547，floor 约 0.13 USDG。付费公铸，免费档已满。公开 Robinhood RPC 仍失败。
- bagnotary：$BAGNOT 已开盘（R1775 已推）。Pons V2 池储备约 3212 USD，成交约 2377 USD。官网仍 SSL EOF。付费发币。
- boolish-rh：Possession night 预约 23:00 CST 已过。本窗无官帖；boolish.fun 仍 200。未能核验是否已开铸。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，remaining=9977，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。非免费。
- boxcars：免费驾照仍开放，链上已领 151→152/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上 58→59/11055，免费 58→59/555，paid=0，gift=0，仍在免费档。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12… totalSupply 仍为 0。R1764 已通知，不单独重推。
- agx-402：付费 fair launch 仍 OPEN。unitsMinted 10325→10334，distributedAgx 4.1300 亿→4.1336 亿，mintUnitPriceU 0.2674→0.2656。genesisClaims 仍 OPEN，voting 仍 NOT_OPEN。migrationDeadline 2026-11-14 16:00:58 CST。仍需 .ai Agent ID + Binance Agentic Wallet。本号不自动 mint。
- dripevm：白名单免费仍开，Elysium RPC 与 OpenSea drip-nft 165→166/888。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸 1485→1497，owners 875→877，sales 1826→1838，floor 约 0.00070 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea 仍 528/777，owners 343，sales 663，floor 约 0.0010 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸仍 1748/2222，wallets 141，priceUsd≈2.57。不是免费窗。
- arctic-bear：链上已铸仍为 82/5555。
- clause-protocol：链上已铸仍为 9/7777。
- momo-mochi：链上已铸仍为 299/2222。
- tsbdotfun：OpenSea the-shadow-born 仍 0。Discord 已通知，不重推。
- ashling：本轮未再补拉官帖。官网仍 SSL EOF。R1772 已通知 Pons 池与 CA，不重推。
- clankbots：Ink 免费白名单登记仍 LIVE，whitelist 页仍开放。R1772 已通知，不重推。

## 例行侧 skips

- BurstLabs_io：LayerZero 关键词窗为 Flare DVN / FTSO 基础设施讨论，非新打新窗口，不收录。
- Daejinxyz / @9Xvenom 帖：第三方称 DogeOS 预测市场积分季免费开放，本窗无该项目官帖、未另耗 X 核验官号，不收录。
- GIWAUP Tilekeepers：已在库；本窗仅为 @0xunchain 第三方 giveaway（主网上线日铸造，价格 TBA），不另建卡、不重推。
- AmmoraHQ / Flizyapp / Jumak_app / tapeupio / LaikaSuperApp / stockmonapp 等已在库生态或活动帖，不重开卡。
- Starknet 关键词窗本轮 5 帖均为 “Bramble” 鸟类/游戏误伤，无 Starknet 打新信号。
- silent Elysium mentions：1 帖为个人祝贺 “Elysium Sounds” 语境，sentToReview=0。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1776 merge）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
