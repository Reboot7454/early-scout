# RESULT R1895

- time: 2026-11-16 10:12 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 920 → 895 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: （无）
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit efdecf5 R1894）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=920），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent GO盘栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=920（UF1 后页脚 919/1000）。25 次读取后 remaining=895。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 235 swiprdotxyz 起 packed 2 片 kept 49（24+25；hint 50），wrap=false，walkScanned 59。NF_skip 10（swiprdotxyz / GlitchOnHood / rh_ofsherwood / wildlife_uni / layertrade / envarai_ / scripdrop / huntfieldrh / ciowworld / hahastage）。其中 6 个为本轮新写入 NF_skip（swiprdotxyz / huntfieldrh / ciowworld / hahastage 已在列）。firstKept gobbyrobinhood，lastKept ToritoTeamES。next 294 pocket_rh。
- MUST1：24 个 live/窗口号；MUST2：10 个（inklegions / hoojafun / usePaidTok + 7 个优先号）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 105 号 5 片全读（26+25+26+26+2）。THIN1 / THIN3 / THIN5 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T00:30:00Z（约 1.5h，与 R1894 official 00:00Z 窗口重叠约 1h）；KW 与 mentions 自 2026-11-16T00:00:00Z（约 2h）；silent 自 2026-11-15T02:00:00Z（约 24h）。空结果：UF2 / THIN1 / THIN3 / THIN5 / KW_MINE。
- mentions 4 组轮换：Tape 25 / GIWA 5 / BTC 1 / Starknet+DogeEVM 1。
- silent：1895%11=3 GO盘。search_users 仍不在 X 目录；只跑 SILENT_MEN 1 次（7 帖），未再花 get_users_by_usernames（doNotSpendSilentOn 仍为 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT）。sentToReview 0，admitted 0。下一轮 lane=LayerZero。
- 部分查询的 write_to_file 预览在约 6.3KB 处被插入省略标记，已从同目录完整资产文件还原后解析，未重拉同一查询。truncated=[]。

## 信号与结论

无新录取。无 ≤2h 新窗口。watchLeaks=0。判断/文案走 DeepSeek，dsFallback=false。notify=true：满足 R1894 对 PaidTok 所设例外（官推公布并核验 CA + 真实链上发射/交易），并提醒 hooja-fun 首次给出 UNVAULT 日期。已把 hooja-fun 写入 forcePanelIds，以便面板能显示这条日程更新。

- **paidtok**（在库更新，notify）：R1894 已按真新提醒，当时 CA 仅站点声明。本轮 09:23 CST 官帖 https://x.com/usePaidTok/status/2122138539034890738 发出 `ScqzaRCpW4vCze1wc9QCx553PYNC7w7G53b5CQ9pump`，09:24 CST https://x.com/usePaidTok/status/2122138707079934422 称 “Our only CA its not going to change”。DexScreener 公开 API 约 10:08 CST 拉取：mint 名称/符号均为 PaidTok，地址与官推一致；pump.fun 池（计价 PAID，pair `3j2gWcUDXQs2BEDG2TxWTZ2vj25wAn1jdTjSeNbPdaYW`）pairCreatedAt=2026-11-16 09:23:13 CST，priceUsd=0.00001239，marketCap/fdv=12398.27，h24 volume=47408.44，h1 +290，h1 买/卖 989/871；页面 https://dexscreener.com/solana/3j2gwcudxqs2bedg2txwtz2vj25wan1jdtjsenbpdayw 。另有极薄 Meteora-SOL 池（09:45:31 CST 创建，marketCap=17236，h24 volume=1.96，liquidity.usd=1.52）。不是免费 mint / 免费登记。本号不自动买卖。
- **hooja-fun**（在库更新，notify）：10:04 CST 官帖 https://x.com/hoojafun/status/2122148704400576821 首度公布 UNVAULT 日期：DeBugz 周二 11-17，Genesis Bugz 周三 11-18，随后 First Class Frenchies，再后 Hooja。此前口径为 “Not yet, soon”。原文未写具体时刻与时区，不能标 ≤2h，也尚未开窗。
- **microfrens**（在库）：09:59 CST 官宣 “Mint is Complete. Reveal in 20 minutes or less.”；同窗 OpenSea 隐藏/仿盘预警与“买 3 份以上才有免费 mint”讨论已在 R1894 覆盖。mint 已结束，reveal 不是新的首次开窗，不重推。
- **dualforge-bsc**：09:40 CST “Day two at the forge”，trial keys 32 个，付费档仍是 opening tier FCFS、满了涨价、每 24h 一轮，入口 dualforge.fun。官方开闸已在 R1868 提醒，R1874 已说明同一已开闸窗口进度不重推。
- **sunfall-world**：09:34 CST Season 2. Game on（每周奖池等）。Season 1 结算已在 R1894 记录，非新 mint/登记窗口，不重推。
- **cipher-syndicate**：08:31 CST 再发同一份 11-17 00:00 CST AL/公售时间表。距今约 14h，非 ≤2h。已在 R1892 按真新提醒，不重推。
- **payphone-rh**：本窗仅第三方转帖 “FREE MINT this week / last call to allowlist”，与 R1645 已记社区消息同类；官号仍未给出开窗时刻，不重推、不重收。
- **inklegions / Hood_Bitz**：MUST 本窗无这两号新帖。Ink Legions 开铸仍 2026-11-17 03:00 CST 免费 mint，非 ≤2h。
- **tapemine**：二期 #2755 进度帖与上轮同类，不重推。
- 预拒 / skip：
  - **@usesparkpad / Spark**：09:51 CST 官帖称 “SPARK is live”，t.co 展开 https://tryspark.fun/ HTTP 200；但 /spark.html 源码注释原文写明 “Everything here is simulated in the browser: sample offerings, a demo wallet, no transactions.”，前端无 window.solana / sendTransaction / RPC / 程序 ID，未发现已核验 CA。按演示站 skip，不把演示说成可真实打。若日后官推公布真实程序/CA 或出现链上交易再收。
  - **@Nekointhehood / Nekohood**：开号 2026-08-26，粉 297，tweet_count=0，bio 写 free mint；本窗只有第三方/社区转帖称 Robinhood Chain 免费 mint、3000 供应，无官网、无官宣开窗、无合约。defer/skip，待官号发帖或上线站点再收。
  - shellytoken / anubislayer1 已在库或仅科普；myelysiumwp 研究工具；clientsearchapp 非加密 Peerlist。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 294 pocket_rh。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent：已跑 GO盘；下一轮 LayerZero。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap / xChainPadWatch。

## 不重推（沿用并补充）

- PaidTok 本轮已按「官推公布并核验 CA + DexScreener 可见链上交易」短更新提醒；同一份 CA / 同一泵池行情不重复推，除非出现免费窗口、改 CA，或出现新的可操作发射/结算变化。
- hooja-fun 同一份 UNVAULT 日期（11-17 DeBugz / 11-18 Genesis Bugz，未给时刻）不重推；补公布具体时刻、进入 ≤2h，或实际开窗再提醒。
- MicroFrens mint 已完成 / reveal 倒计时不重推，除非出现新的首次可操作窗口或新集合 LIVE。同一份 OpenSea 隐藏/仿盘预警与“买 3 份以上才有免费 mint”讨论继续不重推。
- DualForge 同一已开闸窗口的 day-two / trial keys 进度不重推。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- sunfall-world Season 1 结算与 Season 2 开赛宣传不重推，除非出现新 mint/登记窗口。
- payphone-rh 同一份社区 “FREE MINT this week” 不重推，除非官号公布开窗时刻或确认 LIVE。
- 沿用 R1894/R1893/R1892：deadhood 售罄确认、hood-bitz 无 BITBOTZ 开窗时刻、shielded-wizards Ledgermaw raid、zerolotl 主网将至介绍、banknotes_btc “this week”、Hokori 燃烧已落地但官网无用户入口、wrapped-eth 会计示例且 /claim 仍 404。
- 其余已提醒窗口沿用：pillowbook 同一未开盘窗口、jacketagent 付费阶段无新变化、ozero 同一份 Base Sepolia 测试网宣传、TapeMine/Behemoth 二期进度、raccoonslimestd 仍在选择发射台、Elysium Portals 免费登记未见合约、boxcars 进度/箱子奖励刷新（除非预售开盘/改期、驾照售罄、改入口/改 CA）。
- Spark / Nekohood 本轮 skip，不建卡；若官号公布真实程序/CA、出现链上交易，或 Nekohood 官号发帖/上线站点并给出窗口，再收录并提醒。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint / 不自动买卖。
