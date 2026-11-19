# RESULT R1966

- time: 2026-11-19 13:20:16 CST
- mode: ample（R1956 为 08:00 CST 后首轮全量补扫；本轮为其后第十轮正常节流，lastFullAfterReset 仍为 R1956）
- xReads: 20（main 19 + silent 1 + EXTRA 0）
- remainingBefore: 782 → remaining: 762
- softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50
- tenLanes: yes（11 条关键词全跑，近 30 分钟，start_time 2026-11-19T04:37:00Z：LZ 1 / TAPE 12 / GIWA 9 / DOGE 15 / BTC 1 / SN 9 / MINT 25 / MINE 2 / PAD 25 / GO 25 / ELY 25。MINT、PAD、GO、ELY 触顶，未翻页。无 EXTRA。）
- userFollow: 刷完本分片，wrap=false。start 747 AIZOBsc，kept 50（AIZOBsc→axmi_bnb），walkScanned 67，NF_skip 17（SolumMrkt / bndoge_bn / oblaunchpadAll / babycz_ai / mint_WRIT / BinanceCanFly / Meteorszmint / AiPullpad / oblaunchpadbase / bianfenhong / dinomitesnft / Morumai_ / emberlingreal / TrineProtocol / LongAgentBNB / computeroll / btcliu205），skip_already 0。next 814 bnb_agent_dog。prio_folded 全部 7 个：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer / mobster_meme。窗口号 INMATES_RH / yuange99988852 / Oathbots / spiritsHOOD / Vice6fun 另 1 次 from:。本分片 UF 帖 UF1=0 / UF2=0，MUST=0，FAT_PAD=0。
- mentions: 本轮轮换子集 4 组 LayerZero 5（@LayerZero_Core @LaunchOnPangea @PlunderPort @ZeroVaultxyz @0padfun，25 帖触顶未翻页）/ Elysium+kinetiq 5（@Enter_Elysium @kinetiq_xyz @AgentKinetiq @AscendLaunch @elywatch，24 帖）/ mining-squeek+Nutshell 5（@squeekchain @NutshellMarkets @ComputeRollLabs @TracNetwork @squeektoshi，0 帖）/ BN Agent pads+STARX 5（@dotaipad @PulseLaunchpad @starx_xlayer @yinghubnb @gangdotfun，1 帖）。下一轮子集 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent: DogeEVM（1966%11=8；SILENT_MEN result_count=3，约 24h 窗；search_users 仍不可用）。未见需新收录的官方项目。下一轮 silent=BTC。
- watchLeaksFixed: []（新卡 founder 已进 userFollowWatch + agentPadWatch）
- fat cursors：agentPad 58→89（本轮 1 次 from: 分片，kept 25 LuckyCatsBNB→AgentPad_ai，跳过 computeroll/project_hoodmon/blindfloor，skip_already mobster_meme/bscaidrop/PulseLaunchpad，帖 0，wrap=false，next idbot_fun）；freeMint 66 / bnAgent 169 / elysium 283 未动
- discordPeekDeferred: true（DC 未登录）
- thinOfficialDeferred: true（本轮 ample 不打 THIN1–5 薄栏官号 from:）
- newThisRound: ["founder"]
- statusFlipThisRound: []
- le2hThisRound: []
- notify: true（真新收录 Founder，announced，不是免费 mint，无≤2h）
- xReadsExtra: 0。主扫 19 + silent 1 达到 minSpend 20、低于 softCap 28。开跑前 remaining 782（上轮结束后 784，间隔另有 2 次读取），读后 762。@FounderMkt 用户字段已在 KW_PAD includes 中，未另查。
- docsSynced: true

## 本轮判定

- **真新收录 Founder（@FounderMkt，founder，overall 58，status=announced，focus=false）。** 官网 https://founder.market/ 经 WebFetch/jina 可读（本机 curl 被 Cloudflare 403）与官推部分互证：资料栏 expanded_url 为 https://founder.market，jina/WebFetch 正文未见回链 @FounderMkt，siteXMutual=partial-x-to-site。账号 2026-11-19 10:44:51 CST 创建，未认证，0 粉、3 帖，xUserId=2123245303684050944。官帖（https://x.com/FounderMkt/status/2123281620094558587，2026-11-19 13:06:01 CST，本轮 30 分钟窗口内）称 The Founder launchpad will be live shortly. Please stand by。站点标题 Founder — The city is yours；文案 Trade in SOL. Launch coins paired with tokenized TTWO；LAUNCH PAIR 指向 Backpack Securities TTWO mint TTWofwAge91oFhZs7kpQdyrVRkmevgM88xijGvQFbKo；页内展示社区币 DCTY、GTA6 的 Jupiter 行情，并声明独立于 Rockstar Games 与 Take-Two。因此发射台按 announced（尚未官宣 live），不是免费 mint，无≤2h。DexScreener/pump.fun 上存在已交易的 $Founder 代币 CA B2qjRYNwgJzWy9TiHSw37J84cUBDCNcj6RdWcf55pump，但官网正文未列出，caUnverified=true，不视为已核验平台币。由本窗 KW_PAD 官帖发现。DeepSeek admit=true，overall 58，栏目 台子/Meme。非仓鼠/toychain，focus=false。已进 userFollowWatch + agentPadWatch。账号极新、0 粉、官网无可见回链、GTA 主题、CA 未上官网，风险高。本号不自动 mint。
- **skip / 不重收 Tzero @T0dotfun、Garasu、Spike__wtf、KGIWA、PlunderPort、EnterXLaunch**：均已在库。Garasu 白名单自 R1952 起已跟踪，mint 仍 2026-11-23 22:00 CST，无翻转。
- **skip Deadpool Ninja ordinals（furbi59360，netlify）** 与 Bramble/GTA/tip-bot/KOL 噪音。
- **defer StealthOS_xyz**：仅 24h silent 窗第三方提问，未另开 X 查询。
- **gmgm.fun / @gmgmdotfun**：同一已提醒 LIVE 发射台。$GMGM DexScreener 本轮观察时价约 $0.00002130，FDV/市值约 $19,706（上轮约 $21,948），流动性约 $9,269 / 53.37 SOL（上轮约 $9,836 / 57.06），近 1 小时成交约 $10,099。扭蛋程序 CA 仍未核验。不是免费 mint，不重推。
- **skip / 不重推 All in crypto / @allincrypto_ai**：同一已提醒开池窗口。链上 totalMinted 12760（上轮 12632，+128），opened=1，paused=0；本轮 nextPrice()/currentPrice() eth_call 仍回退，下档价按价格曲线本地估算约 0.0026 BNB；Pancake V2 官方对约 74.57 BNB（上轮约 62.16）；LB totalShares=12759、holderCount=1346（上轮 12624 / 1323；updatedAt 2026-11-19 13:10:52 CST）。不重推。
- **Arklis / @arklisdotapp**：同一已提醒 FCFS 领取窗口，API 仍 spotsTaken=11/150（与上轮相同），minXp=2000，不是无门槛公开免费 mint，不重推。
- **Unicorn Grand Prix / @UnicornGPrix**：白名单接口仍 open=true、phase=FCFS，count 522/15000（与上轮相同，剩 14778，used 222），不视为新翻转，免费 mint 日期仍 TBA，不重推。
- **Dead Zone / @DeadZonecrypto**：同一已提醒付费 mint LIVE，API 仍 open=true，minted=133/4500（与上轮相同），left 4367，VIP pack sold 仍 3，OG pack sold 仍 1，不视为新翻转，不重推。
- **VICE6 / @Vice6fun**：MUST 本窗 0 帖。大门仍 2026-11-20 08:00 CST（约 18.7 小时），CA 仍未公布，le2h=false，不重推。
- **the one（@yuange99988852）**：仍 announced。距 2026-11-19 19:00 CST 约 5.7 小时，le2h=false，尚未 LIVE，MUST 本窗无新开闸帖，不重推。
- **SpiritsRH**：免费 mint 窗口 2026-11-20 00:00 CST，距约 10.7 小时，le2h=false，MUST 0 帖，不重推。
- **Oathbots**：MUST 本窗 0 帖；代币窗口仍 2026-11-19 22:00 CST，距约 8.7 小时，le2h=false，不重推。
- **Boxcars / @BoxcarsHQ**：同一已提醒预售窗口，截止 2026-11-20 21:00 CST（约 31.7 小时，le2h=false）。不重推。
- **INMATES / @INMATES_RH**：同一已提醒窗口。MUST 本窗 0 帖。GTD 申请窗仍 2026-11-19 09:00–19:00 CST，约 5.7 小时后关，le2h=false；公开免费 mint 仍 2026-11-21 00:00 CST（约 34.7h）。暂无 CA。不重推。
- **AUGENT / @AugentFun**：同一已提醒免费 LIVE，链上 freeClaimed 711/2999（上轮 558，+153），paid sold 仍 1，paused=0，phase=1，pair 仍为 0，截止/开池仍 2026-11-21 20:52 CST（约 55.5 小时，le2h=false）。只更新进度，不重推。
- **Agent Miner / @AIMMinerBSC**：同一已提醒免费 LIVE，链上 totalMinted 仍 717，不重推。
- **AONE / @aone_agent**：同一已提醒开池/抽干窗口。链上 freeMinted 仍 10000/10000、hero 仍 22864；Pancake V2 对约 0.0097 BNB（与上轮相同），不重推。
- **Bsc Cat / @Bobkjyj**：同一已提醒免费 LIVE，freeMinted 554/800（上轮 550，+4），paid=0，pair 仍为 0，不重推。
- **DUCKS / @Duckslife9**：同一已提醒免费 LIVE，链上 minted 85/3000（上轮 81，+4），freeMinted=85，freeRemaining=415，paid=0，mintClosed=false。站点写 2026-11-20 11:00 CST 关（约 21.7h），链上 endTime 2026-11-23 11:00 CST（约 93.7h），非≤2h。不重推。
- **Fistagent / @Fistagent_（bonkagent）**：同一已提醒 mint LIVE，链上 totalMinted 仍为 4，本窗 FAT_PAD 0 帖，不重推。

## 覆盖与节流

- 判断/文案/打分一律 DeepSeek（deepseek-flash，思考开启）。DS 对 Founder admit=true、overall 58、栏目 台子/Meme、status=announced。无 DS fallback。
- 本号不自动 mint。
- 下一轮 mentions：Tape / GIWA / BTC / Starknet+DogeEVM；silent=BTC；UF next=814 bnb_agent_dog；agentPad next=89 idbot_fun。
