# 早期打新雷达 R1861

- 时间：2026-11-15 17:10 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（DualForge 首次进入 ≤2h，开铸 2026-11-15 19:00 CST，约 1.9h）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ a769261 R1860）。

## X 额度与覆盖

- remainingBefore 529 → remaining 505（日硬顶 1000，重置约 08:00 CST）。xReads 24（main 23 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 23 超 softCap 18（+5），已达 minSpend 18：UF×2 + MUST×2 + THIN×4 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 24。因 remaining 529≫200，按用户「额度够时不得砍栏」补齐核心栏 KW×5 与 mentions 轮换 4 组，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 190 / 1-based 191 Elysdex 起，kept 48，真实 NF_skip 0（不沿用过期 NF 表），walkScanned 48，无绕回。last kept 0-based 237 / 1-based 238 theneonodyssey，next 0-based 238 / 1-based 239 acmeonbtc。
- DualForgeBSC 落在本 UF 分片，MUST1 去重不再拉。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：DualForgeBSC（本轮在 UF）。MUST1 覆盖 MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。MUST1 打满 25 条硬顶（MicroFrens 11 + OSK 7 + infamousScratch 4 + tmachinroBot 3），未翻页。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=台子/Meme（1861%11=2）。search_users 仍不在 X 工具目录，只走 mentions，result_count=25，无本雷达可操作新官号，未送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T08:03:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T07:03:00Z（约 2h）。silent start=2026-11-14T09:03:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 0、UF2 1、MUST1 25、MUST2 0、THIN1 3、THIN2 0、THIN3 0、THIN4 7、KW_LZ 2、KW_TAPE 25、KW_GIWA 23、KW_DOGE 25、KW_BTC 2、KW_SN 5、KW_MINT 25、KW_MINE 1、KW_PAD 25、KW_GO 2、KW_ELY 25、MEN_LZ 9、MEN_ELY 25、MEN_MINE 0、MEN_BN 2、SILENT_MEN 25。
- 首读 UF1 快照 528 / 1000，末次 SILENT_MEN 快照 505 / 1000。remainingBefore 取上轮结束 529，按 24 次递减记 remaining=505。
- THIN official 本轮 4 批。thinSkipDedup：tapekeyofficial / TapeId_AI / owlgatecli / GiwaPumpPad（本轮在 UF 分片）。

## 新收录

- 无。

## DeepSeek 未收录 / 未送审

- 本轮无送审项（dsFallback=false）。文案 alertMessage / whatsNew / 卡片 whatsNew 由 deepseek-flash 生成（卡片细则按既有窗口事实补全，未编造）。
- **未送审**：SneakPeak560 为已在 Peak Launchpad 发射的 Solana meme，非本雷达可操作新窗；HOODVERSENFTs / tinylegendsfun / glyphoras 仅为第三方 GTD/免费名单转帖，本窗未见官号发帖，不另开核验读；puuma012 / Galadomaiugb / Ooriven 为社区转帖或回复；Bullshot911 已在库；dogstarter 测试网 $SPARKY 已在库；KLV Gold Miner 在 Klever，不在本雷达链范围。其余多为 Tape/GIWA/Elysium 社区回复与 GTD 噪音。

## 在库进度

- **DualForge**（@DualForgeBSC）：开铸仍 2026-11-15 19:00 CST。本 1h 官方窗无新官帖，档期未改。本轮约 17:10 CST，距开铸约 1.9h，**首次进入 ≤2h，本轮推送**。仅限 Binance Agent ID 持有者，每轮一对 Agent ID / 一台 rig，可 burn tokens 提升 key weight/tier。未见新 CA。本号不自动 mint。
- **osk-agent**（@AIAgent_OSK，status=failed）：官号约 17:03 CST 再确认 2026-11-15 18:00 CST 开池，满不满员都开，0.008 BNB，每个 BSC .ai Agent ID 一席，免费席已尽（https://x.com/AIAgent_OSK/status/2121891880715616660 ；约 16:32 CST https://x.com/AIAgent_OSK/status/2121884134369022327）。同一窗口已在 R1859 首次推送，本轮约 0.9h，**不重推**。付费只告警不自动打。
- **MicroFrens**：对公 FCFS 已结束。持有者 OG FREE 仍在进行（R1860 已首次确认并推送）。本窗官号继续客服：约 16:35 CST 称 this free mint IS for paid minters（https://x.com/MicroFrens/status/2121884579183448451）；约 16:35 CST 称正在 remaking the NFT，rare 数量不变（https://x.com/MicroFrens/status/2121884683877368220）；约 16:51 CST 让用户检查钱包或仍有可铸额度（https://x.com/MicroFrens/status/2121888813027090789）。不是新阶段或份额规则重开，**不重推**。
- **POLYROB**（@tmachinroBot）：约 17:01 CST 再确认公售仍开放，一口价 0.033 ETH，至 Sun 15 Nov 17:12 UTC（2026-11-16 01:12 CST）。https://x.com/tmachinroBot/status/2121891224604880943 。已按此前窗口通知，不重推。
- **Animal Pharm**（@infamousScratch）：仍为售罄后的日常回复，无新开窗，不重推。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST）；hokiseries 公售至 20:00 CST（约 2.9h）尚未进入结束窗 ≤2h；qtronlaptops / pillowbookRH 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。tapeai 11 月 16 日开放 BEM 预存仍无具体钟点。DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗，均未进入 ≤2h。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/ELY 与薄栏 TAPE/DOGE 打满 25 条硬顶；KW_GIWA 23；KW_MINE 1；MEN_MINE 0。
- mentions：LayerZero 9（已在库 PlunderPort/Twinkle 等互动与第三方讨论）；Elysium+kinetiq 25（社区/archerswap 等已在库互动）；mining-squeek+Nutshell 0；BN Agent pads+STARX 2（无新官号）。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮关键词/mentions 盲捞未独立发现可收录的新官号；UF 分片仅 ARCYResearch 1 条研究报告（已在库）。

## Watch 漏挂修复

- 本轮 0。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1861.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：0 新收录，但 DualForge 首次进入 ≤2h（19:00 CST 开铸，仅限 Binance Agent ID）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 238 acmeonbtc 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- DualForge 同一 19:00 CST 开铸窗口已在本轮按首次 ≤2h 推送，后续轮次不要重复提醒，除非档期改动、出现新 CA/开闸确认，或进入可操作变化。
- osk-agent 同一 18:00 CST 开池窗口已在 R1859 推送，不要重复提醒，除非档期改动或出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复客服回复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售至 20:00 CST，约 18:00 CST 起进入结束窗 ≤2h，届时再判断是否提醒（R1815 已作过开窗 ≤2h 通知）。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
