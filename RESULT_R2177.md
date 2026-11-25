# R2177 执行结果（2026-11-25 约 11:28–11:42 CST，Asia/Shanghai）

- mode=ample，常规增量（非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- xReads=27（主扫 23 + SILENT_STARK 1 + 瘦栏 24h 3），remainingBefore=801，remainingAfter=774 / 1000
- softCap=28，minSpend=20，silentCap=2（silent 计在 softCap 外）；主扫含瘦栏 24h 为 26，未超 softCap
- 27/27 search_posts_all 一次成功，无分页、无同 query 重试、无额外探索、getUsers=0
- lastScout= 2026-11-25 11:44:49 CST（已写入工作区并待推送）

## 覆盖

- 十栏+GAPS 30m 关键词：全部跑到（KW_LZ/TAPE/GIWA/DOGE/BTC/STARK/MINT/MINE/PAD/GO/ELY/GAPS）
- 瘦栏 30m 命中：LayerZero 3、Tape 12、GIWA 10、DogeEVM 19、BTC 0、Starknet 1
- 瘦栏 24h 补搜：KW_LZ_24（20）、KW_BTC_24（25）、KW_STARK_24（25）；Tape/GIWA/DogeEVM 30m≥5，跳过
- userFollow：soft-brush 完成。cursor 911 @Gravitieslol 起 50 号至 @kpadfun；next 961 @geniedotfun；wrap=false；MUST 重叠 0。UF1/UF2/UF3 均为 0 帖
- mentions 本轮 24h：pads-rest 14、GIWA 25 触顶、Tape 25 触顶、LayerZero-24h 24、Elysium-rest 24。下轮：DogeEVM / BTC / Starknet / squeek / STARX
- silentAccounts：ran=true，lane=Starknet，method=24h has:mentions 回退（searchUsers 不可用），hits=4，capped=false，seen=3（@JokerFaceCM、@TheAltconomy、@HBO_data），sentToReview=1（@JokerFaceCM），admitted=0。下轮 silent：打新

## 新收录

1. **duet** / @DuetFun / https://useduet.fun  
   Solana 上面向人类与 AI 代理的 pump.fun 发射台：一步发币并在同一笔交易里用 SOL 做首买。建号 2026-11-23 06:09:06 CST（约 2.22 天），13 粉 / 1 帖。官帖 11:21:20 CST 称已 LIVE；官网写 $DUET CA Soon，本轮未见 CA。官网与官推互证（siteXMutual=yes）。不是免费 mint。栏位：台子/Meme。DS overall=80，admit=true。已挂 userFollowWatch + agentPadWatch。focus=false。

2. **the-jacket** / @TheJacket_NVDA / https://opensea.io/collection/the-jacket-man/overview  
   Robinhood Chain NFT 铸造窗。官帖 11:17:21 CST 宣布 2026-11-25 18:00 CST（10:00 UTC，不要误读成 10:00 CST）向 RebelKin / Argonauts / Vaultlings / Quotrons404 持有人免费 mint（只付 gas）。OpenSea 收藏页回链 @TheJacket_NVDA，供应 4,444、本轮 totalSupply=0。无独立官网。本轮尚未进入 2 小时窗口，不是已开铸 LIVE。本轮未另拉该 handle 资料，不编造建号时间或粉数。栏位：打新。DS overall=72，admit=true。已挂 userFollowWatch + freeMintWatch。focus=false。@westofpixels 仅为转发/艺术家号，不另建卡。

3. **nopvp** / @NoPvPfun / https://nopvp.fun  
   Solana 上基于 pump.fun 的叙事发射台：同一叙事先填满曲线者为 #1，之后 copy 支付翻倍费用并买给先到持有人；0.1 SOL 入场且不退款。建号 2026-10-30 13:37:27 CST（约 25.91 天），237 粉 / 31 帖。官网与 app.nopvp.fun 均回链 @NoPvPfun（siteXMutual=yes）。不是免费 mint。本轮无自有官帖，仅见他人转发 72 小时活动。栏位：台子/Meme。DS overall=63，admit=true（账号已不新，仍因官网互证且入口可操作而收录）。已挂 userFollowWatch + agentPadWatch。focus=false。

## 库内重要变化

- **TRIFORGE** @TriForgeAgent / https://triforge.fun：公共 BSC RPC 只读（约 2026-11-25 11:35:24 CST，https://bsc-dataseed.binance.org/；选择子取自官网 config.js）。Forge Keys 免费铸仍 LIVE 未暂停，**271/3333→281/3333**（小幅增加，不重推）；付费预售仍开，lpMintOpen=true，lpOpened=false，lpFinalized=false，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST；claimsOpen=true、totalClaimed=1；miningTotalShares=6，miningPaused=false；tokenTradingEnabled=false。本轮见到 10:43 CST 白皮书上线官帖（https://triforge.fun/whitepaper），以及 09:17 CST 那则旧的「Presale — opens 02:01 UTC」帖，未见关窗/改期。免费 mint 与预售打开此前已提醒。本号不自动 mint。
- **Coffee Agents** @thecoffeeagents / https://coffeeagents.netlify.app：本轮仍见到 10:27 CST 官帖，进度仍 **188/1,500**，付费阶梯未开，未见 CA。官网静态页仍是占位进度。无实质变化，不重推。
- **Sparecycle**：新见 11:15 CST「100% Burn for $SPARE」及链上交易，以及 10:51 CST 奖励池说明（与 R2176 新收时一致）。不是免费 mint，不重推。
- **GiwaTerminal**：10:46 CST 回复称 GIWA is moving fast. More coming soon，无实质变化，不重推。
- **ORIPA** @oripaxyz：10:00 CST 官帖称 10 hours left，开窗仍 **2026-11-25 20:00 CST**（Taipei UTC+8）。本轮尚未进入 2 小时窗口，不告警、不重推。
- Ugly Puggies：再见到 first wl batch 官帖与 11:06 CST 互动回复，开铸仍 2026-11-25 21:00 CST（13:00 UTC），未到 2 小时窗口，不重推。
- 2hour.fun：再见到 10:02 CST Reservations are OPEN / 21:00 UTC 首窗官帖，真实开窗仍 **2026-11-26 05:00 CST**，不按今天 21:00 CST 或 ≤2h 告警，不重推。
- Shit Capital：11:09 CST 官帖称 300%+ oversubscribed、Genesis 仍约 44 小时关闭。付费，不是免费 mint，不重推。
- Thinkers Club / Shielded Wizards / Flame-BTC：付费窗口仍在或仅产品更新，无实质变化，不重推。
- Z3RO / lore / Amend / DAEMONS / ANKOU（本轮 0 帖，未见登记已开或日期落地）/ SPCX / Lamoryant / QQAI：无实质变化或未见新官宣，不重推。LE2H=0。

## 看见但未收

- **@Blob4agentk** / https://www.blobkinetiq.xyz/：自称 Elysium 吉祥物，官网仍写 CA Coming soon、Launched on Sent.money，未达 Elysium「On testnet/Announced 且写明部署」门槛。R2175 已看过，本轮无自有官帖，不收。
- **@JokerFaceCM** / http://Cartoon-Money.com：自称 $CBUCKS 于 2026-12-03 15:00 EST 开盘，静态站未回链官推，不是免费 mint。R2176 已不收，本轮无新互证，仍不收。
- **@GamaDotWin** / https://gama.win：GIWA 发射台 waitlist，官网回链官推，但约 65 天、本轮无自有官帖（仅被提及），不另建卡。
- **@2hourfunEco**：已知 2hour.fun 生态号，不另建卡。
- **@silentkeyeth**：无官网，以太坊 dead-man-switch，非铸造窗。本轮无自有官帖。
- **@QikLaunch** / https://qiklaunch.com、**@fleetify_dev** / https://fleetify.dev：非加密数字产品/Agent 控制台，KW_GO 噪声，不收。
- **@hoopermoran3597** / Moralume：约 12 天、4 粉，个人号发 $HOOPER 并称 Moralume is live on GIWA，不像官号且无独立官网，不收。
- **@szymansk68**、**@aripintujg**、**@abdo_mahmoud_7**：GIWA Sepolia 个人/测试网发射浏览页，非官方，不收。
- **@westofpixels**：约 132 天、3221 粉，资料栏写 Artis on Robinhood，转发 The Jacket 免费铸窗口；官号按 @TheJacket_NVDA 建卡，不另建艺术家号。
- **@TheAltconomy**、**@HBO_data**：silent Starknet 回退里的老号研究/社区向帖，与铸造窗无关。

## discordPeek

attempted，loginOk=false，discordPeekDeferred=true。登录墙 https://discord.com/login?redirect_to=%2Flogin%3Fredirect_to=%252Fchannels%252F1502958818865188956%252F1537897411668746302 （Welcome back / Email or Phone / QR / passkey）。未填凭证、未点 Log In。channelsPeeked=false，lastSeen 未改（2026-11-23 22:19–22:56 CST，积压约 37h+）。R2158 已请用户重登，本轮 nag=false，未重发登录表。详情见 /tmp/r2177/discord_peek.json（约 11:29:08 CST）。父代理可再核或补填。

## 失败 / dsFallback

- 无 dsFallback。X 搜索 27/27 成功，无重试。
- DeepSeek flash：Duet / The Jacket / NoPvP 同批评分成功（admit 均为 true；overall 80 / 72 / 63）。首轮评分 JSON 曾在 the-jacket 处截断，已提高 max_tokens 后重评成功，未改用本地兜底。alert 调用成功；alertMessage 仅做「值班提醒」结构、站点/供应/2 小时窗口与「本号不自动 mint」句式的轻度整理，事实未改（原文见 notify.json alertMessageDsRaw）。
- TRIFORGE RPC 只读成功（bsc-dataseed.binance.org，约 11:35:24 CST）。
- write_to_file 预览曾截断长回包，已改用 Full text 资产文件解析，数据齐全。

## 写盘说明

执行端未改 `/workspace/early-scout/data.json`，也未 git commit / push。自检可用：

```
cp /workspace/early-scout/data.json /tmp/r2177/data.json.src && \
EARLY_SCOUT_DATA=/tmp/r2177/data.json.src APPLY_DRY_RUN=1 APPLY_DRY_OUT=/tmp/r2177/data.json \
python3 /tmp/r2177/apply_r2177.py
```

父代理正式写盘：先备份，再 `APPLY_ALLOW_WORKSPACE=1 EARLY_SCOUT_DATA=/workspace/early-scout/data.json python3 /tmp/r2177/apply_r2177.py`（不要用执行端来 commit/push）。

## notify / alert

- notify: true
- reason: 真新收录 The Jacket（自称持有人免费 mint，开窗 2026-11-25 18:00 CST，尚未进入 2 小时窗口，不是已开铸 LIVE）、Duet（不是免费 mint）与 NoPvP（不是免费 mint）。TRIFORGE 271→281 仅小幅增加，不作为重推理由。
- alert:

值班提醒 R2177：新收录 The Jacket（@TheJacket_NVDA / OpenSea the-jacket-man）——Robinhood Chain 上 4,444 份持有人免费 mint（RebelKin / Argonauts / Vaultlings / Quotrons404，只付 gas），开窗 2026-11-25 18:00 CST（10:00 UTC），本轮尚未进入 2 小时窗口，不是已开铸 LIVE。新收录 Duet（@DuetFun / https://useduet.fun）——Solana 上人类与 AI 代理 pump.fun 发射台，建号约 2.22 天，13 粉，官帖称已 LIVE，$DUET CA Soon，不是免费 mint。新收录 NoPvP（@NoPvPfun / https://nopvp.fun）——Solana pump.fun 叙事发射台，0.1 SOL 入场不退款，不是免费 mint。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/


## 父代理写盘

已于 2026-11-25 11:44:49 CST 正式写入 /workspace/early-scout/data.json（WATCH_LEAK_RECENT 0）。准备只提交 data.json 与 RESULT_R2177.md。
