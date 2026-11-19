# RESULT R1982

- time: 2026-11-19 21:16:17 CST
- notify: true（① Dividends / @Dividendsarts 公开铸造由 LIVE 翻转为售罄：链上 totalMinted()=1000/1000，官帖 20:59 CST officially SOLD OUT、21:00 CST 称二级（OpenSea）开启后 1 小时处理退款，属 R1981 预告的铸满/关口翻转，必须补推；② 真新收录 MemeBSC / @MemeBSC_（watching，overall 50，非免费）。Oathbots 代币窗仍约 0.73h，R1980 已首次推送，本轮仅 Bot Hop 小游戏帖、开盘/可领未确认，不重推）
- panel: https://reboot7454.github.io/early-scout/
- commit: fc9c011517040c903675d10cb63b7a4a2ec0326b
- docs: 本轮已运行 scripts/sync_docs_panel.sh 并推送 docs/data.json（补 R1981 只推了根 data.json、Pages 仍停在 R1980 的遗漏）。sold_out 后的 Dividends 因原 round=1747 会被 120 轮窗口丢掉，已写入 meta.forcePanelIds 以留在面板。

## 覆盖

- xReads 20（main 19 + silent 1 + EXTRA 0），remainingBefore 458→remaining 438，mode pace 但因额度充足未砍栏，softCap 21 / minSpend 18。
- UF 分片 start 1596 getclocked，kept 50（→Envara_Agent），wrap=false，UF1=2 / UF2=0 / MUST=4 / FAT_PAD=0，PRIO 7 号已折进 UF1 未另读，next 1646 PonkeAgent。
- 十栏关键词全跑（各栏均查询 1 次；KW_LZ=6 / KW_TAPE=25 / KW_GIWA=17 / KW_DOGE=18 / KW_BTC=4 / KW_SN=1 / KW_MINT=25 / KW_MINE=4 / KW_PAD=25 / KW_GO=25 / KW_ELY=25。TAPE/MINT/PAD/GO/ELY 达 25 上限未翻页。无 truncated，未因截断补读）。
- mentions LayerZero 25 / Elysium+kinetiq 21 / mining-squeek+Nutshell 3 / BN Agent pads+STARX 25；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent=台子/Meme（25 帖，无独立新录取），下一轮 GO盘。
- agentPad 从 557 Elarune_ 起 kept 25（Elarune_→OREAutos），walk 26，NF_skip 1（Panba_EmojiPack），next 583 cashcat_Agent。
- EXTRA：0。候选核验使用本轮 search_posts_all includes，未另开 get_users 重读。
- KW_MINE / MEN_SQ 对 @squeekchain 有非致命 User is unavailable 展开错误，查询仍返回帖子。
- thinOfficialDeferred=true（pace，无 THIN official from:）。discordPeekDeferred=true（DC 未登录）。
- lastFullAfterReset 仍为 R1956。

## 新收录 / 翻转

- 状态翻转：Dividends（@Dividendsarts，已在库 R1747，R1981 刚由白名单翻转为公开铸造 LIVE，当时链上 924/1000）。MUST 本轮加入该号以核验收口。官帖 20:59:39 CST「We're officially SOLD OUT」（https://x.com/Dividendsarts/status/2123400814454620299），21:00:40 CST「Refunds will be processed 1 hour after secondary opens」（https://x.com/Dividendsarts/status/2123401070089298326），并给出 OpenSea 二级 https://opensea.io/collection/dividendsarts（官帖写 Trading opens in few minutes）。链上 totalMinted()=1000/1000，publicPrice() 仍 0.0017 ETH。官网首页仍残留白名单文案，铸页静态 HTML 有 MINTED. 字样，以官帖+链上为准。二级是否已成交未独立核验（OpenSea 为 SPA，未看到成交数据）。已更新卡片 status=sold_out、le2h=false，并补进 forcePanelIds。非免费。按硬规则本轮补推。
- 真新收录 1 个：
  - MemeBSC（@MemeBSC_，台子/Meme，评分 50，status=watching，focus=false）。官号 2026-11-19 20:47:52 CST 建立，本轮约 0.3h、106 粉 / 5 帖，20:58:54 CST 发帖（https://x.com/MemeBSC_/status/2123400624083738961），来源 keyword:KW_PAD。官网 https://www.memebsc.fun/ HTTP 200，title「MemeBSC · BNB Chain meme launchpad」，自称一笔交易发射 meme，可选 four.meme / flap.sh / genius.fun，launch fee 0.002 BNB，并写 never holds your keys or your BNB。X 资料栏指向该官网，但官网静态页与抽到的 JS bundle 未见回链 @MemeBSC_（仅表单有 X 输入框），siteXMutual=no。未见独立自有 CA，非免费 mint，无独立限时打新窗。已补进 userFollowWatch + xChainPadWatch。
- 驳回：@pveworld_（2026-11-15 建号，0 粉 / 1 帖，官网 pveworld.com 是免费 isometric MMO，无 mint/盘口窗口，bio 中 $PVE CA 未核验，官网未回链官推，早期但不可操作）；@QomX_io（2026-01-08 建号，约 405 粉 / 1273 帖，已运行较久的 BSC 混合交易所/发射台，非极早期）；@tollchk（t0ll.xyz 同站 check desk，Toll / @Tollxyz_ 已在库 toll-xyz，本轮只补官网与别名，不另建卡）；@GTA6ViceCityDai（粉丝资讯号）；以及若干 KOL/纯回复号。@Mopesnft 已在库 watching，本轮仅第三方提及，未新核验 LIVE 翻转，不重推。
- DeepSeek 只收 MemeBSC（watching / 50），分数按 0-100 返回，无需换算。notifySuggestion 亦为 true（Dividends 关口翻转）。
- 窗口已提醒不重推：Oathbots 代币窗 2026-11-19 22:00 CST（约 0.73h）仍在 ≤2h，R1980 已首次推送，本轮官帖是 Bot Hop 小游戏（oathbots.online/hop），不是开盘/可领确认，不重推。the one 仍为已提醒的免费 LIVE（57/100），只更新进度，不重推。

## 已收录进度（不重推）

- the one / THEONE：链上 totalMintedShares=57/100（上轮 54，+3），pair=0，仍处免费段，池未开。站点 HTTP 200，页内接线仍可能显示即将上线，以链上 minter 为准。
- AUGENT：链上 freeClaimed 1426/2999（上轮 1379，+47），sold() 仍 54，池未开，截止约 47.61h；以链上为准。
- AIC：minted 13350（+16），LP 约 55.75 BNB（上轮约 48.04），LB holderCount=1458（上轮 1479，下降），lbTotalShares=13360（上轮 13315；与链上 minted 不完全一致，分别记）。
- AIM：仍 722。
- AONE：hero 仍 22864、LP 约 0.0097 BNB，freeMinted 仍 10000。
- Bsc Cat：560/800（上轮 559，+1），paid=0，池未开。
- Dead Zone：本轮 api.deadzoneplay.com/api/state 200，minted 仍 133/4500，OG pack sold=1，VIP sold=3，FO sold=0，open=true。
- UGP：WL 仍 open=true、phase=FCFS，仍 533/15000（剩 14767，used 233）。api.unicorngrandprix.xyz 本轮 SSL 失败，以 worker.unicorngrandprix.xyz/api/wl/config 为准。
- Arklis：FCFS 仍 12/150，minXp=2000。
- DUCKS：minted 仍 130/3000，freeRemaining 沿用 374（本轮 minter.freeRemaining 未新读）。站点关 2026-11-20 11:00 CST（约 13.73h），链上 endTime 2026-11-23 11:00 CST，非≤2h。
- Fistagent：主 CA `0xdDD8af1D1C9513D6eB5F4C017516360B26955c26` totalMinted 仍 1246，pair()=`0xf375def1f8f60bf52a2a8d4309498b1fce45c01b`（USDT 对，getReserves 0/0，流动性未注入）。付费已 LIVE、此前已提醒，只更新进度，不重推。
- gmgm $GMGM：本轮观察市值约 $15263（与上轮持平），流动性约 $8005.94 / 45.12 SOL（与上轮持平），价格约 $0.00001650，1h 成交约 $16.97。扭蛋程序 CA 仍未核验。
- Boxcars：执照 NFT 链上 totalSupply 仍 380/1000，预售截止仍 2026-11-20 21:00 CST（约 23.73h，le2h=false）。raised() 与合约余额均为 0.01 BNB。
- ElysAgent Pass：徽章合约 totalSupply 仍 31，仍免费 LIVE，不重收、不单凭进度重推。
- Oathbots：预售仍 finalized，raised 1.8321 BNB / 49 钱包；代币窗 2026-11-19 22:00 CST 仍约 0.73h（R1980 已首次 ≤2h 推送），开盘/可领未确认，本轮不重推。
- PandalZero：Apps Script ?action=status 仍返回 {"cap":111,"remaining":0}（与近几轮相同），站点 /api/status 本轮仍 404。不能证实 First 111 满员翻转，mint 未 LIVE，不重推。
- Toll：已在库 @Tollxyz_。本轮核验官网 https://t0ll.xyz/ 回链 @Tollxyz_ 与 @tollchk，补官网与别名，不另建卡。
- 窗口：Oathbots 代币约 0.73h（22:00 CST，已推过不重刷）；SpiritsRH 免费 mint 约 2.73h（2026-11-20 00:00 CST，尚未 ≤2h）；VICE6 / volta airdrop 约 10.73h（2026-11-20 08:00 CST）；DUCKS 站点关约 13.73h（2026-11-20 11:00 CST）；Boxcars 预售约 23.73h（2026-11-20 21:00 CST）；INMATES 公开免费 mint 约 26.73h（2026-11-21 00:00 CST）；AUGENT 截止约 47.61h。

## 下轮提示

- UF next 1646 PonkeAgent；agentPad next 583 cashcat_Agent。
- mentions 下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 下一轮：GO盘。
- lastFullAfterReset 仍为 R1956。X remaining 438，额度仍充足，下轮继续十栏全跑。
- Oathbots 代币窗口 22:00 CST（约 0.73h），若出现开盘/可领翻转再核验推送；不要只因仍在 ≤2h 窗内每轮重复刷。
- Dividends 二级成交/退款若出现可核验的开盘交易再决定是否补推，不要只因官宣「几分钟后交易」而空刷。
- 本轮已同步并推送 docs/data.json，下轮勿再漏同步。
- 本号不自动 mint。
