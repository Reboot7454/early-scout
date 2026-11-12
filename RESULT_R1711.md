# RESULT R1711

- round: 1711
- completedAt: 2026-11-12 19:15:21 CST
- docsSynced: true
- notify: true
- notifyReason: 无新收录，但库内仍有 ≤2h：clover-rh 待 20:00 揭示、zerva 已进 ≤2h（21:00 Pons 上线）；另有 hoodrockers 售罄与揭示完成需同步
- newThisRound: []
- candidates: 4061
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- panel: https://reboot7454.github.io/early-scout/
- pushSha: 1f1ade5
- pushPending: false

## xQuota
- xReads: 18
- remainingBefore: 397
- remaining: 378
- mode: pace
- softCap: 18
- minSpend: 18
- silentCap: 2
- ufCursor: 1198→1246 (kept 48, skip 0, considered 48)
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 挖矿
- kwCoreDeferred: 打新, Elysium, 台子/Meme, GO盘
- mentionsThin: []（因 pace softCap=18 裁掉；原计划保持 @ZeroVaultxyz/@TapeOutWorld, @YeonPad/@LaikaSuperApp, @banknotes_btc/@Starknet）
- mentionsRest: []（因 softCap 裁掉；原计划奇数轮 @fulldotfun/@PulseLaunchpad）
- fatShards: agentPad 86→111 kept=23 drop=2, freeMint 218→243 kept=23 drop=2, bnAgent 195→220 kept=19 drop=6, elysium 139→164 kept=25 drop=0
- lastFullAfterReset: 仍为 R1692（本轮不是重置后全量补扫）

## silentAccounts
- ran: true
- seen: 33
- sentToReview: 0
- admitted: 0
- skipped: 33
- lane: Tape/电路
- index: 6
- userQuery: TapeOut
- search_users_unavailable: true
- deferredHandles: ['XLayerOfficial', 'nancy_c813', 'bitcoin2themars', 'UnaBehindMars', 'M5Stack', 'surpr164', 'LoyalSiman', 'Pump_TANG', 'tapeout', 'tapeai']
- skipReasons: {"too_many_posts": 19, "already_in_library": 4, "profile_unresolved": 10}

## 本轮结论
R1711 非全量补扫（lastFullAfterReset 仍 R1692）：送审 1 个新号，跳过 Theinn3rside（研究/社群号，仅第三方提及已在库的 plunderport，无精确时刻/CA，不建卡）。库内：hoodrockers 18:40:08 CST 官帖称约 5 分钟售罄并 fully minted，18:54:50 CST 揭示完成，关闭 le2h，status=sold_out，粉保持 76，未见 CA 不编造；zerva 17:29 官帖确认今日 21:00 CST（13:00 UTC）上 Pons / Robinhood Chain，19:00 已进 ≤2h，仍无 CA，粉保持 52；clover-rh 本轮无新帖，揭示仍 20:00 CST、代币+平台仍 11-13 02:00 CST，保持 le2h=true；elysiumpunks 仍 21:30/快照 21:00，未见 CA，19:30 才进窗，保持 le2h=false，粉保持 5827；bloodstockrh 档期不变（22:00 独占/22:10 公开/$SIRE 23:00），未进窗，粉保持 13，团队钱包不是代币 CA；mythosbsc FCFS 仍约 22:00，未进窗，粉保持 106；giwahook 17:41 后无新帖，le2h=false 仍 live，粉保持 37，CA 不变；pairmine Genesis 34/888 minted，非今晚新开盘，粉保持 978；roboagent 255 deployed / 856 free left，免费窗仍至 11-14 05:51 CST，le2h=false；hamster-hour / squeekchain / ascendlaunch tonight 查询无新帖仅刷 lastChecked；Enter_Elysium 与 GIWAHOOK 同查询但 20 条全是 GIWAHOOK，不改 lastChecked。粉丝上调 globemkts 750→751、kairo-market 1895→1902、agentlifebnb 695→697、sakura-she-nft 63→68、digigolds 271→273、giwaup 3896→3899、wiseguyz 1393→1508、rgbhorse 33516→33519、packswap 62→63、evermor 225→372、onchain-pigarc 846→1345、tetrascore 181→205、pixelmonsv2tr 4→7、hokori-quantum 297→298、datt-radar 2→4、lanternhold 874→4560，bond-agent 补空→2112，nibblers-ely 11→2995。notify=true。

## dsNote
deepseek-flash thinking-on：第一次调用 max_tokens=8000 时 completion 额度被 reasoning（6631 tokens）占满，content 在 digigolds 更新处被截断，JSON 不完整。未改用高成本模型；第二次用同一评审材料、max_tokens=16000 并要求紧凑 JSON，一次即完整可解析。admits=[]，skips=[Theinn3rside]，notify=true。未走 dsFallback。

## alertMessage
🔔 R1711 无新收录。hoodrockers 已于 18:40 售罄（fully minted）、18:54 揭示完成，仍无 CA；clover-rh 仍待 20:00 CST 揭示（代币+平台 11-13 02:00）；zerva 已进 ≤2h，今日 21:00 CST 上线 Pons Launchpad / Robinhood Chain，无 CA。面板：https://reboot7454.github.io/early-scout/
