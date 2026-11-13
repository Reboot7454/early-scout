# RESULT R1775（独立例行 pace）

- time: 2026-11-14 00:16:43 CST（Asia/Shanghai）。开跑前 `git pull`，本地已在 R1774 merge（8e8ead0），meta.round 仍为 1774，本轮开 R1775。扫描期间 Discord 未占用本轮，不合并。notify=true。未自动 mint。
- mode: pace 独立轮（tight；R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true。已有预告的 bagnotary（@bagnotary）本轮**首次核实** $BAGNOT 已于 2026-11-14 00:00 CST 在 Pons 开盘。R1770 只推过 ≤2h 预告，开盘确认是新事实。无新收录。禁止重推：lil-giraffies / boolish-rh 预约 23:00 CST 已过，仍未能核验开铸（R1768 已推 ≤2h）；oathbots $OATH 预售仍 OPEN（R1773 已推；链上仍 0.775 BNB / 25 钱包）；hooded-ape / polyrob / Ashling / HonestBull / ponke-agent 及其它已推 LIVE 仅进度刷新。
- xReads: 12（main 11；silent 1；admitVerify 0）；remainingBefore 195 → remaining 183 / 1000；softCap 10，minSpend 10，silentCap 1；main 11 略超 softCap 1（UF×1 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + mentionsThin×2，未砍栏），高于 minSpend。官网 / 链上 / HTTP / OpenSea / GeckoTerminal 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。from: 官号窗 start_time=2026-11-13T15:30:00Z；关键词 / mentions start_time=2026-11-13T15:35:00Z。
- admitVerifyReads: 0。未为候选另耗 X 读。硬禁无官推核验：StinkyPenguinL0 再出现仍不收录。bagnotary CA 来自 GeckoTerminal 与 16:00 UTC 时刻吻合的 Pons V2 池，未为补拉官号另耗 X。lil-giraffies 官帖来自本轮已拉 THIN1，未另开 X 复核。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑。核心栏因 tight / alloc.kwCore=0 本轮延后。BN Agent 靠已有卡 + 官网/RPC 刷新，不另烧 fat shard。不翻页 next_token。帖量 meta.result_count：LayerZero 2、Tape 25、GIWA 10、DogeEVM 20、BTC 7、Starknet 5。部分 write_to_file 回包在约 6.5KB 截断，已用正则从完整 asset 文件抽取完整帖，未为完整 JSON 重拉。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1；核心栏本轮未跑（kwCore=0）
- userFollow: 刷完本片 1278→1318，kept 40，skip 0，1 from: batch，本片 2 帖（UF=2，均 @returntotimmy 回复，与打新窗无关）。下一轮从 1318 续（UF accounts=1666；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、Tape/电路（薄栏 mentionsThin）；kwCore=0、mentionsRest=0，本轮不跑核心栏 KW、不跑 rest mentions。LayerZero 实际查询官号为 @PlunderPort / @0rigindotfun / @globemkts / @ZeroVaultxyz / @ZeroGuysNFT / @zerodroidsio。Tape 实际覆盖 @TapeAIAgent / @Blonskr / @TapeOutWorld / @BEMGoGoGo / @tapeupio / @FirstoAI / @Tape_Pool / @bitcointapes / @TapeLaunch / @TATO_TapeOut / @Tapemonkeworld / @tapekeyofficial / @TapeId_AI / @owlgatecli / @tapebitprotocol / @TapePetDao / @ElysTape / @coverstarlink / @getsarf / @TapeSurge / @fruitfly_world（已与 used-handle / 已知 NF 去重；跳过 TapeFractal、FoundryTape 不连刷）。均已跑，不翻页。帖量 MENT_LayerZero 8、MENT_Tape 0。
- fat shards: 本轮 tight 跳过厚表分片，光标不变：agentPad 154 / freeMint 242 / bnAgent 71 / elysium 168。未改 meta.fatNextStarts。
- thin official watches: 2 个 from: 批次（MUST 优先装进第一批）。去重后薄栏独立 handle 93，加 MUST 13，扣除已知 NF TapeFractal / FoundryTape 不连刷后查询 104。本窗 THIN1=13 帖 / THIN2=2 帖（含 @HoodedApeClubRH 1392/1500、@giraffies_nft 进游戏宣传、@tmachinroBot 27/6551、@BoxcarsHQ 车型、@tapeupio Builder Camp、@Jumak_app / @Flizyapp GIWA 氛围帖）。无 @bagnotary / @boolish_rh 本窗官帖。
- silentAccounts: ran=true，lane=LayerZero（round 1775 % 11 = 4；search_users unavailable，改跑 mentions `has:mentions (LayerZero OR OFT) (mint OR launch OR launchpad) -is:retweet`，softCap 外 1 读）；回包 1 帖。filter seen=2、sentToReview=0、admitted=0；跳过 @yixiualpha too_many_posts(34)、@ZeroGuysNFT already_in_library。未做第二读。
- discordPeekDeferred: false（本例行默认不登录 DC；开跑与扫描期间 Discord 未占用本轮，独立记为 R1775。未尝试登录）。
- DS: 例行 pace 无新收录候选送审，未另开 DeepSeek 批次。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: bagnotary 首次核实已开盘，须推。lil-giraffies / boolish-rh 预约 23:00 CST 已过但未能核验开铸，不作为已开铸通知。oathbots 预售仍 OPEN，仍 0.775 BNB / 25 钱包，不重推。HonestBull 已售仍 23/10000。boxcars 驾照 148→151/1000。ponke-agent 49→58/11055、免费 49→58/555。agx-402 unitsMinted 仍 10325，distributedAgx 仍 4.1300 亿，mintUnitPriceU 0.2685→0.2674，genesisClaims 仍 OPEN，voting 仍 NOT_OPEN，migrationDeadline 2026-11-14 16:00:58 CST。hooded-ape-club 公铸仍 LIVE，OS 1353→1392/1500，不重推。polyrob 官帖仍 27、OS 28→29，不重推。
- watch-bug: 本轮无新卡，无须新挂 Watch。历史漏挂仍约 1686 张；本轮未做整表回填。
- new cards: 无新卡。已清上一轮 newThisRound（orbyt / sonna-agent / holt / passage / pterodaktil / rushr）。meta.newThisRound == 顶层 newThisRound == roundNAdded == []。candidateCount 仍 4194。bagnotary 为已在库卡的首次开盘核实，不作为新收录。

## 须推

- bagnotary（@bagnotary）$BAGNOT 已于 2026-11-14 00:00 CST 在 Pons 开盘（首次核实）。Pons V2 BAGNOT/WETH 池 0xce96780f28b173f138f8da9a8625deaf7aebec33 创建于 16:00:10 UTC，与官宣时刻吻合；代币 CA 0x977441dc8a267a7b5410988d922e4dde45ef6283（来自该池，非本轮官帖原文）。池储备约 3214 USD，1h 成交约 2377 USD。同名更早 Pons 池 0x2377a8789ce500fe336bceecadec6b9dbdddfd7f（07:40:29Z，代币 0x64bc58becdf714442da98afdda8ca0b8817fd5a3）勿当官 CA。本窗无开盘官帖；官网 bagnotary.pro 仍 SSL EOF。付费发币，非免费铸。本号不自动 mint。

## 仍在跟（刷新，不重推）

- oathbots：$OATH 付费预售仍 OPEN。链上 status=1，已存入仍为 0.775 BNB / 25 钱包，finalized=False，50000000 枚 OATH 仍在预售合约内。窗口至 11-18 22:00 CST。非免费。R1773 已推。
- hooded-ape-club：公开铸造仍 LIVE。本窗官帖称 1,392 / 1,500，还剩 108。OpenSea 1353→1392/1500，sales 1362→1389，owners 537→540，floor 约 0.14 USDG。付费公铸，免费档已满。公开 Robinhood RPC 仍失败。
- polyrob：白名单铸造仍 LIVE。本窗官帖仍为 23:31 CST：27 of 6,551 minted，Allowlist 仍余约 22h，0.033 ETH。OpenSea 已铸 28→29，owners 12→14，sales 0。铸造页写公开销售将于 11-14 21:52 CST 开始。卡内 CA 0xbBa60AB93Fc409b1A34371CBF6c3173795Ed2c7e，OS 合约 0xe0cfdd0f7ec8bba180e7cdea93e521ddcba4f63a，未裁定哪个为铸造合约。仍需 WL，非免费公铸。官网 polyrob.xyz 仍 SSL EOF。
- lil-giraffies：预约 23:00 CST 已过。本窗官帖 23:50 CST 为持有人进游戏宣传，并非开铸原文。官网仍写 Join the Lil whitelist。原记 CA 0x20b25DA8785990CC89330AF56310024Bb199CD36 公开 RPC 仍 hasCode false，官号资料栏仍写该 CA。OpenSea 集合 lil-giraffies-club（verified）total_supply 5654→6245，sales 6538→7464，owners 4558→4397，floor 约 5.0 USDG，合约 0x440c0d01b8d1065446dc178a42e213e6d3b15686，与卡内原 CA 不同；不以该集合当作已核验开铸。
- boolish-rh：Possession night 预约 23:00 CST 已过。本窗无官帖；boolish.fun 仍为文化页、无铸造 CTA；页上 BUY $BOOL 链到 2026-09-12 即已存在的 Bool/USDG 池，不是本晚新开铸造窗。公开 RPC 失败，OpenSea 集合未找到。未能核验是否已开铸。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，remaining=9977，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。非免费。
- boxcars：免费驾照仍开放，链上已领 148→151/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上 49→58/11055，免费 49→58/555，paid=0，gift=0，仍在免费档。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12DB0F8F5816750Eb2A4ac6076FDb912d3 totalSupply 仍为 0。R1764 已通知，不单独重推。
- GateCerberus：本窗无新官帖更新已售数。R1762 已通知，不单独重推。
- Freememe：应用已 LIVE。本窗无新开铸官帖。R1762 已通知，不作为新 mint 窗重推。
- agx-402：付费 fair launch 仍 OPEN。unitsMinted 仍 10325，distributedAgx 仍 4.1300 亿，mintUnitPriceU 0.2685→0.2674。genesisClaims 仍 OPEN，voting 仍 NOT_OPEN。migrationDeadline 2026-11-14 16:00:58 CST。仍需 .ai Agent ID + Binance Agentic Wallet。本号不自动 mint。
- dripevm：白名单免费仍开，Elysium RPC 与 OpenSea drip-nft 本轮均为 165/888。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸仍 1485，owners 875，sales 1826，floor 约 0.00070 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea 仍 528/777，owners 346→343，sales 658→663，floor 约 0.0010 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1742→1748/2222，wallets 139→141，priceUsd≈2.57。不是免费窗。
- arctic-bear：链上已铸仍为 82/5555。
- clause-protocol：链上已铸仍为 9/7777。
- momo-mochi：链上已铸仍为 299/2222。
- tsbdotfun：OpenSea the-shadow-born 仍 0。Discord 已通知，不重推。
- ashling：本轮未再补拉官帖。官网仍 SSL EOF。R1772 已通知 Pons 池与 CA，不重推。
- clankbots：Ink 免费白名单登记仍 LIVE，whitelist 页仍开放。R1772 已通知，不重推。

## 例行侧 skips

- StinkyPenguinL0：关键词窗再次出现弱 Layer Zero meme，R1774 已 skip，本轮仍无已核验官网/官推可操作窗口，不收录。
- ZeroGuysNFT：已在库（mint 预约 11-30），静号/mentions 窗仅第三方讨论，不另建卡。
- AmmoraHQ / PlunderPort / Flizyapp / Jumak_app / tapeupio 等已在库生态或活动帖，不重开卡。
- 同名 BOOLISH / BAGNOT 更早或 Flap 池：非官宣时刻吻合的 Pons 官池，不以这些 CA 建卡或覆盖官 CA。
- silent LayerZero mentions：1 帖为粉很少的第三方综述已在库 @ZeroGuysNFT，sentToReview=0。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1775）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
