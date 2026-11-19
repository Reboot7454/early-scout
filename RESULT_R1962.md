# RESULT R1962

- time: 2026-11-19 11:18:19 CST
- mode: ample（R1956 为 08:00 CST 后首轮全量补扫；本轮为其后第六轮正常节流，lastFullAfterReset 仍为 R1956）
- xReads: 21（main 19 + silent 1 + EXTRA 1）
- remainingBefore: 865 → remaining: 844
- softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50
- tenLanes: yes（11 条关键词全跑，近 30 分钟，start_time 2026-11-19T02:33:36Z：LZ 1 / TAPE 12 / GIWA 1 / DOGE 1 / BTC 7 / SN 3 / MINT 25 / MINE 1 / PAD 12 / GO 25 / ELY 19。MINT/GO 触顶，未翻页。部分 write_to_file 预览中段省略，已从完整 companion 文件回收全部帖，未重查）
- userFollow: 刷完本分片，wrap=false。start 493 OmbrelloNFT，kept 50（OmbrelloNFT→balboa_studios），walkScanned 59，NF_skip 9（rheacatnear / 99901dotfun / magnitudeagent / bububullfun / lanternfield / streamlitmaker / trycortano / hook404rh / agentpunkai），skip_already 0。next 552 klll_floor。prio_folded 全部 7 个：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer / mobster_meme（含上轮跳过的 mobster_meme）。窗口号 INMATES_RH / yuange99988852 / Oathbots / spiritsHOOD / Vice6fun 另 1 次 from:。本分片 UF 帖 UF1=0 / UF2=0，MUST=0。
- mentions: 本轮轮换子集 4 组 LayerZero 5（@LayerZero_Core @LaunchOnPangea @PlunderPort @ZeroVaultxyz @0padfun，25 帖触顶）/ Elysium+kinetiq 5（@Enter_Elysium @kinetiq_xyz @AgentKinetiq @AscendLaunch @elywatch，15 帖）/ mining-squeek+Nutshell 5（@squeekchain @NutshellMarkets @ComputeRollLabs @TracNetwork @squeektoshi，1 帖）/ BN Agent pads+STARX 5（@dotaipad @PulseLaunchpad @starx_xlayer @yinghubnb @gangdotfun，0 帖）。下一轮子集 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent: LayerZero（1962%11=4；SILENT_MEN result_count=25 触顶，约 24h 窗；search_users 仍不可用）。未见需新收录的官方项目（@stinky-penguin 已在库旧帖）。下一轮 silent=Elysium。
- watchLeaksFixed: []（新卡 arklis 已进 userFollowWatch + freeMintWatch）
- fat cursors：agentPad 755→780（本轮 1 次 from: 分片，kept 25 ReceiptHash→RimeGlow，帖 1 为 @BoxcarsHQ 同预售窗口，next Testudo_rbh）；freeMint 66 / bnAgent 169 / elysium 283 未动
- discordPeekDeferred: true（DC 未登录）
- thinOfficialDeferred: true（本轮 ample 不打 THIN1–5 薄栏官号 from:）
- newThisRound: ["arklis"]
- statusFlipThisRound: []
- le2hThisRound: []
- notify: true（真新收录 Arklis，Early Access Pass FCFS 领取已 LIVE，虽有 2000 XP 门槛、不是无门槛公开免费 mint，仍按免费领取/登记窗口已开必须 notify。overall 84。无≤2h）
- xReadsExtra: 1（get_users_by_usernames 核验 @arklisdotapp）。主扫 19 + silent 1 达到 minSpend 20、低于 softCap 28。开跑前 remaining 865，读后 844。

## 本轮判定

- **真新收录 Arklis（@arklisdotapp，arklis，overall 84，status=live，focus=false）。** 官网 https://arklis.app/ 与官推互证（资料栏 URL 解析为 arklis.app；页脚 JS 硬编码 https://x.com/arklisdotapp，claim 页 JS 常量 Q=arklisdotapp）。账号 2026-09-07 01:43 CST 创建，蓝V，16636 粉、8363 帖，bio「Where ideas become markets. Launch tokens, share your vision, and trade — all in one place.」。官帖（https://x.com/arklisdotapp/status/2123043938525155593，2026-11-18 21:21 CST）写 Early access is live. Claim your pass，并带 https://arklis.app/claim。claim 页 HTTP 200：New spots are live. First come, first served；OG 写 Arklis Genesis Collection: 333 NFTs, free mint, and 60% of protocol fees to holders。公开 API https://arklis.app/api/fcfs 返回 spotsCap=150、spotsTaken=11、minXp=2000，即 FCFS 窗口已开（11/150），需 2000 XP。站点文案还有 Follow @arklisdotapp、Claim yours、It lands in your wallet over the coming hours。首页 /trade 自称 Trade live on Robinhood Chain。CA 未核验。由本窗 KW_MINT 第三方 @MikdarSmith 引用官帖发现。官帖本身约在 R1939/R1940 窗口，当时关键词未必覆盖 early access / claim your pass，属可能漏收，本轮补录。DeepSeek admit=true，overall 84，栏目 台子/Meme。非仓鼠/toychain，focus=false。按免费领取/登记窗口已开必须 notify，但须标明不是无门槛公开免费 mint。本号不自动 mint。
- **skip Floats / @floats37**：官网 floats.trade HTTP 200 与官推互证，极新号（2026-11-17，60 粉），合约 0x50187d5b6fdd6d39e89f30a161d77a6956fef437，Robinhood 链上实时 ERC-4626 IPO 指数金库，可 Connect wallet。本窗官帖在讲 LayerZero omnichain 计划，不是免费 mint。DeepSeek admit=false（overall 60），不建卡。
- **skip GEARVAULT / @GearVaultNFT**：官网 gearvault.fun 与官推互证，2026-11-14 创建、237 粉；2222 把武器 NFT，页面写 Mint · soon，价格/日期 TBA；站内 Free crate 为 off-chain，不是钱包 mint。DeepSeek admit 关口 skip（打分 admit=true、overall 58，本轮以 admit 关口为准），不建卡，维持观察。
- **skip DANDI / @dandi_fun**：官网 dandi.fun 与官推互证（twitter:site=@dandi_fun），自称 coming to Zero、Live day one of Zero mainnet，发射台尚未上线。DeepSeek admit=false（overall 54），不建卡。
- **skip FounderTrading / founder.bz**：账号当日创建、9 粉，页面几乎为空，站点无官推链接，Larpcheck 称 sketchy，已跌约 72%，不建卡。
- **skip QuoteZero_ / LayerFee_DeFi**：无官网，不建卡。
- **skip edeldotfinance**：2.2 万粉、2025 年账号，非早期。
- **skip NucleusCodes**：2022 年分发层，非早期打新。
- **skip / 不重推 Boxcars / @BoxcarsHQ**：本窗 FAT_PAD 分片见到官帖，仍为同一已提醒预售窗口，截止 2026-11-20 21:00 CST（约 33.7 小时，le2h=false）。本轮未重新拉 licence 链上计数，不重推。
- **skip / 不重推 zeru-finance**：已在库 upcoming 3333 RH 免费 mint，本窗仅第三方活动讨论，无官方 LIVE 确认，不重推。
- **skip / 不重推 Fistagent / @Fistagent_（bonkagent）**：同一已提醒 mint LIVE，链上 totalMinted 仍为 4，不重推。
- **skip / 不重推 teseralab / vibe / beepz / spike-wtf / plunderport / Aurum Desk**：已在库或同窗口，无新翻转，不重推。
- **The Notties / @thenottiesworld**：官网口径同前轮，不视为新的免费登记翻转，不重推。
- **8BITS HOOD / @8bitshood**：仍 announced，不重推。
- **Unicorn Grand Prix / @UnicornGPrix**：白名单接口仍 open=true、phase=FCFS，count 520/15000（上轮 519，+1，剩 14780），不视为新翻转，免费 mint 日期仍 TBA，不重推。
- **Dead Zone / @DeadZonecrypto**：同一已提醒付费 mint LIVE，API 仍 open=true，minted=119/4500（上轮 118，+1），VIP pack sold 仍 3，OG pack sold=1（上轮 0），0.01 SOL/份，不视为新翻转，不重推。
- **VICE6 / @Vice6fun**：仍 PRE-LAUNCH，距 2026-11-20 08:00 CST 约 20.7 小时，le2h=false，CA 未公布，MUST 0 帖，不重推。
- **the one（@yuange99988852）**：仍 announced。距 2026-11-19 19:00 CST 约 7.7 小时，le2h=false，尚未 LIVE，MUST 0 帖，不重推。
- **SpiritsRH**：免费 mint 窗口 2026-11-20 00:00 CST，距约 12.7 小时，le2h=false，MUST 0 帖，不重推。
- **Oathbots**：代币窗口 2026-11-19 22:00 CST，距约 10.7 小时，le2h=false，MUST 0 帖，不重推。
- **Just Headz / @JustheadzHQ**：同一已提醒白名单已开窗口，本窗未见 mint LIVE，不重推。
- **GTAFounder / @GTAFounder**：同一已提醒 LIVE 窗口，仍以已核验平台币 CA ALtBh7RxCc98sp6vG4EmMQ1VFWfvoWSTvUPqyFwmGTA6 为准，不重推。
- **Zolk / @zolkdotio**：同一已提醒森林寻卡白名单窗口，未见 mint/CA，不重推。
- **rooms.fun / @shroomsdotfun**：同一已提醒 LIVE 发射台，未见新翻转，不重推。
- **INMATES / @INMATES_RH**：同一已提醒窗口。GTD 申请窗仍 2026-11-19 09:00–19:00 CST，约 7.7 小时后关，le2h=false；表单仍只写本机 localStorage，页面仍写明不向团队提交，暂无 CA。MUST 0 帖。不重推。
- **AUGENT / @AugentFun**：同一已提醒免费 LIVE，链上 freeClaimed 349/2999（上轮 292，+57），paid sold 仍 1，paused=0，phase=1，pair 仍为 0，截止/开池仍 2026-11-21 20:52 CST（约 57.6 小时，le2h=false）。只更新进度，不重推。
- **Agent Miner / @AIMMinerBSC**：同一已提醒免费 LIVE，链上 totalMinted 716（与上轮相同），不重推。
- **AONE / @aone_agent**：同一已提醒开池/抽干窗口。链上 freeMinted 仍 10000/10000、hero 仍 22864；Pancake V2 对约 0.0097 BNB（与上轮相同），不重推。
- **All in crypto / @allincrypto_ai**：同一已提醒开池窗口。链上 totalMinted 11525（上轮 11297，+228），opened=1，paused=0；本轮 nextPrice()/currentPrice() eth_call 仍回退，下档价按价格曲线本地估算约 0.0024 BNB；Pancake V2 官方对约 67.63 BNB（上轮约 52.05）；LB totalShares=11365、holderCount=1101（上轮 11318 / 1022；updatedAt 2026-11-19 10:56:50 CST，接口已刷新，略低于链上）。不重推。
- **Bsc Cat / @Bobkjyj**：同一已提醒免费 LIVE，freeMinted 550/800（与上轮相同），paid=0，pair 仍为 0，不重推。

## 覆盖与节流

- 判断/文案/打分一律 DeepSeek（deepseek-flash，思考开启）。DS 对 Arklis admit=true、overall 84、栏目 台子/Meme。Floats / DANDI admit=false。GEARVAULT 打分 admit=true 但 admit 关口 skip，本轮不建卡。无 DS fallback。
- 本号不自动 mint。
- 下一轮 mentions：Tape / GIWA / BTC / Starknet+DogeEVM；silent=Elysium；UF next=552 klll_floor。
