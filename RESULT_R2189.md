# RESULT R2189

- 轮次：R2189（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 17:36–17:48 CST（Asia/Shanghai）。queries 窗口 start30=2026-11-25T09:06:01Z，start24=2026-11-24T09:36:01Z。apply lastScout=2026-11-25 17:51:27 CST（parent 复核后入库；dry-run 初稿 17:48:05 CST）。
- mode：x_budget.py 在第一笔 UF1 之后 remainingToday=476（即 remainingBefore=477）时建议 mode=pace、softCap=18、minSpend=18、silentCap=2；因 remaining≫200 且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185–R2188 同一 override；含 MUST_WIN3，因 R2188 新收 @sovmoneyfun，且仍保留未挤进 MUST_WIN/MUST_WIN2 的 R2187 官号）。silentCap=2（silent 不计 softCap）。
- xReads=26（main 25 + silent 1），未低于 minSpend
- remainingBefore=477 / 1000（第一笔 UF1 remainingToday=476，+1）；remainingAfter=451（末笔 KW_STARK_24 remainingToday=451；477−26=451，与 live 一致）
- Judgment / admit / score / alert：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score（送审 3 项：ZeroGate overall 55、OPCOM overall 60、TAIL overall 50，DS 均建议 admit=true）+ 1 次 alert 文案。parent 复核后只入库 ZeroGate 与 OPCOM；TAIL 维持 R2183-R2188 skip，不入库。dsFallback=false。告警正文采用带 @handle 的点名稿（DS 草稿省略了 handle，不满足点名要求）。
- 本号不自动 mint。notify=true（真新收录 ZeroGate / OPCOM，须点名，两项都不是免费 mint；TAIL 维持往轮 skip 不入库；The Jacket 已在 R2186 首次≤2h 告警，本轮不重推；ORIPA 收尾时 17:51 CST 尚未到 18:00 CST，不提前告警；TRIFORGE 仅小幅进度，不重推）。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=11，KW_TAPE=25，KW_GIWA=25，KW_DOGE=17，KW_BTC=1，KW_STARK=0
  - KW_MINT=25，KW_MINE=2，KW_PAD=24，KW_GO=24，KW_ELY=7，KW_GAPS=24
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_BTC_24=25、KW_STARK_24=25。
- 未跑：KW_LZ_24（30m=11）、KW_TAPE_24（30m=25）、KW_GIWA_24（30m=25）、KW_DOGE_24（30m=17）。MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=2 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2，cursor 1511 @Fearnxyz 起 50 号至 @playplotrise，next 1561 @ZodiacFortune_N，wrap=false，total 写盘后=2401（原 2399 + 本轮 2 个新收录；TAIL 未入库）。ufOnlyFrom=50，mustOverlap=0，skippedNF=[]。UF1=6 帖（均为 @hoodicorns 回复），UF2=0 帖。
- MUST_WIN 24h 三批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷 from:；本轮 mentions 不含 MEN_STARX，因 STARX mentions 已在 R2188 跑过，正确）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_WIN3=25 触顶，MUST_OFF=0。must_win 含 TheJacket_NVDA、TriForgeAgent、sleighpad、ZEROFLASH_NFT、StrayKinNFT、try4pumpdotfun、sovmoneyfun 等；本轮返回的官帖中未见 @TheJacket_NVDA / @TriForgeAgent / @thecoffeeagents 新帖（可能无新帖或被触顶挤出，未另开探索性补读）。
- Mentions 24h 本轮（R2188 留给本轮）：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest。pads 已 drop 本轮已 from: 读过的 flapdotsh / PulseLaunchpad；GIWA/Tape/LZ/ELY 仍保留官号在 mentions。
  - MEN_PADS=3
  - MEN_GIWA=25 触顶
  - MEN_TAPE=15
  - MEN_LZ=25 触顶
  - MEN_ELY=24
- mentionsNext：DogeEVM / BTC / Starknet / squeek / STARX
- Silent：本轮 打新（2189 % 11 = 0）。search_users 仍不可用，回退 SILENT_MINT（24h，has:mentions has:links …），25 帖触顶。看见第三方 giveaway 提到 @BotInTheHood（bio 自称 Robinhood 2000 份免费 mint、日期 TBA、无官网、本轮无该号自己的官帖），未送审未收录。其余多为已入库项目的白名单转发/抽奖，未另花静号额度。next silent：挖矿（2190 % 11 = 1）。
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_MINT）各跑一次，另加 2 次正当薄栏 24h，合计 26。

## 新收录

1. **ZeroGate（@ZeroGate0G / https://zerogate.fun/，台子/Meme，overall 55，announced，focus=false，lzVerified=false）。** 官号建号 2026-11-25 07:13:04 CST，粉/推 9/1，xUserId 2125366198963703808。本轮 17:30:05 CST 唯一官帖（https://x.com/ZeroGate0G/status/2125522402998136886）自称 ØG ZeroGate is launching soon，Launch time: 10:00 UTC（即 2026-11-25 18:00 CST），Launch on BNB. Go LayerZero Mainnet，fair launch + anti-sniper，PancakeSwap LP locked forever，Creators earn 50% of trading fees。官帖链接展开为 https://zerogate.fun 。官网 HTTPS 200，标题 ZeroGate | Launch on BNB. Go LayerZero.，twitter:site=@ZeroGate0G，window.__LZ.brand.x=https://x.com/ZeroGate0G，与资料栏互证成立。官网 brand.ca 为空；brand.zeroLaunch=2026-11-30（仅日期），与官帖今日 10:00 UTC 口径冲突，本轮未能核清是发射台开张、平台币开盘还是两套日程，**不按已确认 ≤2h / 已 LIVE 告警**。window.__LZ 写 chainId=56、eid=30102、creationFee=0.001 BNB、graduationFeeBps=300、virtualNative=6 BNB。本轮用公共 BSC RPC eth_getCode 核到均有字节码（均来自官网，不把它们写成 $0G 代币 CA）：launchpad `0xaf6b21ae0f52d1e7b32a116cf4f341e76dec0c42`；router `0x4449d35fdb3363ffa1af16be2812ee40deeb28a8`；hub `0x6db13A069e925daF540A634e2FEc52850E663BFc`；splitter `0xd9bbc425d948d442b20bebeb900fce70c94513c0`；locker `0x2ac413c6a82f67978e201586b37e0fd3cf09ca38`；staking `0xc744248163d72be744d03b351a568fab5c0c6699`；buyback `0x58460dea5d952194a8da87aec73a060b91f7f067`。DexScreener 搜 zerogate 与对该 launchpad 查 pairs 均为 0。搜 0G 会命中无关高市值同名代币，不得记到本项目。库内已有另一项目 zerogates-rh / @zerogates_rh（Robinhood），**不是同一项**。创建费 0.001 BNB，不是免费 mint / 免费登记。自称 LayerZero（官网 window.__LZ / eid=30102）但尚未独立核验，按硬规则 lzVerified=false 进台子/Meme，不进 LayerZero 栏。已挂 userFollowWatch + agentPadWatch。DeepSeek admit=true，early 96 / actionable 58 / novelty 66 / risk 78 / overall 55。

2. **OPCOM（@tryopencom / https://tryopen.computer/，打新，overall 60，live，focus=false）。** 官号建号 2026-11-25 00:32:33 CST（显示名 Try Open Computer），粉/推 5/25，xUserId 2125266078783696896。本轮 KW_PAD 见到多条官帖，最近 17:37:51 CST（https://x.com/tryopencom/status/2125524355505668387）自称 New on Pons: OPCOM，an AI agent with its own computer on Robinhood Chain，每笔 stock-token 交易都是 pull request，需用户 merge；另条官帖称 We launched OPCOM on Pons、Live now，permit ETH 进入回购销毁 OPCOM 的轮盘。多条官帖与官网重复给出同一 CA `0x7B4377084284f5A1Cd5C3515fCda0Da296a3c7dd`。官网 HTTPS 200，标题 OPCOM | An agent with its own computer，页内回链 https://x.com/tryopencom，互证成立。本轮 DexScreener 对该 CA 查询 pairs=0（可能因 Robinhood Chain 未被索引，不写成已确认无流动性）。访问 robin.etherscan.io 代币页遇 Cloudflare 挑战，未能核到链上名称/供应/持有人，不编造。不是免费 mint / 免费登记。已挂 userFollowWatch。DeepSeek admit=true，early 92 / actionable 64 / novelty 78 / risk 72 / overall 60。

## 库内更新（不重推，除非已在告警中点名的实质变化）

- **The Jacket @TheJacket_NVDA：** 仍在 ≤2h 窗口，官方开窗仍为 2026-11-25 18:00 CST（10:00 UTC）。本轮 MUST 24h 返回中未见新官帖，未见改期或已开铸 LIVE。持有人免费 mint（RebelKin / Argonauts / Vaultlings / Quotrons404，只付 gas），OpenSea the-jacket-man，4444 份、上次已铸 0。首次 ≤2h 告警已在 R2186 发出，本轮 **不重推**。卡上 le2h=true 保留。
- **ORIPA @oripaxyz：** 本轮 MUST 再见同一则 16:43:16 CST Allowlist emails 官帖（https://x.com/oripaxyz/status/2125510621185839205），Rips open tonight, 8 PM GMT+8（仍为 2026-11-25 20:00 CST，无改期）；未中签可从 11-26 铸造 Early Bird badge。Mint here 展开为 https://oripa.xyz/#early。dry-run 收尾 17:48:05 CST，尚未到 18:00 CST，未进入首次 ≤2h，**不提前告警**。卡上 le2h=false。若 parent 实际 apply 时已 ≥18:00 CST，apply_r2189.py 会按当时时钟把 le2h 置 true，那时才是首次 ≤2h，应当 notify 并点名。
- **TRIFORGE @TriForgeAgent：** 本路公共 BSC RPC 只读（约 2026-11-25 17:42:12 CST，https://bsc-dataseed.binance.org/），Forge Keys 免费 mint 仍 LIVE，354/3333（R2188 为 348/3333），nftMintPaused=false。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=3；miningShares=6；tokenTradingEnabled=false。小幅进度，已更新卡片，**不重推**。MUST 24h 返回中未见新官帖。
- **4pump @try4pumpdotfun：** 17:16 CST 之后官帖继续更新：17:31 CST 称 all errors and backend are fixed, publishing the site now（https://x.com/try4pumpdotfun/status/2125522645202723106）；17:33 CST 称 4.6% now locked。CA 仍为 `8ypx9tHqwLjJk51tqrm1iCrhTQ1PKshnw1FfpQjWpump`，未见改约或新的免费 mint。R2188 已提醒 $4PUMP CA 上线，本轮 **不重推**。
- **Sov Money @sovmoneyfun：** 17:15 CST 官帖称 Supply is locked（Streamflow 链接）；17:21 CST 再发 How to use Sov Money。SOV mint 仍为 `CwRV3zq42eMDtXiYWBK9Pp3m7xWjct73rUHAhq5iSbgn`。R2188 已收录并提醒，本轮无新的免费 mint / 新 CA，**不重推**。
- **SleighPad @sleighpad：** 本轮可见 $SLEIGH is live 及同一 CA `EF3MmGHFR5wG7LvW2bXAJjTuzhPabXzq9YRFeaLHpump`，均已在 R2188 提醒，无新实质变化，不重推。
- **Ugly Puggies：** 公开开窗仍 2026-11-25 21:00 CST（13:00 UTC）。本轮仅见 11:06 CST 回复 “see you there”，不是改期或已开铸 LIVE。约 19:00 CST 才进入 2 小时窗口，不重推。
- **2hour.fun：** 仍可见 Reservations are OPEN 官帖，第一场窗口 Today at 21:00 UTC = 2026-11-26 05:00 CST。不要把 21:00 UTC 误读成今天 21:00 CST。尚未进入 2 小时窗口，不重推。
- **Plato/The Unseen：** schedule.publicEndsAt 2026-11-25 18:00 CST 是结束而非开窗，未当作新开窗或 LE2H-open。本轮未见新官帖。
- Coffee Agents：本轮 MUST 返回中未见新官帖，上次官方进度仍 188/1500，无实质变化。
- gonk.fun / MEME FACTORY：本轮可见官帖或既有 $SHREKMAS 宣称（16:25 CST 官帖已落在 R2188 窗口内），未见足以改判的新 CA 或免费铸，不重推。
- Duet：未见需要把单一 CA 写入或作为重推理由的新变化。
- Flame-BTC 付费公铸仍开；DAEMONS 仍 waitlist / 圣诞节前；ANKOU 日期仍 TBA。不重推已提醒过的付费 LIVE / 非免费项目。
- ZEROFLASH / StrayKin / SYMPHONY Prelude：本轮未见改期或免费 mint LIVE，不重推。

## 看见但未收录

- @tailtradesxyz（https://tailtrades.xyz/）：R2183-R2188 已见未收，理由是「自称 Hyperliquid / Elysium AI 交易台，不是 mint/发射台，官网与官推互证不全」。本轮 MEN_ELY 再见 13:07:33 CST 官帖，DexScreener 核到 bio CA 0xC6333959D096f151dee397AC56c9259a1127B870 与 Elysium Uniswap TAIL/HYPE 池一致（池约 2026-11-24 08:56:24 CST 创建，本轮流动性约 $17.5k、市值约 $40.5k）。官网仍未回链 X、也未内嵌该 CA。这反而说明已是在交易的交易台代币，不是新开铸造窗；parent 维持往轮 skip，不入库、不告警。DeepSeek 本轮曾给出 admit=true / overall 50，未采纳。
- @BotInTheHood：静号栏第三方 giveaway 提到该号。bio 自称 Robinhood 免费 mint、2000 份、Community is the utility；giveaway 文案写 Mint date: TBA。号龄约 8.3 天、247 粉 / 51 帖，无官网，本轮无该号自己的官帖，未送审未收录。
- @SadBatteryoffic / sadbattery.grok.me：自称 Solana meme，6 days to launch，官方 CA 只在 Telegram，未送审。
- @Arakuni_：号龄约 5.7 天，bio 写 Anime raccoons heading to RobinhoodApp，仅 1 帖、无官网，信息不足，未收。
- @Wildlifeuni_55 / Tiger Universe：第三方称明日 Robinhood 免费 mint（5,555，1:30 PM UTC）。@Wildlifeuni_55 已在库，不重收，也未把转发号当官号。
- @Vicehood_RH / @SmileQuokkaNFT / @MMIX_io / @GAMA_GIWA / @gamapadcom / @AmmoraHQ：已在库项目的白名单/任务转发，不重收。
- 不要把 ZeroGate（@ZeroGate0G / zerogate.fun）与库内 zerogates-rh / @zerogates_rh 当成同一项。

## Discord Peek

- parent 本轮已并行 computerUse 补 Peek，并留下 /tmp/r2189/discord_peek.json，dry-run apply 已合并（parent 仍可再覆盖）。
- attemptedAt=2026-11-25 17:37:19 CST。loginOk=false，loginWall=true，channelsPeeked=false。
- 打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone / Password / Log In / QR / passkey / Register）。本路未操作登录。
- 四频道均未翻，lastSeen 保持约 2026-11-23 22:19–22:56 CST。discordPeekDeferred=true。nag=false，不单为登录墙再催。

## 失败 / 限制

- 无 X 工具拒绝，规划搜索均各执行 1 次；无同查询重试、无探索性补读。部分 write_to_file 预览被截断，已从 Full text 路径还原写入 x_raw，未重查。
- search_users 仍不可用，静号走 SILENT_MINT 关键词回退。
- MUST_WIN / MUST_WIN2 / MUST_WIN3 均 25 触顶；@TheJacket_NVDA、@TriForgeAgent、@thecoffeeagents 未出现在本轮返回的 25 条中。
- OPCOM 的 robin.etherscan.io 代币页遇 Cloudflare 挑战，链上名称/供应未核到。
- ingest_direct.py 原 ORDER 漏了 SILENT_MINT，已在 /tmp/r2189/ingest_direct.py 补进后重跑；x_usage.round 已改为 2189，mode=pace-override-full。
- parent 复核后已 apply：去掉 TAIL、ZeroGate 改归台子/Meme 并挂 agentPadWatch，写入仓库 data.json + docs/data.json 并推送。

## notify

- notify=true
- reason：真新收录 ZeroGate（@ZeroGate0G）、OPCOM（@tryopencom），须点名，两项都不是免费 mint / 免费登记。TAIL @tailtradesxyz 维持往轮 skip，不入库。The Jacket 已在 R2186 首次≤2h 告警，本轮未见改期或 LIVE，不重推。ORIPA 首包仍 20:00 CST，收尾时 17:51 CST 尚未到 18:00 CST，不提前告警。TRIFORGE 仅 348→354 小幅进度，不重推。4pump / SleighPad / Sov Money 无新的需重推实质变化。
- alertMessage：【R2189】新收录 ZeroGate（@ZeroGate0G，BNB 发射台，自称 LayerZero，官帖称今日 18:00 CST 开、官网写 11-30，日程未核清，非免费 mint）、OPCOM（@tryopencom，Robinhood Chain，非免费 mint）；面板：https://reboot7454.github.io/early-scout/
- namedFreeMintOrRegistration：无
- dsFallback=false

## 产出路径

- /tmp/r2189/RESULT_R2189.md
- /tmp/r2189/notify.json
- /tmp/r2189/new_cards.json
- /tmp/r2189/ds_payload.json、/tmp/r2189/ds_score.json、/tmp/r2189/ds_alert.json、/tmp/r2189/ds_alert_payload.json
- /tmp/r2189/apply_r2189.py（默认 dry-run：APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2189/data.json.src APPLY_DRY_OUT=/tmp/r2189/data.json）
- /tmp/r2189/data.json（dry-run 结果，lastScout=2026-11-25 17:48:05 CST）
- /tmp/r2189/x_usage.json、/tmp/r2189/x_all.json、/tmp/r2189/x_raw/
- /tmp/r2189/triforge_rpc.json
