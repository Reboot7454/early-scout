# 早期打新雷达 R1866

- 时间：2026-11-15 19:43 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 lanternsol、panko；均非已核验免费 LIVE、非首次 ≤2h，但属真新。panko 站点写首只宠物免费且 soon / launches not open，不得当成免费 LIVE）
- 新收录：lanternsol（@lanternsolana）、panko（@PankoAI）
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 53a7b70 R1865）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 406 → remaining 381（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 406≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。本轮 thin official 与 UF 分片无重叠，THIN official 5 批全读，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM（GIWA 与 Tape 按官方核心子集，避免超长 query 拆成额外读）。
- userFollowWatch 已刷完本分片：从 0-based 430 / 1-based 431 SwarmHiveBNB 起，kept 48，真实 NF_skip 6（SwarmHiveBNB、twinmetahq、astrispace、Fairagent_bnb、ChyAI_Official、snakeidbnb，按已知 NF 未重读），walkScanned 54，无绕回。last kept 0-based 483 / 1-based 484 WobblokzAI，next 0-based 484 / 1-based 485 usekyte。收录后已把 @lanternsolana、@PankoAI 追加进 UF。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1（另含 ozero_fun）。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun（thinSkipDedup 仅 ozero_fun 已在 MUST1，未在 THIN 重读）。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=GIWA（1866%11=7）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=44，sentToReview=0，admitted=0，skipped=44（too_many_posts 24，already_in_library 11，profile_unresolved 9）。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。
- UF/MUST/THIN official start_time=2026-11-15T10:37:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T09:37:00Z（约 2h）。silent start=2026-11-14T11:37:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 1、MUST1 3、MUST2 0、THIN1 2、THIN2 7、THIN3 0、THIN4 0、THIN5 0、KW_LZ 4、KW_TAPE 25、KW_GIWA 24、KW_DOGE 25、KW_BTC 10、KW_SN 10、KW_MINT 25、KW_MINE 8、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 25、MEN_GIWA 25、MEN_BTC 18、MEN_SNDOGE 25、SILENT_MEN 25。
- 首读 UF1 后快照 405 / 1000，故 remainingBefore=406；末次 SILENT_MEN 快照 381 / 1000。
- THIN official 本轮 5 批。thinSkipDedup 仅 ozero_fun。watchLeaks 0。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 新收录

- **lanternsol**（@lanternsolana，id=lanternsol）：本轮 KW_PAD 盲捞发现。官号 2021-05-17 14:15 CST 建立（xUserId 1394174565895446529），0 粉、3 帖、following=2，疑似旧号新用。官网 https://lanternsol.xyz/ HTTP 200，资料栏回链官网，站点 /api/sky 字段 `x=https://x.com/lanternsolana`，互链成立。官帖 19:14 CST https://x.com/lanternsolana/status/2121924810515120271 宣布 LANTERN is live on Solana：Raydium LaunchLab 发射台，每日 00:00 UTC 把当日手续费 50% 分给 $LANTERN 持有者、30% 给当日头部代币、20% 随机一名买家。站点 JS `HOST_CLUSTER=mainnet`；API `cluster=mainnet`，`house.launched=false`，公布 $LANTERN mint `CqDb6nerCnUJLT4Gg7DiPjhB78QZUaZ1wUDE7k12Wsky`（本轮未做链上独立核验，caUnverified=true），lanterns=[]、成交与奖池均为 0。DeepSeek-flash（思考开）admit=true，overall 63（early 88 / actionable 52 / novelty 55 / risk 35），category=台子/Meme，status=live（发射台主网已开，house token 尚未发射），focus=false。已进 userFollowWatch。非免费 mint、非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。
- **panko**（@PankoAI，id=panko）：本轮 KW_PAD 盲捞发现。官号 2026-10-08 05:05 CST 建立（xUserId 2107939449820663808），138 粉、22 帖、following=20。官网 https://pankopets.com/ HTTP 200，资料栏回链官网，但站点 JS/HTML 未见回链 https://x.com/PankoAI，互链不成立（单向）。官帖 19:36 CST https://x.com/PankoAI/status/2121930383797227873 介绍 ERC-8004 公开记录与后续 Uniswap v4 hooks。站点文案写 Your first pet is free. Soon on Robinhood Chain，同时写 Launches are not open yet。未见 CA。DeepSeek-flash admit=true，overall 57（early 80 / actionable 40 / novelty 68 / risk 52），category=打新，status=announced，focus=false。已进 userFollowWatch。**不得写成已核验免费 LIVE**。非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。

## 在库窗口 / 可操作变化

- **DualForge**（@DualForgeBSC）：原定开铸 2026-11-15 19:00 CST 已过。本轮约 19:43 CST 复查，MUST1 本 1h 官方窗仍无该号新帖，仍无官网/新 CA/开闸确认，status 保持 announced，不是已确认开铸。首次进入 ≤2h 已在 R1861 推送，本轮不重推。le2h 已关（开铸时刻已过且未确认 LIVE）。仅限 Binance Agent ID。
- **osk-agent**（@AIAgent_OSK）：MUST1 本 1h 官方窗无该号新帖。池已开事件已在 R1863 推送并写入已核验 CA，R1865 已记录 19:04 CST 再述同一口径，本轮不重推。付费只告警，本号不自动 mint。
- **hokiseries**：Base Bots 公售仍至 2026-11-15 20:00 CST（约 0.3h），仍在结束窗 ≤2h。该公售已在 R1815 按开窗 ≤2h 通知且当时已写明结束时间，本轮无该号新帖，不重推。价格 0.0001 ETH，不是免费。
- **POLYROB**（@tmachinroBot）：MUST1 再见同一条关窗官帖 https://x.com/tmachinroBot/status/2121921345948705009，关闭时间仍为 Sun 17:12 UTC = 2026-11-16 01:12 CST，约 5.5h，尚未 ≤2h，已按此前窗口通知，不重推。
- **pillowbook-rh**（@pillowbookRH）：MUST1 再见同一条 T-6h 官帖 https://x.com/pillowbookRH/status/2121921165199290586，开窗仍为 Sun 15 Nov 17:00 UTC = 2026-11-16 01:00 CST，尚未进入 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST（5pm UTC），尚未 ≤2h，不重推。
- **jacketagent**：MUST1 本 1h 官方窗无该号新帖。免费仍 LIVE 至 2026-11-16 00:00 CST（约 4.3h），尚未进入 ≤2h，不重推。
- **MicroFrens**：MUST1 本 1h 官方窗无该号新帖。对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送），无新的对公窗口或份额规则变化，不重推。
- **Gloopix**（@Gloopix_）：官号 19:33 CST https://x.com/Gloopix_/status/2121929608761323822 再发“2,222 Gloopix coming to @RobinhoodCrypto soon / The next chapter of Gloopix starts on-chain / Drop EVM”。仍是预告口径，无开铸时间、无官网、无已核验 CA，不能写成免费 LIVE，也不是新的可操作窗口，不重推。
- HoodTurtle / DeadHood_nft / infamousScratch / ozero_fun 本窗无新帖。hood-turtle mint 仍是 11-17 22:15 CST。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_GIWA 24；KW_SN 10；KW_BTC 10；KW_MINE 8；KW_LZ 4。mentions：Tape 25、GIWA 25、BTC 18、Starknet+DogeEVM 25。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。GIWA（40 handle）与 Tape（24 handle）mentions 使用官方核心子集，未拆成额外读。
- 发现不等于关注：本轮主栏盲捞独立发现 @lanternsolana（0 粉旧号新用）与 @PankoAI（138 粉），不是靠关注表。
- 未送审（不收录）：**framble**（@FrambleAI，0 粉、16 帖，资料栏无网站，官帖称本月才上官网并开 open beta，无 CA、无链上证据）DeepSeek admit=false overall 38，暂不列入。另跳过 BrokeAF_Sol（已在 Raydium 上线的 meme 币、非早期窗口）以及 KOL/giveaway 噪音。numencash 已在库。

## Watch 漏挂修复

- 本轮 0。lanternsol / panko 写入 userFollowWatch。在库且本轮新卡均已在至少一个 Watch。matrix-agents 无官推，已在 agentPadWatch / bnAgentWatch / freeMintWatch，不视为漏挂。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1866.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 lanternsol、panko（未核验免费 LIVE）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 484 usekyte 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- DualForge 原定 19:00 CST 开铸已过但本窗仍无开闸/CA 确认，不要把「到点」写成已开铸；首次 ≤2h 已在 R1861 推送，后续不要重复提醒，除非出现新 CA、官方开闸确认、改期或其他可操作变化。
- osk-agent 池已开事件已在 R1863 推送并写入已核验 CA，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复客服回复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售至 20:00 CST，已进入结束窗但因 R1815 已写明结束时间不重推；结束后如有新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 免费 LIVE 至 11-16 00:00 CST，进入 ≤2h 后再判断。
- bamboo-ronin 不得在后续轮次仅凭 bio 写成免费 LIVE；需官网、官方开窗帖或 CA 之一确认。
- panko 不得把站点「Your first pet is free / Soon on Robinhood Chain」写成已核验免费 LIVE；需官方开窗或可核验 mint 入口。
- kinetiq-toons 已在 R1865 DS skip（WL 已关、mint TBA）；若后续官宣开铸/免费 LIVE 再核收录。
- framble 本轮 DS skip（无官网、无 CA）；若官网或链上证据出现再核收录。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
- Gloopix 本轮新预告帖仍无时间/官网/已核验 CA，不要写成免费 LIVE 或当作新窗口重推。
