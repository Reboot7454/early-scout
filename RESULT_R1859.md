# 早期打新雷达 R1859

- 时间：2026-11-15 16:05 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（osk-agent 首次进入 ≤2h；付费 0.008 BNB，只告警不自动打）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ ffcfee9 R1858）。

## X 额度与覆盖

- remainingBefore 577 → remaining 553（日硬顶 1000，重置约 08:00 CST）。xReads 24（main 23 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 23 超 softCap 18（+5），已达 minSpend 18：UF×2 + MUST×2 + THIN×4 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 24。因 remaining 577≫200，按用户「额度够时不得砍栏」补齐核心栏 KW×5 与 mentions 轮换 4 组，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖，且本轮 mentions 轮换含 BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 89 / 1-based 90 hanokreserve 起，kept 48，真实 NF_skip 5（pearsdotfamily / battle_pad / cabaldotfun / project_hoodmon / elysiumpepecoin），walkScanned 53，无绕回。last kept 0-based 141 / 1-based 142 beepboopmeme，next 0-based 142 / 1-based 143 slymzcrew。
- 优先号 NutshellMarkets 落在本 UF 分片；其余优先号（mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / starx_xlayer）折入 MUST2，本窗 0 帖、非 NF。
- mustSkip：无。MUST1 覆盖 MicroFrens / DualForgeBSC / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=打新（1859%11=0）。search_users 仍不在 X 工具目录，只走 mentions，result_count=25，多为 WFit/Companion 免费 GTD 任务噪音，无新可操作官号，未送审。silentCap=2 用 1。
- UF/MUST/THIN official start_time=2026-11-15T07:01:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T06:01:00Z（约 2h）。silent start=2026-11-14T08:01:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析（244 帖、179 作者、0 解析错误），未重拉 X（禁止额外/重复 X 查询）。
- 解析：review 98，skipped 70，in_lib 11，mentions_new 48。
- 栏 rc：UF1 0、UF2 0、MUST1 25、MUST2 0、THIN1 0、THIN2 0、THIN3 1、THIN4 0、KW_LZ 2、KW_TAPE 25、KW_GIWA 18、KW_DOGE 25、KW_BTC 4、KW_SN 3、KW_MINT 25、KW_MINE 1、KW_PAD 25、KW_GO 2、KW_ELY 25、MEN_LZ 13、MEN_ELY 25、MEN_MINE 0、MEN_BN 0、SILENT_MEN 25。
- 首读 UF1 快照 576 / 1000，末次 SILENT_MEN 快照 553 / 1000。remainingBefore 取上轮结束 577，按 24 次递减记 remaining=553。
- THIN official 本轮 4 批。thinNew：tapeupio / FoundryTape（上轮在 UF 分片，本轮回到薄栏官号）。thinSkipDedup：Tapemonkeworld / hanokreserve / PunkOnGiwa。

## 新收录

- 无。

## DeepSeek 未收录 / 未送审

- 本轮无送审项（dsFallback=false）。文案 alertMessage / whatsNew / metaWhatsNew 由 deepseek-flash 生成。
- **未送审**：GROUNDEDbyfaa（1 日新号，自称 $GROUNDED fan meme 已 live 且 mint revoked，不是可打的新铸窗）；CharityBoxCBOX（已上线 30 天的慈善代币，仍在 bonding-curve）；BulwarkScore、ZingYuantx 前轮已 skip；WFit / Labyrinth Companion 免费 GTD 任务跟帖；oripaxyz 仅第三方提及 Hyperliquid 卡包 11-25 开，本轮未另开核验读；HoodTheTurtle 前轮已记；numencash / muchfi_xyz 已在库或已跳过。其余多为 Tape/GIWA/Elysium 社区回复与 GTD 噪音。

## 在库进度

- **osk-agent**（@AIAgent_OSK，status=failed）：官号再确认 2026-11-15 18:00 CST 开池，0.008 BNB，每个 BSC .ai Agent ID 一席（https://x.com/AIAgent_OSK/status/2121869566460485987）。本轮约 16:05 CST，距开池约 1.9h，**首次进入 ≤2h，本轮推送**。免费席已尽，付费只告警不自动打。
- **MicroFrens**：本窗官号继续处理钱包额度——约 15:37 CST 称 added more spots it should let you mint more（https://x.com/MicroFrens/status/2121870166032330817），约 15:56 CST 问 were you able to snag the 12？（https://x.com/MicroFrens/status/2121875061741351223）。仍未官宣持有者 OG FREE 阶段已开窗，也未给出确定开窗时刻，对公窗已关，不重推；le2h 保持 false。
- **DualForge**（@DualForgeBSC）：本窗再讲 Flint+Quench 双钥匙（https://x.com/DualForgeBSC/status/2121868318735032592）。开铸仍 2026-11-15 19:00 CST，约 2.9h，尚未 ≤2h，不重推。
- **Animal Pharm**（@infamousScratch）：官号约 15:40 CST 确认 Minted out! Now to zero!（https://x.com/infamousScratch/status/2121870818405761431）。已售罄，不是新开窗，不重推。
- **jpeg-monkes**：官号 16:00 CST 发帖称免费阶段 30 分钟后结束、每钱包上限提到 2（https://x.com/jpegmonkes/status/2121875854502551848），链接指向既有 OpenSea 合集 jpegmonkes（约 3277 供 / 2340 持有者）。库内此前已记免费窗结束，不按新的早期窗口重推。
- jacketagent 免费仍 LIVE（至 11-16 00:00 CST）；hokiseries 公售至 20:00 CST（约 4h）尚未 ≤2h；polyrob / qtronlaptops / pillowbookRH 窗口仍在 11-16 01:00 前后；hood-turtle mint 仍是 11-17 22:15 CST。tapeai 11 月 16 日开放 BEM 预存仍无具体钟点。DeadHood_nft、Gloopix_、matrix-agents、dydxfun、BackBidFun 本窗无新开窗，均未进入 ≤2h。

## 关键词 / mentions 摘记

- 十栏均跑全。核心栏 KW_MINT/PAD/ELY 与薄栏 TAPE/DOGE 打满 25 条硬顶；KW_GIWA 18；KW_MINE 1；MEN_MINE 0、MEN_BN 0。
- mentions：LayerZero result_count 13（多为 PlunderPort / Zero 生态互动）；Elysium+kinetiq 25（已在库 sasa-pad / elyscreener 等互动）；mining-squeek+Nutshell 0；BN Agent pads+STARX 0。各链同等轮换，本轮未空转只扫单链。
- 发现不等于关注：本轮关键词/mentions 盲捞未独立发现可收录的新官号；关注表分片本身也无新帖。

## Watch 漏挂修复

- 本轮 0。在库且 round≥1790 的卡均已在至少一个 Watch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1859.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：0 新收录，但 osk-agent 首次进入 ≤2h（付费 0.008 BNB，免费席已尽）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 142 slymzcrew 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- DualForge 19:00 CST 开铸若下一轮已进入 ≤2h（约 17:00 CST 起），届时再推。
- hokiseries 公售至 20:00 CST，约 18:00 CST 起进入结束窗 ≤2h，届时再判断是否提醒（R1815 已作过开窗 ≤2h 通知）。
- MicroFrens 持有者免费阶段一旦实际开窗或给出确定时刻，再推，不要每轮重复额度/客服回复。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
- osk-agent 本轮已按 ≤2h 推送，后续轮次不要在同一 18:00 CST 开池窗口上重复提醒，除非档期改动或出现新的可操作变化。
