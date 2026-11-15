# RESULT R1843（独立例行 pace · 08:00 CST 后首轮全量补扫）

时间：2026-11-15 约 08:09 CST。mode=post-reset-full。Discord 未占本轮（R1834 为 03:58 CST 的 Discord 补漏，已收录 elysiasealed / sifrswap / volume-live 并通知，不重推；R1835–R1842 为 04:12 / 04:38 / 05:09 / 05:40 / 06:10 / 06:38 / 07:06 / 07:35 CST 独立例行 pace，R1839 新收 radiance-meme 已通知不重推）。notify=false。未自动 mint。dsFallback=false。discordPeekDeferred=true（按惯例 DC 不登录）。本轮新收录 0 个。这是 08:00 CST 额度重置后第一轮全量补扫（不得连续再跑第二次 post-reset-full）。

## 额度与覆盖

- xReads 32（main 30 + silent 1 + admitVerify 1），remainingBefore 1000 → remaining 968/1000。开跑时 `x_budget.py` 仍读到 data.json 里过期的 remaining=28；08:00:24 CST 用 UF1 实查页脚为 999 of 1000 today，确认已重置，remainingBefore=1000，模式改为 post-reset-full（softCap 50，minSpend 24，silentCap 2，ufAccountShard=80）。main 30 已过 minSpend 24、未超 softCap 50。
- 分解：UF 4 个 from: 批次；MUST 3 个 from: 批次（radiance_meme 单独成 MUST1，25 条硬顶不翻页；tmachinroBot 已在 UF，MUST 去重；PlayPixelora 本轮落在 UF 分片，MUST 去重）；THIN 官号 4 批次；薄栏独立 KW×6 + 核心栏 KW×5；mentions 8 道全链；silent mentions×1；admitVerify get_users_by_username(@muchfi_xyz)×1。同一 handle 本轮只拉一次，无 next_token 翻页。
- UF / MUST / THIN start_time=2026-11-14T23:00:00Z（约 1h 官方窗）。薄栏 KW 与 mentions start=2026-11-14T22:00:00Z。核心栏 KW start=2026-11-14T19:00:00Z（补 R1833 之后因额度紧而延后的核心栏）。silent start=2026-11-14T00:00:00Z。search_posts_all 的 max_results 实际硬顶 25。search_users 仍不在 X 工具目录。
- lastFullAfterReset 现为 **R1843**。laneReads：十栏独立/核心 KW 全部为 true（BN Agent 钱包经 MEN_BN + 台子 KW / UF 优先号覆盖）。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- UF 库表 walk 从 cursor 1059 之后（1060）起 kept 80 skip 2 已知 NF（ePegsV4、Haltercard），last kept 1141，next start 1142，未回绕。优先软刷 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets 折入 UF1（R1103 名单曾误标 PulseLaunchpad / machinedotfun 为 NF，已按近轮存活恢复进优先折入，不推进 cursor）；starx_xlayer / mobster_meme 为历史 NF，本轮不重查（prioritySkippedNF）。UF1 0 帖；UF2 1 帖 @OakAgentKit；UF3 0 帖；UF4 2 帖 @LetheansNFT / @qHooks_。
- mentions 本轮全量：LayerZero 1 / Elysium+kinetiq 17 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 0 / Tape 1 / GIWA 0 / BTC 0 / Starknet+DogeEVM 2。下轮轮换子集：Tape / GIWA / BTC / Starknet+DogeEVM。
- silent 栏 1843%11=6 → Tape/电路；search_users 不可用，只走 mentions，ran=true，25 条硬顶，无新号送审。silentCap=2 用 1。
- Watch：round≥1790 卡均已在至少一个 Watch，本轮 0 漏挂。无新卡。软债 canton/glaze/tokenWorks/flap lastChecked 刷到本轮完成时点（2026-11-15 08:09 CST）。
- THIN 官号 4 批次去重后 97 个 handle，1h 官方窗内 0 帖（页脚额度正常，非接口失败）。

## 本轮收录

无。预拒在库进度与重叠旧帖（polyrob 一口价仍开放、jacketagent 免费进度仍 147/500、ElysiaSealed 的 PONSVISION/VEKTA 成交播报、radiance 仍 coming soon 回复），不送 DS。

@muchfi_xyz（DogeOS 测试网 DeFi，CLMM+CLOB / $MUCH）不在库、不在任何 Watch。admitVerify：2025-09-05 开号，粉 25562，24 帖，简介 “Much Yield, Much Wow, only on @DogeOS”，无官网。仅见第三方喊单、未见本轮官方 from: 窗。偏成熟、不够早期，未送 DeepSeek，不收录。RESULT 记见，不建卡。

HoodedLegends / CATPADSOL / avadaq_AVAX / Printer_Launch 等为第三方抽奖或其它链已上线台子噪音，未送审。

无候选送 DeepSeek。未收录。

## 在库进度（不重推）

- polyrob：本窗再见到官号 @tmachinroBot 同一条一口价公开铸造仍开放帖，closes Sun 17:12 UTC（2026-11-16 01:12 CST，约 17h，非 ≤2h）。已按 R1816/R1821/R1827/R1833 通知，不重推。
- jacketagent：本窗再见同一条 147/500 免费铸造进度帖，免费阶段仍至 11-16 00:00 CST（约 16h，非 ≤2h）。已是在库免费 LIVE，非首次窗口，不重推。
- elysiasealed：官号 07:48 CST 报 PONSVISION 近 24h 717 笔、创建税 3%、顶持仓 9.85%、未毕业；07:18 CST VEKTA 1128 笔为 R1842 已见。该 live 窗口已在 R1834 收录并通知，不重推。
- radiance-meme：本窗大量回复仍是 very soon / sunrise / the last 13% is where we launch，无窗口。已在 R1839 通知，不重推。MUST1 单独查询，25 条硬顶不翻页。
- tinylegends-io：**补记漏因**。关键词补扫经第三方 RT 见到官帖 2026-11-13 20:00:05 CST「THE MINT IS LIVE!」（id 2121211497816973363，Founders 1111 / OpenSea，GTD→FCFS→public）。该官帖恰落在此前第三方所称的 20:00 CST 窗口，R1792/R1793 因 MUST 近窗未见官帖而写成未确认。现距官帖已约 36–48h，无法确认仍开放，不改 LIVE、不算 ≤2h、不预推。已在 userFollowWatch + freeMintWatch。
- hood-bitz：官号 04:15 CST 宣布 BITBOTZ minting Monday（2026-11-16），曾被下架的 HoodBitz 持有人可免费铸造。周一窗口尚未 ≤2h，不预推。
- play-pixelora：关键词见到对旧官帖的转发（白名单 2026-11-07、utility 文案 2026-11-13）；本轮官方 from: 窗无新官帖，不改 LIVE、不预推。
- letheans-nft：官号 00:01 CST 公布 GTD 中奖地址，无新的首次 mint 窗口，不推。
- qhooks / oak-agent-kit / ballers：进度或 building 动态，无 mint/开窗，不推。
- laika-doge：第三方转发称 GovernOS 已在 DogeOS testnet 经 Laika Super App 上线；卡已是 testnet LIVE，不新开窗口、不预推。
- ember-pow：本窗无官帖（每日免费 wood 08:00 CST 重置今日已到，但未见新官推）。已在 R1811 通知，不重推。
- baglings / burybud / fused-ai / meow-cards / 0pad / hoodnutts / cashed / giwagmi / shinob-rh / forgepass-bnb / sifrswap / volume-live / dogstarter / tapemine / shillscope / kycabal / coinfin / madang-fun / punchin / dusktape：MUST/进度窗无新的首次可操作窗口，不重推。

## 关键词 / mentions 摘记

- 薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）与核心栏 5 条 KW 本轮均已跑全。核心栏自约 R1833 起因 remaining<200 连续延后，本轮用 19:00Z 起点做补扫。
- mentions 八道全链一次补齐，见上表。命中多为已在库官号播报或第三方挂靠，无新号过筛。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1843.md`。面板 https://reboot7454.github.io/early-scout/
- notify=false：无真新收录，无未告知的 ≤2h 首次可操作窗口，无新的免费 LIVE / 免费 mint。tinylegends 官帖为 48h 前漏记，只补卡不推。

## 未做 / 交接

- 未自动 mint。本轮 0 个候选送 DeepSeek，dsFallback=false。
- search_users 仍不可用；silent 已用 mentions 路径跑完 Tape/电路。
- lastFullAfterReset=R1843。**此后恢复正常节流，不得连续再跑第二次 post-reset-full。** 下轮按当时 remaining 选 pace/tight 等（预计仍 ample/pace）。UF cursor=1141（下一 walk 从 1142 起）。mentionsNext=Tape / GIWA / BTC / Starknet+DogeEVM。fat 分片起点未变。BITBOTZ Monday 窗口待临近 ≤2h 再报。
