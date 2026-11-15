# 早期打新雷达 R1871

- 时间：2026-11-15 22:07 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（在库 Jacket Agent 免费铸造首次进入 ≤2h；新收录 Anchain 发射台 LIVE，非免费 mint）
- 新收录：anchain
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 6ecca19 R1870）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 281 → remaining 256（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 281≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读，thinSkipDedup=THIN1_LZ 去掉 ozero_fun（已在 MUST1，同一 handle 只拉一次），未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- userFollowWatch 已刷完本分片：从 0-based 721 / 1-based 722 OmniArb 起，kept 48，真实 NF_skip 14（RedirectCash、kyte_market、vytraqfun、hyperlinkdotfun、HordeOnElysium、lazabitmeme、XiangHao91647、BrokeNiggameme、bndoge_bn、Mintbncat_ai、oblaunchpadAll、mint_WRIT、AiPullpad、oblaunchpadbase，按已知 NF 未重读），walkScanned 62，无绕回。first kept 0-based 721 OmniArb，last kept 0-based 782 / 1-based 783 nibblerss，next 0-based 783 / 1-based 784 noryxtradehq。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2（均不在本 UF 分片）；MUST2 本窗 0 帖。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun / PlayBitsigil / SpoxyGang。
- mustSkip：无。thinSkipDedup：ozero_fun。
- mentions 本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- silentLane=挖矿（1871%11=1）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=1，sentToReview=0，admitted=0，skipped=0。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST/THIN official start_time=2026-11-15T13:00:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T11:55:00Z（约 2h）。silent start=2026-11-14T13:55:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 12、MUST2 0、THIN1_LZ 3、THIN2_TAPE 6、THIN3_GIWA 3、THIN4_BTC 5、THIN5_DOGE_SN 2、KW_LZ 5、KW_TAPE 25、KW_GIWA 17、KW_DOGE 25、KW_BTC 16、KW_SN 6、KW_MINT 25、KW_MINE 10、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_LZ 25、MEN_ELY 25、MEN_MINE 1、MEN_BN 0、SILENT_MEN 1。
- 首读 UF1 后快照 280 / 1000，故 remainingBefore=281；末次 SILENT_MEN 快照 256 / 1000。
- THIN official 本轮 5 批。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **jacketagent**（@jacketagent）：免费铸造首次进入 ≤2h，截止 2026-11-16 00:00 CST。官帖 21:27 CST 倒计时 https://x.com/jacketagent/status/2121958144683409567。官网 jacketagent.pages.dev 仍 HTTP 200。BNB Chain status() 核验：phase=1，minted=171，freeSold=171，paidSold=0，freeRemaining=329，paidRemaining=15000。免费 500 份、每 Agent ID 1 份、0.0001 BNB；付费 0.003 BNB 将在免费结束后开启（15,000 份）。NFT CA 0x70FdD1a7f382893708d00fC2eF9C38cAe7DEC92B。R1824 已按免费 LIVE 通知，本轮是首次 ≤2h 提醒。le2h=true，status=live。本号不自动 mint。
- **Bitsigil**（@PlayBitsigil，id=bitsigil）：MUST1 再见同一免费 WL / GTD $2 23:00 CST 窗口，已在 R1870 按首次 ≤2h 提醒，不重推。CA 仍未独立核验。本号不自动 mint。
- **SpoxyFun**（@SpoxyGang）：MUST1 官号称 staking coming soon；付费 mint 仍 0.001 BNB，免费已售罄。已在 R1870 按付费 LIVE 新收录通知，不重推。本号不自动 mint。
- **PlunderPort**（@PlunderPort）：未见新的可核验开铸入口；官网 plunderport.fun 本轮仍 TLS/HTTP 失败（HTTP 000），不得写成已核验免费 LIVE。同一 3333/FREE 官帖不重推。
- **POLYROB**（@tmachinroBot）：关闭时间仍为 2026-11-16 01:12 CST（约 3.1h），尚未 ≤2h，已按此前窗口通知，不重推。
- **pillowbook-rh**（@pillowbookRH）：开窗仍为 2026-11-16 01:00 CST（约 2.9h），尚未 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST，尚未 ≤2h，不重推。
- **DualForge**（@DualForgeBSC）/ **osk-agent**（@AIAgent_OSK）/ **MicroFrens** / **hokiseries**：MUST1 本窗无新的可操作变化；此前窗口已通知，不重推。
- **Motherlode**（id=motherlode-fun，原号 @motherlode_fun）：本轮确认官方站点 https://motherlode.live（HTTP 200，互链 @Motherlode_live，不是 @motherlode_fun）。不另建第二张卡。@Motherlode_live 于 2026-11-14 17:22 CST 建立（xUserId 2121533965479944192），47 粉、9 帖。官帖 21:37 CST https://x.com/Motherlode_live/status/2121960811568697705 称 Devnet Beta 已开，Genesis waitlist 仅 100 席，入口 https://motherlode.live/beta。非主网免费 mint，非 ≤2h，不按新收录通知。已把 @Motherlode_live 补进 userFollowWatch + miningWatch。本号不自动 mint。

## 新收录

- **anchain**（@AnchainApp）：KW_PAD includes 用户对象核验（未另拉时间线）。官号 2026-11-15 20:45:30 CST 建立（xUserId 2121947039349260288），未认证，0 粉、3 帖、following=0。资料栏 t.co 解析为 https://anchain.app/。R1870 因站点默认 TLS 失败暂缓；本轮改用 TLS1.2+HTTP/1.1 后 GET 200。站点为印尼语界面的 Solana USDC 发射台（创建代币、bonding curve、目标 100 万美元毕业 Raydium）。站点静态 HTML/JS 未见 x.com/AnchainApp 回链（仅创建表单 twitter 占位），siteXMutual 不成立，与 R1864 usemerged 同类口径。官帖 21:51 CST https://x.com/AnchainApp/status/2121964315729437001。未见独立核验 CA。非免费 mint，非 ≤2h。DeepSeek-flash admit=true，overall 46（early 90 / actionable 28 / novelty 35 / risk 78），category=台子/Meme，status=live（发射台已开，**不是免费 LIVE**），focus=false。已进 userFollowWatch + agentPadWatch。本号不自动 mint。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_GIWA 17；KW_BTC 16；KW_MINE 10；KW_SN 6；KW_LZ 5。mentions：LayerZero 25、Elysium+kinetiq 25、mining-squeek+Nutshell 1、BN Agent pads+STARX 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞经 KW_PAD includes 独立抓到 @AnchainApp，并在站点可达后收录。
- 未另建卡 / 不收录：**@Motherlode_live** 与在库 motherlode-fun 同一产品，只更新原卡；**rugsightapp** 为 Solana rug-risk 工具，非打新窗口。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂。
- 新卡已进 Watch：anchain → userFollowWatch + agentPadWatch。
- 在库补挂：@Motherlode_live → userFollowWatch + miningWatch（挂在已有 id=motherlode-fun；@motherlode_fun 原 Watch 保留）。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1871.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：Jacket Agent 免费铸造首次进入 ≤2h（截止 11-16 00:00 CST，链上 171/500）；新收录 Anchain（非免费 mint，仅观察）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=1，无新静号收录。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 783 noryxtradehq 起。mentions 下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。silent 下一轮 台子/Meme（1872%11=2）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 同一免费 WL / GTD $2 23:00 CST 窗口已在 R1870 提醒，不要每轮重推；后续除非关窗、改规则、公布已核验 CA、FCFS/公售开始或 mint 入口变化，否则不要只因同一窗口仍开再推。
- DualForge 官方开闸已在 R1868 推送，后续不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟 20:00 CST 已过且无新阶段官宣，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 本轮已按首次 ≤2h 提醒；免费至 11-16 00:00 CST。后续除非关窗、名额售罄、付费阶段开始或规则变化，否则不要只因仍在同一免费窗口再推。
- PlunderPort 不得仅凭官宣「Mint: FREE / 供应 3333」写成已核验免费 LIVE；需官网可达或可核验 mint 入口后再判断。
- SpoxyFun 免费已售罄，不要写成免费 LIVE；付费 0.001 BNB 已开铸。与 @spoxydev / Cyber Spirits 同域，不要合并覆盖旧卡。
- Motherlode 不要把 @Motherlode_live 再建一张卡；官网与 Devnet/waitlist 已记入 motherlode-fun，非主网免费 mint，不要按新收录或免费 LIVE 重推。
- Anchain 已收录；站点未见回链 X，不得写成已互链核验官网站。
