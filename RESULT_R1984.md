# RESULT R1984

- time: 2026-11-19 22:12:25 CST
- notify: true（Oathbots 链上确认 22:00:02 CST 开盘翻转，R1980 只推过窗口预告；SpiritsRH 免费 mint 首次进入 ≤2h，2026-11-20 00:00 CST，约 1.79h。VICE6 官帖称约 1 小时后 launches，但官网仍 PRE-LAUNCH、未见 CA，不以已开盘重推，仅作同条 nuance。本轮无真新收录）
- panel: https://reboot7454.github.io/early-scout/
- commit: d2dc0cd536e8ff1cc87eb2e6c725aed55fe75d74
- docs: 本轮已运行 scripts/sync_docs_panel.sh 并推送 docs/data.json。oathbots 原 round 798 会被 120 轮窗口丢掉，已写入 meta.forcePanelIds。
- dsFallback: true（DeepSeek 一次 thinking 调用把推理写进可见正文、未吐出可直接使用的 alert；开盘/窗口判定与文案按链上 Mint/DEX、官网与既有 MUST 帖核验事实撰写）

## 覆盖

- xReads 20（main 19 + silent 1 + EXTRA 0），remainingBefore 416→remaining 396，mode pace 但因额度充足未砍栏，softCap 22 / minSpend 18。x_budget 开跑快照曾报 418，20 次并行 search_posts_all 的 footer 最高 415、最低 396，故 remainingBefore 按 footer 记 416。
- UF 分片 start 1696 useFeeTag，kept 50（→elysiumverse），wrap=false，UF1=2 / UF2=0 / MUST=2 / FAT_PAD=0，PRIO 7 号已折进 UF1 未另读，next 1746 ShinobRH。
- 十栏关键词全跑（各栏均查询 1 次；KW_LZ=0 / KW_TAPE=11 / KW_GIWA=12 / KW_DOGE=3 / KW_BTC=25 / KW_SN=5 / KW_MINT=25 / KW_MINE=2 / KW_PAD=25 / KW_GO=25 / KW_ELY=25。BTC/MINT/PAD/GO/ELY 达 25 上限未翻页。未因截断补读）。
- mentions LayerZero 25 / Elysium+kinetiq 23 / mining-squeek+Nutshell 1 / BN Agent pads+STARX 3；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent=LayerZero（25 帖，达上限未翻页，无独立新录取），下一轮 Elysium。
- agentPad 从 613 AMDPAD_64 起 kept 25（AMDPAD_64→geniedotfun），walk 27，NF_skip 2（spiderproject69、kpin_ai），next 640 Kismonft。
- EXTRA：0。候选核验使用本轮 search_posts_all includes，未另开 get_users 重读。
- search_users 仍不可用，silent 仅 SILENT_MEN（约 24h 窗）。
- thinOfficialDeferred=true（pace，无 THIN official from:）。discordPeekDeferred=true（DC 未登录）。
- lastFullAfterReset 仍为 R1956。

## 新收录 / 翻转

- 真新收录 0 个。
- 开盘翻转（推送）：Oathbots（@Oathbots，$OATH）。预售仍 finalized，raised 1.8321 BNB / 49 钱包。代币窗 2026-11-19 22:00 CST。MUST 本窗 0 新官帖，但链上确认 22:00:02 CST 向 Pancake V2 对 `0x1abbE55Cc37a405D89B56f01b1B0A5dC7d951f69` 注入 LP（Mint tx `0xcfb04fa7b6bd70f72250f992a4ca5a8af1a38e31b2cf661f97b7e7e0bc016aa3`），随后已有成交。代币 CA `0x1e311022fEe30A395291eA21e5f339D3016a0Ed4`。Dexscreener 当时价约 $0.00003929，流动性约 $5806 / 4.90 BNB，FDV 约 $39298，1h 成交约 $851（51 买 / 9 卖）。R1980 只推过窗口预告，本轮确认 listing 后推送。已写入 forcePanelIds。本号不自动 mint。
- 窗口首次进入 ≤2h（推送）：SpiritsRH（@spiritsHOOD）。免费 mint 2026-11-20 00:00 CST（11-19 23:00 WIB，约 1.79h），3333 份白名单免费、仅 OpenSea（https://opensea.io/collection/spiritsrh）。官网 https://spiritsrh.surge.sh/ HTTP 200，仍 WHITELIST OPEN，CA 未公布。此前未推过该 ≤2h 窗。
- 未证实开盘、不单列重推：VICE6（@Vice6fun）官帖 21:40 CST（https://x.com/Vice6fun/status/2123411038951415954）称 “$VICE6 launches in about an hour”，并写大门 20 Nov 00:00 UTC（2026-11-20 08:00 CST，约 9.79h）。官网 vice6.fun 仍 PRE-LAUNCH、写 “$VICE6 isn't live yet”，本轮未见 CA。不以该官帖当作已开盘，仅在同一条 alert 中作 nuance。
- 驳回 / 不建卡：@PariProtocol（2026-11-09 建号，约 10 天、22 粉 / 3 帖，自称 Solana PariPad 公平发射、开盘前 30 秒费率 99%→1%，资料栏无官网 URL，本轮未见可核验站点/CA，证据不足，未另开 X 重读）；@HyperLogicFun（约 87k 粉、771 天，已有 Elysium 网关，非极早期新项目）；@Elymunati（2025-10-26 建号、5 粉，自称 Elysium 社区发射台，证据弱）；@BulladinEVM（当日 0 粉游戏向帖，非打新项目）；junzhou1212 等第三方 pokemon mint 回复，无独立官号项目。
- 已在库不重推：@fruitfly_world / TapeFly 称 Genesis Passport 正式开放领取；该卡自 R459 已 LIVE、按 UTC0 日更，不是新限时窗。Dividends 仍 1000/1000，MUST 0 新官帖，二级成交未独立核验，不重推。the one 仍为已提醒的免费 LIVE（79/100），只更新进度，不重推。

## 已收录进度（不重推）

- the one / THEONE：链上 totalMintedShares=79/100（上轮 78，+1），pair=0，仍处免费段，池未开。站点 HTTP 200，页内接线仍可能显示即将上线，以链上 minter 为准。
- AUGENT：链上 freeClaimed 1450/2999（上轮 1439，+11），sold() 仍 74，池未开，截止约 46.67h；以链上为准。
- AIC：minted 13406（+30），LP 约 58.88 BNB（上轮约 50.50，上升），LB holderCount=1476（上轮 1457，+19），lbTotalShares=13406（上轮 13376；本轮与链上 minted 一致）。
- AIM：totalMinted=723（上轮 722，+1）。
- AONE：hero 仍 22864、LP 约 0.0097 BNB，freeMinted 仍 10000。
- Bsc Cat：仍 560/800，paid=0，池未开。
- Dead Zone：本轮 api.deadzoneplay.com/api/state 200，minted 仍 133/4500，OG pack sold=1，VIP sold=3，FO sold=0，open=true。
- UGP：WL 仍 open=true、phase=FCFS，534/15000（上轮 533，+1；剩 14766，used 234）。
- Arklis：FCFS 仍 12/150，minXp=2000。
- DUCKS：minted 135/3000（上轮 130，+5），freeRemaining 沿用 374（本轮 minter.freeRemaining 调用 reverted）。站点关 2026-11-20 11:00 CST（约 12.79h），链上 endTime 2026-11-23 11:00 CST，非≤2h。
- Fistagent：主 CA `0xdDD8af1D1C9513D6eB5F4C017516360B26955c26` totalMinted 仍 1246，pair()=`0xf375def1f8f60bf52a2a8d4309498b1fce45c01b`（USDT 对，getReserves 0/0，流动性未注入）。付费已 LIVE、此前已提醒，只更新进度，不重推。
- gmgm $GMGM：本轮观察市值约 $16302（上轮约 $16045），流动性约 $8344.29 / 46.35 SOL（上轮约 $8243.33），价格约 $0.00001762，1h 成交约 $1332。扭蛋程序 CA 仍未核验。
- Boxcars：执照 NFT 链上 totalSupply 仍 380/1000，预售截止仍 2026-11-20 21:00 CST（约 22.79h，le2h=false）。raised() 与合约余额均为 0.01 BNB。
- ElysAgent Pass：徽章合约 totalSupply 仍 31，仍免费 LIVE，不重收、不单凭进度重推。
- PandalZero：Apps Script ?action=status 仍返回 {"cap":111,"remaining":0}（与近几轮相同），站点 /api/status 本轮仍 404。不能证实 First 111 满员翻转，mint 未 LIVE，不重推。
- Dividends：链上仍 1000/1000，publicPrice 仍 0.0017 ETH；MUST 本窗 0 新官帖，二级成交仍未独立核验，不重推。
- 窗口：Oathbots 已于 22:00:02 CST 开盘（本轮推送）；SpiritsRH 免费 mint 约 1.79h（2026-11-20 00:00 CST，首次 ≤2h，本轮推送）；VICE6 / volta airdrop 约 9.79h（2026-11-20 08:00 CST，开盘未证实）；DUCKS 站点关约 12.79h（2026-11-20 11:00 CST）；Boxcars 预售约 22.79h（2026-11-20 21:00 CST）；INMATES 公开免费 mint 约 25.79h（2026-11-21 00:00 CST）；AUGENT 截止约 46.67h。

## 下轮提示

- UF next 1746 ShinobRH；agentPad next 640 Kismonft。
- mentions 下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 下一轮：Elysium。
- lastFullAfterReset 仍为 R1956。X remaining 396，额度仍充足，下轮继续十栏全跑。
- SpiritsRH 00:00 CST 免费 mint 若出现 CA/实际开铸翻转再核验补推，不要只因仍在 ≤2h 窗内每轮重复刷。
- VICE6 空投门 2026-11-20 08:00 CST；若官网/CA/盘口出现可核验开盘再推，勿把「launches in about an hour」当成已开盘。
- Dividends 二级成交/退款若出现可核验的开盘交易再决定是否补推，不要空刷。
- 本轮已同步并推送 docs/data.json，下轮勿再漏同步。
- 本号不自动 mint。
