# 早期打新雷达 R1876

- 时间：2026-11-16 00:40 CST（Asia/Shanghai）
- 模式：tight（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（在库 Bitsigil：Free Mint 档持有者可再免费铸造剩余 2 个 Firstbound，仅 gas）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 1278ac1 R1875，已是最新）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 169 → remaining 158（日硬顶 1000，重置约 08:00 CST）。xReads 11（main 10 + silent 1），admitVerify 0。
- mode=tight，softCap 10，minSpend 10，silentCap 1，ufAccountShard hint 40、实际 25。main 10 已达 softCap / minSpend：UF×1 + MUST×1 + 薄栏 KW×6 + mentionsThin×2；另 silent×1 = 11。因 remainingBefore 169<200，按紧额度口径未补核心栏 KW、未跑 THIN official、mentions 只跑轮换前 2 组。同一 handle 只拉一次，未与厚表合并，未另开探索读。
- 薄栏六条独立关键词均跑到（LZ/Tape/GIWA/DogeEVM/BTC/Starknet）。核心栏 打新/挖矿/台子/GO/Elysium 关键词本轮延后（tight alloc kwCore=0）。BN Agent 钱包本轮靠 MUST 优先号覆盖，核心 PAD KW 未跑。mentions 本轮 mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 972 / 1-based 973 VelixoMarket 起，kept 25，真实 NF_skip 2（topaaafun、ripstackfun，按已知 NF 未重读），walkScanned 27，无绕回。first kept 0-based 972 VelixoMarket，last kept 0-based 998 / 1-based 999 DarkSoulSlayer8，next 0-based 999 / 1-based 1000 NullaryXYZ。因 from: 查询 512 字上限，40 个号需 2 次查询；为守 tight softCap（alloc.uf=1）只跑第一批 25 个。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST1（本轮 alloc.mustLe2h=1，与 live/≤2h 号合并为一次查询，查询长度 464≤512）。MUST1 本窗见到 PlayBitsigil、tmachinroBot、DeadHood_nft、pillowbookRH 的帖；优先号本窗 0 帖。MUST1 覆盖既有 live/≤2h 号（含 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / jacketagent / hokiseries / ozero_fun / PlayBitsigil / SpoxyGang / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch）以及上述 7 个优先号。
- mustSkip：无。THIN official 本轮未读（tight 无槽位），无 thinSkipDedup 查询。勿把 stale meta.nfSkipR1103 里误标为 NF 的 live 优先号再当 NF 跳过。
- mentions 本轮：mining-squeek+Nutshell / BN Agent pads+STARX（完成 R1874 预告四组中未跑的后半）。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=Tape/电路（1876%11=6）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=52，sentToReview=0，admitted=0，skipped=52（too_many_posts 47，already_in_library 4，profile_unresolved 1=p2eabs），deferredHandles=["p2eabs"]。silentCap=1 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST official start_time=2026-11-15T15:35:00Z（约 1h）。薄栏 KW 与 mentions start=2026-11-15T14:35:00Z（约 2h）。silent start=2026-11-14T16:35:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、MUST1 11、KW_LZ 2、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 22、KW_SN 7、MEN_MINE 1、MEN_BN 0、SILENT_MEN 25。
- 首读 UF1 后快照 168 / 1000，故 remainingBefore=169；末次 SILENT_MEN 快照 158 / 1000。
- THIN official 本轮 0 批（tight 延后）。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **Bitsigil**（@PlayBitsigil，id=bitsigil，Firstbound / Robinhood Chain）：官帖 00:14 CST https://x.com/playbitsigil/status/2122000307806732568 宣布 Free Mint 档持有者可以再铸造剩余 2 个 Firstbound NFT，免费、仅 gas。入口仍为 OpenSea https://opensea.io/collection/bitsigil/overview HTTP 200。官网 bitsigil.xyz HTTP 200，未见已核验 CA。这是 R1875 已通知「FCFS 名单钱包免费开铸（≤2/钱包）」之后的新官宣，对象是 Free Mint 档/剩余额度，必须通知。公售 $3（11-16 02:00 CST，约 1.3h）尚未开始、也未宣布取消，不得写成已开或已免费。le2h=true，status=live，focus=false。本号不自动 mint。
- **qtronlaptops**（@qtronlaptops）：同一开铸仍为 2026-11-16 01:00 CST（约 0.3h），$1 / 4444，OpenSea https://opensea.io/collection/q-tron-laptops HTTP 200。本窗无新官帖。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=true，status=watching。本号不自动 mint。
- **pillowbook-rh**（@pillowbookRH，$PILLOW / Pons）：同一开窗仍为 2026-11-16 01:00 CST（约 0.3h，17:00 UTC）。本窗再见的仍是 R1875 已记录的 00:00 CST T-1h 倒计时帖，称 CA 将只发官号和官网，尚未公布 CA。官网 pillowbook.pro 本轮 3 次探测均 TLS unexpected eof，未拿到 HTTP 200；R1874/R1875 曾重试成功，视为瞬时故障，不得据此改判关窗或下线。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=true，status=watching。本号不自动 mint。
- **POLYROB**（@tmachinroBot）：官帖 00:12 CST https://x.com/tmachinroBot/status/2121999886224621720 称还剩 1 小时，关闭时间仍为 2026-11-16 01:12 CST（17:12 UTC，约 0.5h），固定价 0.033 ETH，任何人可铸。铸造页 https://6551.polyrob.dev/ HTTP 200。已在 R1873 按关窗首次 ≤2h 提醒，不重推。le2h=true，status=live。本号不自动 mint。
- **Dead Hood**（@DeadHood_nft，id=deadhood）：本窗再见的仍是 R1875 已通知的 00:00 CST Mint is Live 官帖与 OpenSea 入口，无新的价格/CA/官网变化，不重推。le2h=false，status=live。本号不自动 mint。
- **jacketagent**（@jacketagent）：付费阶段已在 R1875 通知，本窗无新官帖，不重推。le2h=false，status=live。本号不自动 mint。
- **VoidCashio**（@VoidCashio，id=voidcash）：UF1 官帖 00:24 CST 称超过 2.5% 的 VOID 总供应已用交易费/协议收入回购并永久销毁。产品续更，不是新的打新窗口，不通知。
- **DualForge**（@DualForgeBSC）/ **SpoxyFun**（@SpoxyGang）/ **MicroFrens** / **osk-agent**：本窗无新的可操作事件，已分别提醒，不重推。本号不自动 mint。

## 新收录

- 无。silent 送审 0；关键词/mentions 盲捞未见可独立建卡的新官号。未为「再确认」额外刷 X。

## 关键词 / mentions 摘记

- 薄栏 KW 全跑：KW_TAPE/GIWA/DOGE 打满 25；KW_BTC 22；KW_SN 7；KW_LZ 2。核心栏 KW 本轮未跑。mentions：mining-squeek+Nutshell 1、BN Agent pads+STARX 0。
- mentions 按轮换同等覆盖本轮两组，未空转只扫单链。MEN_MINE 仅一条第三方回复讨论 squeekchain 改免费铸造，不是新官号官宣。
- 发现不等于关注：本轮盲捞 0 个新官号录取。
- 未另建卡 / 不收录：@Ord_Dropz 仍为既有铭文掉落/二级市场号，不是新项目；@Tbdoubleu 为个人/艺术家铭文 mint 预告（称明日官宣），不是新台；@spontan199 / @MandyHush8duw / @hhhh3i2o 等为评论/粉丝/垃圾引流号，不是项目官号。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂。
- soft-debt lastChecked：canton / glaze / tokenWorks 相关 Watch 仅刷新时间，无新 Canton/Glaze/TW 收录。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1876.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：在库 Bitsigil Free Mint 档持有者可再免费铸造剩余 2 个 Firstbound（仅 gas，OpenSea）。qtronlaptops / pillowbook-rh / POLYROB 已在 R1873 按首次 ≤2h 提醒，不重推。DeadHood / jacketagent 已在 R1875 提醒，不重推。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=25，送审 0。deferredHandles=["p2eabs"]。
- 核心栏 KW、THIN official、其余 mentions 因 tight 延后。fat official nextStart 未推进，fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 999 NullaryXYZ 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。silent 下一轮 GIWA（1877%11=7）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 本次已按「Free Mint 档持有者可再打剩余 2 个」通知。后续除非关窗、售罄、公布已核验 CA、入口变化，或公售 $3（11-16 02:00 CST）实际开始（且官方未取消/未改免费），否则不要只因同一 FCFS/Free Mint 免费窗口仍开再推。不要把未宣布取消的公售写成也已免费。
- jacketagent 已在 R1875 按「免费结束、付费 0.003 BNB 开始」通知。后续除非关窗、售罄、改价或规则变化，否则不要只因同一付费窗口仍开再推。
- DeadHood 已在 R1875 按首次官方开铸+OpenSea 入口通知。后续除非关窗、改价、公布 CA/价格，或官网恢复，否则不要只因同一开铸仍开再推。
- DualForge 官方开闸已在 R1868 推送；不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟已过且无新阶段官宣，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 开铸窗口已在 R1873 按首次 ≤2h 提醒；后续除非关窗、开铸确认、改价、改入口、公布 CA 或规则变化，否则不要只因同一窗口仍未开再推。
- POLYROB 公售关窗 2026-11-16 01:12 CST 已在 R1873 按首次 ≤2h 提醒；后续除非关窗、改价或入口变化，否则不要只因同一公售仍开再推。
- PlunderPort 不得仅凭官宣或第三方「Mint: FREE / 供应 3333」写成已核验免费 LIVE；需官网可达或可核验 mint 入口后再判断。
- SpoxyFun 免费已售罄，不要写成免费 LIVE；付费 0.001 BNB 已开铸。
- Motherlode 不要把 @Motherlode_live 再建一张卡。
- Anchain / Zeroportal 站点未见回链 X，不得写成已互链核验。
- escapehub Launchpad 时钟仍为 2026-11-16 23:00 CST，尚未 ≤2h，已在 R1684 按定档通知，不要提前重推。
- remaining 158，仍低于 200，后续轮继续按紧额度口径：保 UF soft → 必盯 Watch 增量/≤2h → 关键词去重合并；mentions 继续按链轮换子集。remaining 仍允许时尽量保留十栏独立薄栏 KW，remaining <50 再考虑进一步合并。若额度回升到能多 1 次主扫，优先补 THIN official 或被砍掉的核心栏 KW，不要扩探索读。勿把 stale nfSkipR1103 误标号再当 NF 跳过。
