# RESULT R1964

- time: 2026-11-19 12:14:45 CST
- mode: ample（R1956 为 08:00 CST 后首轮全量补扫；本轮为其后第八轮正常节流，lastFullAfterReset 仍为 R1956）
- xReads: 20（main 19 + silent 1 + EXTRA 0）
- remainingBefore: 824 → remaining: 804
- softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50
- tenLanes: yes（11 条关键词全跑，近 30 分钟，start_time 2026-11-19T03:30:00Z：LZ 0 / TAPE 25 / GIWA 7 / DOGE 16 / BTC 3 / SN 3 / MINT 25 / MINE 2 / PAD 18 / GO 23 / ELY 16。TAPE、MINT 触顶，未翻页。无 EXTRA。）
- userFollow: 刷完本分片，wrap=false。start 620 orenfinance_，kept 50（orenfinance_→oil_hood），walkScanned 65，NF_skip 15（agentharvest_ai / seatworkcells / NidavellirBSC / frogsagent / Honestcoin60 / DropMinters / onbeatfun / lettucegrow_rh / beatdotfamily / nonamespnft / heyribbid / inkwellonbnb / certuna_rh / miuadotfun / origopad），skip_already 0。next 685 pumpgld。prio_folded 全部 7 个：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer / mobster_meme。窗口号 INMATES_RH / yuange99988852 / Oathbots / spiritsHOOD / Vice6fun 另 1 次 from:。本分片 UF 帖 UF1=0 / UF2=1（Type_SOL 工具链帖，非 mint），MUST=0。
- mentions: 本轮轮换子集 4 组 LayerZero 5（@LayerZero_Core @LaunchOnPangea @PlunderPort @ZeroVaultxyz @0padfun，25 帖触顶）/ Elysium+kinetiq 5（@Enter_Elysium @kinetiq_xyz @AgentKinetiq @AscendLaunch @elywatch，14 帖）/ mining-squeek+Nutshell 5（@squeekchain @NutshellMarkets @ComputeRollLabs @TracNetwork @squeektoshi，0 帖）/ BN Agent pads+STARX 5（@dotaipad @PulseLaunchpad @starx_xlayer @yinghubnb @gangdotfun，1 帖）。下一轮子集 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent: Tape/电路（1964%11=6；SILENT_MEN result_count=3，约 24h 窗；search_users 仍不可用）。未见需新收录的官方项目。下一轮 silent=GIWA。
- watchLeaksFixed: []（新卡 acruxhub 已进 userFollowWatch；mercatura 已进 userFollowWatch + miningWatch）
- fat cursors：agentPad 8→33（本轮 1 次 from: 分片，kept 25 LuckyAgent_bsc→BAi_Binance，跳过 0，帖 0，wrap=false，next Leeonmort）；freeMint 66 / bnAgent 169 / elysium 283 未动
- discordPeekDeferred: true（DC 未登录）
- thinOfficialDeferred: true（本轮 ample 不打 THIN1–5 薄栏官号 from:）
- newThisRound: ["acruxhub", "mercatura"]
- statusFlipThisRound: []
- le2hThisRound: []
- notify: true（真新收录 2 个，都不是免费 mint，仍按真新收录必须 notify。无≤2h）
- xReadsExtra: 0。主扫 19 + silent 1 达到 minSpend 20、低于 softCap 28。开跑前 remaining 824，读后 804。@AcruxHub / @MercaturaCore 用户字段已在 KW includes 中，未另查。

## 本轮判定

- **真新收录 AcruxHub（@AcruxHub，acruxhub，overall 64，status=testnet，focus=false）。** 官网 https://acruxhub.com/ HTTP 200 与官推互证（资料栏 https://t.co/rXJiW77F7w 解析为 https://acruxhub.com；前端 JS 硬编码 `qe={x:"https://x.com/AcruxHub",github:"https://github.com/acruxhub/acruxhub"}`，页脚 AcruxHub on X）。账号 2026-11-18 08:48 CST 创建，未认证，9 粉、22 帖。官帖（https://x.com/AcruxHub/status/2123260352519692325，2026-11-19 11:41 CST，本轮 30 分钟窗口内）称 AcruxHub is live on Acrux Net: pump-style, one screen, liquidity locked forever at graduation. Free test tokens for now。产品是独立于 Acrux 官方的泵盘/债券曲线发射台+DEX（FAQ：Is AcruxHub part of Acrux? No.），报价币为 AXB；RPC https://rpc.acrux.computer，水龙头 https://acrux.computer/faucet。站点写明仍在用测试资金，尚无真实资产桥（bridge waits for independent security review）。不是无门槛公开免费 mint，也没有已核验的主网代币 CA。由本窗 KW_PAD 官帖发现。DeepSeek admit=true，overall 64，栏目 台子/Meme。非仓鼠/toychain，focus=false。已进 userFollowWatch。本号不自动 mint。
- **真新收录 Mercatura（@MercaturaCore，mercatura，overall 71，status=announced，focus=false）。** 官网 https://mercaturacore.com/ HTTP 200 与官推互证（资料栏 https://t.co/UMixVnhdu2 解析为 https://mercaturacore.com/；站点硬编码 https://x.com/MercaturaCore，另有 GitHub https://github.com/Mercatura-Core 与 https://explorer.mercaturacore.com）。账号 2026-10-03 16:54 CST 创建，未认证，38 粉、142 帖。官帖（https://x.com/MercaturaCore/status/2123260995414245668，2026-11-19 11:44 CST，本轮窗口内）确认主网 December 1, 2026 05:00 UTC（2026-12-01 13:00 CST，距约 12 天 / 288.8h，le2h=false）。定位 CPU 向 PoW 币（MCA），MercaHash 挖矿、原生 ML-DSA-65 后量子签名；官网提供 testnet 客户端 v0.1.4-testnet。不是免费 mint，主网代币 CA 未公布。由本窗 KW_GO 官帖发现。DeepSeek admit=true，overall 71，栏目 挖矿。非仓鼠/toychain，focus=false。已进 userFollowWatch + miningWatch。本号不自动 mint。
- **skip HICON / @hicon_app**：bio 写 Coming to Elysium，站点 https://hicon.app 是 Coming soon 的 agent 产品页，未回链官推、未写 Elysium 部署；本窗帖只是向 @UniswapBuilders @Enter_Elysium 提问路由。按 Elysium 规则 Exploring 不计，DeepSeek skip。
- **skip 其它新作者**：PlunderPort / erupt-fun / RuninAI / floats37 / sticksdotfun / PandalZero / zropunks 等已在库或前轮 defer/skip，不重收。Type_SOL 为 TypeScript Solana 工具链，非 mint。
- **gmgm.fun / @gmgmdotfun**：同一已提醒 LIVE 发射台。$GMGM DexScreener 本轮观察时价约 $0.00002104，FDV/市值约 $19,520（上轮约 $31,482），流动性约 $9,189 / 53.69 SOL（上轮约 $11,979），近 1 小时成交约 $24,427。扭蛋程序 CA 仍未核验。不是免费 mint，不重推。
- **skip / 不重推 All in crypto / @allincrypto_ai**：同一已提醒开池窗口。链上 totalMinted 12286（上轮 11913，+373），opened=1，paused=0；本轮 nextPrice()/currentPrice() eth_call 仍回退，下档价按价格曲线本地估算约 0.0026 BNB；Pancake V2 官方对约 65.91 BNB（上轮约 63.13）；LB totalShares=12121、holderCount=1296（上轮 11913 / 1238；updatedAt 2026-11-19 11:50:42 CST；链上 minted 12286，与 LB 不完全一致）。不重推。
- **Arklis / @arklisdotapp**：同一已提醒 FCFS 领取窗口，API 仍 spotsTaken=11/150（与上轮相同），minXp=2000，不是无门槛公开免费 mint，不重推。
- **Unicorn Grand Prix / @UnicornGPrix**：白名单接口仍 open=true、phase=FCFS，count 521/15000（与上轮相同，剩 14779），不视为新翻转，免费 mint 日期仍 TBA，不重推。
- **Dead Zone / @DeadZonecrypto**：同一已提醒付费 mint LIVE，API 仍 open=true，minted=130/4500（与上轮相同），VIP pack sold 仍 3，OG pack sold 仍 1，0.01 SOL/份，不视为新翻转，不重推。
- **VICE6 / @Vice6fun**：仍 PRE-LAUNCH，距 2026-11-20 08:00 CST 约 19.8 小时，le2h=false，CA 未公布，MUST 0 帖，不重推。
- **the one（@yuange99988852）**：仍 announced。距 2026-11-19 19:00 CST 约 6.8 小时，le2h=false，尚未 LIVE，MUST 0 帖，不重推。
- **SpiritsRH**：免费 mint 窗口 2026-11-20 00:00 CST，距约 11.8 小时，le2h=false，MUST 0 帖，不重推。
- **Oathbots**：代币窗口 2026-11-19 22:00 CST，距约 9.8 小时，le2h=false，MUST 0 帖，不重推。
- **Boxcars / @BoxcarsHQ**：同一已提醒预售窗口，截止 2026-11-20 21:00 CST（约 32.8 小时，le2h=false）。本窗 FAT_PAD 未见新官帖，不重推。
- **INMATES / @INMATES_RH**：同一已提醒窗口。GTD 申请窗仍 2026-11-19 09:00–19:00 CST，约 6.8 小时后关，le2h=false；表单仍只写本机 localStorage，页面仍写明不向团队提交，暂无 CA。MUST 0 帖。不重推。
- **AUGENT / @AugentFun**：同一已提醒免费 LIVE，链上 freeClaimed 465/2999（上轮 445，+20），paid sold 仍 1，paused=0，phase=1，pair 仍为 0，截止/开池仍 2026-11-21 20:52 CST（约 56.6 小时，le2h=false）。只更新进度，不重推。
- **Agent Miner / @AIMMinerBSC**：同一已提醒免费 LIVE，链上 totalMinted 716（与上轮相同），不重推。
- **AONE / @aone_agent**：同一已提醒开池/抽干窗口。链上 freeMinted 仍 10000/10000、hero 仍 22864；Pancake V2 对约 0.0097 BNB（与上轮相同），不重推。
- **Bsc Cat / @Bobkjyj**：同一已提醒免费 LIVE，freeMinted 550/800（与上轮相同），paid=0，pair 仍为 0，不重推。
- **Fistagent / @Fistagent_（bonkagent）**：同一已提醒 mint LIVE，链上 totalMinted 仍为 4，本窗 FAT_PAD 0 帖，不重推。

## 覆盖与节流

- 判断/文案/打分一律 DeepSeek（deepseek-flash，思考开启）。DS 对 AcruxHub admit=true、overall 64、栏目 台子/Meme、status=testnet；对 Mercatura admit=true、overall 71、栏目 挖矿、status=announced；对 HICON skip。无 DS fallback。
- 本号不自动 mint。
- 下一轮 mentions：Tape / GIWA / BTC / Starknet+DogeEVM；silent=GIWA；UF next=685 pumpgld；agentPad next=33 Leeonmort。
