# R2205 X-radar RESULT

- Round: **R2205**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-26 02:48:50 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170（保持，未改）
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2205/RESULT_R2205.md`、`/tmp/r2205/notify.json`、`/tmp/r2205/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2205/apply_r2205.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2205/data.json.src APPLY_DRY_OUT=/tmp/r2205/data.json` 已成功）

## X 预算与检索

- **remainingBefore=102/1000**（首搜 UF1 后脚注 remainingToday=101，故开火前为 102；预期 104，落在 tight ±20 内，按已排 13 次照跑，未再加搜。）
- **remainingAfter=89/1000**
- **xReads=13**（main 12 + silent 1；按已排 queries.json 13 次照跑，无计划外搜索，未补 MUST_OFF，未做薄栏 24h）
- **十栏覆盖：** 六个薄栏独立 30m KW（LZ / TAPE / GIWA / DOGE / BTC / STARK）+ 核心栏与 GAPS 合并为一次 KW_CORE（30m）。MUST_OFF 本轮 tight 已跳过（官号 30m 延期），未补跑（live remainingBefore=102，未达 ≥250 阈值）。
- **mode=tight** / softCap=10 / minSpend=10 / silentCap=1。已写入 `meta.xBudgetMode=tight`。计划 13 次略高于 softCap 10，按已排 queries.json 照跑，未 override-full，未再加计划外搜索。
- 未对已知 NF `@starx_xlayer` 做 from: 重试。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 0 | 101 |
| UF2 | 30m | 0 | 100 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 99 |
| KW_LZ | 30m | 1（有 next_token，未翻页） | 98 |
| KW_TAPE | 30m | 6（有 next_token，未翻页） | 97 |
| KW_GIWA | 30m | 25（触顶，有 next_token，未翻页） | 96 |
| KW_DOGE | 30m | 17（有 next_token，未翻页） | 95 |
| KW_BTC | 30m | 4（有 next_token，未翻页） | 94 |
| KW_STARK | 30m | 2（有 next_token，未翻页） | 93 |
| KW_CORE | 30m | 25（触顶，有 next_token，未翻页） | 92 |
| MEN_DOGE | 24h | 6（有 next_token，未翻页） | 91 |
| MEN_BTC | 24h | 25（触顶，有 next_token，未翻页） | 90 |
| SILENT_ELY | 24h | 25（触顶，有 next_token，未翻页） | 89 |

（KW_STARK 与 KW_CORE 之间发生分钟重置，remMin 21→29，今日额度仍按 93→92 连续扣减。）

## UF 分片 / 光标

- 本轮分片：cursor **2261 @stalliononeth** 起 40 个到 **@scotydotfun**，两次 from:（UF1 23 + UF2 17），wrap=false
- UF1：0 帖
- UF2：0 帖
- 无新官号窗口
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2301 @antebellrh**，uf_total 2430（新挂 @yoricolors 在名单末尾，cursor 指向不变），wrap=false

## Mentions 与静号

- **本轮 mentions：** DogeEVM（MEN_DOGE 6）/ BTC（MEN_BTC 25）
- **下轮 mentions 轮转：** Starknet / squeek / STARX（先补完本轮轮转剩余，再回到 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest）
- **本轮静号：** Elysium（2205 % 11 = 5；SILENT_ELY 25 条，触顶未翻页）
- **下轮静号：** Tape/电路
- **silentAccounts：** ran=true，seen=25，sentToReview=0，admitted=0，skipped=0。search_users 仍不可用，用 mentionQuery 兜底。25 条多为已在库 Elysium 发射/机器人讨论（如 @Hypesium），未见可核验的新官号窗口。本轮新收录 YORI 来自 KW_CORE，不是静号栏。

## 薄栏 24h 回看

- 30m 命中：KW_LZ=1、KW_BTC=4、KW_STARK=2，均 <5；KW_TAPE=6、KW_GIWA=25、KW_DOGE=17，均 ≥5
- 主计划跑完后 remainingToday=89，**低于**大致 ≥150 的门槛，**未做**薄栏 24h 补搜
- **没做：** KW_LZ_24（30m 为 1 且优先）、KW_BTC_24、KW_STARK_24。KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（尤其 KW_CORE）改成 24h。未为 24h 补搜翻页。

## 新收录（DeepSeek 打分，dsFallback=false）

`meta.round2205Added` = 顶层 `newThisRound` = `['yoricolors']`。该卡 focus=false，已同时挂 userFollowWatch + freeMintWatch。links 写了 `x` 与 `twitter`。

- **YORI @yoricolors / https://yoricolors.xyz/**（打新，score=74）：建号 2026-11-06 01:10:27 CST（约 20.1 天），668 粉 / 仅 1 帖，资料栏无网址，bio 写 More than colors on @Aptos。本轮未见该号自己出现在搜索主结果（未做 from: 重读）。KW_CORE 30m 见第三方抽奖转发（https://x.com/Christianftud/status/2125660159968194810）：20 GTD for @yoricolors，3,333 • Free mint • Aptos。官网 https://yoricolors.xyz/（HTTP 200，跳转 https://www.yoricolors.xyz/）标题 YORI | More Than Colors，页内链 https://x.com/yoricolors（与官号互证），脚本 CFG.account=yoricolors。站点是白名单申请页：Apply for WL（follow/like/rt/qt/cm + 提交 Aptos 钱包），另有 Claim WL 转盘（GTD/FCFS/$YORI/积分）、Checker、Leaderboard，页脚 Built on Aptos。公开 /api 配置 404，需登录才可看申请状态。铸造日期官网未见，第三方 Tessera 抽奖文案写 date remains TBA、Price FREE MINT、supply 3333。不是已确认免费 mint LIVE，但是已核到的官方免费登记/WL 申请窗口。DeepSeek admit + score（overall=74，admit=true）。本号不自动 mint。

## 看见但未收录

- **GIWAPUNK @giwapunk / https://giwapunk.xyz**：本轮 KW_GIWA 仍见该号（建号约 109 天，1171 粉 / 46 帖，bio 仍写 4,450 Free mint、Coming soon）。R2204 已初筛后因 overall=44 且 admit=false（名单已定、主网未上、早期度下降）不入库。本轮未见新的主网上线或开铸证据，不重收。
- **@2hourfunEco**：2hour.fun 生态号，官网指向已在库的 2hour.fun，不新建卡。
- **@ElysiumHubHB**：Elysium 日更综述号，不是铸造窗口，不入库。
- **已在库项目的转发/复述：** @beavzclub（First 150 Free mint / Drop EVM wallet，R2196 已记，仍无官网/CA，不重推）、@Chainbitz、@RebelianRH、@Owltopia_sol、@MMIX_io、@Riftidegame、@OUTLAWSxNFT、@UnicornGPrix、@Vicehood_RH、@Wildlifeuni_55、@Wolfy_Syndicate、@Hypesium 等，不新建卡。
- **@Zara_Quinnx**：KOL 给已在库 @Chainbitz 做 20GTD 抽奖，不是新官号。
- **OpenSea 合集 vicehood（username PlayVicehood）**：已在公售、209/3333，与官方 @Vicehood_RH 合集 **vchood** 不是同一个，不要混淆。未新建卡。

## 必须通知的 ≤2h / 库内刷新

- **Ugly Puggies @uglypuggies**：免费 mint 仍 LIVE。SeaDrop mintStatus=MINTING，260/777（R2204 为 253/777；公开 API total_supply=259），持有 195（R2204 为 190），地板 0.000169 ETH（与 R2204 相同）。时间表未变：activeDropStage 仍是 stageIndex=2 SIGNED_PRESALE，至 2026-11-26 13:30 CST；stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 仍要到 2026-11-27 13:30 CST。本轮 MUST 未见 @uglypuggies 新官帖。只是仍 LIVE 与小幅进度，不重推。
- **deMiners @deMinersNft**：付费公售仍按原时间表进行。SeaDrop mintStatus=MINTING，activeDropStage stageIndex=0 PUBLIC_SALE，572/3333（R2204 为 568/3333），持有 152（R2204 为 150），地板 0.0001 ETH（二级地板）。铸造价沿用已核验 0.0002 ETH，未见改价。时间表未改：PUBLIC_SALE 仍是 2026-11-26 00:30:04 CST–2026-11-28 00:30:04 CST。MUST 24h 只见 01:14 CST 教人用钱包的短回复，无改期/改价/取消。R2197 已发付费公售首次 ≤2h，R2201 已核到公售按点开出。只是小幅进度，不重推。
- **Agent Cards @agentcardshq**：官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=5427/1,007,493，现价约 0.00198 BNB，与 R2204 持平。MUST 24h 再见回购/纠偏续帖（含 00:38 CST「We got the AGENTMINT launch wrong」），是开盘后说明，不是新的铸造规则或免费窗口。不是免费 mint。只刷新，不重推。
- **Slime @Slime_agents**：OpenSea 仍 total_supply=0、持有 0。SeaDrop 仍 mintStatus=MINTING_SOON，555 份，activeDropStage=null。SIGNED_PRESALE 仍 2026-11-29 00:00 CST 起，PUBLIC_SALE 仍 2026-11-30 01:00 CST 起。不是已开铸 LIVE。R2204 刚收录并已通知，无实质变化，不重推。
- **The Jacket**：OpenSea 仍 213/777，持有 135，公售阶段未变。无实质变化，不重推。
- **TRIFORGE**：链上 Forge Keys 750/3333（R2204 为 728/3333），claims 31，付费预售与挖矿仍开。MUST 再见 01:32 CST 官帖，规则未变。只是小幅进度，不重推。
- **F0B90B**：链上 mintOpen=true，418/10000（R2204 为 406/10000）。无新官帖。小幅进度，不重推。
- **Antopia**：链上仍 6253/8888，saleOpen=true，freeRemaining=0。无新官帖，不重推。
- **VALORIX**：Hero Cards 仍 12，fillSold 仍 0。无实质变化，不重推。
- **Helium @launchhelium**：官网 heliumpad.com 仍可访问（私人 payout 发射台，非免费 mint）。R2202 已收录并通知。无实质变化，不重推。
- **BAD APE @artnesh**：OpenSea total_supply 仍 0、持有 0，合约仍是 0xa5678ecc22cb5be376a222559a7d09cb562243d7。不是已确认免费 mint LIVE。R2203 已通知收录。不重推。
- **Fueltender / AGX**：站点/合约仍在，无实质变化，不重推。
- **2hourfun / Shielded Wizards**：公售仍是 **2026-11-26 05:00 CST**。本轮 lastScout 02:48:50 CST，距首窗约 2.2 小时，**未到首次 ≤2h，不提前告警**。MUST 再见 2hourfun 01:09 CST「4 hours」官帖，与既定首窗一致，不是改期。Shielded Wizards 本轮 MUST 未见新官帖；WL 免费铸仍按此前 LIVE 口径（R2165 已提醒），不因仍 LIVE 重推。
- **Vicehood @Vicehood_RH**（已在库，本轮补到官方时间表）：KW_CORE 见到官帖转发「MINT TOMORROW AT 17:00 UTC」。官网 vicehood.xyz 仍是 Early List。官方合集是 OpenSea **vchood**（twitter_username=Vicehood_RH 互证，合约 `0x0648b448fe7b0bf828445a63a44927932f95d839`，robinhood），SeaDrop mintStatus=MINTING_SOON，0/3333。SIGNED_PRESALE 2026-11-27 01:00–04:00 CST，第二段 04:00–05:00 CST，PUBLIC_SALE 2026-11-27 05:00 CST–2026-11-30 07:00 CST。不是已开铸 LIVE。距首窗约 22 小时，未到首次 ≤2h，**不提前告警、不重推**。注意同名合集 vicehood（PlayVicehood，已在铸 209/3333）不是该官号。
- **Wildlife Universe @Wildlifeuni_55 / Tiger Universe**（已在库，本轮补到官网+SeaDrop）：官网 https://wildlifeuniverseofficial.com/ 与官号、OpenSea `tiger-universe-415604972` 互证（合约 `0xbbc8acefe610e09552df941e445a765f916f946f`），写 Launch 26 November 2026 · 7:00 PM IST（21:30 CST）。SeaDrop mintStatus=MINTING_SOON，0/5555。SIGNED_PRESALE 自 2026-11-26 21:30 CST 起分段，PUBLIC_SALE 2026-11-27 02:29 CST 起。不是已开铸 LIVE。R2189 已记录第三方「明日 1:30 PM UTC 免费 mint」口径。距首窗约 18.7 小时，未到首次 ≤2h，**不提前告警、不重推**。

## notify 判定

- **notify=true**
- 原因：真新收录 1 项 YORI，官网白名单申请已开（免费登记），自称/第三方称 Aptos 3333 份 FREE MINT、日期 TBA，不是已开铸 LIVE；告警已点名，禁止只写「见面板」。
- 无首次 ≤2h、无新的开铸确认需要另报。
- alert：`R2205｜YORI @yoricolors 官网白名单申请已开，自称/第三方称 Aptos 3333 份 FREE MINT，铸造日期 TBA，并非已开铸 LIVE，属高风险；详情 https://reboot7454.github.io/early-scout/ ，本号不自动 mint。`
- namedFreeMintOrRegistration：`YORI @yoricolors`
- namedPaidLe2h：无
- namedMintConfirm：无
- dsFallback=false（admit / score / alert 均走 DeepSeek deepseek-flash，思考开启）

## Discord Peek

- `discordPeekDeferred=true`（占位，父进程后补合并）。apply 见到 `/tmp/r2205/discord_peek.json`：attemptedAt 2026-11-26 02:37:04 CST，loginOk=false，loginWall=true，未翻频道、cutoffs 未推进。X 路径未开浏览器、未自行 Peek。

## 其它

- Canton / Glaze / TokenWorks watch 已 soft-touch lastChecked。
- 本号不自动 mint。

## 写盘合并

- 本轮 dry-run 期间（2026-11-26 02:38:39 CST）远程/工作区已有用户点名补收 **ONE LaunchPad @one_launchpad**（commit f593696，round=2204，挂 userFollowWatch + agentPadWatch，focus=false）。不是免费 mint / 免费登记 / 已开盘 LIVE。写盘已把该卡与 Watch 条目合并进 R2205 面板，未覆盖用户补收；不列入 round2205Added，不重推。写盘后 uf_total=2431（@one_launchpad 在 @yoricolors 之前），ufCursor 仍是 2301 @antebellrh。
