# 早期打新雷达 R2229 RESULT

工作目录 /tmp/r2229/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_BTC）、站点/链上核验、写盘并推送面板。新收录 2 项：Necrolock / @NecroLockDotFun，antwork / @antworkdotfun。DeepSeek HTTP 401，admit/score/alert 走 dsFallback。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 14:29 CST。写盘 lastScout 以 data.json meta.lastScout 为准（2026-11-26 14:44:07 CST）。这是重置后的第十四轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=671（首搜 UF1 脚注 remainingToday=670，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 25 + silent 1 = 26，低于 softCap，已达 minSpend。MUST_WIN 因 24h 句柄列表过长拆成 2 次检索（仍计入主计划，未超 softCap）。未翻页（MUST_WIN / MINT / PAD / GO / MEN_GIWA / MEN_LZ24 / 瘦栏 24h 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=26（main=25，silent=1），remainingBefore=671，remainingAfter=645。额度 delta=26，与检索次数一致。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；KW_STARK_24 对引用帖 2125815935869325525 有非致命 include-level Authorization Error，数据仍 n=25 可用）：
UF1 3（有 next_token，未翻页），UF2 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 5，MUST_OFF 1，
KW_LZ 0，KW_TAPE 25（触顶），KW_GIWA 18，KW_DOGE 3，KW_BTC 1，KW_STARK 0，
KW_MINT 25（触顶），KW_MINE 0，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 22，KW_GAPS 19，
MEN_GIWA 25（触顶），MEN_TAPE 7，MEN_LZ24 25（触顶），MEN_ELY 21，
SILENT_BTC 13，
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 25 触顶、GIWA 18、DOGE 3、BTC 1、STARK 0、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 22、GAPS 19。MUST_WIN 24h 25 触顶 + MUST_WIN2 5、MUST_OFF 30m 1。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 947 @FlywheelAgent → 写盘后 cursor 997 @RoboDucksRH，wrap=false，分片末端 @drachma_elysium。预跳已知 NF 4 个（@kpin_ai @LostGodsOnRH @topaaafun @ripstackfun），from: 实际 46 个。UF1 result_count=3（已在库 @Kismonft / @SafeArcSpace），UF2=0。UF 总账户写盘后 2460（+@NecroLockDotFun +@antworkdotfun）。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25，MEN_TAPE=7，MEN_LZ24=25，MEN_ELY=21）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_DOGE_24（30m=3→24h=25）、KW_BTC_24（30m=1→24h=25）、KW_STARK_24（30m=0→24h=25）。TAPE 25、GIWA 18 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY）改成 24h。
- 静号：SILENT_BTC，search_users 不可用，24h has:mentions 回退，命中 13。下轮静号：Starknet。

## 新收录

- **Necrolock（@NecroLockDotFun / https://necrolock.fun/）**：建号 2026-11-11 22:43:27 CST（约 14.7 天），0 粉 / 6 帖，xUserId 2120527441097637888。官网与官推互证。Base 上独立 fair-launch 发射台（Bankr Launch SDK #4，Uniswap v4，流动性不可撤）。官帖 14:30 CST（https://x.com/NecroLockDotFun/status/2125839686342221961）自称独立、非 Bankr 运营，币大多归零。官网写明未审计。**不是免费 mint / 免费登记**。栏：台子/Meme，focus=false，dsFallback overall 72。已进 userFollowWatch，未兼挂其它专项 Watch。
- **antwork（@antworkdotfun / https://antwork.fun/）**：建号 2026-11-25 23:00:54 CST（约 0.65 天），171 粉 / 143 帖 / 84 媒体，xUserId 2125604714268246016。官网 HTTP 200，正文仍是 setting up the Hill；GitHub https://github.com/antwork。本轮未见该号自己的官帖；第三方 @SB_Rozz 称已在 Robinhood Chain 的 Pons pad 上线。约 15 小时 143 帖，发帖量异常，已在卡片标明刷量风险。**不是免费 mint / 免费登记**。栏：台子/Meme，focus=false，status=watching，dsFallback overall 69。已进 userFollowWatch。

因真新收录，notify=true。两项都不是免费 mint / 免费登记，告警里已逐个点名。

## 看见但未收

- @LOLOnCanton / https://www.loloncanton.xyz/：Canton 上 $LOL 已在 SuperNova 交易（本轮快照约 16 持有、9.5% bonded），带推荐链接，9 天号 601 帖偏刷，不是极早期可打机会，未建卡。
- @Kimchifunxyz / kimchifun.xyz：资料栏有站，但本轮官网 HTTP 500，且未见该号自有官帖，不收录。
- @Fire_Goat_Ember：本轮只有转推，资料展开为 Linktree/Instagram，证据薄，未收。
- @GiwaPump、@memeko 等：仅 mentions includes 见到资料，无本轮官帖、未额外 getUsers，不收录。
- @yeriyaps 点到的 GIWA 名（gasokfun、hamrdotfun、GIWAForge 等）已在库，不重复建卡。
- QikLaunch 等 web2/个人喊单、已在库的 LawoftheAbyss / wiseguyzRH / mmix_io / CubistHood，跳过。

## 库内进度（无首次 ≤2h，不重推）

- Ugly Puggies：免费 mint 仍 LIVE，OpenSea 496/777、持有 317、地板 0.000159 ETH（R2228 为 484/313/0.000159）。阶段沿用 R2227 SIGNED_PRESALE #3 至 2026-11-27 13:30 CST。R2223 已首次 ≤2h。
- deMiners：付费公售仍 LIVE，1373/3333、持有 181、地板 0.000107 ETH，与 R2228 持平。
- The Jacket：214/777、持有 136、地板 0.61 USDG，与 R2228 持平。
- Guns Of The Hood：111/10000、持有 16，与 R2228 持平。
- Shielded Wizards：免费公售仍 LIVE，146/3333（R2228 为 145），只是进度。
- F0B90B：472/10000，与 R2228 持平，mintOpen 仍 True。
- Antopia：6350/8888，免费额度仍满；游戏 beta 今日 21:00 CST 不是 mint 改期。
- TriForge：链上 Forge Keys 861/3333、claims 42、预售 1（R2228 为 856/41/1），只是进度。
- 2hour.fun：窗口仍关，/api/window traderCount=43，下一窗仍 2026-11-27 05:00–07:00 CST。
- Vicehood 官方合集 vchood 仍 0、MINTING_SOON，首窗 2026-11-27 01:00 CST；未与同名 vicehood 合集混淆。
- Wildlife Universe：仍 0，首窗 2026-11-26 21:30 CST，未到 ≤2h。
- Bonebloom：仍 0，预售仍 2026-11-27 20:30 CST。
- Lamoryant：免费登记仍开；官方 mint 页 https://lamoryant.com/mint 本轮已公开，仍写 0 / 1,356 minted、OG Phase 11:00 UTC / 19:00 CST。未注水 HTML 倒计时全零按 JS 占位处理，不以开铸 LIVE 计。距开铸未到 ≤2h，不提前告警。
- QQAI：开铸仍约 18:00 CST，未到 ≤2h。
- Crawlers Agent：官网仍 MINT · OPENING SOON，开铸仍约 20:00 CST，未到 ≤2h。
- RuninAI：每日 20:00 CST 窗口重申；one-click launchpad 仍未见已 LIVE。未到首次 ≤2h。
- Hamster CombatHQ：仍 WL Launching Soon，R2226 已通知，不重推。
- 卡灵战争：免费开包仍自称 LIVE，R2224 已通知，不重推。

写盘时即将到来但均未进入首次 ≤2h：QQAI 约 3.3h（18:00）、Lamoryant 约 4.3h（19:00）、Crawlers / RuninAI 约 5.3h（20:00）、Wildlife 约 6.8h（21:30）（均为 2026-11-26 CST）。

## Discord

未打开 computerUse。discordPeekDeferred=true，discordLoginOk=false。登录墙与 R2206 以来相同，不要重发登录表单。须父进程在同一轮补 Peek；若补扫出现免费 mint/登记，再通知。

## notify

notify=true：新收录 Necrolock、antwork（都不是免费 mint，但属真新收录，须提醒一次）。无 le2h。面板 https://reboot7454.github.io/early-scout/

本号不自动 mint。
