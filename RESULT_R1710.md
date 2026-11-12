# RESULT R1710

- round: 1710
- completedAt: 2026-11-12 18:39:37 CST
- docsSynced: true
- notify: true
- notifyReason: 新收录 hoodrockers，public free mint 约 18:35 CST 已开铸，处于 ≤2h 窗内（约至 20:35 CST）；clover-rh 亦仍 le2h=true（20:00 CST 揭示）。
- newThisRound: ['hoodrockers']
- candidates: 4061
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- panel: https://reboot7454.github.io/early-scout/
- pushSha: PENDING
- pushPending: true

## xQuota
- xReads: 18
- remainingBefore: 416
- remaining: 397
- mode: pace
- softCap: 18
- minSpend: 18
- silentCap: 2
- ufCursor: 1150→1198 (kept 48, skip 0, considered 48)
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 打新
- kwCoreDeferred: GO盘, Elysium, 挖矿, 台子/Meme
- mentionsThin: []（因 pace softCap=18 裁掉；原计划保持 @ZeroVaultxyz/@TapeOutWorld, @YeonPad/@LaikaSuperApp, @banknotes_btc/@Starknet）
- mentionsRest: []（因 softCap 裁掉；原计划偶数轮 @flapdotsh/@irys_xyz）
- fatShards: agentPad 61→86 kept=23 drop=2, freeMint 193→218 kept=17 drop=8, bnAgent 170→195 kept=14 drop=11, elysium 114→139 kept=25 drop=0
- lastFullAfterReset: 仍为 R1692（本轮不是重置后全量补扫）

## silentAccounts
- ran: true
- seen: 44
- sentToReview: 0
- admitted: 0
- skipped: 44
- lane: Elysium
- index: 5
- userQuery: Elysium mint
- search_users_unavailable: true
- deferredHandles: []
- skipReasons: {"too_many_posts": 32, "already_in_library": 12}

## 本轮结论
R1710 非全量补扫（lastFullAfterReset 仍 R1692）：送审 4 个新号，收录 hoodrockers（Robinhood Chain 6,666 免费公开铸造，约 18:35 CST 开铸，live+le2h，无 CA 不编造，focus=false）；跳过 3 个（DogeOS 中文转述无确定日期、Superstake 邀请码晒单、QUID 骂帖）。库内：giwahook 原 ~18:35 CST 窗已过，关闭 le2h，状态仍 live，粉保持 37，CA 不变；bloodstockrh 18:30 CST 官帖给出团队钱包 0xA3453ac3AD2e5170d84d0840a87F33c9af97Dbc3，22:00 CST 开放、前 10 分钟仅该钱包可领一个空节点（Nvidia），22:10 CST 起全员开放，$SIRE 仍 23:00 CST，未进 ≤2h，粉保持 13，不把团队钱包写成代币 CA；clover-rh 保持 le2h=true，仅刷 lastChecked（揭示仍 20:00 CST，代币+平台仍 11-13 02:00 CST）；zerva/elysiumpunks/mythosbsc/dispersa-labs 仅刷 lastChecked 与短 whatsNew，粉丝不下调；粉丝上调 anipals 54→109、qubits-sh 3→502、wag-agent 1→158、bem-domains 118→133、digigolds 268→271、giwaup 3894→3896、hexis 277→317、globemkts 747→750、nest-exchange 8260→8263、rgbhorse 33509→33516，mendlingsnft 补 0→1856；hamster-hour/squeekchain/ascendlaunch/lot-bsc/elarune/wayangx 无新帖仅刷 lastChecked。Enter_Elysium 本轮查询被 GIWAHOOK 刷满，不更新 lastChecked。notify=true。

## dsNote
deepseek-flash thinking-on：一次调用（max_tokens=8000，系统要求只输出完整 JSON）即得出完整对象，但 admits[0] 末尾多了一个闭合花括号（「非官方钟点"}}]」），本地去掉多余 } 后 json.loads 成功，未再调 DS、未走 dsFallback。admits=[hoodrockers]，skips=3，notify=true。

## alertMessage
🔔 R1710：新卡 Hood Rockers（@hoodrockers，Robinhood Chain，6,666，免费公开铸造）约 18:35 CST 已开铸，进入 ≤2h 窗（约至 20:35 CST），帖中无 CA 未编造；clover-rh 仍待 20:00 CST 揭示。giwahook ≤2h 窗已关（仍 LIVE）。bloodstockrh 团队钱包已公布，22:00 CST 独占 / 22:10 CST 公开（尚未进窗）。面板：https://reboot7454.github.io/early-scout/
