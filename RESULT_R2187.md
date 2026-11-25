# RESULT R2187

- 轮次：R2187（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 16:33–16:45 CST（Asia/Shanghai）。queries 窗口 start30=2026-11-25T08:01:33Z，start24=2026-11-24T08:31:33Z。dry-run lastScout=2026-11-25 16:45:34 CST。
- mode：x_budget.py 在 live remaining=532 时建议 mode=pace、softCap=18、minSpend=18、silentCap=2；因 remaining≫200 且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185/R2186 同一 override）。silentCap=2（silent 不计 softCap）。
- xReads=27（main 26 + silent 1），未低于 minSpend
- remainingBefore=532 / 1000（第一笔 UF1 remainingToday=531，+1）；remainingAfter=505（末笔 KW_STARK_24 remainingToday=505；532−27=505，与 live 一致）
- Judgment / admit / score / alert：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score（送审 3 项，均 admit）+ 1 次 alert 文案。dsFallback=false
- 本号不自动 mint。notify=true（真新收录 3 项，均须点名；三者皆非免费 mint / 免费登记 / 已确认免费 LIVE。The Jacket 已在 R2186 首次≤2h 告警，本轮不重推；TRIFORGE 仅小幅进度，不重推）。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=2，KW_TAPE=25，KW_GIWA=14，KW_DOGE=20，KW_BTC=1，KW_STARK=2
  - KW_MINT=25，KW_MINE=7，KW_PAD=25，KW_GO=25，KW_ELY=10，KW_GAPS=19
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=20、KW_BTC_24=25、KW_STARK_24=25。
- 未跑：KW_TAPE_24（30m=25）、KW_GIWA_24（30m=14）、KW_DOGE_24（30m=20）。MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=7 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1411 @NiuBiAgent 起 50 号至 @falqoxyz，next 1461 @baggieshood，wrap=false，total 写盘后=2398（原 2395 + 本轮 3 个新收录 @try4pumpdotfun、@gonkdotfun、@x_MemeFactory_x）。ufOnlyFrom=50，mustOverlap=0（bons_world 在本分片，已由 UF 30m 覆盖，未另跑 MUST_WIN 24h），skippedNF=[]。UF1=0 帖，UF2=1 帖（@ciphersaints 确认延期），UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷 from:；本轮 mentions 不含 MEN_STARX，正确）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=16。must_win 含 TheJacket_NVDA、TriForgeAgent、sleighpad、ZEROFLASH_NFT、StrayKinNFT；本轮返回的 25+25 官帖中未见 @TheJacket_NVDA / @TriForgeAgent 新帖（可能无新帖或被触顶挤出，未另开探索性补读）。
- Mentions 24h 本轮：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest。
  - MEN_PADS=3
  - MEN_GIWA=25 触顶
  - MEN_TAPE=15
  - MEN_LZ=25 触顶
  - MEN_ELY=24
- mentionsNext：DogeEVM / BTC / Starknet / squeek / STARX
- Silent：本轮 BTC。search_users 仍不可用，回退 SILENT_BTC（24h，has:mentions has:links …），3 帖，未见需新收的静号官号。next silent：Starknet（2188 % 11 = 10）。
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_BTC）各跑一次，另加 3 次正当薄栏 24h，合计 27。

## 新收录

1. **4pump（@try4pumpdotfun / https://try4pump.fun/，台子/Meme，overall 58，watching，focus=false）。** 官号建号 2026-11-25 13:49:26 CST，0 粉 / 1 帖，xUserId 2125466462953582592。本轮 16:34:20 CST 官帖（https://x.com/try4pumpdotfun/status/2125508371101122681）自称 4pump，the launchpad built on 4chan：把 4chan 新帖拉进 live feed，一键发成 pump.fun 币，默认与 $4PUMP 配对；creator fees 50% 给 holder 或 launcher、50% 给原帖匿名者（可用 tripcode 领取）。官网 HTTPS 200，标题 4pump，文案与官帖一致，并回链 @try4pumpdotfun，互证成立。前端 LaunchDialog 明示 `$4PUMP is not live yet. Launching opens when its contract address is available.` 以及 `The $4PUMP pair is not available on pump.fun yet.`；硬币列表为 `No coins launched yet`。本轮不编造 $4PUMP 或已发射币 CA。不是免费 mint / 免费登记。已挂 userFollowWatch + agentPadWatch。

2. **gonk.fun（@gonkdotfun / https://gonk.fun/，台子/Meme，overall 64，live，focus=false）。** 官号建号 2026-11-11 04:58:30 CST，90 粉 / 74 帖，xUserId 2120259642953695232。官网 https://gonk.fun/ 与 https://gonk.fun/launch 均 HTTPS 200，标题 Gonk.fun Solana memecoin launchpad，自称可用钱包或 AI 助手经 Raydium LaunchLab 发币，默认报价 SOL，并有 remix / burn flywheel。页内回链 @gonkdotfun，互证成立。本轮 16:22:09 CST 官帖展开为 X Article（id 2125501408271351808），遇登录墙，未读取正文，未另开 X 读、不编造文章内容或 CA。静态页未见平台币或已发射币合约。属已上线发射台，不是免费 mint / 免费登记。已挂 userFollowWatch + agentPadWatch。

3. **MEME FACTORY（@x_MemeFactory_x / https://meme-factory.site/，台子/Meme，overall 45，watching，focus=false）。** 官号建号 2026-11-11 20:24:58 CST，199 粉 / 81 帖，xUserId 2120492674222350336。本轮 16:25:44 CST 官帖（https://x.com/x_MemeFactory_x/status/2125506206257025063）自称 THE FIRST LAUNCH IS LIVE，$SHREKMAS 为该台第一枚已发射币，bonding curve is filling up。Charts 短链展开仅为官网首页；TG 为 https://t.me/Shrekmas。官网 HTTPS 200 并回链 @x_MemeFactory_x，但明确写 Launchpad Beta、`Preview build · all figures are sample data until the live backend connects.` 资料栏 HTTP `www.Meme-Factory.site` 本轮 500。本轮未核到 $SHREKMAS 或平台币 CA，不编造。不是免费 mint / 免费登记。已挂 userFollowWatch + agentPadWatch。

## 库内更新（不重推）

- **The Jacket @TheJacket_NVDA：** 仍在 ≤2h 窗口，官方开窗仍为 2026-11-25 18:00 CST（10:00 UTC）。本轮 MUST 24h 未见新官帖，未见改期或已开铸 LIVE。持有人免费 mint（RebelKin / Argonauts / Vaultlings / Quotrons404，只付 gas），OpenSea the-jacket-man，4444 份、上次已铸 0。首次 ≤2h 告警已在 R2186 发出，本轮 **不重推**。卡上 le2h=true 保留。
- **TRIFORGE @TriForgeAgent：** 沿用 parent 已跑的公共 BSC RPC（2026-11-25 16:30:37 CST），Forge Keys 免费 mint 仍 LIVE，345/3333（R2186 为 342/3333），nftMintPaused=false。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=3；miningShares=6；tokenTradingEnabled=false。小幅进度，已更新卡片，**不重推**。本轮未再打 RPC。
- **Cipher Saints @ciphersaints：** UF2 官号 16:10:47 CST 回复确认 delay the mint（The Swop 在做基础设施更新并准备 marketplace；https://x.com/ciphersaints/status/2125502446856270194）。原公告 11-19 免费铸 10,000 份（ICP），本轮未公布新日期，不是已开铸 LIVE，已更新卡片，**不重推**。
- **ORIPA @oripaxyz：** 仍可见 10:00 CST 官帖「10 hours left before minting $ORIPA」，与既定首包 2026-11-25 20:00 CST 一致。约 18:00 CST 才进入 2 小时窗口，本轮未进入，无改期，不提前告警。
- **Ugly Puggies：** 公开开窗仍 2026-11-25 21:00 CST（13:00 UTC）。本轮仍可见 09:35 CST first wl batch 已添加官帖，不是改期或已开铸 LIVE。约 19:00 CST 才进入 2 小时窗口，不重推。
- **2hour.fun：** 仍可见同一则 10:02 CST 官帖 Reservations are OPEN，第一场窗口 Today at 21:00 UTC = 2026-11-26 05:00 CST。不要把 21:00 UTC 误读成今天 21:00 CST。尚未进入 2 小时窗口，不重推。
- **Plato/The Unseen：** schedule.publicEndsAt 2026-11-25 18:00 CST 是结束而非开窗，未当作新开窗或 LE2H-open。本轮未见新官帖。
- Coffee Agents：本轮 MUST 未见新官帖，上次官方进度仍 188/1500，无实质变化。
- DAEMONS 仍 waitlist / 圣诞节前、成员免费 mint，无新日期；ANKOU 日期仍 TBA。Flame-BTC 付费公铸仍开。不重推已提醒过的付费 LIVE / 非免费项目。

## 看见但未收录

- @tailtradesxyz（https://tailtrades.xyz/）：R2183–R2185 已见未收；自称 Hyperliquid / Elysium AI 交易台，资料栏已有 CA，不是 mint/发射台。本轮无足以改判的新证据，不重收。
- @FINGERSAREHAPPY / https://happycanton.xyz/：Canton 上已在交易的 $HAPPY 社区币（站点展示价格与持有人），不是早期 mint/发射台，不收。
- @ODYbtc：资料栏已有 pump.fun CA，属已发射代币，不是极早期发射台，不收。
- @Chainbitz / https://www.chainbitz.xyz/：约 58 日号、689 粉。本轮仅 RT 第三方 @Zara_Quinnx 的 20GTD FREE mint 抽奖；官网是 Robinhood Chain 10,000 像素收藏 + 游戏解锁 GTD 白名单申请，OpenSea 集合存在。本轮无官宣开铸日期，不够极早期，不收。
- @2hourfunEco：已在库 @2hourfun 的生态号，不另建卡。
- @ValbloxGG：自称即将上线的 Roblox 赌场，不在本雷达打新/发射台主车道，不收。
- @supersmoney 转述 @AscendLaunch 规划免费 mint（500、日期 TBA、文档称尚未 LIVE）——AscendLaunch 已在库，不把评论号当官号收录。
- GIWA/Ammora 测试网个人作品（@aripintujg、@abdo_mahmoud_7、@szymansk68 等）及纯回复/空号，不收。
- @GamaDotWin（gama.win，约 65 日）：本轮无可用官帖/铸造窗，不收。@GAMA_GIWA / @gamapadcom 已在库。

## Discord Peek

- parent 本轮已并行 computerUse 补 Peek，并合并 /tmp/r2187/discord_peek.json。
- attemptedAt=2026-11-25 16:33:20 CST。loginOk=false，loginWall=true，channelsPeeked=false，items=[]。
- 打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone / Password / Log In / QR / passkey / Register）。未输入凭证，未点 Log In / Register，未扫码，未用 passkey。
- 四频道均未翻，lastSeen 保持约 2026-11-23 22:19–22:56 CST。discordPeekDeferred=true。nag=false，不单为登录墙再催。

## 失败 / 限制

- 无 X 工具拒绝，规划搜索均各执行 1 次；无同查询重试、无探索性补读。
- search_users 仍不可用，静号走 SILENT_BTC 关键词回退。
- MUST_WIN / MUST_WIN2 均 25 触顶；@TheJacket_NVDA、@TriForgeAgent 未出现在本轮返回的 25 条中。
- @gonkdotfun 本轮官帖为 X Article，遇登录墙，未读正文，未重查。
- 部分 write_to_file 预览被截断，已从 Full text 路径还原写入 x_raw，未重查。
- 未改 /workspace/early-scout/data.json（sha256 仍为 83886ba0e622516f72c1ee8402ed1b74461369572e0fe3487a3dcf042fc4fc85），无 git commit/push。

## notify

- notify=true
- 理由：真新收录 4pump、gonk.fun、MEME FACTORY，须逐个点名。三者皆非免费 mint / 免费登记 / 已确认免费 LIVE。The Jacket 非本轮首次≤2h；TRIFORGE 非实质进度。
- 草稿 alertMessage：
  【R2187】新收录：4pump（@try4pumpdotfun，https://try4pump.fun/）非免费 mint 且暂无已发射币/CA；gonk.fun（@gonkdotfun，https://gonk.fun/）非免费 mint 且未见平台币 CA；MEME FACTORY（@x_MemeFactory_x，https://meme-factory.site/）官网仍 preview/sample、未核到 CA，非免费 mint，三者均非已确认免费 LIVE。面板：https://reboot7454.github.io/early-scout/

## 关键产物路径

- /tmp/r2187/x_usage.json
- /tmp/r2187/x_raw/（27 个搜索）
- /tmp/r2187/new_cards.json
- /tmp/r2187/notify.json
- /tmp/r2187/ds_payload.json、/tmp/r2187/ds_score.json、/tmp/r2187/ds_alert.json
- /tmp/r2187/apply_r2187.py（dry-run）
- /tmp/r2187/data.json（dry-run 写盘；源为 /tmp/r2187/data.json.src）
- /tmp/r2187/RESULT_R2187.md
- /tmp/r2187/triforge_rpc.json（parent 预跑，本轮未重打）
- /tmp/r2187/discord_peek.json（若存在，交 parent 合并）
