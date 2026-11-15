# 早期打新雷达 R1862

- 时间：2026-11-15 17:37 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=false（0 新收录，也无首次进入 ≤2h / 首次确认免费 LIVE 的窗口）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ f61820a R1861）。
- dsFallback=false，docsSynced=true

## X 额度与覆盖

- remainingBefore 505 → remaining 481（日硬顶 1000，重置约 08:00 CST）。xReads 24（main 23 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 23 超 softCap 18（+5），已达 minSpend 18：UF×2 + MUST×2 + THIN×4 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 24。因 remaining 505≫200，按用户「额度够时不得砍栏」补齐核心栏 KW×5 与 mentions 轮换 4 组，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 238 / 1-based 239 acmeonbtc 起，kept 48，真实 NF_skip 0（不沿用过期 NF 表），walkScanned 48，无绕回。last kept 0-based 285 / 1-based 286 sigmacybercat，next 0-based 286 / 1-based 287 oddoneout_fun。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1，本窗 0 帖。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。MUST1 打满 25 条硬顶（MicroFrens 12 + OSK 7 + infamousScratch 4 + tmachinroBot 2），未翻页。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=GO盘（1862%11=3）。search_users 仍不在 X 工具目录，只走 mentions，result_count=6，全部为口语 go launch 噪音，无本雷达可操作新官号，未送审。silentAccounts.ran=true，seen=16，sentToReview=0，admitted=0，skipped=16。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T08:29:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T07:29:00Z（约 2h）。silent start=2026-11-14T09:29:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包（MUST1 与若干 KW）被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 0、UF2 0、MUST1 25、MUST2 0、THIN1 4、THIN2 0、THIN3 1、THIN4 2、KW_LZ 3、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 4、KW_SN 5、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 3、KW_ELY 25、MEN_TAPE 5、MEN_GIWA 1、MEN_BTC 0、MEN_SN_DOGE 1、SILENT_MEN 6。
- 首读 UF1 快照 504 / 1000，末次 SILENT_MEN 快照 481 / 1000。remainingBefore 取上轮结束 505，按 24 次递减记 remaining=481。
- THIN official 本轮 4 批。thinSkipDedup：GiwaGasok / GIWAForge / GenPad_Ai / acmeonbtc（本轮在 UF 分片）。

## 新收录

- 无。

## DeepSeek 未收录 / 未送审

- 本轮无送审项（dsFallback=false）。文案 metaWhatsNew / 卡片 whatsNew 由 deepseek-flash 生成（卡片附已核验证据链接，未编造）。
- **未送审**：Thesis_Protocol 为 Robinhood Chain 分红代币（官网 https://thesisprotocol.com/ ，testnet live，bio 称 Hold $THESIS get paid in stocks），未见可操作 mint/公平发售窗口，不收录；HOODVERSENFTs 仅为第三方 GTD/免费名单账号，社区称今天 14:00 UTC 开铸，本窗未见官号发帖，不另开核验读；fufufafau7 为已在库 @numencash 的新号喊单；web3xJQ 只是重复已知的 TapeAI 11 月 16 日 BEM 预存提醒，仍无具体钟点。静号 GO盘 mentions 全是口语 go launch。

## 在库进度

- **DualForge**（@DualForgeBSC）：开铸仍 2026-11-15 19:00 CST。本 1h 官方窗无新官帖，档期未改。本轮约 17:37 CST，距开铸约 1.4h，仍在 ≤2h，**首次进入已在 R1861 推送，本轮不重推**。仅限 Binance Agent ID 持有者。未见新 CA。本号不自动 mint。
- **osk-agent**（@AIAgent_OSK，status=failed）：官号再确认 2026-11-15 18:00 CST 开池，满不满员都开，0.008 BNB，每个 BSC .ai Agent ID 一席，免费席已尽（https://x.com/AIAgent_OSK/status/2121891880715616660 ；约 16:32 CST https://x.com/AIAgent_OSK/status/2121884134369022327）。这两帖 R1861 已引用。同一窗口已在 R1859 首次推送，本轮约 0.4h，**不重推**。付费只告警不自动打。
- **MicroFrens**：对公 FCFS 已结束。持有者 OG FREE 仍在进行（R1860 已首次确认并推送）。本窗新客服约 17:08 CST 称 yes but if you are on the snapshot you are able to mint for free !!（https://x.com/MicroFrens/status/2121893131469951243）。仍是同一持有者/快照免费阶段，不是新阶段或份额规则重开，**不重推**。
- **POLYROB**（@tmachinroBot）：约 17:01 CST 再确认公售仍开放，一口价 0.033 ETH，至 Sun 15 Nov 17:12 UTC（2026-11-16 01:12 CST）。https://x.com/tmachinroBot/status/2121891224604880943 。该帖 R1861 已引用，已按此前窗口通知，不重推。
- **Animal Pharm**（@infamousScratch）：仍为售罄后的日常回复，无新开窗，不重推。
- **TapeOut**（@TapeOutWorld）：约 17:14 CST 称 The Behemoth Official Mining Pool has completed its Phase 1（https://x.com/TapeOutWorld/status/2121894592715096123）。这是在库进度，不是新的可操作 mint 窗，不另推。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST），本窗无官帖，未进入 ≤2h；hokiseries 公售至 20:00 CST（约 2.4h）尚未进入结束窗 ≤2h，本窗无官帖（R1815 已作过开窗 ≤2h）；qtronlaptops / pillowbookRH 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。tapeai 11 月 16 日开放 BEM 预存仍无具体钟点。DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗，均未进入 ≤2h。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/ELY 与薄栏 TAPE/GIWA/DOGE 打满 25 条硬顶；KW_MINE 0；MEN_BTC 0。
- mentions：Tape 5（多为已在库生态互动与社区提醒）；GIWA 1；BTC 0；Starknet+DogeEVM 1（已在库 dogstarter 测试网水龙头说明）。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮关键词/mentions 盲捞未独立发现可收录的新官号；UF 分片本窗 0 帖。

## Watch 漏挂修复

- 本轮 0。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1862.md`。面板 https://reboot7454.github.io/early-scout/
- notify=false：0 新收录，无首次 ≤2h / 首次确认免费 LIVE 窗口。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 286 oddoneout_fun 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- DualForge 同一 19:00 CST 开铸窗口已在 R1861 按首次 ≤2h 推送，后续轮次不要重复提醒，除非档期改动、出现新 CA/开闸确认，或进入可操作变化。
- osk-agent 同一 18:00 CST 开池窗口已在 R1859 推送，不要重复提醒，除非档期改动或出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复客服回复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售至 20:00 CST，约 18:00 CST 起进入结束窗 ≤2h，届时再判断是否提醒（R1815 已作过开窗 ≤2h 通知）。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
