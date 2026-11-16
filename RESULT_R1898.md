# RESULT R1898

- time: 2026-11-16 11:43 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 845 → 820 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: tape-exit
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit ca763a1 R1897）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=845），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent Tape/电路 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=845。25 次读取后 remaining=820。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 435 astrispace 起（已在 NF_skip，首个跳过）packed 2 片 kept 49（25+24），wrap=false，walkScanned 63。NF_skip 14，其中 10 个为本轮新写入（AIDOGagentai / halfhook / Fruits_by_Amy / cardstockfun / potionrh / beatmissapp / sharpsheet_rh / safufundbnb / Asciidogs / rheacatnear）；其余 4 个已在列（astrispace / Fairagent_bnb / ChyAI_Official / snakeidbnb）。firstKept YieldFields_RH，lastKept elysiumbrokers。next 497 rheacatnear（也在本轮 NF_skip，下轮将首个跳过）。
- MUST1：24 个 live/窗口号；MUST2：16 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 107 号 5 片全读（26+25+26+26+4；TapeAIAgent / Writ_Fi 已落入 MUST/UF 去重）。THIN3 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T02:00:00Z（约 1.5h，与 R1897 official 01:30Z 窗口重叠约 1.5h）；KW 与 mentions 自 2026-11-16T01:30:00Z（约 2h）；silent 自 2026-11-15T03:32:00Z（约 24h）。空结果：THIN3 / THIN5 / MEN_MINE / MEN_BN。
- mentions 4 组轮换：LayerZero 3 / Elysium+kinetiq 13 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 0。
- silent：1898%11=6 Tape/电路。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（25 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 1（@TapeExit，同时命中 KW_TAPE），admitted 1。下一轮 lane=GIWA。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]。

## 信号与结论

新录取 1 张（tape-exit）。无 ≤2h 窗口。判断/文案走 DeepSeek，dsFallback=false。notify=true：一张真新收录 + 一张在库卡首次确认可操作的免费早期登记入口（plunderport；mint 本身未开）。已把 tape-exit 与 plunderport 写入 forcePanelIds；tape-exit 进 userFollowWatch + tapeOutWatch。新卡 focus=false。round≥1840 的 leak 检查为 0。本轮无新的 Watch 漏挂修复。

- **tape-exit**（真新，notify）：@TapeExit（开号 2023-10-21T13:08:30Z = 2023-10-21 21:08 CST，粉 6，tweet_count=12）。KW_TAPE + SILENT_MEN 命中。本轮 11:29 CST 官帖 https://x.com/TapeExit/status/2122170280370184669 称参加 @XLayerOfficial 黑客松，请在投票页找 TapeExit 投票；投票页 https://web3.okx.com/zh-hans/xlayer/hackathon-voting 。GitHub https://github.com/wangyangmingsss/tapeexit 创建于 2026-10-27，TypeScript / MIT，stars=0。README 确认 Demo（无需钱包）https://wangyangmingsss.github.io/tapeexit/ ，主网只读入口 https://2-2-289.netlify.app/ ，备用入口 https://2-2-289.vercel.app/ ；公开版只读，生产签名关闭，独立安全审阅尚未完成，Demo 使用模拟资产。已支持 Uniswap V3 仓位 NFT 与 Spark Savings USDC 的读取/预演/核验。不是 mint，不要编造未提供的合约。本号不自动操作。
- **plunderport**（在库，首次确认官网+早期登记可操作，notify）：此前官网 plunderport.fun 在 R1870/R1871 为 TLS/HTTP 000，不得写成已核验免费 LIVE。本轮 https://plunderport.fun/ 首次探测 HTTP 200；early-access 页 https://plunderport.fun/early-access 亦 200，可 Connect Wallet（免费签名，不要付款）+ Connect X / Follow @plunderport 解锁免费早期登记，并有 $10,000 Prize Pool。页面写明 3,333 Genesis NFTs · FREE MINT，同时写 The mint is not live: the chain and the mint date will be announced。status 改为 early-access，不得写成免费 mint LIVE 或已经开铸。官推互链与库内 @PlunderPort 一致。本号不自动 mint。
- **microfrens**（在库，不重推）：11:19 CST 官帖 https://x.com/MicroFrens/status/2122167630253666795 确认 MetaData 已更新，隐藏特质揭示时刻为 2026-11-17 01:00 CST（Monday 9am PST / 12pm EST / 5pm GMT）。mint 已结束 / reveal 不构成新的首次开窗，只记下 hiddenTraitRevealAt，不重推。
- **wrapped-eth**（在库，不重推）：11:34 CST 官帖 https://x.com/wrapped__eth/status/2122171356876091852 讲赎回路径，docs https://wrapped.wtf/docs/ 200；/explore 200，/claim 仍 404，未见新的已核验 CA，不写成 claim 已开放。
- **spoxyfun**：官帖重申免费 800/800 售罄，付费 0.001 BNB 仍开放；R1890 已记录，不重推。
- **zaibatsu-wagies**：官帖重申 MegaCorp Launchpad / Candlelords intern mint（持有人免费，其他人 $3）；库内已有该 highlights，不是首次公布。本轮记下 Candlelords 页面 `0xaDA0134Ca44ed9c68c4149D7a35AFF8893C01462`，不重推。
- **tapeai / bombshell-cats / 1k-art-gallery**：同一份已提醒时间表（TapeAI BEM 预存 16:00 CST，距今约 4.5h 仍非 ≤2h；Bombshell Cats AL 20:00 CST / 公售次日 20:00 CST），不重推。
- **whale-fun**：本轮静态页仍是 SPA，可见 Newly created / Graduating / Live on DEX 三个列表标题，HTML 中未见代币名称，无首批发射证据，不重推。
- **不重推**：usePaidTok 同一 live 发射台 / Video Coins 更新；hooja-fun 同一份 UNVAULT 日期 11-17/11-18 无钟点；escapehub / ephemeral-eth 仍 23:00 CST；hood-bitz BITBOTZ 同一份 11-17 02:00/06:00 CST；inklegions 仍 11-17 03:00 CST 免费 mint；cipher-syndicate 仍 11-17 00:00 CST；dogstarter / gekko 为 DogeOS 测试网；wowpad 仍建设中。
- 预拒 / skip：
  - **ChaoticorderNFT**：1111 免费 mint 仍仅第三方转帖，本轮未拉官号。skip/defer。
  - **VitrumFalcons**：Free mint November 18 on OpenSea / 5000 Falcons on Robinhood，仍仅第三方转帖。skip/defer。
  - **KukiVerse3D**：launches Nov 23 on Robin Hood / OpenSea，5555 免费 mint，仅第三方 RT，未拉官号、未核验站点。skip/defer。
  - **@abdulszj / Metaxx**：个人称给 Ammora Season 2 做的 launchpad 演示，非已核验官号项目。skip。
  - **@phew_pro / $PHEW**：预售宣传，已毕业/预售打新套路。skip。
  - **BarbarianNFT / KrownApes** 等第三方赠送转帖：未核验官号。skip/defer。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 497 rheacatnear。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：已跑 Tape/电路；下一轮 GIWA。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- TapeExit 本轮已按真新提醒；同一份只读 Demo / 黑客松投票、生产签名仍关闭的状态不重推，除非生产签名实际开放、完成独立审阅，或出现已核验可操作的退出/铸造窗口。
- PlunderPort 本轮已按「官网首次可访问 + 早期登记入口开放」提醒；同一份早期登记 / 同一份「3,333 FREE MINT 但 mint 未开、链与日期未公布」不重推；补公布链或 mint 日期、进入 ≤2h，或免费 mint 实际开窗再提醒。不得把 early-access 写成免费 mint LIVE。
- Whale.Fun 本轮已按真新提醒（R1897）；同一空列表发射台不重推，除非出现首批可参与的发射（Newly created / Graduating / Live on DEX 出现已核验代币）或官号给出已核验 CA/开窗。本轮静态 HTML 仍无代币名，不构成该变化。
- Bombshell Cats 本轮已按真新+免费 AL 提醒（R1897）；同一份 11-16 20:00 CST AL / 11-17 20:00 CST 公售时间表不重推；进入 ≤2h、确认 LIVE，或公布已核验合约再提醒。不要把 OpenSea “Minting now” 标签当成已经开放。
- hood-bitz / BITBOTZ 本轮已按首次补出时刻提醒（R1897）；同一份 11-17 02:00 CST 快照 / 11-17 06:00 CST 开铸、仅已下架持仓、无公售的时间表不重推；临近 ≤2h 或实际开窗再提醒。
- TapeAI BEM 预存本轮已按首次补出 16:00 CST 钟点提醒（R1897）；同一份预存窗口不重推；进入 ≤2h、预存实际开启，或官号补全并核验 2% 检察官快照时刻再提醒。
- Voxel World Pixel 同一份付费 Genesis（0.0015 BNB）/ 同一 CA 不重推，除非出现新的免费窗口、改 CA，或 Genesis 售罄/关闭被核验。
- Liquid Reserve 同一份 Elysium CA / 同一 Ascend 池行情不重推，除非出现免费窗口、官号澄清或撤回 Solana CA，或流动性/交易出现新的可操作变化。勿把 `71mfKdePwyWXtiF1mqu2aaCdMKnKuN664z2vEM2Xpump` 当作本项目 Solana CA。
- PaidTok 同一份 CA / 同一泵池行情不重推，除非出现免费窗口、改 CA，或出现新的可操作发射/结算变化。
- hooja-fun 同一份 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，未给时刻）不重推；补公布具体时刻、进入 ≤2h，或实际开窗再提醒。
- MicroFrens mint 已完成 / reveal 倒计时（含本轮记下的隐藏特质揭示 2026-11-17 01:00 CST）不重推，除非出现新的首次可操作窗口或新集合 LIVE。
- DualForge 同一已开闸窗口的 day-two 进度不重推。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- escapehub / ephemeral-eth 同一份 11-16 23:00 CST 上线时刻不重推；临近 ≤2h 或确认 LIVE 再提醒。
- sunfall-world Season 1 结算与 Season 2 开赛宣传不重推，除非出现新 mint/登记窗口。
- spoxyfun 同一份免费 800/800 售罄、付费 0.001 BNB 仍开放的状态不重推。
- zaibatsu-wagies 同一份 Candlelords 持有人免费 / 其他人 $3 的 intern mint 不重推，除非出现新窗口或改规则。
- wrapped-eth /claim 仍 404、未见已核验 CA，不重推；claim 实际开放或公布已核验合约再提醒。
