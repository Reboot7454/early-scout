# RESULT R2188

- 轮次：R2188（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 17:02–17:16 CST（Asia/Shanghai）。queries 窗口 start30=2026-11-25T08:30:13Z，start24=2026-11-24T09:00:13Z。dry-run lastScout=2026-11-25 17:16:13 CST。
- mode：x_budget.py 在 live remaining=505 时建议 mode=pace、softCap=18、minSpend=18、silentCap=2；因 remaining≫200 且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185–R2187 同一 override；含 MUST_WIN3，因 R2187 新收 3 个官号）。silentCap=2（silent 不计 softCap）。
- xReads=28（main 27 + silent 1），未低于 minSpend
- remainingBefore=505 / 1000（第一笔 UF1 remainingToday=504，+1）；remainingAfter=477（末笔 KW_STARK_24 remainingToday=477；505−28=477，与 live 一致）
- Judgment / admit / score / alert：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score（送审 1 项 Sov Money，admit=true，overall 68）+ 1 次 alert 文案。dsFallback=false
- 本号不自动 mint。notify=true（真新收录 Sov Money，须点名，非免费 mint；另有库内实质变化：4pump $4PUMP、SleighPad $SLEIGH 已公布 CA 并在 pump.fun 上线。The Jacket 已在 R2186 首次≤2h 告警，本轮不重推；ORIPA 收尾时 17:16 CST 尚未到 18:00 CST，不提前告警；TRIFORGE 仅小幅进度，不重推）。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=1，KW_TAPE=25，KW_GIWA=25，KW_DOGE=7，KW_BTC=2，KW_STARK=0
  - KW_MINT=25，KW_MINE=1，KW_PAD=25，KW_GO=24，KW_ELY=19，KW_GAPS=25
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=19、KW_BTC_24=25、KW_STARK_24=25。
- 未跑：KW_TAPE_24（30m=25）、KW_GIWA_24（30m=25）、KW_DOGE_24（30m=7）。MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=1 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1461 @baggieshood 起 50 号至 @TapSeal，next 1511 @Fearnxyz，wrap=false，total 写盘后=2399（原 2398 + 本轮 1 个新收录 @sovmoneyfun）。ufOnlyFrom=50，mustOverlap=0（oryvnlaunch 在本分片，已由 UF 30m 覆盖，未另跑 MUST_WIN 24h），skippedNF=[]。UF1=0 帖，UF2=0 帖，UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_WIN3（R2187 新官号 try4pumpdotfun / gonkdotfun / x_MemeFactory_x）+ MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷 from:；本轮 mentions 含 MEN_STARX，正确）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_WIN3=23，MUST_OFF=4。must_win 含 TheJacket_NVDA、TriForgeAgent、sleighpad、ZEROFLASH_NFT、StrayKinNFT、try4pumpdotfun 等；本轮返回的 25+25 官帖中未见 @TheJacket_NVDA / @TriForgeAgent / @thecoffeeagents 新帖（可能无新帖或被触顶挤出，未另开探索性补读）。
- Mentions 24h 本轮：DogeEVM / BTC / Starknet / squeek / STARX（官号 from: 已读的已 drop）。
  - MEN_DOGE=4
  - MEN_BTC=25 触顶
  - MEN_STARK=0
  - MEN_SQUEEK=0
  - MEN_STARX=0
- mentionsNext：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- Silent：本轮 Starknet。search_users 仍不可用，回退 SILENT_STARK（24h，has:mentions has:links …），3 帖。看见 @JokerFaceCM / cartoon-money.com 自称 Launch Day Dec 3rd 3pm EST，号龄约 27 天、130 粉 / 384 帖，不是极早期，未送审。next silent：打新（2189 % 11 = 0）。
- 无额外探索性 X 读取。规划 25 次（24 main + SILENT_STARK）各跑一次，另加 3 次正当薄栏 24h，合计 28。

## 新收录

1. **Sov Money（@sovmoneyfun / https://sovmoney.fun/，打新，overall 68，live，focus=false）。** 官号建号 2026-11-15 12:49:50 CST，粉/推 4/4，xUserId 2121827779704729600。本轮 17:03:28 CST 官帖（https://x.com/sovmoneyfun/status/2125515703088562611）自称 1 SOV 是九只股票的固定篮子：$NVDA $AAPL $MSFT $GOOGL $AMZN $META $TSLA、SpaceX 与 Anthropic，上线时等权切分后数量不再改变，可随时赎回成分股代币。官网 HTTPS 200，标题 Sov Money - one token backed by nine stocks，文案与官帖一致，并回链 @sovmoneyfun，互证成立。官网站内说明可用九只成分股或 USDC 铸造、随时赎回，铸造一次性收费 0.10%，无持有费、无赎回费；程序只做 mint/redeem、不读价格、无管理员可改篮子或挪出 vault。#addresses 写明 Solana mainnet，并警告同名代币风险。本轮核到：Program `C7mgXqUFw7zuJsM8kZoJUaU4kxDFpXooxwtYJX9HtQLf`；SOV token (mint) `CwRV3zq42eMDtXiYWBK9Pp3m7xWjct73rUHAhq5iSbgn`；Program authority `74pNSsiYxZhS4zExXTQd27kCzAPEmk8DzRJBsxG7wuCY`；Fee account `ELHUL3KMEJxyuK66d51cJXysGULPEeBKTzMcHYBqU2aW`；Lookup table `DBfQKexdyeCii2FU4aeQn8H7fGNY5MeNhNaDNzWbcBy3`。成分股页内写 NVDAx 等为 xStocks、SPCX/ANT 为 Backpack。DexScreener 对本轮 SOV mint 查询 pairs=0，不编造价格或流动性。不是免费 mint / 免费登记。已挂 userFollowWatch。DeepSeek admit=true，early 95 / actionable 55 / novelty 82 / risk 80 / overall 68。

## 库内更新（不重推，除非已在告警中点名的实质变化）

- **4pump @try4pumpdotfun：** R2187 收录时官网写 $4PUMP 尚未上线、无 CA。本轮 16:36:24 CST 官帖（https://x.com/try4pumpdotfun/status/2125508893363331138）称 $4PUMP is live，并给出 CA `8ypx9tHqwLjJk51tqrm1iCrhTQ1PKshnw1FfpQjWpump`。DexScreener 核到 4pump/4PUMP，pumpfun 交易对创建于 2026-11-25 16:35:01 CST。16:46:51 CST 官帖称 Launching is now live on 4PUMP；16:50:47–17:01:05 CST 又说后端升级、wrapping up the final code / All operations will be live shortly。官网仍回链 @try4pumpdotfun；前端 JS 未内嵌该 CA，但已不再出现 R2187 的 not live yet / No coins launched yet。官号本轮 10 粉 / 8 帖。已更新卡片为 live 并写入 CA。不是免费 mint。已在本轮告警中点名，不另开第二次推送。
- **SleighPad @sleighpad：** R2186 收录时官网 $SLEIGH mint 未配置、无 CA。本轮 16:37:45 CST 官帖（https://x.com/sleighpad/status/2125509232522850708）称 $SLEIGH is live，并给出 CA `EF3MmGHFR5wG7LvW2bXAJjTuzhPabXzq9YRFeaLHpump`；16:39:48 CST 再发 The sleigh has left the North Pole。官网 `/build/app.js` 已写入该 mint（symbol SLEIGH, name SleighPad）。DexScreener 核到 sleighpad/SLEIGH，交易对创建于 2026-11-25 16:37:26 CST。官网 HTML last-modified 16:40:02 CST。页内 DEX Screener 按钮仍标 coming soon。资料栏现为 http://sleighpad.fun ，静态页仍未见回链官号。官号本轮仍 0 粉 / 5 帖。已更新卡片为 live 并写入 CA。不是免费 mint。已在本轮告警中点名。
- **Duet @DuetFun：** 官号 16:08:22 CST 再发 DUET is live on @pumpfun，16:08:34 CST 回复 @Pumpfun 给出 `HGSnJj9eemRD2ZnFSVXpapi4fvZ2qKrzy8r7abppump`。DexScreener 核到 Duet/DUET，交易对创建于 16:08:27 CST。官网 https://useduet.fun 文案仍写 CA Soon，并回链 @DuetFun；前端 JS 另有 `HCbkdsqo3jTYAkA7eqHfxLxkGZgYMV2epYWmiautpump`（亦名 Duet/DUET，交易对创建于 2026-11-23 13:34:14 CST）。两枚同名代币并存，本轮不把单一 CA 写入 contract，**不单独作为重推主因**，仅更新卡片风险说明。
- **The Jacket @TheJacket_NVDA：** 仍在 ≤2h 窗口，官方开窗仍为 2026-11-25 18:00 CST（10:00 UTC）。本轮 MUST 24h 返回中未见新官帖，未见改期或已开铸 LIVE。持有人免费 mint（RebelKin / Argonauts / Vaultlings / Quotrons404，只付 gas），OpenSea the-jacket-man，4444 份、上次已铸 0。首次 ≤2h 告警已在 R2186 发出，本轮 **不重推**。卡上 le2h=true 保留。
- **ORIPA @oripaxyz：** 新官帖 16:43:16 CST（https://x.com/oripaxyz/status/2125510621185839205）确认 Allowlist emails are out，Rips open tonight, 8 PM GMT+8（仍为 2026-11-25 20:00 CST，无改期）；未中签可从 11-26 铸造 Early Bird badge。官帖 Mint here 展开为 https://oripa.xyz/#early。dry-run 收尾 17:16:13 CST，尚未到 18:00 CST，未进入首次 ≤2h，**不提前告警**。卡上 le2h=false。若 parent 实际 apply 时已 ≥18:00 CST，apply_r2188.py 会按当时时钟把 le2h 置 true，那时才是首次 ≤2h，应当 notify 并点名。
- **TRIFORGE @TriForgeAgent：** 沿用 parent 已跑的公共 BSC RPC（2026-11-25 17:00:14 CST），Forge Keys 免费 mint 仍 LIVE，348/3333（R2187 为 345/3333），nftMintPaused=false。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=3（未变）；miningShares=6；tokenTradingEnabled=false。小幅进度，已更新卡片，**不重推**。本轮未再打 RPC。MUST 24h 返回中未见新官帖。
- **Ugly Puggies：** 公开开窗仍 2026-11-25 21:00 CST（13:00 UTC）。本轮仅见 11:06 CST 回复 “see you there”，不是改期或已开铸 LIVE。约 19:00 CST 才进入 2 小时窗口，不重推。
- **2hour.fun：** 仍可见 Reservations are OPEN 官帖，第一场窗口 Today at 21:00 UTC = 2026-11-26 05:00 CST。不要把 21:00 UTC 误读成今天 21:00 CST。尚未进入 2 小时窗口，不重推。
- **Plato/The Unseen：** schedule.publicEndsAt 2026-11-25 18:00 CST 是结束而非开窗，未当作新开窗或 LE2H-open。本轮未见新官帖。
- Coffee Agents：本轮 MUST 返回中未见新官帖，上次官方进度仍 188/1500，无实质变化。
- gonk.fun / MEME FACTORY：本轮可见官帖或既有 $SHREKMAS 宣称，未见足以改判的新 CA 或免费铸，不重推。
- Flame-BTC 付费公铸仍开；DAEMONS 仍 waitlist / 圣诞节前；ANKOU 日期仍 TBA。不重推已提醒过的付费 LIVE / 非免费项目。

## 看见但未收录

- @supersmoney：再次转述已在库的 @AscendLaunch 规划免费 mint（500、日期 TBA、文档称尚未 LIVE），不把评论号当官号收录。
- @jamedtzy / @Tezanaki22：宣传 GAMA / gama.win / launch.gamatiles.com（Sepolia testnet）。@GamaDotWin 约 65 日号；@GAMA_GIWA / @gamapadcom 已在库。不重收。
- @tailtradesxyz（https://tailtrades.xyz/）：R2183–R2187 已见未收；自称 Hyperliquid / Elysium AI 交易台，资料栏已有 CA，不是 mint/发射台。本轮无足以改判的新证据，不重收。
- @2hourfunEco：已在库 @2hourfun 的生态号，不另建卡。
- @JokerFaceCM / https://cartoon-money.com/：静号栏见到自称 Launch Day Dec 3rd 3pm EST（t.co 展开为官网）。号龄约 27 天、130 粉 / 384 帖，站点标题 Cartoon Money · Own the coin. Launch the market.，不是极早期，未送审。
- @DamonPooleHQ / onbold.com：跨境支付 Merchant of Record，不在本雷达打新主车道，不收。
- @Settxon：RT 第三方 @HoodHavocNFTS 的 GTD WL 抽奖；@HoodHavocNFTS 已在库，不把转发号当官号。
- @zerrrxyz 等为已在库 @RGBHorse 拉人，不另建卡。
- @Gwynne566：RT 无关 Flight X 发射，不收。

## Discord Peek

- parent 本轮已并行 computerUse 补 Peek，并留下 /tmp/r2188/discord_peek.json，dry-run apply 已合并（parent 仍可再覆盖）。
- attemptedAt=2026-11-25 17:02:30 CST。loginOk=false，loginWall=true，channelsPeeked=false。
- 打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone / Password / Log In / QR / passkey / Register）。未输入凭证，未点 Log In / Register，未扫码，未用 passkey。
- 四频道均未翻，lastSeen 保持约 2026-11-23 22:19–22:56 CST。discordPeekDeferred=true。nag=false，不单为登录墙再催。

## 失败 / 限制

- 无 X 工具拒绝，规划搜索均各执行 1 次；无同查询重试、无探索性补读。
- search_users 仍不可用，静号走 SILENT_STARK 关键词回退。
- MUST_WIN / MUST_WIN2 均 25 触顶；@TheJacket_NVDA、@TriForgeAgent、@thecoffeeagents 未出现在本轮返回的 25 条中。
- 部分 write_to_file 预览被截断，已从 Full text 路径还原写入 x_raw，未重查。
- 4pump 官网 JS 未内嵌官方公布的 $4PUMP CA，改以官帖原文 + DexScreener 互证；官帖后期又说后端升级，发射功能稳定性未实测。
- Duet 出现两枚同名 DUET CA（官号新帖 vs 官网 JS 旧 mint），未把单一 CA 写入 contract。
- 未改 /workspace/early-scout/data.json（sha256 仍为 40f1ad7cd6e7e01d6de3af407b69592200d2bd5e46a975aba529bcb405d094fe），无 git commit/push。

## notify

- notify=true
- reason：真新收录 Sov Money（@sovmoneyfun），须点名，不是免费 mint / 免费登记。另有库内实质变化：4pump $4PUMP、SleighPad $SLEIGH 均已公布 CA 并在 pump.fun 上线。The Jacket 已在 R2186 首次≤2h 告警，本轮未见改期或 LIVE，不重推。ORIPA 首包仍 20:00 CST，收尾时尚未到 18:00 CST，不提前告警。TRIFORGE 仅 345→348 小幅进度，不重推。
- alertMessage：【R2188】新收录 Sov Money（@sovmoneyfun，0.10% 铸造费，非免费 mint）；4pump 已公布 $4PUMP CA 并上线、SleighPad 已公布 $SLEIGH CA 并上线；面板：https://reboot7454.github.io/early-scout/
- namedFreeMintOrRegistration：无
- dsFallback=false

## 产出路径

- /tmp/r2188/RESULT_R2188.md
- /tmp/r2188/notify.json
- /tmp/r2188/new_cards.json
- /tmp/r2188/ds_payload.json、/tmp/r2188/ds_score.json、/tmp/r2188/ds_alert.json
- /tmp/r2188/apply_r2188.py（默认 dry-run：APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2188/data.json.src APPLY_DRY_OUT=/tmp/r2188/data.json）
- /tmp/r2188/data.json（dry-run 结果，lastScout=2026-11-25 17:16:13 CST）
- /tmp/r2188/x_usage.json、/tmp/r2188/x_all.json、/tmp/r2188/x_raw/
