# 早期打新雷达 R1869

- 时间：2026-11-15 21:07 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（在库 Bitsigil 官方确认免费 WL 已开铸并公布 OpenSea 链接；新收录 klayo、setcap、st0cks，均非已核验免费 LIVE）
- 新收录：klayo、setcap、st0cks
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ e7d25c9 R1868）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 331 → remaining 306（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 331≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读，thinSkipDedup 无，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 599 / 1-based 600 thevoidling_rh 起，kept 48，真实 NF_skip 15（Ainubsc、agentcityuk、UseHyperLiquid、MonsterRH_、Derpagent_、Proxisfun、ramencoinmeme、letswinhood、agentharvest_ai、seatworkcells、frogsagent、Honestcoin60、DropMinters、onbeatfun、beatdotfamily，按已知 NF 未重读），walkScanned 63，无绕回。first kept 0-based 599 thevoidling_rh，last kept 0-based 661 / 1-based 662 moonfall_bnb，next 0-based 662 / 1-based 663 usetrenchscope。
- DualForgeBSC / PlayBitsigil 不在本 UF 分片，已放入 MUST1（另含 ozero_fun）。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2；本窗仅 machinedotfun 一条视频向帖，非新 mint 窗口，非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun / PlayBitsigil。thinSkipDedup：无。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=Starknet（1869%11=10）。search_users 仍不在 X 工具目录，只走 mentions（Starknet OR Bramble）(mint OR launchpad)。silentAccounts.ran=true，seen=0，sentToReview=0，admitted=0，skipped=0。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST/THIN official start_time=2026-11-15T12:00:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T11:00:00Z（约 2h）。silent start=2026-11-14T13:00:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 0、UF2 1、MUST1 13、MUST2 1、THIN1 2、THIN2 8、THIN3 2、THIN4 2、THIN5 0、KW_LZ 7、KW_TAPE 25、KW_GIWA 14、KW_DOGE 25、KW_BTC 12、KW_SN 7、KW_MINT 24、KW_MINE 8、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_LZ 17、MEN_ELY 25、MEN_MINE 0、MEN_BN 0、SILENT_MEN 0。
- 首读 UF1 后快照 330 / 1000，故 remainingBefore=331；末次 SILENT_MEN 快照 306 / 1000。
- THIN official 本轮 5 批。thinSkipDedup：无。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **Bitsigil**（@PlayBitsigil，id=bitsigil）：在库自 R655，R1868 已按 21:00 CST 免费 WL ≤2h 首次推送（当时未见官方 mint 链接/CA，status=announced）。本轮 MUST1 官号 20:30 CST 公布 Official OpenSea link，21:00:02 CST 官帖 https://x.com/playbitsigil/status/2121951358425481451 称 “Firstbound, it starts here. Free Mint WL holders can now mint 1 NFT per wallet. Gas only.”，t.co/4IAwigwevW 解析为 https://opensea.io/collection/bitsigil/overview。同期官帖称 TEAM MINT COMPLETE，133 枚入金库不做销售。官网 bitsigil.xyz 与官推互链仍成立。FAQ 阶段表不变：21:00 免费 WL（只付 gas）→ 23:00 GTD $2 → 11-16 01:00 FCFS $2 → 02:00 公售 $3 共 48h。本轮仍未见独立核验 CA，不得发明合约。DeepSeek-flash（思考开）复评 overall 84（early 52 / actionable 94 / novelty 55 / risk 42），status 改为 live，le2h=true，focus=false。按 R1868 交接「若官方公布 mint 链接再判断是否重推」，本轮因官方开铸确认 + OpenSea 链接再提醒。本号不自动 mint。
- **DualForge**（@DualForgeBSC）：MUST1 再见同一组 20:21 CST “Minting is live” 官帖，已在 R1868 因官方开闸确认 + 官网 + 公布 CA 推送，本轮无改价/关窗/池已开等新的可操作变化，不重推。付费，仅限 Binance Agent ID。本号不自动 mint。
- **POLYROB**（@tmachinroBot）：MUST1 本窗再发末日提醒（https://x.com/tmachinroBot/status/2121939112093434165），关闭时间仍为 2026-11-16 01:12 CST（17:12 UTC），约 4h，尚未 ≤2h，已按此前窗口通知，不重推。
- **jacketagent**：MUST1 本 1h 官方窗无该号新帖。免费仍 LIVE 至 2026-11-16 00:00 CST（约 2.9h），尚未进入 ≤2h，不重推。
- **pillowbook-rh**（@pillowbookRH）：MUST1 本 1h 官方窗无该号新帖。开窗仍为 2026-11-16 01:00 CST，约 3.9h，尚未进入 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST（5pm UTC），尚未 ≤2h，不重推。
- **hokiseries**：公售官方结束时钟 2026-11-15 20:00 CST 已过。MUST1 本 1h 官方窗无该号新帖，未见官方新阶段。已在 R1815 写明结束时间，不重推。
- **osk-agent**（@AIAgent_OSK）：MUST1 本 1h 官方窗无该号新帖。池已开事件已在 R1863 推送，本轮不重推。
- **MicroFrens**：MUST1 本 1h 官方窗无该号新帖。对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送），无新的对公窗口或份额规则变化，不重推。
- **Gloopix**（@Gloopix_）：MUST1 本窗无新的可操作官帖，不能写成免费 LIVE，不重推。
- **ozero**（@ozero_fun）：MUST1 本窗无新的可操作变化，不重推。
- **AgentCardsHQ**（@AgentCardsHQ）：UF2 本窗发帖称持卡对 CARDS 预售加成为 +20%/+50%，快照 11-24 15:00 UTC。已是在库卡，不是新的对公 mint 窗口，不推送。
- **machinedotfun**：MUST2 本窗一条视频向帖，非新 mint 窗口，不推送。

## 新收录

- **klayo**（@klayonft）：KW_MINT 用户对象核验（未另拉时间线）。官号 2026-11-09 06:39 CST 建立，544 粉、11 帖，资料栏官网 https://www.klayo.xyz/。官网 HTTP 200，Checker 页写明 Follow @klayonft，互链成立。Robinhood Chain NFT launchpad，有 WL Arena 与 $KLAYO 空投估分 Checker；Checker 写明不是 NFT mint / 白名单。bio 有 /Free Mint，但未见已核验开铸入口、开窗时刻或 CA，**不得写成已核验免费 LIVE**。DeepSeek-flash admit=true，overall 66，category=打新，status=announced，focus=false。已进 userFollowWatch + freeMintWatch。
- **setcap**（@setcapdotfun）：KW_PAD 独立盲捞。官号 2026-11-04 23:21 CST 建立，0 粉、13 帖。官网 https://setcap.fun HTTP 200，自称 Solana 发币台（$5K–$100K 起、5x 毕业），站点未见回链 X，互链不成立。20:47 CST 官帖讨论计价精度。未见 CA 或可操作窗口。DeepSeek-flash admit=true，overall 54，category=台子/Meme，status=announced，focus=false。已进 userFollowWatch。
- **st0cks**（@St0cksfun）：THIN1 @0rigindotfun 回复提及后，用已有 includes 用户对象核验，未另开 X 查询。官号 2026-11-10 00:45 CST 建立，91 粉、仅 2 帖。官网 https://st0cks.fun HTTP 200 但页面极薄，自称 Zero 股票 meme launchpad concept，未见回链 X。LZ 未核验，lzVerified=false，归台子/Meme。未见 CA 或窗口。DeepSeek-flash admit=true，overall 42，status=announced，focus=false。已进 userFollowWatch + layerZeroWatch。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_PAD/GO/ELY 打满 25 条硬顶；KW_MINT 24；KW_GIWA 14；KW_BTC 12；KW_MINE 8；KW_LZ 7；KW_SN 7。mentions：LayerZero 17、Elysium+kinetiq 25、mining-squeek+Nutshell 0、BN Agent pads+STARX 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞独立抓到 @setcapdotfun；@klayonft 经 KW_MINT includes 核验官网与互链后收录。
- 未送审（不收录）：**WelcomeGTA6** 为 GTA 6 粉丝盘，资料栏是 grok.me 页、无正规官网、自称 dropping soon，不收录；**Lanternhold** 本轮仅见第三方 @Jennifer_Verse 送 30× GTD 免费名额，无本轮官号核验新窗口，在库卡不重推；**MeowCardsBSC** 已在库免费首铸/预售 LIVE，规则未变，已多次提醒，不重推；PlayPixelora / numencash / companions-wfit / syndicate-rhc / rarelist 已在库。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张漏挂。
- 新卡已进 Watch：klayo → userFollowWatch + freeMintWatch；setcap → userFollowWatch；st0cks → userFollowWatch + layerZeroWatch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1869.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：Bitsigil 免费 WL 已开铸（官方 OpenSea 链接已公布，未见 CA）；新收录 klayo / setcap / st0cks（均非已核验免费 LIVE）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=0。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 662 usetrenchscope 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。silent 下一轮 打新（1870%11=0）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 官方开铸 + OpenSea 链接已在本轮推送；后续不要只因同一免费 WL 窗口每轮重推，除非出现关窗、改规则、公布已核验 CA、阶段切换（如 GTD/FCFS/公售开始）或 mint 入口变化。
- DualForge 官方开闸已在 R1868 推送，后续不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟 20:00 CST 已过且无新阶段官宣，已在 R1815 写明结束时间，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 免费 LIVE 至 11-16 00:00 CST，进入 ≤2h（约 22:00 CST）后再判断。
- bamboo-ronin 不得在后续轮次仅凭 bio 写成免费 LIVE；需官网、官方开窗帖或 CA 之一确认。
- panko 不得把站点「Your first pet is free / Soon on Robinhood Chain」写成已核验免费 LIVE；需官方开窗或可核验 mint 入口。
- loopiez 不得把官帖「FREE MINT | 1111 LOOPIEZ | DROP EVM」写成已核验免费 LIVE；需官网、官方开窗或可核验 mint 入口。
- klayo 不得把 bio「/Free Mint」或 Checker/WL Arena 写成已核验免费 LIVE；需官方开窗或可核验 mint 入口。
- setcap / st0cks 暂无可操作窗口，不要当作 LIVE 重推。
- WelcomeGTA6 未收录（粉丝盘 + grok.me 页）；不要为再确认额外刷 X，除非出现正规官网或官号可核验 mint 证据。
- cubicle_hood 仅第三方 RT，未收录；不要为再确认额外刷 X，除非出现官号或官网证据。
- Gloopix 预告/合作征集口径不要写成免费 LIVE 或当作新窗口重推。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
