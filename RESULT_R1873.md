# 早期打新雷达 R1873

- 时间：2026-11-15 23:12 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（在库 qtronlaptops、pillowbook-rh 开铸，以及 POLYROB 公售关窗，均首次进入 ≤2h）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 802fec4 R1872，已是最新）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 231 → remaining 206（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 231>200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读，thinSkipDedup=THIN3_GIWA 去掉 narupay_com（已在本轮 UF+MUST 覆盖），同一 handle 只拉一次，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 834 / 1-based 835 elysium_machine 起，kept 48，真实 NF_skip 10（SENSEIAgent_、Agentspunks、cryptosympbnb、BN_Big_Bang、LumenGenesisNFT、Estock_、pixelboyzai、Panba_EmojiPack、AmberPoW_BSC、DigitalBombAI，按已知 NF 未重读），walkScanned 58，无绕回。first kept 0-based 834 elysium_machine，last kept 0-based 891 / 1-based 892 elywatch，next 0-based 892 / 1-based 893 ditherglyphs。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2（均不在本 UF 分片）；MUST2 本窗 0 帖。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun / PlayBitsigil / SpoxyGang。
- mustSkip：无。thinSkipDedup：narupay_com。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=GO盘（1873%11=3）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=15，sentToReview=0，admitted=0，skipped=15（too_many_posts 15），deferredHandles=[]。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST/THIN official start_time=2026-11-15T14:00:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T13:00:00Z（约 2h）。silent start=2026-11-14T15:05:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 7、MUST2 0、THIN1_LZ 0、THIN2_TAPE 11、THIN3_GIWA 1、THIN4_BTC 1、THIN5_DOGE_SN 1、KW_LZ 4、KW_TAPE 25、KW_GIWA 14、KW_DOGE 25、KW_BTC 15、KW_SN 8、KW_MINT 25、KW_MINE 6、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_LZ 25、MEN_ELY 25、MEN_MINE 1（另 @squeekchain Resource Unavailable，未重试）、MEN_BN 0、SILENT_MEN 7。parse_errors=[]。
- 首读 UF1 后快照 230 / 1000，故 remainingBefore=231；末次 SILENT_MEN 快照 206 / 1000。
- THIN official 本轮 5 批。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **qtronlaptops**（@qtronlaptops）：首次进入 ≤2h。官帖 23:01 CST https://x.com/qtronlaptops/status/2121981986461896737 称 MINT IN TWO HOURS，开铸仍为 2026-11-16 01:00 CST（约 1.8h），$1 / 4444，OpenSea https://opensea.io/collection/q-tron-laptops ；并称仍在整改/做收尾。按首次 ≤2h 提醒。le2h=true，status=watching（尚未实际开铸）。本号不自动 mint。
- **pillowbook-rh**（@pillowbookRH，$PILLOW / Pons）：首次进入 ≤2h。开窗仍为 2026-11-16 01:00 CST（约 1.8h，17:00 UTC）。MUST1 本 1h 官方窗无该号新帖；官网 https://pillowbook.pro HTTP 200。按时钟首次提醒。le2h=true，status=watching。本号不自动 mint。
- **POLYROB**（@tmachinroBot）：公售关窗首次进入 ≤2h。关闭时间仍为 2026-11-16 01:12 CST（约 1.99h），固定价 0.033 ETH 仍开，铸造页 https://6551.polyrob.dev/ 。MUST1 本窗无该号新帖。此前已按公售开窗通知，本次按关窗首次 ≤2h 提醒。le2h=true，status=live。本号不自动 mint。
- **jacketagent**（@jacketagent）：同一免费窗口仍开，不重推。官网 jacketagent.pages.dev 仍 HTTP 200。BNB Chain status() 核验：phase=1，minted=172，freeSold=172，paidSold=0，freeRemaining=328，paidRemaining=15000。较 R1872 无变化。免费仍 LIVE，付费尚未开始，截止 2026-11-16 00:00 CST。R1871 已按首次 ≤2h 提醒。le2h=true，status=live。本号不自动 mint。
- **Bitsigil**（@PlayBitsigil，id=bitsigil）：官帖 23:00 CST 确认 GTD MINT IS LIVE（$2 ETH，每 GTD 名单钱包 2 枚，OpenSea https://opensea.io/collection/bitsigil/ ），另见 22:34 CST「30 MINUTES TO GTD」。仍是 R1870 已提醒的同一免费 WL / GTD $2 窗口，未见已核验 CA、关窗或 FCFS/公售开始（FCFS 仍 01:00、公售 $3 仍 02:00 CST），不重推。le2h=true，status=live。本号不自动 mint。
- **SpoxyFun**（@SpoxyGang）：MUST1 本窗无该号新帖；付费 mint 仍 0.001 BNB，免费已售罄。已在 R1870 按付费 LIVE 新收录通知，不重推。本号不自动 mint。
- **DualForge**（@DualForgeBSC）/ **osk-agent**（@AIAgent_OSK）/ **MicroFrens** / **hokiseries**：MUST1 本窗无新的可操作变化；此前窗口已通知，不重推。
- **escapehub**（@escape_hub）：KW_PAD 再见官帖称 Launchpad 明天开闸，时钟仍为 2026-11-16 23:00 CST（约 23.8h），尚未 ≤2h。已在 R1684 按定档通知，不重推。本号不自动 mint。
- **dotbots-ai / dotbots**（@dotBots_ai）：UF1 官帖 22:10 CST 称 Bot Battle（testnet）将于 Nov 16 11:00 GMT+7（12:00 CST）开放，free bot for everyone，无需 NFT。是测试网对战预热，不是主网免费 mint 窗口，不按开铸通知。本号不自动 mint。
- **shielded-wizards**（@ShieldedWizBTC）：THIN4 再见 raid update 今日 18:00 UTC（2026-11-16 02:00 CST，约 2.8h），前 5 队得 WL，不是公开免费 mint，尚未 ≤2h，不按新开铸通知。本号不自动 mint。

## 新收录

- 本轮 0 张新卡。DeepSeek 未做批量打分（无送审新卡）。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_GIWA 14；KW_BTC 15；KW_SN 8；KW_LZ 4；KW_MINE 6。mentions：LayerZero 25、Elysium+kinetiq 25、mining-squeek+Nutshell 1（@squeekchain 查询 Resource Unavailable，未重试）、BN Agent pads+STARX 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮盲捞未见达到收录门槛的独立新号。
- 未另建卡 / 不收录：**@ArenaLaunchPVP**（已在 Base 上线的 omnichain pad，约 12 天、110 粉 446 帖，早期度不足，未送 DS）；**@Motherlode_live** 已记入 motherlode-fun，不另建卡；**@styxscan** 为代币安全扫描工具，不是打新/发射项目。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂。
- 本轮无新卡进 Watch。
- soft-debt lastChecked：canton / glaze / tokenWorks 相关 Watch 仅刷新时间，无新 Canton/Glaze/TW 收录。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1873.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：qtronlaptops、pillowbook-rh 开铸与 POLYROB 公售关窗均首次进入 ≤2h。Jacket Agent 同一免费窗口仍开（链上 172/500）已在 R1871 提醒，Bitsigil GTD 已按点开闸仍属 R1870 已通知窗口，均不重推。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=7，无新静号进入审核。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 892 ditherglyphs 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。silent 下一轮 LayerZero（1874%11=4）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 同一免费 WL / GTD $2 窗口（含已按点开闸的 GTD LIVE）已在 R1870 提醒，不要每轮重推；后续除非关窗、改规则、公布已核验 CA、FCFS/公售开始或 mint 入口变化，否则不要只因同一窗口仍开再推。FCFS $2 01:00 CST、公售 $3 02:00 CST 进入后再判断是否首次推送。
- DualForge 官方开闸已在 R1868 推送，后续不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟已过且无新阶段官宣，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 开铸窗口已在 R1873 按首次 ≤2h 提醒；后续除非关窗、开铸确认、改价、改入口或规则变化，否则不要只因同一窗口仍未开再推。
- POLYROB 公售关窗 2026-11-16 01:12 CST 已在 R1873 按首次 ≤2h 提醒；后续除非关窗、改价或入口变化，否则不要只因同一公售仍开再推。
- jacketagent 已在 R1871 按首次 ≤2h 提醒；免费至 11-16 00:00 CST。后续除非关窗、名额售罄、付费阶段开始或规则变化，否则不要只因仍在同一免费窗口再推。
- PlunderPort 不得仅凭官宣「Mint: FREE / 供应 3333」写成已核验免费 LIVE；需官网可达或可核验 mint 入口后再判断。
- SpoxyFun 免费已售罄，不要写成免费 LIVE；付费 0.001 BNB 已开铸。与 @spoxydev / Cyber Spirits 同域，不要合并覆盖旧卡。
- Motherlode 不要把 @Motherlode_live 再建一张卡；官网与 Devnet/waitlist 已记入 motherlode-fun，非主网免费 mint，不要按新收录或免费 LIVE 重推。
- Anchain 已收录；站点未见回链 X，不得写成已互链核验官网站。
- Zeroportal 已收录为 announced，不得写成已开闸、免费 LIVE 或 LayerZero 项目；站点未见回链 X，不得写成已互链核验。Zero 链 ≠ LayerZero。
- escapehub Launchpad 时钟仍为 2026-11-16 23:00 CST，尚未 ≤2h，已在 R1684 按定档通知，不要提前重推。
- remaining 206，约仍有 16 轮至 08:00 CST；后续若 remaining 逼近 200 再收紧，额度够时不得砍栏。
