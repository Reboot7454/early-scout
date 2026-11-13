# RESULT R1774（Discord 占用 + 例行 pace 合并）

- time: 2026-11-13 23:42:41 CST（Asia/Shanghai）。开跑前 `git pull`，本地在 R1773（cd45155）。扫描期间 Discord 已于 23:36 CST 占用 R1774 并补收 orbyt / sonna-agent / holt / passage / pterodaktil / rushr（commit 2f40a44，已通知，不重推），故例行 pace 合并进同一轮，不另开 R1775。二次 `git pull` 后在 2f40a44 上应用 pace 刷新与 Watch 漏挂修复。notify=false。未自动 mint。
- mode: pace 合并进 discord-alpha-40（R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false。pace 本轮无新收录、无新确认免费 LIVE / 首次 ≤2h。Discord 六卡已在 23:36 CST 推送，不重推。禁止重推：bagnotary 仍 11-14 00:00 CST（R1770 已推 ≤2h；本窗官帖 23:30 CST 确认 Last stop: 30 minutes，未改期）；lil-giraffies / boolish-rh 预约 23:00 CST 已过，本窗仍无官帖，未能核验开铸（R1768 已推 ≤2h）；oathbots $OATH 预售仍 OPEN（R1773 已推；链上 0.725→0.775 BNB / 22→25 钱包）；hooded-ape / polyrob / Ashling / HonestBull / ponke-agent 及其它已推 LIVE 仅进度刷新。
- xReads: 22（main 21；silent 1；admitVerify 0）；remainingBefore 217 → remaining 195 / 1000；softCap 18，minSpend 18，silentCap 2；main 21 略超 softCap（UF×2 + 厚表分片×4 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + 核心 KW 合并 3 + mentionsThin×3 + mentionsRest×1，未砍栏），高于 minSpend。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。from: 官号窗 start_time=2026-11-13T15:15:00Z；关键词 / mentions start_time=2026-11-13T15:19:00Z。
- admitVerifyReads: 0。未为候选另耗 X 读。硬禁无官推核验：BambooRonin 555 免费 mint TBA、StinkyPenguinL0 弱 Layer Zero meme 等均不收录。oathbots / bagnotary / polyrob 进度来自本轮已拉官帖 + HTTP/RPC/OpenSea。lil-giraffies / boolish-rh 未另开 X 复核。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑。核心 KW 为控软顶合并为 3 路：打新+挖矿、台子+GO+GAPS 专名（不含 TapeOut，Tape 有独立薄栏）、Elysium 单独。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。帖量 meta.result_count：LayerZero 2、Tape 25（JSON 截断，抽到 3 帖）、GIWA 3、DogeEVM 17（截断，抽到 6 帖）、BTC 12、Starknet 4、打新挖矿 25（截断，抽到 6 帖）、台子GO 25（截断，抽到 5 帖）、Elysium 25（截断，抽到 5 帖）。部分 write_to_file 回包在约 6.5KB 截断，已用正则抽取完整帖，未为完整 JSON 重拉。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1，核心打新挖矿=1，核心台子GO（含 GAPS 专名）=1，核心 Elysium=1
- userFollow: 刷完本片 1230→1278，kept 48，skip 0，2 from: batches，本片 2 帖（UF1=0，UF2=2，Roomzzio/NVDA 无关）。下一轮从 1278 续（挂 Watch 后 UF accounts=1666；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 DogeEVM、BTC、Starknet（薄栏 mentionsThin）；rest 实际查询官号为 @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @flapdotsh / @irys_xyz / @fulldotfun / @arcxtrade / @dotaipad。均已跑，不翻页。帖量 MENT_DogeEVM 6、MENT_BTC 15、MENT_Starknet 10、MENT_REST 25（后三条 JSON 截断，已抽取）。
- fat shards: agentPad 126→154 kept 26 skip 2；freeMint 214→242 kept 25 skip 3；bnAgent 43→71 kept 17 skip 11（known_nf）；elysium 140→168 kept 27 skip 1。本窗 FAT 帖：agentPad 0、freeMint 1（Lanternhold 游戏补丁）、bnAgent 1（zaplonl $ZAP 11-18 Pancake 领取提醒，已在库）、elysium 0。下一轮 nextStarts：agentPad 154 / freeMint 242 / bnAgent 71 / elysium 168
- thin official watches: 2 个 from: 批次。本窗 THIN1=6 帖 / THIN2=1 帖（含 @bagnotary 倒计时、@tmachinroBot 27/6551、@agent_raise / @agent_octan / @strix_agents 产品或回复、Flizyapp emoji）。无 giraffies_nft / boolish_rh 官帖。
- silentAccounts: ran=true，lane=GO盘（round 1774 % 11 = 3；search_users unavailable，改跑 mentions `has:mentions ("GO launch" OR "AR launch") -is:retweet`，softCap 外 1 读）；回包 12 帖，均为英语口语 go launch 噪音。filter sentToReview=0、admitted=0。未做第二读。
- discordPeekDeferred: false（本例行默认不登录 DC；扫描期间 Discord 已占用本轮并补收 6 卡，lastSeen ~23:26 CST）。DC 跳过 mysubs / charon-protocol；alreadyInDb: VordaLaunch。
- DS: 例行 pace 无新收录候选送审，未另开 DeepSeek 批次。未编造 CA/官号/官网。未自动 mint。Discord 侧 admits=6 已由其本轮 deepseek-flash 完成并推送。
- MUST_TODAY: bagnotary 仍 11-14 00:00 CST，官帖确认未改期，R1770 已推，不重推。lil-giraffies / boolish-rh 预约 23:00 CST 已过但未能核验开铸，不作为已开铸通知。oathbots 预售仍 OPEN，0.725→0.775 BNB / 22→25 钱包，不重推。HonestBull 已售仍 23/10000。boxcars 驾照 145→148/1000。ponke-agent 47→49/11055、免费 47→49/555。agx-402 unitsMinted 仍 10325，distributedAgx 仍 4.1300 亿，mintUnitPriceU 0.2704→0.2685，genesisClaims 仍 OPEN，voting 仍 NOT_OPEN，migrationDeadline 2026-11-14 16:00:58 CST。hooded-ape-club 公铸仍 LIVE，OS 1342→1353/1500，不重推。polyrob 官帖 27、OS 22→28，不重推。
- watch-bug: Discord 六卡写入时均未进任何 Watch（监控 bug），本轮已补：orbyt @Orbyt3d、holt @holtrh_、passage @enterpassage、rushr @rushrtrade → userFollowWatch；sonna-agent @sonnaagent → userFollowWatch + agentPadWatch；pterodaktil @ptrdktlnft → userFollowWatch + bnAgentWatch + freeMintWatch。历史漏挂仍约 1686 张；本轮未做整表回填。
- new cards: 例行 pace 无新卡。newThisRound 保留 Discord 六卡 orbyt / sonna-agent / holt / passage / pterodaktil / rushr（不重推）。新卡规则仍 focus=false（六卡均未 focus）。candidateCount 4194（Discord 自 4188 增 6，pace 未再增）。

## Discord 已推（不重推）

- Orbyt（@Orbyt3d）：3D 引擎产品，官网 orbyt3d.space，本轮无官方 CA。
- Sonna Agents（@sonnaagent）：Robinhood Chain，官网 sonnarh.com，$SONNA 将上链，本轮无官方 CA。
- Holt（@holtrh_）：Robinhood Chain 钱包隐私扫描，官网 holtrh.xyz，$HOLT soon，本轮无官方 CA。
- Passage（@enterpassage）：Robinhood Chain 灵魂绑定 pass，不能买，需 ETH vouch，官网 enterpassage.xyz，本轮无已核验 CA。
- Pterodaktil（@ptrdktlnft）：BNB Chain Agent ID 项目，官网 pterodaktil.fun，官方 NFT CA 0x35dfeF79f25660F63471Fae76833b1E7D8Dd9750，本轮 Discord 记 totalSupply=62/1600；首次 mint 仅 SPACE ID Agent ID 持有人免费，其后阶梯付费。非本轮例行新发现，已推过，不重推。本号不自动 mint。
- Rushr（@rushrtrade）：Robinhood Chain，Beta 50 席，官网 rushr.trade / app.rushr.trade/trenches，本轮无官方 CA。

## 仍在跟（刷新，不重推）

- oathbots：$OATH 付费预售仍 OPEN。链上 status=1，已存入 0.725→0.775 BNB / 22→25 钱包，5000 万枚 OATH 仍在预售合约内。窗口至 11-18 22:00 CST。非免费。R1773 已推。
- bagnotary：仍定 2026-11-14 00:00 CST（16:00 UTC）于 Pons 发 $BAGNOT。本窗官帖 23:30 CST 确认 Last stop: 30 minutes，未改期。官网 bagnotary.pro 仍 SSL EOF。R1770 已推。
- hooded-ape-club：公开铸造仍 LIVE。OpenSea 1342→1353/1500，sales 1358→1362，owners 535→537，floor 约 0.14 USDG。付费公铸，免费档已满。公开 Robinhood RPC 仍失败。
- polyrob：白名单铸造仍 LIVE。本窗官帖 23:31 CST：27 of 6,551 minted，Allowlist 仍余约 22h，0.033 ETH。OpenSea 已铸 22→28，owners 7→12，sales 0。卡内 CA 0xbBa60AB93Fc409b1A34371CBF6c3173795Ed2c7e，OS 合约 0xe0cfdd0f7ec8bba180e7cdea93e521ddcba4f63a，未裁定哪个为铸造合约。仍需 WL，非免费公铸。官网 polyrob.xyz 仍 SSL EOF。
- lil-giraffies：预约 23:00 CST 已过。本窗无 @giraffies_nft 官帖；官网仍写 Join the Lil whitelist。原记 CA 0x20b25DA8785990CC89330AF56310024Bb199CD36 公开 RPC 仍 hasCode false。本轮发现 OpenSea 集合 lil-giraffies-club（verified）total_supply=5654，sales=6538，owners=4558，floor 约 5.5 USDG，合约 0x440c0d01b8d1065446dc178a42e213e6d3b15686（Robinhood，created 2026-11-09），与卡内原 CA 不同；近 24h sales 很高，但无本窗官帖确认这就是 23:00 开铸，不以该集合当作已核验开铸。
- boolish-rh：Possession night 预约 23:00 CST 已过。本窗无官帖；boolish.fun 仍为文化页、无铸造 CTA；公开 RPC 失败，OpenSea 集合未找到。未能核验是否已开铸。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，remaining=9977，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。非免费。
- boxcars：免费驾照仍开放，链上已领 145→148/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上 47→49/11055，免费 47→49/555，paid=0，gift=0，仍在免费档。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12DB0F8F5816750Eb2A4ac6076FDb912d3 totalSupply 仍为 0。R1764 已通知，不单独重推。
- GateCerberus：本窗无新官帖更新已售数。R1762 已通知，不单独重推。
- Freememe：应用已 LIVE。本窗无新开铸官帖。R1762 已通知，不作为新 mint 窗重推。
- agx-402：付费 fair launch 仍 OPEN。unitsMinted 仍 10325，distributedAgx 仍 4.1300 亿，mintUnitPriceU 0.2704→0.2685。genesisClaims 仍 OPEN，voting 仍 NOT_OPEN。migrationDeadline 2026-11-14 16:00:58 CST。仍需 .ai Agent ID + Binance Agentic Wallet。本号不自动 mint。
- dripevm：白名单免费仍开，Elysium RPC 与 OpenSea drip-nft 本轮均为 165/888。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸 1484→1485，owners 874→875，sales 1824→1826，floor 约 0.00080 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea 仍 528/777，owners 349→346，sales 653→658，floor 约 0.0010 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1737→1742/2222，wallets 138→139，priceUsd≈2.57。不是免费窗。
- arctic-bear：链上已铸仍为 82/5555。
- clause-protocol：链上已铸仍为 9/7777。
- momo-mochi：链上已铸仍为 299/2222。
- tsbdotfun：OpenSea the-shadow-born 仍 0。Discord 已通知，不重推。
- ashling：本轮未再补拉官帖。官网仍 SSL EOF。R1772 已通知 Pons 池与 CA，不重推。
- zaplonl：本窗官帖称 $ZAP 于 11-18 上 PancakeSwap；未领取的 Pass 在开池时销毁对应 500,000 $ZAP。824 Passes minted，101 claimed。已在库，仅刷新。

## 例行侧 skips

- BambooRonin：关键词窗出现 555 免费 mint TBA。不在库。本轮未见已核验官号原文，未另开 X 核验 handle（硬禁误判无官推），mint 时刻 TBA，不收录。
- StinkyPenguinL0：弱 Layer Zero meme，粉很少，无已核验官网/官推可操作窗口，不收录。
- StarXCoreTeam CMC 上币帖：不是 @starx_xlayer 本体，不另建卡。
- 已在库第三方/活动：PotionRh、PlunderPort、PlayEverMagic、Gangstazfun 17:00 UTC 讨论、EtchydotFun、RGBHorse、sasapadfun（sasa-pad）不重开卡。
- SquidKorea：GIWA 测试网基建，非打新窗口。
- silent GO mentions：12 帖均为英语口语 “go launch …” 噪音，sentToReview=0。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1774 merge）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
