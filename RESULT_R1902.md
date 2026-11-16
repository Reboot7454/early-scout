# RESULT R1902

- time: 2026-11-16 13:36 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 745 → 720 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: pingpay
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1901）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=745），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent Starknet 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=745。25 次读取后 remaining=720。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 688 fagent_ 起 packed 2 片 kept 52（26+26，略超 50 条分片提示，查询长度仍在 512 内），wrap=false，walkScanned 68。NF_skip 16，其中 1 个为本轮新写入（SolumMrkt）；其余 15 个已在列（lootbale / useapppayfun / CyclopesElysium / elyword_xyz / AgentFramlin404 / RedirectCash / kyte_market / vytraqfun / hyperlinkdotfun / HordeOnElysium / lazabitmeme / XiangHao91647 / BrokeNiggameme / bndoge_bn / Mintbncat_ai）。firstKept fagent_，lastKept fistagent_bnb。next 753 BrokeNiggameme（该号也在本轮 NF_skip，下轮将首个跳过）。
- MUST1：24 个 live/窗口号；MUST2：23 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + PlunderPort + PonkeAgent + KomaAgentID + pumptoksocial + pantheonperps + SYR0xyz + ZyroxRH + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 107 号 5 片全读（26+25+26+26+4）。UF1 / THIN1 / THIN2 / THIN4 / THIN5 / KW_LZ / MEN_MINE / SILENT_MEN 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T04:00:00Z（约 1.5h，与 R1901 official 03:30Z 窗口重叠）；KW 与 mentions 自 2026-11-16T03:30:00Z（约 2h）；silent 自 2026-11-15T05:26:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 11 / Elysium+kinetiq 14 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 1。
- silent：1902%11=10 Starknet。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（0 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 0，admitted 0。下一轮 lane=打新。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]（MUST2 / KW_TAPE / KW_GIWA / KW_DOGE / KW_MINT / KW_PAD / KW_ELY / MEN_LZ / MEN_ELY 预览曾截断，均已用 .full 还原）。

## 信号与结论

新录取 1 张（pingpay）。无 ≤2h 窗口。判断/文案走 DeepSeek，dsFallback=false。notify=true：真新收录（不是免费 mint / 免费登记）。已把 pingpay 写入 forcePanelIds 与 userFollowWatch。新卡 focus=false，lzVerified=false。round≥1840 的 leak 检查为 0。本轮无新的 Watch 漏挂修复。

- **pingpay**（真新，notify）：@usePingPay / PingPay（开号 2026-11-15T22:37:00Z = 2026-11-16 06:37 CST，粉 10，following 0，tweet_count=39，xUserId=2122095523515498496，未认证）。KW_PAD 命中。本轮 13:26 CST https://x.com/usePingPay/status/2122199548491686131 与 13:27 CST https://x.com/usePingPay/status/2122199883348156778 官帖介绍产品（13:27 帖正文在第 3 点处被截断，不补写未读到的后文）。官网 https://pingpay.fun/ 本轮 HTTP 200，title「PingPay · Ping a coin to anyone on X」：live 发射表单；回复指令 `@usePingPay $TICKER @handle`；付款指令 `@usePingPay pay @handle 0.5 SOL`；powered by X / pump.fun / fomo / Solana。官网脚本 `window.PP.ca` 写入 3cwB9HvoSkWSjvUarK6Z575yogYnSZXFzdvyxKj8pump，未做独立源码/审计核验。/api/config 200，siteFundBps=0、fund=null（不把这项写成已核验的零平台费）。/api/coins?limit=24 返回 6 枚 source=bot、launcher=usePingPay、kind=tag 的 live 币（JUSTDOIN / PRECIPICE / NOONEKNOWS / DOWNALOT / DEGENPOT / NODOOM，看起来像给知名账号打的示例发射）；官方 CA 不在这 6 枚之中，独立行情未再查。pump.fun 首页与币页本轮 Cloudflare 403，不能写成已打开 pump.fun 币页。DexScreener 有 Solana/pumpfun 池 https://dexscreener.com/solana/gjvoxjn14wjguywjqtdg2j1ycpeucq8zo5zpzm4kqkj4（pairAddress GJVoXjN14WJGUYWJQTDG2J1YcpeUCq8Zo5ZPzm4KQkJ4）：base 即官网 CA（PingPay/PingPay），报价币为 PAID（98kfF7rmsg1QDUEoCqNE7g7M1FdrTt92TEp2CLzypump）而非 SOL，不得写成 SOL 配对；priceUsd 0.000004560，priceNative 0.003235，liquidity=null（不编造流动性），fdv=marketCap=4560.75，vol.h24/h6/h1=12878.72，m5=3478.26，txns h24/h6/h1 235买/156卖，m5 70/49，priceChange h24/h6/h1=49.8、m5=-18.12，pairCreatedAt 2026-11-16 13:22 CST。未做持有人统计。/docs 与 /about 返回同一份 SPA。不是免费 mint。本号不自动 mint / 不自动买卖。
- **pumptok**（在库，不重推）：本窗继续四步发射教程，并再说将为 elgato 发测试代币；仍未见已核验 live coin，不重推。
- **paidtok**（在库，不重推）：本窗继续长期建设 / Video Coins / fee vault 说明，同一份已开 live 发射台，不重推。
- **creedo**（在库，不重推）：再次说明 Token Tools are live；R1885/R1901 已记录，不是第一次补出入口，不重推。
- **wrapped-eth**（在库，不重推）：本窗再述费率 1–10%、平台 30% / 创作者政策 70%。费率说明已在 R1900/R1901 记下。本轮未再探测 /claim，不得写成 claim 已开放。
- **zyro / syro**：同一份已提醒口径，不重推。SYRØ 本窗仍是 Base Sepolia 测试网 + 通往 FREE MINT whitelist 的路上，不要写成免费 mint LIVE。
- **tapeai**：本窗仅表情回复；BEM 预存仍是 2026-11-16 16:00 CST，距今约 2.4h，尚未 ≤2h，不重推。第三方「开始预存了」不能当作官方确认已开。
- **hyperolius**（R1901 已提醒）：本窗再次出现同一条 13:00 CST 官帖，不重推。
- **不重推**：tape-exit 同一份只读/备份退出界面；tapemine 无新 CA/开窗；sunfall-world Season 1 日记；hood-bitz 未改 11-17 时间表；hooja-fun 未见补公布 UNVAULT 时刻；microfrens / hokori-quantum / outriggerrh / archerswap-elysium / memeko 无新窗口。
- 尚未 ≤2h：Bombshell Cats AL 11-16 20:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST。
- 预拒 / skip：
  - AnFeng0858：TapeOut 布道者转发，R1901 已 skip，本窗仍无独立官号/站点。
  - Trovehaven / CompanionsWfit：已在库，本窗只是第三方模板，不新建卡。
  - KukiVerse3D：仅第三方转帖称 11-23 Robin Hood / OpenSea 免费 mint，未见已核验官号，不建卡。
  - Ammora / GIWA Season 2 祝贺回复号、bonding curve 讨论回复号：不是新项目官号。
  - thespotdotapp / davethespot：V2 is taking shape，尚未给出已核验可操作开窗，defer。
  - Monko Mania / $MONKO DogeOS testnet 积分分享、Laika/GovernOS 测试网转帖：不新建卡。
  - bramble_game：视频游戏通关回复，不是 Starknet @Bramble_fi。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 753 BrokeNiggameme。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：已跑 Starknet；下一轮 打新。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- PingPay 本轮已按真新提醒；同一份官网 CA、同一份 DexScreener Solana/pumpfun 池（报价币 PAID、liquidity=null）、同一份 `/api/coins` 6 枚示例币、同一份 X 回复发射/付款指令不重推。出现已核验的新产品入口、改 CA，或出现免费窗口再提醒。不要写成 SOL 配对，不要编造流动性或持有人数，不要写成免费 mint，也不要把 pump.fun 403 写成已打开币页。
- Hyperolius 已按真新提醒（R1901）；同一份 CA / 同一 Montra-DexScreener 池、同一份微盘数字与同名仿盘风险说明不重推。出现已核验的流动性/交易新变化、官方撤回或澄清仿盘 CA，或出现免费窗口再提醒。不要编造单一 24h 涨跌，不要写成免费 mint。
- Neon Sports 已按真新提醒（R1901）；同一份 Robinhood CA、同一份「流媒体已上、DEX/NFT Exchange Coming Soon、mint 价与是否开放未核验」口径不重推。补公布并核验 mint 价/开窗、进入 ≤2h，或 DEX/交易所实际开放再提醒。不要把 Coming Soon 写成已上线，也不要把「launching in 14…」补全成确定时刻。
- SYRØ 同一份「测试网水龙头与排行榜已开、主网免费 mint 未开、快照与主网时刻未公布」状态不重推。补公布快照或主网时刻、进入 ≤2h，或免费 mint 实际开窗、公布已核验合约再提醒。不要写成免费 mint LIVE，也不要把第三方 Zero 主网倒计时写成 SYRØ 官方时间。
- Zyro 同一份 Pons 曲线 / 同一 CA / 同一「股票已上、perps 下一步」口径不重推。Dex 图表实际上线、出现已核验链上数字，或 perps 实际开放再提醒。不要编造市值，不要写成免费 mint。
- PumpTok 已按真新提醒（R1899）；同一份「官网已开但 Explore 仍 0 live coins」、同一份「将发测试代币 / elgato」预告不重推，除非出现首个已核验 live coin、官方激励/开窗，或补充并核验除 $PUMPTOK 以外的可操作合约。不要写成免费 mint。
- Pantheon perps 已按真新提醒（R1899）；同一份已开的 /api/markets、同一份 Elysium 标的成交/持仓为 0、同一份 AGI 2026-11-17 02:47 CST 开放时刻不重推。AGI 进入 ≤2h 或实际 open=true，或 Elysium 标的出现已核验成交/持仓、独立核验 CA，再提醒。不要写成免费 mint。
- TapeExit 已按真新提醒（R1898）；同一份只读 Demo / 黑客松投票、生产签名仍关闭的状态不重推，除非生产签名实际开放、完成独立审阅，或出现已核验可操作的退出/铸造窗口。
- PlunderPort 已按「官网首次可访问 + 早期登记入口开放」提醒（R1898）；同一份早期登记 / 同一份「3,333 FREE MINT 但 mint 未开、链与日期未公布」不重推；补公布链或 mint 日期、进入 ≤2h，或免费 mint 实际开窗再提醒。不得把 early-access 写成免费 mint LIVE。
- Whale.Fun 已按真新提醒（R1897）；同一空列表发射台不重推，除非出现首批可参与的发射或官号给出已核验 CA/开窗。
- Bombshell Cats 已按真新+免费 AL 提醒（R1897）；同一份 11-16 20:00 CST AL / 11-17 20:00 CST 公售时间表不重推；进入 ≤2h、确认 LIVE，或公布已核验合约再提醒。不要把 OpenSea “Minting now” 标签当成已经开放。
- hood-bitz / BITBOTZ 已按首次补出时刻提醒（R1897）；同一份 11-17 02:00 CST 快照 / 11-17 06:00 CST 开铸、仅已下架持仓、无公售的时间表不重推；临近 ≤2h 或实际开窗再提醒。
- TapeAI BEM 预存已按首次补出 16:00 CST 钟点提醒（R1897）；同一份预存窗口不重推；进入 ≤2h、预存实际开启，或官号补全并核验 2% 检察官快照时刻再提醒。第三方「开始预存了」不能当作官方确认。
- Voxel World Pixel 同一份付费 Genesis（0.0015 BNB）/ 同一 CA 不重推，除非出现新的免费窗口、改 CA，或 Genesis 售罄/关闭被核验。
- Liquid Reserve 同一份 Elysium CA / 同一 Ascend 池行情不重推，除非出现免费窗口、官号澄清或撤回 Solana CA，或流动性/交易出现新的可操作变化。勿把 `71mfKdePwyWXtiF1mqu2aaCdMKnKuN664z2vEM2Xpump` 当作本项目 Solana CA。
- PaidTok 同一份 CA / 同一泵池行情、同一 live 发射台上的 Video Coins 更新不重推，除非出现免费窗口、改 CA，或出现新的可操作发射/结算变化。
- hooja-fun 同一份 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，未给时刻）不重推；补公布具体时刻、进入 ≤2h，或实际开窗再提醒。
- MicroFrens mint 已完成 / reveal 倒计时（含隐藏特质揭示 2026-11-17 01:00 CST）不重推，除非出现新的首次可操作窗口或新集合 LIVE。
- DualForge 同一已开闸窗口的 day-two 进度不重推。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- escapehub / ephemeral-eth 同一份 11-16 23:00 CST 上线时刻不重推；临近 ≤2h 或确认 LIVE 再提醒。
- sunfall-world Season 1 结算与 Season 2 开赛宣传不重推，除非出现新 mint/登记窗口。
- spoxyfun 同一份免费 800/800 售罄、付费 0.001 BNB 仍开放的状态不重推。
- zaibatsu-wagies 同一份 Candlelords 持有人免费 / 其他人 $3 的 intern mint 不重推，除非出现新窗口或改规则。
- wrapped-eth /claim 仍按既有 404 记录；费率说明与 redeem 文档已记下，不重推；claim 实际开放或公布已核验合约再提醒。
- tapemine / TapeOut 官方矿池 harvestRange Permissionless 机制说明已记下，不重推；出现新的已核验 CA 或新的 mint/开窗再提醒。
- Ammora 同一份等待名单/积分产品口径不重推；Season 2 若出现已核验官帖或可打开的官方入口，再评估是否提醒。
