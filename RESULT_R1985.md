# RESULT R1985

- time: 2026-11-19 22:47:01 CST
- notify: true（真新收录 AnthPad（@UseAnthPad）；BEETLE / beetleai 销售开闸 + CA 核验翻转。不重推 SpiritsRH 同窗、Oathbots 已报开盘、VICE6 仍 PRE-LAUNCH 无 CA）
- panel: https://reboot7454.github.io/early-scout/
- commit: bacd1b713a364233ce18c10f1d973429c532032f
- docs: 本轮已运行 scripts/sync_docs_panel.sh 并推送 docs/data.json。oathbots、spiritsrh、beetleai 已在 meta.forcePanelIds。
- dsFallback: false（DeepSeek flash、thinking on，一次调用吐出可解析 JSON，用于 AnthPad 收录/打分与 alert 文案；链上与站点数字均按本轮探针，未采用模型臆造数值）

## 覆盖

- xReads 20（main 19 + silent 1 + EXTRA 0），remainingBefore 396→remaining 376，mode pace 但因额度充足未砍栏，softCap 22 / minSpend 18。20 次并行 search_posts_all 的 footer 最高 395、最低 376，故 remainingBefore 按 footer+1 记 396。
- UF 分片 start 1746 ShinobRH，kept 50（→coinfinfun），wrap=false，UF1=3 / UF2=0 / MUST=3 / FAT_PAD=0，PRIO 7 号已折进 UF1 未另读，next 1796 0padfun。
- 十栏关键词全跑（各栏均查询 1 次；KW_LZ=0 / KW_TAPE=10 / KW_GIWA=22 / KW_DOGE=4 / KW_BTC=11 / KW_SN=4 / KW_MINT=25 / KW_MINE=5 / KW_PAD=25 / KW_GO=25 / KW_ELY=25。MINT/PAD/GO/ELY 达 25 上限未翻页。未因截断补读）。
- mentions Tape 0 / GIWA 7 / BTC 2 / Starknet+DogeEVM 0；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent=Elysium（25 帖，达上限未翻页，无独立新录取；AnthPad 来自 KW_GO），下一轮 Tape/电路。
- agentPad 从 640 Kismonft 起 kept 25（Kismonft→HashDogeIO），walk 31，NF_skip 6（topaaafun、ripstackfun、UseZPadX、agenticsocial、dyorcash、404Naroba），next 671 themunos_。
- EXTRA：0。候选核验使用本轮 search_posts_all includes，未另开 get_users 重读。
- search_users 仍不可用，silent 仅 SILENT_MEN（约 24h 窗）。
- thinOfficialDeferred=true（pace，无 THIN official from:）。discordPeekDeferred=true（DC 未登录）。
- lastFullAfterReset 仍为 R1956。

## 新收录 / 翻转

- 真新收录 1 个：AnthPad（@UseAnthPad，id=anthpad）。账号 2026-11-19 19:52:42 CST 新建（X id 2123383637571756032），约 2.9h，1 粉 / 3 帖，未认证。官帖 22:23 CST（https://x.com/UseAnthPad/status/2123421894967746886）称 AnthPAD is live：发射代币、配 Claude agent、手续费池用于 Anthropic IPO 买股。资料栏 t.co 解析到 https://anthpad.xyz/（HTTP 200），站点自称 Solana launchpad，有 Connect wallet 与 /launch；「Starting 0%」为进场动画而非铸造进度。站点 X 按钮仅为 https://x.com，未回链 @UseAnthPad，siteXMutual=incomplete。未见 CA。非免费 mint，无独立限时打新窗。watching，focus=false，栏=台子/Meme，DeepSeek overall 76（early 92 / actionable 78 / novelty 72 / risk 68）。已补挂 userFollowWatch + xChainPadWatch。与库内 AnthroBit 不是同一项目。本号不自动 mint。
- 开闸/CA 翻转（推送）：BEETLE（@CherylB83488，id=beetleai）。此前 announced、caUnverified=true，beetleai.fun 仍 Cloudflare 403。本轮官帖 21:14 CST（https://x.com/CherylB83488/status/2123404437192630673）称正式开启 Mint，短链指向 https://beetleai.pages.dev（HTTP 200）。销售合约与代币 CA 均为 `0xAe695409da1601232Fd00c43413d73Fc3c68F59c`，部署交易 `0x3256c20a9f91f85e560f5b8541220f736a2071abae5ff74b6a93a8f7ec174021`（2026-11-18 21:45:47 CST，receipt 合约地址一致）。链上 startsAt 2026-11-19 21:00:00 CST 已过，endsAt 2026-11-21 21:00:00 CST（约 46.22h），price=0.003 BNB，maxShares=8000，已售 totalShares=69 / buyerCount=13，phase=0，launched=false，pair=0，合约余额 0.15525 BNB = 69×0.003×75%。静态 config.js 仍写 saleStatus=upcoming，以链上为准。status 改为 live，caUnverified=false。付费，本号不自动 mint。
- 不重推：Oathbots 已于 R1984 确认 22:00:02 CST 开盘；本轮 MUST 官帖 22:06 CST 仅复述已知 CA `0x1e311022fEe30A395291eA21e5f339D3016a0Ed4`，只刷新价/LP。SpiritsRH 免费 mint 仍 2026-11-20 00:00 CST（约 1.22h，仍 ≤2h），官网仍 WHITELIST OPEN，CA 未公布，R1984 已推过该窗。VICE6 官网仍 PRE-LAUNCH、写 “$VICE6 isn't live yet”，未见 CA，空投门仍 2026-11-20 08:00 CST（约 9.22h）；本窗仍是 R1984 已引用的 21:40 CST 官帖，不以该帖当作已开盘。
- 驳回 / 不建卡：@Fleafamily（13.76 天、82 粉，fleafamily.com 为已上线 workspace「换新域名」更新，无定时铸造窗）；@MiningIsLife_（GoMining 使用笔记，非项目）；@ElysorOnElysium（回复让 clanker 发射代币，无站点/部署）；ARIWA 铸币转发不重收（@ARIWA_on_Giwa 自 R1947 已 LIVE）；@joinseedborn 自 R893 已 LIVE。R1984 已驳回的 @PariProtocol、@HyperLogicFun、@Elymunati、@BulladinEVM 本轮无新硬证据，维持驳回。
- 已在库不重推：the one 仍为已提醒的免费 LIVE（81/100），只更新进度。ElysAgent Pass 徽章 32（+1），仍免费 LIVE，不单凭进度重推。ANVIL / Ember 本窗有官帖，均已是库内 LIVE，不重收。

## 已收录进度（不重推）

- the one / THEONE：链上 totalMintedShares=81/100（上轮 79，+2），pair=0，仍处免费段，池未开。站点 HTTP 200，以链上 minter 为准。
- AUGENT：链上 freeClaimed 1463/2999（上轮 1450，+13），sold() 仍 74，池未开，截止约 46.10h（2026-11-21 20:52:53 CST）；以链上为准。
- AIC：minted 13407（+1），LP 约 54.10 BNB（上轮约 58.88，下降），LB holderCount=1478（上轮 1476，+2），lbTotalShares=13407（上轮 13406；本轮与链上 minted 一致）。
- AIM：totalMinted=723（上轮 723，持平）。
- AONE：hero 仍 22864、LP 约 0.0097 BNB，freeMinted 仍 10000。
- Bsc Cat：561/800（上轮 560，+1），paid=0，池未开。
- Dead Zone：本轮 api.deadzoneplay.com/api/state 200，minted 仍 133/4500，OG pack sold=1，VIP sold=3，FO sold=0，open=true。
- UGP：WL 仍 open=true、phase=FCFS，534/15000（上轮 534，持平；剩 14766，used 234）。
- Arklis：FCFS 仍 12/150，minXp=2000。
- DUCKS：minted 135/3000（上轮 135，持平），freeRemaining 沿用 374（本轮 minter.freeRemaining 调用仍 reverted）。站点关 2026-11-20 11:00 CST（约 12.22h），链上 endTime 2026-11-23 11:00 CST，非≤2h。
- Fistagent：主 CA `0xdDD8af1D1C9513D6eB5F4C017516360B26955c26` totalMinted 仍 1246，pair()=`0xf375def1f8f60bf52a2a8d4309498b1fce45c01b`（USDT 对，getReserves 0/0，流动性未注入）。付费已 LIVE、此前已提醒，只更新进度，不重推。
- gmgm $GMGM：本轮观察市值约 $14989（上轮约 $16302），流动性约 $7940.39 / 44.14 SOL（上轮约 $8344.29 / 46.35 SOL），价格约 $0.00001620，1h 成交约 $1515.67。扭蛋程序 CA 仍未核验。
- Boxcars：执照 NFT 链上 totalSupply 仍 380/1000，预售截止仍 2026-11-20 21:00 CST（约 22.22h，le2h=false）。raised() 与合约余额均为 0.01 BNB。
- ElysAgent Pass：徽章合约 totalSupply 32（上轮 31，+1），仍免费 LIVE，不重收、不单凭进度重推。
- PandalZero：Apps Script ?action=status 仍返回 {"cap":111,"remaining":0}（与近几轮相同），站点 /api/status 本轮仍 404。不能证实 First 111 满员翻转，mint 未 LIVE，不重推。
- Dividends：链上仍 1000/1000，publicPrice 仍 0.0017 ETH；MUST 本窗 0 新官帖，二级成交仍未独立核验，不重推。
- 窗口：BEETLE 销售已开（本轮推送），截止约 46.22h（2026-11-21 21:00 CST）；Oathbots 已于 22:00:02 CST 开盘（R1984 已推，本轮只刷新价/LP：pair 快照约 $0.00009233，流动性约 $8927.48 / 7.5332 BNB，FDV 约 $92332，预售仍 finalized 1.8321 BNB / 49 钱包）；SpiritsRH 免费 mint 约 1.22h（2026-11-20 00:00 CST，仍 ≤2h，不重推）；VICE6 / volta airdrop 约 9.22h（2026-11-20 08:00 CST，开盘未证实）；DUCKS 站点关约 12.22h（2026-11-20 11:00 CST）；Boxcars 预售约 22.22h（2026-11-20 21:00 CST）；INMATES 公开免费 mint 约 25.22h（2026-11-21 00:00 CST）；AUGENT 截止约 46.10h。

## 下轮提示

- UF next 1796 0padfun；agentPad next 671 themunos_。
- mentions 下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent 下一轮：Tape/电路。
- lastFullAfterReset 仍为 R1956。X remaining 376，额度仍充足，下轮继续十栏全跑。
- SpiritsRH 00:00 CST 免费 mint 若出现 CA/实际开铸翻转再核验补推，不要只因仍在 ≤2h 窗内每轮重复刷。
- VICE6 空投门 2026-11-20 08:00 CST；若官网/CA/盘口出现可核验开盘再推，勿把「launches in about an hour」当成已开盘。
- BEETLE 为付费销售（已开、已售 69/8000），只报不自动打；售罄开池或退款期若出现可核验翻转再报。
- Dividends 二级成交/退款若出现可核验的开盘交易再决定是否补推，不要空刷。
- 本轮已同步并推送 docs/data.json，下轮勿再漏同步。
- 本号不自动 mint。
