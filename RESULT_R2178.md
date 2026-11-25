# R2178 执行结果（2026-11-25 约 12:07–12:18 CST，Asia/Shanghai）

- mode=ample，常规增量（非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- xReads=27（主扫 23 + SILENT_MINT 1 + 瘦栏 24h 3），remainingBefore=774，remainingAfter=747 / 1000
- softCap=28，minSpend=20，silentCap=2（silent 计在 softCap 外）；主扫含瘦栏 24h 为 26，未超 softCap
- 27/27 search_posts_all 一次成功，无分页、无同 query 重试、无额外探索、getUsers=0
- lastScout= 2026-11-25 12:20:21 CST（已写入工作区并待推送）

## 覆盖

- 十栏+GAPS 30m 关键词：全部跑到（KW_LZ/TAPE/GIWA/DOGE/BTC/STARK/MINT/MINE/PAD/GO/ELY/GAPS）
- 瘦栏 30m 命中：LayerZero 0、Tape 25、GIWA 11、DogeEVM 5、BTC 0、Starknet 0
- 瘦栏 24h 补搜：KW_LZ_24（20）、KW_BTC_24（25）、KW_STARK_24（25）；Tape/GIWA/DogeEVM 30m≥5，跳过
- userFollow：soft-brush 完成。cursor 961 @geniedotfun 起 50 号至 @Shift_Forever；next 1011 @404Naroba；wrap=false；MUST 重叠 0。UF1/UF2/UF3 均为 0 帖
- mentions 本轮 24h：DogeEVM 10、BTC 25 触顶、Starknet 5、squeek 0、STARX 0。下轮：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- silentAccounts：ran=true，lane=打新，method=24h has:mentions has:links 回退（searchUsers 不可用），hits=25，capped=true，seen=24（未知作者，几乎全是已入库项目的白名单申请转帖），sentToReview=0，admitted=0。下轮 silent：挖矿

## 新收录

无。

## 库内重要变化

- **TRIFORGE** @TriForgeAgent / https://triforge.fun：公共 BSC RPC 只读（约 2026-11-25 12:11:53 CST，https://bsc-dataseed.binance.org/；选择子取自官网 config.js）。Forge Keys 免费铸仍 LIVE 未暂停，**281/3333→297/3333**（小幅增加，不重推）；付费预售仍开，lpMintOpen=true，lpOpened=false，lpFinalized=false，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST；claimsOpen=true、totalClaimed=1；miningTotalShares=6，miningPaused=false；tokenTradingEnabled=false。本轮再见到 10:43 CST 白皮书上线官帖。免费 mint 与预售打开此前已提醒。本号不自动 mint。官网静态 HTML 仍可能有 JS 水合前 “Contracts are not deployed yet” 占位，不以该句判断未部署。冷号风险仍在。
- **Coffee Agents** @thecoffeeagents / https://coffeeagents.netlify.app：本轮仍见到 10:27 CST 官帖，进度仍 **188/1,500**，付费阶梯未开，未见 CA。官网静态页仍是占位进度。无实质变化，不重推。
- **The Jacket** @TheJacket_NVDA / OpenSea the-jacket-man：再见到 11:17 CST 开窗官帖，时间仍 **2026-11-25 18:00 CST（10:00 UTC）**。本轮约 12:07 CST 开跑，尚未进入 2 小时窗口，不是已开铸 LIVE。已提醒过，不重推。
- **Amend** @useamend：11:07 CST 官帖称 Pairing is live（SOL/USDC/$AMEND/任意 CA/代币化股票配对），另有 $AMEND 回购销毁说明。不是免费 mint，不重推。
- **Sparecycle** @sparecycle7：11:51–11:53 CST 官帖称 rewards / job payments / $SPARE 合约已在浏览器验证。不是免费 mint，不重推。
- **ORIPA** @oripaxyz：10:00 CST 官帖称 10 hours left，开窗仍 **2026-11-25 20:00 CST**（Taipei UTC+8）。本轮尚未进入 2 小时窗口，不告警、不重推。
- Ugly Puggies：再见到 first wl batch 官帖与互动回复，开铸仍 2026-11-25 21:00 CST（13:00 UTC），未到 2 小时窗口，不重推。
- 2hour.fun：再见到 10:02 CST Reservations are OPEN / 21:00 UTC 首窗官帖，真实开窗仍 **2026-11-26 05:00 CST**，不按今天 21:00 CST 或 ≤2h 告警，不重推。
- Shit Capital：11:09 CST 官帖仍称 300%+ oversubscribed、Genesis 约 44 小时关闭。付费，不是免费 mint，不重推。
- Thinkers Club / Shielded Wizards / Flame-BTC：付费窗口仍在或仅产品更新，无实质变化，不重推。本轮 Shielded Wizards 0 帖。
- Duet：再见到 11:21 CST 已 LIVE 官帖（与 R2177 新收时同一则），无新变化，不重推。
- GiwaTerminal / SPCX / Z3RO / lore / DAEMONS / ANKOU（本轮 0 帖，未见登记已开或日期落地）/ Lamoryant / QQAI / NoPvP：无实质变化或未见新官宣，不重推。LE2H=0。
- **Vicehood** @Vicehood_RH（已在库，R2095）：官网 https://www.vicehood.xyz/ 标题 Vicehood RH | Early List，JS 可见 Early List open / Join 与 EVM 表单；本轮无自有官帖，仅见他人转发登记。不按新登记重推。

## 看见但未收

- **@velmarstocks** / https://www.velmarstocks.xyz/：2026-11-22 10:07:18 CST 建号（约 3.09 天），18 粉 / 5 帖。Robinhood Chain 股票代币只读价格看板，读取约 60 个股票代币的 Uniswap 池并标记价格是否一致。官网 HTTP 200，页脚与 twitter:site 回链 https://x.com/velmarstocks（siteXMutual=yes）。$VELMAR 栏目写 Soon，尚未公布 CA。本轮有两则自有官帖（12:02、12:06 CST）。DeepSeek admit=false，overall=36（early 94 / actionable 15）：只读看板，无 mint/发射窗，先观察不建卡。
- **@Overdriveagents** / https://www.overdriveagents.xyz/：约 33.83 天、1280 粉，资料栏自称 autonomous agent 发射台。本轮无自有官帖，仅出现在他人 KW_GO 帖的 includes。静态站与 JS 未见回链官推（仅表单占位 https://x.com/yourname），siteXMutual=no，不收。
- **@deca_labs** / https://decalabs.ai/：约 35.53 天、14593 粉，官网回链官推，文案称已融资 $12M 的 agent 孵化器。本轮无自有官帖，不是打新/发射台，非极早期，不收。
- **@JokerFaceCM** / http://Cartoon-Money.com：自称 $CBUCKS 于 2026-12-03 15:00 EST 开盘，静态站未回链官推，不是免费 mint。R2176/R2177 已不收，本轮无新互证，仍不收。
- **@GamaDotWin** / https://gama.win：GIWA 发射台 waitlist，官网回链官推，但约 65 天、本轮无自有官帖（仅被提及），不另建卡。
- **@2hourfunEco**：已知 2hour.fun 生态号，不另建卡。
- **@Nekointhehood**：约 91 天、915 粉、2 帖，资料写 free mint，无官网，本轮仅出现在他人 giveaway，不像已核验官宣窗，不收。
- **@NftGazers**：2020 年老号，转发已知 Lanternhold giveaway，不另建卡。

## discordPeek

attempted，loginOk=false，discordPeekDeferred=true。登录墙 https://discord.com/login?redirect_to=%2Flogin%3Fredirect_to=%252Fchannels%252F1502958818865188956%252F1537897411668746302 （Welcome back / Email or Phone / QR / passkey）。未填凭证、未点 Log In。channelsPeeked=false，lastSeen 未改（2026-11-23 22:19–22:56 CST，积压约 37h+）。R2158 已请用户重登，本轮 nag=false，未重发登录表。详情见 /tmp/r2178/discord_peek.json（约 12:08:48 CST）。父代理可再核或补填。

## 失败 / dsFallback

- 无 dsFallback。X 搜索 27/27 成功，无重试。
- DeepSeek flash：Velmar Stocks 评分成功（admit=false，overall=36）。因无新收录且库内无实质需提醒变化，未再调用 alert。
- TRIFORGE RPC 只读成功（bsc-dataseed.binance.org，约 12:11:53 CST）。
- write_to_file 预览曾截断长回包，已改用 Full text 资产文件解析，数据齐全。

## 写盘说明

执行端未改 `/workspace/early-scout/data.json`，也未 git commit / push。自检可用：

```
cp /workspace/early-scout/data.json /tmp/r2178/data.json.src && \
EARLY_SCOUT_DATA=/tmp/r2178/data.json.src APPLY_DRY_RUN=1 APPLY_DRY_OUT=/tmp/r2178/data.json \
python3 /tmp/r2178/apply_r2178.py
```

父代理正式写盘：先备份，再 `APPLY_ALLOW_WORKSPACE=1 EARLY_SCOUT_DATA=/workspace/early-scout/data.json python3 /tmp/r2178/apply_r2178.py`（不要用执行端来 commit/push）。

## notify / alert

- notify: false
- alertMessage: （无，本轮不推送）
- 原因见 `/tmp/r2178/notify.json`


## 父代理写盘

已于 2026-11-25 12:20:21 CST 正式写入 /workspace/early-scout/data.json（WATCH_LEAK_RECENT 0）。准备只提交 data.json 与 RESULT_R2178.md。
