# 早期打新雷达 R1858

- 时间：2026-11-15 15:41 CST（Asia/Shanghai）
- 模式：ample（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=false
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 62f60d6 R1857）。

## X 额度与覆盖

- remainingBefore 602 → remaining 577（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=ample，softCap 28，minSpend 20，silentCap 2，ufAccountShard 50。main 24 未超 softCap、已达 minSpend：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换是 Tape/GIWA/BTC/Starknet+DogeEVM，不含 BN Agent pads。
- userFollowWatch 已刷完本分片：从 0-based 29 / 1-based 30 flapdotsh 起，kept 50，真实 NF_skip 10（ElysiumOutlaws / deadpacksol / blindfloor / blobsdotmeme / trytoprint / PlayFarmFi / reynarlabs / world_ygg / rektazhy59942 / 0xvernull），walkScanned 60，无绕回。last kept 0-based 88 / 1-based 89 CrackAFortune，next 0-based 89 / 1-based 90 hanokreserve。
- 优先号 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom 落在本 UF 分片；其余优先号（mobster_meme / NutshellMarkets / starx_xlayer）折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无（窗口号均不在本 UF 分片）。MUST1 覆盖 MicroFrens / DualForgeBSC / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=Starknet（1858%11=10）。search_users 仍不在 X 工具目录，只走 mentions，result_count=0，无新可操作官号，未送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T06:36:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T05:36:00Z（约 2h）。silent start=2026-11-14T07:36:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析（198 帖、142 作者、0 解析错误），未重拉 X（禁止额外/重复 X 查询）。
- 解析：review 65，skipped 68，in_lib 9，mentions_new 59。
- 栏 rc：UF1 0、UF2 0、MUST1 25、MUST2 0、THIN1 0、THIN2 7、THIN3 0、THIN4 0、THIN5 0、KW_LZ 2、KW_TAPE 25、KW_GIWA 20、KW_DOGE 25、KW_BTC 5、KW_SN 4、KW_MINT 25、KW_MINE 1、KW_PAD 25、KW_GO 3、KW_ELY 25、MEN_TAPE 5、MEN_GIWA 0、MEN_BTC 1、MEN_SN_DOGE 0、SILENT_MEN 0。
- 首读 UF1 快照 601 / 1000，末次 SILENT_MEN 快照 577 / 1000。remainingBefore 取上轮结束 602，按 25 次递减记 remaining=577。
- THIN official 因名单变长本轮 5 批（thinNew：0padfun / DyDxfun / dogstarter / TapeLaunch / TapeFractal / giwagmi / umbrapad）；thinSkipDedup：tapeupio / FoundryTape（已在本 UF 分片读过）。

## 新收录

- 无。

## DeepSeek 未收录 / 未送审

- 本轮无送审项（dsFallback=false）。文案 whatsNew 由 deepseek-flash 生成。
- **未送审**：BulwarkScore（R1856/R1857 已 skip 的 LZ 安全打分工具）；ZingYuantx（DogeOS RT）；HoodTheTurtle（仿 @HoodTurtleRH，R1855 已记）；WheelX_fi（既有聚合器，GIWA faucet 宣传）；hey_daisy_01 为已 ended 的 mortal-apes 做 GTD 抽奖；Wildlifeuni_55 / CompanionsWfit / trippiart / MonchiesNFT / numencash 均已在库；muchfi_xyz 官号约 2025-09-05 建立，站点 muchfi.xyz 为 DEX/CLOB 测试网而非极早期打新；ATLOVofficial（今日新建 1 粉，只问 Elysium 前景）；dragondozememe（Cronos 债券曲线 meme）；sentinel_dapper/Fusebox（个人在 X Layer 要测试资金，无开窗）；elysium_gympepe（R1853 已 skip）。其余多为 Tape/GIWA/Elysium 社区回复与 GTD 噪音。

## 在库进度（不重推）

- **osk-agent**（@AIAgent_OSK，status=failed）：官号再确认 2026-11-15 18:00 CST 开池，0.008 BNB，每个 BSC .ai Agent ID 一席（https://x.com/AIAgent_OSK/status/2121869566460485987）。本轮约 15:41 CST，距开池约 2.3h，尚未进入 ≤2h（约 16:00 CST 才到）。免费席已尽，不重推。
- **MicroFrens**：本窗官号约 15:19–15:35 CST 回复 snapshot/钱包口径——若 snapshot 前铸过 3 枚则在 OG FREE WL、每钱包额度 12、mint 结束后空投补发（https://x.com/MicroFrens/status/2121865767197290540）。持有者免费阶段仍未给出确定开窗时刻，对公窗已关，不重推；le2h 保持 false。
- **DualForge**（@DualForgeBSC）：本窗再预热 Tonight / Flint+Quench（https://x.com/DualForgeBSC/status/2121862820929454529）。开铸仍 2026-11-15 19:00 CST，约 3.3h，尚未 ≤2h，不重推。
- **tapeai**：11 月 16 日开放 BEM 预存仍无具体钟点，本窗无新官帖时刻，不按新窗口推送。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST）；hokiseries 公售至 20:00 CST（约 4.3h）；polyrob / qtronlaptops / pillowbookRH 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。infamousScratch/animal-pharm、DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗，均未进入 ≤2h。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/ELY 与薄栏 TAPE/DOGE 打满 25 条硬顶；KW_GIWA 20；KW_MINE 1；MEN_GIWA 0、MEN_SN_DOGE 0、SILENT_MEN 0。
- mentions：Tape result_count 5（多为在库 Tape 社区/定投）；GIWA 0；BTC 1（UnseenOrdo 在库宣传）；Starknet+DogeEVM 0。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮关键词/mentions 盲捞未独立发现可收录的新官号；关注表分片本身也无新帖。

## Watch 漏挂修复

- 本轮 0。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1858.md`。面板 https://reboot7454.github.io/early-scout/
- notify=false：0 新收录，无新的免费 LIVE/免费 mint，无新的 ≤2h 关窗。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 89 hanokreserve 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- osk-agent 若下一轮已进入 ≤2h（约 16:00 CST 起），需按 ≤2h 规则推送（付费 0.008 BNB，只告警不自动打）。
- DualForge 19:00 CST 开铸约在再下一轮前后进入 ≤2h（约 17:00 CST 起），届时再推。
- MicroFrens 持有者免费阶段一旦实际开窗或给出确定时刻，再推，不要每轮重复 soon。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
