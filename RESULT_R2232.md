# 早期打新雷达 R2232 RESULT

工作目录 /tmp/r2232/。本路完成 X 常规增量（UF1–UF3 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_DOGE）、站点/链上核验、写盘并推送面板。新收录 1 项：TickPlus / @tickplus_xyz。另：QQAI（@QQAI_BNB）自称免费 mint 首次进入 ≤2h。DeepSeek HTTP 401，admit/score/alert 走 dsFallback。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 15:56 CST。写盘 lastScout 以 data.json meta.lastScout 为准（2026-11-26 16:12:26 CST）。这是重置后的第十七轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=588（首搜脚注 remainingToday=587，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。remaining<600 会标 pace/softCap 18，但 remaining≫200，本轮仍跑完全量增量，未砍栏、未缩盲捞。
- mode=pace（未执行砍栏），softCap=18，minSpend=18，silentCap=2。独立查询 26（主扫 25 + silent 1），无写盘失败补拉、无重试。未翻页。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=26，remainingBefore=588，remainingAfter=562。额度 delta=26，与 API 调用次数一致。
- 写盘 meta.xBudgetMode=pace。

各次检索（id / result_count；KW_STARK_24 对引用帖 2125815935869325525 有非致命 include-level Authorization Error，数据仍 n=25 可用，未重试）：
UF1 0，UF2 0，UF3 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 5，MUST_OFF 3，
KW_LZ 0，KW_TAPE 13，KW_GIWA 25（触顶），KW_DOGE 8，KW_BTC 3，KW_STARK 0，
KW_MINT 25（触顶），KW_MINE 5，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 25（触顶），KW_GAPS 6，
MEN_DOGE 1，MEN_BTC 25（触顶），MEN_STARK 3，MEN_PADS 22，
SILENT_DOGE 0，
KW_LZ_24 23，KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 13、GIWA 25 触顶、DOGE 8、BTC 3、STARK 0、MINT 25 触顶、MINE 5、PAD 25 触顶、GO 25 触顶、ELY 25 触顶、GAPS 6。MUST_WIN 24h 25 触顶 + MUST_WIN2 5、MUST_OFF 30m 3。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 1097 @OakAgentKit → 写盘后 cursor 1147 @guppofish，wrap=false，分片末端 @animebigtitty。预跳已知 NF 1 个（@Haltercard），from: 实际 49 个。UF1=0，UF2=0，UF3=0。UF 总账户写盘后 2463（+@tickplus_xyz）。
- mentions 本轮轮换：DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=1，MEN_BTC=25，MEN_STARK=3，MEN_PADS=22）。下轮：GIWA / Tape / LayerZero / Elysium。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_BTC_24（30m=3→24h=25）、KW_STARK_24（30m=0→24h=25）。TAPE 13、GIWA 25、DOGE 8 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY/MINE）改成 24h。
- 静号：SILENT_DOGE，search_users 不可用，24h has:mentions 回退，命中 0。下轮静号：BTC。

## 新收录

- **TickPlus（@tickplus_xyz / https://www.tickplus.cc）**：建号 2026-11-24 10:18:54 CST（约 2.2 天），16 粉 / 4 帖，未认证，xUserId 2125050411828555776。官网 HTTP 200，标题 “TickPlus — Travel Further. Earn More.”，twitter:site 与 schema.org sameAs 均回链 https://x.com/tickplus_xyz，siteXMutual=mutual。官帖 2026-11-26 15:50:24 CST（https://x.com/tickplus_xyz/status/2125859703117041923）仅挂 X 文章 https://x.com/i/article/2125854322663837696，文章页本轮 403，正文未核到。官网 config.js 与资料栏均给出代币 CA 0x1512ee49a4ae4301f4f5789f651c17d195688512，useTestnet=false；机票/酒店 API 基址本轮为空。本轮未在 Robinhood RPC 独立核实该 CA，合约未核实。是产品/工具站预热，**不是发射台，不是免费 mint / 免费登记**。栏：台子/Meme，focus=false，status=watching，dsFallback overall 70。已进 userFollowWatch（未兼挂 agentPad / Elysium / Tape / giwa Watch）。

因真新收录，notify=true。不是免费 mint / 免费登记，告警已点名 TickPlus。另因 QQAI 首次 ≤2h，告警一并点名。

## 看见但未收

- @FamiliarsAI / https://familiars-app.pages.dev/：约 29.8 天、35 粉。本轮关键词再次看见，官网仍写 4,444 已售罄；本轮未见自有官帖。R2231 已因售罄跳过，本轮仍不收录。
- @Oathlydotai：约 0.78 天、22 粉，本轮 0 官帖、无官网，不额外 getUsersPosts，跳过。
- @VardoBot：约 1.45 天，test.vardo.gg，本轮 0 官帖；是 MegaEth 上 Vardo 的机器人号，不收录，未额外搜官方主号。
- 其余 SEO/健身/用户申请帖/旧号噪音（QikLaunch、hyperbodyapp、bobi23ex、officialbunnyos、kembangsinar6）跳过。OutcowlRH、Chainbitz 已在库。

## 库内进度与首次 ≤2h

- **QQAI：自称免费 mint 首次进入 ≤2h**（2026-11-26 18:00 CST，写盘时约 1.8h）。MUST 未见官号 @QQAI_BNB 新帖或改期。后建号站点 https://qqai-bnb.pages.dev/ 与 Token/Mint/Vesting 沿用 R2231，未合并后建号为官号，合约未核实。**仍不是已开铸 LIVE**。须提醒一次。
- Ugly Puggies：免费 mint 仍 LIVE，OpenSea 531/777、持有 338、地板 0.000159 ETH（R2231 为 515/327/0.000159）。阶段沿用 R2227 SIGNED_PRESALE #3 至 2026-11-27 13:30 CST。R2223 已首次 ≤2h。只是进度，不重推。
- The Jacket：214/777、持有 136、地板 0.61 USDG，与 R2231 持平。
- deMiners / Guns Of The Hood / Shielded Wizards / Valorix / Agent Cards：本轮未新拉对应 OpenSea/官网 API，进度沿用 R2231，MUST（Guns）仅表情回复无改期，不重推。
- F0B90B：508/10000（R2231 为 490），mintOpen 仍 True。只是进度（+18）。
- Antopia：6351/8888（R2231 为 6350），免费额度仍满。只是进度（+1）。
- TriForge：本轮公共 BSC RPC（2026-11-26 16:05:05 CST）Forge Keys 873/3333、claims 42、预售 1、挖矿 6（R2231 链上为 869/42/1）。只是进度（Keys +4）。
- 2hour.fun：窗口仍关，/api/window traderCount=43；/api/v1/window 本轮 404。下一窗仍 2026-11-27 05:00–07:00 CST，未到 ≤2h。
- Vicehood 官方合集 vchood 仍 0；首窗 2026-11-27 01:00 CST。
- Wildlife Universe：仍 0，官网仍写 26 Nov 7:00 PM IST（21:30 CST），未到 ≤2h。
- Bonebloom：仍 0，预售仍 2026-11-27 20:30 CST。MUST 再见周五预告，时间表未改。
- Lamoryant：免费登记仍开。本轮再拆 mint 页，仍写 OG Phase 2026-11-26 19:00 CST，0/1356；倒计时全零按 JS 占位，不以开铸 LIVE 计。距开铸约 2.8h，未到首次 ≤2h。
- Crawlers Agent：本轮再拆官网仍为 MINT · OPENING SOON，开铸仍 2026-11-26 20:00 CST（0.004 BNB，仅限 Agent ID）。约 3.8h，未到首次 ≤2h。不是全员免费 mint。
- RuninAI：MUST 再见到每日 20:00 CST 窗口重申；CA 仍 0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6。one-click launchpad 仍未见已 LIVE。约 3.8h，不提前告警、不重推。
- Hamster CombatHQ：MUST 再见 1,111 free mint RH / WL Launching Soon，未见开铸 LIVE。R2226 已通知，不重推。

写盘时即将到来但除 QQAI 外均未进入首次 ≤2h：Lamoryant 约 2.8h（19:00）、Crawlers / RuninAI 约 3.8h（20:00）、Wildlife 约 5.3h（21:30）、Vicehood 约 8.8h（2026-11-27 01:00）（均为 CST）。

## Discord

未打开 computerUse。discordPeekDeferred=true，discordLoginOk=false。登录墙与 R2206 以来相同，不要重发登录表单。须父进程在同一轮补 Peek；若补扫出现免费 mint/登记，再通知。

## notify

notify=true：新收录 TickPlus / @tickplus_xyz（不是免费 mint，但属真新收录，须提醒一次）；QQAI / @QQAI_BNB 自称免费 mint 首次进入 ≤2h（仍不是已开铸 LIVE）。面板 https://reboot7454.github.io/early-scout/

本号不自动 mint。
