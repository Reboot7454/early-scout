# 早期打新雷达 R2228 RESULT

工作目录 /tmp/r2228/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_DOGE）、站点/链上核验、写盘并推送面板。新收录 1 项：Ruby / @rubykit_cc。DeepSeek HTTP 401，admit/score/alert 走 dsFallback。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 14:03 CST。写盘 lastScout 以 data.json meta.lastScout 为准。这是重置后的第十三轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=696（首搜 UF1 脚注 remainingToday=695，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 24 + silent 1 = 25，低于 softCap，已达 minSpend。MUST_WIN 因 24h 句柄列表过长拆成 2 次检索（仍计入主计划，未超 softCap）。未翻页（MUST_WIN / MINT / PAD / GO / ELY / KW_*_24 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=25（main=24，silent=1），remainingBefore=696，remainingAfter=671。额度 delta=25，与检索次数一致。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；KW_STARK_24 对引用帖 2125815935869325525 有非致命 include-level Authorization Error，数据仍 n=25；其余主结果可用；中间 remainingToday 未逐条落盘，不捏造）：
UF1 0，UF2 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 5，MUST_OFF 0，
KW_LZ 0，KW_TAPE 17，KW_GIWA 22，KW_DOGE 4，KW_BTC 10，KW_STARK 2，
KW_MINT 25（触顶），KW_MINE 0，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 25（触顶），KW_GAPS 15，
MEN_DOGE 3，MEN_BTC 24，MEN_STARK 2，MEN_PADS 18，
SILENT_DOGE 0，
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 17、GIWA 22、DOGE 4、BTC 10、STARK 2、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 25 触顶、GAPS 15。MUST_WIN 24h 25 触顶 + MUST_WIN2 5、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 897 @toshidotfun → 写盘后 cursor 947 @FlywheelAgent，wrap=false，分片末端 @BNBRunnerz。预跳已知 NF 6 个（@exec_terminal @orivatbnb @spiderproject69 @useampad @astropad_real @bianjiayou），from: 实际 44 个。UF1/UF2 result_count=0。UF 总账户写盘后 2458（+@rubykit_cc）。
- mentions 本轮轮换：DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=3，MEN_BTC=24，MEN_STARK=2，MEN_PADS=18）。下轮：GIWA / Tape / LayerZero / Elysium。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_DOGE_24（30m=4→24h=25）、KW_STARK_24（30m=2→24h=25）。TAPE 17、GIWA 22、BTC 10 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY）改成 24h。
- 静号：SILENT_DOGE，search_users 不可用，24h has:mentions 回退，命中 0，sentToReview=0。下轮静号：BTC。

## 新收录

- **Ruby（@rubykit_cc / https://rubykit.cc/）**：建号 2026-11-25 09:25:52 CST（约 1.2 天），165 粉 / 71 帖，xUserId 2125400209824022528。官网与官推互证，GitHub https://github.com/rubykit-star/ruby。Robinhood Chain 只读工具套件（radar/clip/daily/lend/MCP 等）自称已 LIVE。官帖 14:00 CST（https://x.com/rubykit_cc/status/2125831920030523666）介绍 Ruby Lend 只读 Aave V3 LTV。官网写 $RUBY CA coming soon，本轮未见代币合约。**不是免费 mint / 免费登记**。栏：台子/Meme，focus=false，dsFallback overall 70。已进 userFollowWatch，未兼挂其它专项 Watch。因真新收录，notify=true。

## 看见但未收

- @openhypecom：建号 2021-03-30，约 8.5 万粉，官网 https://openhype.com/，自称 X Layer 上 TCG 已 live。旧号大体量，不是极早期，未建卡。
- Orbz 免费 mint（仅见第三方 @Annyd0o 转发点到 @0xstonkdad / Founder @HoodDrakes）：无官方 Orbz handle / 官网 / 官帖，不按已确认免费 mint LIVE 收录。@HoodDrakes 已在库。
- @tapegoldgolf：2023-11-28 号，X Layer circuit golf，不是极早期。
- @officialbunnyos：2025-09-26 号，约 14 个月、三千粉级，Base 发射预告，不是极早期。
- @ChainDNAapp：仅见发射地投票，无官网无已开张证据，未收。

## 库内进度（无首次 ≤2h，不重推）

- Ugly Puggies：免费 mint 仍 LIVE，OpenSea 484/777、持有 313、地板 0.000159 ETH（R2227 为 459/300/0.000169）。阶段沿用 R2227 SIGNED_PRESALE #3 至 2026-11-27 13:30 CST。R2223 已首次 ≤2h。
- deMiners：付费公售仍 LIVE，1373/3333、持有 181、地板 0.000107 ETH（R2227 为 1364/180）。
- The Jacket：214/777、持有 136、地板 0.61 USDG，与 R2227 持平。
- Guns Of The Hood：111/10000、持有 16，与 R2227 持平。
- Shielded Wizards：免费公售仍 LIVE，145/3333，与 R2227 持平。
- F0B90B：472/10000（R2227 为 469），mintOpen 仍 True。
- Antopia：6350/8888，免费额度仍满；官帖预告游戏 beta 今日 21:00 CST，不是 mint 改期。
- TriForge：链上 Forge Keys 856/3333、claims 41、预售 1（R2227 卡片 837/40/1），只是进度。
- 2hour.fun：窗口仍关，/api/window traderCount=43，下一窗仍 2026-11-27 05:00–07:00 CST。
- Vicehood 官方合集 vchood 仍 0、MINTING_SOON，首窗 2026-11-27 01:00 CST；未与同名 vicehood 合集混淆。
- Wildlife Universe：仍 0，首窗 2026-11-26 21:30 CST，未到 ≤2h。
- Bonebloom：仍 0，预售仍 2026-11-27 20:30 CST。
- Lamoryant：/apply 仍 200，免费登记仍开；02:40 CST 官帖称 WL 将在数小时内重开、mint 站即将公开。开铸仍约 19:00 CST，未到 ≤2h。
- QQAI：开铸仍约 18:00 CST，未到 ≤2h。
- Crawlers Agent：开铸仍约 20:00 CST。本轮 BSC RPC 核到 CA 0x5c92D8b2aa748722D7855CD4493F208f66757fd6 已有代码（codeLen=15400），此前写未部署/未核到；官网仍 MINT OPENING SOON，不是已开铸 LIVE，未到 ≤2h，不提前告警。
- RuninAI：每日 20:00 CST 窗口重申；另预告 one-click launchpad，未见已 LIVE。未到首次 ≤2h。
- Hamster CombatHQ：仍 WL Launching Soon，R2226 已通知，不重推。
- 卡灵战争：免费开包仍自称 LIVE，R2224 已通知，不重推。

写盘时即将到来但均未进入首次 ≤2h：QQAI 18:00、Lamoryant 19:00、Crawlers / RuninAI 20:00、Wildlife 21:30（均为 2026-11-26 CST）。

## Discord

未打开 computerUse。discordPeekDeferred=true，discordLoginOk=false。登录墙与 R2206 以来相同，不要重发登录表单。须父进程在同一轮补 Peek；若补扫出现免费 mint/登记，再通知。

## notify

notify=true：新收录 Ruby（不是免费 mint，但属真新收录，须提醒一次）。无 le2h。面板 https://reboot7454.github.io/early-scout/

本号不自动 mint。
