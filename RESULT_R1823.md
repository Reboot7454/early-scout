# RESULT R1823（独立例行 pace）

时间：2026-11-14 23:43 CST。mode=pace。Discord 未占轮。notify=true（giphyfun 官方 $GIPHY CA 落地；meow-cards $MEOW 预售与早鸟免费领取 LIVE。无新收录。push 见提交记录）。未自动 mint。dsFallback=false。discordPeekDeferred=true（本轮为例行 pace X，按惯例 DC 不登录，未做 Discord peek）。

## 额度与覆盖

- xReads 20（main 19 + silent 1 + admitVerify 0），remainingBefore 348 → remaining 328/1000。开跑 `x_budget.py` 曾报 remaining 388、softCap 24、minSpend 18、silentCap 2；但首读工具回包即为 347/1000，以工具回包为准记 remainingBefore=348。因 remaining ≫200，按用户「额度够时十栏跑全」把核心栏 KW 从 alloc 3 补到 5（计划主读 19，实际主读 19）。无 recover。
- 分解：UF shard×2 + MUST×2 + 薄栏 KW×6 + 核心栏 KW×5 + mentions×4 + silent×1。官网 / HTTP / 链外只读无 X 成本。同一 handle 本轮只拉一次，未为再确认重读。write_to_file 对部分 UF/薄栏/核心栏 KW / MEN_ELY 结果截断，已从截稿前的最新帖提取信号；未因此重拉同一查询。
- UF / silent start_time=2026-11-13T15:30:00Z；MUST / 关键词 / mentions start_time=2026-11-14T15:00:00Z。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。search_users 本轮仍不在 X 工具目录，silent 仅 mention 路径。
- lastFullAfterReset 仍为 R1792。十栏关键词已跑全（KW_LZ 1、KW_TAPE 22、KW_GIWA 21、KW_DOGE 21、KW_BTC 4、KW_SN 25、KW_MINT 25、KW_MINE 17、KW_PAD 25、KW_GO 25、KW_ELY 25）。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。未刷薄栏官号 from: 与四表 FAT 分片。
- UF 91→144 kept 48 skip 5（片内已知 NF：pearsdotfamily / battle_pad / cabaldotfun / project_hoodmon / elysiumpepecoin），无 wrap。NutshellMarkets 已在本片；另把 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / starx_xlayer 折进 UF1，不推进 cursor。下一起点 cursor=144。UF accounts 仍 1781。
- mentions 轮换本轮：LZ / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX（补 R1822 已扫的 Tape / GIWA / BTC / Starknet+DogeEVM）。MEN_LZ 3、MEN_ELY 11、MEN_MINE 0、MEN_BN 1。
- silent 栏 1823%11=8 → DogeEVM；search_users 仍不在工具目录，仅 mentions。hits 3，sentToReview=0，admitted=0（DogeOS 主网临近与 Daejin 积分活动闲聊）。
- Watch 漏挂：round≥1790 的在库卡均已在至少一个 Watch（handle 或 id 交集）。未把大量历史无 Watch 旧卡当作本轮漏挂补挂。软债 canton/glaze/tokenWorks/flap lastChecked 刷到 23:43 CST。

## 本轮新收录

- 例行 pace 无新收录。上一轮 NTR 已为空，本轮无待清新卡。

## 首次紧窗口 / ≤2h / 已落地 CA

- giphyfun：官帖 23:00:09 CST 宣布 $GIPHY 已在 Robinhood Chain / Pons 交易。官方 CA 0xafA7D9D246Cae5e69daF5092d11cc6a21BcF5e5a，购买页 https://ponsfamily.com/launchpad/0xafA7D9D246Cae5e69daF5092d11cc6a21BcF5e5a。核验时 DexScreener 暂无该 CA 交易对；发射台 giphy.fun/launch 仍 HTTP 200、需 access code。R1822 只记到发射台上线与 First 999 drop addy，未写入代币 CA，本轮按 CA 落地提醒。
- meow-cards：官帖 23:13–23:35 CST 宣布 $MEOW 预售 LIVE，且预售前已铸卡可免费领 50,000 $MEOW/张。此前预售页合约调用失败、首页写 no presale。本轮发射合约 0x6140ACbc2E363B2deb4A3aB59c4A121583fD479C 已有代码且 paused=false：1 份=0.001 BNB=500,000 $MEOW，上限 1000、每钱包最多 10、满 500 开 LP；链上 paidShares=0 / paidRemaining=1000，deadline=11-21 16:45:53 CST，lpCreated=false，claimMaxTokenId=1297，totalClaimed=0。$MEOW 代币 CA 0x013e7cd09d7afb06ceddab2aa95a36681c535b23（已有代码）。NFT 仍 LIVE，totalSupply=1337/10000。已按 R1816 提醒免费首铸，本轮按预售/免费领/代币 CA 落地再提醒。
- 当前仍在 ≤2h、此前已通知、本轮不重推：
  - jacketagent：官网 200，页面仍 0/500、0/15,000。BNB Chain status()：phase=0，minted=0，freeRemaining=500，paidRemaining=15000；开售仍 11-15 00:00:34 CST（约 0.3h），发售尚未打开。官帖 23:30 CST 称倒计时 30 分钟。已按 R1820 首次 ≤2h 通知。
  - dusktape：$LULL 仍 11-15 00:00 CST（约 0.3h）。本 MUST 窗无新官帖。官网 dusktape.live 本轮 TLS 再次失败。不是免费 NFT。已按 R1820 首次 ≤2h 通知。
  - shinob-rh：时钟仍 11-15 01:00 CST（约 1.3h），官网 shinobrh.art 200、Whitelist 仍开、mint 倒计时仍为占位、铸造未开。已按 R1822 首次 ≤2h 通知。

## 已在库进度（不重推）

- punchin：BSC Pass 合约 totalSupply=92（上一轮记录 57/500），免费窗口仍 LIVE。已按 R1815 通知，不按进度重推。
- hotpad：官帖解释 $HOT 创建者奖励用于运营、平台刚上线约两小时，未见新发射或官方代币 CA。不重推。
- burybud / ape-city：本 MUST 窗无新官帖，官方 CA 未改，DexScreener 仍无对。已按既有 CA 落地通知，不重推。
- agent-cat / omenpad / plumbers-plungers / anvil-nft / crimson / baglings / polyrob：本 MUST 窗无新官帖或新的开窗/CA 事实，已通知的不重推。
- microfrens：关键词命中转发「OG Free Mint is LIVE! 2 Hour Window」，短链指向 OpenSea 收藏页且写 Minting now / Ethereum。本轮未 MUST 直拉官号，无法核验是否确为免费 OG 窗（R1815 记 paid mint 0.0015 ETH），不按免费 LIVE 重推。

## 跳过

- KW_MINT 多为已有项目的 GTD/免费名额转发（ITIA / Agentlifebnb / HoodNFTz2 / MendlingsNFT / BitMinersonRH / MicroFrens 转发）。
- KW_GO 多为 SpaceX/车展等无关噪音；KW_SN 多为 Bramble Hexwood 挑战转发；KW_DOGE 多为 DogeOS 测试网/主网临近闲聊；KW_TAPE 多为 BEM×TapeOut 宣传转发；KW_PAD 多为已有 ononepad / Flap 新闻与无关 bonding 噪音。
- MEN_ELY 多为 Hypesium / Enter_Elysium 闲聊；MEN_MINE 0 命中；MEN_BN 1 条非新项目。
- 未把 search_users 不可用时的静号路径扩成探索性重读。

面板：https://reboot7454.github.io/early-scout/
