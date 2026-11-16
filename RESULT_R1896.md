# RESULT R1896

- time: 2026-11-16 10:40 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 895 → 870 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: voxel-world-pixel, liquid-reserve
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit abca1ac R1895）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=895），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent LayerZero 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=895（UF1 后页脚 894/1000）。25 次读取后 remaining=870。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 294 pocket_rh 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 67。NF_skip 17（rinseddotfun / hollytallycheck / divade_xyz / LiquidityStonk / Agent__arena / playholeshot / FlotyllOnRH / Agentkey_ / use_moche / luckycatchgame / LongBaoLNB / DavidJohnsvcen / firstpadfun / Obelisdotfun / tickupfun / darkllartech / Headroom_X），全部为本轮新写入 NF_skip。firstKept pocket_rh，lastKept OrvexLabsxyz。next 360 Headroom_X（已在 NF_skip，下轮将首个跳过）。
- MUST1：24 个 live/窗口号；MUST2：10 个（inklegions / hoojafun / usePaidTok + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 109 号 5 片全读（26+25+26+26+6）。THIN1 / THIN3 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T01:00:00Z（约 1.5h，与 R1895 official 00:30Z 窗口重叠约 1h）；KW 与 mentions 自 2026-11-16T00:30:00Z（约 2h）；silent 自 2026-11-15T02:26:00Z（约 24h）。空结果：UF1 / UF2 / THIN1 / THIN3 / THIN5 / KW_MINE / MEN_MINE。
- mentions 4 组轮换：LayerZero 3 / Elysium+kinetiq 17 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 1。
- silent：1896%11=4 LayerZero。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（25 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 0，admitted 0。下一轮 lane=Elysium。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]。

## 信号与结论

新录取 2 张（voxel-world-pixel、liquid-reserve）。无 ≤2h 新窗口。watchLeaks=0。判断/文案走 DeepSeek，dsFallback=false。notify=true：两张均为真新收录。在库卡均无新的首次可操作变化，不重推。已把两张新卡写入 forcePanelIds，并分别补进 freeMintWatch+bnAgentWatch / elysiumWatch。两张新卡 focus=false。

- **voxel-world-pixel**（真新，notify）：@VoxelWorldPixel（开号 2026-07-14，粉 2，tweet_count=6）。本轮约 10:26 CST 官帖 https://x.com/VoxelWorldPixel/status/2122152767557185736 给出 BSC 合约 `0x097E34c0A1657537aA0D94d171D39AB3954Fee57`，并称昨晚免费 mint 售罄、站点旧缓存已修复。官网 https://voxelworld.fun/ HTTP 200，首页即有 Connect Wallet + doMint('paid') / #mint（/mint /app /claim 独立路由本轮 503）。站点徽章：“Free Mint Sold Out · Genesis Live · BNB”；Genesis 标价 0.0015 BNB、max 5 per wallet。站点还写免费 1,000 份 “SOLD OUT — all 1,000 claimed in under an hour”，此说法仅来自站点文案，本轮未独立链上核对份数。Sourcify chainId 56 exact_match，verifiedAt=2026-11-15T18:55:00Z（2026-11-16 02:55 CST）。BSC public RPC 约 10:32 CST：合约存在（bytecode 19586 bytes），name()=“Voxel World Pixel”，symbol()=“VOXEL”，owner()=0x2f2146666221191f946d12acc925546902208f2a；totalSupply() 在该 RPC 上 revert，已铸/Genesis 剩余份数未取到，勿引用任何铸量数字。不是免费 LIVE，当前只剩付费 Genesis。本号不自动 mint。
- **liquid-reserve**（真新，notify）：@xliquidreserve（开号 2026-11-14，粉 1）。官网 https://liquidreserve.xyz/ HTTP 200（JS shell），twitter:site=@xliquidreserve。官帖称 $liquid live on Ascend，Elysium CA `0x247c91C14b5Aa1cF57f02d638B0287F5cd69E9f6`。DexScreener Elysium uniswap v4 liquid/WHYPE 池约 2026-11-16 06:21 CST 创建，priceUsd=0.000003239，MC/FDV=3239，h24 vol=855.41，liq.usd=3238.81，h24 买/卖 7/4；页面 https://dexscreener.com/elysium/0xe522ea941342149346fa6641ad358ac49d8bf10abec2bba9106ac6bcc42b210c 。另有极薄 liquid/HYPE 池约 10:04 CST 创建，liq.usd=13.31，vol 0。风险：官帖另提 Solana `71mfKdePwyWXtiF1mqu2aaCdMKnKuN664z2vEM2Xpump`，但 DexScreener 显示该地址是 “Meme Liquid” / LIQUID，站点 https://memeliquid.io/ ，官推 https://x.com/MemeLiquidio ，pairCreatedAt=2026-02-08 04:54 CST，MC=53336，属另一公共身份，不得当作本项目已核验 Solana CA。不是免费 mint。流动性极薄。本号不自动买卖。
- **paidtok**（在库）：官号继续产品帖并提到 $BEAST for @mrbeast，同一 live pad / 同一已核验 CA，无新的首次开窗，不重推。
- **hooja-fun**（在库）：10:04 CST 仍是同一组已提醒 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，无钟点）；10:27 回复链到该帖配图。不重推；非 ≤2h。
- **microfrens**（在库）：09:59–10:00 CST 官帖称 Mint is Complete、Reveal 约 20 分钟内。mint 已结束，reveal 不是新的首次可操作窗口，不重推。
- **dualforge-bsc**：09:40 CST “Day two at the forge”，同一已开闸窗口进度，不重推。
- **sunfall-world**：S1 已结束、S2 game on，与已覆盖进度一致，不重推。
- **wrapped-eth / wowpad / void-giwa / gekko-launchpad / monko-mania / owlgate / hood-bitz**：本窗无新的首次 mint 窗口，只刷 lastChecked。
- **inklegions / cipher-syndicate**：本轮官方窗口无新帖。Ink Legions 开铸仍 2026-11-17 03:00 CST 免费 mint；Cipher Syndicate 仍 2026-11-17 00:00 CST。均非 ≤2h，已提醒不重推。
- 预拒 / skip：
  - **@Rezofun**：开号 2026-11-15T23:19:07Z，粉 5，tweet_count=8，bio 误写 “@LayeZero_Core”，无官网、无 CA、无开窗；仅 LayerZero 挂靠预告视频。skip/defer。
  - **@VitrumFalcons**：仅出现在第三方 @kombatrh 转帖（“Free mint November 18 on OpenSea, 5000 Falcons on Robinhood”），本轮未拉官号时间线/站点、无合约，非 ≤2h。skip/defer。
  - **@SocialGruff**：仅第三方 RT “coming to DogeOS”，无官网/无核验/无窗口。skip。
  - **@usesparkpad / Spark**：仍是 R1895 已 skip 的同一条 09:51 CST demo-site 官帖（tryspark.fun 源码写明浏览器模拟），继续 skip。
  - **@MyelysiumWP / @ClientSearchApp**：R1895 已 skip（研究工具 / Peerlist 非加密），本窗无新证据。
  - **@PlunderPort**：库内已有卡；本轮官方窗口无新帖，“3333 免费 mint / 扩容”说法来自第三方，不改时间表不重推。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 360 Headroom_X。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：已跑 LayerZero；下一轮 Elysium。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- Voxel World Pixel 本轮已按真新提醒；同一份付费 Genesis（0.0015 BNB）/ 同一 CA 不重推，除非出现新的免费窗口、改 CA，或 Genesis 售罄/关闭被核验。站点“免费 1,000 份已售罄”未独立链上核对，勿把未核验铸量当事实再推。
- Liquid Reserve 本轮已按真新提醒；同一份 Elysium CA / 同一 Ascend 池行情不重推，除非出现免费窗口、官号澄清或撤回 Solana CA，或流动性/交易出现新的可操作变化。勿把 `71mfKdePwyWXtiF1mqu2aaCdMKnKuN664z2vEM2Xpump` 当作本项目 Solana CA。
- PaidTok 同一份 CA / 同一泵池行情不重推，除非出现免费窗口、改 CA，或出现新的可操作发射/结算变化。
- hooja-fun 同一份 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，未给时刻）不重推；补公布具体时刻、进入 ≤2h，或实际开窗再提醒。
- MicroFrens mint 已完成 / reveal 倒计时不重推，除非出现新的首次可操作窗口或新集合 LIVE。
- DualForge 同一已开闸窗口的 day-two 进度不重推。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- sunfall-world Season 1 结算与 Season 2 开赛宣传不重推，除非出现新 mint/登记窗口。
- payphone-rh 同一份社区 “FREE MINT this week” 不重推，除非官号公布开窗时刻或确认 LIVE。
- 沿用 R1895/R1894/R1893/R1892：deadhood 售罄确认、hood-bitz 无 BITBOTZ 开窗时刻、shielded-wizards Ledgermaw raid、zerolotl 主网将至介绍、banknotes_btc “this week”、Hokori 燃烧已落地但官网无用户入口、wrapped-eth 会计示例且 /claim 仍 404。
- 其余已提醒窗口沿用：pillowbook 同一未开盘窗口、jacketagent 付费阶段无新变化、ozero 同一份 Base Sepolia 测试网宣传、TapeMine/Behemoth 二期进度、raccoonslimestd 仍在选择发射台、Elysium Portals 免费登记未见合约、boxcars 进度/箱子奖励刷新（除非预售开盘/改期、驾照售罄、改入口/改 CA）。
- Spark 继续 skip；Rezofun / VitrumFalcons / SocialGruff 本轮 skip/defer，不建卡。若官号公布真实程序/CA、开窗时刻或出现已核验站点，再收录并提醒。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint / 不自动买卖。
