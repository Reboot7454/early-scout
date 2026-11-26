# 早期打新雷达 R2230 RESULT

工作目录 /tmp/r2230/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_STARK）、站点/链上核验、写盘并推送面板。新收录 1 项：Sae / @SaePadKR。DeepSeek HTTP 401，admit/score/alert 走 dsFallback。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 15:01 CST。写盘 lastScout 以 data.json meta.lastScout 为准（2026-11-26 15:15:53 CST）。这是重置后的第十五轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=645（首搜脚注 remainingToday=644，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。独立查询 26（主扫 25 + silent 1）。MUST_WIN 与 KW_TAPE 因写盘失败各补拉 1 次（补的是丢失的原始结果，不是再确认重读），API 调用合计 28，触到 softCap。未翻页（MUST_WIN / TAPE / GIWA / MINT / PAD / GO / ELY / MEN_BTC 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=28（独立查询 26 + 2 次写盘失败补拉），remainingBefore=645，remainingAfter=617。额度 delta=28，与 API 调用次数一致。ingest 曾按原始文件把 remainingAfter 记成 619，写盘已改用 live 脚注 617。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；KW_STARK_24 对引用帖 2125815935869325525 有非致命 include-level Authorization Error，数据仍 n=25 可用）：
UF1 0，UF2 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 5，MUST_OFF 1，
KW_LZ 1，KW_TAPE 25（触顶），KW_GIWA 25（触顶），KW_DOGE 4，KW_BTC 4，KW_STARK 0，
KW_MINT 25（触顶），KW_MINE 0，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 25（触顶），KW_GAPS 9，
MEN_DOGE 1，MEN_BTC 25（触顶），MEN_STARK 3，MEN_PADS 21，
SILENT_STARK 4，
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 1、TAPE 25 触顶、GIWA 25 触顶、DOGE 4、BTC 4、STARK 0、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 25 触顶、GAPS 9。MUST_WIN 24h 25 触顶 + MUST_WIN2 5、MUST_OFF 30m 1。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 997 @RoboDucksRH → 写盘后 cursor 1047 @Joayofundev，wrap=false，分片末端 @latebitcoiners。预跳已知 NF 5 个（@UseZPadX @agenticsocial @dyorcash @404Naroba @MOIbitcoin），from: 实际 45 个。UF1=0，UF2=0。UF 总账户写盘后 2461（+@SaePadKR）。
- mentions 本轮轮换：DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=1，MEN_BTC=25，MEN_STARK=3，MEN_PADS=21）。下轮：GIWA / Tape / LayerZero / Elysium。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=1→24h=23）、KW_DOGE_24（30m=4→24h=25）、KW_BTC_24（30m=4→24h=25）、KW_STARK_24（30m=0→24h=25）。TAPE 25、GIWA 25 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY）改成 24h。
- 静号：SILENT_STARK，search_users 不可用，24h has:mentions 回退，命中 4。下轮静号：GIWA。

## 新收录

- **Sae / Sae 새（@SaePadKR / https://sae.wtf/）**：建号 2026-11-26 07:57:57 CST（约 0.3 天），9 粉 / 8 帖 / 1 媒体，未认证，xUserId 2125740427852824576。官网 HTTP 200，标题 “SAE 새 — Where New Things Take Flight”，描述与官帖一致；站点为约 1337 字节 SPA 壳，静态 HTML 未见回链 x.com，siteXMutual=partial。官帖 2026-11-26 15:55 CST 线程（https://x.com/SaePadKR/status/2125845988636287223 ，续帖 2125845990662094909，回复 2125847591833448895）自称 GIWA 测试网发射台：一笔交易发射代币，可用 ETH 或从 Solana 钱包交易；无预售、无 bonding curve、无后续迁移。平台币 $SAE 先在 Solana 上线，GIWA 主网后再 1:1 快照并正式开台。测试网已自称上线，但不是主网 mint LIVE。**不是免费 mint / 免费登记**。栏：GIWA，focus=false，status=watching，dsFallback overall 74。已进 userFollowWatch + giwaWatch。

因真新收录，notify=true。不是免费 mint / 免费登记，告警已点名 SaePad。

## 看见但未收

- VardoBot：约 1.41 天、1 粉，bio 写 MegaEth；站点 https://vardo.gg / test.vardo.gg HTTP 200，标题为 Vardø - Prediction Markets on Base。官方 X 是 @vardo_gg，本轮未在已知 handle 表中，VardoBot 不是官号。未额外 getUsers，不收录。
- @LOLOnCanton：R2229 已跳过（约 9.4 天、603 帖，带推荐链接），本轮仍不是极早期可打机会，不建卡。
- TINDGEAR：26 天 / 953 帖，不是早期，跳过。
- @getleash_app 已在库（id getleash / leashwick）。本轮见到 “Unleash releases today” 免费游玩 $500 游戏口径，不是 mint，不另建卡、不重推。
- 其余 RT / 经文类 / 中龄噪音跳过。

## 库内进度（无首次 ≤2h，不重推）

- Ugly Puggies：免费 mint 仍 LIVE，OpenSea 507/777、持有 319、地板 0.000159 ETH（R2229 为 496/317/0.000159）。阶段沿用 R2227 SIGNED_PRESALE #3 至 2026-11-27 13:30 CST。R2223 已首次 ≤2h。
- deMiners：付费公售仍 LIVE，1373/3333、持有 181、地板 0.000107 ETH，与 R2229 持平。
- The Jacket：214/777、持有 136、地板 0.61 USDG，与 R2229 持平。
- Guns Of The Hood：111/10000、持有 16，与 R2229 持平。MUST 仅见表情回复，无改期。
- Shielded Wizards：免费公售仍 LIVE，146/3333（与 R2229 持平），reserved=6（R2229 为 2），mintOpen 仍 True，price=0。
- F0B90B：473/10000（R2229 为 472），mintOpen 仍 True。
- Antopia：6350/8888，免费额度仍满；游戏 beta 今日 21:00 CST 不是 mint 改期。
- TriForge：本轮公共 BSC RPC（2026-11-26 15:12:34 CST）Forge Keys 864/3333、claims 42、预售 1、挖矿 6（R2229 链上为 861/42/1）。MUST 官帖称 855/3333、claims 41，相对链上略滞后，以链上为准。只是进度。
- 2hour.fun：窗口仍关，/api/window traderCount=43；本轮 RSC 快照含 `"open":false`，确认当前窗未开。下一窗仍 2026-11-27 05:00–07:00 CST。
- Vicehood 官方合集 vchood 仍 0、MINTING_SOON，首窗 2026-11-27 01:00 CST；未与同名 vicehood 合集混淆。
- Wildlife Universe：仍 0，首窗 2026-11-26 21:30 CST，未到 ≤2h。
- Bonebloom：仍 0，预售仍 2026-11-27 20:30 CST。
- Lamoryant：免费登记仍开。本轮未再拆 mint 页，沿用 R2229：官方 mint 页已公开，仍写 0 / 1,356 minted、OG Phase 11:00 UTC / 19:00 CST。未注水 HTML 倒计时全零按 JS 占位处理，不以开铸 LIVE 计。距开铸未到 ≤2h，不提前告警。
- QQAI：开铸仍约 18:00 CST，写盘时约 2.7h，未到首次 ≤2h。
- Crawlers Agent：MUST 再见到官帖重申今晚 20:00 CST，CA 仍 0x5c92D8b2aa748722D7855CD4493F208f66757fd6。官网口径沿用 R2229 OPENING SOON（本轮未再拆站）。未到 ≤2h。
- RuninAI：每日 20:00 CST 窗口重申；CA 仍 0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6。one-click launchpad 仍未见已 LIVE。未到首次 ≤2h。
- Hamster CombatHQ：仍 WL Launching Soon，R2226 已通知，不重推。
- 卡灵战争：免费开包仍自称 LIVE，R2224 已通知，不重推。
- AbyssLabs / Bonebloom：MUST 仍见周五 Nov 27 预告，无改期。

写盘时即将到来但均未进入首次 ≤2h：QQAI 约 2.7h（18:00）、Lamoryant 约 3.7h（19:00）、Crawlers / RuninAI 约 4.7h（20:00）、Wildlife 约 6.2h（21:30）、Vicehood 约 9.7h（2026-11-27 01:00）（均为 CST）。

## Discord

未打开 computerUse。discordPeekDeferred=true，discordLoginOk=false。登录墙与 R2206 以来相同，不要重发登录表单。须父进程在同一轮补 Peek；若补扫出现免费 mint/登记，再通知。

## notify

notify=true：新收录 Sae / @SaePadKR（不是免费 mint，但属真新收录，须提醒一次）。无 le2h。面板 https://reboot7454.github.io/early-scout/

本号不自动 mint。
