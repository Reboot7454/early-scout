# 早期打新雷达 R1874

- 时间：2026-11-15 23:36 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（在库 Bitsigil 官帖改规则：Firstbound 现已免费铸造、仅付 gas，已付费者退款）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 9ea3c52 R1873，已是最新）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 206 → remaining 181（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remainingBefore 206≥200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读。thinSkipDedup：THIN1_LZ 去掉 ozero_fun（已在 MUST1）；THIN3_GIWA 去掉 JoseonFun、MulleProtocol（已在本轮 UF）；THIN5_DOGE_SN 去掉 DogeOSExchange（已在 UF）。同一 handle 只拉一次，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 892 / 1-based 893 ditherglyphs 起（该号为已知 NF，未重读），kept 48，真实 NF_skip 6（ditherglyphs、exec_terminal、orivatbnb、spiderproject69、useampad、bianjiayou，按已知 NF 未重读），walkScanned 54，无绕回。first kept 0-based 893 mirroragent，last kept 0-based 945 / 1-based 946 DABAIAgent，next 0-based 946 / 1-based 947 BNBRunnerz。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2；MUST2 本窗 0 帖。MUST1 覆盖既有 live/≤2h 号（含 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / jacketagent / hokiseries / ozero_fun / PlayBitsigil / SpoxyGang 等）。
- mustSkip：无。thinSkipDedup 见上。注意：勿把 stale meta.nfSkipR1103 里误标为 NF 的 live 优先号（starx_xlayer、mobster_meme、machinedotfun、PulseLaunchpad）以及 TapeFractal 再当 NF 跳过。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=LayerZero（1874%11=4）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=54，sentToReview=0，admitted=0，skipped=54（too_many_posts 38，already_in_library 15，profile_unresolved 1），deferredHandles=["p2eabs"]。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST/THIN official start_time=2026-11-15T14:30:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T13:30:00Z（约 2h）。silent start=2026-11-14T15:30:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 15、MUST2 0、THIN1_LZ 0、THIN2_TAPE 8、THIN3_GIWA 1、THIN4_BTC 0、THIN5_DOGE_SN 2、KW_LZ 4、KW_TAPE 25、KW_GIWA 9、KW_DOGE 25、KW_BTC 15、KW_SN 8、KW_MINT 25、KW_MINE 7、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 4、MEN_GIWA 1、MEN_BTC 0、MEN_SN_DOGE 0、SILENT_MEN 20。parse_x.py 仍按旧名找 MEN_LZ/ELY/MINE/BN，属脚本残留，真实 mentions 文件已按本轮轮换名解析，未重拉 X。
- 首读 UF1 后快照 205 / 1000，故 remainingBefore=206；末次 SILENT_MEN 快照 181 / 1000。
- THIN official 本轮 5 批。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **Bitsigil**（@PlayBitsigil，id=bitsigil，Firstbound / Robinhood Chain）：官帖 23:16 CST https://x.com/playbitsigil/status/2121985651134378251 宣布 FIRSTBOUND IS NOW FREE TO MINT，仅付 gas，已付费铸造者将获退款。Mint page 帖 https://x.com/playbitsigil/status/2121985826762694670 的 t.co 仍解析为 OpenSea https://opensea.io/collection/bitsigil/overview 。官网 bitsigil.xyz HTTP 200，未见已核验 CA。此为改规则（R1870–R1873 所跟的付费 GTD $2 → 免费/仅 gas + 退款），必须通知。官帖未明确取消 FCFS $2（11-16 01:00 CST）或公售 $3（11-16 02:00 CST），不得写成这两档也已免费。le2h=true，status=live，focus=false。本号不自动 mint。
- **jacketagent**（@jacketagent）：同一免费窗口仍开，不重推。官网 jacketagent.pages.dev 仍 HTTP 200。BNB Chain status() 核验：phase=1，minted=172，freeSold=172，paidSold=0，freeRemaining=328，paidRemaining=15000。与 R1873 相同。免费仍 LIVE，付费尚未开始，截止 2026-11-16 00:00:34 CST（约 0.4h）。R1871 已按首次 ≤2h 提醒。le2h=true，status=live。本号不自动 mint。
- **qtronlaptops**（@qtronlaptops）：同一开铸仍为 2026-11-16 01:00 CST（约 1.4h），$1 / 4444，OpenSea https://opensea.io/collection/q-tron-laptops 。官帖仍是 R1873 已用的 23:01 CST https://x.com/qtronlaptops/status/2121981986461896737「MINT IN TWO HOURS」，不是新窗口。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=true，status=watching。本号不自动 mint。
- **pillowbook-rh**（@pillowbookRH，$PILLOW / Pons）：同一开窗仍为 2026-11-16 01:00 CST（约 1.4h，17:00 UTC）。MUST1 本窗无该号新帖。官网 pillowbook.pro 首次探测短暂失败后重试 HTTP 200，视为瞬时，不按站点故障。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=true，status=watching。本号不自动 mint。
- **POLYROB**（@tmachinroBot）：关闭时间仍为 2026-11-16 01:12 CST（约 1.6h），固定价 0.033 ETH 仍开，铸造页 https://6551.polyrob.dev/ HTTP 200。MUST1 本窗无该号新帖。已在 R1873 按关窗首次 ≤2h 提醒，不重推。le2h=true，status=live。本号不自动 mint。
- **DualForge**（@DualForgeBSC，id=dualforge-bsc）：官帖 23:09 CST 复盘今晚已开铸、前几小时约 47 枚，属同一已开闸窗口进度，不是新的可操作事件。官方开闸已在 R1868 提醒，不重推。本号不自动 mint。
- **SpoxyFun**（@SpoxyGang）：MUST1 再见官帖称自建市场即将上线；付费 mint 仍 0.001 BNB，免费已售罄。已在 R1870 按付费 LIVE 新收录通知，不重推。本号不自动 mint。
- **osk-agent**（@AIAgent_OSK）/ **MicroFrens** / **hokiseries**：MUST1 本窗无新的可操作变化；此前窗口已通知，不重推。

## 新收录

- 本轮 0 张新卡。DeepSeek 未做批量打分（无送审新卡）。短 alert / whatsNew 由 DeepSeek-flash 撰写（思考开启）；首包 JSON 在 whatsNew 处截断，完整 alert 字段可用，其余短字段按同一草稿与已核验事实补全。dsFallback=false。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_GIWA 9；KW_BTC 15；KW_SN 8；KW_LZ 4；KW_MINE 7。mentions：Tape 4、GIWA 1、BTC 0、Starknet+DogeEVM 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮盲捞未见达到收录门槛的独立新号。
- 未另建卡 / 不收录：@Motherlode_live 已记入 motherlode-fun，不另建卡；@EscapeyESC 为非官方 EscapeHub 吉祥物号；@aynonline / @Candy__Rus 为个人喊单；@BulwarkScore 为代币安全扫描工具（类 styxscan），不是打新/发射项目；@brewpadlat / @hyperhaulio / @companionswfit 已在库。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂。
- 本轮无新卡进 Watch。
- soft-debt lastChecked：canton / glaze / tokenWorks 相关 Watch 仅刷新时间，无新 Canton/Glaze/TW 收录。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1874.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：Bitsigil 改规则（付费 GTD → 免费/仅 gas + 退款）。Jacket Agent 同一免费窗口仍开（链上 172/500）已在 R1871 提醒；qtronlaptops / pillowbook-rh 开铸与 POLYROB 公售关窗已在 R1873 按首次 ≤2h 提醒；DualForge 开闸已在 R1868 提醒，均不重推。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=20，无新静号进入审核。deferredHandles=["p2eabs"]。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 946 BNBRunnerz 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。silent 下一轮 Elysium（1875%11=5）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 本次已按「改规则：现已免费/仅 gas + 退款」通知。后续除非再改规则、关窗、公布已核验 CA、入口变化，或 FCFS $2（11-16 01:00 CST）/ 公售 $3（11-16 02:00 CST）实际开始（且官方未取消），否则不要只因同一免费窗口仍开再推。不要把未宣布取消的 FCFS/公售写成也已免费。
- DualForge 官方开闸已在 R1868 推送；本轮 23:09 CST「约 47 枚」只是同一窗口进度，不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟已过且无新阶段官宣，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 开铸窗口已在 R1873 按首次 ≤2h 提醒；后续除非关窗、开铸确认、改价、改入口或规则变化，否则不要只因同一窗口仍未开再推。
- POLYROB 公售关窗 2026-11-16 01:12 CST 已在 R1873 按首次 ≤2h 提醒；后续除非关窗、改价或入口变化，否则不要只因同一公售仍开再推。
- jacketagent 已在 R1871 按首次 ≤2h 提醒；免费至 11-16 00:00:34 CST。后续除非关窗、名额售罄、付费阶段开始或规则变化，否则不要只因仍在同一免费窗口再推。
- PlunderPort 不得仅凭官宣「Mint: FREE / 供应 3333」写成已核验免费 LIVE；需官网可达或可核验 mint 入口后再判断。
- SpoxyFun 免费已售罄，不要写成免费 LIVE；付费 0.001 BNB 已开铸，自建市场「即将上线」不是新的开铸事件。与 @spoxydev / Cyber Spirits 同域，不要合并覆盖旧卡。
- Motherlode 不要把 @Motherlode_live 再建一张卡；官网与 Devnet/waitlist 已记入 motherlode-fun，非主网免费 mint，不要按新收录或免费 LIVE 重推。
- Anchain 已收录；站点未见回链 X，不得写成已互链核验官网站。
- Zeroportal 已收录为 announced，不得写成已开闸、免费 LIVE 或 LayerZero 项目；站点未见回链 X，不得写成已互链核验。Zero 链 ≠ LayerZero。
- escapehub Launchpad 时钟仍为 2026-11-16 23:00 CST，尚未 ≤2h，已在 R1684 按定档通知，不要提前重推。
- remaining 181，已低于 200，后续轮按紧额度口径：保 UF soft → 必盯 Watch 增量/≤2h → 关键词去重合并；mentions 继续按链轮换子集。但在 remaining 仍允许时尽量保留十栏独立薄栏 KW，remaining <50 再考虑进一步合并。勿把 stale nfSkipR1103 误标号再当 NF 跳过。
