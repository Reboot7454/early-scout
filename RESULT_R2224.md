# 早期打新雷达 R2224 RESULT

工作目录 /tmp/r2224/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_LZ）、站点/链上核验、写盘并推送面板。DeepSeek API 401（key invalid），判断/文案/打分改为本地兜底，**dsFallback=true**，未用高成本模型批量。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 12:00 CST。写盘 lastScout=2026-11-26 12:17:04 CST。这是重置后的第九轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=795（首搜 UF1 脚注 remainingToday=794，+1 回溯）。todayReset=2026-11-27T00:00:00.000Z。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 23 + silent 1 = 24，低于 softCap，已达 minSpend。未翻页（MUST_WIN / MINT / PAD / GO / MEN_BTC / KW_*_24 / SILENT_LZ 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=24（main=23，silent=1），remainingBefore=795，remainingAfter=771。额度 delta=24，与检索次数一致。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；error=None；多数 remainingToday 仅能从首尾脚注回溯，不逐条捏造中间剩余）：
UF1 0，UF2 0，MUST_WIN 25（触顶未翻页），MUST_OFF 0，
KW_LZ 2，KW_TAPE 25（触顶），KW_GIWA 10，KW_DOGE 10，KW_BTC 1，KW_STARK 2，
KW_MINT 25（触顶），KW_MINE 2，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 8，KW_GAPS 6，
MEN_DOGE 3，MEN_BTC 25（触顶未翻页），MEN_STARK 2，MEN_PADS 20，
SILENT_LZ 25（触顶未翻页），
KW_LZ_24 23，KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 2、TAPE 25 触顶、GIWA 10、DOGE 10、BTC 1、STARK 2、MINT 25 触顶、MINE 2、PAD 25 触顶、GO 25 触顶、ELY 8、GAPS 6。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 697 @Trexionbsc → 写盘后 cursor 747 @AIZOBsc，wrap=false，分片末端 @iglusol。预跳已知 NF 12 个（@lootbale @useapppayfun @CyclopesElysium @elyword_xyz @AgentFramlin404 @RedirectCash @kyte_market @vytraqfun @hyperlinkdotfun @HordeOnElysium @lazabitmeme @XiangHao91647），from: 实际 38 个。UF1 result_count=0，UF2 result_count=0。UF 总账户写盘后 2452（含本轮新挂的 @Arbitershield @closari_rh @askinkbot @octiohq @kaling_war）。
- mentions 本轮轮换：DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=3，MEN_BTC=25 触顶未翻页，MEN_STARK=2，MEN_PADS=20）。下轮：GIWA / Tape / LayerZero / Elysium。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=2→24h=23）、KW_BTC_24（30m=1→24h=25）、KW_STARK_24（30m=2→24h=25）。TAPE 25、GIWA 10、DOGE 10 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO）改成 24h。
- 静号：SILENT_LZ，search_users 不可用，24h has:mentions 回退。ran=true，result_count=25 触顶未翻页，未见需新收的静号作者，sentToReview=0，admitted=0。未做 getUsers 第二读。下轮静号指向 Elysium。

## 新收录

### 卡灵战争 @kaling_war（id=kaling-war）

- 类别 Tape/电路，chain=BNB / TapeOut / Binance Agent ID，**focus=false**（不是仓鼠/toychain）。
- **免费开包已开张**：官网 https://agentid.cards/ 写明现在有 12 个免费包，不用注册、不用钱包。官帖 2026-11-26 11:55:25 CST（https://x.com/kaling_war/status/2125800568744755377）宣布今天正式开张，并给免费开一包链接。必须 notify 并点名。
- 建号 2024-01-23 17:43:45 CST（约 1038 天），87 粉 / 仅 4 帖，xUserId 1749729508746276864，属旧号新启用，风险高。
- 自称用 Agent ID 做身份、TapeOut 电路做灵魂，开包后可流片成 BSC 电路 NFT；官号也写明不构成链上强制拦截。官网静态页未见 X 链接（siteXMutual=none），但官帖与官网文案一致。
- dsFallback score overall=66（early=55，actionable=88，novelty=80，risk=82）。已挂 userFollowWatch + tapeWatch + tapeOutWatch + bnAgentWatch + freeMintWatch。

### Arbiter Protection @Arbitershield（id=arbitershield）

- 类别 台子/Meme，chain=Robinhood Chain，focus=false，不是免费 mint/登记。
- 建号 2026-11-26 03:29:27 CST（约 0.36 天），18 粉 / 24 帖，xUserId 2125671575798063104。
- 官帖 2026-11-26 11:59:00 CST（https://x.com/Arbitershield/status/2125801468443894021）称钱包快照、股票报价、交易解释三项覆盖服务已可试用，每笔 0.02 USDG、10 分钟窗口。官网 https://www.arbiterprotection.xyz/ HTTPS 200，与官推互链（siteXMutual=yes）。站点展示 $ARBITER 0x5fCb44CE44d3f82e37E893Ad14F86D26948876bD，本轮未上链独立复核。
- dsFallback score overall=68（early=96，actionable=70，novelty=72，risk=80）。已挂 userFollowWatch。

### Closari Protocol @closari_rh（id=closari-rh）

- 类别 台子/Meme，chain=Robinhood Chain，focus=false，不是免费 mint/登记。
- 建号 2026-11-23 15:59:39 CST（约 2.84 天），12 粉 / 38 帖，xUserId 2124774600538279936。
- 官帖 2026-11-26 12:00:01 CST（https://x.com/closari_rh/status/2125801727483879617）介绍日度股票收盘参考仓位方案（3/10）。bio 写 Coming to Robinhood Chain。官网 https://closari.net/ HTTPS 200，静态页很薄（偏 SPA），未见 X 链接（siteXMutual=none），描述可试 paper position。不是已开交易。
- dsFallback score overall=55（early=92，actionable=40，novelty=68，risk=75）。已挂 userFollowWatch。

### Inkbot @askinkbot（id=askinkbot）

- 类别 台子/Meme，**不进 Elysium 栏**。chain 自称迁往 Elysium（此前在 Base）。focus=false，不是免费 mint/登记。
- 建号 2026-11-18 12:06:52 CST（约 8.0 天），16 粉 / 39 帖，xUserId 2122903801908637696。
- 官帖 2026-11-26 11:52:17 CST（https://x.com/askinkbot/status/2125799778613149851）明确：正在从 Base 迁往 Elysium，**尚无官方代币**，Base 上任何 Inkbot 代币都不是官方的。官网 https://www.askinkbot.app/ HTTPS 200，twitter:site=@askinkbot（siteXMutual=yes）。Elysium 生态页本轮 HTTP 429，未核到名录；仅 moving to + NO token，没有 testnet/Announced+明确部署证据。先前轮次曾因过薄暂不建卡，本轮已有官号自述，故收录到台子/Meme。
- dsFallback score overall=56（early=78，actionable=50，novelty=60，risk=78）。已挂 userFollowWatch（未挂 elysiumWatch）。

### Octio @octiohq（id=octiohq）

- 类别 台子/Meme，chain=Robinhood Chain，focus=false，不是免费 mint/登记。
- 建号 2026-11-07 02:04:02 CST（约 19.42 天），35 粉 / 31 帖，xUserId 2118765496040607744。
- 官帖 2026-11-26 12:03:00 CST（https://x.com/octiohq/status/2125802475378954502）介绍读取 Polymarket 隐含概率。官网 https://www.octio.xyz/ HTTPS 200，按次付费 API（CREDIT），失败不收费。bio 自报 $OCTIO 0x5e900b41adaba86881a07c2e7f5f761e601f027c，本轮未上链独立复核。静态页未见 X 链接（siteXMutual=none）。
- dsFallback score overall=58（early=70，actionable=62，novelty=64，risk=72）。已挂 userFollowWatch。

## 看见但未收

- **LumixPad @lumixpad**：账号 2023-09-05（约 1178 天）、19 粉 / 3 帖，官网 lumixpad.fun 自称 0% 费 Solana 发射台+DEX、0 coins launched。本轮无自有官帖，旧号证据薄，skip。
- **Nekohood @Nekointhehood**：约 92 天、936 粉 / 仅 2 帖，bio 写 free mint 3000，无官网、本轮无自有官帖。先前已 defer，继续 skip，避免把第三方转述误报成免费 mint LIVE。
- 已在库或非早期：ugly puggies 10:02 CST 致歉帖此前已记；Shielded Wizards 公售仍开（本轮 API 未重拉）；2hour.fun 第一场已关、发币费改免费此前已通知、第二窗仍 2026-11-27 05:00–07:00 CST，不重推。VardoBot / QikLaunch / 无粉转推垃圾等已过滤。

## 首次 ≤2h / 库内刷新（不另作改期）

- **Ugly Puggies @uglypuggies**：仍 MINTING，OpenSea 314/777（R2223 为 313），持有 237（R2223 为 240），地板 0.000169 ETH（R2223 为 0.000167 ETH）。SIGNED_PRESALE #2 仍至 2026-11-26 13:30:00 CST，写盘时约 1.22h，**首次 ≤2h 已在 R2223 提醒，本轮不重推**。SeaDrop HTML 本轮解析失败，供应取 OpenSea API。本号不自动 mint。
- Shielded Wizards：本轮未重拉 brimhollow API，仍沿用 R2223 的 138/3333。R2210 已通知，不重推。
- Antopia：链上 6344/8888（R2223 为 6342），saleOpen=true，免费额度仍满 4000/4000。付费窗仍至 2026-11-27 20:45 CST，未到 ≤2h，不重推。
- F0B90B：仍 mintOpen=true，462/10000，与 R2223 持平。
- The Jacket：仍 214/777，持有 136，地板 0.61 USDG，与上轮持平。
- deMiners：仍 1373/3333，持有 181，地板约 0.000107 ETH，与上轮持平。
- Wildlife / tiger-universe：合集 API 本轮 401，stats 仍 0 持有。SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起，距首窗约 9.2h，未到首次 ≤2h。
- Vicehood / vchood：官方合集仍 0/3333、MINTING_SOON。首窗仍 2026-11-27 01:00 CST（约 12.7h），未到首次 ≤2h。同名合集 vicehood 仍约 209、不是该官号，未混淆。
- 2hour.fun / TRIFORGE / VALORIX / Agent Cards / Guns Of The Hood / Bonebloom / Crawlers Agent / HOLD：本轮未重拉对应站点/RPC，时间表未见新官宣改期，不重推。Crawlers 开铸仍预告 20:00 CST，未到首次 ≤2h。

## Watch / 漏挂

- 新卡均同时进 Watch（见上）。近期（round≥2100）Watch 漏挂检查 0，无需补挂。
- 软债 lastChecked 已刷新（含 canton/glaze/tokenWorks 与各必盯 Watch）。

## notify

- notify=true。原因：五项真新收录，其中 **卡灵战争为免费开包 LIVE，告警必须点名**。Ugly Puggies 仍在已提醒过的首次 ≤2h 窗内，不重推。
- namedFreeMintOrRegistration=['kaling-war']。namedPaidLe2h=[]。
- 面板 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。

## Discord

discordPeekDeferred=true。X 路径未打开 Discord/浏览器，只写占位。登录墙与 R2206/R2223 相同（Welcome back / Email/Password / Log In / QR / passkey），loginOk=false，四频道 lastSeen/cutoff 仍停在 2026-11-23 22:19–22:56 CST。用户此前已被告知用已有表单再登。同一未登录会话无法翻过登录墙，本轮不重复开浏览器、不重发登录表单。须父代理在同一轮补 Peek；补扫若出现免费 mint/登记再通知。
