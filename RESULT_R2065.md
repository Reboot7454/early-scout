# RESULT R2065

- time: 2026-11-21 06:02:25 CST（Asia/Shanghai）
- lastScout: 2026-11-21 06:02:25 CST
- notify: false
- newAdmits: （无）
- panel: https://reboot7454.github.io/early-scout/
- prev: R2064 为 X-pass（commit 6830e16，无新收录）；本轮为 X-pass R2065

## alert
notify=false，无新收录、无 mint/open ≤2h、窗口无实质变化，不推送。

## X 额度
- remainingBefore: 33（与 R2064 remainingAfter 一致；UF1 第一读后余 32 of 1000）
- xReads: 6
- remainingAfter: 27
- mode: near-exhausted（距 08:00 CST 重置约 4 轮；`python3 scripts/x_budget.py 33`）
- softCap / minSpend / silentCap: 8 / 6 / 0
- breakdown: UF 5 + MUST 1 = 6（KW_THIN=0、KW_CORE=0、MEN=0、SILENT=0、THIN_24h=0）
- 为达到 minSpend 6 且不超过 softCap 8，UF 用 5 次合并 from: 覆盖分片，MUST 1 次合并 1.5h。MUST 9 帖、oldest 20:30:26Z 已到 start_time 20:30:00Z（04:30 CST），无需翻页。不是 post-reset-full。
- 同一 handle 本轮只拉一次。历史 NF 未连刷。

## 覆盖
- userFollow: 是。cursor 1000 @BnbCache → next 1028 @IgniteDotFun。walk 28 kept 24；firstKept @BnbCache，lastKept @Kitzyclubz。历史 NF 未连刷：@UseZPadX（i=1001）、@agenticsocial（i=1005）、@dyorcash（i=1006）、@404Naroba（i=1011）。skip_already=0，wrap=false，posts=0（UF1–5 均为 0）。
- 十栏关键词: 否。tenLanes 因 near-exhausted（kwCore=0 / kwThin=0）延期。
- 瘦栏 24h 补搜: 否，未跑。
- MUST 官号合并 1.5h：page1=9 帖，oldest 04:30:26 CST，已盖住窗口，未翻页。覆盖 @KToonsNFT @RobinYieldRH @Hooddrivee @Kismonft @mercesdotlive @RuninAI_com @FinalDays365 @kangozro。
- mentions: 本轮延期，原计划下轮：LayerZero 与 Elysium+kinetiq。
- silentAccounts.ran: false（silentCap=0，未跑；主扫不记成 silent）。silentNext: Elysium（保持 R2064 指定，不按 2065%11 跳步）。
- thinOfficial: near-exhausted 本轮未单开，薄栏 KW / 24h / mentions 均延期。
- Discord Peek: deferred=true。peek 文件已落地但 loginOk=false：computerUse 打开 #alpha-3-new-accounts 即遇登录墙（Welcome back / 邮箱密码 / QR / passkey），立即停止，未登录未扫其余频道。用户电脑离线，浏览走 box 网络，box 无已登录 Discord 会话。lastSeen 沿用 R2062 未改（alpha-3 04:53 / backup 03:44 / smart 04:44 / alpha-1 04:49 CST）。请父代理在有会话的路径立刻补增量 Peek，不要向用户催登录、不要重发 Secure Form。11/15–11/18 积压仍不在本轮增量范围。

## 新收录
- 无。本轮 X 路径无新卡。未调用 DeepSeek 批量 admit/score（无候选）。

## 库内续更 / 看见但未新收（不重推）
- @mercesdotlive：MUST 未见更新帖；最新仍是 05:30:00 CST 预告 $WAGE on Pons Sat 21 Nov · 15:00 UTC（23:00 CST），时间未改。
- @RuninAI_com：05:02–05:29 CST 多条回复仍在预热 Agent ID PoW mining，文案为 “the mine is next” / “when the mine opens”，未宣布已开窗。
- @RobinYieldRH：05:05:50 CST 仅自转旧「MINT IS LIVE」帖；进度官帖仍是 04:30:26 CST 的 389/500。
- @kangozro：05:45:12 / 05:59:58 CST 两条回复仅附图片（t.co 指向自身帖 photo/1），无新开铸/登记官宣。已在库，不重收。
- UF 分片 1.5h 内 0 帖，未见新号。

## 窗口刷新（均不重推）
- Kinetiq Toons：关窗仍未二次确认。OpenSea 584/5555、持有 449、地板 0.0088 HYPE。MUST 未见 @KToonsNFT 新帖，最新仍是 02:05:51 CST 关窗官宣。
- Robin Yield：公售仍 LIVE。OpenSea 404/500、持有 151、地板 0.00005 ETH。MUST 官帖仍 04:30:26 CST 报 389/500 Almost sold out。
- Hood Drive：官网仍 WL Closed，开铸仍 2026-11-22 01:00 CST（官网页文案 Mint Nov 21, 17:00 UTC，约 18.9h，le2h=false），OpenSea hood-drive 供应 0。
- Kismo Seekers：WL Phase II 仍开（/api/gen-wl open=true, phase=2）。接口仍未返回 until，沿用既有截止 2026-11-21 08:31:58 CST（约 2.5h，le2h=false）。报名页静态文案仍有默认 “closed for now”，但页面会请求该接口，以 open=true 为准。未见开铸 LIVE。
- Merces / RuninAI：无新开窗。时间与预热状态未改，不重推。

## Watch / 漏挂
- 本轮无新卡。近轮已收录（kangozro / singularity-cash / spek-fun / final-days 等）均已在 Watch。
- 未对历史旧卡整库补挂。
- 软债：cantonPadWatch / glazeWatch / tokenWorksPlaygroundWatch lastChecked 已刷新为本轮时间。

## 下轮
- UF 从 1028 @IgniteDotFun 继续（@UseZPadX / @agenticsocial / @dyorcash / @404Naroba / @MOIbitcoin 等为历史 NF 或 suspended，禁止再请求）。
- mentions: LayerZero 与 Elysium+kinetiq（本轮延期，原计划保留）。
- silent: Elysium（保持，勿按轮次取模跳步）。
- 十栏 KW 与瘦栏 24h：近耗尽已延期；08:00 CST 后首轮全量补扫须含瘦栏 24h 关键词 + Discord 积压。
- Kismo 截止 08:31:58 CST，下轮若仍开放可能进入 le2h（约 2.5h → 下轮约 2.0h 临界）。
- Discord：本轮 deferred，父代理若有会话须立刻补增量；未到 cutoff 或触顶的频道下轮续翻。11/15–11/18 积压仍待专门清理。
