# RESULT R1822（独立例行 pace）

时间：2026-11-14 23:12 CST。mode=pace。Discord 未占轮。notify=true（burybud 官方 $BURY CA 落地；shinob-rh 首次进入 ≤2h。无新收录。push 见提交记录）。未自动 mint。dsFallback=false。discordPeekDeferred=true（本轮为例行 pace X，按惯例 DC 不登录，未做 Discord peek）。

## 额度与覆盖

- xReads 20（main 19 + silent 1 + admitVerify 0），remainingBefore 368 → remaining 348/1000。开跑模式 pace（softCap 22，minSpend 18，silentCap 2）。因 remaining 368≫200，按用户「额度够时十栏跑全」把核心栏 KW 从 alloc 3 补到 5（计划主读 19，实际主读 19）。无 recover。
- 分解：UF shard×2 + MUST×2 + 薄栏 KW×6 + 核心栏 KW×5 + mentions×4 + silent×1。官网 / HTTP / 链外只读无 X 成本。同一 handle 本轮只拉一次，未为再确认重读。write_to_file 对部分 UF/薄栏/核心栏 KW 结果截断，已从截稿前的最新帖提取信号；未因此重拉同一查询。
- UF / silent start_time=2026-11-13T15:00:00Z；MUST / 关键词 / mentions start_time=2026-11-14T14:30:00Z。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。search_users 本轮仍不在 X 工具目录，silent 仅 mention 路径。
- lastFullAfterReset 仍为 R1792。十栏关键词已跑全（KW_LZ 3、KW_TAPE 25、KW_GIWA 22、KW_DOGE 18、KW_BTC 2、KW_SN 25、KW_MINT 25、KW_MINE 2、KW_PAD 25、KW_GO 25、KW_ELY 25）。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。未刷薄栏官号 from: 与四表 FAT 分片。
- UF 38→91 kept 48 skip 5（片内已知 NF：ElysiumOutlaws / deadpacksol / blindfloor / blobsdotmeme / trytoprint），无 wrap。优先号 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom 已在本片；另把 NutshellMarkets + starx_xlayer 折进 UF1，不推进 cursor。下一起点 cursor=91。UF accounts 1780→1781（追加 @giphydotfun）。
- mentions 轮换本轮：Tape / GIWA / BTC / Starknet+DogeEVM（补 R1821 已扫的 LZ / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX）。MEN_TAPE 1、MEN_GIWA 1、MEN_BTC 0、MEN_SN_DOGE 0。
- silent 栏 1822%11=7 → GIWA；search_users 仍不在工具目录，仅 mentions。hits 25，sentToReview=0，admitted=0（多为 GIWA 测试网数据闲聊与已有 Ammora/官号挂靠）。
- Watch 漏挂：round≥1790 的在库卡均已在至少一个 Watch（handle 或 id 交集）。未把大量历史无 Watch 旧卡当作本轮漏挂补挂。软债 canton/glaze/tokenWorks/flap lastChecked 刷到 23:12 CST。

## 本轮新收录

- 例行 pace 无新收录。上一轮 NTR 在 R1821 已清空，本轮无待清新卡。

## 首次紧窗口 / ≤2h / 已落地 CA

- burybud：官帖 23:00:15–23:05:50 CST 宣布 $BURY 已在 Pons（Robinhood Chain）交易。官方 CA 0xb1F1502800802a96b245e32cd10282f377C97676，购买页 https://ponsfamily.com/launchpad/0xb1F1502800802a96b245e32cd10282f377C97676。花园/锁仓合约仍为 0xC5476b293f7825f88301683D480c485bfbE7662d，不是代币 CA。核验时 DexScreener 暂无该 CA 交易对；官网 burybud.xyz TLS 仍失败。已按 R1818 首次 ≤2h 通知档期，本轮按 CA 落地再提醒。
- shinob-rh：首次进入 ≤2h。时钟仍 11-15 01:00 CST（约 1.8h），官网 shinobrh.art 200、Whitelist 仍开、mint 入口仍隐藏、铸造未开。已按 R1808 作为新收录通知，本轮按首次 ≤2h 再提醒。
- 当前仍在 ≤2h、此前已通知、本轮不重推：
  - jacketagent：官网 200，页面仍 0/500、0/15,000。BNB Chain status()：phase=0，minted=0，freeRemaining=500，paidRemaining=15000；开售仍 11-15 00:00:34 CST（约 0.8h），发售尚未打开。官帖 23:01 CST 称倒计时 1 小时。已按 R1820 首次 ≤2h 通知。
  - dusktape：$LULL 仍 11-15 00:00 CST（约 0.8h）。本 MUST 窗无新官帖。官网 dusktape.live 本轮 TLS 恢复（HTTP 200），倒计时仍指向 14 NOV 16:00 UTC。不是免费 NFT。已按 R1820 首次 ≤2h 通知。

## 已在库进度（不重推）

- giphyfun：关键词命中现用官号 @giphydotfun 称 launchpad is live、First 999 drop addy。官网 giphy.fun/launch 200，Zero cost to launch，Live on Pons · Robinhood Chain，需 access code。与库内 @giphyfun 为同一项目，已改记官号并追加进 UF，不另建卡、不按新收录重推。
- punchin：BSC Pass 合约 totalSupply=57（上一轮记录 3/500），免费窗口仍 LIVE。已按 R1815 通知，不按进度重推。
- hotpad：官帖称 $HOT 质押页更新与约 100 万枚奖励，未见新发射或官方代币 CA。不重推。
- crimson：本窗再见 $CRMSN / Solana pump CA，与 R1821 已记相同，不重推。
- ape-city：官帖 22:41 CST 宣布社区转发比赛，官方 CA 未改。已按 R1820 通知 CA 落地，不重推。
- agent-cat / meow-cards / omenpad / elysium-pepes / plumbers-plungers / anvil-nft：本 MUST 窗无新官帖或新的开窗/CA 事实，已通知的不重推。

## 跳过

- giphydotfun：不是新项目，而是已在库 giphyfun 的现用官号，已并入原卡。
- pickhash_bnb / Dividendsarts / HoodNFTz2 / PlayPixelora / AmmoraHQ / numencash / PlunderPort / fruitfly_world / Hypesium：均已在库。
- seedhqx（自称在做 FUSE mint 终端）与 DegenCapitalVC（12/1 Based Mining Block Party）不是本轮可操作的早期发射/免费 mint，未送审、未建卡。
- KW_MINT 多为已有项目的 GTD/免费名额转发；KW_GO 多为 SpaceX/歌曲等无关噪音；KW_SN 多为 Bramble Hexwood 挑战转发；KW_DOGE 多为 DogeOS 测试网游戏分数。
- 未把 search_users 不可用时的静号路径扩成探索性重读。

面板：https://reboot7454.github.io/early-scout/
