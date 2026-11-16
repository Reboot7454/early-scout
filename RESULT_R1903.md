# RESULT R1903

- time: 2026-11-16 14:13 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 720 → 695 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: spiritsrh, unicorn-grand-prix, isomatrica
- le2hIds: tapeai
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1902）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=720），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent 打新栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=720。25 次读取后 remaining=695。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 753 BrokeNiggameme 起（该号已在 NF_skip，首个跳过）packed 2 片 kept 49（24+25），wrap=false，walkScanned 70。NF_skip 21，其中 11 个为本轮新写入（babycz_ai / BinanceCanFly / Meteorszmint / emberlingreal / TrineProtocol / LongAgentBNB / dotaipad / btcliu205 / Sambario_bnb / KDAgentAI / Gweiwbbb）；其余 10 个已在列（BrokeNiggameme / bndoge_bn / Mintbncat_ai / oblaunchpadAll / mint_WRIT / AiPullpad / oblaunchpadbase / bianfenhong / dinomitesnft / Morumai_）。firstKept StyxnTerminal，lastKept ElynxNFT。next 823 Elysiumgloom。说明：@dotaipad 仍在库（dotai-pad）且仍在 agentPadWatch / userFollowWatch；本轮只按 UF 分片已有 NF 口径跳过 from: 查询并写入 NF_skip，未另做确认读取。
- MUST1：24 个 live/窗口号；MUST2：24 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + TapeAIAgent + 1KArtGallery + Whalefun_io + PlunderPort + PonkeAgent + KomaAgentID + pumptoksocial + pantheonperps + SYR0xyz + ZyroxRH + usePingPay + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 107 号 5 片全读（26+25+26+26+4）。UF1 / THIN1 / THIN4 / THIN5 / KW_LZ / KW_MINE / MEN_BTC / MEN_SN_DOGE 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T04:30:00Z（约 1.5h，与 R1902 official 04:00Z 窗口重叠）；KW 与 mentions 自 2026-11-16T04:00:00Z（约 2h）；silent 自 2026-11-15T06:00:00Z（约 24h）。
- mentions 4 组轮换：Tape 15 / GIWA 5 / BTC 0 / Starknet+DogeEVM 0。
- silent：1903%11=0 打新，SILENT_MEN 1 次 25 帖，录取 spiritsrh。下一轮 lane=挖矿。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 52+；在库作者 12；新作者 172，短名单保留 118。

## 收录与在库

- **新收录 spiritsrh / SpiritsRH（@spiritsHOOD）**：2026-11-16 12:53:13 CST 开号，0 粉、1 条推文。官网 https://spiritsrh.surge.sh/ HTTP 200 已核验。13:46 CST 官帖宣布白名单开放（关注/点赞/转推/引用 + 站内表单提交 RH 链钱包与 X handle），表单经 formsubmit.co 发往 Gmail。官帖「LIVE」指项目/白名单已开，**不是**免费 mint LIVE；mint 日期、合约、OpenSea drop 链接均未公布，本轮未核验 OpenSea 收藏。免费登记已开 → notify。focus=false。进 userFollowWatch + freeMintWatch。
- **新收录 unicorn-grand-prix / Unicorn Grand Prix（@UnicornGPrix）**：2026-11-15 18:45:31 CST 开号，30 粉。官网 https://unicorngrandprix.xyz/ HTTP 200 已核验。RH 链 3,333 免费 mint（0 ETH，只付 gas），日期 TBA。bio 写白名单已开，但官网白名单页本轮写 opens soon 且「not reachable right now」，**不要当成已可提交**。门槛：RH 链 ≥$5 ETH + ≥10 笔交易。未公布合约，OpenSea 收藏本轮未核验。真新 → notify。不是免费 mint LIVE。focus=false。进 userFollowWatch + freeMintWatch。与已在库 unicornxdotfun 不是同一项目。
- **新收录 isomatrica / Isomatrica（@isomatricaaa）**：2026-11-13 23:48:49 CST 开号，8 粉。官网 https://isomatricaa.netlify.app/ HTTP 200 已核验。官网写 Ethereum（ERC-721）、Mint Not Yet Live、白名单 Now Open（收 Ethereum 地址）；13:43 CST 官帖与 bio 写 Robinhood Chain + OpenSea 发射。**链口径冲突本轮不裁定**。未公布日期与合约。旧收藏页 https://opensea.io/collection/isomatrica-art 仅解析到 URL（SPA），未核验状态。真新（站内白名单开放）→ notify。不要写成免费 mint LIVE。focus=false。进 userFollowWatch + freeMintWatch。
- **tapeai ≤2h**：BEM 预存仍是既有 2026-11-16 16:00 CST（R1897 已按首次补出钟点提醒）。现约 14:13 CST，距窗口约 1.7h，已进入 ≤2h，预存尚未开始。@tapeupio 14:01 CST 官方 Watch 帖（https://x.com/tapeupio/status/2122208412662726779）复述同一时刻，t.co 指向已记录的 @TapeAIAgent 官帖 https://x.com/TapeAIAgent/status/2122159276403851324；该帖另述预存空投 630,000 TAI 按积分、检察官空投 420,000 TAI 按快照时已质押 Inspector 数量。2% / 快照具体钟点仍未核验。不要写成预存已经开始。勿标 Elysium。le2h=true，notify。tapeup 卡只补一句「将在 TapeUP 进行」，不单独再推。
- **pingpay**：本窗继续同一套回复发射/付款教程，同一份已提醒产品，不重推。
- **runin-ai**：本窗继续「when the window opens」预热，CA 仍为 0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6，不是新的已开窗时刻，不重推。
- **pumptok / paidtok / creedo / wrapped-eth / zyro**：同一份已提醒口径，不重推。wrapped-eth 本轮未再探测 /claim，不得写成 claim 已开放。zyro 不要编造市值。
- **不重推**：tape-exit 同一份只读/备份退出界面；hood-bitz 未改 11-17 时间表；hokori-quantum 仅建设口号；microfrens mint 已完成。
- 尚未 ≤2h：Bombshell Cats AL 11-16 20:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST。hooja-fun UNVAULT 仍仅有日期无时刻。
- 预拒 / skip：
  - AnFeng0858：TapeOut 布道者个人号，R1901/R1902 已 skip，本窗仍无独立官号或站点。
  - LongLaunches：Robinhood Chain 发射提醒聚合号，本窗在报 Pons 上的 $Marvin，非新项目官方账号。
  - hajime_umemiva 等第三方在推 @tsbdotfun（The Shadow Born）免费 mint / Phase 1 表格，已在库，不新建卡。
  - CompanionsWfit / Trovehaven / PlayPixelora / Mendlings / PayphoneNFT / Hood Drive 的第三方白名单模板或转帖：已在库，不新建卡。
  - 0xipanx / GitafPad：作者自述 GIWA Sepolia 测试网社区发射台，Testnet only / no real funds，不新建卡。
  - lovebarlin 等第三方为 @Bullshot911 拉新，非新官号。
  - alexinsaan / Alvinppw 等空转/转帖号。
  - bramble_game：若再出现仍不是 @Bramble_fi。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 823 Elysiumgloom。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent：已跑 打新；下一轮 挖矿。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。
- watchLeaks=0。新卡已进 Watch。

## 不重推（沿用并补充）

- SpiritsRH 本轮已按「免费白名单已开、mint 未开窗」提醒；同一份 surge.sh 表单 / 同一份「日期与 OpenSea drop 待官 X 公布」不重推。补公布并核验 mint 日期或 OpenSea drop、进入 ≤2h，或免费 mint 实际开窗再提醒。不要把官帖「LIVE」写成免费 mint LIVE，不要编造合约。
- Unicorn Grand Prix 本轮已按真新提醒；同一份「免费 mint 已官宣、日期 TBA、白名单页 opens soon / 暂不可达」不重推。白名单实际可提交、补公布并核验 mint 日期、进入 ≤2h，或免费 mint 实际开窗再提醒。不要把 bio「Whitelist is open」写成已可提交，不要编造合约。
- Isomatrica 本轮已按真新提醒；同一份「站内白名单开放、Mint Not Yet Live、官网 Ethereum vs 官帖 Robinhood Chain 口径冲突」不重推。官方澄清链/发射台、补公布并核验日期或合约、进入 ≤2h，或免费 mint 实际开窗再提醒。不要自行裁定哪条链为准，不要写成免费 mint LIVE。
- TapeAI BEM 预存本轮已按进入 ≤2h 提醒（既有 16:00 CST 时刻，尚未开始；@tapeupio 14:01 CST 复述同一官帖）。同一份窗口不重推；预存实际开启，或官号补全并核验检察官快照时刻再提醒。不要写成预存已经开始。勿标 Elysium。
- PingPay 已按真新提醒（R1902）；同一份官网 CA、同一份 DexScreener Solana/pumpfun 池（报价币 PAID、liquidity=null）、同一份 `/api/coins` 6 枚示例币、同一份 X 回复发射/付款指令不重推。出现已核验的新产品入口、改 CA，或出现免费窗口再提醒。不要写成 SOL 配对，不要编造流动性或持有人数，不要写成免费 mint，也不要把 pump.fun 403 写成已打开币页。
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
- runin-ai 同一份「window 尚未开 / Agent ID PoW mining preheat」、同一 CA `0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6` 不重推；补公布并核验开窗时刻或新的可操作入口再提醒。不要把「Soon, launching your own fair mint」写成已上线。
