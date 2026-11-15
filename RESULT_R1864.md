# 早期打新雷达 R1864

- 时间：2026-11-15 18:42 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 usemerged、pynki；均非免费 mint、非首次 ≤2h，但属真新）
- 新收录：usemerged（@usemerged）、pynki（@PynkiXYZ）
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 39b3e03 R1863）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 456 → remaining 431（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 456≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。本轮 thin official 与 UF 分片无重叠，THIN official 5 批全读，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 334 / 1-based 335 mcnuggetsonline 起，kept 48，真实 NF_skip 0，walkScanned 48，无绕回。last kept 0-based 381 / 1-based 382 AgenticHive，next 0-based 382 / 1-based 383 pitpadfun。收录后已把 @usemerged、@PynkiXYZ、@ArcPulseApp 追加进 UF。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=Elysium（1864%11=5）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，unique authors 21（rc 23），sentToReview=0，admitted=0。作者去重 21：在库 1；@ArcPulseApp 实为已在库 arc-pulse 的新官号（已改卡、不另收、不计入送审）；其余多为高帖量内容号或无产品信号（如 @dexgrade 安全检查工具）。pynki / usemerged 在主栏发现并收录，不计入静号送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T09:33:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T08:33:00Z（约 2h）。silent start=2026-11-14T10:33:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包（MUST1 及若干 KW/MEN）被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 16、MUST2 0、THIN1 3、THIN2 2、THIN3 1、THIN4 0、THIN5 1、KW_LZ 4、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 9、KW_SN 22、KW_MINT 25、KW_MINE 8、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 25、MEN_GIWA 25、MEN_BTC 25、MEN_SN_DOGE 25、SILENT_MEN 23。
- 首读 UF1 快照 455 / 1000，末次 SILENT_MEN 快照 431 / 1000。remainingBefore 取上轮结束 456，按 25 次递减记 remaining=431。
- THIN official 本轮 5 批。thinSkipDedup 无。watchLeaks 0。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 新收录

- **usemerged**（@usemerged，id=usemerged）：本轮主栏盲捞发现。官号 2026-11-14 17:01 CST 建立（xUserId 2121528716735987712），未认证，0 粉、1 帖、following=0。官网 https://usemerged.fun/ HTTP 200（另有 /docs /launch /coins /claim /token）。产品：为任意 GitHub 账号在 pump.fun（Solana）发射代币，creator fee 100% 锁定分给该 GitHub 账号，平台抽成 0%，可选首购 ≤5 SOL。资料栏 URL 解析为官网；站点静态/JS 未见 x.com/usemerged 回链，siteXMutual 不成立。官帖 18:27 CST https://x.com/usemerged/status/2121912913589879103。与库内 merged-finance（@MergedFinance_，旧 pump.fun meme，R371）不是同一项目。DeepSeek-flash（思考开）admit=true，overall 80（early 93 / actionable 72 / novelty 88 / risk 58），category=台子/Meme，status=live，focus=false。已进 userFollowWatch。非免费 mint、非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。
- **pynki**（@PynkiXYZ，id=pynki）：本轮主栏盲捞发现。官号 2026-10-31 07:17 CST 建立（xUserId 2116307815497158656），蓝标，34 粉、116 帖、following=80。官网 https://pynki.xyz/ HTTP 200，标题 PYNKI Protocol · Web3 Tools on Elysium；站点回链 https://x.com/PynkiXYZ，资料栏回链官网，互链成立。Telegram https://t.me/TheMaskedClub。工具：代币发现、交易终端、钱包、HYPE 桥、质押；宣称 $PYNKI 质押获项目收入 90%。静态页未见已核实 CA。本窗官帖仅为回复，非新开窗。Elysium 主网已于 2026-11-09 上线，属已上线工具，可收。DeepSeek-flash（思考开）admit=true，overall 71（early 80 / actionable 70 / novelty 62 / risk 72），category=Elysium，status=live，focus=false。已进 userFollowWatch + elysiumWatch。非免费 mint、非 ≤2h，但属真新，按 notify 规则推送。本号不自动 mint。

## 在库窗口 / 可操作变化

- **arc-pulse**（原 @Arcdepthoock）：本轮发现 @ArcPulseApp + https://arcpulse.app/ 为同一项目（docs 回链 @ArcPulseApp，hub 仍回链 @Arcdepthoock 并讨论 FTHM）。已把新官号与官网写入既有卡，并追加进 userFollowWatch + agentPadWatch + xChainPadWatch + arcPadWatch，不另建卡。站点现写 13 链（含 Elysium）、Pulse Squad 吉祥物；本窗官帖 18:28 CST https://x.com/ArcPulseApp/status/2121913125813248510 介绍 Elysium 吉祥物 Lumi，非新 mint 开窗，不推送。
- **osk-agent**（@AIAgent_OSK）：池已开事件已在 R1863 推送并写入已核验 CA（pair `0x0C1d8C5ec49A0075921922143e04ADF8240Bc8bB`，token `0xF3DE5D50Ff0b21fDAB5f5ee7AcD3Cbf78C2b2e68`）。本窗 18:33 CST https://x.com/AIAgent_OSK/status/2121914435002577287 仍写 “The pool is due now: the next seat opens it”，属同一开池窗口口径，不是新的可操作变化，不重推。付费只告警，本号不自动 mint。
- **DualForge**（@DualForgeBSC）：开铸仍 2026-11-15 19:00 CST。本窗 17:51 CST Flint/Quench 帖已在 R1863 记录，档期未改。本轮约 18:42 CST，距开铸约 0.3h，仍在 ≤2h，首次进入已在 R1861 推送，不重推。仅限 Binance Agent ID。未见新 CA。
- **MicroFrens**：对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送）。本窗无新的对公窗口或份额规则变化，不重推。
- **hokiseries**：Base Bots 公售仍至 2026-11-15 20:00 CST（约 1.3h），仍在结束窗 ≤2h。该公售已在 R1815 按开窗 ≤2h 通知且当时已写明结束时间，不重推。价格 0.0001 ETH，不是免费。
- **qtronlaptops**：官帖 18:34 CST https://x.com/qtronlaptops/status/2121914769716228435 称 SECOND BATCH UPLOADED，开铸仍为 Today 5pm UTC = 2026-11-16 01:00 CST，$1 / 4444，Robinhood via OpenSea。距开铸约 6.3h，尚未进入 ≤2h，不重推。
- **POLYROB**（@tmachinroBot）：本窗无新开窗确认，公售仍至 2026-11-16 01:12 CST，已按此前窗口通知，不重推。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST），未进入 ≤2h；pillowbookRH 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/GO/ELY 与薄栏 TAPE/GIWA/DOGE 打满 25 条硬顶；KW_MINE 8；KW_LZ 4；KW_BTC 9；KW_SN 22。mentions 四组均打满 25。
- mentions：Tape 25、GIWA 25、BTC 25、Starknet+DogeEVM 25。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞独立发现 @usemerged（新建号、0 粉）与 @PynkiXYZ，不是靠关注表。
- 未送审（不收录）：@launchonmorph 在 R1863 已拒绝，仍无已确认官网（0 粉、当日新建、2 帖）；@dexgrade 为跨链代币安全检查工具，不是 mint；@ValkyriSecurity 为安全公司；dogecolony.com 为域名出售页。其余为 giveaway / RT / KOL 噪音。OrdDropz 此前口径仍为只观察、不收录。

## Watch 漏挂修复

- 本轮 0。usemerged 写入 userFollowWatch；pynki 写入 userFollowWatch + elysiumWatch；@ArcPulseApp 追加进既有 arc-pulse 所在的 userFollowWatch + agentPadWatch + xChainPadWatch + arcPadWatch。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1864.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 usemerged、pynki。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 382 pitpadfun 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- DualForge 同一 19:00 CST 开铸窗口已在 R1861 按首次 ≤2h 推送，后续轮次不要重复提醒，除非档期改动、出现新 CA/开闸确认，或进入可操作变化。
- osk-agent 池已开事件已在 R1863 推送并写入已核验 CA，后续不要重复「池已开」提醒，除非出现新的可操作变化（例如新阶段、停池、明显流动性变化或新规则）。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复客服回复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售至 20:00 CST，已进入结束窗但因 R1815 已写明结束时间不重推；结束后如有新阶段再判断。
- qtronlaptops 同一 2026-11-16 01:00 CST 开铸窗口（本轮官帖只确认第二批已上传），尚未进入 ≤2h，进入后再判断是否首次推送。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
