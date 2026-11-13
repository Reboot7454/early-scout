# RESULT R1777（例行 pace 合并进 Discord 已占轮）

- time: 2026-11-14 01:14:18 CST（Asia/Shanghai）。开跑前 `git pull`，远程已是 Discord R1777（00:46 CST 补收 veltrixcodes / krypnous / melaps-system，已通知，不重推；随后 abf7046 记录推送核验）。例行 pace 合并进同一轮，不另起 R1778。notify=false。未自动 mint。
- mode: tight merge（R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false。pace 本轮无新收录、无新确认免费 LIVE / 首次 ≤2h。hooded-ape-club 本轮官宣售罄 1500/1500，铸造窗已过，不作为可打窗口重推；lil-giraffies 本轮官宣 reveal LIVE，同样不重推；polyrob 公开销售仍 11-14 22:00 CST，非 ≤2h；oathbots / ponke-agent / bagnotary 等已推 LIVE 仅进度刷新。Discord 三卡不重推。
- xReads: 12（main 11；silent 1；admitVerify 0）；remainingBefore 171 → remaining 159 / 1000；softCap 10，minSpend 10，silentCap 1；main 11 略超 softCap 1（UF×1 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + mentionsThin×2，未砍栏），高于 minSpend。官网 / 链上 / HTTP / OpenSea / GeckoTerminal 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。from: 官号窗 start_time=2026-11-13T16:30:00Z；关键词 / mentions start_time=2026-11-13T16:35:00Z。
- admitVerifyReads: 0。未为候选另耗 X 读。硬禁无官推核验：本窗无新收录候选。BTC 关键词窗出现 @Wizdeadrollx_ Ordinals “free mint” 宣传帖，作者 bio 为泛影响力账号、无已核验项目官号，未为猎号另烧 X，不收录。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑。核心栏因 tight / alloc.kwCore=0 本轮延后。BN Agent 靠已有卡 + 官网/RPC 刷新，不另烧 fat shard。不翻页 next_token。帖量：LayerZero 1、Tape 17、GIWA 8、DogeEVM 15、BTC 25、Starknet 4。部分 write_to_file 回包在约 6.5KB 截断，已用 Full text 完整 asset 抽取完整帖，未为完整 JSON 重拉。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1；核心栏本轮未跑（kwCore=0）
- userFollow: 刷完本片 1358→1398，kept 40，skip 0，1 from: batch，本片 2 帖（@solpoolparty、@SunfallWorld，均已在库，非新开铸）。下一轮从 1398 续（UF accounts=1674，含本轮补挂 3 个 Discord 官号；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 BTC、Starknet（薄栏 mentionsThin；R1776 已覆盖 GIWA+DogeEVM，R1775 已覆盖 LayerZero+Tape）。kwCore=0、mentionsRest=0，本轮不跑核心栏 KW、不跑 rest mentions。BTC 实际查询官号为 @ShieldedNaka / @banknotes_btc / @Unpairxyz / @acmeonbtc / @XMRVMachine / @ShieldedWizBTC / @RGBHorse / @UnseenOrdo / @DigiGolds / @crest_btc / @TapSeal / @alkanesagentic。Starknet 实际覆盖 @Bramble_fi / @Starknet / @HOKORI_QUANTUM / @_Set_It_ / @oryvnlaunch。已与已知 NF（TapeFractal / FoundryTape）去重。均已跑，不翻页。帖量 MENT_BTC 5、MENT_STARK 0。
- fat shards: 本轮 tight 跳过厚表分片，光标不变：agentPad 154 / freeMint 242 / bnAgent 71 / elysium 168。未改 meta.fatNextStarts。
- thin official watches: 2 个 from: 批次（MUST 优先装进第一批）。去重后薄栏独立 handle 91，加 MUST 13，扣除已知 NF TapeFractal / FoundryTape 不连刷后查询 104。本窗 THIN1=8 帖 / THIN2=0 帖（含 @HoodedApeClubRH 售罄官宣 1500/1500 及后续扫货帖、@giraffies_nft reveal LIVE、@tmachinroBot “Mint is live now” 营销帖、@RUNECLAW_AI 市场笔记、@0rigindotfun 回复、@ZeroGuysNFT 假白名单站警告）。无 @bagnotary / @boolish_rh / @Oathbots / @PonkeAgent 本窗官帖。
- silentAccounts: ran=true，lane=Tape/电路（round 1777 % 11 = 6；search_users unavailable，改跑 mentions `has:mentions (TapeOut OR TapeAI OR bitcointapes) -is:retweet`，softCap 外 1 读）；回包 1 帖。filter seen=1、sentToReview=0、admitted=0；@9118Liwei 为个人号提到 @Tapeout，非新项目官号。未做第二读。
- discordPeekDeferred: false（本例行默认不登录 DC；开跑前 Discord 已占用本轮并补收 3 卡，例行合并进 R1777。未尝试登录）。
- DS: 例行 pace 无新收录候选送审，未另开 DeepSeek 批次。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: hooded-ape-club 首次官宣售罄 1500/1500（00:33:58 CST），不重推。lil-giraffies 本轮官宣 reveal LIVE（00:45:51 CST），铸造窗已过，不重推。polyrob 公开销售仍 11-14 22:00 CST，非 ≤2h；OS 29→31，不重推。oathbots 预售仍 OPEN，0.805→0.825 BNB / 27→28 钱包，不重推。HonestBull 已售仍 23/10000。boxcars 驾照 152→161/1000。ponke-agent 59→63/11055、免费 59→63/555。agx-402 unitsMinted 仍 10334，distributedAgx 仍 4.1336 亿，mintUnitPriceU 0.2656→0.2623，genesisClaims 仍 OPEN，voting 仍 NOT_OPEN，migrationDeadline 2026-11-14 16:00:58 CST。bagnotary 池储备约 3209 USD，成交约 2377 USD，R1775 已推开盘，不重推。
- watch-bug: Discord 三张新卡在库不在任何 Watch，已补进 userFollowWatch（@veltrixcodes / @Krypnous / @melaps_system）。均为台子/Meme（RH 代币类），未兼挂 agentPad/bnAgent/freeMint。历史漏挂仍约 1686 张；本轮未做整表回填。
- new cards: pace 无新卡。保留 Discord 本轮 newThisRound（veltrixcodes / krypnous / melaps-system）。meta.newThisRound == 顶层 newThisRound == round1777Added。candidateCount 仍 4202。挂 Watch 后 UF accounts=1674。

## 仍在跟（刷新，不重推）

- hooded-ape-club：官号于 2026-11-14 00:33:58 CST 官宣 WE ARE SOLD OUT（1,500 / 1,500），并称 REVEAL in 1 HOUR、UTILITY in 6 HOURS。01:03:12 CST 另发扫货帖。R1768 已推公开铸造 LIVE；本轮是售罄确认，不重推。OpenSea hoodedapeclub 1442→1500，sales 1440→1529，owners 547→541，floor 约 0.57 USDG。卡内 CA 0x6b1d830e… 与 OS 合约一致；公开 Robinhood RPC 仍 hasCode false。付费公铸，免费档此前已满。
- lil-giraffies：官号于 2026-11-14 00:45:51 CST 官宣 reveal is now Live，并说明 4 阶段成长。此前 00:15:47 CST 已官宣 Officially Sold Out（R1776 已记录）；铸造窗已过，本轮是揭示/游戏更新，不重推。卡内原 CA 0x20b25D… 公开 RPC 仍 hasCode false。OpenSea lil-giraffies-club 仍 6666，sales 8271→8827，owners 4395→4148，floor 约 4.09 USDG，合约 0x440c0d01…，与卡内原 CA 不同。
- polyrob：本窗 00:30:27 CST 官号再发 “Mint is live now”，内容是 6551 钱包身份说明，并非改期。公开销售仍为 11-14 22:00 CST，距公开销售仍约 21h，非 ≤2h。OpenSea 已铸 29→31；OS 索引合约 0xe0cfdd0f… 与卡内 CA 0xbBa60AB9… 不同，本轮不改写官方 CA。官网仍 SSL EOF。仍需 WL 才能打当前窗；公开销售尚未开始。
- oathbots：$OATH 付费预售仍 OPEN。链上 status=1，已存入 0.805→0.825 BNB / 27→28 钱包，finalized=False，50000000 枚 OATH 仍在预售合约内。窗口至 11-18 22:00 CST。非免费。R1773 已推。
- bagnotary：$BAGNOT 已开盘（R1775 已推）。Pons V2 池储备约 3209 USD，FDV 约 3215 USD，成交约 2377 USD（6h/24h 同值，近 1h 无成交）。官网仍 SSL EOF。付费发币。
- boolish-rh：Possession night 预约 23:00 CST 已过。本窗无官帖；boolish.fun 仍 200。未能核验是否已开铸。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，remaining=9977，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。非免费。
- boxcars：免费驾照仍开放，链上已领 152→161/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上 59→63/11055，免费 59→63/555，paid=0，gift=0，仍在免费档。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12… totalSupply 仍为 0。R1764 已通知，不单独重推。
- agx-402：付费 fair launch 仍 OPEN。unitsMinted 仍 10334，distributedAgx 仍 4.1336 亿，mintUnitPriceU 0.2656→0.2623。genesisClaims 仍 OPEN，voting 仍 NOT_OPEN。migrationDeadline 2026-11-14 16:00:58 CST。仍需 .ai Agent ID + Binance Agentic Wallet。本号不自动 mint。
- dripevm：白名单免费仍开。Elysium RPC 与 OpenSea drip-nft 仍 166/888；OS sales 150→157，owners 55→63，floor 仍 0.03 HYPE。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸仍 1497，sales 1838→1840，owners 仍 877，floor 约 0.00069 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea 仍 528/777，sales 663→664，owners 343，floor 约 0.00099 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1748→1779/2222，wallets 141→145，priceUsd≈2.60。不是免费窗。
- arctic-bear：链上已铸仍为 82/5555。
- clause-protocol：链上已铸仍为 9/7777。
- momo-mochi：链上已铸 299→300/2222。
- tsbdotfun：OpenSea the-shadow-born 仍 0。Discord 已通知，不重推。
- ashling：本轮未再补拉官帖。官网仍 SSL EOF。R1772 已通知 Pons 池与 CA，不重推。
- clankbots：Ink 免费白名单登记仍 LIVE，whitelist 页仍开放。R1772 已通知，不重推。

## 例行侧 skips

- MariaOnchainDev：LayerZero 关键词窗为跨链桥随笔，非新打新窗口，不收录。
- @Wizdeadrollx_：BTC 关键词窗 “DEADPOOL NINJA TURTLE” Ordinals “free mint” 宣传；作者为泛影响力账号，无已核验项目官号，未另耗 X 猎号，不收录。
- ShieldedNaka / OrdDropz 等 BTC 窗多为转推或已在库生态，不重开卡。
- Mentions BTC：@RGBHorse / @UnseenOrdo 等已在 Watch 的喊单帖，不另建卡。
- GIWA 窗 Ammora / globemkts 等已在库。
- DogeEVM 窗 Monko / Laika / BarkSwap 等为测试网/已在库生态，不收录新卡。
- Tape 窗 17 帖均为 @Blonskr 社区氛围，无新官号。
- Starknet 关键词窗本轮 4 帖均为 “Bramble” 鸟类/游戏误伤，无 Starknet 打新信号。MENT_STARK=0。
- silent Tape mentions：1 帖为 @9118Liwei 个人号提到 @Tapeout，sentToReview=0。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1777 merge）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
