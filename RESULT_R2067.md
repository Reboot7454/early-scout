# RESULT R2067

- time: 2026-11-21 06:41:17 CST（Asia/Shanghai）
- lastScout: 2026-11-21 06:41:17 CST
- notify: true
- newAdmits: （无）
- notifyReason: Kismo Seekers Whitelist Phase II 截止沿用 2026-11-21 08:31:58 CST，约 1.84h，首次进入 ≤2h（免费报名，不是免费 mint LIVE）
- panel: https://reboot7454.github.io/early-scout/
- prev: 写盘前远程已是 R2066（7e9d690，DC 增量合并到 R2065 X-pass：commit / camellia-dex / futderby / pari-protocol / corbelfinance）；本轮为 X-pass R2067

## alert
notify=true（≤2h，非新收录）。见面板 alertMessage / 本聊天转发。

## X 额度
- remainingBefore: 27（与 R2065 remainingAfter 一致；UF1 第一读后余 26 of 1000）
- xReads: 6
- remainingAfter: 21
- mode: near-exhausted（距 08:00 CST 重置约 2 轮；`python3 scripts/x_budget.py 27`）
- softCap / minSpend / silentCap: 8 / 6 / 0
- breakdown: UF 5 + MUST 1 = 6（KW_THIN=0、KW_CORE=0、MEN=0、SILENT=0、THIN_24h=0）
- 为达到 minSpend 6 且不超过 softCap 8，UF 用 5 次合并 from: 覆盖分片，MUST 1 次合并 1.5h（start_time 2026-11-20T21:07:05Z）。MUST page1=10 帖，oldest 05:20:08 CST，距 start_time 05:07:05 CST 仍有 13 分钟缺口，但该段已被 R2065 MUST（从 04:30 CST）覆盖，故未翻页。不是 post-reset-full。
- 同一 handle 本轮只拉一次。历史 NF 未连刷。

## 覆盖
- userFollow: 是。cursor 1028 @IgniteDotFun → next 1053 beefdotfamily。walk 25 kept 24；firstKept @IgniteDotFun，lastKept @KymaLiquidity。历史 NF/suspended 未连刷：@MOIbitcoin（i=1030）。skip_already=0，wrap=false，posts=0（UF1–5 均为 0）。
- 十栏关键词: 否。tenLanes 因 near-exhausted（kwCore=0 / kwThin=0）延期。
- 瘦栏 24h 补搜: 否，未跑。
- MUST 官号合并 1.5h：page1=10 帖，oldest 05:20:08 CST；覆盖 @KToonsNFT @RobinYieldRH @Hooddrivee @Kismonft @mercesdotlive @RuninAI_com @FinalDays365 @kangozro。未见 @KToonsNFT / @RobinYieldRH / @Hooddrivee / @Kismonft / @FinalDays365 新帖。
- mentions: 本轮延期，原计划下轮：LayerZero 与 Elysium+kinetiq。
- silentAccounts.ran: false（silentCap=0，未跑；主扫不记成 silent）。silentNext: Elysium（保持 R2065/R2064 指定，不按 2067%11 跳步）。
- thinOfficial: near-exhausted 本轮未单开，薄栏 KW / 24h / mentions 均延期。
- Discord Peek: deferred=true。本路 computerUse 打开 #alpha-3-new-accounts 即遇登录墙，落地 https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302（Welcome back / 邮箱密码 / QR / passkey），loginOk=false，立即停止，未登录未扫其余频道。用户电脑离线，浏览走 box 网络，box 无已登录 Discord 会话。lastSeen 沿用 R2066 未改（alpha-3 05:57 / backup 05:29 / smart 05:36 / alpha-1 05:44 CST）。请父代理在有会话的路径立刻补增量 Peek，不要向用户催登录、不要重发 Secure Form。11/15–11/18 积压仍不在本轮增量范围。

## 新收录
- 无。本轮 X 路径无新卡。未调用 DeepSeek 批量 admit/score（无候选）。告警文案由 DeepSeek 生成。

## 库内续更 / 看见但未新收（不重推）
- @RuninAI_com：06:04–06:26 CST 多条新回复仍在预热 Agent ID PoW mining，文案为 “Mining is coming” / “the mine is next” / “when the mine opens”，未宣布已开窗。
- @mercesdotlive：MUST 未见更新帖；最新仍是 05:30:00 CST 预告 $WAGE on Pons Sat 21 Nov · 15:00 UTC（23:00 CST，约 16.3h），时间未改。
- @kangozro：窗口内仍是 R2065 已见的 05:45:12 / 05:59:58 CST 两条仅附图片回复，无新开铸/登记官宣。已在库，不重收。
- UF 分片 1.5h 内 0 帖，未见新号。

## 窗口刷新
- Kismo Seekers：WL Phase II 仍开（/api/gen-wl open=true, phase=2）。接口仍未返回 until，沿用既有截止 2026-11-21 08:31:58 CST（约 1.84h，**le2h=true，首次进入 ≤2h**）。报名页静态文案仍有默认 “closed for now”，但页面会请求该接口，以 open=true 为准。未见开铸 LIVE。R2005 已提醒 Phase II 开放，本轮是截止临近提醒（notify=true）。
- Kinetiq Toons：关窗仍未二次确认。OpenSea 584/5555、持有 449、地板 0.0087 HYPE（上轮 0.0088）。MUST 未见 @KToonsNFT 新帖，最新仍是 02:05:51 CST 关窗官宣。不重推。
- Robin Yield：公售仍 LIVE。OpenSea 404/500、持有 151、地板 0.00005 ETH。MUST 未见新进度官宣，官帖仍 04:30:26 CST 报 389/500。R2045 已提醒，不重推。
- Hood Drive：官网仍 WL Closed，开铸仍 2026-11-22 01:00 CST（官网页文案 Mint Nov 21, 17:00 UTC，约 18.3h，le2h=false），OpenSea hood-drive 供应 0。不重推。
- Merces / RuninAI：无新开窗。时间与预热状态未改（Runin 仅多了预热回复），不重推。

## Watch / 漏挂
- 本轮 X 路径无新卡。
- **监控 bug 修复（不重推）**：R2066 Discord 入库的 5 卡当时不在任何 Watch：commit（@commitdotfun）、camellia-dex（@camelliadexx）、futderby（@futderby）、pari-protocol（@pariprotocol）、corbelfinance（@corbelfinance）。本轮已补进 userFollowWatch（accounts + candidateIds）。无对应专用栏 Watch（非已核验 Elysium / 非 BN Agent pad / 非免费 mint）；corbelfinance 的 Elysium 仅 “next” 预告，不进 elysiumWatch。
- 未对历史旧卡整库补挂。
- 软债：cantonPadWatch / glazeWatch / tokenWorksPlaygroundWatch lastChecked 已刷新为本轮时间。

## 下轮
- UF 从 1053 beefdotfamily 继续（@MOIbitcoin 为历史 suspended，禁止再请求）。
- mentions: LayerZero 与 Elysium+kinetiq（本轮延期，原计划保留）。
- silent: Elysium（保持，勿按轮次取模跳步）。
- 十栏 KW 与瘦栏 24h：近耗尽已延期；08:00 CST 后首轮全量补扫须含瘦栏 24h 关键词 + Discord 积压。
- Kismo 截止 08:31:58 CST，已 le2h；下轮若仍开放应续盯，关闭或开铸再报，勿重复刷同一截止提醒（除非状态变化）。
- Discord：本轮 deferred，父代理若有会话须立刻补增量；未到 cutoff 或触顶的频道下轮续翻。11/15–11/18 积压仍待专门清理。
