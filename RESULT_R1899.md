# RESULT R1899

- time: 2026-11-16 12:16 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 820 → 795 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: pumptok, pantheon-perps
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit 20cb6c3 R1898）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=820），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent GIWA 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=820。25 次读取后 remaining=795。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 497 rheacatnear 起（已在 NF_skip，首个跳过）packed 2 片 kept 49（25+24），wrap=false，walkScanned 58。NF_skip 9，其中 8 个为本轮新写入（99901dotfun / magnitudeagent / bububullfun / lanternfield / streamlitmaker / trycortano / hook404rh / agentpunkai）；其余 1 个已在列（rheacatnear）。firstKept mattresssafu，lastKept launchviafun。next 555 nomadfinanceio。
- MUST1：24 个 live/窗口号；MUST2：19 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + PlunderPort + PonkeAgent + KomaAgentID + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+27+4）。UF1 / UF2 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T02:30:00Z（约 1.5h，与 R1898 official 02:00Z 窗口重叠约 1.5h）；KW 与 mentions 自 2026-11-16T02:00:00Z（约 2h）；silent 自 2026-11-15T04:04:00Z（约 24h）。空结果：UF1 / UF2 / THIN5。
- mentions 4 组轮换：Tape 25 / GIWA 1 / BTC 1 / Starknet+DogeEVM 3。
- silent：1899%11=7 GIWA。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（25 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 0，admitted 0（多为 Ammora Season 2 / GIWA Sepolia 演示互动）。下一轮 lane=DogeEVM。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]。

## 信号与结论

新录取 2 张（pumptok、pantheon-perps）。无 ≤2h 窗口。判断/文案走 DeepSeek，dsFallback=false。notify=true：两张均为真新收录（均不是免费 mint）。已把 pumptok 与 pantheon-perps 写入 forcePanelIds；pumptok 进 userFollowWatch，pantheon-perps 进 userFollowWatch + elysiumWatch。新卡 focus=false。round≥1840 的 leak 检查为 0。本轮无新的 Watch 漏挂修复。

- **pumptok**（真新，notify）：@pumptoksocial / PumpTok（开号 2026-11-09T12:22:59Z = 2026-11-09 20:22 CST，粉 4，tweet_count=2）。KW_PAD 命中。本轮 11:54 CST 官帖 https://x.com/pumptoksocial/status/2122176372374118589 「We are live.」。官网 https://www.pumptok.social/ 与 docs https://www.pumptok.social/docs 本轮 HTTP 200：在 pump.fun（Solana）上发射，每枚币绑定一个 TikTok 账号或单条视频，100% creator fees 归被绑定账号，无平台费；用 TikTok 公开 bio 里的一次性验证码证明所有权；发射成本为自选 dev buy 外加约 ◎0.045 网络成本。Explore 页静态可见「Explore 0 live coins」，不要编造已发射代币。官方 bio/官网给出 $PUMPTOK 地址 9iWwzVWcanVFs5WNnmnoFDkDSj1XD2DWHR8GoQ8apump，未做链上独立核验，材料未提供其它合约。不要与库内 @usePaidTok / PaidTok 合并。不是免费 mint。本号不自动 mint。
- **pantheon-perps**（真新，notify）：@pantheonperps / Pantheon（开号 2026-11-09T00:18:25Z = 2026-11-09 08:18 CST，粉 121，tweet_count=45）。KW_ELY + KW_PAD 命中。本轮 11:38 CST 官帖 https://x.com/pantheonperps/status/2122172550516199503 称 Elysium（Ascend/Montra）新币上线约 1 小时 40 分后可在 Pantheon 开杠杆做多/做空。官网 https://pantheonperps.com/ HTTP 200；https://pantheonperps.com/api/markets 200，listing 11 个 Elysium 相关标的（10 个 open=true，AGI/Agorian open=false：上架 2026-11-16 02:47:11 CST，开放 2026-11-17 02:47:11 CST，距今约 14.6h，不是 ≤2h）。抽样的 Elysium 标的 dayVolumeUsd=0、openInterestUsd=0，仅有 markPx；接口内 BTC 等大额成交是 Hyperliquid 风格市场数据，不能当成 Elysium 币已有巨大成交。CA 0x892723bf41f2e1af70adb1ff19036810888473a3 来自 bio 与前端 JS，本轮未做独立区块浏览器核验，不要编造代币符号或是否可买。与库内 @askpantheon / @PantheonDesk / @Pantheonindex / @pantheonsi 不是同一项目，未合并。不是免费 mint。本号不自动买卖。
- **tapemine**（在库，不重推）：官帖解释 TapeOut 官方矿池 harvestRange(start, count) 为 Permissionless，任何地址可调用并付网络手续费，把矿机产出从 Mining 合约收进矿池账本。机制说明，非新开窗、无新核验 CA，不重推。
- **tapeai / bombshell-cats / 1k-art-gallery**：同一份已提醒时间表（TapeAI BEM 预存 16:00 CST，距今约 3.8h 仍非 ≤2h；Bombshell Cats AL 20:00 CST / 公售次日 20:00 CST），不重推。
- **不重推**：usePaidTok 同一 live 发射台，本窗继续有 Video Coins / $TUCKER / $MOG 宣传，未改 CA、无新免费窗口；wrapped-eth 11:34 CST 赎回路径官帖与 R1898 为同一条；microfrens 隐藏特质揭示仍是 2026-11-17 01:00 CST，mint 已结束；spoxyfun 免费 800/800 售罄、付费 0.001 BNB 仍开放；dogstarter $PENGO 等标明 DOGEOS TESTNET ONLY；plunderport 同一份早期登记 / mint 未开；whale-fun / hooja-fun / escapehub / ephemeral-eth / hood-bitz / inklegions / cipher-syndicate / voxel-world-pixel / liquid-reserve / wowpad / gekko-launchpad 同一份已记录日程或状态。
- 预拒 / skip：
  - **@samuraiblob_ / Samurai Blob**：官网 samuraiblob.xyz 为已上线 Elysium/Montra meme（$SLOB，no mint）；本轮「First Launchpad just live」的 t.co 只解析到库内 @StinkyPenguinL0 推文，不作新打新收录。
  - **@abdulszj / Metaxx** 及 @officialcorpltd、@kee1525、@yetu891、@ariesbalweell：Ammora SDK / GIWA Sepolia 测试网 launchpad 演示，与 R1898 同类，skip。
  - **Ammora Season 2** 连接故障/积分讨论：已在库生态互动，不建卡。
  - **Trovehaven / CompanionsWfit / FungoLabs / Ghost Pixel Planet / HyperHaul**：库内项目的第三方提及或旧活动转帖，本轮未拉这些官号、无新的首次官宣窗口，不重推也不新建卡。
  - 其它仅回复/仅转帖、无独立官号与站点的免费 mint 传言：skip/defer。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 555 nomadfinanceio。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent：已跑 GIWA；下一轮 DogeEVM。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- PumpTok 本轮已按真新提醒；同一份「官网已开但 Explore 仍 0 live coins」状态不重推，除非出现首个已核验 live coin、官方激励/开窗，或补充并核验除 $PUMPTOK 以外的可操作合约。不要写成免费 mint。
- Pantheon perps 本轮已按真新提醒；同一份已开的 /api/markets、同一份 Elysium 标的成交/持仓为 0、同一份 AGI 2026-11-17 02:47 CST 开放时刻不重推。AGI 进入 ≤2h 或实际 open=true，或 Elysium 标的出现已核验成交/持仓、独立核验 CA，再提醒。不要写成免费 mint。
- TapeExit 已按真新提醒（R1898）；同一份只读 Demo / 黑客松投票、生产签名仍关闭的状态不重推，除非生产签名实际开放、完成独立审阅，或出现已核验可操作的退出/铸造窗口。
- PlunderPort 已按「官网首次可访问 + 早期登记入口开放」提醒（R1898）；同一份早期登记 / 同一份「3,333 FREE MINT 但 mint 未开、链与日期未公布」不重推；补公布链或 mint 日期、进入 ≤2h，或免费 mint 实际开窗再提醒。不得把 early-access 写成免费 mint LIVE。
- Whale.Fun 已按真新提醒（R1897）；同一空列表发射台不重推，除非出现首批可参与的发射或官号给出已核验 CA/开窗。
- Bombshell Cats 已按真新+免费 AL 提醒（R1897）；同一份 11-16 20:00 CST AL / 11-17 20:00 CST 公售时间表不重推；进入 ≤2h、确认 LIVE，或公布已核验合约再提醒。不要把 OpenSea “Minting now” 标签当成已经开放。
- hood-bitz / BITBOTZ 已按首次补出时刻提醒（R1897）；同一份 11-17 02:00 CST 快照 / 11-17 06:00 CST 开铸、仅已下架持仓、无公售的时间表不重推；临近 ≤2h 或实际开窗再提醒。
- TapeAI BEM 预存已按首次补出 16:00 CST 钟点提醒（R1897）；同一份预存窗口不重推；进入 ≤2h、预存实际开启，或官号补全并核验 2% 检察官快照时刻再提醒。
- Voxel World Pixel 同一份付费 Genesis（0.0015 BNB）/ 同一 CA 不重推，除非出现新的免费窗口、改 CA，或 Genesis 售罄/关闭被核验。
- Liquid Reserve 同一份 Elysium CA / 同一 Ascend 池行情不重推，除非出现免费窗口、官号澄清或撤回 Solana CA，或流动性/交易出现新的可操作变化。勿把 `71mfKdePwyWXtiF1mqu2aaCdMKnKuN664z2vEM2Xpump` 当作本项目 Solana CA。
- PaidTok 同一份 CA / 同一泵池行情、同一 live 发射台上的 Video Coins / $TUCKER / $MOG 更新不重推，除非出现免费窗口、改 CA，或出现新的可操作发射/结算变化。
- hooja-fun 同一份 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，未给时刻）不重推；补公布具体时刻、进入 ≤2h，或实际开窗再提醒。
- MicroFrens mint 已完成 / reveal 倒计时（含隐藏特质揭示 2026-11-17 01:00 CST）不重推，除非出现新的首次可操作窗口或新集合 LIVE。
- DualForge 同一已开闸窗口的 day-two 进度不重推。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- escapehub / ephemeral-eth 同一份 11-16 23:00 CST 上线时刻不重推；临近 ≤2h 或确认 LIVE 再提醒。
- sunfall-world Season 1 结算与 Season 2 开赛宣传不重推，除非出现新 mint/登记窗口。
- spoxyfun 同一份免费 800/800 售罄、付费 0.001 BNB 仍开放的状态不重推。
- zaibatsu-wagies 同一份 Candlelords 持有人免费 / 其他人 $3 的 intern mint 不重推，除非出现新窗口或改规则。
- wrapped-eth /claim 仍 404、11:34 CST 赎回路径官帖已记录，不重推；claim 实际开放或公布已核验合约再提醒。
- tapemine / TapeOut 官方矿池 harvestRange Permissionless 机制说明已记下，不重推；出现新的已核验 CA 或新的 mint/开窗再提醒。
