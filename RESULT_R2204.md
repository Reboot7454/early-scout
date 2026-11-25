# R2204 X-radar RESULT

- Round: **R2204**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-26 02:17:19 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170（保持，未改）
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2204/RESULT_R2204.md`、`/tmp/r2204/notify.json`、`/tmp/r2204/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2204/apply_r2204.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2204/data.json.src APPLY_DRY_OUT=/tmp/r2204/data.json` 已成功）

## X 预算与检索

- **remainingBefore=117/1000**（首搜 UF1 后脚注 remainingToday=116，故开火前为 117；与 R2203 直播脚注 remainingAfter 一致，落在 tight 预期 ±20 内。）
- **remainingAfter=104/1000**
- **xReads=13**（main 12 + silent 1；按已排 queries.json 13 次照跑，无计划外搜索，未补 MUST_OFF，未做薄栏 24h）
- **十栏覆盖：** 六个薄栏独立 30m KW（LZ / TAPE / GIWA / DOGE / BTC / STARK）+ 核心栏与 GAPS 合并为一次 KW_CORE（30m）。MUST_OFF 本轮 tight 已跳过（官号 30m 延期），未补跑（live remainingBefore=117，未达 ≥250 阈值）。
- **mode=tight** / softCap=10 / minSpend=10 / silentCap=1。已写入 `meta.xBudgetMode=tight`。计划 13 次略高于 softCap 10，按已排 queries.json 照跑，未 override-full，未再加计划外搜索。
- 未对已知 NF `@starx_xlayer` 做 from: 重试。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 0 | 116 |
| UF2 | 30m | 0 | 115 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 114 |
| KW_LZ | 30m | 3（有 next_token，未翻页） | 113 |
| KW_TAPE | 30m | 10（有 next_token，未翻页） | 112 |
| KW_GIWA | 30m | 25（触顶，有 next_token，未翻页） | 111 |
| KW_DOGE | 30m | 11（有 next_token，未翻页） | 110 |
| KW_BTC | 30m | 4（有 next_token，未翻页） | 109 |
| KW_STARK | 30m | 1（有 next_token，未翻页） | 108 |
| KW_CORE | 30m | 25（触顶，有 next_token，未翻页） | 107 |
| MEN_LZ | 24h | 25（触顶，有 next_token，未翻页） | 106 |
| MEN_ELY | 24h | 20（有 next_token，未翻页） | 105 |
| SILENT_LZ | 24h | 25（触顶，有 next_token，未翻页） | 104 |

（KW_STARK 与 KW_CORE 之间发生分钟重置，remMin 21→29，今日额度仍按 108→107 连续扣减。）

## UF 分片 / 光标

- 本轮分片：cursor **2221 @cbreakersnft** 起 40 个到 **@xanderterminal**，两次 from:（UF1 25 + UF2 15），wrap=false
- UF1：0 帖
- UF2：0 帖
- 无新官号窗口
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2261 @stalliononeth**，uf_total 2429（新挂 @Slime_agents 在名单末尾，cursor 指向不变），wrap=false

## Mentions 与静号

- **本轮 mentions：** LayerZero（MEN_LZ 25）/ Elysium（MEN_ELY 20）
- **下轮 mentions 轮转：** DogeEVM / BTC / Starknet / squeek / STARX
- **本轮静号：** LayerZero（2204 % 11 = 4；SILENT_LZ 25 条，触顶未翻页）
- **下轮静号：** Elysium
- **silentAccounts：** ran=true，seen=25，sentToReview=0，admitted=0，skipped=0。search_users 仍不可用，用 mentionQuery 兜底。25 条多为 LayerZero/OFT 讨论或已在库项目提及，未见可核验的新官号窗口。本轮新收录 Slime 来自 KW_CORE，不是静号栏。

## 薄栏 24h 回看

- 30m 命中：KW_LZ=3、KW_BTC=4、KW_STARK=1，均 <5；KW_TAPE=10、KW_GIWA=25、KW_DOGE=11，均 ≥5
- 主计划跑完后 remainingToday=104，**低于**大致 ≥150 的门槛，**未做**薄栏 24h 补搜
- **没做：** KW_LZ_24（30m 为 3 且优先）、KW_BTC_24、KW_STARK_24。KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（尤其 KW_CORE）改成 24h。未为 24h 补搜翻页。

## 新收录（DeepSeek 打分，dsFallback=false）

`meta.round2204Added` = 顶层 `newThisRound` = `['slime-agents']`。该卡 focus=false，已同时挂 userFollowWatch + freeMintWatch。links 写了 `x` 与 `twitter`。

- **Slime @Slime_agents / https://opensea.io/collection/slime-302038161**（打新，score=76）：建号 2026-10-25 01:45:46 CST（约 32 天），107 粉 / 11 帖，资料栏无独立官网。本轮未见该号自己出现在搜索主结果，KW_CORE 30m 转发了其官帖 2026-11-25 14:29:08 CST（https://x.com/Slime_agents/status/2125476864277778667）：自称 mint page is live on OpenSea，Date 28th November 16:00 UTC，Supply 555，Price FREE MINT，Chain Robinhood Chain，并收集 EVM 钱包做 WL。OpenSea API：name=Slime，created_date=2026-11-23，chain=robinhood，合约 `0xbc05c29b74bb812c1f270b085d294f6bcccc4938`，twitter_username=Slime_agents（与官号互证），project_url 空，total_supply=0，持有 0。合集 HTML SeaDrop：mintStatus=MINTING_SOON，maxSupply=555，totalSupply=0，activeDropStage=null。SIGNED_PRESALE 2026-11-28T16:00:00Z–2026-11-29T17:00:00Z（2026-11-29 00:00 CST–2026-11-30 01:00 CST）；PUBLIC_SALE 2026-11-29T17:00:00Z–2026-12-01T17:00:00Z（2026-11-30 01:00 CST–2026-12-02 01:00 CST）。不是已确认免费 mint LIVE。DeepSeek admit + score（overall=76，admit=true）。本号不自动 mint。

## 看见但未收录

- **GIWAPUNK @giwapunk / https://giwapunk.xyz**：建号 2026-08-08 20:35:00 CST（约 109 天），1171 粉 / 46 帖。本轮官帖 2026-11-26 01:59:31 CST（https://x.com/giwapunk/status/2125650606513602749）称已在 GIWA testnet 跑通 free mint / waitlist / public / reveal（115 checks，0 failed），现在等 GIWA 主网。官网与 https://x.com/giwapunk 互证，写供应 5,000（免费 4,450 + 公售 500 + 团队 50），Nothing is minted yet，Community project，不隶属 GIWA/Dunamu。不是已确认免费 mint LIVE。DeepSeek 初筛 admit，打分 overall=44 且 admit=false（名单已定、主网未上、早期度下降），本轮不入库。
- **Famulus @famulusai / https://famulusai.app**：建号 2026-11-19 00:56:24 CST（约 7 天），2 粉 / 10 帖。官帖 2026-11-26 00:15:11 CST 称 Famulus is live，面向 Elysium 与 Hyperliquid 的链上监控工具（不签名、不持钥，Telegram 汇报）。不是免费 mint / 免费登记。DeepSeek 初筛 admit，打分 overall=42 且 admit=false（无打新路径、信息过薄），本轮不入库。
- **Zayro @zayrotrade / https://zayro.trade**：建号 2026-11-18 17:30:12 CST（约 7 天），951 粉 / 20 帖，twitter:site=@zayrotrade 互证。官网称 GIWA 测试网合成永续，最高 1000x，traded against the house。不是免费 mint。DeepSeek 初筛 admit，打分 overall=38 且 admit=false（高杠杆对赌 + 涨粉异常），本轮不入库。
- **BO @Bo1488J / https://bo1488.xyz/**：建号 2014-05-01（约 12.6 年），809 粉 / 179 帖。官网互证 https://x.com/Bo1488J，自称 Robinhood Chain 888 anime skulls，合约 `0x98f662cdb17540f1f412368cdc2a7bbe875aeca0`，mint date not set yet。本轮未见该号自己的主结果帖，只有第三方 @ayoolag60 抽奖称 upcoming mint。未自称免费 mint。DeepSeek skip（号龄极长、非早期窗口）。
- **SHILLit @Shillitfun / https://shillit.fun/**：建号约 165 天，458 粉，已在运营的 Solana 发射台，非极早期，不入库。
- **Voxro / @ShieldSuite_**（http://voxro.shieldsuite.xyz）：TapeOut hackathon 产品称已 LIVE，工作室号龄约 227 天，不是 mint 窗口，本轮站点 HTTP 500，不入库。
- **Hood Havoc @HoodHavocNFTS**：已在库。KW_CORE 转发的「mint dates have moved」是 2026-11-23 官帖，R2150 已记 GTD 12-01 / FCFS 12-02 / Public 12-03，不是新改期，不重推。
- **已在库项目的转发/复述：** @Spike__wtf（LayerZero 免费 mint 抽奖，已在库）、@UnicornGPrix、@Riftidegame、@AI_SlopRH、@MMIX_io、@NorthBoundNFT、@GAMA_GIWA / @GamaDotWin、@AscendLaunch（@supersmoney 只是观望帖）、@useatlaspad 等，不新建卡。

## 必须通知的 ≤2h / 库内刷新

- **deMiners @deMinersNft：** 付费公售仍按 2026-11-26 00:30:04 CST 原时间表进行（activeDropStage=PUBLIC_SALE stageIndex=0，至 2026-11-28 00:30:04 CST）。SeaDrop mintStatus=MINTING，OpenSea 568/3333（与 R2203 持平），持有 150（与 R2203 持平），地板 0.0001 ETH（R2203 为 0.00016 ETH，此为二级地板）。价格字段本轮 SeaDrop JSON 仍无，沿用已核验 0.0002 ETH，未见改价/改期/取消。MUST 24h 仍见已在 R2203 记过的 01:14:52 CST 短回复。R2197 已发付费公售首次 ≤2h，R2201 已核到按点开出。**供应持平，仅二级地板变化，不重推。**
- **Ugly Puggies @uglypuggies：** 免费 mint 仍 LIVE。SeaDrop mintStatus=MINTING，253/777（R2203 为 252），持有 190（与 R2203 持平），地板 0.000169 ETH（与 R2203 持平）。activeDropStage 仍是 stageIndex=2 SIGNED_PRESALE，至 2026-11-26 13:30 CST；stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 仍要到 2026-11-27 13:30 CST。时间表与 R2203 完全一致。MUST 本轮未见该号新帖。**仍 LIVE / +1 进度，不重推。**
- **Agent Cards @agentcardshq：** 官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=5427/1,007,493，现价约 0.00198 BNB（与 R2203 完全持平）。MUST 24h 再见已在 R2202/R2203 记过的回购/纠偏续帖（含 00:38 CST「We got the AGENTMINT launch wrong」），不是新的铸造规则变化。不是免费 mint。R2200 已通知确认开铸。**无实质变化，不重推。**
- **The Jacket @TheJacket_NVDA：** OpenSea 仍 MINTING / PUBLIC_SALE，213/777（与 R2203 持平），持有 135（与 R2203 持平），地板 0.61 USDG。MUST 未见新官帖。**进度持平，不重推。**
- **TRIFORGE @TriForgeAgent：** 链上 Forge Keys 728/3333（R2203 为 723，未暂停），claims 31（R2203 为 30），lpMintOpen=True，lpTotalMinted=1，挖矿仍开（miningTotalShares=6）。MUST 24h 仍见已在 R2203 记过的 01:32:26 CST 官帖。**规则未变，小幅进度，不重推。**
- **F0B90B @F0B90Bclub：** 链上 mintOpen=True，totalMinted=406/10000（R2203 为 402），remaining=9594。MUST 未见新官帖。**小幅进度，不重推。**
- **Antopia @antopia_xyz：** 链上 saleOpen=True，totalMinted=6253/8888（与 R2203 持平），freeRemaining=0。MUST 未见新官帖。**无实质变化，不重推。**
- **VALORIX @VALORIXBNB：** 公共 BSC RPC：ValorixCards totalMinted=12（与 R2203 持平），ValorixMint fillSold=0/5500。MUST 未见新官帖。**无实质变化，不重推。**
- **AGX @Agx_bsc：** 官网 https://agx.98stay.com 本轮改为「官网维护中，即将回来 / Under maintenance. Back soon.」（R2203 仍写「演示版，合约尚未部署」）。三份地址在 BSC 上仍有 bytecode。MUST 未见新官帖。未确认开铸 LIVE，不是免费 mint。官网改为维护页，不是开铸/改价/改期。**不重推。**
- **Fueltender @fueltenderagent：** 官网 https://fueltender.agency 本轮 HTTPS 200。MUST 未见新官帖，无新的首次铸造窗口。R2199 已通知。**不重推。**
- **Helium @launchhelium：** 官网 https://heliumpad.com 本轮 HTTPS 200，twitter:site=@launchhelium，文案未变。本轮未见新官帖。不是免费 mint / 免费登记。R2202 已收录并通知。**无实质变化，不重推。**
- **BAD APE @artnesh：** OpenSea 仍 total_supply=0、持有 0，合约仍是 `0xa5678ecc22cb5be376a222559a7d09cb562243d7`，合集 HTML 未见 SeaDrop 阶段。不是已确认免费 mint LIVE。R2203 刚收录并已通知。**无实质变化，不重推。**
- **2hourfun @2hourfun：** 官方第一场窗口仍是 2026-11-26 05:00 CST（21:00 UTC）。MUST 24h 仍见已在 R2203 记过的 01:09:03 CST 官帖（https://x.com/2hourfun/status/2125637903741063614）倒计时 4 hours，另有 01:13 / 01:31 CST 短回复，与既定首窗一致，不是改期。本轮约 02:10–02:14 CST，尚未进入首次 ≤2h（约 03:00 CST）。**不提前告警。**
- **Shielded Wizards @ShieldedWizBTC：** 公售仍按 2026-11-26 05:00 CST（21:00 UTC）。MUST 未见新官帖。WL 免费铸仍按此前 LIVE 口径（R2165 已提醒），不因仍 LIVE 重推。本轮未到公售首次 ≤2h，**不提前告警。**

## notify 判定

- **notify=true**
- 原因：本轮新收录 1 项 Slime（真新），官帖自称 Robinhood Chain 555 份 FREE MINT，OpenSea 铸页已上，但 SeaDrop 为 MINTING_SOON、供应 0，不是已确认免费 mint LIVE，告警已点名。库内 LIVE/公售项目均不重推。2hourfun / Shielded Wizards 未到首次 ≤2h，不提前告警。
- namedFreeMintOrRegistration：`Slime @Slime_agents`
- namedPaidLe2h：无
- namedMintConfirm：无
- alert 由 DeepSeek 撰写（dsFallback=false）

## 其它

- dsFallback=false（admit / score / alert 均走 deepseek-flash，思考开启）
- discordPeekDeferred=true（本轮盒内 Chrome 已尝试 Peek，loginOk=false、loginWall=true，landed https://discord.com/login?... ；四频道 lastSeen 仍停在 2026-11-23，cutoffs 未推进。未重发登录表单。）
- Canton / Glaze / TokenWorks：本轮仅 soft-touch lastChecked，无新 admit
- 本号不自动 mint
