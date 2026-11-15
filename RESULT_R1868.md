# 早期打新雷达 R1868

- 时间：2026-11-15 20:40 CST（Asia/Shanghai）
- 模式：pace（独立例行；lastFullAfterReset 保持 R1843，本轮不是 08:00 后首轮全量补扫）
- notify=true（在库 Bitsigil 首次进入 Firstbound 免费 WL mint ≤2h；DualForge 官方开闸确认 + 官网 + 公布 CA。0 新卡）
- 新收录：无
- 工作目录 `/workspace/early-scout/`，开跑已 `git pull`（当时 main @ 8efc9db R1867）。
- dsFallback=false，docsSynced=true
- 本号不自动 mint

## X 额度与覆盖

- remainingBefore 356 → remaining 331（日硬顶 1000，重置约 08:00 CST）。xReads 25（main 24 + silent 1），admitVerify 0。
- mode=pace，softCap 18，minSpend 18，silentCap 2，ufAccountShard 48。main 24 超 softCap 18（+6），已达 minSpend 18：UF×2 + MUST×2 + THIN×5 + 薄栏 KW×6 + 核心 KW×5 + mentions×4；另 silent×1 = 25。因 remaining 356≫200，按用户「额度够时不得砍栏」补齐全部十栏 KW 与 mentions 轮换 4 组。THIN official 5 批全读，未与厚表合并，未另开探索读。
- 十栏关键词均跑到（薄栏 LZ/Tape/GIWA/DogeEVM/BTC/Starknet；核心栏 打新/挖矿/台子/GO/Elysium）。BN Agent 钱包经核心栏 PAD/MINT KW、UF+MUST 覆盖；本轮 mentions 轮换为 Tape / GIWA / BTC / Starknet+DogeEVM。
- userFollowWatch 已刷完本分片：从 0-based 539 / 1-based 540 streamlitmaker 起，kept 48，真实 NF_skip 12（streamlitmaker、trycortano、hook404rh、agentpunkai、stockcatsfun、volitionxyz、tollsfun、bibiainft、agentboss_ai、trysmolpadfun、fistagent、villagers_rh，按已知 NF 未重读），walkScanned 60，无绕回。first kept 0-based 542 buckme_sol，last kept 0-based 598 / 1-based 599 resafudao，next 0-based 599 / 1-based 600 thevoidling_rh。在库 bitsigil 已补进 UF 与 freeMintWatch（含 candidateIds）；并补 loopiez / umbrapad 的 candidateIds。
- DualForgeBSC 不在本 UF 分片，已放入 MUST1（另含 ozero_fun）。优先号（starx_xlayer / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets）全部折入 MUST2；本窗仅 machinedotfun 一条视频向帖，非新 mint 窗口，非 NF。
- mustSkip：无。MUST1 覆盖 DualForgeBSC / MicroFrens / AIAgent_OSK / qtronlaptops / pillowbookRH / tmachinroBot / HoodTurtleRH / DeadHood_nft / Gloopix_ / infamousScratch / jacketagent / hokiseries / ozero_fun（thinSkipDedup：THIN1 去重 ozero_fun 已在 MUST1，THIN5 去重 anoncoinit 已在 UF2，未重读）。
- mentions 本轮：Tape / GIWA / BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silentLane=BTC（1868%11=9）。search_users 仍不在 X 工具目录，只走 mentions（Ordinals OR CRC20 OR ShieldedNaka）(mint OR launch)。silentAccounts.ran=true，seen=10，sentToReview=0，admitted=0，skipped=10。deferredHandles：slothnvivi、bitcoincoreorg、utexocom、BitlightLabs（多非 mint 项目）。silentCap=2 用 1。不要把下一轮 silentCap 花在 bitcoincoreorg。本轮不追加 get_users_by_usernames 第二读。
- UF/MUST/THIN official start_time=2026-11-15T11:30:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T10:30:00Z（约 2h）。silent start=2026-11-14T12:30:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。无 next_token 翻页。同一 handle 本轮只拉一次。
- 部分回包被 write_to_file 长行先截断，已从 Full text 完整文件恢复后解析，未重拉 X（禁止额外/重复 X 查询）。
- 栏 rc：UF1 0、UF2 1、MUST1 4、MUST2 1、THIN1 1、THIN2 2、THIN3 1、THIN4 2、THIN5 0、KW_LZ 7、KW_TAPE 25、KW_GIWA 13、KW_DOGE 25、KW_BTC 15、KW_SN 8、KW_MINT 25、KW_MINE 7、KW_PAD 25、KW_GO 25、KW_ELY 25、MEN_TAPE 1、MEN_GIWA 0、MEN_BTC 0、MEN_SN_DOGE 0、SILENT_MEN 6。
- 首读 UF1 后快照 355 / 1000，故 remainingBefore=356；末次 MEN_SN_DOGE 快照 331 / 1000。
- THIN official 本轮 5 批。thinSkipDedup：ozero_fun、anoncoinit。fat official nextStart 未推进，fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。

## 在库窗口 / 可操作变化

- **Bitsigil**（@PlayBitsigil，id=bitsigil）：在库自 R655（当时是 Early Access / top2000 WL，不是新 id），此前不在任何 Watch，lastChecked 停在 2026-10-27。本轮 KW_MINT 官号首帖 2026-11-15 20:30 CST https://x.com/playbitsigil/status/2121943802529370589 称 “Free Mint WL, it’s almost your turn. 30 minutes to go. See you on Robihood Chain.” 资料栏解析官网 https://bitsigil.xyz/，站点 twitter:site=@PlayBitsigil 且链到 https://x.com/PlayBitsigil，互链成立。FAQ 核验：Sunday 15 November 2026 在 OpenSea 铸造 Bitsigil: Firstbound，3333（3318 肖像 + 15 独份），阶段 UTC：12:00 团队预留 133 枚不售（20:00 CST）；13:00 Free Mint 只付 gas（21:00 CST）；15:00 GTD $2（23:00 CST）；17:00 FCFS $2（11-16 01:00 CST）；18:00 公售 $3 持续 48 小时至 11-17 18:00 UTC（11-16 02:00–11-18 02:00 CST）。白名单来自已结束 Early Access（10-25 至 11-1）与 Banner War 及合作社区；白名单阶段每钱包 1 份、公售 2 份，以 ETH 按当日汇率支付。官网写明官方 mint 链接只由 @PlayBitsigil 和 bitsigil.xyz 公布。本轮站点 HTML 未见 CA，不得发明合约。官号约 750 粉、242 帖，2026-10-09 建号。DeepSeek-flash（思考开）admit=true，overall 74（early 86 / actionable 78 / novelty 62 / risk 58），focus=false，status=announced，le2h=true。已补进 userFollowWatch + freeMintWatch。本轮约 20:40 CST 距免费 WL 约 19 分钟，按免费 mint ≤2h 必须推送。本号不自动 mint。
- **DualForge**（@DualForgeBSC）：MUST1 本 1h 官方窗出现开闸官帖。20:21 CST 两度宣布 “Minting is live at https://t.co/cx32nRM2Df”（https://x.com/DualForgeBSC/status/2121941729398198317 与 2121941533578641755），t.co 解析为 https://dualforge.fun/。官网 config status='live'。链上 ForgeCore `launchTime()`=0x6af990b0=1794740400=2026-11-15 19:00 CST，现已过。付费：首档 0.0100 BNB/钥，试用 0.00011 BNB，需一对 .ai Agent ID（Flint+Quench）；流动性达标 7 BNB 后开池。官网/SKILL 公布 CA：forgeCore 0x4dc8684d9b0e6a3374e5a6b9f371925b0baf36c4，keyNft 0xe8c8c27fc250c0aac4792ee8e2613e70260fdc4f，mineForge 0xe93714961cb5d0a66d0227cdff344e8b8fd34f81，token $DFORGE 0xe40eae1af7e792a53bd4eeb7e7a05de369a6a0f9，splitter 0x53147166074b8247fc97726df5fad846a317b8bc，CheckInGate 0x1ec7c35a3a8dcc2cb3fbf84e851422843056bc21，registry 0x60B9262456dE011F7d15a54CdD8c48bAaa8B022F。本轮 Sourcify 未独立再核验（403/404），caUnverified=true；其他选择子未见已核验 minted 数量。status 由 announced 改为 live。首次进入 ≤2h 已在 R1861 推送，本轮因「官方开闸确认 + 官网 + 公布 CA」再提醒。仅限 Binance Agent ID。付费，本号不自动 mint。
- **hokiseries**：Base Bots 公售官方结束时钟 2026-11-15 20:00 CST 已过。MUST1 本 1h 官方窗无该号新帖，未见官方新阶段。已在 R1815 写明结束时间，本轮不重推。le2h 已关。价格 0.0001 ETH，不是免费。
- **osk-agent**（@AIAgent_OSK）：MUST1 本 1h 官方窗无该号新帖。池已开事件已在 R1863 推送并写入已核验 CA，本轮不重推。付费只告警，本号不自动 mint。
- **jacketagent**：MUST1 本 1h 官方窗无该号新帖。免费仍 LIVE 至 2026-11-16 00:00 CST（约 3.3h），尚未进入 ≤2h，不重推。
- **POLYROB**（@tmachinroBot）：MUST1 本窗有末日提醒，关闭时间仍为 2026-11-16 01:12 CST（17:12 UTC），约 4.5h，尚未 ≤2h，已按此前窗口通知，不重推。
- **pillowbook-rh**（@pillowbookRH）：MUST1 本 1h 官方窗无该号新帖。开窗仍为 2026-11-16 01:00 CST，约 4.3h，尚未进入 ≤2h，不重推。
- **qtronlaptops**：MUST1 本 1h 官方窗无该号新帖。第二批窗口仍为 2026-11-16 01:00 CST（5pm UTC），尚未 ≤2h，不重推。
- **MicroFrens**：MUST1 本 1h 官方窗无该号新帖。对公 FCFS 已结束，持有者 OG FREE 仍在进行（R1860 已首次确认并推送），无新的对公窗口或份额规则变化，不重推。
- **Gloopix**（@Gloopix_）：MUST1 仍可见 19:44 CST 合作征集/预告帖（R1867 已记），无开铸时间、无官网、无已核验 CA，不能写成免费 LIVE，也不是新的可操作窗口，不重推。
- **ozero**（@ozero_fun）：MUST1 本窗无新的可操作变化，不重推。
- **marketmugs**：UF2 有帖，尚无 mint 窗口，不是新卡，不推送。

## 关键词 / mentions 摘记

- 十栏均跑全。薄栏 KW_TAPE/DOGE 与核心栏 KW_MINT/PAD/GO/ELY 打满 25 条硬顶；KW_GIWA 13；KW_BTC 15；KW_SN 8；KW_LZ 7；KW_MINE 7。mentions：Tape 1、GIWA 0、BTC 0、Starknet+DogeEVM 0。
- mentions 各链按轮换同等覆盖，本轮未空转只扫单链。
- 发现不等于关注：本轮主栏盲捞独立抓到官号 @PlayBitsigil 的即将免费 WL 窗口（该卡 10-27 已在库但已过期且未挂 Watch）。
- 未送审（不收录）：**cubicle_hood** 称今日 Robinhood+OpenSea 免费 mint，仅来自第三方 RT @oxztd，无本轮官号核验，不收录；**DarkHorse Wallet $RGB** 免费 mint 已约 70%/10 万地址，非早期；**utsexchange** 仅 RT 提及 token sale；PlayPixelora / numencash / zerolotl / boxcars / seedborn / Spike__wtf 已在库。未为「再确认」额外刷 X。

## Watch 漏挂修复

- 面板在库但不在任何 Watch（12）：misthra、spirit-bomb、elysium-family、dataloomsol、shush-pit、quiversbs-rh、obxid-agent、homeiraxyz、squeekcrumb、agent-pioneer（补 handle @agentpioneer）、deadhood（本轮 MUST1 已扫但仍漏挂）、getelysiumpass → 已补进 userFollowWatch 及对应 elysiumWatch / miningWatch / freeMintWatch / agentPadWatch / bnAgentWatch。
- 在库 bitsigil（R655）不在任何 Watch → 已补进 userFollowWatch + freeMintWatch。
- candidateIds 补挂：loopiez（R1867 只写入 accounts）、umbrapad（UF accounts 有、cids 只有 umbra-perps；兼补 giwaWatch candidateIds）。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1868.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：Bitsigil 免费 WL mint ≤2h（未见 CA）；DualForge 官方已确认开闸（付费，需 .ai Agent ID）。本号不自动 mint。

## 未做 / 交接

- 未自动 mint（本号只雷达；打新仍交 BAW 打新号）。
- Discord Peek 未做（DC 不登录），discordPeekDeferred=true。dsFallback=false。
- search_users 仍不可用，静号只走 mentions。
- fat official nextStart 未推进（与上轮相同口径）；fatNextStarts 元数据保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- 下一轮 UF 从 0-based 599 thevoidling_rh 起。mentions 下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。silent 下一轮 Starknet（1869%11=10）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- DualForge 官方开闸 + 官网 + 公布 CA 已在本轮推送，后续不要重复「已开铸」提醒，除非出现改价、关窗、池已开、已核验 minted 或其它新的可操作变化。
- Bitsigil Firstbound 免费 WL 21:00 CST 已按 ≤2h 推送；若后续官方公布 mint 链接 / CA、关窗或阶段变化再判断是否重推，不要只因同一 21:00 窗口每轮重推。
- osk-agent 池已开事件已在 R1863 推送并写入已核验 CA，后续不要重复「池已开」提醒，除非出现新的可操作变化。
- MicroFrens 持有者免费阶段已在 R1860 按首次确认进行中推送，后续不要每轮重复，除非出现关窗、新阶段或份额规则变化。
- hokiseries 公售官方结束时钟 20:00 CST 已过且无新阶段官宣，已在 R1815 写明结束时间，不重推；若官方宣布新阶段再判断。
- qtronlaptops / pillowbook-rh 同一 2026-11-16 01:00 CST 前后窗口，POLYROB 关窗 01:12 CST，均尚未进入 ≤2h，进入后再判断是否首次推送。
- jacketagent 免费 LIVE 至 11-16 00:00 CST，进入 ≤2h 后再判断。
- bamboo-ronin 不得在后续轮次仅凭 bio 写成免费 LIVE；需官网、官方开窗帖或 CA 之一确认。
- panko 不得把站点「Your first pet is free / Soon on Robinhood Chain」写成已核验免费 LIVE；需官方开窗或可核验 mint 入口。
- loopiez 不得把官帖「FREE MINT | 1111 LOOPIEZ | DROP EVM」写成已核验免费 LIVE；需官网、官方开窗或可核验 mint 入口。
- kinetiq-toons 已在 R1865 DS skip（WL 已关、mint TBA）；若后续官宣开铸/免费 LIVE 再核收录。
- framble 已在 R1866 DS skip（无官网、无 CA）；若官网或链上证据出现再核收录。
- Matrix Agents 无官推，后续轮次靠链上/官网跟进度，不要为「再确认官号」额外刷 X。
- Gloopix 预告/合作征集口径不要写成免费 LIVE 或当作新窗口重推。
- cubicle_hood 仅第三方 RT，未收录；不要为再确认额外刷 X，除非出现官号或官网证据。
