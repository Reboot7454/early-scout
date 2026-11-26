# 早期打新雷达 R2231 RESULT

工作目录 /tmp/r2231/。本路完成 X 常规增量（UF1–UF3 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_GIWA）、站点/链上核验、写盘并推送面板。新收录 1 项：PonsVista / @ponsvista。DeepSeek HTTP 401，admit/score/alert 走 dsFallback。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 15:28 CST。写盘 lastScout 以 data.json meta.lastScout 为准（2026-11-26 15:50:06 CST）。这是重置后的第十六轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=617（首搜脚注 remainingToday=616，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。独立查询 26（主扫 25 + silent 1）。MUST_WIN、KW_TAPE、KW_GIWA 因写盘失败各补拉 1 次（补的是丢失的原始结果，不是再确认重读），API 调用合计 29。主扫正好触到 softCap 28，另加 silent 1。未翻页（MUST_WIN / TAPE / GIWA / MINT / PAD / GO / ELY / MEN_GIWA / MEN_LZ24 / SILENT_GIWA 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=29（独立查询 26 + 3 次写盘失败补拉），remainingBefore=617，remainingAfter=588。额度 delta=29，与 API 调用次数一致。ingest 曾按原始文件把 reads 记成 26 / remainingAfter 591，写盘已改用 live 脚注 29 / 588。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；KW_STARK_24 对引用帖 2125815935869325525 有非致命 include-level Authorization Error，数据仍 n=25 可用）：
UF1 0，UF2 0，UF3 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 5，MUST_OFF 0，
KW_LZ 0，KW_TAPE 22，KW_GIWA 25（触顶），KW_DOGE 3，KW_BTC 6，KW_STARK 0，
KW_MINT 25（触顶），KW_MINE 2，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 25（触顶），KW_GAPS 13，
MEN_GIWA 25（触顶），MEN_TAPE 6，MEN_LZ24 25（触顶），MEN_ELY 21，
SILENT_GIWA 25（触顶），
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 22、GIWA 25 触顶、DOGE 3、BTC 6、STARK 0、MINT 25 触顶、MINE 2、PAD 25 触顶、GO 25 触顶、ELY 25 触顶、GAPS 13。MUST_WIN 24h 25 触顶 + MUST_WIN2 5、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 1047 @Joayofundev → 写盘后 cursor 1097 @OakAgentKit，wrap=false，分片末端 @priors_trade。预跳已知 NF 1 个（@ePegsV4），from: 实际 49 个。UF1=0，UF2=0，UF3=0。UF 总账户写盘后 2462（+@ponsvista）。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25，MEN_TAPE=6，MEN_LZ24=25，MEN_ELY=21）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_DOGE_24（30m=3→24h=25）、KW_STARK_24（30m=0→24h=25）。TAPE 22、GIWA 25、BTC 6 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY/MINE）改成 24h。
- 静号：SILENT_GIWA，search_users 不可用，24h has:mentions 回退，命中 25 触顶。下轮静号：DogeEVM。

## 新收录

- **PonsVista（@ponsvista / https://ponsvista.xyz/）**：建号 2026-11-24 00:04:26 CST（约 2.6 天），57 粉 / 9 帖，未认证，xUserId 2124896480557174784。官网 HTTP 200，标题 “PONSVISTA | Pons markets”，静态页回链 https://x.com/ponsvista 与 GitHub https://github.com/PonsVista/ponsvista，siteXMutual=mutual。官帖 2026-11-26 15:29 CST（https://x.com/ponsvista/status/2125854357338091648）列出当日已毕业 Pons 代币成交榜。页面自称含 Screener / Sniper / Bridge / Staking。资料栏自称 CA 0x182cd45105880a924c6e282c97a0b61bdce69e04，公共 BSC RPC 无代码，应为 Robinhood 链合约，本轮未在 RH RPC 独立核实，合约未核实。是已上线的行情/交易面板，**不是发射台，不是免费 mint / 免费登记**。栏：台子/Meme，focus=false，status=watching，dsFallback overall 71。已进 userFollowWatch（未兼挂 agentPad / Elysium / Tape / giwa Watch）。

因真新收录，notify=true。不是免费 mint / 免费登记，告警已点名 PonsVista。

## 看见但未收

- @FamiliarsAI / https://familiars-app.pages.dev/：约 29.8 天、35 粉，BNB Chain 4,444 NFT。官网同时有 “Sold out” 与占位 “Altar opens soon”；公共 BSC RPC totalSupply=4444 / MAX_SUPPLY=4444，已售罄。不是可打的早期机会，不收录。
- @QQAgent_BNB：后建号（约 1.3 天、0 粉），指向已在库 QQAI（@QQAI_BNB）。给出站点 https://qqai-bnb.pages.dev/ 与 Token/Mint 合约，已回写到 qqai 卡，**未把后建号并进官方 handle**，不另建卡。
- GIWA 第三方列表（@yeriyaps）提到但本轮无自有官帖、未做额外 getUsers 的号：@Kimchifunxyz（约 68 天）、@GiwaPump（约 120 天、库内已有 @GiwaPumpPad / giwapump）、@Deoksangi、@Loopy_GIWA、@Gaejuki_Giwa、@GIWA_Accordpay、@OsigeExchange、@Hanok_io、@kaachi_io。仅第三方提及，不收录，待官帖核验。
- KaleidoFi 约 138 天、ShieldSuite_ 约 227 天，不是极早期，跳过。
- @getleash_app 已在库。本轮未见新的 mint 翻转，不另建卡、不重推。
- 其余 RT / 空号机器人 / 中龄噪音跳过。

## 库内进度（无首次 ≤2h，不重推）

- Ugly Puggies：免费 mint 仍 LIVE，OpenSea 515/777、持有 327、地板 0.000159 ETH（R2230 为 507/319/0.000159）。阶段沿用 R2227 SIGNED_PRESALE #3 至 2026-11-27 13:30 CST。R2223 已首次 ≤2h。
- deMiners：付费公售仍 LIVE，1373/3333、持有 182（R2230 为 181）、地板 0.000107 ETH。只是进度。
- The Jacket：214/777、持有 136、地板 0.61 USDG，与 R2230 持平。
- Guns Of The Hood：111/10000 与 R2230 持平；/stats 本轮 401，持有沿用 16。MUST 仅见表情回复，无改期。官网 drop 页仍写 public mint stage is open。
- Shielded Wizards：免费公售仍 LIVE，brimhollow /launchpad/api/status minted=149/3333（R2230 为 146），reserved=2（R2230 为 6），mintOpen 仍 True，price=0。
- F0B90B：490/10000（R2230 为 473），mintOpen 仍 True。
- Antopia：6350/8888，免费额度仍满，与 R2230 持平。
- TriForge：本轮公共 BSC RPC（2026-11-26 15:44:46 CST）Forge Keys 869/3333、claims 42、预售 1、挖矿 6（R2230 链上为 864/42/1）。只是进度（Keys +5）。
- Valorix：Hero Card totalMinted=16（R2230 为 15），VALX fillSold 仍 0。
- Agent Cards：付费续铸仍开，sold=6844（fill 5000 + curve 1844），现价约 0.00252 BNB。不是免费 mint。
- 2hour.fun：窗口仍关，/api/window traderCount=43；本轮 HTML 仍见 SSR 占位 Window open，未解析到 open=true，无窗口已开证据。下一窗仍 2026-11-27 05:00–07:00 CST。
- Vicehood 官方合集 vchood 仍 0；首窗 2026-11-27 01:00 CST；未与同名 vicehood 合集混淆。
- Wildlife Universe：仍 0，官网仍写 26 Nov 7:00 PM IST（21:30 CST），未到 ≤2h。
- Bonebloom：仍 0，预售仍 2026-11-27 20:30 CST。
- Lamoryant：免费登记仍开。本轮未再拆 mint 页，沿用 R2229：官方 mint 页已公开，仍写 OG Phase 19:00 CST。不以开铸 LIVE 计。距开铸未到 ≤2h。
- QQAI：开铸仍约 18:00 CST。本轮后建号 @QQAgent_BNB 给出 https://qqai-bnb.pages.dev/ 与 Token 0x69b8cA186337701262310079C14a715387338888、Mint 0x313eedfBb409A886F55203AEEb7270CF77B65DfF；链上 startTime=2026-11-26 18:00 CST、token totalSupply=0、paused=0。未合并后建号为官号，合约未核实。写盘时约 2.2h，未到首次 ≤2h。
- Crawlers Agent：MUST 再见到官帖重申今晚 20:00 CST，CA 仍 0x5c92D8b2aa748722D7855CD4493F208f66757fd6。未到 ≤2h。
- RuninAI：每日 20:00 CST 窗口重申；CA 仍 0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6。one-click launchpad 仍未见已 LIVE。未到首次 ≤2h。
- Hamster CombatHQ：仍 WL Launching Soon，R2226 已通知，不重推。

写盘时即将到来但均未进入首次 ≤2h：QQAI 约 2.2h（18:00）、Lamoryant 约 3.2h（19:00）、Crawlers / RuninAI 约 4.2h（20:00）、Wildlife 约 5.7h（21:30）、Vicehood 约 9.2h（2026-11-27 01:00）（均为 CST）。

## Discord

未打开 computerUse。discordPeekDeferred=true，discordLoginOk=false。登录墙与 R2206 以来相同，不要重发登录表单。须父进程在同一轮补 Peek；若补扫出现免费 mint/登记，再通知。

## notify

notify=true：新收录 PonsVista / @ponsvista（不是免费 mint，但属真新收录，须提醒一次）。无 le2h。面板 https://reboot7454.github.io/early-scout/

本号不自动 mint。
