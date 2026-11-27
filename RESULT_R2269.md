# RESULT R2269

- time: 2026-11-27 10:42:27 CST（Asia/Shanghai）
- mode: ample（remainingBefore=806，softCap 28 / minSpend 20 / silentCap 2；lastFullAfterReset=2264，本轮为重置后常规全栏，不是第二次全量补扫）
- xReads: 37（UF 3 + MUST 2 + KW_CORE 6 + KW_THIN30 6 + KW_THIN24 5 + MEN 4 + THIN_WATCH 10 + SILENT_MEN 1；无单独 PROBE；无额外/重复 X 查询）
- remaining: 806 → 769 / 1000（reset 2026-11-28 08:00 CST）
- slightly over softCap：额度充足，须跑全十栏 + 5 组瘦栏 24h 补搜 + 薄 Watch，未砍栏
- dsFallback: true（DEEPSEEK_API_KEY 仍在，DeepSeek HTTP 401 invalid api key，评分与文案本地兜底）
- notify: true（新收录含 BlockPay Genesis 免费 mint LIVE，freeLiveForcedNotify=true，告警须点名；另 7 项 watching 均不是免费 mint）
- discordPeekDeferred: true，loginOk=false（未开浏览器、未重发登录表；登录墙约自 R2206；lastSeen 仍 2026-11-23 22:19–22:56 CST）

## 新收录

- **BlockPay Genesis**（id `blockpay-genesis` / @BlockpayGenesis / https://www.blockpay.world/）
  - 建号 2026-11-23 16:55:50 CST，本轮 21 粉 / 11 帖
  - **免费 mint LIVE**（必须通知）：官网写总供 3333、免费额 1111（1 钱包 1 份，仅 gas），本轮显示已铸 266、免费剩余 845；函数 `freeMint()`，自称合约 `0x0BF3Cf8eEeC4fE71305738c75aA9574A24DDf57b`
  - 官帖 2026-11-27 10:27:04 CST（https://x.com/BlockpayGenesis/status/2126140721128518043）称免费额 266/1111、今天结束，之后 0.001 BNB；付费至 12-01 12:00 UTC，Element 上架 12-02
  - 关窗口径：第三方/日历写 2026-11-27 12:00 UTC = **20:00 CST**（约 9.5h，不是 ≤2h）
  - 官网 HTTP 200；资料栏指向 Discord（https://discord.gg/FE6YCGFFhP），官网静态页未回链官推（siteXMutual=false）；Telegram 转载确认官推与官网。仍建卡（有可指认官网 + 官号）
  - 自称支持 Binance Agentic Wallet 合约调用，但任意钱包也可 freeMint（非仅 Agent ID）
  - 栏位：打新，status=live，focus=false；已进 userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch
  - 合约/权限未本轮链上核验；高风险
  - 本号不自动 mint

- **Asyncium**（id `asyncium` / @asyncium / https://asyncium.com）
  - 建号 2026-11-27 04:06:08 CST（今天），本轮 33 粉 / 19 帖
  - 官网 HTTP 200，标题 Asyncium: async HyperCore, settled，页脚/twitter:site 回链 @asyncium（互证）
  - 自称 Elysium 合约向 HyperCore 下单并回收据，另提供 MCP/agent 工具；官网写 $ASYNC 已 live，CA `0x3a6d21bafa830c9571ee2aa63629451255b63f6c`（未链上核验）
  - 官方生态页本轮 429，未核到挂名，**不进 Elysium 栏**（台子/Meme，focus=false）；仍挂 elysiumWatch
  - 不是免费 mint；已进 userFollowWatch + elysiumWatch
  - 本号不自动 mint

- **Ionia**（id `ionia` / @ioniamarkets / https://ionia.markets）
  - 建号 2026-11-21 19:51:11 CST，本轮 7 粉 / 1 帖
  - 官网 HTTP 200，twitter:site 回链 @ioniamarkets（互证）
  - 官帖 2026-11-27 10:32:47 CST（https://x.com/ioniamarkets/status/2126142159950589956）称 Ionia is live，并给 $IONIA CA `0x65adf7baf31087a6209eca153682c7475c15f8b4`（未链上核验）
  - 自称 Elysium+Hyperliquid 期权层；生态页 429，**不进 Elysium 栏**；已进 userFollowWatch + elysiumWatch
  - 不是免费 mint；focus=false
  - 本号不自动 mint

- **Lockium**（id `lockium` / @TryLockium / https://lockium.org/）
  - 建号 2026-11-03 00:45:50 CST，本轮 56 粉 / 18 帖
  - 官网 HTTP 200，标题 Lockium: token locks & vesting on Elysium，twitter:site=@TryLockium（互证），静态页主体为 JS 壳
  - 自称 Elysium 代币锁仓/归属工具；生态页 429，**不进 Elysium 栏**；已进 userFollowWatch + elysiumWatch
  - 不是免费 mint；focus=false
  - 本号不自动 mint

- **NEXEL**（id `nexel` / @NEXEL_ely / http://usenexel.com）
  - 建号 2026-10-14 22:54:24 CST，本轮 62 粉 / 37 帖（库内此前未建卡，本轮补收）
  - 官网 HTTP 200，标题 NEXEL · Compute, metered onchain，twitter:site=@NEXEL_ely（互证），静态页较薄
  - 官帖自称 Live on Elysium，并给 $NEXEL CA `0x2c41ff518f0a9ea28fab7047055545c5ff3552d3`（未链上核验）
  - 生态页 429，**不进 Elysium 栏**；已进 userFollowWatch + elysiumWatch
  - 不是免费 mint；focus=false
  - 本号不自动 mint

- **Curbwire**（id `curbwire` / @curbwirelive / https://curbwire.live）
  - 建号 2026-11-26 12:19:37 CST（昨天），本轮 51 粉 / 59 帖
  - 官网 HTTP 200 并回链 @curbwirelive（互证）；自称 Robinhood Chain ANT 价格链上日志
  - 页面/帖文出现多个合约地址，未本轮链上核验
  - 栏位：台子/Meme，focus=false；已进 userFollowWatch
  - 不是免费 mint
  - 本号不自动 mint

- **Rostrum**（id `rostrum` / @rostrumsale / https://www.rostrum.sale/）
  - 建号 2026-11-23 03:07:14 CST，本轮 87 粉 / 13 帖
  - 官网 HTTP 200 并回链 @rostrumsale（互证）；自称 Base 代币发行拍卖行，页面写 Pre-launch、No sale is live，可加入名单
  - 候补名单 ≠ 免费登记 / 免费 mint，也不是已开售 LIVE
  - 栏位：台子/Meme，focus=false；已进 userFollowWatch
  - 本号不自动 mint

- **Tessel**（id `tessel` / @tesselfamily / http://tessel.family）
  - 建号 2026-11-25 11:39:54 CST，本轮 73 粉 / 10 帖
  - 官网 HTTP 200 并回链 @tesselfamily（互证）；自称 AMM/流动性协议
  - 页面出现若干合约地址，未本轮链上核验
  - 栏位：台子/Meme，focus=false；已进 userFollowWatch
  - 不是免费 mint
  - 本号不自动 mint

## 更新但不重推

- lumixpad：官帖续推约 14 hours left until $LUMIX，非 ≤2h；R2265 已提醒，不重推。
- crawlers-agent：自称转介/mint 窗今晚结束，官网仍写 MINT · OPENING SOON；非 ≤2h，R2268 已记，不重推。
- runin-ai：MUST 再见每日 20:00 CST $RMINE 窗宣传，无新的免费 mint 开窗，不重推。
- OUTLAWSxNFT：免费 mint 仍 2026-11-27 21:30 CST（约 11h），未到首次 ≤2h，不重推。

## 跳过 / 看见但未建卡

- **MORFO TRADE**（https://morfotrade.pages.dev/）：官网自称 Binance Agent ID 免费 soulbound 卡 LIVE，关窗 2026-11-27 23:59 WIB（约 2026-11-28 00:59 CST，不是 ≤2h），卡合约口径 `0xB22aC9b2…C718186`。官网与本轮公开页均未挂官推，硬禁「无官推误判」，本轮未建卡、未发明 handle。请自行甄别站点。
- d1.exchange（@d1_exchange / http://d1.exchange）：Private preview / 口令墙，页内无回链，互证弱，跳过。
- Vested（@vestedfun / https://usevested.fun/）：Cloudflare 拦截/跳转可疑，未完成官网核验，跳过。
- SquadOnPump（@SquadOnPump）：1 粉 / 1 帖，资料栏无官网，跳过。
- ballastperps：R2266 已跳（Hyperliquid，仅自称 anchored on Elysium），不建卡。
- igotsomadi：R2267 已跳，不建卡。
- TapeOut 刷屏（@binbin181818 等）：mentions/Tape 噪音，不建卡。
- 静号 GO盘 7 条命中多为体育黑话，无新静号官号。

## 覆盖

- userFollow：优先 8 号 + 分片 87 @zkblast9 起 50 个（shard 内 NutshellMarkets / squeekchain 与 UF_PRI 去重，实际分片查询 48），末号 @Synklings。下轮起点 **137 @napkinrh**。刷完本轮分片，未回绕。UF 表在新收录后 **2498**。
- 十栏关键词都跑到：核心 30m（打新/挖矿/台子/GO/Elysium + BN Agent；挖矿含 Nutshell/squeek，BN 含 STARX/X Layer）+ 瘦栏 30m 六组。
- 瘦栏 30m：LayerZero 0、Tape/电路 22、GIWA 2、DogeEVM 1、BTC 0、Starknet 1。**<5 才补 24h**：LayerZero / GIWA / DogeEVM / BTC / Starknet 各 1 次（各 25 命中）。Tape=22 未改 24h。
- mentions 本轮轮换（45m）：Tape 16、GIWA 2、BTC 1、Starknet+DogeEVM 0。下一轮：**Elysium+kinetiq / LayerZero / pads+squeek+STARX / BN+STARX**。
- 薄 Watch 45m 官号 from: 已扫（同 handle 本轮只拉一次）。
- 静号：轮换栏 **GO盘**；connectors/x 无 search_users，只跑 24h mention（7 命中，无新静号官号）。下一轮静号：**LayerZero**。
- Canton/Glaze/TokenWorks lastChecked 软刷。
- Discord Peek 本轮仍延期，见上。不打开浏览器、不重发登录表。
- Elysium 官方生态页本轮再 429 / Vercel checkpoint。

## 面板

- 已写 data.json，并同步 docs/data.json。
- 本轮只提交 data.json + docs/data.json + RESULT_R2269.md。
- 面板 https://reboot7454.github.io/early-scout/
