# 早期打新雷达 R1860

- 时间：2026-11-15 16:33 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（MicroFrens 持有者 OG FREE 阶段首次确认进行中；每钱包 12 份，对公 FCFS 已结束）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 2704705 R1859）。

## X 额度与覆盖

- remainingBefore 553 → remaining 529（日硬顶 1000，重置约 08:00 CST）。xReads 24（main 23 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 23 超 softCap 18（+5），已达 minSpend 18：UF×2 + MUST×2 + THIN×4 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 24。因 remaining 553≫200，按用户「额度够时不得砍栏」补齐核心栏 KW×5 与 mentions 轮换 4 组，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 142 / 1-based 143 slymzcrew 起，kept 48，真实 NF_skip 0，walkScanned 48，无绕回。last kept 0-based 189 / 1-based 190 HashOre_BNB，next 0-based 190 / 1-based 191 Elysdex。
- 优先号 starx_xlayer 落在本 UF 分片（本窗 0 帖、非 NF；未沿用 R1824 过期 NF 标记，因 R1858/R1859 MUST2 已确认非 NF）。其余优先号（mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 MicroFrens / DualForgeBSC / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。MUST1 打满 25 条硬顶（多为 MicroFrens + OSK），未翻页。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=挖矿（1860%11=1）。search_users 仍不在 X 工具目录，只走 mentions，result_count=1（KLV Gold Miner on Klever），无本雷达可操作新官号，未送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T07:26:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T06:26:00Z（约 2h）。silent start=2026-11-14T08:26:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 0、UF2 1、MUST1 25、MUST2 0、THIN1 1、THIN2 0、THIN3 0、THIN4 5、KW_LZ 1、KW_TAPE 25、KW_GIWA 18、KW_DOGE 25、KW_BTC 1、KW_SN 3、KW_MINT 25、KW_MINE 6、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 25、MEN_GIWA 18、MEN_BTC 0、MEN_SN_DOGE 13、SILENT_MEN 1。
- 首读 UF1 快照 552 / 1000，末次 SILENT_MEN 快照 529 / 1000。remainingBefore 取上轮结束 553，按 24 次递减记 remaining=529。
- THIN official 本轮 4 批。thinSkipDedup：Giwatron / mimdotcash（本轮在 UF 分片）。

## 新收录

- 无。

## DeepSeek 未收录 / 未送审

- 本轮无送审项（dsFallback=false）。文案 alertMessage / whatsNew / 卡片 whatsNew 由 deepseek-flash 生成。
- **未送审**：Frenzz_1515 / PlayPixelora / HyperHaulio / CompanionsWfit 已在库，不重推；HoodNFTz2 / mortalApes / Violetblocks 等 Robinhood 免费 GTD/跟帖赠票噪音；numencash 已在库；KLV Gold Miner 在 Klever，不在本雷达链范围；dogstarter 测试网首只 $SPARKY 已在库；Jumak_app 仅为 GIWA 风格帖，无新铸窗；SolVillageFun 为游戏平衡回复。其余多为 Tape/GIWA/Elysium 社区回复与 GTD 噪音。

## 在库进度

- **MicroFrens**：对公 FCFS 已结束（官号 16:12 CST 回复 FCFS already ended fren!，https://x.com/MicroFrens/status/2121878997705666972）。官号 16:15:29 CST 发公开帖，称 OG Holders FREE Mint 正按不同钱包累计前序各阶段铸造，不足 12 份可报钱包与已铸数量申请提额，仅限 OG Holders FREE MINT（https://x.com/MicroFrens/status/2121879750763479113）；同期继续处理每钱包 12 份。R1859 仍视为尚未官宣开窗，**本轮首次确认持有者免费阶段已在进行，本轮推送**。本号不自动 mint。
- **osk-agent**（@AIAgent_OSK，status=failed）：官号 16:05 CST 再确认 2026-11-15 18:00 CST 开池，0.008 BNB，每个 BSC .ai Agent ID 一席（https://x.com/AIAgent_OSK/status/2121877121635434859）。本轮约 16:33 CST，距开池约 1.5h，仍 ≤2h，但同一窗口已在 R1859 首次推送，**不重推**。免费席已尽，付费只告警不自动打。
- **DualForge**（@DualForgeBSC）：开铸仍 2026-11-15 19:00 CST，约 2.5h，尚未 ≤2h，不重推。MUST1 打满 25 条硬顶（多为 MicroFrens/OSK），未翻页，本 1h 窗未见新档期。
- **Animal Pharm**（@infamousScratch）：上轮已记 Minted out，本窗无新开窗，不重推。
- **pillowbookRH**：16:00 CST 发 Day 2 投票帖，发射仍 11-16 01:00 CST，未 ≤2h，不重推。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST）；hokiseries 公售至 20:00 CST（约 3.5h）尚未进入结束窗 ≤2h；polyrob / qtronlaptops 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。tapeai 11 月 16 日开放 BEM 预存仍无具体钟点。DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗，均未进入 ≤2h。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/GO/ELY 与薄栏 TAPE/DOGE 打满 25 条硬顶；KW_GIWA 18；KW_MINE 6；MEN_BTC 0。
- mentions：Tape 25（BEM/TapeOut 社区互动，11-16 BEM 预存已在库）；GIWA 18（Ammora 季节结束与 numencash 预热，已在库）；BTC 0；Starknet+DogeEVM 13（LootRealms/Devcon 与 dogstarter 测试网，已在库）。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮关键词/mentions 盲捞未独立发现可收录的新官号；UF 分片仅 SolVillageFun 1 条游戏回复。

## Watch 漏挂修复

- 本轮 0。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1860.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：0 新收录，但 MicroFrens 持有者 OG FREE 阶段首次确认进行中（每钱包 12 份，对公 FCFS 已结束）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 190 Elysdex 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- DualForge 19:00 CST 开铸若下一轮已进入 ≤2h（约 17:00 CST 起），届时再推。
- hokiseries 公售至 20:00 CST，约 18:00 CST 起进入结束窗 ≤2h，届时再判断是否提醒（R1815 已作过开窗 ≤2h 通知）。
- osk-agent 同一 18:00 CST 开池窗口已在 R1859 推送，后续轮次不要重复提醒，除非档期改动或出现新的可操作变化。
- MicroFrens 持有者免费阶段本轮已按首次确认进行中推送，后续不要每轮重复额度/客服回复，除非出现关窗、新阶段或份额规则变化。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
