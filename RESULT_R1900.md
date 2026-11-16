# RESULT R1900

- time: 2026-11-16 12:41 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 795 → 770 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: syro, zyro
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit 5d16b5c R1899）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=795），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent DogeEVM 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=795。25 次读取后 remaining=770。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 555 nomadfinanceio 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 69。NF_skip 19，其中 3 个为本轮新写入（stockcatsfun / Trysmolpadfun / agentharvest_ai）；其余 16 个已在列（Volitionxyz / tollsfun / whackyrh / bibiainft / AgentBoss_AI / obolworld / Elysium_Rocks / agents_estates / ClassifiedMRNG / Villagers_RH / agentcityuk / MonsterRH_ / Derpagent_ / Proxisfun / ramencoinmeme / letswinhood）。firstKept nomadfinanceio，lastKept moarpixelss。next 624 agenticheist。
- MUST1：24 个 live/窗口号；MUST2：21 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + PlunderPort + PonkeAgent + KomaAgentID + pumptoksocial + pantheonperps + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 107 号 5 片全读（26+25+26+26+4）。UF1 / UF2 / THIN1 / THIN5 / MEN_MINE / MEN_BN 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T03:00:00Z（约 1.5h，与 R1899 official 02:30Z 窗口重叠）；KW 与 mentions 自 2026-11-16T02:30:00Z（约 2h）；silent 自 2026-11-15T04:31:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 11 / Elysium+kinetiq 10 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 0。
- silent：1900%11=8 DogeEVM。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（5 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 0，admitted 0。下一轮 lane=BTC。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]。

## 信号与结论

新录取 2 张（syro、zyro）。无 ≤2h 窗口。判断/文案走 DeepSeek，dsFallback=false。notify=true：两张均为真新收录（SYRØ 不是免费 mint LIVE，Zyro 不是免费 mint）。已把 syro 与 zyro 写入 forcePanelIds；syro 进 userFollowWatch + zeroWatch，zyro 进 userFollowWatch。新卡 focus=false，lzVerified=false。round≥1840 的 leak 检查为 0。本轮无新的 Watch 漏挂修复。

- **syro**（真新，notify）：@SYR0xyz / SYRØ（开号 2026-11-15T13:48:11Z = 2026-11-15 21:48 CST，粉 13，tweet_count=5，xUserId=2121963023262949376）。MEN_LZ 命中。本轮 11:38 CST 官帖 https://x.com/SYR0xyz/status/2122172482069446856 称 Base Sepolia 测试网已开、通往 FREE MINT 白名单的路已开。官网 https://xn--syr-2na.xyz/（punycode 的 syrø.xyz）本轮 HTTP 200，title「SYRØ — The NFT Desk on Zero」：4,444 枚固定价 NFT 柜台（每枚 100,000 Ø），柜台卖 4,000 枚、其余 444 枚留给免费 mint 白名单且永不在柜台出售；随机买加 10% ZRO 费、指定编号买加 15% ZRO 费，卖回无卖出费；70% 柜台费给已激活持有人。官网原文：「The free mint itself is not open on testnet — it opens at the mainnet launch, for whitelist wallets only」。测试网积分来自 curve / desk / activation / loans 与推荐，快照时排行榜前 444 钱包获主网免费 mint 白名单（每钱包 1 枚）；领取的 NFT 前 7 天不能卖回或抵押。tZRO 水龙头每 24 小时 100 tZRO，另需 Base Sepolia ETH 作 gas；官网写明「Testnet tokens have no value」。本轮官网 HTML 未见 0x 合约。快照时刻与 Zero 主网开线时刻均未在官方向材料中给出，禁止引用第三方「还有两周」说法作为本项目官方时间。自称 Forged on LayerZero / The NFT Desk on Zero，未见已核验主网或 OFT 合约，栏位置于台子/Meme，lzVerified=false，状态 testnet。不要写成免费 mint LIVE。本号不自动 mint。
- **zyro**（真新，notify）：@ZyroxRH / Zyro（开号 2026-11-14T06:18:57Z = 2026-11-14 14:18 CST，粉 29，tweet_count=23，xUserId=2121487647701098496）。KW_PAD 命中。本轮 12:10 CST 官帖 https://x.com/ZyroxRH/status/2122180604062310771 称 $ZYRO 仍在 Pons bonding curve，实时图表暂放自家站点，股票交易（auto TP/SL）已上线、perps 下一步。官网 https://www.zyro-ai.xyz/ 与 /chart 本轮 HTTP 200；Pons https://ponsfamily.com/launchpad/0x50e05d1ee5e545540190a1136667af06a496f6d2 title「Zyro (ZYRO) | Pons」200；Blockscout 代币页 https://robinhoodchain.blockscout.com/token/0x50e05d1ee5e545540190a1136667af06a496f6d2 200。CA 0x50e05d1ee5e545540190a1136667af06a496f6d2 来自 bio 并与上述 URL 一致，未做独立源码核验。图表页静态市值/成交量为破折号并写着 Loading；Blockscout API 被 Cloudflare 拦截，本轮无独立 holders / totalSupply / 报价，禁止编造链上数字。GitHub https://github.com/zyroai11/Zyro-Agent ；官网扫描示例自述为 made-up tokens 的格式演示。不是免费 mint。本号不自动买卖。
- **pumptok**（在库，不重推）：本窗继续发四步发射教程，并预告将创建一个测试代币（elgato 相关）；截至本轮仍未见已发射的 live 代币，Explore 仍 0 live coins，不重推。
- **wrapped-eth**（在库，不重推）：12:28 CST 官帖 https://x.com/wrapped__eth/status/2122184889823056007 解释总费率 1–10%、平台拿所收费用的 30%、其余 70% 走 creator policy。费率说明，不是新的 claim/CA/开窗。上一轮 /claim 仍 404，本轮未再探测，不得写成 claim 已开放。
- **pantheon-perps**：11:38 CST 官帖与 R1899 收录时为同一条；AGI 仍是 2026-11-17 02:47 CST 才开放（距今约 14.1h），非 ≤2h，不重推。
- **tapeai**：本窗仅 12:26 CST 表情回复；BEM 预存仍是 2026-11-16 16:00 CST，距今约 3.3h，仍非 ≤2h，不重推。
- **microfrens**：11:19 CST 官帖再次确认隐藏特质揭示 2026-11-17 01:00 CST，与 R1898 已记录为同一时刻，mint 已结束，不重推。
- **不重推**：sunfall-world Season 1 日记；spoxyfun 免费 800/800 售罄、付费 0.001 BNB 仍开放；dogstarter $PENGO 等仍为 DOGEOS TESTNET ONLY；tape-exit 同一份只读 Demo / 黑客松投票；hood-bitz / inklegions / cipher-syndicate / escapehub / ephemeral-eth / hooja-fun / plunderport / whale-fun / voxel-world-pixel / liquid-reserve / wowpad / usePaidTok 同一份已提醒或已记录日程/状态；hypesium 本轮未见官帖，第三方「230 users / 19 launchpads」未核验，不写卡不重推。
- 预拒 / skip：
  - **@SamuraiBlob_ / Samurai Blob**：R1899 已 skip；本窗同一条 First Launchpad just live 口径，不作为新打新收录。
  - **@ShrabonRoy01**：t.co 只解析到已在库 @tsbdotfun / The Shadow Born（卡 id tsbdotfun），不是新项目官号。
  - **@DEVMASTERHB**：仅转发已在库 Hood_Bitz / BITBOTZ 铸造说明，不建新卡。
  - **@BitBlitzBuzz** 等第三方「2 weeks till zero mainnet」以及 GTE / lzATLAS 阵容转述：未拉对应官号，不能当作 SYRØ 或其它项目的官方时刻。
  - Ammora / GIWA Sepolia 测试网演示、仅回复/仅转帖且无独立官号与站点的免费 mint 传言：skip/defer。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 624 agenticheist。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：已跑 DogeEVM；下一轮 BTC。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- SYRØ 本轮已按真新提醒；同一份「测试网水龙头与排行榜已开、主网免费 mint 未开、快照与主网时刻未公布」状态不重推。补公布快照或主网时刻、进入 ≤2h，或免费 mint 实际开窗、公布已核验合约再提醒。不要写成免费 mint LIVE，也不要把第三方 Zero 主网倒计时写成 SYRØ 官方时间。
- Zyro 本轮已按真新提醒；同一份 Pons 曲线 / 同一 CA / 同一「股票已上、perps 下一步」口径不重推。Dex 图表实际上线、出现已核验链上数字，或 perps 实际开放再提醒。不要编造市值，不要写成免费 mint。
- PumpTok 已按真新提醒（R1899）；同一份「官网已开但 Explore 仍 0 live coins」、同一份「将发测试代币 / elgato」预告不重推，除非出现首个已核验 live coin、官方激励/开窗，或补充并核验除 $PUMPTOK 以外的可操作合约。不要写成免费 mint。
- Pantheon perps 已按真新提醒（R1899）；同一份已开的 /api/markets、同一份 Elysium 标的成交/持仓为 0、同一份 AGI 2026-11-17 02:47 CST 开放时刻不重推。AGI 进入 ≤2h 或实际 open=true，或 Elysium 标的出现已核验成交/持仓、独立核验 CA，再提醒。不要写成免费 mint。
- TapeExit 已按真新提醒（R1898）；同一份只读 Demo / 黑客松投票、生产签名仍关闭的状态不重推，除非生产签名实际开放、完成独立审阅，或出现已核验可操作的退出/铸造窗口。
- PlunderPort 已按「官网首次可访问 + 早期登记入口开放」提醒（R1898）；同一份早期登记 / 同一份「3,333 FREE MINT 但 mint 未开、链与日期未公布」不重推；补公布链或 mint 日期、进入 ≤2h，或免费 mint 实际开窗再提醒。不得把 early-access 写成免费 mint LIVE。
- Whale.Fun 已按真新提醒（R1897）；同一空列表发射台不重推，除非出现首批可参与的发射或官号给出已核验 CA/开窗。
- Bombshell Cats 已按真新+免费 AL 提醒（R1897）；同一份 11-16 20:00 CST AL / 11-17 20:00 CST 公售时间表不重推；进入 ≤2h、确认 LIVE，或公布已核验合约再提醒。不要把 OpenSea “Minting now” 标签当成已经开放。
- hood-bitz / BITBOTZ 已按首次补出时刻提醒（R1897）；同一份 11-17 02:00 CST 快照 / 11-17 06:00 CST 开铸、仅已下架持仓、无公售的时间表不重推；临近 ≤2h 或实际开窗再提醒。
- TapeAI BEM 预存已按首次补出 16:00 CST 钟点提醒（R1897）；同一份预存窗口不重推；进入 ≤2h、预存实际开启，或官号补全并核验 2% 检察官快照时刻再提醒。
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
- wrapped-eth /claim 仍 404；12:28 CST 费率说明官帖已记下，不重推；claim 实际开放或公布已核验合约再提醒。
- tapemine / TapeOut 官方矿池 harvestRange Permissionless 机制说明已记下，不重推；出现新的已核验 CA 或新的 mint/开窗再提醒。
