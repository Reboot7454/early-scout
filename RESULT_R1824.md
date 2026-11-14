# RESULT R1824（独立例行 pace）

时间：2026-11-15 00:12 CST。mode=pace。Discord 未占轮。notify=true（jacketagent 免费 mint LIVE，phase=1 minted=30/500；dusktape $LULL 官方 CA 落地 Pons。无新收录。push 见提交记录）。未自动 mint。dsFallback=false。discordPeekDeferred=true（本轮为例行 pace X，按惯例 DC 不登录，未做 Discord peek）。

## 额度与覆盖

- xReads 20（main 19 + silent 1 + admitVerify 0），remainingBefore 328 → remaining 308/1000。开跑 `x_budget.py` 曾报 remaining 388、softCap 20、minSpend 18、silentCap 2；但首读工具回包即为 327/1000，以工具回包为准记 remainingBefore=328。因 remaining ≫200，十栏关键词跑全。无 recover。
- 分解：UF shard×2 + MUST×2 + 薄栏 KW×6 + 核心栏 KW×5 + mentions×4 + silent×1。官网 / HTTP / 链外只读无 X 成本。同一 handle 本轮只拉一次，未为再确认重读。write_to_file 对部分 UF/KW 结果截断，已从截稿前最新帖提取信号；未因此重拉同一查询。
- UF / silent start_time=2026-11-13T16:00:00Z；MUST / 关键词 / mentions start_time=2026-11-14T15:30:00Z。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。search_users 本轮仍不在 X 工具目录，silent 仅 mention 路径。
- lastFullAfterReset 仍为 R1792。十栏关键词已跑全（KW_LZ 1、KW_TAPE 25、KW_GIWA 20、KW_DOGE 21、KW_BTC 3、KW_SN 25、KW_MINT 25、KW_MINE 10、KW_PAD 25、KW_GO 25、KW_ELY 25）。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。未刷薄栏官号 from: 与四表 FAT 分片。
- UF 144→204 kept 48 skip 12（片内及补位段已知 NF：starx_xlayer / GatorEyesSolada / _pointzz / keyhasp / Arcdepthoock / vaultdock / cloakcapitalai / kuranto_rh / arka_fun / AGENTICABOT / HashOre_BNB / usejackbay），无 wrap。优先号均不在可读片内；另把 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets 折进 UF1，不推进 cursor。starx_xlayer 与 mobster_meme 已在 NF_skip，本轮未查询、未连刷。下一起点 cursor=204。UF accounts 仍 1781。
- mentions 轮换本轮：Tape / GIWA / BTC / Starknet+DogeEVM（补 R1823 已扫的 LZ / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX）。MEN_TAPE 0、MEN_GIWA 3、MEN_BTC 0、MEN_SN_DOGE 0。
- silent 栏 1824%11=9 → BTC；search_users 仍不在工具目录，仅 mentions。hits 25，sentToReview=0，admitted=0（Bitcoin 生态新闻与 ShieldedNaka / Ordinals 闲聊）。
- Watch 漏挂：round≥1790 的在库卡均已在至少一个 Watch（handle 或 id 交集）。未把大量历史无 Watch 旧卡当作本轮漏挂补挂。软债 canton/glaze/tokenWorks/flapPadWatch lastChecked 刷到 00:12 CST。

## 本轮新收录

- 例行 pace 无新收录。上一轮 NTR 已为空，本轮无待清新卡。

## 首次紧窗口 / ≤2h / 已落地 CA

- jacketagent：官帖 00:03:50 CST（https://x.com/jacketagent/status/2121635225977671938）宣布 JACKETAGENT Free Mint is LIVE。官网 jacketagent.pages.dev 仍 HTTP 200。BNB Chain status() 约 00:11 CST：phase=1（R1823 仍为 0），minted=30，freeRemaining=470，paidRemaining=15000（付费尚未开始）。免费 500 份、每个 Agent ID 限 1 份，手续费 0.0001 BNB；免费阶段至 11-16 00:00:34 CST 或名额用尽。付费 15,000 份、0.003 BNB、每 ID 最多 10 张。NFT CA 0x70FdD1a7f382893708d00fC2eF9C38cAe7DEC92B。R1820 仅按首次 ≤2h（当时 phase=0 发售未开）通知过，本轮按免费 LIVE 硬规则再提醒。
- dusktape：官帖 00:00:17 CST（https://x.com/dusktape/status/2121634331076784569）宣布 $LULL 已在 Robinhood Chain / Pons 交易。官方 CA 0x7CB1D940aaFE0912f000582A96a08BC99e2a0934，购买页 https://ponsfamily.com/launchpad/0x7CB1D940aaFE0912f000582A96a08BC99e2a0934。同一 CA 亦写入官网 dusktape.live/config.js；Buy on Pons 已启用。核验时 DexScreener 暂无该 CA 交易对。官网 TLS 仍不稳定。不是免费 NFT。LullLedger（评分合约，非代币）仍为 0x5eeAF93840D7fED94A9f2e5322Aeed3965Bd6F12。R1820 仅按首次 ≤2h（当时尚未公布 CA）通知过，本轮按官方 CA 落地再提醒。
- 当前仍在 ≤2h、此前已通知、本轮不重推：
  - shinob-rh：时钟仍 11-15 01:00 CST（约 0.8h），官网 shinobrh.art 200、Whitelist 仍开、mint 倒计时仍为占位、铸造未开。本 MUST 窗无新官帖改时钟。已按 R1822 首次 ≤2h 通知。

## 已在库进度（不重推）

- punchin：BSC Pass 合约 totalSupply=96（上一轮记录 92/500），免费窗口仍 LIVE。已按 R1815 通知，不按进度重推。
- meow-cards：官帖 00:00:47 CST 复述 $MEOW 预售还剩 6 天，规则未改。链上 NFT totalSupply=1339/10000（上一轮 1337），paidShares=0 / paidRemaining=1000，totalClaimed=0，paused=false。已按 R1823 提醒预售/免费领/代币 CA 落地，不重推。
- hotpad：官帖 23:47:26 CST 仅发 Engineering Launch Day 海报，未见新发射或官方代币 CA。不重推。
- giphyfun / burybud / ape-city：本 MUST 窗无新官帖，官方 CA 未改，DexScreener 仍无对。已按既有 CA 落地通知，不重推。
- agent-cat / omenpad / plumbers-plungers / anvil-nft / crimson / baglings / polyrob：本 MUST 窗无新官帖或新的开窗/CA 事实，已通知的不重推。

## 跳过

- Lobynfi / @Lobynfi：2026-11-14 新建、9 粉 10 帖，官网 lobynfi.xyz HTTP 200，Solana pump.fun CA GdVKRE9Aw9NLgN6hRzjev5sL88xs9xdcaMwZ5hEGpump 已有交易对，核验时 DexScreener 价约 $0.000002431、FDV 约 $2,432。已是极低市值在交易 meme，不是免费 mint / 公平发射窗口，本轮不收录。
- KW_MINT 多为已有项目或无关免费/预售转发；KW_GO 多为 SpaceX / 车展等无关噪音；KW_SN 多为 Bramble / Starknet 闲聊转发；KW_DOGE 多为 DogeOS 生态闲聊；KW_TAPE 多为已有 Tape / BEM 宣传；KW_PAD 多为已有发射台与 bonding 噪音；KW_ELY 多为已在库生态转发。
- MEN_GIWA 3 条为 Ammora 挂靠刷屏，非新项目；MEN_TAPE / MEN_BTC / MEN_SN_DOGE 无有效新号。
- 未把 search_users 不可用时的静号路径扩成探索性重读。

面板：https://reboot7454.github.io/early-scout/
