# 早期打新雷达 R1875

- 时间：2026-11-16 00:06 CST（Asia/Shanghai）
- 模式：tight（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 Elysium Rigs；在库 Bitsigil FCFS 名单钱包免费开铸、jacketagent 付费阶段开始、DeadHood 首次官方开铸）
- 新收录：elysium-rigs（@elysiumrigs）
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 5d97e65 R1874，已是最新）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 181 → remaining 169（日硬顶 1000，重置约 08:00 CST）。xReads 12（main 11 + silent 1），admitVerify 0。
- mode=tight，softCap 11，minSpend 11，silentCap 1，ufAccountShard hint 40、实际 24。main 11 已达 softCap / minSpend：UF×1 + MUST×2 + 薄栏 KW×6 + mentionsThin×2；另 silent×1 = 12。因 remainingBefore 181<200，按紧额度口径未补核心栏 KW、未跑 THIN official、mentions 只跑轮换前 2 组。同一 handle 只拉一次，未与厚表合并，未另开探索读。
- 薄栏六条独立关键词均跑到（LZ/Tape/GIWA/DogeEVM/BTC/Starknet）。核心栏 打新/挖矿/台子/GO/Elysium 关键词本轮延后（tight alloc kwCore=0）。BN Agent 钱包本轮靠 MUST 优先号（MUST2）覆盖，核心 PAD KW 未跑。mentions 本轮 LayerZero / Elysium+kinetiq。
- userFollowWatch 已刷完本分片：从 0-based 946 / 1-based 947 BNBRunnerz 起，kept 24，真实 NF_skip 2（kpin_ai、LostGodsOnRH，按已知 NF 未重读），walkScanned 26，无绕回。first kept 0-based 946 BNBRunnerz，last kept 0-based 971 / 1-based 972 hoodiemoneygang，next 0-based 972 / 1-based 973 VelixoMarket。因 from: 查询 512 字上限，40 个号需 2 次查询；为守 tight softCap（alloc.uf=1）只跑第一批 24 个。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2；MUST2 本窗 0 帖。MUST1 覆盖既有 live/≤2h 号（含 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / jacketagent / hokiseries / ozero_fun / PlayBitsigil / SpoxyGang / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch）。
- mustSkip：无。THIN official 本轮未读（tight 无槽位），无 thinSkipDedup 查询。勿把 stale meta.nfSkipR1103 里误标为 NF 的 live 优先号再当 NF 跳过。
- mentions 本轮：LayerZero / Elysium+kinetiq。下一轮：mining-squeek+Nutshell / BN Agent pads+STARX（先完成 R1874 预告四组中未跑的后半），然后 Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=Elysium（1875%11=5）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=39，sentToReview=1（@elysiumrigs，已录取），admitted=1，skipped=38（too_many_posts 29，already_in_library 6，no_product_signal 2，profile_unresolved 1），deferredHandles=["p2eabs"]。silentCap=1 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST official start_time=2026-11-15T15:00:00Z（约 1h）。薄栏 KW 与 mentions start=2026-11-15T14:00:00Z（约 2h）。silent start=2026-11-14T16:00:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、MUST1 21、MUST2 0、KW_LZ 3、KW_TAPE 25、KW_GIWA 25、KW_DOGE 25、KW_BTC 16、KW_SN 8、MEN_LZ 14、MEN_ELY 25、SILENT_MEN 25。
- 首读 UF1 后快照 180 / 1000，故 remainingBefore=181；末次 SILENT_MEN 快照 169 / 1000。
- THIN official 本轮 0 批（tight 延后）。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **Bitsigil**（@PlayBitsigil，id=bitsigil，Firstbound / Robinhood Chain）：官帖 00:00 CST https://x.com/playbitsigil/status/2121996655507444055 宣布 FCFS IS LIVE。Firstbound 对 FCFS 名单钱包免费铸造（仅 gas），每钱包最多 2 个，先到先得、售完即止。入口 t.co 仍解析为 OpenSea https://opensea.io/collection/bitsigil/overview 。23:51 CST https://x.com/playbitsigil/status/2121994404168863979 宣布退款已完成。官网 bitsigil.xyz HTTP 200，未见已核验 CA。原定 11-16 01:00 CST 的 FCFS $2 实际提前开且改为免费，不得再写成 $2。公售 $3（11-16 02:00 CST）未宣布取消；23:53 CST 官号回复「You can mint at public stage」，不得把公售也写成已免费。此为 FCFS 实际开铸（规则/价格相对 R1874 再变），必须通知。le2h=true，status=live，focus=false。本号不自动 mint。
- **jacketagent**（@jacketagent）：免费阶段已于 2026-11-16 00:00:34 CST 结束。BNB Chain status()：phase=2，minted=172，freeSold=172，paidSold=0，freeRemaining=328（免费额度未售完即到期），paidRemaining=15000，付费价 0.003 BNB。官网 jacketagent.pages.dev HTTP 200。官帖 23:34 CST https://x.com/jacketagent/status/2121990280417321175 预告免费截止后立即开付费。R1871 已按免费窗口首次 ≤2h 提醒；此为付费阶段开始，必须通知。付费截止 2026-11-17 00:00:34 CST（约 24h），不再记入 le2h 列表。le2h=false，status=live。本号不自动 mint。
- **Dead Hood**（@DeadHood_nft，id=deadhood）：官帖 00:00 CST https://x.com/DeadHood_nft/status/2121996654710775895 宣布 Mint is Live，入口 OpenSea https://opensea.io/collection/deadhood/overview HTTP 200。官网 deadhood.fun 仍 HTTP 403。价格、链、CA 均未核验。R1851 只报过 mint day + 10 钱包 GTD、页面未核验；这是首次官方开铸+可核验铸造入口，必须通知。不得编造价格或写成已核验免费。le2h=false，status=live。本号不自动 mint。
- **qtronlaptops**（@qtronlaptops）：同一开铸仍为 2026-11-16 01:00 CST（约 0.9h），$1 / 4444，OpenSea https://opensea.io/collection/q-tron-laptops 。官帖仍是 R1873 已用的 23:01 CST https://x.com/qtronlaptops/status/2121981986461896737「MINT IN TWO HOURS」，不是新窗口。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=true，status=watching。本号不自动 mint。
- **pillowbook-rh**（@pillowbookRH，$PILLOW / Pons）：同一开窗仍为 2026-11-16 01:00 CST（约 0.9h，17:00 UTC）。官帖 00:00 CST T-1h 倒计时，称 CA 将只发官号和官网，尚未公布 CA。官网 pillowbook.pro 重试 HTTP 200（中间一次 SSL 失败视为瞬时，与 R1874 相同口径）。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=true，status=watching。本号不自动 mint。
- **POLYROB**（@tmachinroBot）：关闭时间仍为 2026-11-16 01:12 CST（约 1.1h），固定价 0.033 ETH 仍开，铸造页 https://6551.polyrob.dev/ HTTP 200。MUST1 本窗无该号新帖。已在 R1873 按关窗首次 ≤2h 提醒，不重推。le2h=true，status=live。本号不自动 mint。
- **DualForge**（@DualForgeBSC）/ **SpoxyFun**（@SpoxyGang）：MUST1 再见的仍是 R1874 已用的 23:09 CST 进度/市场预热帖，不是新的可操作事件。已分别在 R1868 / R1870 提醒，不重推。本号不自动 mint。

## 新收录

- **elysium-rigs**（@elysiumrigs，Elysium Rigs）：silent mentions + MEN_ELY 盲捞到的新官号。X includes 核验：user id 2120843143788601345，2026-11-12 19:39 CST 创建，5 粉、1 帖、资料栏无网站。bio：Mine to mint on @Enter_Elysium. 2,048 rigs mined by your own CPU and GPU. The hash you find decides the rig you get。Elysium 主网已于 2026-11-09 上线，属 Announced+明确部署，可进 Elysium 栏。官帖 https://x.com/elysiumrigs/status/2121995809961267233 被 InkInsiders / Web3Connects / ZentroHub 引用，转述为 first mine-to-mint NFT collection，并呼吁 drop wallets；本轮未再请求该条正文，不得把第三方转述写成已核验官文全文。无官网、无已核验 CA、未见 mint/mine 入口。status=announced（钱包征集/预告），不是免费 LIVE。focus=false。DeepSeek-flash（思考开启）admit=true，overall 61（early 92 / actionable 28 / novelty 74 / risk 78）。已补进 elysiumWatch 与 miningWatch。本号不自动 mint。

## 关键词 / mentions 摘记

- 薄栏 KW 全跑：KW_TAPE/GIWA/DOGE 打满 25；KW_BTC 16；KW_SN 8；KW_LZ 3。核心栏 KW 本轮未跑。mentions：LayerZero 14、Elysium+kinetiq 25。
- mentions 按轮换同等覆盖本轮两组，未空转只扫单链。
- 发现不等于关注：盲捞独立新号录取 1 个（@elysiumrigs）。
- 未另建卡 / 不收录：@ArenaLaunchPVP（站点 arenalaunch.trade / 帖链 arenalaunch.tech/zro）与在库 arena-elysium（@ArenaElysium，官网 arenalaunch.tech）同域家族，不另建卡；@ZgoatNoya 为个人号转述 @PlunderPort 扩供与免费 mint，不是官号，且 PlunderPort 仍不得仅凭第三方「Mint: FREE / 供应 3333」写成已核验免费 LIVE；@Ord_Dropz 为既有铭文掉落号「明日官宣」，不是新项目；@SpanX_bridge 为跨链桥合作帖，不是打新；@VoltaFamily / @addzerosfun / @ontrench_fun 已在库。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂。
- 本轮新卡 elysium-rigs 已进 elysiumWatch + miningWatch。
- soft-debt lastChecked：canton / glaze / tokenWorks 相关 Watch 仅刷新时间，无新 Canton/Glaze/TW 收录。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1875.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 Elysium Rigs（预告/钱包征集，非免费 LIVE）；Bitsigil FCFS 名单钱包免费开铸；jacketagent 付费阶段开始；DeadHood 首次官方开铸+OpenSea 入口。qtronlaptops / pillowbook-rh / POLYROB 已在 R1873 按首次 ≤2h 提醒，不重推。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=25，送审 1 个并录取。deferredHandles=["p2eabs"]。
- 核心栏 KW、THIN official、其余 mentions 因 tight 延后。fat official nextStart 未推进，fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 972 VelixoMarket 起。mentions 下一轮 mining-squeek+Nutshell / BN Agent pads+STARX。silent 下一轮 Tape/电路（1876%11=6）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 本次已按「FCFS 名单钱包免费开铸」通知。后续除非关窗、售罄、公布已核验 CA、入口变化，或公售 $3（11-16 02:00 CST）实际开始（且官方未取消/未改免费），否则不要只因同一 FCFS 免费窗口仍开再推。不要把未宣布取消的公售写成也已免费。
- jacketagent 本次已按「免费结束、付费 0.003 BNB 开始」通知。后续除非关窗、售罄、改价或规则变化，否则不要只因同一付费窗口仍开再推。
- DeadHood 本次已按首次官方开铸+OpenSea 入口通知。后续除非关窗、改价、公布 CA/价格，或官网恢复，否则不要只因同一开铸仍开再推。
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
- remaining 169，仍低于 200，后续轮继续按紧额度口径：保 UF soft → 必盯 Watch 增量/≤2h → 关键词去重合并；mentions 继续按链轮换子集。remaining 仍允许时尽量保留十栏独立薄栏 KW，remaining <50 再考虑进一步合并。若额度回升到能多 1 次主扫，优先补 THIN official 或被砍掉的核心栏 KW，不要扩探索读。勿把 stale nfSkipR1103 误标号再当 NF 跳过。
