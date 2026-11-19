# RESULT R1965

- time: 2026-11-19 12:43:17 CST
- mode: ample（R1956 为 08:00 CST 后首轮全量补扫；本轮为其后第九轮正常节流，lastFullAfterReset 仍为 R1956）
- xReads: 20（main 19 + silent 1 + EXTRA 0）
- remainingBefore: 804 → remaining: 784
- softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50
- tenLanes: yes（11 条关键词全跑，近 30 分钟，start_time 2026-11-19T03:55:00Z：LZ 1 / TAPE 25 / GIWA 9 / DOGE 13 / BTC 4 / SN 3 / MINT 25 / MINE 0 / PAD 20 / GO 25 / ELY 25。TAPE、MINT、GO、ELY 触顶，未翻页。无 EXTRA。）
- userFollow: 刷完本分片，wrap=false。start 685 pumpgld，kept 50（pumpgld→iglusol），walkScanned 62，NF_skip 12（lootbale / useapppayfun / CyclopesElysium / elyword_xyz / AgentFramlin404 / RedirectCash / kyte_market / vytraqfun / hyperlinkdotfun / HordeOnElysium / lazabitmeme / XiangHao91647），skip_already 0。next 747 AIZOBsc。prio_folded 全部 7 个：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer / mobster_meme。窗口号 INMATES_RH / yuange99988852 / Oathbots / spiritsHOOD / Vice6fun 另 1 次 from:。本分片 UF 帖 UF1=0 / UF2=0，MUST=3，FAT_PAD=0。
- mentions: 本轮轮换子集 4 组 Tape 5（@TapeAIAgent @Blonskr @TapeOutWorld @BEMGoGoGo @tapeupio，12 帖）/ GIWA 5（@GIWA_by_Upbit @YeonPad @gamapadcom @GiwaPumpPad @GIWALAUNCHPAD，8 帖）/ BTC 5（@ShieldedNaka @banknotes_btc @Unpairxyz @alkanesagentic @acmeonbtc，2 帖）/ Starknet+DogeEVM 5（@Starknet @Bramble_fi @DogeOS @LaikaSuperApp @wowpadlol，5 帖）。下一轮子集 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent: GIWA（1965%11=7；SILENT_MEN result_count=24，约 24h 窗；search_users 仍不可用）。未见需新收录的官方项目（ARIWA 已在库）。下一轮 silent=DogeEVM。
- watchLeaksFixed: []（新卡 ducks 已进 userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch）
- fat cursors：agentPad 33→58（本轮 1 次 from: 分片，kept 25 Leeonmort→koaidotfun，跳过 0，帖 0，wrap=false，next LuckyCatsBNB）；freeMint 66 / bnAgent 169 / elysium 283 未动
- discordPeekDeferred: true（DC 未登录）
- thinOfficialDeferred: true（本轮 ample 不打 THIN1–5 薄栏官号 from:）
- newThisRound: ["ducks"]
- statusFlipThisRound: ["x-launch"]（announced→live；R1925 已提醒今日主网，不重推）
- le2hThisRound: []
- notify: true（真新收录 DUCKS 且为免费 LIVE，即便 overall 60<70 也必须提醒。无≤2h）
- xReadsExtra: 0。主扫 19 + silent 1 达到 minSpend 20、低于 softCap 28。开跑前 remaining 804，读后 784。@Duckslife9 用户字段已在 KW_MINT includes 中，未另查。
- docsSynced: true

## 本轮判定

- **真新收录 DUCKS（@Duckslife9，ducks，overall 60，status=live，focus=false）。** 官网 https://ducks-mint.surge.sh/ HTTP 200 与官推互证（资料栏 https://t.co/cLLGE0UMOq 解析为 https://ducks-mint.surge.sh/；页内硬编码 https://x.com/Duckslife9）。账号 2026-11-19 12:23:10 CST 创建，未认证，0 粉、1 帖。官帖（https://x.com/Duckslife9/status/2123271934695878763，2026-11-19 12:27:32 CST，本轮 30 分钟窗口内）称 DUCKS is LIVE on BNB Chain! 3,000 ducks. Solve the riddle to mint. Free mint for AI agents；Each duck claims 120,000 $DUCK；64,000 DUCK/slot, 0.0009 BNB；100% of sale BNB → pool。链上核验 NFT 0x2cEeDADAE7504f1B0561e1BFc808Ee1E349AFc7f（name/symbol=DUCKS，MAX_SUPPLY=3000，totalMinted=81，freeMinted=81，freeRemaining=419，paidMinted=0，mintClosed=false）；TOKEN 0x510E127990F837C452F5BaFb86f3Bb3d5111d07f（$DUCK 18 位，totalSupply=1,000,000,000）；MINTER 0x1b334B26A534B522Fb5bD541b695cDaA1BdF6FDC（startTime=2026-11-19 11:00 CST，endTime=2026-11-23 11:00 CST，sale remaining=5000、sold=0）。免费档：前 500、每钱包 1 份、需持有 Agent ID、0 BNB；付费档 0.0015 BNB、每钱包最多 2 只。站点文案关闭 2026-11-20 11:00 CST（约 22.3h），与链上 endTime（约 94.3h）不一致，均非≤2h。不是无门槛公开免费 mint（必须解谜，免费档还需 Agent ID）。由本窗 KW_MINT 官帖发现。DeepSeek admit=true，overall 60，栏目 打新。非仓鼠/toychain，focus=false。已进 userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch。账号极新、surge.sh 静态页、合约未审计，风险高。本号不自动 mint。
- **翻转但不重推 X-Launch / @EnterXLaunch**：官帖 https://x.com/EnterXLaunch/status/2123271580805673141（2026-11-19 12:26:07 CST）与母公司 https://x.com/LiquidLogicX/status/2123271190341185802（12:24:34 CST）均称 X-Launch is live on Elysium mainnet。官网 config.mainnet.json launchpad 已改为 0xFd987ba8a7BCfB0beA0D41307A0A98b5c967a188（原 0xC26b7E24F38b1B8EC352a137F33aec6e4350dFCC），且主网配置不再带 preview 字段。status announced→live。R1925 已提醒今日主网窗口，本轮只更新状态与合约，不重推。创建费仍 0.05 HYPE。不是免费 mint。
- **不重推 Roobak / @roobak_xyz**：官帖 https://x.com/roobak_xyz/status/2123265175587602842（2026-11-19 12:00:40 CST）称 launchpad testnet is now live。已收录项目的测试网进度，status 改为 testnet，不重推。
- **skip Bound_Exchange / @Bound_Exchange**：官帖 Coming soon to HyperEVM and Elysium，按 Elysium 规则 Exploring 不计。
- **defer Zero_Pengus**：本窗几乎只有转推 INMATES，无独立官宣，未另开 X 查询。
- **skip / 不重收 ARIWA_on_Giwa**：已在库，第三方 mint 帖不重收。
- **gmgm.fun / @gmgmdotfun**：同一已提醒 LIVE 发射台。$GMGM DexScreener 本轮观察时价约 $0.00002369，FDV/市值约 $21,948（上轮约 $19,520），流动性约 $9,836 / 57.06 SOL（上轮约 $9,189），近 1 小时成交约 $13,445。扭蛋程序 CA 仍未核验。不是免费 mint，不重推。
- **skip / 不重推 All in crypto / @allincrypto_ai**：同一已提醒开池窗口。链上 totalMinted 12632（上轮 12286，+346），opened=1，paused=0；本轮 nextPrice()/currentPrice() eth_call 仍回退，下档价按价格曲线本地估算约 0.0026 BNB；Pancake V2 官方对约 62.16 BNB（上轮约 65.91）；LB totalShares=12624、holderCount=1323（上轮 12121 / 1296；updatedAt 2026-11-19 12:24:53 CST；链上 minted 12632，与 LB 不完全一致）。不重推。
- **Arklis / @arklisdotapp**：同一已提醒 FCFS 领取窗口，API 仍 spotsTaken=11/150（与上轮相同），minXp=2000，不是无门槛公开免费 mint，不重推。
- **Unicorn Grand Prix / @UnicornGPrix**：白名单接口仍 open=true、phase=FCFS，count 522/15000（上轮 521，+1，剩 14778，used 222），不视为新翻转，免费 mint 日期仍 TBA，不重推。
- **Dead Zone / @DeadZonecrypto**：同一已提醒付费 mint LIVE，API 仍 open=true，minted=133/4500（上轮 130，+3），left 4367，VIP pack sold 仍 3，OG pack sold 仍 1，不视为新翻转，不重推。
- **VICE6 / @Vice6fun**：MUST 官帖 https://x.com/Vice6fun/status/2123266012028243982 称 $VICE6 将在 pumpfun 上线 Soon，持仓门槛 100k；大门仍 2026-11-20 00:00 UTC = 2026-11-20 08:00 CST（约 19.3 小时），CA 仍未公布，le2h=false，不重推。
- **the one（@yuange99988852）**：仍 announced。距 2026-11-19 19:00 CST 约 6.3 小时，le2h=false，尚未 LIVE，MUST 本窗无新开闸帖，不重推。
- **SpiritsRH**：免费 mint 窗口 2026-11-20 00:00 CST，距约 11.3 小时，le2h=false，MUST 0 帖，不重推。
- **Oathbots**：MUST 见 Bot Crush 游戏更新，不是新的 mint 窗口；代币窗口仍 2026-11-19 22:00 CST，距约 9.3 小时，le2h=false，不重推。
- **Boxcars / @BoxcarsHQ**：同一已提醒预售窗口，截止 2026-11-20 21:00 CST（约 32.3 小时，le2h=false）。不重推。
- **INMATES / @INMATES_RH**：同一已提醒窗口更新。MUST 官帖 https://x.com/INMATES_RH/status/2123271335522546083（约 12:25 CST）称 Free mint tomorrow. 999 inmates … 4PM UTC. First 400 wallet，解读为 2026-11-20 16:00 UTC = 2026-11-21 00:00 CST（约 35.3h，非≤2h）。GTD 申请窗仍 2026-11-19 09:00–19:00 CST，约 6.3 小时后关，le2h=false；表单仍只写本机 localStorage，暂无 CA。不重推。
- **AUGENT / @AugentFun**：同一已提醒免费 LIVE，链上 freeClaimed 558/2999（上轮 465，+93），paid sold 仍 1，paused=0，phase=1，pair 仍为 0，截止/开池仍 2026-11-21 20:52 CST（约 56.2 小时，le2h=false）。只更新进度，不重推。
- **Agent Miner / @AIMMinerBSC**：同一已提醒免费 LIVE，链上 totalMinted 717（上轮 716，+1），不重推。
- **AONE / @aone_agent**：同一已提醒开池/抽干窗口。链上 freeMinted 仍 10000/10000、hero 仍 22864；Pancake V2 对约 0.0097 BNB（与上轮相同），不重推。
- **Bsc Cat / @Bobkjyj**：同一已提醒免费 LIVE，freeMinted 550/800（与上轮相同），paid=0，pair 仍为 0，不重推。
- **Fistagent / @Fistagent_（bonkagent）**：同一已提醒 mint LIVE，链上 totalMinted 仍为 4，本窗 FAT_PAD 0 帖，不重推。

## 覆盖与节流

- 判断/文案/打分一律 DeepSeek（deepseek-flash，思考开启）。DS 对 DUCKS admit=true、overall 60、栏目 打新、status=live。无 DS fallback。
- 本号不自动 mint。
- 下一轮 mentions：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；silent=DogeEVM；UF next=747 AIZOBsc；agentPad next=58 LuckyCatsBNB。
