# R2175 执行结果（2026-11-25 约 10:46 CST，Asia/Shanghai）

- mode=ample，常规增量（非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2170）
- xReads=28（主扫 23 + SILENT_DOGE 1 + 瘦栏 24h 4），remainingBefore=856，remainingAfter=828 / 1000
- softCap=28，minSpend=20，silentCap=2（silent 计在 softCap 外）；主扫含瘦栏 24h 为 27，未超 softCap
- 28/28 search_posts_all 一次成功，无分页、无同 query 重试、无额外探索、getUsers=0
- lastScout（dry-run 副本）= 2026-11-25 10:46:24 CST

## 覆盖

- 十栏+GAPS 30m 关键词：全部跑到（KW_LZ/TAPE/GIWA/DOGE/BTC/STARK/MINT/MINE/PAD/GO/ELY/GAPS）
- 瘦栏 30m 命中：LayerZero 2、Tape 25、GIWA 11、DogeEVM 1、BTC 0、Starknet 0
- 瘦栏 24h 补搜：KW_LZ_24（18）、KW_DOGE_24（25）、KW_BTC_24（25）、KW_STARK_24（25）；Tape/GIWA 30m≥5，跳过
- userFollow：soft-brush 完成。cursor 811 @computeroll 起 50 号至 @foomeapp；next 861 @wildlifeuni_55；wrap=false；MUST 重叠 0。UF1 2 帖（已入库 @RuninAI_com 回复），UF2/UF3 0 帖
- mentions 本轮 24h：pads-rest 12、GIWA 25 触顶、Tape 25 触顶、LayerZero-24h 21、Elysium-rest 24。下轮：DogeEVM / BTC / Starknet / squeek / STARX
- silentAccounts：ran=true，lane=DogeEVM，method=24h has:mentions 回退（searchUsers 不可用），hits=1，capped=false，seen=1，sentToReview=0，admitted=0。下轮 silent：BTC

## 新收录

1. **coffee-agents** / @thecoffeeagents / https://coffeeagents.netlify.app  
   自称免费 mint LIVE（官帖 188/1,500），BNB Chain / Agent ID 持有人每钱包 1 份免费，总量 5,555，付费阶梯未开。栏位：BN Agent 钱包。siteXMutual=yes。本轮未见 CA。DS overall=67。已挂 userFollowWatch + freeMintWatch + bnAgentWatch。focus=false。

2. **giwaterminal** / @Giwaterminal / https://giwaterminal.com  
   GIWA 链发射台聚合交易终端，不是免费 mint。栏位：GIWA。siteXMutual=yes。本轮未见自有原创帖（includes 核到资料）。DS overall=52。已挂 userFollowWatch + giwaWatch。focus=false。

## 库内重要变化

- **TRIFORGE** @TriForgeAgent / https://triforge.fun：公共 BSC RPC 只读（约 2026-11-25 10:42:02 CST，https://bsc-dataseed.binance.org/）。Forge Keys 免费铸仍 LIVE 未暂停，**56/3333→238/3333**（大幅跳升）；付费预售仍开，lpMintOpen=true，lpOpened=false，lpFinalized=false，lpTotalMinted=0，lpTotalPaid=0，窗口仍 2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST；claimsOpen=true、totalClaimed=1；miningTotalShares 1→6，miningPaused=false；tokenTradingEnabled=false。本轮仍见到 09:17 CST 那则「Presale — opens 02:01 UTC」官帖，未见关窗/改期。免费 mint 与预售打开此前已提醒，本轮因免费铸大幅跳升写入 alert。本号不自动 mint。
- **ORIPA** @oripaxyz / https://oripa.xyz：官网+官帖确认首包开窗 **2026-11-25 20:00 CST**（Taipei UTC+8；官帖 10:00 CST 称 10 hours left）。此前 Nov 25 仅为日期占位。本轮尚未进入 2 小时窗口，不告警、不重推。
- Ugly Puggies：再见到 09:35 CST first wl batch 官帖（与 R2173/R2174 同一则），开铸仍 2026-11-25 21:00 CST，未到 2 小时窗口，不重推。
- 2hour.fun：10:02 CST 官帖称 Reservations are OPEN，Today at 21:00 UTC 首窗打开 = **2026-11-26 05:00 CST**，不要误读成今天 21:00 CST，不按 ≤2h，不重推。
- Thinkers Club / Shit Capital / Shielded Wizards / Flame-BTC：付费窗口仍在，无实质变化，不重推。
- Z3RO / lore / Amend / DAEMONS / ANKOU / SPCX / Lamoryant / QQAI：无实质变化或未见新官宣，不重推。LE2H=0。

## 看见但未收

- **@QQAgent_BNB**（2026-11-25 08:02:57 CST 建号，0 粉）自称 QQAI 官网已 LIVE（https://qqai-bnb.pages.dev/）并给 CA 0x69b8cA186337701262310079C14a715387338888；官网只回链该后建号，不回链库内更早官号 @QQAI_BNB。视为可能马甲/仿号，不另建卡，也未把 CA/官网并进 QQAI 卡。
- **@warpnetp2p** / https://warpnet.site：P2P 社交网络，非铸造窗。
- **@Blob4agentk** / https://www.blobkinetiq.xyz/：自称 Elysium 吉祥物，CA Coming soon，站称 Launched on Sent.money，未达 Elysium「On testnet/Announced 且写明部署」门槛。
- **@zauberdotfun**：本轮无资料栏官网、无自有官帖（仅 MEN_LZ24 includes）。
- **@WeathookETH**、**@PilotusTrade**：无官网、无自有官帖。
- **@2hourfunEco**：已知 2hour.fun 生态号，不另建卡。
- **@abdo_mahmoud_7**（GiwaPad github.io）：GIWA Sepolia 个人浏览页，测试网，非官方。
- silent @fizalasdair：2011 年老号，DogeOS 测试网任务搬运，不收录。

## discordPeek

attempted，loginOk=false，discordPeekDeferred=true。登录墙 https://discord.com/login?redirect_to=%2Flogin%3Fredirect_to%3D%252Fchannels%252F1502958818865188956%252F1537897411668746302 （Welcome back / Email or Phone / QR / passkey）。未填凭证、未点 Log In。channelsPeeked=false，lastSeen 未改（2026-11-23 22:19–22:56 CST，积压约 36h+）。R2158 已请用户重登，本轮 nag=false，未重发登录表。

## 失败 / dsFallback

- 无 dsFallback。X 搜索 28/28 成功，无重试。
- DeepSeek flash：Coffee Agents 首批评分成功（admit=true / overall=67）；同批 GiwaTerminal 在 highlights 处截断，已单独补评成功（admit=true / overall=52）。alert 调用成功；alertMessage 仅做「新收录」结构与面板句式的轻度整理，事实未改（原文见 notify.json alertMessageDsRaw）。
- TRIFORGE RPC 只读成功（bsc-dataseed.binance.org，约 10:42:02 CST）。
- write_to_file 预览曾截断长回包，已改用 Full text 资产文件解析，数据齐全。

## 写盘说明

执行端未改 `/workspace/early-scout/data.json`，也未 git commit / push。自检可用：

```
cp /workspace/early-scout/data.json /tmp/r2175/data.json.src && \
EARLY_SCOUT_DATA=/tmp/r2175/data.json.src APPLY_DRY_RUN=1 APPLY_DRY_OUT=/tmp/r2175/data.json \
python3 /tmp/r2175/apply_r2175.py
```

父代理正式写盘：先备份，再 `APPLY_ALLOW_WORKSPACE=1 EARLY_SCOUT_DATA=/workspace/early-scout/data.json python3 /tmp/r2175/apply_r2175.py`（不要用执行端来 commit/push）。

自检 dry-run 已成功（WATCH_LEAK_RECENT 0，added coffee-agents / giwaterminal，uf_next 861 @wildlifeuni_55，uf_total 2378；workspace 仍为 R2174 / lastScout 2026-11-25 10:15:07 CST）。

## notify / alert

- notify: true
- reason: 真新收录 Coffee Agents（自称免费 mint LIVE，188/1,500）与 GiwaTerminal（GIWA 交易终端，非免费 mint）；库内 TRIFORGE Forge Keys 免费铸大幅跳升 56/3333→238/3333。
- alert:

值班提醒 R2175：新收录 Coffee Agents（@thecoffeeagents / https://coffeeagents.netlify.app）——BNB Chain 上 Agent ID 持有人免费 mint 仍 LIVE，官帖称 188/1,500 免费份已领，总量 5,555，付费阶梯尚未开，本轮未见 CA。新收录 GiwaTerminal（@Giwaterminal / https://giwaterminal.com）——GIWA 链聚合交易终端，不是免费 mint。库内 TRIFORGE（@TriForgeAgent / https://triforge.fun）Forge Keys 免费铸仍 LIVE 未暂停，公共 BSC RPC 进度 56/3333→238/3333（核验约 2026-11-25 10:42:02 CST）；付费预售仍开（lpMintOpen=true，本轮 lpTotalMinted=0）。免费 mint 与预售打开此前已提醒，本轮只因免费铸大幅跳升写入。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
