# 早期打新雷达 R2225 RESULT

工作目录 /tmp/r2225/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_ELY）、站点/链上核验、写盘并推送面板。DeepSeek API 401（key invalid），判断/文案/打分改为本地兜底，**dsFallback=true**，未用高成本模型批量。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 12:31 CST。写盘 lastScout=2026-11-26 12:44:08 CST。这是重置后的第十轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=771（首搜 UF1 脚注 remainingToday=770，+1 回溯）。todayReset=2026-11-27T00:00:00.000Z。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 24 + silent 1 = 25，低于 softCap，已达 minSpend。未翻页（MUST_WIN / MINT / PAD / GO / MEN_GIWA / KW_*_24 / SILENT_ELY 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=25（main=24，silent=1），remainingBefore=771，remainingAfter=746。额度 delta=25，与检索次数一致。ingest 若只看到 UF1 戳记会误写成 min(stamped)=770，已按末次活脚注 746 校正。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；error=None；多数 remainingToday 仅能从首尾脚注回溯，不逐条捏造中间剩余）：
UF1 1，UF2 0，MUST_WIN 25（触顶未翻页），MUST_OFF 0，
KW_LZ 1，KW_TAPE 19，KW_GIWA 24，KW_DOGE 1，KW_BTC 2，KW_STARK 0，
KW_MINT 25（触顶），KW_MINE 0，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 25（触顶），KW_GAPS 7，
MEN_GIWA 25（触顶未翻页），MEN_TAPE 7，MEN_LZ24 24，MEN_ELY 20，
SILENT_ELY 25（触顶未翻页），
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 1、TAPE 19、GIWA 24、DOGE 1、BTC 2、STARK 0、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 25 触顶、GAPS 7。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 747 @AIZOBsc → 写盘后 cursor 797 @MAOBP_agent，wrap=false，分片末端 @emberlingreal。预跳已知 NF 15 个（@SolumMrkt @BrokeNiggameme @bndoge_bn @Mintbncat_ai @oblaunchpadAll @babycz_ai @mint_WRIT @BinanceCanFly @Meteorszmint @AiPullpad @oblaunchpadbase @bianfenhong @dinomitesnft @Morumai_ @emberlingreal），from: 实际 35 个。UF1 result_count=1（@Peggerdotfun 已在库，官帖称 coded + pegger.fun，非新收录），UF2 result_count=0。UF 总账户写盘后 2456（含本轮新挂的 @Payday_Direct @cookhousememe @elderwoodwiz @CryptoSociety_L）。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25 触顶未翻页，MEN_TAPE=7，MEN_LZ24=24，MEN_ELY=20）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=1→24h=23）、KW_DOGE_24（30m=1→24h=25）、KW_BTC_24（30m=2→24h=25）、KW_STARK_24（30m=0→24h=25）。TAPE 19、GIWA 24 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY）改成 24h。
- 静号：SILENT_ELY，search_users 不可用，24h has:mentions 回退。ran=true，result_count=25 触顶未翻页，sentToReview=1，admitted=1（payday-direct，第三方提及后核官网收录）。未做 getUsers 第二读。下轮静号指向 Tape/电路。

## 新收录

### Elderwood Wizards @elderwoodwiz（id=elderwoodwiz）

- 类别 打新，ecosystem=GIWA，chain=GIWA，**focus=false**（不是仓鼠/toychain）。
- **免费登记 / waitlist 已开**：官网 https://elderwoodwiz.xyz/ HTTPS 200，页面为 Join the Waitlist，需关注旅程、分享 X 帖并登记 EVM 钱包。不是已开铸 LIVE，也未见开铸时间。必须 notify 并点名。
- 建号 2026-07-24 17:46:43 CST（约 124.79 天），2323 粉 / 24 帖，xUserId 2080590410053795840，未认证。
- 官推 bio 写 A story-driven fantasy universe on @GIWA_by_Upbit。官网与官推互链（twitter:site=@elderwoodwiz，siteXMutual=yes），但官网正文未见 GIWA 字样。本轮无自有官帖，线索来自 MEN_GIWA / KW_GIWA 社区名单。
- dsFallback score overall=56（early=48，actionable=72，novelty=58，risk=65）。已挂 userFollowWatch + giwaWatch + freeMintWatch。

### Payday @Payday_Direct（id=payday-direct）

- 类别 台子/Meme，ecosystem=Elysium，chain=Elysium / Solana / pump.fun，focus=false，不是免费 mint/登记。
- 建号 2026-11-09 01:52:38 CST（约 17.45 天），784 粉 / 173 帖，xUserId 2119487548040806400。
- 官网 https://payday.direct HTTPS 200，自称把 pump.fun / Montra 创作者费用打到 X Money；Explore 已列出多枚 Montra 币，并有 /elysium/c/<合约> 路径，说明 Elysium/Montra 侧已上线，不是 Exploring，故进 Elysium 栏。
- 官推资料栏指向官网，官网未回链 @Payday_Direct（siteXMutual=partial-x-to-site）。bio Official CA uHMWNFjUNxbPy1q43WrdbzygmJwdeh6AiQm1NKdxPAY 与 Pump verification，本轮未上链独立复核。本轮无自有官帖，线索来自 SILENT_ELY 第三方提及。
- dsFallback score overall=70（early=70，actionable=80，novelty=75，risk=75）。已挂 userFollowWatch + elysiumWatch。

### CookHouse @cookhousememe（id=cookhousememe）

- 类别 GIWA，ecosystem=GIWA，focus=false，不是免费 mint/登记，也不是已开盘 LIVE。
- 建号 2026-07-16 10:30:14 CST（约 133.09 天），2719 粉 / 仅 11 帖，xUserId 2077580823675420672。
- 官网 https://www.cookhouse.meme HTTPS 200，与官推互链（twitter:site=@cookhousememe，siteXMutual=yes）。页面称 Quest board is live、Launching/trading/bridging land at open、Networks revealed at launch。官推 bio 写 Launchpad on @GIWA_by_Upbit，官网正文未见 GIWA 字样。本轮无自有官帖，线索来自 MEN_GIWA / KW_GIWA。
- dsFallback score overall=54（early=45，actionable=55，novelty=60，risk=70）。已挂 userFollowWatch + giwaWatch。

### MIT (Crypto Ledger Society) @CryptoSociety_L（id=cryptosociety-l）

- 类别 台子/Meme，ecosystem=Robinhood Chain，focus=false，不是免费 mint/登记。
- 建号 2026-10-28 01:38:36 CST（约 29.46 天），187 粉 / 73 帖，xUserId 2115135508187926528。
- 官网 https://cryptoledgersociety.com HTTPS 200，回链 @CryptoSociety_L（siteXMutual=yes）。站点称 $MIT 提供交易信号与 Bybit/Lighter AutoTrade，钱包追踪、合约审计、锁仓和发射台写 coming next。bio 写 Project is made by @Adityaedwinb。发射台尚未上线。线索来自 KW_LZ_24。
- dsFallback score overall=54（early=65，actionable=50，novelty=55，risk=75）。已挂 userFollowWatch。

## 看见但未收

- **Kimchifunxyz @Kimchifunxyz**：出现在 GIWA 名单，kimchifun.xyz 本轮 TLS unexpected EOF / HTTP 500，无自有官帖，证据不足 skip。未另开 getUsers。
- **ODYbtc @ODYbtc**：pump 类 meme 喊单，非本雷达目标。
- **yeriyaps @yeriyaps**：评论员/转述号，非项目方。
- **ElysiumHubHB @ElysiumHubHB**：Elysium 资讯复盘号，非新项目。
- **MythicMint_NFT @MythicMint_NFT**：无官网、无自有开铸官帖，仅写 something is coming，继续 defer。
- 另有 violetblocks（2012 抽奖喊单号）、morfimarkets（约 222 天成熟盘）、DogeFeedApp、wukonglegendz 等过滤。GIWA 名单中仅有 handle、includes 无 user 对象的 Deoksangi / Loopy_GIWA / Gaejuki_Giwa / GIWA_Accordpay / OsigeExchange / Hanok_io / kaachi_io 未另开 getUsers。

## 首次 ≤2h / 库内刷新（不另作改期）

- **Ugly Puggies @uglypuggies**：仍 MINTING，OpenSea 315/777（R2224 为 314），持有 238（R2224 为 237），地板 0.000169 ETH（与 R2224 持平）。SIGNED_PRESALE #2 仍至 2026-11-26 13:30:00 CST，写盘时约 0.76h，**首次 ≤2h 已在 R2223 提醒，本轮不重推**。SeaDrop HTML 本轮解析失败，供应取 OpenSea API。本号不自动 mint。
- Shielded Wizards：本轮未重拉 brimhollow API。MUST_WIN 见公售仍开的既有口径，R2210 已通知，不重推。
- Antopia：链上 6344/8888（与 R2224 持平），saleOpen=true，免费额度仍满 4000/4000。付费窗仍至 2026-11-27 20:45 CST，未到 ≤2h，不重推。
- F0B90B：仍 mintOpen=true，463/10000（R2224 为 462），只是进度，不重推。
- The Jacket：仍 214/777，持有 136，地板 0.61 USDG，与 R2224 持平。
- deMiners：仍 1373/3333，持有 181，地板约 0.000107 ETH，与 R2224 持平。
- Wildlife / tiger-universe：合集 API 本轮 200、供应仍 0，stats 仍 0 持有。SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起，距首窗约 8.8h，未到首次 ≤2h。
- Vicehood / vchood：官方合集仍 0/3333、MINTING_SOON。首窗仍 2026-11-27 01:00 CST（约 12.3h），未到首次 ≤2h。同名合集 vicehood 仍约 209、不是该官号，未混淆。
- 2hour.fun：MUST_WIN 再见第一场已关、第二窗仍 2026-11-27 05:00–07:00 CST（约 16.3h）的既有口径，未见改期，不重推。
- TRIFORGE / VALORIX / Agent Cards / Guns Of The Hood / Bonebloom / Crawlers Agent / HOLD / kaling-war：本轮未重拉对应站点/RPC，时间表未见新官宣改期，不重推。Crawlers 开铸仍预告 20:00 CST（约 7.3h），未到首次 ≤2h。kaling-war 免费开包已在 R2224 提醒。

## Watch / 漏挂

- 新卡均同时进 Watch（见上）。近期（round≥2100）Watch 漏挂检查 0，无需补挂。
- 软债 lastChecked 已刷新（含 canton/glaze/tokenWorks 与各必盯 Watch）。

## notify

- notify=true。原因：四项真新收录，其中 **Elderwood Wizards 为免费 waitlist/登记，告警必须点名**。Payday / CookHouse / MIT 不是免费 mint。Ugly Puggies 仍在已提醒过的首次 ≤2h 窗内，不重推。
- namedFreeMintOrRegistration=['elderwoodwiz']。namedPaidLe2h=[]。
- 面板 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。

## Discord

discordPeekDeferred=true。X 路径未打开 Discord/浏览器，只写占位。登录墙与 R2206/R2223/R2224 相同（Welcome back / Email/Password / Log In / QR / passkey），loginOk=false，四频道 lastSeen/cutoff 仍停在 2026-11-23 22:19–22:56 CST。用户此前已被告知用已有表单再登。同一未登录会话无法翻过登录墙，本轮不重复开浏览器、不重发登录表单。须父代理在同一轮补 Peek；补扫若出现免费 mint/登记再通知。
