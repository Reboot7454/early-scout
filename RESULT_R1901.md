# RESULT R1901

- time: 2026-11-16 13:13 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 770 → 745 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: hyperolius, neon-sports
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit d9b268f R1900）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=770），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent BTC 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=770。25 次读取后 remaining=745。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 624 agenticheist 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 64。NF_skip 14，其中 3 个为本轮新写入（seatworkcells / Honestcoin60 / DropMinters）；其余 11 个已在列（NidavellirBSC / frogsagent / onbeatfun / lettucegrow_rh / beatdotfamily / nonamespnft / heyribbid / inkwellonbnb / certuna_rh / miuadotfun / origopad）。firstKept agenticheist，lastKept manesnft。next 688 fagent_。
- MUST1：24 个 live/窗口号；MUST2：23 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + PlunderPort + PonkeAgent + KomaAgentID + pumptoksocial + pantheonperps + SYR0xyz + ZyroxRH + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+27+4）。UF1 / UF2 / THIN1 / THIN5 / KW_LZ / MEN_BTC 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T03:30:00Z（约 1.5h，与 R1900 official 03:00Z 窗口重叠）；KW 与 mentions 自 2026-11-16T03:00:00Z（约 2h）；silent 自 2026-11-15T05:02:00Z（约 24h）。
- mentions 4 组轮换：Tape 19 / GIWA 2 / BTC 0 / Starknet+DogeEVM 1。
- silent：1901%11=9 BTC。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（12 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 1（@Neon_RH），admitted 1（neon-sports）。下一轮 lane=Starknet。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]（MUST2 / KW_TAPE / KW_GIWA / KW_DOGE / KW_MINT / KW_PAD / KW_ELY / MEN_TAPE / SILENT_MEN 预览曾截断，均已用 .full 还原）。

## 信号与结论

新录取 2 张（hyperolius、neon-sports）。无 ≤2h 窗口。判断/文案走 DeepSeek，dsFallback=false。notify=true：两张均为真新收录（均不是已核验的免费 mint LIVE）。已把 hyperolius 与 neon-sports 写入 forcePanelIds；hyperolius 进 userFollowWatch + elysiumWatch，neon-sports 进 userFollowWatch。新卡 focus=false，lzVerified=false。round≥1840 的 leak 检查为 0。本轮无新的 Watch 漏挂修复。

- **hyperolius**（真新，notify）：@HyperoliusHYPE / Hyperolius（开号 2026-10-24T10:30:34Z = 2026-10-24 18:30 CST，粉 62，tweet_count=7，xUserId=2113940944667963392）。KW_ELY 命中。本轮 13:00 CST 官帖 https://x.com/HyperoliusHYPE/status/2122193079335575697 称 Hyperolius 是非洲芦蛙真实属名、把这个名字上链。官网 https://hyperolius.xyz/ 本轮 HTTP 200，title「Hyperolius — The Frog of Elysium」：自称独立社区 meme，$HYPEROLIUS 在 Elysium 与 HYPE 配对，选中 Montra 费率档为买卖各 2%，持有人奖励以 HYPE 支付，并写明 2% 是交易费、不是承诺回报。CA 0x3d69554ec106ec13f5676ef02df672da8a18de9b 在 bio、官网与 Montra 代币页三处一致，未做独立源码核验。Montra https://montramarkets.xyz/token/0x3d69554ec106ec13f5676ef02df672da8a18de9b 本轮 200，可见「Launched 2d ago」、Plain ERC-20（no owner / no mint / no pause / no transfer fee，启动流动性自称永久锁定）、Price $0.0000101、Market cap $10.1K / $10.06K、Vol. 24h $10.8K、Holders 35、Supply 1B、173 trades all time、Fees paid 4.56 HYPE（3.67 HYPE to holders）、Graduation 29%、Anti-snipe fee ended。DexScreener 同 CA 的 Elysium uniswap v4 池 pairCreatedAt 换算为 2026-11-14 03:58 CST，liq.usd 7845.1，mcap/fdv 10092，volume.h24 10944.22，h24 68 买 / 43 卖。Montra 页 24h +57.6% 与 DexScreener 24h +2.79% 不一致，不合成单一涨跌数字。同一次搜索还出现同名不同 CA 0x88bDB56266180d85d733d5C82626F329166c42FE（2026-11-16 06:17 CST，h24 成交量 0），不是官方地址，已标仿盘风险。不是免费 mint。本号不自动买卖。
- **neon-sports**（真新，notify）：@Neon_RH / Neon Sports（开号 2026-08-01T02:24:48Z = 2026-08-01 10:24 CST，粉 531，tweet_count=990，xUserId=2083378077254475776）。SILENT_MEN 命中。本轮 06:16 CST 官帖 https://x.com/Neon_RH/status/2122091503371554930 称持有更多本项目 NFT 可从体育流媒体收入获得被动收入（live now），DEX launching this week，跨链 deal maker NFT exchange 支持 ETH/SOL/BASE/ROBINHOOD 与 BTC ORDINALS（原文截断于「launching in 14」，未给出完整单位，不补全成确定时刻）。官网 https://www.neonsportstv.xyz/ 本轮 HTTP 200。/nft 页给出 Robinhood Chain 合约 0x63A08A8635339A5C05e589D774231e03931169Fb。/buy-mint-nft 200，但静态 HTML 未见价格、剩余或 Minting now / Sold out，mint 是否仍开放本轮未核验。/dex 与 /nft-marketplace 均为 Coming Soon，无开线钟点。静态页 OpenSea 只链到 https://opensea.io/ 首页，未给 collection slug，不编造地板价。不是已核验的免费 mint LIVE。本号不自动 mint。
- **pumptok**（在库，不重推）：本窗继续发四步发射教程，并再次预告将为 elgato 创建测试代币；截至本轮仍未见已核验 live coin，不重推。
- **paidtok**（在库，不重推）：本窗发长期建设、Video Coins/gifts 与 fee vault 说明，同一份已开 live 发射台，不重推。
- **creedo**（在库，不重推）：12:57 CST 官帖称 Token Tools（Holder Snapshot + Multisender）are live；R1885 已记录过 Token Tools 上线，不是第一次补出入口，不重推。
- **wrapped-eth**（在库，不重推）：11:34 CST 官帖解释 redeem 路径并链到 https://wrapped.wtf/docs/（本轮 200）；12:28 CST 费率说明已在 R1900 记下。本轮未再探测 /claim，不得写成 claim 已开放。
- **zyro / syro**：同一份已提醒口径，不重推。SYRØ 不要写成免费 mint LIVE。
- **pantheon-perps**：11:38 CST 官帖与已记录为同一条；AGI 仍是 2026-11-17 02:47 CST 才开放（距今约 13.6h），非 ≤2h，不重推。
- **tapeai**：本窗仅表情回复；BEM 预存仍是 2026-11-16 16:00 CST，距今约 2.8h，尚未 ≤2h，不重推。第三方「开始预存了」不能当作官方确认已开。
- **不重推**：tape-exit 同一份只读 Demo / 黑客松投票；tapemine harvestRange Permissionless；sunfall-world Season 1 日记；hood-bitz 未改 11-17 时间表；hooja-fun 未见补公布 UNVAULT 时刻；dogstarter $PENGO 等仍为 DOGEOS TESTNET ONLY；mulle-protocol Mulle Points 站点 200、无新 mint；ammora Season 2 仅第三方祝贺、official 窗无官帖、站点未能独立打开，不写成官方开窗。
- 预拒 / skip：
  - DexScreener 同名不同 CA 的 0x88bDB56266180d85d733d5C82626F329166c42FE：不建第二张官方卡，只作为 hyperolius 仿盘风险。
  - Herkux___09 / Danger_089 等 KW 命中回复号、RebateLaunch bonding curve 讨论：不是新项目官号。
  - Laika Super App / GovernOS 第三方 testnet 说法：已在库 laika-doge，不新建卡。
  - AnFeng0858 等 TapeOut 布道者转发他人电商截图：不建新卡。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 688 fagent_。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent：已跑 BTC；下一轮 Starknet。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- Hyperolius 本轮已按真新提醒；同一份 CA / 同一 Montra-DexScreener 池、同一份微盘数字与同名仿盘风险说明不重推。出现已核验的流动性/交易新变化、官方撤回或澄清仿盘 CA，或出现免费窗口再提醒。不要编造单一 24h 涨跌，不要写成免费 mint。
- Neon Sports 本轮已按真新提醒；同一份 Robinhood CA、同一份「流媒体已上、DEX/NFT Exchange Coming Soon、mint 价与是否开放未核验」口径不重推。补公布并核验 mint 价/开窗、进入 ≤2h，或 DEX/交易所实际开放再提醒。不要把 Coming Soon 写成已上线，也不要把「launching in 14…」补全成确定时刻。
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
