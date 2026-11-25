# R2202 X-radar RESULT

- Round: **R2202**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-26 01:16:04 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170（保持，未改）
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2202/RESULT_R2202.md`、`/tmp/r2202/notify.json`、`/tmp/r2202/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2202/apply_r2202.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2202/data.json.src APPLY_DRY_OUT=/tmp/r2202/data.json` 已成功）

## X 预算与检索

- **remainingBefore=143/1000**（首搜 UF1 后脚注 remainingToday=142，故开火前为 143；与 R2201 直播脚注 remainingAfter 一致。按 ±20 落在 tight 预期内。）
- **remainingAfter=130/1000**
- **xReads=13**（main 12 + silent 1；按已排 queries.json 13 次照跑，无计划外搜索，未补 MUST_OFF，未做薄栏 24h）
- **十栏覆盖：** 六个薄栏独立 30m KW（LZ / TAPE / GIWA / DOGE / BTC / STARK）+ 核心栏与 GAPS 合并为一次 KW_CORE（30m）。MUST_OFF 本轮 tight 已跳过（官号 30m 延期），未补跑（live remainingBefore=143，未达 ≥250 阈值）。
- **mode=tight** / softCap=10 / minSpend=10 / silentCap=1。已写入 `meta.xBudgetMode=tight`。计划 13 次略高于 softCap 10，按已排 queries.json 照跑，未 override-full，未再加计划外搜索。
- 未对已知 NF `@starx_xlayer` 做 from: 重试；本轮 MEN_STARX 是 mentions of @starx_xlayer（0 条），照跑。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 1（有 next_token，未翻页） | 142 |
| UF2 | 30m | 0 | 141 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 140 |
| KW_LZ | 30m | 0 | 139 |
| KW_TAPE | 30m | 12（有 next_token，未翻页） | 138 |
| KW_GIWA | 30m | 25（触顶） | 137 |
| KW_DOGE | 30m | 6（有 next_token，未翻页） | 136 |
| KW_BTC | 30m | 8（有 next_token，未翻页） | 135 |
| KW_STARK | 30m | 1（有 next_token，未翻页） | 134 |
| KW_CORE | 30m | 25（触顶） | 133 |
| MEN_STARX | 24h | 0 | 132 |
| MEN_PADS | 24h | 21（有 next_token，未翻页） | 131 |
| SILENT_PAD | 24h | 25（触顶，有 next_token，未翻页） | 130 |

（脚注顺序上 MEN_STARX 在 MEN_PADS 之前结束，remToday 132→131 与并行完成顺序一致。）

## UF 分片 / 光标

- 本轮分片：cursor **2141 @blackwater_z26** 起 40 个到 **@privacy_hook**，两次 from:（UF1 24 + UF2 16），wrap=false，uf_skip=[]
- UF1：1 帖（@VexthiumX「Manifesting Robinhood season」，已在库）；UF2：0 帖
- 无新官号窗口
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2181 @magpiegiwa**，uf_total 2427（新挂 @launchhelium 在名单末尾，cursor 指向不变），wrap=false

## Mentions 与静号

- **本轮 mentions：** STARX（MEN_STARX 0）/ pads-rest（MEN_PADS 21）
- **下轮 mentions 轮转：** GIWA / Tape / LayerZero-24h / Elysium-rest
- **本轮静号：** 台子/Meme（2202 % 11 = 2；SILENT_PAD 25 条）
- **下轮静号：** GO盘
- **silentAccounts：** ran=true，seen=25，sentToReview=5，admitted=1（helium），skipped=4（BasketXYZ / BasketLaunch / Quotum / Nekointhehood）。search_users 仍不可用，用 mentionQuery 兜底。

## 薄栏 24h 回看

- 30m 命中：KW_LZ=0、KW_STARK=1，均 <5；KW_TAPE=12、KW_GIWA=25、KW_DOGE=6、KW_BTC=8，均 ≥5
- 主计划跑完后 remainingToday=130，**低于**大致 ≥150 的门槛，**未做**薄栏 24h 补搜
- **没做：** KW_LZ_24（30m 虽为 0 且优先）、KW_STARK_24 / KW_BTC_24。KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（尤其 KW_CORE）改成 24h。未为 24h 补搜翻页。

## 新收录（DeepSeek 打分，dsFallback=false）

`meta.round2202Added` = 顶层 `newThisRound` = `['helium']`。该卡 focus=false，已同时挂 userFollowWatch + agentPadWatch。links 写了 `x` 与 `twitter`。

- **Helium @launchhelium / https://heliumpad.com**（台子/Meme，score=58）：建号 2026-11-25 21:19:12 CST（约 0.16 天），4 粉 / 7 帖，xUserId 2125579863511953408。官帖 2026-11-26 00:57:56 CST（https://x.com/launchhelium/status/2125635105666515370）称 Helium is NOW LIVE on Solana，自称私钥密支付发射台：图表/价格公开，持有人收款经 Helius Privacy Rings 以加密 hSOL 到账。官网 HTTPS 200（HTTP 根路径 500），twitter:site=@launchhelium，站点与官号互证。不是免费 mint，也不是免费登记；未见 SPL CA。极新号，风险高。本号不自动 mint。

## 看见但未收录

- **@BasketXYZ / https://buildabasket.xyz** 与 **@BasketLaunch / https://basketlaunch.fun/**：约 73–79 天、81/118 粉。官网与各自官号互证，同属 ETF/篮子发射台叙事。buildabasket 页可见 DEVNET；basketlaunch.fun 写 Confirmed launches will appear here。库内已有 @Basketdotxyz（basketlaunch.xyz）。第三方推文称像复制盘/农场。DeepSeek skip（非早期，且疑似与库内 Basket 重复）。不是免费 mint。
- **@quotumorg / https://quotum.org**：约 62 天、452 粉 / 969 帖。官网 QVOTVM，付费推理座位（ETH/USDG/股票代币），不是 NFT mint。DeepSeek skip（发帖已多、产品偏成熟）。
- **@Nekointhehood**：约 91 天、929 粉 / 仅 2 帖，资料栏无官网。bio 自称 3000 份 free mint。本轮仅见第三方 @Messiahdegreat 转赠 upcoming mint 白名单，未见自身官帖、无链/CA/开铸时间。DeepSeek skip（证据不足，不是已确认免费 mint LIVE）。
- **@DOGEONGIWA / gdoge.xyz**：号龄逾 3 年，本轮称 TIP/Swap+Launchpad ready；gdoge.xyz 本轮 SSL 证书主机名不匹配，未当极早期新窗口收录。
- **@OopsIWonNFT / @Predictulator / @MemeWarGame_bot**：仅见转发或空资料个人/机器人号，未形成可核验官号窗口，未收录。
- **已在库项目的转发/复述：** @Riftidegame（官帖再确认 WL + 2,000 免费 mint，开铸仍 TBA，R2166 已收，不重推）、@LawoftheAbyss、@MMIX_io、@PlunderPort、@PlayJadebound、@freakapesnft、@Zenko_NFT、@musenftxyz、@ThebeliefNFT、@NeoEdo2099、@indexitcash、@AnthroposAgents 等，不新建卡。

## 必须通知的 ≤2h / 库内刷新

- **deMiners @deMinersNft：** 付费公售仍按 2026-11-26 00:30:04 CST 原时间表进行（activeDropStage=PUBLIC_SALE stageIndex=0，至 2026-11-28 00:30:04 CST）。SeaDrop mintStatus=MINTING，OpenSea 536/3333（R2201 为 531），持有 145，地板 0.000349 ETH。价格字段本轮 SeaDrop JSON 仍无，沿用已核验 0.0002 ETH，未见改价/改期/取消。MUST 未见新官帖。R2197 已发付费公售首次 ≤2h，R2201 已核到按点开出。**只是进度变化，不重推。**
- **Ugly Puggies @uglypuggies：** 免费 mint 仍 LIVE。SeaDrop mintStatus=MINTING，246/777（R2201 为 243），持有 186，地板 0.000179 ETH。activeDropStage 仍是 stageIndex=2 SIGNED_PRESALE，至 2026-11-26 13:30 CST；PUBLIC_SALE 仍要到 2026-11-27 13:30 CST。MUST 仅再见已记过的短回复。**仍 LIVE / 小幅进度，不重推。**
- **Agent Cards @agentcardshq：** 官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=5427/1,007,493（与 R2201 持平），现价约 0.00198 BNB，池内约 3.781 BNB。MUST 再见回购/「开盘做得不好」及本周 Lock & Earn 续帖，铸造仍按池价开放。不是免费 mint。R2200 已因确认开铸通知。**无实质规则变化，不重推。**
- **The Jacket @TheJacket_NVDA：** 仍 MINTING，activeDropStage 仍是 PUBLIC_SALE。OpenSea 211/777（R2201 为 209），持有 134（R2201 为 133），地板 0.61 USDG。MUST 未见新官帖。**小幅进度，不重推。**
- **2hourfun @2hourfun：** 首窗仍是 2026-11-26 05:00 CST（21:00 UTC）。MUST 未见新官帖。官网仍提示曲线上暂无币、等窗口打开。本轮约 01:00 CST，**尚未进入首次 ≤2h（约 03:00 CST），不提前告警。**
- **Shielded Wizards @ShieldedWizBTC：** 公售仍是 2026-11-26 05:00 CST。MUST 未见新官帖。WL 免费铸仍按此前 LIVE 口径（R2165 已提醒），不因仍 LIVE 重推。brimhollow.app/mint 本轮为前端壳页，未核到新 minted 数字，不编造进度。**未到公售首次 ≤2h，不提前告警。**
- **Riftide @Riftidegame：** 官帖 01:04:33 CST 再确认白名单已开、2,000 份免费 mint，Apply 指向官网。开铸仍 TBA，不是已开铸 LIVE。R2166 已收录。**不重推。**
- **F0B90B：** 链上 mintOpen=True，398/10000（R2201 为 388）。MUST 未见新官帖。小幅进度，不重推。
- **Antopia：** 链上仍 6253/8888，saleOpen=True，freeRemaining=0。MUST 再见已记过的游戏预告官帖（Clash of Antopia goes live tomorrow），不是铸造规则变化。不重推。
- **VALORIX：** Hero Cards 仍 12，fillSold 仍 0/5500。MUST 未见新官帖。不重推。
- **TRIFORGE：** 链上 716/3333（R2201 为 704），claims 29（R2201 为 27），lpTotalMinted=1。MUST 未见新官帖。小幅进度，不重推。
- **AGX @Agx_bsc：** 官网仍写演示版、合约尚未部署；mint/token/lock 三址仍有 bytecode。MUST 未见新官帖。未确认开铸 LIVE，不是免费 mint，不重推。
- **Fueltender：** 官网 https://fueltender.agency 仍可访问。MUST 未见新官帖，无新铸造窗口，不重推。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅 soft-touch lastChecked。

## notify

- **notify=true**
- 原因：本轮新收录 1 项 Helium（真新）。Helium 不是自称免费 mint / 免费登记 / 免费 LIVE，告警已逐个点名并写明。库内 Ugly Puggies / deMiners / Agent Cards / The Jacket 等仅小幅进度或仍按原时间表，不重推。2hourfun 与 Shielded Wizards 公售仍是 2026-11-26 05:00 CST，本轮未到首次 ≤2h，不提前告警。
- namedFreeMintOrRegistration：无
- namedPaidLe2h：无
- dsFallback：false
- discordPeekDeferred：true（占位，父进程后补合并；本路未开 Discord/浏览器）
- alertMessage：

```
R2202：新增 Helium（@launchhelium）为 Solana 隐私支付发射台，官方帖子自称“NOW LIVE”上线；它不是免费 mint，也不是免费登记（未见 CA，新账号风险高）。库内 LIVE/公售项目均不重推。面板：https://reboot7454.github.io/early-scout/ 本号不自动 mint。
```

## 写盘摘要（供父进程）

- dry-run：`/tmp/r2202/data.json`
- `meta.round2202Added` = 顶层 `newThisRound` = `['helium']`
- ufCursor **2181 @magpiegiwa**，uf_total 2427，wrap=false
- xBudgetMode=tight，remainingBefore=143，remainingAfter=130，xReads=13（main 12 + silent 1）
- 未打开 Discord/浏览器，未改 `/workspace/early-scout/data.json`（sha256 前缀仍与 data.json.src 一致，mtime 仍为 2026-11-26 00:52:27 CST），未 git commit/push。

## 关键失败 / 备注

- OpenSea collection+stats 成功（200）。drops API 未用；`/drop` 会落到合集页，已从合集 HTML 转义 SeaDrop JSON 解析时间表（与 R2195–R2201 相同路径）。
- http://heliumpad.com 根路径 HTTP 500，HTTPS 200。
- gdoge.xyz SSL 证书主机名不匹配。
- flybrainterminal.fun HTTP 500 / HTTPS SSL EOF；thewishlist.site 本轮 SSL EOF（刷新脚本附带探测，非本轮新卡依赖）。
- brimhollow.app/mint 本轮只返回前端壳页，未核到 Shielded Wizards 新的 minted 数字。
- DeepSeek admit/score/alert 均成功，dsFallback=false。score 给 Helium risk=28（与 drawbacks 中的高风险表述不完全同向量），已保留原始分并在卡片 drawbacks 写明风险。
