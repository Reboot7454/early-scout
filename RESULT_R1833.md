# RESULT R1833（独立例行 pace）

时间：2026-11-15 约 03:40 CST。mode=tight。Discord 未占本轮（R1831 为 02:42 CST 的 Discord 补漏，0 新收、notify=false，不重推）。notify=true。未自动 mint。dsFallback=false。discordPeekDeferred=true（按惯例 DC 不登录）。本轮新收录 1 个：fused-ai（@FUSED_OFFICIALS）。

## 额度与覆盖

- xReads 18（main 17 + silent 1 + admitVerify 0），remainingBefore 179 → remaining 161/1000。UF1 后页脚 178 of 1000，故 remainingBefore=179（与 R1832 收工一致）。开跑模式 tight（softCap 12，minSpend 12，silentCap 1）。因 remaining 179<200，核心栏 KW 全部延后（alloc kwCore=0，含打新 mint）。六个薄栏独立 KW 仍全部跑到。为完成上轮交出的 mentions 轮换子集，并遵守「薄栏 Watch 每轮全读」，main 17 超 softCap 12（+5），未另开探索读。
- 分解：UF shard×2 + MUST×1 + 薄栏 Watch from:×4 + 薄栏 KW×6 + mentions×4 + silent×1。官网 / HTTP 只核验新候选 FUSED（fusedai.org 200，与官推互链）；未为再确认重读同一 handle。write_to_file 对 KW_TAPE / KW_GIWA / KW_DOGE / MEN_ELY / SILENT 截断，已从邻近完整工具回包恢复，未因此重拉同一查询。
- UF / MUST / 关键词 / mentions start_time=2026-11-14T18:45:00Z；薄栏 Watch from: start_time=2026-11-14T18:50:00Z；silent mention start_time=2026-11-13T19:30:00Z。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。search_users 本轮仍不在 X 工具目录，silent 仅 mention 路径。
- lastFullAfterReset 仍为 R1792。laneReads：LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet 独立 KW 均已跑到；打新 / 挖矿 / 台子/Meme / GO盘 / Elysium 核心栏 KW 延后。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。未刷四表 FAT 分片。
- UF 库表 walk 从 cursor 551 kept 48 skip 12 已知 NF（Volitionxyz / tollsfun / whackyrh / bibiainft / AgentBoss_AI / obolworld / Elysium_Rocks / agents_estates / ClassifiedMRNG / Villagers_RH / agentcityuk / MonsterRH_），next cursor 611，未回绕。优先软刷 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets 折入 UF1；starx_xlayer / mobster_meme 为历史 NF，本轮不重查（prioritySkippedNF）。分片溢出 UseHyperLiquid / dayzerodrop / 3f3rwefwf / usetagpay / agentsgofirst 与 MUST 窗官号合并，未开第三趟 UF 读。
- mentions 轮换本轮：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX（LZ 0、mining 0、BN 2 条为趋势聚合号；ELY 17 条中扫到新官号 @FUSED_OFFICIALS，其余为已有 sasa / Stoa / Metric / clanker 或 KOL 评论）。下轮轮换子集：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 栏 1833%11=7 → GIWA；search_users 仍不在工具目录，仅 mentions。hits 25，sentToReview=0（numencash/Ammora 口号、GIWA 测试网数据转述、已有项目闲聊）。admitted=0（FUSED 来自 MEN_ELY 而非 silent）。
- Watch：round≥1790 卡均已在至少一个 Watch，本轮 0 漏挂。新卡 fused-ai 已进 userFollowWatch + arcPadWatch。软债 canton/glaze/tokenWorks/flap lastChecked 刷到本轮完成时点。

## 本轮收录

- **fused-ai（@FUSED_OFFICIALS，台子/Meme，Arc/Robinhood 等，watching，overall 62，focus=false）**—官号 2026-09-17 20:21 CST 建立，未认证，168 粉 307 帖。官网 https://www.fusedai.org/ HTTP 200，与官推互链。定位为 AI 发币台（一条推文发一个代币）。官帖 03:17:32 CST 回复 @Enter_Elysium 称 live launch 已回，可在官网 stream；页面仍写 COMING SOON、FUSE trading is not yet available，发射计数为 0，未见已核验 CA。官网网络列表无 Elysium，不进 Elysium 栏。真新收录，notify=true。本号不自动 mint。

预拒个人/口号/RT/已有项目宣传（TapeOut 口号、numencash 666 lights、Ammora 等待名单、Bramble 猫头鹰/游戏名碰撞、GIWA 测试网数据转述、POLYROB/Meow/FORGE PASS 进度等），不送 DS。仅将 FUSED 送 DeepSeek admit。

## 在库进度（不重推）

- meow-cards：官帖 03:31:20 CST 再推 $MEOW 预售规则（0.001 BNB=500,000，满 500 份开 LP，上限 1000，未达标退款），未改期。已按 R1823/R1816 通知，不重推。
- forgepass-bnb：官帖 02:45:14 CST 再述付费 mint 3% 进分红池。免费 LIVE 已按 R1830 通知，不重推。
- polyrob：官帖再确认 0.033 ETH、无名单、每钱包不限量，至 2026-11-16 01:12 CST。已按 R1816/R1821/R1827 通知，不重推。
- giwagmi：官帖 03:09 CST 再介绍即将上线的 GIWA 发射台，仍 watching，不推。
- shinob-rh：仅回复加快铸完，无新的首次窗口，不重推。
- UnseenOrdo：仅第三方 @yixiualpha 转述白单已开，本窗无 @UnseenOrdo 官帖，不改 LIVE、不预推。
- coinfin / jacketagent / 0pad / play-pixelora / hoodnutts：MUST/薄栏窗无新的首次可操作窗口，不重推。

## 关键词 / mentions 摘记

- 薄栏 KW 已跑全。过滤：已在库 Ammora / numencash / giwagmi / TapeMine / DogeOS 生态小费与测试网转述；Starknet 栏含 Bramble 猫头鹰/独立游戏名碰撞；BTC 栏为已有项目 RT。
- mentions：本轮已扫 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；Tape / GIWA / BTC / Starknet+DogeEVM 按轮换留给下轮。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1833.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：真新收录 FUSED AI（@FUSED_OFFICIALS），watching / COMING SOON，无免费 LIVE 窗口，仍按真新规则提醒一次。

## 未做 / 交接

- 未自动 mint。DeepSeek 仅评审 FUSED（overall 62，admit watching）。
- search_users 仍不可用，silent 仅 mention。
- lastFullAfterReset 仍 R1792；下轮若 remaining 仍<200 保持 tight pacing，08:00 CST 后第一轮仍须全量补扫。
- 下轮 mentions 轮换：Tape / GIWA / BTC / Starknet+DogeEVM。UF cursor=611。silent 下轮 1834%11=8 → DogeEVM。
