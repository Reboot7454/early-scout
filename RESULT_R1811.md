# RESULT R1811（Discord 补漏 + 例行 ample X 扫描合并）

- time: 2026-11-14 17:46 CST（Asia/Shanghai）。开跑前远程已是 R1811（ca3c719，Discord alpha 补收 nihilo / petrichor / janzeer，17:42 CST，notify=true，已通知不重推）。例行不另起轮次，ample X 扫描合并进同一轮。notify=true（例行新收录 ember-pow 为每日首根木免费 LIVE；usemodul 为真新台子）。未自动 mint。
- mode: ample。首探 `search_posts_all` 第一读之后页脚为 600 of 1000，故 remainingBefore=601（与 R1810 收尾 601 衔接；R1811 Discord 所称 938→930 与本工具日额页脚不一致，本轮以 search_posts_all 页脚为准）。softCap=28，minSpend=20，silentCap=2，ufAccountShard=50。不是 08:00 CST 后全量补扫（全量已在 R1792 完成）。
- lastFullAfterReset: R1792
- notify: true。例行新收录 2：ember-pow（挖矿，BNB Chain，每日第一根木免费 LIVE，overall 64，即便 <70 也必须提醒）、usemodul（台子/Meme，Solana，今日新建 0 粉，官网已上、$MODUL CA 未公布）。无首次进入 ≤2h 倒计时开窗。le2hCurrent 仍为空。Discord 本轮已通知的 nihilo / petrichor / janzeer 不重推，仅清 newThisRound 徽章，并补挂进 userFollowWatch（开跑后发现三卡均不在任何 Watch，属监控 bug，当场修复）。本号不自动 mint。
- xReads: 23（main 20；silent 1；admitVerify 2）；remainingBefore 601 → remaining 578 / 1000；softCap 28，minSpend 20，silentCap 2；main 20 未超 softCap，已达 minSpend（UF×3 + MUST×2 + 薄栏 KW×6 + 核心栏 KW×5 + mentions×4；另 silent×1，admitVerify 2 为 @EmberPoW / @usemodul `get_users_posts`）。官网 / HTTP / 链外只读无 X 成本。UF / silent start_time=2026-11-13T09:30:00Z；MUST/窗口官号 start_time=2026-11-14T09:00:00Z；关键词 / mentions start_time=2026-11-14T08:55:00Z。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。search_users 本轮仍不在 X 工具目录，silent 仅 mention 路径。部分 25 条结果的 write_to_file 在约 6.5KB 处截断，已用完整对象文件修复解析，未重查同一 query。
- admitVerifyReads: 2。仅核验本轮拟收官号 @EmberPoW、@usemodul（`get_users_posts`；资料已在关键词/搜索结果中拿到的不重拉 `get_users_by_usernames`）。未对已读官号重拉。
- tenLanes: true。薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）+ 核心栏 5 条（mint / mine / pad / GO / Elysium）均已跑。未跑 KW_GAPS（R1792 全量已覆盖）。未刷薄栏官号 from: 与四表 FAT 分片：R1792 post-reset-full 已刷完，本轮 ample 增量只保 UF+MUST/窗口 + 十栏 KW + mentions 轮换（LayerZero、Elysium+kinetiq、mining-squeek+Nutshell、BN Agent pads+STARX）。meta.fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。
- laneReads: 薄栏 KW 各 1，核心栏各 1，mentions 轮换 4 批各 1。silent 1（GIWA 提及路径）。
- userFollow: 刷本片 1284→1334，kept 50，skip 0，另优先软刷 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets；priority 已知 NF 跳过 mobster_meme / starx_xlayer（未再读）。3 个 from: 批次。UF accounts 1751→1756（补挂 Discord 三卡 + ember-pow + usemodul），pending 仍空。下一轮从 1334 续。wrap=false。同时把 meta.ufCursor 与 userFollowWatch.cursor 一并写到 1334。已在库不重推：Sevenbsc 免费 mint 仍在推进；agentmarketbnb 首档免费需 Agent ID、预售至 11-24 11:30 UTC；machinedotfun Docking coming soon；use_stoke 镜像池称明日。
- mentions: 本轮轮换子集，未全链全扫。已跑：LayerZero（@LayerZero_Core / @LayerZero_Labs / @PlunderPort / @0rigindotfun / @globemkts）；Elysium+kinetiq（@Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @AscendLaunch）；mining-squeek+Nutshell（@squeekchain / @NutshellMarkets / @ComputeRollLabs / @hamsterhourgame / @squeektoshi）；BN Agent pads+STARX（@dotaipad / @yinghubnb / @Ptahtrade / @gangdotfun / @PulseLaunchpad / @starx_xlayer / @pipfun_xyz / @Leeonmort / @bscaidrop）。Tape、GIWA、BTC、Starknet+DogeEVM 本轮未再扫（R1810 刚覆盖）。
- fat shards: 本轮未刷，cursors 不变。
- thin official watches: 本轮未刷薄栏官号 from: / FAT。MUST/窗口官号 2 批（含 dusktape / burybud / AgentCatRh / Ape_CityRH / DualForgeBSC / mizukaironft / pickhash_bnb / tmachinroBot / ShinobRH / GTAFiPad / UseVledge / theflyingcareco / pillowbookRH，以及 JustGivingPad / foodcoinpf / Puppet_pro / thejenslax / nave_hl / Zero_Kitties / playraidfolk / hwandotio / boostockxyz / kinetraagent / securityum_xyz / lontralaunchxyz / 0utdotfun / eserchain / brewpadlat）。MUST 本窗见到 Ape_CityRH 再澄清 TOKEN 而非 NFT、playraidfolk「Today the outlaws open it」但站点仍是 waitlist，均不重推。polyrob / agent-cat / burybud / dusktape / DualForge / pickhash / mizukairo / flyingcar / shinob / gtafi / pillowbook 本窗无新开窗官帖。
- silentAccounts: ran=true，lane=GIWA，silentCap=2 本轮用 1（search_users 仍不可用，仅 mention 路径）。见到 Ammora 等候名单刷屏与已在库 GIWA / Numen / UnseenOrdo 讨论，无独立静号新卡。sentToReview=0，admitted=0。
- discordPeekDeferred: false（开跑前 Discord 已完成 R1811 补收 nihilo / petrichor / janzeer，17:42 CST；本例行默认不登录 DC）。
- DS: deepseek-flash，思考开启。max_tokens=4096。对 ember-pow 给出 admit=true、挖矿、overall=64（early 62 / actionable 76 / novelty 68 / risk 66）；对 usemodul 给出 admit=true、台子/Meme、overall=40（early 72 / actionable 26 / novelty 54 / risk 72）。dsFallback=false。未编造 CA/官号/官网。未自动 mint。
- watch-bug: Discord 本轮新收的 nihilo / petrichor / janzeer 开跑时不在任何 Watch，已补进 userFollowWatch。例行新卡 ember-pow 进 UF + miningWatch + agentMiningWatch；usemodul 进 UF。软债 cantonPadWatch / glazeWatch / tokenWorksPlaygroundWatch / cantonWatch / tokenWorksWatch / flapPadWatch lastChecked 已刷新。
- skip / 未收：analosorg（@analosorg，约 6.3h，analos.org 200，app-config 空，玩笑向 Solana fork meme，无存活网络/CA）；alphamorpheus（站点 CA TBA 与 bio CA 冲突，不收）；vekta0x（vekta.one 写 CA 未公布 / Pons soon / 15.11 Soon，与推文「45% on curve」矛盾，不按已开盘收，亦无 ≤2h 时钟）；zolkdotio（zolk.io 现已标明官推 @zolkdotio，R1804「无官推」原因已消除，但号龄约 22 天、108 粉，白名单森林已开、自称 LZ 主网收藏仍未上链，仍偏晚 announced，本轮不收）。大量 Ammora 等候名单垃圾号、InsomniaCoinSOL / LayerZeroInu / sakaladva 跳过。tradeTopo（topo.wtf HTTPS 失败/HTTP 500）仍推迟。Vault Pass 仍无可靠官推，不收。
- new cards: 例行 2 个（ember-pow、usemodul）。meta.newThisRound == 顶层 newThisRound == ["ember-pow", "usemodul"]。round1811Added == ["nihilo", "petrichor", "janzeer", "ember-pow", "usemodul"]（Discord 三卡已通知，不重推、只清徽章）。candidateCount=4274。UF accounts=1756。

## Discord 本轮（17:42 CST 已完成并通知，不重推）

- 补收 nihilo（@nihilo_fun）：台子/Meme。任务页可交互，官帖称实验约 11-16 06:01 CST 开始；自称 LZ 未核验。
- 补收 petrichor（@petrichorbio_）：台子/Meme。$PETRIC 称今日在 Pons 上线，官网为 YC F2026 湿实验室，与代币关系未互证。
- 补收 janzeer（@JanzeerOrg）：打新。已运行约 6 周的小型 L1，JNZ 无市价。
- coverage: #alpha-3-new-accounts + #alpha-1-backup + #smart-accounts-tracker + #alpha-1。loginOk=true。扫卡 lastSeen 之后 28 张 / 23 个独立号。lastSeenByChannel→alpha-3 17:13、backup 17:04、smart 17:13、alpha-1 16:59。Discord 侧 X 核验读 8，其所称 remaining 938→930 与本工具日额页脚不一致。

## 本轮例行新收

- ember-pow（@EmberPoW，挖矿，BNB Chain，live，overall 64，focus=false）：官网 emberpow.xyz 200，官号与 twitter:site 一致。BSC CA 0x5898AD3b7578BF244F9940e860A1051647996633 有码。globalInfo：已开矿、强火、第 2 轮、deaths=1、totalWoods=136、lpOpen=false、lpEscrow 仅约 0.00025 BNB（目标 3 BNB）。需 SPACE ID / Binance Agent ID；每 UTC 日最多 5 根木，价格 0 / 0.0005 / 0.001 / 0.002 / 0.004 BNB，第一根仅 gas。下次免费重置 11-15 08:00 CST。开矿始于 11-12 23:00 CST（已约 42.7h），非倒计时开窗，但是雷达首次收录的免费 LIVE。风险：X 号 2024-03 旧号；付费木 50% BNB 立刻进 owner；开池后 2% 税 + 团队 100M 全解锁。与库内 feedthefirerh / @FeedTheFireRH（Robinhood）不是同一项目。
- usemodul（@usemodul，台子/Meme，Solana，watching，overall 40，focus=false）：官号 2026-11-13 20:22 UTC（约 11-14 04:22 CST）新建，蓝V，0 粉 / 2 帖。官网 usemodul.xyz 200，与官号互链。定位为规则型 pump.fun 发射台（分润/回购/金库/销毁/投票先仿真再发射）。17:30 CST 官帖首发。$MODUL CA coming soon，非免费 NFT mint，无可交互开窗，先观察。

## 已在库进度（不重推）

- polyrob（@tmachinroBot）：本窗无新官帖。公开销售仍 11-14 21:52 CST（约 4.1h），白名单付费窗同时到期。付费窗，非免费、非 ≤2h。
- agent-cat（@AgentCatRh）：本窗无新官帖。Launch 仍 11-14 21:00 CST（约 3.2h），非 ≤2h。
- burybud（@burybud）：本窗无新开窗官帖。档期仍 11-14 23:00 CST（约 5.2h），非 ≤2h。
- dusktape（@dusktape）：本窗无新开窗官帖。开窗仍 11-15 00:00 CST（约 6.2h），非 ≤2h。
- dualforge-bsc（@DualForgeBSC）：本窗无新开窗官帖。Mint 仍 11-15 19:00 CST（约 25.2h），非 ≤2h。
- ape-city（@Ape_CityRH）：17:00–17:10 CST 官号再澄清今日发 TOKEN 而非 NFT、NFT 另行宣布，与 R1806/R1810 口径一致，仍无官网/CA/精确时钟，不预推。
- raidfolk（@playraidfolk）：17:07 CST 官帖称 Today the outlaws open it，但官网 raidfolk.io 仍为 waitlist / Soon，未见可铸入口或 CA，不重推。
- pickhash / mizukairo：免费首铸仍按已推口径；本窗窗口官号无新开铸帖。
- theflyingcar-bnb / usevledge / pillowbook-rh / shinob-rh / gtafi / nihilo / petrichor / janzeer：均已通知，不重推。

面板：https://reboot7454.github.io/early-scout/
