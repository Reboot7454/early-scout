# R2203 X-radar RESULT

- Round: **R2203**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-26 01:48:09 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170（保持，未改）
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2203/RESULT_R2203.md`、`/tmp/r2203/notify.json`、`/tmp/r2203/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2203/apply_r2203.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2203/data.json.src APPLY_DRY_OUT=/tmp/r2203/data.json` 已成功）

## X 预算与检索

- **remainingBefore=130/1000**（首搜 UF1 后脚注 remainingToday=129，故开火前为 130；与 R2202 直播脚注 remainingAfter 一致，落在 tight 预期 ±20 内。）
- **remainingAfter=117/1000**
- **xReads=13**（main 12 + silent 1；按已排 queries.json 13 次照跑，无计划外搜索，未补 MUST_OFF，未做薄栏 24h）
- **十栏覆盖：** 六个薄栏独立 30m KW（LZ / TAPE / GIWA / DOGE / BTC / STARK）+ 核心栏与 GAPS 合并为一次 KW_CORE（30m）。MUST_OFF 本轮 tight 已跳过（官号 30m 延期），未补跑（live remainingBefore=130，未达 ≥250 阈值）。
- **mode=tight** / softCap=10 / minSpend=10 / silentCap=1。已写入 `meta.xBudgetMode=tight`。计划 13 次略高于 softCap 10，按已排 queries.json 照跑，未 override-full，未再加计划外搜索。
- 未对已知 NF `@starx_xlayer` 做 from: 重试。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 1（有 next_token，未翻页） | 129 |
| UF2 | 30m | 2（有 next_token，未翻页） | 128 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 127 |
| KW_LZ | 30m | 1（有 next_token，未翻页） | 126 |
| KW_TAPE | 30m | 5（有 next_token，未翻页） | 125 |
| KW_GIWA | 30m | 25（触顶，有 next_token，未翻页） | 124 |
| KW_DOGE | 30m | 9（有 next_token，未翻页） | 123 |
| KW_BTC | 30m | 3（有 next_token，未翻页） | 122 |
| KW_STARK | 30m | 1（有 next_token，未翻页） | 121 |
| KW_CORE | 30m | 25（触顶，有 next_token，未翻页） | 120 |
| MEN_GIWA | 24h | 25（触顶，有 next_token，未翻页） | 119 |
| MEN_TAPE | 24h | 5（有 next_token，未翻页） | 118 |
| SILENT_GO | 24h | 8（有 next_token，未翻页） | 117 |

（脚注顺序上后 4 次并行完成，remToday 120→117 与完成顺序一致。）

## UF 分片 / 光标

- 本轮分片：cursor **2181 @magpiegiwa** 起 40 个到 **@brainex__ai**，两次 from:（UF1 25 + UF2 15），wrap=false，uf_skip=[]
- UF1：1 帖（@Solvyren 说明 explorer 上 best/finalized block，已在库）
- UF2：2 帖（@tolseytools 审计结果与 Pons CA `0x6B99a880F35e93A6cb849fCCC436B8c69d668816`，已在库）
- 无新官号窗口
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2221 @cbreakersnft**，uf_total 2428（新挂 @artnesh 在名单末尾，cursor 指向不变），wrap=false

## Mentions 与静号

- **本轮 mentions：** GIWA（MEN_GIWA 25）/ Tape（MEN_TAPE 5）
- **下轮 mentions 轮转：** LayerZero-24h / Elysium-rest
- **本轮静号：** GO盘（2203 % 11 = 3；SILENT_GO 8 条）
- **下轮静号：** LayerZero
- **silentAccounts：** ran=true，seen=8，sentToReview=0，admitted=0，skipped=0。search_users 仍不可用，用 mentionQuery 兜底。8 条多为 GO/AR launch 口语或无关讨论，未见可核验的新官号窗口。本轮新收录 BAD APE 来自 KW_CORE，不是静号栏。

## 薄栏 24h 回看

- 30m 命中：KW_LZ=1、KW_BTC=3、KW_STARK=1，均 <5；KW_TAPE=5、KW_GIWA=25、KW_DOGE=9，均 ≥5
- 主计划跑完后 remainingToday=117，**低于**大致 ≥150 的门槛，**未做**薄栏 24h 补搜
- **没做：** KW_LZ_24（30m 为 1 且优先）、KW_BTC_24、KW_STARK_24。KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（尤其 KW_CORE）改成 24h。未为 24h 补搜翻页。

## 新收录（DeepSeek 打分，dsFallback=false）

`meta.round2203Added` = 顶层 `newThisRound` = `['badape']`。该卡 focus=false，已同时挂 userFollowWatch + freeMintWatch。links 写了 `x` 与 `twitter`。

- **BAD APE @artnesh / https://opensea.io/collection/badape**（打新，score=50）：本轮未见该号出现在搜索主结果（includes 无 user 对象，未取到建号时间/粉丝/帖数，未做额外 X 读；xUserId 1205439240844107777 来自 referenced 帖 author_id）。官帖 2026-11-25 22:48:22 CST（https://x.com/artnesh/status/2125602499159797792）称将把 BAD APE 带到 Robinhood Chain 做免费 mint，并请大家 drop EVM address。OpenSea 合集 API：name=BAD APE，created_date=2026-11-25，chain=robinhood，合约 `0xa5678ecc22cb5be376a222559a7d09cb562243d7`，total_supply=0，持有 0，twitter_username 空，无 project_url。合集 HTML 同样 totalSupply=0，未见 SeaDrop 阶段。不是已确认免费 mint LIVE，也不是已核到的免费登记表单，只是自称免费 mint 并收集地址。无独立官网，站点与官号未互证。高风险。DeepSeek admit（overall=50）。本号不自动 mint。

## 看见但未收录

- **@HYPECAT_GANG / https://opensea.io/collection/hypecat-gang**：建号 2020-10-29（约 6 年），1324 粉 / 246 帖，资料栏无官网。本轮官帖 2026-11-26 01:29:33 CST（https://x.com/HYPECAT_GANG/status/2125643062378676403）自称 Whitelist (FREE MINT)，并给 OpenSea 合集与 Google 表单（WHITELIST HYPECAT PHASE 1，https://forms.gle/cvR8j7gd13w8EwC3A）。合集页在 HyperEVM，HTML 可见 uniqueItemCount=0、totalSupply=0、ownerCount=0，未见 SeaDrop 阶段；公开 collection API 本轮 401。不是已确认免费 mint LIVE，只是白名单表单登记。DeepSeek skip（号龄很长，非极早期）。
- **Vice City Babies @robinioquants / https://www.scatter.art/c/vicecitybabies**：建号 2026-07-09（约 139 天），426 粉 / 114 帖，资料栏 https://linktr.ee/robinio（bio 自称 Robinhood Chain 上的 Robinio Quants NFT）。官帖 2026-11-26 01:00:36 CST 称 Public is now live on Scatter，并介绍 Vice City Babies；01:36:37 CST 帖称 20% minted already, free mint for those eligible! Public also live。本轮两次请求 scatter.art 均 HTTP 429，未能核到已铸/价格/阶段。linktr 互证 @robinioquants，但列出的是 https://opensea.io/collection/robinio 与 Robinhood，并未列出 Vice City / Scatter。DeepSeek skip（非极早期，站点未核到）。
- **@FlickerrNft**：社区向 giveaway（FLICKERR SANTA X OWLTOPIA，50 个 GTD 免费 mint 名额指向已在库的 @Owltopia_sol），不是新项目窗口。
- **@Grumplings_2026**：被转发的「FREE GRUMPLINGS mint」兴趣贴是 2026-10-06 的旧帖，不是本轮新开铸。
- **@deuslaunch**：已在库。本轮仅见第三方回复 “free mint”，未见新的已确认开铸证据，不重推。
- **@OUTLAWSxNFT**：已在库。资料写 Free Mint on OpenSea · Nov 27 | 1:30 PM UTC（2026-11-27 21:30 CST），本轮不是 ≤2h，不重推。
- **已在库项目的转发/复述：** @LawoftheAbyss、@Vicehood_RH、@gamapadcom / @GAMA_GIWA（testnet First Firing，已在库）、@Solvyren、@tolseytools 等，不新建卡。

## 必须通知的 ≤2h / 库内刷新

- **deMiners @deMinersNft：** 付费公售仍按 2026-11-26 00:30:04 CST 原时间表进行（activeDropStage=PUBLIC_SALE stageIndex=0，至 2026-11-28 00:30:04 CST）。SeaDrop mintStatus=MINTING，OpenSea 568/3333（R2202 为 536），持有 150（R2202 为 145），地板 0.00016 ETH（R2202 为 0.000349 ETH，此为二级地板）。价格字段本轮 SeaDrop JSON 仍无，沿用已核验 0.0002 ETH，未见改价/改期/取消。MUST 仅见 01:14:52 CST 短回复「Learn how to use a wallet first」。R2197 已发付费公售首次 ≤2h，R2201 已核到按点开出。**只是进度变化，不重推。**
- **Ugly Puggies @uglypuggies：** 免费 mint 仍 LIVE。SeaDrop mintStatus=MINTING，252/777（R2202 为 246），持有 190（R2202 为 186），地板 0.000169 ETH（R2202 为 0.000179 ETH）。activeDropStage 仍是 stageIndex=2 SIGNED_PRESALE，至 2026-11-26 13:30 CST；stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 仍要到 2026-11-27 13:30 CST。时间表与 R2202 完全一致。MUST 本轮未见该号新帖。**仍 LIVE / 小幅进度，不重推。**
- **Agent Cards @agentcardshq：** 官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=5427/1,007,493，现价约 0.00198 BNB（与 R2202 完全持平）。MUST 24h 再见已在 R2202 记过的回购/纠偏续帖，不是新的铸造规则变化。不是免费 mint。R2200 已通知确认开铸。**无实质变化，不重推。**
- **The Jacket @TheJacket_NVDA：** OpenSea 仍 MINTING / PUBLIC_SALE，213/777（R2202 为 211），持有 135（R2202 为 134），地板 0.61 USDG。MUST 未见新官帖。**小幅进度，不重推。**
- **TRIFORGE @TriForgeAgent：** 链上 Forge Keys 723/3333（R2202 为 716，未暂停），claims 30（R2202 为 29），lpMintOpen=True，lpTotalMinted=1，挖矿仍开（miningTotalShares=6）。MUST 再见 01:32:26 CST 官帖复述 721/3333、30 claims、预售至 2 Dec、挖矿 LIVE，与链上一致。**规则未变，小幅进度，不重推。**
- **F0B90B @F0B90Bclub：** 链上 mintOpen=True，totalMinted=402/10000（R2202 为 398），remaining=9598。MUST 未见新官帖。**小幅进度，不重推。**
- **Antopia @antopia_xyz：** 链上 saleOpen=True，totalMinted=6253/8888（与 R2202 持平），freeRemaining=0。MUST 未见新官帖。**无实质变化，不重推。**
- **VALORIX @VALORIXBNB：** 公共 BSC RPC：ValorixCards totalMinted=12（R2202 为 12），ValorixMint fillSold=0/5500。MUST 未见新官帖。**无实质变化，不重推。**
- **AGX @Agx_bsc：** 官网 https://agx.98stay.com 仍写「演示版，合约尚未部署」。三份地址在 BSC 上仍有 bytecode。MUST 未见新官帖。未确认开铸 LIVE，不是免费 mint。**不重推。**
- **Fueltender @fueltenderagent：** 官网 https://fueltender.agency 本轮 HTTPS 200。MUST 未见新官帖，无新的首次铸造窗口。R2199 已通知。**不重推。**
- **Helium @launchhelium：** 官网 https://heliumpad.com 本轮 HTTPS 200，twitter:site=@launchhelium，文案未变。本轮未见新官帖。不是免费 mint / 免费登记。R2202 刚收录并已通知。**无实质变化，不重推。**
- **2hourfun @2hourfun：** 官方第一场窗口仍是 2026-11-26 05:00 CST（21:00 UTC）。MUST 再见 01:09:03 CST 官帖（https://x.com/2hourfun/status/2125637903741063614）倒计时 4 hours，并确认 Opening Night 为 21:00–23:00 UTC 交易、Premiere 为窗口内发射，与既定首窗一致，不是改期。本轮约 01:45–01:48 CST，尚未进入首次 ≤2h（约 03:00 CST）。**不提前告警。**
- **Shielded Wizards @ShieldedWizBTC：** 公售仍按 2026-11-26 05:00 CST（21:00 UTC）。MUST 未见新官帖。WL 免费铸仍按此前 LIVE 口径（R2165 已提醒），不因仍 LIVE 重推。本轮未到公售首次 ≤2h，**不提前告警。**

## notify 判定

- **notify=true**
- 原因：本轮新收录 1 项 BAD APE（真新），官帖自称免费 mint 并收集 EVM 地址，告警已点名。不是已确认免费 mint LIVE。库内 LIVE/公售项目均不重推。2hourfun / Shielded Wizards 未到首次 ≤2h，不提前告警。
- namedFreeMintOrRegistration：`BAD APE @artnesh`
- namedPaidLe2h：无
- namedMintConfirm：无
- alert 由 DeepSeek 撰写（dsFallback=false）

## 其它

- dsFallback=false（admit / score / alert 均走 deepseek-flash，思考开启）
- discordPeekDeferred=true（占位；工作目录已有父进程 Discord Peek 文件，loginOk=false、loginWall=true，已合并进 dry-run 面板，仍标 deferred 供父进程后补合并）
- Canton / Glaze / TokenWorks：本轮仅 soft-touch lastChecked，无新 admit
- 本号不自动 mint
