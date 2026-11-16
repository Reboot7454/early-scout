# RESULT R1897

- time: 2026-11-16 11:08 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 870 → 845 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: whale-fun, bombshell-cats
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit 7c8eda6 R1896）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=870），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent Elysium 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=870。25 次读取后 remaining=845。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 360 Headroom_X 起（已在 NF_skip，首个跳过）packed 2 片 kept 50（25+25），wrap=false，walkScanned 76。NF_skip 26，其中 8 个为本轮新写入（bnAgent_ / AgentID_AI / PrinterAi_BNB / telefees_pump / agentkin_ / AgenticHive / pitpadfun / torpornet）；其余 18 个已在列（含 Headroom_X / SwarmHiveBNB / twinmetahq / astrispace 等）。firstKept graveonchain，lastKept ACRE_io。next 435 astrispace（也在本轮 NF_skip，下轮将首个跳过）。
- MUST1：24 个 live/窗口号；MUST2：13 个（inklegions / hoojafun / usePaidTok + VoxelWorldPixel + ephemeral_eth + escape_hub + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+26+5；gazuaxyz 已落入 UF1 去重）。THIN3 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T01:30:00Z（约 1.5h，与 R1896 official 01:00Z 窗口重叠约 1.5h）；KW 与 mentions 自 2026-11-16T01:00:00Z（约 2h）；silent 自 2026-11-15T02:57:00Z（约 24h）。空结果：UF2 / THIN3 / THIN5。
- mentions 4 组轮换：Tape 25 / GIWA 2 / BTC 2 / Starknet+DogeEVM 2。
- silent：1897%11=5 Elysium。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（25 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 0，admitted 0。下一轮 lane=Tape。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]。

## 信号与结论

新录取 2 张（whale-fun、bombshell-cats）。无 ≤2h 新窗口。判断/文案走 DeepSeek，dsFallback=false（DeepSeek 误把两张新卡 lzVerified=true，apply 已强制改为 false，二者均非 LayerZero）。notify=true：两张真新收录 + 两张在库卡首次补出具体可操作时刻（hood-bitz BITBOTZ、tapeai BEM 预存）。已把两张新卡写入 forcePanelIds；whale-fun 进 userFollowWatch+agentPadWatch，bombshell-cats 的 candidateId 补进已有 @1KArtGallery 的 userFollowWatch+freeMintWatch。两张新卡 focus=false。

Watch 漏挂修复（在库但不在任何 Watch，当场补进）：hood-bitz / @Hood_Bitz（R298）→ freeMintWatch + userFollowWatch；forge-elysium / @forge_elysium（R1505）→ elysiumWatch + userFollowWatch。round≥1840 的 leak 检查仍为 0。

- **whale-fun**（真新，notify）：@Whalefun_io（开号 2025-06-03T19:07:57Z = 2025-06-04 03:07 CST，粉 1313，tweet_count=286）。官网 https://whalefun.io/bnb HTTP 200，Official X 与 @Whalefun_io 互认；文案为 BNB Smart Chain 公平发射协议，两种模式 Fixed-price Fair Mint 或 Bonding Curve，auto-lists on the DEX，No presale/no insiders；CertiK 报告 https://skynet.certik.com/projects/whale-fun 。本轮 10:18 CST 官帖 https://x.com/Whalefun_io/status/2122152373644861752 介绍双模式。站点列表当前 Newly created 0 / Graduating 0 / Live on DEX 0，无代币 CA。不是免费 LIVE，也没有可打的发射中代币，先观察首批标的。本号不自动 mint。
- **bombshell-cats**（真新 + 免费 AL，notify）：@1KArtGallery 第五个集合（库内旧卡 1k-art-gallery 是已过期的 Time Travelers，未覆盖、不重推旧卡）。官帖 10:33–10:37 CST，例如 https://x.com/1KArtGallery/status/2122157019910066569 。官网 https://1kgallery.com/collection/bombshell-cats/ HTTP 200：Art Dealers AL 2026-11-16 07:00 AM New York = 2026-11-16 20:00 CST 免费（112 钱包，最多 3/钱包）；Public 2026-11-17 07:00 AM New York = 2026-11-17 20:00 CST 起至 2027-02-15，0.0003 ETH，3/钱包。OpenSea https://opensea.io/collection/bombshell-cats/overview 本轮有 “Minting now” 标签，但 24h volume/地板均为 $0；官方时刻尚未到，不以该标签当作已开放的 LIVE 证据。未核验集合合约。免费仅限已登记 Art Dealers，不是公售免费。非 ≤2h（距 AL 约 9h）。本号不自动 mint。
- **hood-bitz**（在库，首次补出时刻，notify）：10:38 CST 官帖 https://x.com/Hood_Bitz/status/2122157433447661680 首次给出 BITBOTZ 时刻。888 供应；快照 Monday Nov 16 1:00 PM EST = 2026-11-17 02:00 CST；开铸 5:00 PM EST = 2026-11-17 06:00 CST；每枚已下架 Hoodbitz 可免费 mint 1 个；仅持仓、无公售；揭示为开铸后 24h。非 ≤2h（距开铸约 19h）。粉已更新为 492。先前 RESULT 写「无 BITBOTZ 开窗时刻、补公布再提醒」，本轮按该约定提醒。
- **tapeai**（在库，首次补出时刻，notify）：10:46 CST 官帖 https://x.com/TapeAIAgent/status/2122159276403851324 首次给出 BEM 预存钟点：2026-11-16 16:00 CST（UTC+8）；预存按积分分享 630,000 枚 TAI（占总量 3%），1 BEM=1 积分，直邀 20% / 间邀 10%。2% 检察官空投的「快照时间：11」在配图中被截断，本轮未读图，未核验快照时刻，不要编造。非 ≤2h（距预存约 5h）。站点仍 https://tapeai.net/ 。勿标 Elysium。R1856/R1857 已记日期但无钟点、当时不按新窗口推送，本轮按补公布时刻提醒。
- **1k-art-gallery**：只刷 lastChecked，并注明同官号新集合已另建 bombshell-cats；旧 Time Travelers 时间表保持已过期，不重推本卡。
- **forge-elysium**（在库，不重推）：确认官网 https://forgeonelysium.com/ HTTP 200，前端 JS 官推为 @Forge_elysium，与库内 handle 一致；Uniswap v4 Hook Blocks 发射协议，JS 中 TokenFactory/Router 仍标 (not deployed)。无新 mint/开窗。线索来自 @onlyfrensbiz 目录提交，该号不是 FORGE 官号。不要把 JS 里的 LP Locker `0x406838c47575171453D6F94A9e73f197BF464289` 或报价代币 `0xb47c4c8f73f009cc0c0d3f92b388d13e293f0b65` 写成已核验的项目代币 CA。
- **escapehub**：官帖称 Android 已上 Google Play；上线仍是 2026-11-16 23:00 CST（15:00 UTC），该时刻此前已提醒（R1684），不重推。
- **ephemeral-eth**：本窗无新帖，上线仍 23:00 CST，此前已提醒，不重推。
- **不重推**：usePaidTok 同一 live CA / 产品帖；hooja-fun 同一份 UNVAULT 日期 11-17/11-18 无钟点；MicroFrens mint 完成 / reveal；VoxelWorldPixel 同一份已提醒的付费 Genesis（0.0015 BNB）；DualForge day-two；sunfall-world S2；wowpad 建设中；void-giwa / gekko / owlgate / wrapped-eth 评论或会计说明。
- **inklegions / cipher-syndicate**：本轮沿用已提醒时间表。Ink Legions 开铸仍 2026-11-17 03:00 CST 免费 mint；Cipher Syndicate 仍 2026-11-17 00:00 CST。均非 ≤2h，已提醒不重推。
- 预拒 / skip：
  - **@elysium_lords**：本窗多为 bankrbot 发射请求，t.co 只解析到自身推文，无官网/CA/开窗。skip。
  - **@HOODVERSENFTs**：HV Pass「今日 14:00 UTC / 22:00 CST 免费 mint」仅第三方转帖，本轮未拉官号，按与 VitrumFalcons 相同标准 skip/defer。
  - **ChaoticorderNFT**：1111 免费 mint 为第三方赠送转帖，未核验官号。skip/defer。
  - **@geeduppppp / ANICET**：仅 gauging interest，无日期。skip。
  - **@SocialGruff**：R1896 已 skip，本窗无新核验。继续 skip。
  - **@themitecho / MitechoSwap**：GIWA Sepolia 测试网 Ammora SDK 工具演示，非主网可打新。skip。
  - **@quityourjobfun $QUIT**：已毕业至 PumpSwap，属已毕业 memecoin 行情，不新收。skip。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 435 astrispace。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent：已跑 Elysium；下一轮 Tape。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- Whale.Fun 本轮已按真新提醒；同一空列表发射台不重推，除非出现首批可参与的发射（Newly created / Graduating / Live on DEX 不再为 0）或官号给出已核验 CA/开窗。
- Bombshell Cats 本轮已按真新+免费 AL 提醒；同一份 11-16 20:00 CST AL / 11-17 20:00 CST 公售时间表不重推；进入 ≤2h、确认 LIVE，或公布已核验合约再提醒。不要把 OpenSea “Minting now” 标签当成已经开放。
- hood-bitz / BITBOTZ 本轮已按首次补出时刻提醒；同一份 11-17 02:00 CST 快照 / 11-17 06:00 CST 开铸、仅已下架持仓、无公售的时间表不重推；临近 ≤2h 或实际开窗再提醒。
- TapeAI BEM 预存本轮已按首次补出 16:00 CST 钟点提醒；同一份预存窗口不重推；进入 ≤2h、预存实际开启，或官号补全并核验 2% 检察官快照时刻再提醒。
- Voxel World Pixel 同一份付费 Genesis（0.0015 BNB）/ 同一 CA 不重推，除非出现新的免费窗口、改 CA，或 Genesis 售罄/关闭被核验。
- Liquid Reserve 同一份 Elysium CA / 同一 Ascend 池行情不重推，除非出现免费窗口、官号澄清或撤回 Solana CA，或流动性/交易出现新的可操作变化。勿把 `71mfKdePwyWXtiF1mqu2aaCdMKnKuN664z2vEM2Xpump` 当作本项目 Solana CA。
- PaidTok 同一份 CA / 同一泵池行情不重推，除非出现免费窗口、改 CA，或出现新的可操作发射/结算变化。
- hooja-fun 同一份 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，未给时刻）不重推；补公布具体时刻、进入 ≤2h，或实际开窗再提醒。
- MicroFrens mint 已完成 / reveal 倒计时不重推，除非出现新的首次可操作窗口或新集合 LIVE。
- DualForge 同一已开闸窗口的 day-two 进度不重推。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- sunfall-world Season 1 结算与 Season 2 开赛宣传不重推，除非出现新 mint/登记窗口。
- escapehub 同一份 2026-11-16 23:00 CST 上线时刻不重推（本轮仅 Android 上架确认）；临近 ≤2h 或实际开闸再提醒。
- ephemeral-eth 同一份 23:00 CST 上线时刻不重推。
- payphone-rh 同一份社区 “FREE MINT this week” 不重推，除非官号公布开窗时刻或确认 LIVE。
- 沿用 R1896/R1895/R1894/R1893/R1892：deadhood 售罄确认、shielded-wizards Ledgermaw raid、zerolotl 主网将至介绍、banknotes_btc “this week”、Hokori 燃烧已落地但官网无用户入口、wrapped-eth 会计示例且 /claim 仍 404。
- 其余已提醒窗口沿用：pillowbook 同一未开盘窗口、jacketagent 付费阶段无新变化、ozero 同一份 Base Sepolia 测试网宣传、TapeMine/Behemoth 二期进度、raccoonslimestd 仍在选择发射台、Elysium Portals 免费登记未见合约、boxcars 进度/箱子奖励刷新（除非预售开盘/改期、驾照售罄、改入口/改 CA）。
- Spark / Rezofun / VitrumFalcons / SocialGruff / HOODVERSENFTs / ChaoticorderNFT 继续 skip/defer，不建卡。若官号公布真实程序/CA、开窗时刻或出现已核验站点，再收录并提醒。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint / 不自动买卖。
