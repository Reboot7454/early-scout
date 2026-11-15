# 早期打新雷达 R1857

- 时间：2026-11-15 15:05 CST（Asia/Shanghai）
- 模式：ample（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true
- 新收录：matrix-agents、dydxfun
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 202827c R1856）。

## X 额度与覆盖

- remainingBefore 626 → remaining 602（日硬顶 1000，重置约 08:00 CST）。xReads 24（main 23 + silent 1），admitVerify 0。
- mode=ample，softCap 28，minSpend 20，silentCap 2，ufAccountShard 50。main 23 未超 softCap、已达 minSpend：UF×2 + MUST×2 + THIN×4 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 24。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST、以及本轮 mentions（BN Agent pads+STARX）覆盖。
- userFollowWatch 已刷完本分片：从 0-based 1792 / 1-based 1793 SnipeTech_ 走到表尾（1820）后回绕，kept 50，真实 NF_skip 7（safureload / Seethebsc / Charzardxpox / LuckyAgent_bsc / Agentrocksclub / sunrigfun / kaAgents），walkScanned 57。last kept 0-based 28 / 1-based 29 elysianfieldnft，next 0-based 29 / 1-based 30 flapdotsh。
- 优先号 mobster_meme 落在本 UF 分片；其余优先号（machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）折入 MUST2，本窗 0 帖、非 NF。
- mustSkip（已在 UF 分片读过，不是 username-not-found）：HoodTurtleRH / Gloopix_ / infamousScratch。qtronlaptops / pillowbookRH 不在本分片，已进 MUST1。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=BTC（1857%11=9）。search_users 仍不在 X 工具目录，只走 mentions，result_count=10，无新可操作官号，未送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T05:58:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T04:58:00Z（约 2h）。silent start=2026-11-14T06:58:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析（264 帖、171 作者、0 解析错误），未重拉 X（禁止额外/重复 X 查询）。
- 解析：review 88，skipped 68，in_lib 15，mentions_new 52。
- 栏 rc：UF1 19、UF2 1、MUST1 7、MUST2 0、THIN1 0、THIN2 23、THIN3 0、THIN4 1、KW_LZ 1、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 7、KW_SN 3、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 3、KW_ELY 25、MEN_LZ 14、MEN_ELY 25、MEN_MINE 0、MEN_BN 0、SILENT_MEN 10。
- 首读 UF1 快照 625 / 1000，末次 SILENT_MEN 快照 602 / 1000。remainingBefore 取上轮结束 626，按 24 次递减记 remaining=602。

## 新收录

1. **Matrix Agents**（`matrix-agents`，打新 / BNB Chain / BN Agent，status=live，focus=false）
   - 官网 https://matrixagents.pages.dev/ HTTP 200。合约 `0x1F669b714337F3C2585072c53fdDD89581F928fF` 已核验（name=Matrix Agents，symbol=MATRIX，Sourcify exact match），owner `0xbc8f04b7fd68bbe4c2c298a63d20da0962879ced`。
   - 链上 15:04 CST 左右：mintOpen=true，mintedCount=280，freeMinted=280，freeRemaining=720，FREE_MAX=1000，PAID_PRICE=0.001 BNB，MAX_PAID_PER_AGENT=10，MAX_SUPPLY=5000。每个 Binance Agent ID 可免费用 1 份（只付 gas），付费最多 10 份。
   - MintRadar first seen 2026-11-15 03:50 UTC（约 11:50 CST），标签 owner controls。
   - 由第三方新号 @Omthapa749（2 天、2 粉）14:58 CST 晒单发现（https://x.com/Omthapa749/status/2121860335682605336），不是官号。官网全程无 X/TG/DC。库内 usexmatrix/@usexMatrix（xMatrix 协作空间）不是同一项目。
   - DeepSeek overall 52，因「无官推不 admit」建议不收录。操作员按「官网+已核验合约+免费 LIVE」例外收录（比照 computeroll 早期无推特官网例外），以满足「免费 LIVE 必须立刻提醒、尽量不漏可操作机会」。未编造官推，故无 `links.x`——面板 hasTwitter 可能隐藏该卡和本轮芯片，以本聊天提醒为准。已进 freeMintWatch / bnAgentWatch / agentPadWatch 的 candidateIds（无 accounts 可写）。本号不自动 mint。

2. **DyDx.fun**（`dydxfun`，@DyDxfun，LayerZero / Zero，status=announced，focus=false）
   - 官号 2026-11-14 18:04 CST 建立（xUserId 2121544488321798145），未认证，10 粉、1 帖。官网 https://dydx.fun/ HTTP 200，site.js `X_HANDLE='DyDxfun'`，资料栏回链官网，互链成立。
   - 官帖 13:48 CST https://x.com/DyDxfun/status/2121842793350082707：Coming soon on @LayerZero_Core。尚未开放创建/交易。名称极易与老牌交易所 dYdX 混淆，未见隶属或切割声明。
   - DeepSeek overall 64，admit=true。已进 userFollowWatch + layerZeroWatch + zeroWatch。非免费 mint，非 ≤2h。本号不自动 mint。

## DeepSeek 未收录 / 未送审

- DS 对 matrix-agents 因无官推判 skip（已由操作员例外收录，见上）。
- **未送审**：oinkersxrp / @First_Ledger（XRPL 测试集合，帖文写明 test collection，约 1h 开铸但是测试垫，First_Ledger 本窗无官帖、未另开 X 读）；BulwarkScore（R1856 已 skip 的 LZ 安全打分工具）；Pitbiapp（文档/MCP 工具，非 mint）；ZingYuantx（DogeOS RT）；HoodedLegends / PlunderPort / HyperHaulio / beepzfun / TSBdotfun / Dividendsarts（GTD 抽奖/RT 噪音，与 R1855/R1856 同类）；@entertheanime（库内已有 upcoming，11-20 免费 mint，非 ≤2h）；bakeruip（Not Human Club 申请）。静号 BTC mentions 噪音未送审。

## 在库进度（不重推）

- **osk-agent**（@AIAgent_OSK，status=failed）：官号再确认 2026-11-15 18:00 CST 开池，0.008 BNB，每个 BSC .ai Agent ID 一席（https://x.com/AIAgent_OSK/status/2121854592094711833）。本轮约 15:05 CST，距开池约 3h，尚未进入 ≤2h（约 16:00 CST 才到）。免费席已尽，不重推。
- **MicroFrens**：本窗官号无新帖。对公窗已关，持有者免费阶段仍 soon（开启后约 12–16 小时），不重推；le2h 保持 false。
- **tapeai**：官号再述 11 月 16 日开放 BEM 预存（https://x.com/TapeAIAgent/status/2121849787498823934），仍无具体钟点，不按新窗口推送。
- **BackBidFun**：已在库 live（R1853 已通知），本窗有 LP 100% locked 进展，非新窗口，不重推。
- infamousScratch/animal-pharm live（社区赠品，无官宣售罄）；ElysiaSealed watching；useXFee / usegnomon / DeadHood_nft 无新开窗。jacketagent / hokiseries / DualForgeBSC / qtronlaptops / pillowbookRH / polyrob 窗口仍在更晚时段，均未进入 ≤2h。hood-turtle mint 仍是 11-17 22:15 CST。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/ELY 与薄栏 TAPE/GIWA/DOGE 打满 25 条硬顶；KW_MINE 0、MEN_MINE 0、MEN_BN 0。
- mentions：LayerZero result_count 14（含新官号 @DyDxfun）；Elysium+kinetiq 25（多为在库/社区噪音）；mining-squeek+Nutshell 0；BN Agent pads+STARX 0。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：Matrix Agents 由关键词盲捞（第三方晒单）独立发现；DyDx.fun 由 LayerZero 官号 mentions 盲捞发现，不是从关注表里长出来的。

## Watch 漏挂修复

- 本轮 0。在库且 round≥1790 的卡均已在至少一个 Watch。新卡 dydxfun 已进 userFollowWatch + layerZeroWatch + zeroWatch；matrix-agents 无官推，已进 freeMintWatch / bnAgentWatch / agentPadWatch 的 candidateIds。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1857.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 DyDx.fun；以及 Matrix Agents 免费 LIVE（即便 overall 52、无官推，按 SIEGE 课必须立刻提醒）。无新的 ≤2h 关窗。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 29 flapdotsh 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- osk-agent 若下一轮已进入 ≤2h（约 16:00 CST 起），需按 ≤2h 规则推送（付费 0.008 BNB，只告警不自动打）。
- MicroFrens 持有者免费阶段一旦实际开窗或给出确定时刻，再推，不要每轮重复 soon。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
