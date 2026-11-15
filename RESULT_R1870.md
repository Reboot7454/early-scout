# 早期打新雷达 R1870

- 时间：2026-11-15 21:43 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（新收录 SpoxyFun 付费 mint 已 LIVE；在库 Bitsigil GTD $2 23:00 CST 首次进入 ≤2h）
- 新收录：spoxyfun
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 3f53e4a R1869）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 306 → remaining 281（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 306≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读，thinSkipDedup=THIN3_GIWA 去掉 GAMA_GIWA（本轮已在 UF 分片，同一 handle 只拉一次），未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 662 / 1-based 663 usetrenchscope 起，kept 48，真实 NF_skip 11（nonamespnft、heyribbid、inkwellonbnb、certuna_rh、miuadotfun、origopad、lootbale、useapppayfun、CyclopesElysium、elyword_xyz、AgentFramlin404，按已知 NF 未重读），walkScanned 59，无绕回。first kept 0-based 662 usetrenchscope，last kept 0-based 720 / 1-based 721 GBOSS_onsol，next 0-based 721 / 1-based 722 OmniArb。
- 优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2（均不在本 UF 分片）；MUST2 本窗 0 帖。MUST1 仍覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun / PlayBitsigil。
- mustSkip：无。thinSkipDedup：GAMA_GIWA。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=打新（1870%11=0）。search_users 仍不在 X 工具目录，只走 mentions。silentAccounts.ran=true，seen=25，sentToReview=0，admitted=0，skipped=0。silentCap=2 用 1。本轮不追加 get_users_by_usernames 第二读。不要把下一轮 silentCap 花在 bitcoincoreorg。
- UF/MUST/THIN official start_time=2026-11-15T12:30:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T11:30:00Z（约 2h）。silent start=2026-11-14T13:30:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 1、UF2 0、MUST1 13、MUST2 0、THIN1_LZ 4、THIN2_TAPE 9、THIN3_GIWA 4、THIN4_BTC 3、THIN5_DOGE_SN 1、KW_LZ 5、KW_TAPE 25、KW_GIWA 16、KW_DOGE 25、KW_BTC 19、KW_SN 5、KW_MINT 25、KW_MINE 10、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 1、MEN_GIWA 1、MEN_BTC 0、MEN_SN_DOGE 0、SILENT_MEN 25。
- 首读 UF1 后快照 305 / 1000，故 remainingBefore=306；末次 SILENT_MEN 快照 281 / 1000。
- THIN official 本轮 5 批。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **Bitsigil**（@PlayBitsigil，id=bitsigil）：免费 WL 仍开放（每钱包 1 份只付 gas，官方 OpenSea https://opensea.io/collection/bitsigil/overview），同一免费 WL 窗口不重推。GTD $2 将于 2026-11-15 23:00 CST 开始，本轮已进入 ≤2h，这是该阶段首次提醒。FCFS $2 11-16 01:00 CST、公售 $3 自 02:00 CST 起 48h，均尚未 ≤2h。CA 仍未独立核验。le2h=true，status=live。本号不自动 mint。
- **PlunderPort**（@PlunderPort）：21:16 CST 官帖 https://x.com/PlunderPort/status/2121955508412125273 称供应 1024→3333，文案 Mint: FREE、LayerZero。官网 plunderport.fun 本轮 GET 不可达（HTTP 000），未见开铸入口或独立核验 CA，不得写成已核验免费 LIVE，status 仍 watching。已在 alert 中一句带过。本号不自动 mint。
- **BEM**（@BEMGoGoGo）：21:18 CST 官帖 https://x.com/BEMGoGoGo/status/2121955918908706986 称 Phase 2 is open for Behemoth NAND contributions，目标 500–1882 NAND。此前 R1719 仅是「下周」预告，本轮为官方首次宣布二期已开放。无新 CA。未单独作为 notify 主因。本号不自动 mint。
- **DualForge**（@DualForgeBSC）：MUST1 本 1h 官方窗无该号新帖。官方开闸已在 R1868 推送，不重推。
- **POLYROB**（@tmachinroBot）：关闭时间仍为 2026-11-16 01:12 CST（约 3.6h），尚未 ≤2h，已按此前窗口通知，不重推。
- **jacketagent**：MUST1 再见官方倒计时，免费仍至 2026-11-16 00:00 CST（开跑时约 2.4h，21:43 CST 仍约 2.3h），尚未进入 ≤2h，不重推。下一轮约 22:00 CST 后再判断。
- **pillowbook-rh**（@pillowbookRH）：官号有 $PILLOW 费用用途说明；开窗仍为 2026-11-16 01:00 CST（约 3.4h），尚未 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST，尚未 ≤2h，不重推。
- **hokiseries**：公售官方结束时钟 2026-11-15 20:00 CST 已过。MUST1 本窗无该号新帖，未见官方新阶段，不重推。
- **osk-agent**（@AIAgent_OSK）：MUST1 本窗无该号新帖。池已开事件已在 R1863 推送，不重推。
- **MicroFrens**：MUST1 本窗无该号新帖。持有者 OG FREE 仍在进行（R1860 已推送），无新的对公窗口，不重推。
- **Gloopix**（@Gloopix_）/ **ozero**（@ozero_fun）：MUST1 本窗无新的可操作变化，不重推。

## 新收录

- **spoxyfun**（@SpoxyGang）：KW_MINT includes 用户对象核验（未另拉时间线）。官号 2026-11-15 00:30 CST 建立（xUserId 2121641382507081728），约 21h，11 粉、4 帖。资料栏 t.co 解析为 https://spoxydev.fun，站点 HTTP 200 并回链 https://x.com/SpoxyGang，互链成立。BNB Chain 2,222 只幽灵 NFT。站点写明免费 800 份（仅 Agent ID）已售罄 800/800；付费 mint() 已对所有钱包开放，0.001 BNB，不再要 Agent ID。站点公布 CA 0xf814792B5C3E8b2953AC00CC1F55B21d7B36BaD0（文案 SpoxyFun V2）；本轮 bsc-dataseed eth_getCode 确认有合约字节码（约 7378 字节），未做完整独立审计，不得当作已审计。该域名此前被在库卡 spoxy/@spoxydev（R647，Cyber Spirits，另一 CA 0x0Fa1…E74E）使用，已另建新卡、不覆盖旧卡。DeepSeek-flash admit=true，overall 53（early 80 / actionable 72 / novelty 42 / risk 78），category=打新，status=live（付费开铸，**不是免费 LIVE**），focus=false。已进 userFollowWatch + freeMintWatch + agentPadWatch + bnAgentWatch。本号不自动 mint。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_BTC 19；KW_GIWA 16；KW_MINE 10；KW_LZ 5；KW_SN 5。mentions：Tape 1、GIWA 1、BTC 0、Starknet+DogeEVM 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞经 KW_MINT includes 独立抓到 @SpoxyGang 并核验官网后收录。
- 未送审（不收录）：**Anchain**（@AnchainApp，约 0.9h、0 粉，Solana 台宣传，https://anchain.app 本轮 GET 不可达，未见互链核验）；PlayPixelora 仍仅第三方 WL 讨论、无官方 LIVE 确认，在库不重推。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 近轮（round≥1840）在库卡扫描：0 张新漏挂（matrix-agents 无官推属已知例外，已在 agentPadWatch / freeMintWatch / bnAgentWatch 的 candidateIds）。
- 历史漏挂补挂：在库 spoxy/@spoxydev（R647）此前不在任何 Watch accounts，本轮补进 userFollowWatch + freeMintWatch + agentPadWatch。
- 新卡已进 Watch：spoxyfun → userFollowWatch + freeMintWatch + agentPadWatch + bnAgentWatch。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1870.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：新收录 SpoxyFun 付费 mint 已 LIVE（免费已售罄）；Bitsigil GTD $2 23:00 CST 首次进入 ≤2h。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。本轮 SILENT_MEN rc=25，无新静号收录。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 721 OmniArb 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。silent 下一轮 挖矿（1871%11=1）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- Bitsigil 同一免费 WL 窗口不要每轮重推；本轮已按阶段切换（GTD ≤2h）提醒。后续除非关窗、改规则、公布已核验 CA、FCFS/公售开始或 mint 入口变化，否则不要只因免费 WL 仍开再推。
- DualForge 官方开闸已在 R1868 推送，后续不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- osk-agent 池已开事件已在 R1863 推送，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟 20:00 CST 已过且无新阶段官宣，已在 R1815 写明结束时间，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 免费 LIVE 至 11-16 00:00 CST，进入 ≤2h（约 22:00 CST）后再判断。
- PlunderPort 不得仅凭官宣「Mint: FREE / 供应 3333」写成已核验免费 LIVE；需官网可达或可核验 mint 入口后再判断。
- SpoxyFun 免费已售罄，不要写成免费 LIVE；付费 0.001 BNB 已开铸。与 @spoxydev / Cyber Spirits 同域，不要合并覆盖旧卡。
- Anchain 未收录（站点本轮不可达）；不要为再确认额外刷 X，除非出现可达官网或互链证据。
- bamboo-ronin / panko / loopiez / klayo 不得在后续轮次仅凭 bio 或预告文案写成已核验免费 LIVE；需官网、官方开窗帖或可核验 mint 入口。
- setcap / st0cks 暂无可操作窗口，不要当作 LIVE 重推。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
- canton/glaze/tokenWorks 本轮仅 soft-touch lastChecked，无新 admit。
