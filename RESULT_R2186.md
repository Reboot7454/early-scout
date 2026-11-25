# RESULT R2186

- 轮次：R2186（常规增量，非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- 时间：约 2026-11-25 16:03–16:14 CST（Asia/Shanghai）。queries 窗口 start30=2026-11-25T07:31:19Z，start24=2026-11-24T08:01:19Z。dry-run lastScout=2026-11-25 16:14:45 CST。
- mode：x_budget.py 在 live remaining=559 时建议 mode=pace、softCap=18、minSpend=18、silentCap=2；因 remaining≫200 且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185 同一 override）。silentCap=2（silent 不计 softCap）。
- xReads=27（main 26 + silent 1），未低于 minSpend
- remainingBefore=559 / 1000（第一笔 UF1 remainingToday=558，+1）；remainingAfter=532（末笔 KW_BTC_24 remainingToday=532；559−27=532，与 live 一致）
- Judgment / admit / score / alert：DeepSeek（deepseek-flash，thinking on）本轮 1 次 batch score（送审 3 项，均 admit）+ 1 次 alert 文案。dsFallback=false
- 本号不自动 mint。notify=true（The Jacket 首次进入 ≤2h 窗口；真新收录 3 项，其中 ZEROFLASH 自称即将免费 mint、StrayKin 官网白名单申请已开，均须点名）。

## 搜索是否跑全

- 10 栏独立 30m KW + KW_GAPS：全部各 1 次。
  - KW_LZ=1，KW_TAPE=25，KW_GIWA=15，KW_DOGE=4，KW_BTC=1，KW_STARK=5
  - KW_MINT=25，KW_MINE=3，KW_PAD=25，KW_GO=25，KW_ELY=14，KW_GAPS=12
- 薄栏 24h 回填（同一组词，仅 30m 独立 KW <5 时 +1）：跑了 KW_LZ_24=20、KW_DOGE_24=25、KW_BTC_24=25。
- 未跑：KW_TAPE_24（30m=25）、KW_GIWA_24（30m=15）、KW_STARK_24（30m=5，不是 <5）。MINT/PAD/GO 已高命中或为厚栏，不转 24h。MINE=3 但是核心栏，未加 24h。
- UF 软刷 30m：UF1/UF2/UF3，cursor 1361 @HypeWaveDeFi 起 50 号至 @blown_xyz，next 1411 @NiuBiAgent，wrap=false，total 写盘后=2395（原 2392 + 本轮 3 个新收录 @sleighpad、@ZEROFLASH_NFT、@StrayKinNFT）。ufOnlyFrom=50，mustOverlap=0，skippedNF=[]。UF1=0 帖，UF2=0 帖，UF3=0 帖。
- MUST_WIN 24h 两批 + MUST_OFF 30m（跳过已知 NF @starx_xlayer，未连刷 from:；本轮 mentions 含 MEN_STARX，正确）。MUST_WIN=25 触顶，MUST_WIN2=25 触顶，MUST_OFF=21。must_win 含 TheJacket_NVDA、symphonyopus、AzukePad、femeoraApp、dogstarterhq、gAntsbsc、MergedSite、Fulcrumius、useClassified。
- Mentions 24h 本轮：DogeEVM / BTC / Starknet / squeek / STARX。
  - MEN_DOGE=4
  - MEN_BTC=25 触顶
  - MEN_STARK=0
  - MEN_SQUEEK=0
  - MEN_STARX=0
- mentionsNext：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- 无额外探索性 X 读取。规划 24 次（23 main + SILENT_DOGE）各跑一次，另加 3 次正当薄栏 24h，无同查询重试。errors=[]。

## 静号

- silentAccounts.ran=true；lane=DogeEVM；next=BTC（2187 % 11 = 9）
- search_users 不可用；fallback 一次 SILENT_DOGE（24h，has:mentions has:links (DogeEVM OR DogeOS) (mint OR launch OR launchpad)，不占 softCap）
- hits=1；seen=1；sentToReview=[]；admitted=[]；skipped=[]（@fizalasdair 讨论串提及 DogeOS testnet / 多个已有或无关号，未见需新收的静号官号）

## 新收录

3 项，已同时挂 Watch（focus=false）。DeepSeek 三项均 admit=true。

1. **SleighPad** @sleighpad / https://sleighpad.fun/  
   - 建号 2026-11-12 18:22:14 CST，本轮 0 粉 / 3 帖（xUserId 2120823690879455232）。资料栏无官网。本轮 KW_GO 见到两条官帖：16:02:42 CST https://x.com/sleighpad/status/2125500411671130544 与 16:02:52 CST https://x.com/sleighpad/status/2125500451424550968。自称 Christmas launchpad on Solana：每枚币与 $SLEIGH 配对，100% creator fees 经 donate.gg 捐给儿童慈善并链上出示收据，费用不经过团队钱包，发射走 pump.fun。  
   - 官帖 t.co 展开为 https://sleighpad.fun/、https://pump.fun/、https://www.donate.gg/。官网 HTTPS 200，标题与文案和官帖一致。前端 JS 里 SLEIGH quote mint 变量为空字符串，并有 “SLEIGH quote mint is not configured. There is no fallback quote.”；Pump.fun / DEX Screener 按钮在 CA 激活前为 coming soon。本轮**不编造** $SLEIGH 或已发射币合约。静态官网未见回链 @sleighpad，site-X 互证不完整。  
   - **不是免费 mint / 免费登记。** DeepSeek overall=58，admit=true。已挂 userFollowWatch + agentPadWatch。本号不自动 mint。

2. **ZEROFLASH** @ZEROFLASH_NFT  
   - 建号 2026-11-24 00:54:19 CST，本轮 119 粉 / 6 帖（xUserId 2124908923882725376）。资料栏无官网。简介写 5,555 PFPs on Zero · Free Mint。本轮未直接搜到 from: 原帖，KW_MINT 见到转帖 https://x.com/AustineChu26295/status/2125500653074313285 引用官帖 2026-11-25 11:42:24 CST（https://x.com/ZEROFLASH_NFT/status/2125434904330822077 ）：Free Mint is coming. 5,555 PFPs on Zero. First 111 wallets get in first. 该官帖只带配图、无外链。  
   - 本轮探测 zeroflash.xyz 为停车页（Parking/1.0，HTTP 445/405、空包），其它候选域名未存活，官网未能指认。“on Zero” 是否指 Z3RO Terminal **本轮无法核实**，不当成已证实。未见链、合约或日期。  
   - **自称即将免费 mint，不是已开铸 LIVE。** DeepSeek overall=42，admit=true。已挂 userFollowWatch + freeMintWatch。本号不自动 mint。

3. **StrayKin** @StrayKinNFT / https://straykin.xyz/  
   - 建号 2026-10-23 07:18:02 CST，本轮 341 粉 / 3 帖（xUserId 2113407703267553280）。资料栏官网 https://straykin.xyz/ 。本轮未见官号原帖；KW_MINT 仅见第三方转发，**以官网为准**。官网 HTTPS 200，twitter:site=@StrayKinNFT 且脚本回链 https://x.com/StrayKinNFT，site-X 互证成立。官网写 3,269 Total individuals、团队 100、Available to mint 3,169，标注 Team / GTD / FCFS，Minting on OpenSea；日期和价格将在 @StrayKinNFT 官宣（源码仍留 TBA 注释）。官网 shop 有 Whitelist application 入口，并写申请不保证名额。本轮未见官方公布的 OpenSea 收藏 slug 或合约。  
   - **官网白名单申请已开，不是已开铸免费 mint LIVE。** DeepSeek overall=60，admit=true。已挂 userFollowWatch + freeMintWatch。本号不自动 mint。

## 库内动态

- **The Jacket @TheJacket_NVDA 首次进入 ≤2h 窗口（本轮 notify=true 事件）。** 官方开窗仍 2026-11-25 18:00 CST（10:00 UTC）。MUST 24h 未见其新官帖。持有人免费 mint（RebelKin / Argonauts / Vaultlings / Quotrons404，只付 gas），OpenSea the-jacket-man，4444 份、上次已铸 0，Robinhood Chain，开火时尚未 LIVE。卡片已写 le2h=true / within2hAtScout=true。R2177 是未进窗口时的新收录提醒，本轮是首次 ≤2h 告警，不跳过。
- ORIPA @oripaxyz：仍可见同一则「10 hours left before minting $ORIPA」官帖（2026-11-25 10:00 CST，https://x.com/oripaxyz/status/2125409137127297404 ），倒计时与首包 2026-11-25 20:00 CST 一致，约 18:00 CST 才进 2h，本轮未进入，无改期，不重推。不要把 UTC 钟面误读成 12:00 CST。
- Ugly Puggies：公开仍 2026-11-25 21:00 CST（13:00 UTC），约 19:00 CST 才进 2h。本轮仍可见 first WL batch / “see you there”，不是改期或已开铸，不重推。
- 2hour.fun：MUST 官帖 2026-11-25 10:02 CST（https://x.com/2hourfun/status/2125409666502930693 ）再次确认 Today at 21:00 UTC, the very first window opens = 2026-11-26 05:00 CST。不要把 21:00 UTC 误读成今天 21:00 CST。本轮未进 2h，不重推。
- Plato/The Unseen：publicEndsAt 2026-11-25 18:00 CST 是结束不是开窗，不当新开铸或 LE2H-open。
- Agent Cards 仍 2026-11-25 23:00 CST，约 21:00 CST 才进 2h，本轮不提前告警。Shielded Wizards 2026-11-26 05:10 CST；Lamoryant 2026-11-26 19:00 CST；QQAI 2026-11-26 18:00 CST。
- TRIFORGE @TriForgeAgent / https://triforge.fun：Forge Keys 免费铸仍 LIVE。沿用 parent 公共 BSC RPC 快照（https://bsc-dataseed.binance.org/，约 2026-11-25 16:01:19 CST）：342/3333（R2185 为 340/3333），nftMintPaused=false。本轮 MUST 未见新的 TriForge 官帖。付费预售仍开，lpMintOpen=true，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST。claimsOpen=true，totalClaimed=3（与 R2185 相同）；miningShares=6；tokenTradingEnabled=false。小幅进度已更新卡片，不重推。本号不自动 mint。官网 HTML 可能仍显示未水合的 “Contracts are not deployed yet”，以 RPC 为准。
- Coffee Agents：MUST 24h 未见新官帖，上次官方进度仍 188/1500，不重推。
- Fulcrumius / Classified：R2185 已收录已通知，非免费 mint，本轮无实质变化，不重收、不重推。
- gAnts / Merged：R2184 已通知。Merged 本轮 MUST 继续有治理/透明度帖（16:02 CST 等），不是新的免费 mint，不重收、不重推。
- Femeora、SYMPHONY、Azuke Pad、AtlasPad、Basket、Dogstarter：无改期或新的免费铸，不重推。AtlasPad 本轮有 $ZRO 分红/毕业进度条等产品帖，Basket 有前 3 小时 payouts 运营更新，均非免费 mint。
- Thinkers Club / Shit Capital / Flame-BTC：付费公售仍 LIVE，不重推。DAEMONS 仍是圣诞前后主网、成员免费 mint、waitlist，不是已开铸。ANKOU 日期仍 TBA。Z3RO Terminal 仍是演示/测试网。
- Sparecycle / Duet / NoPvP / GiwaTerminal / SPCX / Amend：非免费 mint，无实质变化，不重推。

## 看见但未收

- @Leadchains：建号约 2.4 日、26 粉 / 9 帖，资料栏 https://leadchains.trading/prelaunch/ 。自称社交投资游戏，虚拟资金，计划 2026-12-26 开闸，可留邮箱通知。不是加密 mint / 发射台，未送审、不收。
- @tailtradesxyz：已在「看见但未收」名单；本轮仍出现，bio 有 CA `0xC6333959D096f151dee397AC56c9259a1127B870`，无足以改判的新证据，不重收。
- @QikLaunch（qiklaunch.com）：Web2 数字产品上架/SEO 页，不是加密发射台，不收。
- @CatchTheRocket：自称 parody token，在讲 pump.fun 模式，不收。
- @SocialGruff / https://gruff.family/：DogeOS 社交/搜寻产品，建号约 42.7 日、2008 粉；本轮见到 11-02 旧官帖「coming to DogeOS」的转帖，站点已有 DogeOS 登录，非免费 mint / 非极早期发射，不收。
- @2hourfunEco：2hour.fun 生态号，不另建卡。
- @Cryptokaranbtc、@trangnguyenpc3：无资料栏、无官网，仅为回复/转帖噪声，不收。
- @deca_labs：静号回退帖中被提及，约 1.4 万粉，不是本轮新的免费 mint/发射官号，不收。
- @furbi59360（Deadpool Ninja Turtle ordinals）：约 594 日号，已在未收名单，本轮无足以改判的新证据，不重收。
- @GeneraNetwork、@LedgerGank、@axtapi、@LongyuNetwork、@BitnetMoney、@CadaCasoxLayer、@ninedragons_rtc、@anvoraapp、@ponsbot_ai、@OUTLAWSxNFT、@tinylegendsfun、@eutoprotocol、@PropsMintHQ、@PixelPuddingsRH：本轮无足以改判的新证据，不重收。

## Discord Peek

- 本路由 parent 并行 computerUse 处理。/tmp/r2186/discord_peek.json 已存在（attemptedAt 2026-11-25 16:03:33 CST）。
- loginOk=false，loginWall=true，channelsPeeked=false。打开频道前被重定向到 Discord 登录墙（Welcome back / Email or Phone / Password / Log In / QR / passkey / Register）。四频道均未翻，lastSeen 应保持约 2026-11-23 22:19–22:56 CST。
- dry-run apply 已写 discordPeekDeferred=true。RESULT 仍留 placeholder，供 parent 按最终 peek JSON 合并。nag=false，不单为登录墙再催。

## 失败 / 备注

- dsFallback=false。X 搜索 27/27 无解析错误（x_usage errors=[]）。部分 MCP 回写被截成 preview，已从 Full text 资产还原进 x_raw，没有重查同一搜索。
- 个别推文（含 @sleighpad、@Leadchains）API 未返回 entities.urls，已用 curl 展开文中 t.co，未另耗 X 读。
- search_users 仍不可用，静号走 SILENT_DOGE 关键词回退。
- 十栏关键词均已跑到；userFollow 本轮分片已刷完；mentions 本轮覆盖 DogeEVM/BTC/Starknet/squeek/STARX；瘦栏 LZ/DOGE/BTC 做了 24 小时补搜。
- 未修改 /workspace/early-scout/data.json，未 git commit / push。dry-run 写在 /tmp/r2186/data.json。

## notify 与告警草稿

- notify=true。理由：The Jacket 首次进入 ≤2h 窗口；同时真新收录 SleighPad、ZEROFLASH（自称即将免费 mint，非 LIVE）、StrayKin（官网白名单申请已开，非已开铸 LIVE）。须点名，不能只写见面板。

草稿 alertMessage：

轮次【R2186】首次≤2h告警：The Jacket @TheJacket_NVDA 首次进入≤2h窗口，官方开窗仍为2026-11-25 18:00 CST（10:00 UTC），Robinhood Chain 持有人免费 mint（RebelKin/Argonauts/Vaultlings/Quotrons404，只付 gas），OpenSea the-jacket-man，4444份、上次已铸0，本轮开火时尚未 LIVE；R2177 是未进2h时的新收录提醒，本轮为首次≤2h告警。新收录：SleighPad（@sleighpad / https://sleighpad.fun/）为 Solana 圣诞慈善发射台，非免费 mint，官网已上线但 $SLEIGH mint 未配置、无CA；ZEROFLASH（@ZEROFLASH_NFT）自称5,555份即将免费 mint（on Zero，前111钱包优先），无官网无合约无日期，不是已开铸 LIVE；StrayKin（@StrayKinNFT / https://straykin.xyz/）官网白名单申请已开（不保证名额），自称将在 OpenSea 铸造，日期和价格待官宣，不是已开铸免费 mint LIVE。面板：https://reboot7454.github.io/early-scout/

## 关键产物路径

- /tmp/r2186/x_raw/*.json、/tmp/r2186/x_all.json、/tmp/r2186/x_usage.json、/tmp/r2186/x_flat.json
- /tmp/r2186/ds_payload.json、/tmp/r2186/ds_score.json、/tmp/r2186/ds_alert.json
- /tmp/r2186/new_cards.json、/tmp/r2186/notify.json
- /tmp/r2186/apply_r2186.py（dry-run 默认；APPLY_ALLOW_WORKSPACE 守卫仍在）
- /tmp/r2186/data.json（dry-run 输出，源 /tmp/r2186/data.json.src）
- /tmp/r2186/RESULT_R2186.md
- /tmp/r2186/discord_peek.json（parent 并行 peek，登录墙）
- /tmp/r2186/triforge_rpc.json（parent 约 16:01:19 CST 快照，本轮未再打 RPC）
