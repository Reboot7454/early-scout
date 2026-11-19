# RESULT_R1990

- round: 1990
- lastScout: 2026-11-20 01:11:41 CST
- notify: true
- added: 无真新收录
- alert: R1990 面板 https://reboot7454.github.io/early-scout/ ：INMATES 已开铸，CA 0x5162a8b2B31B45215471C70F93AD11bcadd814A0，链上 6/999，PRICE 0.0005 ETH（非0），官网 https://inmates3.vercel.app/ ；官推写 Free Mint，但以合约为准，不能写成免费 LIVE；本号不自动 mint。SpiritsRH 链上 112/3333、仅2个收款地址，不像对公众开闸。

## 通知原因

已在库 INMATES（@INMATES_RH）**实际开铸翻转**。官推 2026-11-20 00:35:44 CST（https://x.com/INMATES_RH/status/2123455193169674716）宣布 Mint is live / First 100 wallet，00:49:23 CST（https://x.com/INMATES_RH/status/2123458629676536193）宣布 Free Mint is live / sold out soon，均指向新站 https://inmates3.vercel.app/（站内链到 @INMATES_RH，siteXMutual=yes）。新站 mint.js HTTP 200；deployments.json 在 Robinhood 4663 登记 CA `0x5162a8b2B31B45215471C70F93AD11bcadd814A0` 且 mintOpen=true。链上已核验 name/symbol=INMATES，MAX_SUPPLY=999，totalSupply=6，MAX_PER_TX=100，PRICE=0.0005 ETH（500000000000000 wei，非 0）。TREASURY=`0x0ce921C407Dd60d72DB28C4381a50dFfc06d43A2`。合约无 mintOpen()，开闸标志来自官网 deployments.json。观察到 1 笔 Transfer：00:21:54 CST tx `0xfe354a306e5212794b5ab1d0a74e01d3089d3367e35ff57cfd1898dd3a239129`，tokenId=6 铸给金库。旧站 https://www.inmates.online/ 仍 HTML MINT_STATE=live 但 /mint.js 404。原公开窗预告 2026-11-21 00:00 CST，已提前开闸。**官推写免费，但合约价非 0，不能写成免费 LIVE，以合约为准。** DeepSeek overall=70。本号不自动 mint。

SpiritsRH 不单独按对公众开铸重推（见下），仅在同一条告警里作附记。

## X 覆盖

- xReads 20（main 19 + silent 1 + EXTRA 0），remainingBefore 296 → remaining 276。
- mode pace（softCap 18 / minSpend 18 / silentCap 2），但 remaining ≫ 200，按用户规则未砍栏，十栏关键词 + BTC/Starknet + 4 组 mentions 全跑。
- 20 次并行 search_posts_all footer 最高 295、最低 276，故 remainingBefore 按 footer+1 记 296。
- 十栏关键词全跑：KW_MINT / KW_PAD / KW_GO / KW_ELY 达 25 上限未翻页；KW_GIWA=21 / KW_DOGE=14 / KW_TAPE=8 / KW_BTC=4 / KW_LZ=3 / KW_SN=3 / KW_MINE=3。
- UF 分片 start 29 flapdotsh，kept 50（flapdotsh→CrackAFortune），walk 60，NF_skip 10（ElysiumOutlaws, deadpacksol, blindfloor, blobsdotmeme, trytoprint, PlayFarmFi, reynarlabs, world_ygg, rektazhy59942, 0xvernull；FoundryTape 因 NF_PROTECTED 保留），wrap=false，next 89 hanokreserve。
- PRIO 在分片内：machinedotfun, bscaidrop, PulseLaunchpad, localbottomcom；折进 UF1 未另读：NutshellMarkets, starx_xlayer, mobster_meme。
- 帖数：UF1=0 / UF2=1 / MUST=2 / FAT_PAD=2。
- MUST 6 号全扫（spiritsHOOD, Vice6fun, Dividendsarts, INMATES_RH, CherylB83488, Oathbots），均不在本 UF 分片；本窗新官帖仅 @INMATES_RH 两条开铸帖。
- agentPad 从 772 wagmint_bnb 起 kept 25（→ITSMEkkdot），walk 25，skip 无，wrap=false，next 797 GTAFounder。
- mentions 本轮：LayerZero 25 / Elysium+kinetiq 25 / mining-squeek+Nutshell 1 / BN Agent pads+STARX 2。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 本轮 Starknet（1990%11=10），SILENT_MEN result_count=1，无新录取。下一轮：打新。
- search_users 仍不可用；thinOfficialDeferred=true；discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 仍为 R1956。无 EXTRA get_users 重读。

## 筛查 / 录取

- parse_x：official_posts 5，authors 167，new 161，in_lib 6，mention_new 102。
- 在库帖：UF2 @StargazeSpooks（已在库，非新窗）；FAT_PAD @allincrypto_ai（已 LIVE，本轮官帖宣布进入 Agent ID Hackathon，只刷新进度）；MUST 两条皆 INMATES 开铸帖。
- 年轻新号未达录取门槛，未批量送审：@SolveOpenMath（0.6d，数学/AI）、@floats37（2.4d，pre-IPO ETF）、@InformedApeAI（4.0d，R1989 已驳回，仍非 On testnet / Announced+deploy）、@TopRugRadar（4.7d，骗局检测）、以及收藏/回复噪声号。
- 无真新收录。INMATES 为已在库项目的开铸翻转（R1960 收录，此前因 mint.js 404、无 CA 不能视为实际开铸）。

## 已收录进度（不单独重推）

- PikaCHAN：仍 62/1111（均为免费），mintOpen=true，与上轮持平，不重推。本号不自动 mint。
- the one：仍 87/100，池未开，仍免费段。
- AUGENT：freeClaimed 仍 1493/2999，sold() 仍 73，池未开，截止约 43.69h。
- AIC：minted 仍 13464，LP 约 63.33 BNB（上轮约 59.83，上升），LB holderCount 1513（上轮 1487，+26），lbTotalShares=13464 与链上 minted 一致。
- AIM：725（上轮 723，+2）。
- AONE：hero 仍 22864、LP 约 0.0097 BNB，freeMinted 仍 10000。
- Bsc Cat：仍 563/800，paid=0，池未开。
- Dead Zone：API 200，minted 159/4500（上轮 142，+17），OG=1，VIP=3，FO=1（上轮 FO=0）。
- UGP：WL 537/15000（上轮 536，+1），phase FCFS，open=true。
- Arklis：FCFS 仍 12/150。
- DUCKS：minted 仍 136/3000，freeRemaining 沿用 374；站点关 2026-11-20 11:00 CST（约 9.81h），非≤2h。
- Fistagent：主 CA totalMinted 仍 1246，pair 储备仍 0/0。
- gmgm：市值约 $19563（上轮约 $15991），流动性约 $9174.7 / 54.2019 SOL。
- Boxcars：执照 NFT 仍 380/1000，raised 0.01 BNB，截止 2026-11-20 21:00 CST（约 19.81h）。
- ElysAgent Pass：totalSupply 仍 32。
- PandalZero：/api/status 仍 404，未证实满员翻转。
- Dividends：仍 1000/1000，publicPrice 0.0017 ETH，MUST 0 新官帖。
- BEETLE：已售仍 69/8000、13 买家、余额 0.15525 BNB，池未开，截止约 43.81h。付费，只报不自动打。
- Oathbots：已开盘（R1984 已推）。价约 $0.0001936（上轮约 $0.0001487），流动性约 $13357 / 11.4234 BNB，FDV 约 $193601。
- VICE6：官网仍 PRE-LAUNCH，空投门 2026-11-20 08:00 CST（约 6.81h，非≤2h），未见 CA，不重推。
- SpiritsRH：GTD 窗已于 01:00 CST 结束。链上 totalSupply 0→112/3333（集合 0x7b1eaef67aab0c5128e59e3d19f85b074c553aef），OpenSea sales=112、volume=0、num_owners=2。112 枚于 00:38:11–00:39:52 CST 约 1.7 分钟铸给 2 个地址（集合 owner 0xa257…4708 与 0x49ecd0…4425）。官网仍 WHITELIST OPEN，MUST 0 新官帖。暂不视为对公众开闸，不单独重推；不要把随后付费 PUBLIC 预告当成新免费窗。

## 下轮提示

- UF next 89 hanokreserve；agentPad next 797 GTAFounder。
- mentions 下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 下一轮：打新。
- lastFullAfterReset 仍为 R1956。X remaining 276，额度仍充足，下轮继续十栏全跑。
- INMATES：已开铸并本轮告警；下轮只刷新已铸进度与价格。若 PRICE 变为 0、售罄、或出现可核验的免费段翻转再报。本号不自动 mint。
- PikaCHAN：已免费 LIVE 并在 R1989 告警，下轮只刷新已铸进度；售罄、付费段占比跳升或开盘/池子出现可核验翻转再报。本号不自动 mint。
- the one：已 87/100，下轮盯满员或开池翻转，不要只因进度微调重推。
- SpiritsRH：仅在官网离开 WHITELIST 并出现可核验的对公众开铸、官方公布 CA 并开放公开 mint、或 OpenSea 出现明确对公众 isMinting 时再补推。不要把 2 地址预铸或付费 PUBLIC 预告当成新免费窗。
- VICE6 空投门 2026-11-20 08:00 CST；若官网/CA/盘口出现可核验开盘或门已开再推，勿把预告文案当成已开盘。若下轮进入 ≤2h 且此前未推过该门，再按 ≤2h 规则评估。
- BEETLE 为付费销售（已开、已售 69/8000），只报不自动打；售罄开池或退款期若出现可核验翻转再报。
- Dividends 二级成交/退款若出现可核验的开盘交易再决定是否补推，不要空刷。
- 本轮已同步并推送 docs/data.json，下轮勿再漏同步。
- 本号不自动 mint。
