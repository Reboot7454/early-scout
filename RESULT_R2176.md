# R2176 执行结果（2026-11-25 约 11:20 CST，Asia/Shanghai）

- mode=ample，常规增量（非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- xReads=27（主扫 23 + SILENT_BTC 1 + 瘦栏 24h 3），remainingBefore=828，remainingAfter=801 / 1000
- softCap=28，minSpend=20，silentCap=2（silent 计在 softCap 外）；主扫含瘦栏 24h 为 26，未超 softCap
- 27/27 search_posts_all 一次成功，无分页、无同 query 重试、无额外探索、getUsers=0
- lastScout（dry-run 副本）= 2026-11-25 11:18:48 CST

## 覆盖

- 十栏+GAPS 30m 关键词：全部跑到（KW_LZ/TAPE/GIWA/DOGE/BTC/STARK/MINT/MINE/PAD/GO/ELY/GAPS）
- 瘦栏 30m 命中：LayerZero 0、Tape 25、GIWA 15、DogeEVM 12、BTC 0、Starknet 1
- 瘦栏 24h 补搜：KW_LZ_24（18）、KW_BTC_24（25）、KW_STARK_24（25）；Tape/GIWA/DogeEVM 30m≥5，跳过
- userFollow：soft-brush 完成。cursor 861 @wildlifeuni_55 起 50 号至 @orivatbnb；next 911 @Gravitieslol；wrap=false；MUST 重叠 0。UF1/UF2/UF3 均为 0 帖
- mentions 本轮 24h：DogeEVM 9、BTC 25 触顶、Starknet 5、squeek 0、STARX 0。下轮：pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- silentAccounts：ran=true，lane=BTC，method=24h has:mentions 回退（searchUsers 不可用），hits=14，capped=false，seen=14，sentToReview=1（@TheEyesBTC），admitted=0。下轮 silent：Starknet

## 新收录

1. **sparecycle** / @sparecycle7 / https://sparecycle.tech  
   Robinhood Chain 闲置 GPU 可核验 AI 任务网络。建号 2026-11-24 12:55:23 CST（约 0.93 天），59 粉 / 38 帖。$SPARE 已在 Pons v2 发射并 LIVE，CA 0x012D695B94377E0c7b9EdEE3d824259BaA37cf3A。官网与官推互证（siteXMutual=yes）。不是免费 mint。栏位：挖矿。DS overall=80，admit=true。已挂 userFollowWatch + miningWatch。focus=false。

## 库内重要变化

- **TRIFORGE** @TriForgeAgent / https://triforge.fun：公共 BSC RPC 只读（约 2026-11-25 11:14:09 CST，https://bsc-dataseed.binance.org/；选择子取自官网 config.js）。Forge Keys 免费铸仍 LIVE 未暂停，**238/3333→271/3333**（小幅增加，不重推）；付费预售仍开，lpMintOpen=true，lpOpened=false，lpFinalized=false，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST；claimsOpen=true、totalClaimed=1；miningTotalShares=6，miningPaused=false；tokenTradingEnabled=false。本轮见到 10:43 CST 白皮书上线官帖，以及 09:17 CST 那则旧的「Presale — opens 02:01 UTC」帖，未见关窗/改期。免费 mint 与预售打开此前已提醒。本号不自动 mint。
- **Coffee Agents** @thecoffeeagents / https://coffeeagents.netlify.app：本轮仍见到 10:27 CST 官帖，进度仍 **188/1,500**，付费阶梯未开，未见 CA。官网静态页仍是占位进度。无实质变化，不重推。
- **GiwaTerminal**：仅一条回复互动，无实质变化，不重推。
- **ORIPA** @oripaxyz：10:00 CST 官帖称 10 hours left，开窗仍 **2026-11-25 20:00 CST**（Taipei UTC+8）。本轮尚未进入 2 小时窗口，不告警、不重推。
- Ugly Puggies：再见到 first wl batch 官帖，开铸仍 2026-11-25 21:00 CST，未到 2 小时窗口，不重推。
- 2hour.fun：再见到 10:02 CST Reservations are OPEN / 21:00 UTC 首窗官帖，真实开窗仍 **2026-11-26 05:00 CST**，不按今天 21:00 CST 或 ≤2h 告警，不重推。
- Thinkers Club / Shit Capital / Shielded Wizards / Flame-BTC：付费窗口仍在，无实质变化，不重推。
- Z3RO / lore / Amend / DAEMONS / ANKOU（本轮 0 帖，未见登记已开或日期落地）/ SPCX / Lamoryant / QQAI：无实质变化或未见新官宣，不重推。LE2H=0。

## 看见但未收

- **@hylsiapools** / https://hylsiapools.tech：Hylsia Privacy Pools，建号约 10.52 天、105 粉，官网 meta 回链 @hylsiapools（siteXMutual=yes）。本轮官帖为预测市场隐私注资开发更新；官网自称 ETH/Robinhood Chain 上 ETH/USDG/USDC 隐私池，并写 Not independently audited。不是免费 mint，未见开放窗口。DeepSeek 评分 overall=50、admit=false（仅开发更新、当前不可操作），故不收录。
- **@TheEyesBTC** / http://eyes4384.com：自称 21,000 份 Bitcoin Ordinals 免费铸 + 感恩节 BAYC 赠送。建号约 221 天、807 粉、462 帖，官网是 SPA，静态 HTML 未回链官推，不够早期，不收。
- **@RGBMonsters**：约 20 天、1 粉、无官网，自称 SatSea 上 333 份免费铸 Soon™，尚未开铸，不收。
- **@JokerFaceCM** / http://Cartoon-Money.com：自称 $CBUCKS 于 2026-12-03 15:00 EST 开盘，静态站未回链官推，不是免费 mint，不收。
- **@GamaDotWin** / https://gama.win：GIWA 发射台 waitlist，官网回链官推，但约 65 天、本轮无自有官帖（仅被提及），不另建卡。
- **@2hourfunEco**：已知 2hour.fun 生态号，不另建卡。
- **@silentkeyeth**：无官网，以太坊 dead-man-switch，非铸造窗。
- **@UseFreed**：无官网，与打新无关。

## discordPeek

attempted，loginOk=false，discordPeekDeferred=true。登录墙 https://discord.com/login?redirect_to=%2Flogin%3Fredirect_to%3D%252Fchannels%252F1502958818865188956%252F1537897411668746302 （Welcome back / Email or Phone / QR / passkey）。未填凭证、未点 Log In。channelsPeeked=false，lastSeen 未改（2026-11-23 22:19–22:56 CST，积压约 37h+）。R2158 已请用户重登，本轮 nag=false，未重发登录表。

## 失败 / dsFallback

- 无 dsFallback。X 搜索 27/27 成功，无重试。
- DeepSeek flash：Sparecycle / Hylsia 同批评分成功；alert 调用成功；alertMessage 仅做「值班提醒」结构与面板句式的轻度整理，事实未改（原文见 notify.json alertMessageDsRaw）。
- TRIFORGE RPC 只读成功（bsc-dataseed.binance.org，约 11:14:09 CST）。首轮探测曾因 claim 地址少写一位、以及 mintStart/Deadline 选择子不同而漏读这两项，已按官网 config.js 纠正后重读，数字以最终 triforge_rpc.json 为准。
- write_to_file 预览曾截断长回包，已改用 Full text 资产文件解析，数据齐全。

## 写盘说明

执行端未改 `/workspace/early-scout/data.json`，也未 git commit / push。自检可用：

```
cp /workspace/early-scout/data.json /tmp/r2176/data.json.src && \
EARLY_SCOUT_DATA=/tmp/r2176/data.json.src APPLY_DRY_RUN=1 APPLY_DRY_OUT=/tmp/r2176/data.json \
python3 /tmp/r2176/apply_r2176.py
```

自检 dry-run 已成功（WATCH_LEAK_RECENT 0，added sparecycle，uf_next 911 @Gravitieslol，uf_total 2379；workspace 仍为 R2175 / lastScout 2026-11-25 10:48:11 CST）。

父代理正式写盘：先备份，再 `APPLY_ALLOW_WORKSPACE=1 EARLY_SCOUT_DATA=/workspace/early-scout/data.json python3 /tmp/r2176/apply_r2176.py`（不要用执行端来 commit/push）。

## notify / alert

- notify: true
- reason: 真新收录 Sparecycle（Robinhood Chain GPU 任务网，$SPARE 已 LIVE，不是免费 mint）。TRIFORGE 238→271 仅小幅增加，不作为重推理由。
- alert:

值班提醒 R2176：新收录 Sparecycle（@sparecycle7 / https://sparecycle.tech）——Robinhood Chain 上的闲置 GPU 可核验 AI 任务网络，建号约 0.93 天，59 粉；$SPARE 已在 Pons v2 发射并 LIVE，CA 0x012D695B94377E0c7b9EdEE3d824259BaA37cf3A，官网与官推互证，不是免费 mint。本轮无新的自称免费 mint / 免费登记 / 免费 LIVE 项目被收录。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
