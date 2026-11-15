# 早期打新雷达 R1872

- 时间：2026-11-15 22:35 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 Zeroportal；尚未开闸、非免费 mint、非 ≤2h，仅观察）
- 新收录：zeroportal
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 3151d1e R1871，已是最新）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 256 → remaining 231（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 256>200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读，thinSkipDedup=THIN1_LZ 去掉 ozero_fun（MUST1）、THIN2_TAPE 去掉 tapebitprotocol（UF1）、THIN3_GIWA 去掉 Flizyapp（UF2），同一 handle 只拉一次，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 783 / 1-based 784 noryxtradehq 起，kept 48，真实 NF_skip 3（bianfenhong、dinomitesnft、Morumai_，按已知 NF 未重读），walkScanned 51，无绕回。first kept 0-based 783 noryxtradehq，last kept 0-based 833 / 1-based 834 baoracletrade，next 0-based 834 / 1-based 835 elysium_machine。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2（均不在本 UF 分片）；MUST2 本窗 0 帖。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun / PlayBitsigil / SpoxyGang。
- mustSkip：无。thinSkipDedup：ozero_fun、tapebitprotocol、Flizyapp。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=台子/Meme（1872%11=2）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=47，sentToReview=0，admitted=0，skipped=47（too_many_posts 40、already_in_library 6、not_new 1），deferredHandles=[]。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST/THIN official start_time=2026-11-15T13:25:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T12:25:00Z（约 2h）。silent start=2026-11-14T14:25:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 2、UF2 3、MUST1 8、MUST2 0、THIN1_LZ 0、THIN2_TAPE 8、THIN3_GIWA 2、THIN4_BTC 4、THIN5_DOGE_SN 1、KW_LZ 3、KW_TAPE 25、KW_GIWA 18、KW_DOGE 25、KW_BTC 13、KW_SN 8、KW_MINT 25、KW_MINE 8、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 4、MEN_GIWA 1、MEN_BTC 0、MEN_SN_DOGE 0、SILENT_MEN 25。parse_errors=[]。
- 首读 UF1 后快照 255 / 1000，故 remainingBefore=256；末次 SILENT_MEN 快照 231 / 1000。
- THIN official 本轮 5 批。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **jacketagent**（@jacketagent）：同一免费窗口仍开，不重推。官帖仍为 21:27 CST 倒计时 https://x.com/jacketagent/status/2121958144683409567。官网 jacketagent.pages.dev 仍 HTTP 200。BNB Chain status() 核验：phase=1，minted=172，freeSold=172，paidSold=0，freeRemaining=328，paidRemaining=15000。较 R1871 仅 +1。免费仍 LIVE，付费尚未开始，截止 2026-11-16 00:00 CST。R1871 已按首次 ≤2h 提醒。le2h=true，status=live。本号不自动 mint。
- **Bitsigil**（@PlayBitsigil，id=bitsigil）：MUST1 仅见欢迎回复，未见关窗/改规则/已核验 CA/FCFS 或公售变化。同一免费 WL / GTD $2 23:00 CST 窗口已在 R1870 按首次 ≤2h 提醒，不重推。CA 仍未独立核验。本号不自动 mint。
- **SpoxyFun**（@SpoxyGang）：MUST1 再见 staking coming soon；付费 mint 仍 0.001 BNB，免费已售罄。已在 R1870 按付费 LIVE 新收录通知，不重推。本号不自动 mint。
- **POLYROB**（@tmachinroBot）：关闭时间仍为 2026-11-16 01:12 CST（约 2.6h），尚未 ≤2h，已按此前窗口通知，不重推。
- **pillowbook-rh**（@pillowbookRH）：MUST1 再见 21:30 CST 官帖重申 Launch: 17:00 UTC（2026-11-16 01:00 CST，约 2.4h），尚未 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST，尚未 ≤2h，不重推。
- **DualForge**（@DualForgeBSC）/ **osk-agent**（@AIAgent_OSK）/ **MicroFrens** / **hokiseries**：MUST1 本窗无新的可操作变化；此前窗口已通知，不重推。
- **runin-ai**（@RuninAI_com）：UF2 官帖 22:19 / 21:48 / 21:36 CST 继续预热 Agent ID + PoW 挖矿（Get ready / before the first window opens），尚未宣布已开窗；CA 仍为 0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6。不是新的免费开铸窗口，不重推。本号不自动 mint。
- **shielded-wizards**（@ShieldedWizBTC）：官帖提醒 raid update 今日 18:00 UTC（2026-11-16 02:00 CST，约 3.4h），前 5 队得 WL，不是公开免费 mint，尚未 ≤2h，不按新开铸通知。本号不自动 mint。

## 新收录

- **zeroportal**（@Zeroportalfun）：KW_GO includes 用户对象核验（未另拉时间线）。官号 2026-11-15 22:08:45 CST 建立（xUserId 2121968343208857600），未认证，1 粉、1 帖、following=18。资料栏 URL 解析为 https://zeroportal.fun。官网 GET 200。站点标题 “zeroportal — launch a token and decide where its fees go”；正文 “Not open yet. zeroportal goes live with its chain.” / “The contracts are written and tested. zeroportal opens the day its chain goes live.” 站点 `<body data-x="" data-telegram="" data-docs="">` 为空，Follow on X 按钮 hidden，siteXMutual 不成立（profile→site yes；site 回链 no）。官帖 22:24 CST https://x.com/Zeroportalfun/status/2121972560577331267：费用最多 8% 可分给发射者/持有者/回购；No owner. No mint. No pause. Opening with Zero chain。未见独立核验 CA。非免费 mint，非发射台 LIVE，非 ≤2h。DeepSeek-flash admit=true，overall 62（early 88 / actionable 32 / novelty 62 / risk 45），category=台子/Meme，status=announced，lzVerified=false，focus=false。已进 userFollowWatch + zeroWatch（Zero 链发射台，不是 BN agentPadWatch，也不是 LayerZero）。本号不自动 mint。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_GIWA 18；KW_BTC 13；KW_MINE 8；KW_SN 8；KW_LZ 3。mentions：Tape 4、GIWA 1、BTC 0、Starknet+DogeEVM 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞经 KW_GO includes 独立抓到 @Zeroportalfun，并在站点可达后收录。
- 未另建卡 / 不收录：**@loxleyswap** DeepSeek admit=false（已上线 Elysium swap，约 53 天、30 粉，早期度不足，不是 mint 窗口）；与库内 askloxleycom 同名不同产品，不合并、不另建卡。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂。
- 新卡已进 Watch：zeroportal → userFollowWatch + zeroWatch。
- soft-debt lastChecked：canton / glaze / tokenWorks 相关 Watch 仅刷新时间，无新 Canton/Glaze/TW 收录。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1872.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 Zeroportal（尚未开闸、非免费 mint，仅观察）。Jacket Agent 同一免费窗口仍开（链上 172/500）已在 R1871 按首次 ≤2h 提醒，不重推。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=25，无新静号进入审核。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 834 elysium_machine 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。silent 下一轮 GO盘（1873%11=3）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 同一免费 WL / GTD $2 23:00 CST 窗口已在 R1870 提醒，不要每轮重推；后续除非关窗、改规则、公布已核验 CA、FCFS/公售开始或 mint 入口变化，否则不要只因同一窗口仍开再推。
- DualForge 官方开闸已在 R1868 推送，后续不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟 20:00 CST 已过且无新阶段官宣，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送（约 23:00 CST 后可能进入）。
- jacketagent 已在 R1871 按首次 ≤2h 提醒；免费至 11-16 00:00 CST。后续除非关窗、名额售罄、付费阶段开始或规则变化，否则不要只因仍在同一免费窗口再推。
- PlunderPort 不得仅凭官宣「Mint: FREE / 供应 3333」写成已核验免费 LIVE；需官网可达或可核验 mint 入口后再判断。
- SpoxyFun 免费已售罄，不要写成免费 LIVE；付费 0.001 BNB 已开铸。与 @spoxydev / Cyber Spirits 同域，不要合并覆盖旧卡。
- Motherlode 不要把 @Motherlode_live 再建一张卡；官网与 Devnet/waitlist 已记入 motherlode-fun，非主网免费 mint，不要按新收录或免费 LIVE 重推。
- Anchain 已收录；站点未见回链 X，不得写成已互链核验官网站。
- Zeroportal 已收录为 announced，不得写成已开闸、免费 LIVE 或 LayerZero 项目；站点未见回链 X，不得写成已互链核验。Zero 链 ≠ LayerZero。
