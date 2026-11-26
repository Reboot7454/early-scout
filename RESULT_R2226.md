# 早期打新雷达 R2226 RESULT

工作目录 /tmp/r2226/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_TAPE）、站点/链上核验、写盘并推送面板。DeepSeek API 401（key invalid），判断/文案/打分改为本地兜底，**dsFallback=true**，未用高成本模型批量。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 12:57 CST。写盘 lastScout=2026-11-26 13:10:19 CST。这是重置后的第十一轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=746（首搜 UF1 脚注 remainingToday=745，+1 回溯）。todayReset=2026-11-27T00:00:00.000Z（约 2026-11-27 08:00 CST）。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 24 + silent 1 = 25，低于 softCap，已达 minSpend。未翻页（MUST_WIN / MINT / PAD / GO / ELY / KW_*_24 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=25（main=24，silent=1），remainingBefore=746，remainingAfter=721。额度 delta=25，与检索次数一致。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；error=None；中间 remainingToday 未逐条落盘，不捏造）：
UF1 2，UF2 0，MUST_WIN 25（触顶未翻页），MUST_OFF 0，
KW_LZ 0，KW_TAPE 14，KW_GIWA 10，KW_DOGE 2，KW_BTC 0，KW_STARK 1，
KW_MINT 25（触顶），KW_MINE 0，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 25（触顶），KW_GAPS 11，
MEN_DOGE 3，MEN_BTC 24，MEN_STARK 2，MEN_PADS 18，
SILENT_TAPE 1，
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 14、GIWA 10、DOGE 2、BTC 0、STARK 1、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 25 触顶、GAPS 11。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 797 @MAOBP_agent → 写盘后 cursor 847 @agentbond_fun，wrap=false，分片末端 @WraithScout。预跳已知 NF 12 个（@TrineProtocol @LongAgentBNB @dotaipad @btcliu205 @Sambario_bnb @KDAgentAI @Gweiwbbb @PlayTycoonCity @PunksOnDrugs @baoracletrade @agentplacewall @LastCall4vx），from: 实际 38 个。UF1 result_count=2（@RuninAI_com 已在库，见下方刷新），UF2 result_count=0。UF 总账户写盘后 2457（含本轮新挂的 @HamsteCombatHQ）。
- mentions 本轮轮换：DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=3，MEN_BTC=24，MEN_STARK=2，MEN_PADS=18）。下轮：GIWA / Tape / LayerZero / Elysium。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_DOGE_24（30m=2→24h=25）、KW_BTC_24（30m=0→24h=25）、KW_STARK_24（30m=1→24h=25）。TAPE 14、GIWA 10 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY）改成 24h。
- 静号：SILENT_TAPE，search_users 不可用，24h has:mentions 回退。ran=true，result_count=1，sentToReview=0，admitted=0。未做 getUsers 第二读。下轮静号指向 GIWA。

## 新收录

### Hamster CombatHQ @HamsteCombatHQ（id=hamste-combathq）

- 类别 打新，ecosystem=Robinhood Chain，chain=Robinhood，**focus=false**（仓鼠 PFP，但不是 squeekchain / 实体 PoW toychain）。
- 建号 2026-11-20 02:34:18 CST（约 6.44 天），43 粉 / 3 帖，xUserId 2123484663654014976，未认证。
- 官帖 2026-11-26 03:40:21 CST（https://x.com/HamsteCombatHQ/status/2125675982266978598）自称 1,111 Unique Hamsters、Free Mint、Robinhood Chain、EVM Compatible、WL Launching Soon、GTD for Early Supporters，并在评论区征集 EVM 地址（Like + RT）。
- **不是已开铸 LIVE，也不是已确认的独立免费登记页**（无官网申请表，只是官帖下留地址）。告警须写清这一点，禁止写成「免费登记已开」或「免费 mint LIVE」。
- 无独立官网，资料栏只有 Telegram https://t.me/hamster_combat_nfthub。未见合约。线索来自 KW_MINT 第三方转帖，includes 中核到自有官帖。未另开 getUsers。
- dsFallback score overall=55（early=82，actionable=50，novelty=42，risk=72）。已挂 userFollowWatch + freeMintWatch。

## 看见但未收

- **VardoBot @VardoBot**：MegaEth 测试机器人（test.vardo.gg），1 粉，非打新目标。
- **QikLaunch @QikLaunch**：非加密 SaaS，跳过。
- **mIRCsg @mIRCsg**：mIRC 官方号谈 USDY/OFT，非新项目。
- **MythicMint_NFT @MythicMint_NFT**：无官网、无自有开铸官帖，仅有 giveaway 闲聊，继续 defer。
- 另有 Oraxelxyz、HoodLockRH、bridgechains、KaleidoFi 等建号约 100–140 天、本轮无强官宣新开铸的中龄号，未按极早期新号收录。未另开 getUsers。

## 首次 ≤2h / 库内刷新（不另作改期）

- **Ugly Puggies @uglypuggies**：仍见 OpenSea 317/777（R2225 为 315），持有 240（R2225 为 238），地板 0.000169 ETH（与 R2225 持平）。SIGNED_PRESALE #2 仍至 2026-11-26 13:30:00 CST，写盘时约 0.33h，**首次 ≤2h 已在 R2223 提醒，本轮不重推**。官帖 2026-11-26 10:02:13 CST（https://x.com/uglypuggies/status/2125772081011040521）致歉称 mint 未达预期、WL 漏加、信息不透明，仍在建设，不视为改期。SeaDrop HTML 本轮解析失败，供应取 OpenSea API。本号不自动 mint。
- **RuninAI @RuninAI_com**：官帖 2026-11-26 12:47:38 CST（https://x.com/RuninAI_com/status/2125813709276934470）补上每日开窗钟点：`$RMINE` 自称 Agent ID + PoW、daily window at 20:00 CST、miners pay only gas。CA 仍为 `0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6`。距今日窗约 6.8h，未到首次 ≤2h，不重推。此前 R2088 仍写无开窗钟点。
- **Crawlers Agent @CrawlersAgent**：付费开铸仍预告 2026-11-26 20:00 CST（0.004 BNB，6000 份，仅限 Agent ID）。官帖 12:41:20 CST（https://x.com/CrawlersAgent/status/2125812121338630410）自称合约 `0x5c92D8b2aa748722D7855CD4493F208f66757fd6`（此前写合约尚未部署），本轮未独立上链核实。距开铸约 6.8h，未到首次 ≤2h，不提前告警、不重推。不是面向全员的免费 mint。
- **Shielded Wizards @ShieldedWizBTC**：免费公售仍 LIVE。brimhollow API phase=public，minted=144/3333（R2223 为 138），reserved=3，mintOpen=true，price=0。官帖 2026-11-26 08:40:34 CST（https://x.com/ShieldedWizBTC/status/2125751533933416762）称计划明天加 staking 和 Voting tab，公售仍开。R2210 已首次确认并通知，本轮只是进度，不重推。
- Antopia：链上 6345/8888（R2225 为 6344），saleOpen=true，免费额度仍满 4000/4000。付费窗仍至 2026-11-27 20:45 CST，未到 ≤2h，不重推。
- F0B90B：仍 mintOpen=true，468/10000（R2225 为 463），只是进度，不重推。
- The Jacket：仍 214/777，持有 136，地板 0.61 USDG，与 R2225 持平。
- deMiners：仍 1373/3333，持有 181，地板约 0.000107 ETH，与 R2225 持平。
- Guns Of The Hood：付费公售仍 LIVE。OpenSea 111/10000（R2223 为 100），持有 16（R2223 为 14），地板 0。R2210 已通知，只是进度，不重推。不是免费 mint。
- Wildlife / tiger-universe：合集 API 供应仍 0，stats 仍 0 持有。SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起，距首窗约 8.3h，未到首次 ≤2h。
- Vicehood / vchood：官方合集仍 0/3333、MINTING_SOON。首窗仍 2026-11-27 01:00 CST（约 11.8h），未到首次 ≤2h。同名合集 vicehood 仍约 209、不是该官号，未混淆。
- Bonebloom：OpenSea API 仍 0/555，持有 0。SIGNED_PRESALE 仍 2026-11-27 20:30 CST，距首窗约 31.3h，未到首次 ≤2h。SeaDrop HTML 本轮解析失败。
- Slime：OpenSea API 供应仍 0，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- 2hour.fun：第一场窗口仍按已关闭处理。/api/window 本轮 traderCount=42（此前记录 37），不是改期。下一窗仍为 2026-11-27 05:00–07:00 CST（约 15.8h），关窗与发币费改免费此前已通知，不重推。
- TRIFORGE / VALORIX / Agent Cards / HOLD / kaling-war / QQAI / Lamoryant / MMIX：本轮未重拉对应站点/RPC，时间表未见新官宣改期，不重推。QQAI 自称免费席约 18:00 CST、Lamoryant 约 19:00 CST，均未到首次 ≤2h。kaling-war 免费开包已在 R2224 提醒。

## Watch / 漏挂

- 新卡同时进 Watch：hamste-combathq → userFollowWatch + freeMintWatch。近期（round≥2100）Watch 漏挂检查 0，无需补挂。
- 软债 lastChecked 已刷新（含 canton/glaze/tokenWorks 与各必盯 Watch）。

## notify

- notify=true。原因：一项真新收录 Hamster CombatHQ。**不是免费 mint LIVE，也不是已确认的免费登记页**，告警必须写清「WL即将开放 / 评论区征集地址」，禁止写成已开铸或免费登记已开。Ugly Puggies 仍在已提醒过的首次 ≤2h 窗内（约 0.33h），不重推。RuninAI 补钟点与 Crawlers 自称合约均未到首次 ≤2h，不另告警。
- namedFreeMintOrRegistration=[]。namedPaidLe2h=[]。
- 面板 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。

## Discord

discordPeekDeferred=true。X 路径未打开 Discord/浏览器，只写占位。登录墙与 R2206/R2223/R2224/R2225 相同（Welcome back / Email/Password / Log In / QR / passkey），loginOk=false，四频道 lastSeen/cutoff 仍停在 2026-11-23 22:19–22:56 CST。用户此前已被告知用已有表单再登。同一未登录会话无法翻过登录墙，本轮不重复开浏览器、不重发登录表单。须父代理在同一轮补 Peek；补扫若出现免费 mint/登记再通知。
