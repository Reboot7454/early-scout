# RESULT R1986

- time: 2026-11-19 23:11:07 CST
- notify: false（无真新收录，也无新的免费 LIVE/开闸/CA 翻转。SpiritsRH 免费 mint 仍 2026-11-20 00:00 CST 且仍 ≤2h，但 R1984 已推过该窗、本轮官网仍 WHITELIST、CA 未公布、MUST 无新官帖，不重推。VICE6 仍 PRE-LAUNCH 无 CA；BEETLE 销售数字持平；Oathbots 只刷新价/LP）
- panel: https://reboot7454.github.io/early-scout/
- commit: PENDING
- docs: 本轮已运行 scripts/sync_docs_panel.sh 并推送 docs/data.json。oathbots、spiritsrh、beetleai 已在 meta.forcePanelIds。
- dsFallback: false（本轮无待收录候选送审；未调用 DeepSeek。链上与站点数字均按本轮探针，未采用模型臆造数值）

## 覆盖

- xReads 20（main 19 + silent 1 + EXTRA 0），remainingBefore 376→remaining 356，mode pace 但因额度充足未砍栏，softCap 23 / minSpend 18。20 次并行 search_posts_all 的 footer 最高 375、最低 356，故 remainingBefore 按 footer+1 记 376。
- UF 分片 start 1796 0padfun，kept 50（→Getelysiumpass），wrap=false，UF1=2 / UF2=1 / MUST=0 / FAT_PAD=0，PRIO 7 号已折进 UF1 未另读，next 1846 klayonft。
- 十栏关键词全跑（各栏均查询 1 次；KW_LZ=3 / KW_TAPE=7 / KW_GIWA=8 / KW_DOGE=22 / KW_BTC=6 / KW_SN=9 / KW_MINT=25 / KW_MINE=1 / KW_PAD=24 / KW_GO=24 / KW_ELY=16。KW_MINT 达 25 上限未翻页；KW_PAD=24 / KW_GO=24 未翻页。未因截断补读）。
- mentions LayerZero 25 / Elysium+kinetiq 9 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 2；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent=Tape/电路（1 帖，命中已在库的 @fruitfly_world / tapefly，R1984 已记录 Genesis Passport 开放领取，不重推），下一轮 GIWA。
- agentPad 从 671 themunos_ 起 kept 25（themunos_→BarbarianNFT20），walk 25，NF_skip 无，next 696 HakunaAgentnft。
- EXTRA：0。候选核验使用本轮 search_posts_all includes，未另开 get_users 重读。部分大体量结果经 write_to_file 完整底稿回读，未为此重查 X。
- search_users 仍不可用，silent 仅 SILENT_MEN（约 24h 窗）。
- thinOfficialDeferred=true（pace，无 THIN official from:）。discordPeekDeferred=true（DC 未登录）。
- lastFullAfterReset 仍为 R1956。

## 新收录 / 翻转

- 真新收录 0 个。无免费 LIVE / 免费 mint / 免费登记新开闸，无 CA/销售/开盘翻转。
- 不重推：SpiritsRH 免费 mint 仍 2026-11-20 00:00 CST（约 0.81h，仍 ≤2h），官网 spiritsrh.surge.sh 仍 WHITELIST OPEN、仅 OpenSea、CA 未公布，MUST 本窗 0 新官帖，R1984 已推过该窗。VICE6 官网仍 PRE-LAUNCH、写 “$VICE6 isn't live yet”，未见 CA，空投门仍 2026-11-20 08:00 CST（约 8.81h）；MUST 本窗 0 新官帖，不以旧帖当作已开盘。BEETLE 销售数字与上轮持平（69/8000、13 买家），beetleai.fun 仍 403，MUST 无新官帖。Oathbots 已于 R1984 确认开盘，本轮只刷新价/LP。
- 已在库补字段、不重推：unseen-ordo（@UnseenOrdo）。第三方帖仍在申请同一份约 300 免费额度的进行中 WL（https://unseen.am/whitelist），R1934 已说明「投稿仍开放，不是新的开闸/免费 LIVE」。本轮补官网 https://unseen.am/（官推资料栏 t.co 解析，HTTP 200）、handle、followers 5397 / 154 帖。已在 userFollowWatch + btcPrivacyWatch，不是监控漏挂。
- 库内官号本窗帖、不重推：@kycabal（kycabal，testnet r1828）营销 KYP cabal；@FUSED_OFFICIALS（fused-ai，watching r1833）「launch it yourself on FUSED」，站点历史上仍 COMING SOON；@dataloomsol（watching r1669）Private Data Rooms 产品更新，非铸造窗；@ARIWA_on_Giwa 转发已是 LIVE（r1947）；@fruitfly_world / tapefly（LIVE r459）Genesis Passport 帖落在约 24h silent 窗（21:49 CST），R1984 已记录，不重推。
- 驳回 / 不建卡：@gtamaxxingyt（约 23.3h、4 粉，bio “bringing retail back”；资料栏解析为 YouTube https://www.youtube.com/@gtamaxxingyt，帖链为 X 文章/登录墙，不是加密铸造/发射台）；@SolveOpenMath（数学 agent 谜题/空投，非打新窗）；@TamuAbde（Agent ID hackathon 投票，非新铸造窗）。R1984–R1985 已驳回项本轮无新硬证据，维持驳回。

## 已收录进度（不重推）

- the one / THEONE：链上 totalMintedShares=81/100（上轮 81，持平），pair=0，仍处免费段，池未开。站点 HTTP 200，以链上 minter 为准。
- AUGENT：链上 freeClaimed 1467/2999（上轮 1463，+4），sold() 仍 74，池未开，截止约 45.70h（2026-11-21 20:52:53 CST）；以链上为准。
- AIC：minted 13410（上轮 13407，+3），LP 约 51.90 BNB（上轮约 54.10，下降），LB holderCount=1478（上轮 1478，持平），lbTotalShares=13410（与链上 minted 一致）。
- AIM：totalMinted=723（上轮 723，持平）。
- AONE：hero 仍 22864、LP 约 0.0097 BNB，freeMinted 仍 10000。
- Bsc Cat：仍 561/800，paid=0，池未开。
- Dead Zone：本轮 api.deadzoneplay.com/api/state 200，minted 仍 133/4500，OG pack sold=1，VIP sold=3，FO sold=0，open=true。
- UGP：WL 仍 open=true、phase=FCFS，536/15000（上轮 534，+2；剩 14764，used 236）。
- Arklis：FCFS 仍 12/150，minXp=2000。
- DUCKS：minted 135/3000（上轮 135，持平），freeRemaining 沿用 374（本轮 minter.freeRemaining 调用仍 reverted）。站点关 2026-11-20 11:00 CST（约 11.81h），链上 endTime 2026-11-23 11:00 CST，非≤2h。
- Fistagent：主 CA `0xdDD8af1D1C9513D6eB5F4C017516360B26955c26` totalMinted 仍 1246，pair()=`0xf375def1f8f60bf52a2a8d4309498b1fce45c01b`（USDT 对，getReserves 0/0，流动性未注入）。付费已 LIVE、此前已提醒，只更新进度，不重推。
- gmgm $GMGM：本轮观察市值约 $16731（上轮约 $14989），流动性约 $8455.66 / 47.411 SOL（上轮约 $7940.39 / 44.14 SOL），价格约 $0.00001808，1h 成交约 $2181.8。扭蛋程序 CA 仍未核验。
- Boxcars：执照 NFT 链上 totalSupply 仍 380/1000，预售截止仍 2026-11-20 21:00 CST（约 21.81h，le2h=false）。raised() 与合约余额均为 0.01 BNB。
- ElysAgent Pass：徽章合约 totalSupply 仍 32（上轮 32，持平），仍免费 LIVE，不重收、不单凭进度重推。
- PandalZero：Apps Script ?action=status 仍返回 {"cap":111,"remaining":0}（与近几轮相同），站点 /api/status 本轮仍 404。不能证实 First 111 满员翻转，mint 未 LIVE，不重推。
- Dividends：链上仍 1000/1000，publicPrice 仍 0.0017 ETH；MUST 本窗 0 新官帖，二级成交仍未独立核验，不重推。
- 窗口：BEETLE 销售已开（R1985 已推），已售仍 69/8000、13 买家，0.003 BNB/份，截止约 45.81h（2026-11-21 21:00 CST），池未开，付费本号不自动 mint；Oathbots 已于 22:00:02 CST 开盘（R1984 已推，本轮只刷新价/LP：pair 快照约 $0.0001481，流动性约 $11518.29 / 9.7071 BNB，FDV 约 $148187，预售仍 finalized 1.8321 BNB / 49 钱包）；SpiritsRH 免费 mint 约 0.81h（2026-11-20 00:00 CST，仍 ≤2h，不重推）；VICE6 / volta airdrop 约 8.81h（2026-11-20 08:00 CST，开盘未证实）；DUCKS 站点关约 11.81h（2026-11-20 11:00 CST）；Boxcars 预售约 21.81h（2026-11-20 21:00 CST）；INMATES 公开免费 mint 约 24.81h（2026-11-21 00:00 CST）；AUGENT 截止约 45.70h。

## 下轮提示

- UF next 1846 klayonft；agentPad next 696 HakunaAgentnft。
- mentions 下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 下一轮：GIWA。
- lastFullAfterReset 仍为 R1956。X remaining 356，额度仍充足，下轮继续十栏全跑。
- SpiritsRH 00:00 CST 免费 mint 若出现 CA/实际开铸翻转再核验补推，不要只因仍在 ≤2h 窗内每轮重复刷。
- VICE6 空投门 2026-11-20 08:00 CST；若官网/CA/盘口出现可核验开盘再推，勿把「launches in about an hour」当成已开盘。
- BEETLE 为付费销售（已开、已售 69/8000），只报不自动打；售罄开池或退款期若出现可核验翻转再报。
- Dividends 二级成交/退款若出现可核验的开盘交易再决定是否补推，不要空刷。
- 本轮已同步并推送 docs/data.json，下轮勿再漏同步。
- 本号不自动 mint。
