# RESULT R1781（例行 pace 合并进 Discord 已占轮）

- time: 2026-11-14 03:12:10 CST（Asia/Shanghai）。开跑前 `git pull`，远程已是 Discord R1781（02:52 CST 补收 agent-lotto，已通知，不重推；commit 37737a1）。例行 pace 合并进同一轮，不另起 R1782。notify=false。未自动 mint。
- mode: tight merge（R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false。pace 本轮无新收录、无新确认免费 LIVE / 首次 ≤2h。ape-city 官号首次给出开窗 11-14 23:00 CST，距窗仍约 20h，非 ≤2h，不预推；polyrob 公开销售仍 11-14 22:00 CST，距公开销售仍约 19h，非 ≤2h；burybud 官帖再确认仍 11-14 23:00 CST，非 ≤2h；agent-lotto 为付费彩票且 Discord 已推，不重推；oathbots / bagnotary / ponke-agent / boxcars 等已推 LIVE 仅进度刷新。
- xReads: 13（main 12；silent 1；admitVerify 0）；remainingBefore 123 → remaining 110 / 1000；softCap 10，minSpend 10，silentCap 1；main 12 超 softCap 2（UF×1 + 薄栏 Watch/MUST×3 + 薄栏 KW×6 + mentionsThin×2，未砍栏）。THIN 因 MUST+薄栏+zeroWatch 去重后 107 个 handle 无法在 1024 字符内装进 2 批，故多 1 次 THIN3，高于 minSpend。官网 / 链上 / HTTP / OpenSea / GeckoTerminal 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重（本轮 MUST 17 个，含 burybud / AgentCatRh / agentai_lotto）。from: 官号窗 start_time=2026-11-13T18:25:00Z；关键词 / mentions / silent start_time=2026-11-13T18:30:00Z。不翻页 next_token。
- admitVerifyReads: 0。未为候选另耗 X 读。硬禁无官推核验：本窗 pace 无新收录候选。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑。核心栏因 tight / alloc.kwCore=0 本轮延后。BN Agent 靠已有卡 + 官网/RPC 刷新，不另烧 fat shard。不翻页。帖量：LayerZero 3、Tape 2、GIWA 3、DogeEVM 18、BTC 8、Starknet 4。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1；核心栏本轮未跑（kwCore=0）
- userFollow: 刷完本片 1518→1558，kept 40，skip 0，1 from: batch，本片 5 帖（@theboatnfish 02:48:12 CST 游戏开场预告、@inklegions “Mint on Monday”、@Ape_CityRH 首次给出 3PM GMT 开窗、@RogueSociety_ / @hoodicorns 社交回复）。下一轮从 1558 续（UF accounts=1682，含本轮补挂 1 个 Discord 官号；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、Tape（薄栏 mentionsThin；R1780 已覆盖 BTC+Starknet，R1779 已覆盖 GIWA+DogeEVM）。kwCore=0、mentionsRest=0，本轮不跑核心栏 KW、不跑 rest mentions。已与已知 NF（TapeFractal / FoundryTape）去重。均已跑，不翻页。帖量 MENT_LayerZero 25、MENT_Tape 3。
- fat shards: 本轮 tight 跳过厚表分片，光标不变：agentPad 154 / freeMint 242 / bnAgent 71 / elysium 168。未改 meta.fatNextStarts。
- thin official watches: 3 个 from: 批次（MUST 优先装进第一批，本轮 MUST 17 个，含 burybud / AgentCatRh / agentai_lotto）。去重后薄栏+zeroWatch 独立 handle 90，加 MUST 后扣除本轮 UF 重叠 4 个（getsarf / giwapad_xyz / soomdotfun / TwinkleNFTs）及已知 NF TapeFractal / FoundryTape 不连刷后查询 107。本窗 THIN1=7 帖 / THIN2=0 / THIN3=0（含 @burybud 03:00:01 CST 再确认 15:00 UTC 上 Pons、@agentai_lotto 02:37:55 CST 确认 0/300 已开铸、@tmachinroBot 两条回复、@banknotes_btc AI curator 测试与招呼）。无 @bagnotary / @boolish_rh / @giraffies_nft / @PonkeAgent / @Oathbots / @HoodedApeClubRH / @AgentCatRh 本窗官帖。公开销售/预约均非 ≤2h：polyrob 11-14 22:00 CST、agent-cat 11-14 21:00 CST、burybud / ape-city 11-14 23:00 CST、agx-402 migrationDeadline 仍 11-14 16:00:58 CST（约 13h）。
- silentAccounts: ran=true，lane=Starknet（round 1781 % 11 = 10；search_users unavailable，改跑 mentions `has:mentions (Starknet OR Bramble) (mint OR launchpad) -is:retweet`，softCap 外 1 读）；回包 0 帖。filter seen=0、sentToReview=0、admitted=0。未做第二读。
- discordPeekDeferred: false（本例行默认不登录 DC；开跑前 Discord 已占用本轮并补收 1 卡，例行合并进 R1781。未尝试登录）。
- DS: 例行 pace 无新收录候选送审，未另开 DeepSeek 批次。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: hooded-ape 仍售罄 1500/1500，本窗无新官帖，不重推；OS sales 1528→1598，owners 531→537，floor 约 0.13 USDG（此前约 0.47）。lil-giraffies 本窗无新官帖，OS 仍 6666，sales 9106→9185，owners 4012→3978，floor 约 2.95 USDG，不重推。polyrob 公开销售仍 11-14 22:00 CST，OS 已铸仍 32，本轮 stats 401。oathbots 预售仍 OPEN，0.825 BNB / 28 钱包不变。HonestBull 已售仍 23/10000。boxcars 驾照 170→174/1000。ponke-agent 仍 63/11055、免费 63/555。agx-402 unitsMinted 仍 10339，distributedAgx 仍 4.1356 亿，接口 status 恢复 OPEN、mintUnitPriceU 约 0.2603，genesisClaims 仍 OPEN，voting 本轮为 SERVICE_DISABLED，migrationDeadline 仍 2026-11-14 16:00:58 CST。bagnotary 池储备约 3237 USD（此前约 3231），成交约 2377 USD，R1775 已推开盘，不重推。agent-lotto 链上仍 0/300、pot=0，Discord 已推，不重推。
- watch-bug: Discord 一张新卡在库不在任何 Watch，已补进 userFollowWatch（@agentai_lotto）。agent-lotto 为 BSC 付费 Agent ID 彩票，只挂 userFollowWatch，未兼挂 agentPad/bnAgent/freeMint。本轮未做整表回填。
- new cards: pace 无新卡。保留 Discord 本轮 newThisRound（agent-lotto）。meta.newThisRound == 顶层 newThisRound == round1781Added。candidateCount=4210（顶层与 meta 对齐）。挂 Watch 后 UF accounts=1682。

## 仍在跟（刷新，不重推）

- hooded-ape-club：仍售罄 1500/1500。本窗无新官帖。R1780 已记录 02:26:15 CST “NFT REVEALED!” 与效用约 08:26 CST 预告，不是新开铸窗，不重推。OpenSea hoodedapeclub 仍 1500，sales 1528→1598，owners 531→537，floor 约 0.13 USDG（此前约 0.47）。卡内 CA 0x6b1d830e… 与 OS 合约一致；公开 Robinhood RPC 仍 hasCode false。付费公铸已结束。
- lil-giraffies：本窗无新官帖。OpenSea lil-giraffies-club 仍 6666，sales 9106→9185，owners 4012→3978，floor 约 2.95 USDG。合约 0x440c0d01…，与卡内原 CA 0x20b25D… 不同。铸造窗已过，不重推。
- polyrob：本窗官号仅回复 listing / “NFT owns the wallet”，无公开销售改期帖。公开销售仍为 11-14 22:00 CST，距公开销售仍约 19h，非 ≤2h。铸造页 6551.polyrob.dev 仍 200；polyrob.xyz 本轮 SSL EOF。OpenSea 已铸仍为 32；本轮 stats 接口 401，未刷新 sales/owners。OS 索引合约 0xe0cfdd0f… 与卡内 CA 0xbBa60AB9… 不同，本轮不改写官方 CA。仍需 WL 才能打当前窗。R1772 已推已开铸，不重推。
- oathbots：$OATH 付费预售仍 OPEN。链上 status=1，已存入仍为 0.825 BNB / 28 钱包，finalized=False，50000000 枚 OATH 仍在预售合约内。本窗无新的铸造/预售改期官帖。窗口至 11-18 22:00 CST。非免费。R1773 已推。
- bagnotary：$BAGNOT 已开盘（R1775 已推）。Pons V2 池储备约 3237 USD，FDV 约 3215 USD，成交约 2377 USD（6h/24h 同值，近 1h 无成交）。官网仍 SSL 失败。付费发币。官 CA 仍为该池代币 0x977441dc…；Dexscreener 另有 flapsh 同名池，勿当官 CA。
- boolish-rh：Possession night 预约 23:00 CST 已过。本窗无官帖；boolish.fun 仍 200。OpenSea boolish 集合本轮 401。未能核验是否已开铸。不重推。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，remaining=9977，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。非免费。
- boxcars：免费驾照仍开放，链上已领 170→174/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上仍 63/11055，免费仍 63/555，paid=0，gift=0，仍在免费档。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12… totalSupply 仍为 0。R1764 已通知，不单独重推。
- agx-402：付费 fair launch 接口 status 恢复 OPEN，mintUnitPriceU 约 0.2603（R1780 曾为 PRICE_UNAVAILABLE / null）。unitsMinted 仍 10339，distributedAgx 仍 4.1356 亿。genesisClaims 仍 OPEN，voting 本轮为 SERVICE_DISABLED（此前 NOT_OPEN）。migrationDeadline 仍 2026-11-14 16:00:58 CST，距截止仍约 13h，非 ≤2h。仍需 .ai Agent ID + Binance Agentic Wallet。价格恢复不是新的免费窗，不重推。本号不自动 mint。
- dripevm：白名单免费仍开。Elysium RPC 仍 166/888；OpenSea drip-nft 集合 166，stats 本轮 401。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸仍 1508，sales 1852→1877，owners 877→871，floor 约 0.00059 ETH。已在跟的付费铸造进度，不重推。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea 仍 528/777，sales 仍 666，owners 仍 342，floor 约 0.00090 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸仍 1798/2222，wallets 仍 148，priceUsd≈2.62。本窗官号 02:48:12 CST 发 “THE OCEAN IS ABOUT TO OPEN… launches in just a few hours”，是已在跟的付费 genesis 之上的游戏开场预告，不是新的免费开铸窗，不重推。
- arctic-bear：链上已铸仍为 82/5555。官网 arcticbear.fun 仍 200。
- clause-protocol：链上已铸仍为 9/7777。ClauseMint 本轮 eth_call 仍 revert。官网 clauseprotocol.fun 仍 200。
- momo-mochi：链上已铸仍为 300/2222。官网 puzzlehave.fun 仍 200。
- tsbdotfun：OpenSea the-shadow-born 供应仍空；stats sales/owners 为 0。Discord 已通知，不重推。
- ashling：本轮未再补拉官帖。官网 ashling.fun 仍 SSL EOF。R1772 已通知 Pons 池与 CA，不重推。
- clankbots：Ink 免费白名单登记仍 LIVE，whitelist.html 仍 200 开放。R1772 已通知，不重推。
- burybud：官号 03:00:01 CST 再确认 $BURY 于 11-14 23:00 CST（15:00 UTC）上 Pons，花园已开放、埋股票无需代币，CA 仍未公布。距窗仍约 20h，非 ≤2h。官网 burybud.xyz 本轮 SSL EOF。不预推。
- agent-cat：仍未开铸。官网 agent-cat-rh.vercel.app 本轮 200。OpenSea agent-cat-bags 供应仍 0，stats 本轮 401。开铸仍为 11-14 21:00 CST，距窗仍约 18h，非 ≤2h。本窗无官帖。
- ape-city：官号 02:35:17 CST 首次给出开窗时刻：14th November 3PM GMT（2026-11-14 23:00 CST），Robinhood Chain，555 NFTs。距窗仍约 20h，非 ≤2h，不预推。本帖未写明免费；此前第三方称 FREE MINT，价格仍待核验。不改成 LIVE。
- inklegions：本窗官号回复 “Mint on Monday”，与卡内开铸 2026-11-17 03:00 CST 一致，非改期，非 ≤2h，不重推。
- agent-lotto：Discord 已补收。官号 02:37:55 CST 再确认已开铸，链上 totalSupply 仍为 0/300，pot=0；官网 200。付费彩票非免费铸，Discord 已通知，不重推。未自动 mint。

## 例行侧 skips

- @Ape_CityRH 开窗官帖：已在库 ape-city，只更新时刻，不另建卡，非 ≤2h 不推。
- @theboatnfish “ocean is about to open”：已在库 boatn-fish 付费 genesis，不另建卡、不重推。
- @inklegions “Mint on Monday”：已在库，开铸时刻未改。
- @burybud 再确认 15:00 UTC：已在库，档期未改。
- @agentai_lotto 再确认 0/300：本轮 Discord 已收录，不重开卡。
- @tmachinroBot 两条回复（listing / NFT-owns-wallet）无改期。
- @banknotes_btc AI curator 测试与招呼，已在库，不是新打新。
- @GIWA / AmmoraHQ / Flizyapp / GIWAUP 等待名单与任务讨论：已在库 GIWA 生态，不重开卡。
- Tape 窗与 MENT_Tape 均为对 @Blonskr / @TapeOutWorld 的社区回复，无新官号。
- LayerZero 关键词窗 3 帖均为 Flare DVN / OFT 流量转推，无新打新。MENT_LayerZero 25 帖多为已在库 @ZeroGuysNFT / @PlunderPort / @zerodroidsio / @LayerZero_Core 的白名单评论，不另建卡。
- Starknet 关键词窗 4 帖均为足球/游戏/刺猬同名 Bramble 误伤，无 Starknet 打新信号。silent Starknet mentions：0 帖。
- BTC 窗 8 帖为 Shielded Naka 二次销售（@Ord_Dropz）与社区招呼，已在库项目，不另建卡。
- DogeEVM 窗 18 帖多为 DogeOS 表情/打赏机器人、@LaikaSuperApp 主网讨论（已在 Watch）及新闻转推，无新的主网官铸，不收录。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1781 merge）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
