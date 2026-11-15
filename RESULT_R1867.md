# 早期打新雷达 R1867

- 时间：2026-11-15 20:07 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 loopiez；宣称免费 mint，但无官网/开铸时间/入口/CA，不得当成已核验免费 LIVE；非首次 ≤2h，属真新）
- 新收录：loopiez（@loopieznft）
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 1f26119 R1866）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 381 → remaining 356（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 381≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。本轮 thin official 与 UF 分片仅 Writ_Fi 重叠（已从 THIN3 去重），THIN official 5 批全读，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 484 / 1-based 485 usekyte 起，kept 48，真实 NF_skip 7（asciidogs、rheacatnear、99901dotfun、magnitudeagent、bububullfun、robinhoodhormuz、lanternfield，按已知 NF 未重读），walkScanned 55，无绕回。last kept 0-based 538 / 1-based 539 dominioncoins，next 0-based 539 / 1-based 540 streamlitmaker。收录后已把 @loopieznft 追加进 UF 与 freeMintWatch。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1（另含 ozero_fun）。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun（thinSkipDedup：ozero_fun 已在 MUST1，Writ_Fi 已在 UF1，未在 THIN 重读）。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=DogeEVM（1867%11=8）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=2，sentToReview=0，admitted=0，skipped=2（already_in_library 1 dogstarter，too_many_posts 1 layzjamal）。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。
- UF/MUST/THIN official start_time=2026-11-15T11:02:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T10:02:00Z（约 2h）。silent start=2026-11-14T12:04:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 1、MUST2 0、THIN1 0、THIN2 7、THIN3 0、THIN4 1、THIN5 1、KW_LZ 4、KW_TAPE 25、KW_GIWA 20、KW_DOGE 25、KW_BTC 6、KW_SN 9、KW_MINT 25、KW_MINE 25、KW_PAD 25、KW_GO 2、KW_ELY 25、MEN_LZ 25、MEN_ELY 25、MEN_SQUE 0、MEN_BN 12、SILENT_MEN 3。
- 首读 UF1 后快照 380 / 1000，故 remainingBefore=381；末次 SILENT_MEN 快照 356 / 1000。
- THIN official 本轮 5 批。thinSkipDedup：ozero_fun、Writ_Fi。watchLeaks 0。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 新收录

- **loopiez**（@loopieznft，id=loopiez）：本轮 KW_MINT 盲捞发现。官号 2026-11-15 19:44 CST 建立（xUserId 2121932375055851520），0 粉、1 帖、following=2，无官网。唯一官帖 20:03 CST https://x.com/loopieznft/status/2121937055597097088 宣布 FREE MINT | 1111 LOOPIEZ | DROP EVM，附件仅为推文图片（t.co 只指向 photo/1），bio 写 Coming soon to Robinhood。无 mint 链接、无开铸时间、无白名单/每钱包规则、无 CA。DeepSeek-flash（思考开）admit=true，overall 55（early 95 / actionable 22 / novelty 45 / risk 25），category=打新，status=announced，focus=false。已进 userFollowWatch + freeMintWatch。话术与同窗 Gloopix（Drop EVM / coming to Robinhood）相似，可能是跟风号。**不得写成已核验免费 LIVE**。非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。

## 在库窗口 / 可操作变化

- **DualForge**（@DualForgeBSC）：原定开铸 2026-11-15 19:00 CST 已过。本轮约 20:07 CST 复查，MUST1 本 1h 官方窗仍无该号新帖，仍无官网/新 CA/开闸确认，status 保持 announced，不是已确认开铸。首次进入 ≤2h 已在 R1861 推送，本轮不重推。le2h 已关。仅限 Binance Agent ID。
- **hokiseries**：Base Bots 公售官方结束时钟 2026-11-15 20:00 CST 已过。MUST1 本 1h 官方窗无该号新帖，未见官方关窗确认或新阶段。已在 R1815 按开窗 ≤2h 通知且当时已写明结束时间，本轮不重推。价格 0.0001 ETH，不是免费。
- **osk-agent**（@AIAgent_OSK）：MUST1 本 1h 官方窗无该号新帖。池已开事件已在 R1863 推送并写入已核验 CA，R1865 已记录 19:04 CST 再述同一口径，本轮不重推。付费只告警，本号不自动 mint。
- **jacketagent**：MUST1 本 1h 官方窗无该号新帖。免费仍 LIVE 至 2026-11-16 00:00 CST（约 3.9h），尚未进入 ≤2h，不重推。
- **POLYROB**（@tmachinroBot）：MUST1 本 1h 官方窗无该号新帖。关闭时间仍为 2026-11-16 01:12 CST，约 5.1h，尚未 ≤2h，已按此前窗口通知，不重推。
- **pillowbook-rh**（@pillowbookRH）：MUST1 本 1h 官方窗无该号新帖。开窗仍为 2026-11-16 01:00 CST，约 4.9h，尚未进入 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST（5pm UTC），尚未 ≤2h，不重推。
- **MicroFrens**：MUST1 本 1h 官方窗无该号新帖。对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送），无新的对公窗口或份额规则变化，不重推。
- **Gloopix**（@Gloopix_）：官号 19:44 CST https://x.com/Gloopix_/status/2121932234391466390 发 “COLLAB IS OPEN - DM US / 2,222 Gloopix coming to @RobinhoodCrypto soon / Drop EVM”。仍是预告/合作征集口径，无开铸时间、无官网、无已核验 CA，不能写成免费 LIVE，也不是新的可操作窗口，不重推。
- HoodTurtle / DeadHood_nft / infamousScratch / ozero_fun 本窗无新帖。hood-turtle mint 仍是 11-17 22:15 CST。
- UF1 见到 @ToritoTeamUS 再发已于 10-07 上线 Pons 的营销帖，项目已在库（toritoteamus），不是新窗口，不重推。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 TAPE/DOGE 与核心栏 KW_MINT/MINE/PAD/ELY 打满 25 条硬顶；KW_GIWA 20；KW_SN 9；KW_BTC 6；KW_LZ 4；KW_GO 2。mentions：LayerZero 25、Elysium 25、squeek/Nutshell 0、BN Agent pads+STARX 12。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞独立发现 @loopieznft（0 粉、今日新建号），不是靠关注表。
- 未送审（不收录）：**MoonAI__BSC**（CA 0x11f07e749af9440c9cb4bd455e7dd992be58cc7f 已在 Pancake 交易，24h 成交约 16 万 U，非早期打新窗口）；**Bizness7771**（指向 trycloudflare 的「免费授权检查」，疑似钓鱼，不收录）；大量 KW_PAD/DOGE 互动号与 K-pop $PULSE 噪音。memecallxxx 第三方复盘提到 Agent ID 免费铸造（Pi、Agent Bubbles、DACITY、Agent PEPE、Entr0pic、Bold Leonidas、SpoxyFun Ghosts），其中 Agent PEPE / Entr0pic / SPOXY 已在库；其余本窗未见官号，未为「再确认」额外刷 X，不收录。

## Watch 漏挂修复

- 本轮 0。loopiez 写入 userFollowWatch + freeMintWatch。在库且本轮新卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1867.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 loopiez（未核验免费 LIVE）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 539 streamlitmaker 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- DualForge 原定 19:00 CST 开铸已过但本窗仍无开闸/CA 确认，不要把「到点」写成已开铸；首次 ≤2h 已在 R1861 推送，后续不要重复提醒，除非出现新 CA、官方开闸确认、改期或其他可操作变化。
- osk-agent 池已开事件已在 R1863 推送并写入已核验 CA，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟 20:00 CST 已过且无新阶段官宣，已在 R1815 写明结束时间，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 免费 LIVE 至 11-16 00:00 CST，进入 ≤2h 后再判断。
- bamboo-ronin 不得在后续轮次仅凭 bio 写成免费 LIVE；需官网、官方开窗帖或 CA 之一确认。
- panko 不得把站点「Your first pet is free / Soon on Robinhood Chain」写成已核验免费 LIVE；需官方开窗或可核验 mint 入口。
- loopiez 不得把官帖「FREE MINT | 1111 LOOPIEZ | DROP EVM」写成已核验免费 LIVE；需官网、官方开窗或可核验 mint 入口。
- kinetiq-toons 已在 R1865 DS skip（WL 已关、mint TBA）；若后续官宣开铸/免费 LIVE 再核收录。
- framble 已在 R1866 DS skip（无官网、无 CA）；若官网或链上证据出现再核收录。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
- Gloopix 本轮新帖仍是合作征集/预告，不要写成免费 LIVE 或当作新窗口重推。
