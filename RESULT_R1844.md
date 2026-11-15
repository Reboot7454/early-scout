# RESULT R1844（独立例行 pace · ample）

时间：2026-11-15 约 08:38 CST。mode=ample。Discord 未占本轮（R1834 为 03:58 CST 的 Discord 补漏，已收录 elysiasealed / sifrswap / volume-live 并通知，不重推；R1835–R1842 为 04:12 / 04:38 / 05:09 / 05:40 / 06:10 / 06:38 / 07:06 / 07:35 CST 独立例行 pace，R1839 新收 radiance-meme 已通知不重推；R1843 为 08:09 CST 的 08:00 后首轮全量补扫，0 新收）。notify=true（真新收录 umbrapad）。未自动 mint。dsFallback=false。discordPeekDeferred=true（按惯例 DC 不登录）。本轮新收录 1 个：umbrapad。lastFullAfterReset 仍为 R1843，本轮按 ample 正常节流，不是第二次 post-reset-full。

## 额度与覆盖

- xReads 26（main 25 + silent 1 + admitVerify 0），remainingBefore 968 → remaining 942/1000。开跑 `x_budget.py` 读到 968，mode=ample（softCap 28，minSpend 20，silentCap 2，ufAccountShard=50）。UF1 页脚确认 967 of 1000（即 remainingBefore=968）。main 25 已过 minSpend 20、未超 softCap 28。
- 分解：UF 3 个 from: 批次；MUST 3 个 from: 批次（radiance_meme 单独成 MUST1；LaikaSuperApp 因字数落到 MUST3）；THIN 官号 4 批次；薄栏独立 KW×6 + 核心栏 KW×5；mentions 4 道轮换链；silent mentions×1。同一 handle 本轮只拉一次，无 next_token 翻页。umbrapad 的用户资料已在 MEN_GIWA includes 拿到，未再 get_users 重拉。
- UF / MUST / THIN start_time=2026-11-14T23:30:00Z（约 1h 官方窗）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-14T22:30:00Z（约 2h）。silent start=2026-11-14T00:32:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。search_users 仍不在 X 工具目录。部分关键词/静号结果 write_to_file 在约 6.3KB 处截断，已从截稿前最新帖提取信号，未因此重拉同一查询。
- lastFullAfterReset 保持 **R1843**。laneReads：十栏独立/核心 KW 全部为 true（BN Agent 钱包经核心栏 PAD KW / UF 优先号覆盖）。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- UF 库表 walk 从 1143 起（R1843 的 UF4 已包含 1142 XypherOnRH，为避免紧挨着重查而从 1143 FletchAgent 起算）。kept 50 skip 0，last kept 1192 PepeAgentbnb，next start 1193，未回绕。优先软刷 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets 折入 UF1（不推进 cursor）；starx_xlayer / mobster_meme 为历史 NF，本轮不重查（prioritySkippedNF）。UF1 0 帖；UF2 2 帖 @escape_hub（问候/互动，无开窗）；UF3 6 帖 @anipalsonsol / @PairMineAI。
- mentions 本轮轮换：Tape 2 / GIWA 1 / BTC 0 / Starknet+DogeEVM 1。GIWA 命中新号 @umbrapad 官宣重启，已送 DeepSeek 并收录。下轮轮换子集：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent 栏 1844%11=7 → GIWA；search_users 不可用，只走 mentions，ran=true，25 条硬顶（结果截断），未见 0 帖新官号送审。silentCap=2 用 1。umbrapad 走的是官号 mentions 主路径，不计入 silent admitted。
- Watch：round≥1790 卡均已在至少一个 Watch，本轮 0 漏挂。新卡 @umbrapad 已进 userFollowWatch + giwaWatch。软债 canton/glaze/tokenWorks/flap lastChecked 刷到本轮完成时点（2026-11-15 08:38 CST）。

## 本轮收录

- **umbrapad**（@umbrapad，Umbra Pad）：官号 2026-11-04 05:24 CST 建立，未认证，235 粉、14 帖。官网 https://umbrapad.xyz/ HTTP 200，与 https://x.com/umbrapad 互链。官帖 08:22 CST 宣布重启，日期待公布；下一版拟做多链发射（不只 Robinhood），并称可能把主链迁到 @GIWA_by_Upbit。官网仍写 Robinhood Chain 隐私 bonding-curve 发射台，有 Create / Launches 页，但 Explore 404、无已上线 CA，页脚写未独立审计且 We'll launch。官方明确 Date announced soon，故 status=watching，不标 LIVE，非免费 mint、非 ≤2h。与库内 umbra-agents / umbra-inference / umbra-perps 不是同一项目。DeepSeek overall 58，台子/Meme，focus=false。已进 userFollowWatch + giwaWatch。真新收录，必须通知。未自动 mint。

预拒在库进度与噪音（polyrob / jacketagent 本 1h 官方窗未见新官帖、radiance 仍 coming soon 回复、ElysiaSealed 成交播报、zerolotl 主网将至介绍、Ammora Season 1 快照、anipals 的 AURA 11-20 预告、Hood_Bitz 互动、PayphoneNFT / onlystreetsfun / CATPADSOL 等已在库或已知噪音），不把已在库项目再送 DS。无其它候选过筛。

## 在库进度（不重推）

- radiance-meme：本窗仍大量回复 launch / sunrise / claimed 等 coming soon 口径，无窗口。已在 R1839 通知，不重推。MUST1 单独查询。
- elysiasealed：官号 08:19 CST 报 THRIVE 近 24h 555 笔、创建税 2%、顶持仓 1.36%、未毕业；PONSVISION 717 笔为 R1843 已见。该 live 窗口已在 R1834 收录并通知，不重推。
- zerolotl：官号 08:15 CST 再发介绍帖（Zero 主网上线在即、曲线发射台机制）。卡已是 watching，非 LIVE，无新的首次可操作窗口，不重推。
- ammora：官号 08:18 CST 宣布 Season 1 快照完成、结果即将可查。无 mint/开盘窗口，不重推。
- anipals：官号本窗称 AURA 将于 11-20 在 Solana 上线。约 5 天，非 ≤2h，不预推。
- hood-bitz：本窗仅互动回复；BITBOTZ Monday（2026-11-16）窗口尚未 ≤2h，不预推。
- polyrob / jacketagent / ember-pow / play-pixelora / tinylegends-io / coinfin / punchin / forgepass-bnb 等：本 1h 官方窗无新的首次可操作窗口，不重推。

## 关键词 / mentions 摘记

- 薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）与核心栏 5 条 KW 本轮均已跑全。核心栏挖矿查询本窗 0 命中。
- mentions 四道轮换链已扫。Tape 为既有矿池二期/社区晨报；GIWA 命中 @umbrapad 重启官宣；BTC 0；Starknet+DogeEVM 为第三方转述 Laika 既有产品点。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1844.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：真新收录 umbrapad。非免费 LIVE / 免费 mint，也无未告知的 ≤2h 首次窗口。

## 未做 / 交接

- 未自动 mint。本轮 1 个候选送 DeepSeek（umbrapad，admit overall 58），dsFallback=false。
- search_users 仍不可用；silent 已用 mentions 路径跑完 GIWA。
- lastFullAfterReset=R1843。UF cursor=1192（下一 walk 从 1193 起）。mentionsNext=LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。fat 分片起点未变。BITBOTZ Monday 窗口待临近 ≤2h 再报。
