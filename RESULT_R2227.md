# 早期打新雷达 R2227 RESULT

工作目录 /tmp/r2227/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_GIWA）、站点/链上核验、写盘并推送面板。本轮无新收录短名单，未调用 DeepSeek，dsFallback=false（不是 API 失败兜底）。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 13:30 CST。写盘 lastScout=2026-11-26 13:44:55 CST。这是重置后的第十二轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=721（首搜 UF1 脚注 remainingToday=720，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 24 + silent 1 = 25，低于 softCap，已达 minSpend。MUST_WIN 因 24h 句柄列表过长拆成 2 次检索（仍计入主计划，未超 softCap）。未翻页（MUST_WIN / MINT / PAD / GO / TAPE / MEN_GIWA / SILENT_GIWA / KW_*_24 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=25（main=24，silent=1），remainingBefore=721，remainingAfter=696。额度 delta=25，与检索次数一致。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；KW_STARK_24 对引用帖 2125815935869325525 有非致命 include-level Authorization Error，数据仍 n=25；其余 error=None；中间 remainingToday 未逐条落盘，不捏造）：
UF1 0，UF2 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 2，MUST_OFF 0，
KW_LZ 1，KW_TAPE 25（触顶），KW_GIWA 18，KW_DOGE 6，KW_BTC 2，KW_STARK 2，
KW_MINT 25（触顶），KW_MINE 0，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 22，KW_GAPS 14，
MEN_GIWA 25（触顶），MEN_TAPE 7，MEN_LZ24 23，MEN_ELY 21，
SILENT_GIWA 25（触顶），
KW_LZ_24 23，KW_BTC_24 25（触顶），KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 1、TAPE 25 触顶、GIWA 18、DOGE 6、BTC 2、STARK 2、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 22、GAPS 14。MUST_WIN 24h 25 触顶 + MUST_WIN2 2、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 847 @agentbond_fun → 写盘后 cursor 897 @toshidotfun，wrap=false，分片末端 @EthereaGenesis。预跳已知 NF 11 个（@SENSEIAgent_ @Agentspunks @cryptosympbnb @BN_Big_Bang @LumenGenesisNFT @Estock_ @pixelboyzai @Panba_EmojiPack @AmberPoW_BSC @DigitalBombAI @ditherglyphs），from: 实际 39 个。UF1/UF2 result_count=0。@Wildlifeuni_55 落在本轮 UF 分片内，按同号只拉一次规则未再进 MUST_WIN 24h。UF 总账户写盘后仍 2457。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25，MEN_TAPE=7，MEN_LZ24=23，MEN_ELY=21）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=1→24h=23）、KW_BTC_24（30m=2→24h=25）、KW_STARK_24（30m=2→24h=25）。TAPE 25、GIWA 18、DOGE 6 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY）改成 24h。
- 静号：SILENT_GIWA，search_users 不可用，24h has:mentions 回退。ran=true，result_count=25 触顶，sentToReview=0，admitted=0。未做 getUsers 第二读。下轮静号指向 DogeEVM。

## 新收录

无。

## 看见但未收

- **Kimchifunxyz @Kimchifunxyz**：GIWA 发射台自称（资料栏 Launch coins on Giwa via kimchifun.xyz）。建号 2026-09-19（约 68 天），268 粉 / 8 帖。仅第三方 @yeriyaps GIWA 生态盘点提到，本轮无自有官帖。官网 http://kimchifun.xyz 本轮 HTTP 500，https SSL 失败，未能核到可访问页面。看见但未收。未另开 getUsers / getUsersPosts。
- **GiwaPump @GiwaPump**：GIWA Sepolia 测试网 Liquid NFT launchpad。建号 2026-07-29（约 120 天），758 粉 / 6 帖。官网 https://giwapump.xyz 本轮 200，与 @giwapump 互证。中龄 + 测试网，本轮无新开铸官宣，看见但未收。未另开 getUsers。
- **QikLaunch @QikLaunch**：非加密 SaaS，继续跳过。
- **ShieldSuite_ @ShieldSuite_**：2026-04 建号的 X Layer 工作室，中老龄，本轮无极早期开铸信号。
- **ElysiumHubHB @ElysiumHubHB**：Elysium 聚合转载号，非项目本体。
- **MythicMint_NFT @MythicMint_NFT**：无官网、无自有开铸官帖，仅有 giveaway 闲聊，继续 defer。

## 首次 ≤2h / 库内刷新（不另作改期）

- **Ugly Puggies @uglypuggies**：SeaDrop 仍为 MINTING，activeDropStage 已切到 SIGNED_PRESALE #3（2026-11-26 13:30–2026-11-27 13:30 CST）。#2 已按点于 13:30 CST 结束。PUBLIC_SALE 仍是 2026-11-27 13:30–2026-11-29 13:30 CST，时间表未改。供应 SeaDrop 459/777（OpenSea collection API 为 458，R2226 为 317），持有 300（HTML stats；API stats 为 297，R2226 为 240），地板 0.000169 ETH（与 R2226 持平）。官回 2026-11-26 13:04 CST（https://x.com/uglypuggies/status/2125817933880533323）称 mint 比预期慢但是有意的、GTD 有一整天，不是改期。**首次 ≤2h 已在 R2223 提醒，本轮阶段切换与供应上涨只是进度，不重推。** 距 #3 结束约 23.8h，未到新的首次 ≤2h。本号不自动 mint。
- **RuninAI @RuninAI_com**：MUST_WIN 再见到官帖重申每日 20:00 CST $RMINE 窗口（已在 R2226 记下）。CA 仍为 `0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6`。距今日窗约 6.3h，未到首次 ≤2h，不重推。
- **Crawlers Agent @CrawlersAgent**：付费开铸仍预告 2026-11-26 20:00 CST（0.004 BNB，6000 份，仅限 Agent ID）。MUST_WIN 再见 12:41 / 12:07 CST 官帖，时间表未改；自称合约仍是 `0x5c92D8b2aa748722D7855CD4493F208f66757fd6`，本轮未独立上链核实。距开铸约 6.3h，未到首次 ≤2h，不提前告警、不重推。不是面向全员的免费 mint。
- **QQAI @QQAI_BNB**：自称免费席仍约 2026-11-26 18:00 CST。本轮 MUST 未见新官帖。距开铸约 4.3h，未到首次 ≤2h，不是已开铸 LIVE。未见 CA。不提前告警、不重推。
- **Lamoryant @Lamoryant**：免费登记/查资格仍开（官网与 /apply 本轮 200，文案仍是 Free mint · 1,356 supply），不是已开铸 LIVE。开铸仍约 2026-11-26 19:00 CST。距开铸约 5.3h，未到首次 ≤2h，不重推。
- **Shielded Wizards @ShieldedWizBTC**：免费公售仍 LIVE。brimhollow API phase=public，minted=145/3333（R2226 为 144），reserved=2，mintOpen=true，price=0。R2210 已首次确认并通知，本轮只是进度，不重推。
- Antopia：链上 6350/8888（R2226 为 6345），saleOpen=true，免费额度仍满 4000/4000。付费窗仍至 2026-11-27 20:45 CST，未到 ≤2h，不重推。
- F0B90B：仍 mintOpen=true，469/10000（R2226 为 468），只是进度，不重推。
- The Jacket：仍 214/777，持有 136，地板 0.61 USDG，与 R2226 持平。持有人名单免费 mint 仍 LIVE；公售仍 0.0003 ETH。
- deMiners：付费公售仍 LIVE，1373/3333，持有 181，地板 0.000107 ETH，与 R2226 持平。PUBLIC_SALE 至 2026-11-27 16:30:04 CST。
- Guns Of The Hood：付费公售仍 LIVE。OpenSea collection API / SeaDrop 仍 111/10000（与 R2226 持平）。本轮 stats API 401，持有/地板未独立核到新值。R2210 已通知，不重推。不是免费 mint。
- Wildlife / tiger-universe：SeaDrop 仍 MINTING_SOON，0/5555，activeDropStage=null。时间表未改：SIGNED_PRESALE 自 2026-11-26 21:30 CST 起，PUBLIC_SALE 2026-11-27 02:29 CST 起。距首窗约 7.8h，未到首次 ≤2h。本号本轮在 UF 分片内（30m 窗），未见新官帖。
- Vicehood / vchood：官方合集仍 0/3333、MINTING_SOON。首窗仍 2026-11-27 01:00 CST（约 11.3h），未到首次 ≤2h。同名合集 vicehood 不是该官号，未混淆。
- Bonebloom：SeaDrop 仍 MINTING_SOON，0/555，持有 0。SIGNED_PRESALE 仍 2026-11-27 20:30 CST，距首窗约 30.8h，未到首次 ≤2h。
- 2hour.fun：第一场窗口仍关闭。官网 RSC payload 明确 open=false；SSR 仍可能显示 Window open + 00:00:00 占位，不以该标签为准。/api/window traderCount=43（R2226 面板记录 37）。下一窗仍为 2026-11-27 05:00–07:00 CST（约 15.3h），无改期，不重推。
- Hamster CombatHQ：MUST_WIN2 再见到昨日「WL Launching Soon / 征集 EVM 地址」官帖及 Collabs are OPEN，仍不是已开铸 LIVE 或独立免费登记页。R2226 已收录并通知，不重推。
- kaling-war 免费开包已在 R2224 提醒，本轮无新状态，不重推。

## Watch / 漏挂

- 本轮无新卡。近期（round≥2100）Watch 漏挂检查 0，无需补挂。
- 软债 lastChecked 已刷新（含 canton/glaze/tokenWorks 与各必盯 Watch）。

## notify

- notify=false。原因：无真新收录，无新的首次 ≤2h，无新的免费 LIVE / 免费 mint / 免费登记，推送若成功则不告警。Ugly Puggies 阶段切换与供应上涨、以及仍 LIVE 的 Shielded Wizards / The Jacket / F0B90B 等只是进度，此前已通知，不重推。即将到来的窗口（QQAI 约 18:00、Lamoryant 约 19:00、Crawlers/RuninAI 20:00、Wildlife 21:30）均未到首次 ≤2h。
- namedFreeMintOrRegistration=[]。namedPaidLe2h=[]。
- 面板 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。

## Discord

discordPeekDeferred=true。X 路径未打开 Discord/浏览器，只写占位。登录墙与 R2206/R2223/R2224/R2225/R2226 相同（Welcome back / Email/Password / Log In / QR / passkey），loginOk=false，四频道 lastSeen/cutoff 仍停在 2026-11-23 22:19–22:56 CST。用户此前已被告知用已有表单再登。同一未登录会话无法翻过登录墙，本轮不重复开浏览器、不重发登录表单。须父代理在同一轮补 Peek；补扫若出现免费 mint/登记再通知。
