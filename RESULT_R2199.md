# R2199 X-radar RESULT

- Round: **R2199**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-25 23:54:11 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2199/RESULT_R2199.md`、`/tmp/r2199/notify.json`、`/tmp/r2199/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2199/apply_r2199.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2199/data.json.src APPLY_DRY_OUT=/tmp/r2199/data.json` 已成功）

## X 预算与检索

- **remainingBefore=200/1000**（首搜 UF1 后脚注 199/1000，故开火前为 200，与 R2198 remainingAfter 一致；开火前预期也是 200）
- **remainingAfter=171/1000**
- **xReads=29**（main 28 + silent 1；计划 26 + 薄栏 24h 3）
- **十栏关键词全部跑完**（LZ / TAPE / GIWA / DOGE / BTC / STARK / MINT / MINE / PAD / GO / ELY + KW_GAPS，均为 30m）
- **Override：** remaining 正好在 pace 边界（=200，不是 >>200，也不是 <200）。按用户额度够时不得砍十栏的规则，跑满 queries.json 已排好的增量计划（25 主搜 + 1 静号），并在薄栏 30m KW <5 时加 24h 回看。已写入 `meta.xBudgetMode=pace-override-full`
- **x_budget 建议** mode=pace、softCap=18、minSpend=18、silentCap=2，本轮实际花费 29（含 3 次薄栏 24h），高于 softCap，但符合额度够时不得砍栏的 override。
- 未对已知 NF `@starx_xlayer` 做 from: 重试；本轮 mentions 子集不含 MEN_STARX。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 2（有 next_token，未翻页） | 199 |
| UF2 | 30m | 0 | 198 |
| UF3 | 30m | 0 | 197 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 196 |
| MUST_WIN2 | 24h | 25（触顶） | 195 |
| MUST_WIN3 | 24h | 25（触顶） | 194 |
| MUST_WIN4 | 24h | 25（触顶） | 193 |
| MUST_OFF | 30m | 1（有 next_token，未翻页） | 192 |
| KW_LZ | 30m | 0 | 191 |
| KW_TAPE | 30m | 25 | 190 |
| KW_GIWA | 30m | 25 | 189 |
| KW_DOGE | 30m | 17 | 188 |
| KW_BTC | 30m | 2 | 187 |
| KW_STARK | 30m | 1 | 186 |
| KW_MINT | 30m | 25 | 185 |
| KW_MINE | 30m | 2 | 184 |
| KW_PAD | 30m | 25 | 183 |
| KW_GO | 30m | 25 | 182 |
| KW_ELY | 30m | 9 | 181 |
| KW_GAPS | 30m | 25 | 180 |
| MEN_PADS | 24h | 17 | 179 |
| MEN_GIWA | 24h | 25（触顶） | 178 |
| MEN_TAPE | 24h | 7 | 177 |
| MEN_LZ | 24h | 25（触顶） | 176 |
| MEN_ELY | 24h | 24 | 175 |
| SILENT_STARK | 24h | 0 | 174 |
| KW_LZ_24 | 24h | 24 | 173 |
| KW_BTC_24 | 24h | 25（触顶） | 172 |
| KW_STARK_24 | 24h | 25（触顶） | 171 |

## UF 分片 / 光标

- 本轮分片：cursor **2011 @goodlauncher** 起 50 个到 **@PredictAgent**（UF3 短尾巴），三次 from:
- UF1 仅 @makefunai 2 帖（AI 比赛平台 make.fun，非铸造窗）；UF2/UF3 全部 0 帖
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2061 @fendrofinance**，uf_total 2423（无新卡，数量未变），wrap=false

## Mentions 与静号

- **本轮 mentions：** pads-rest（MEN_PADS 17）/ GIWA（MEN_GIWA 25 触顶）/ Tape（MEN_TAPE 7）/ LayerZero-24h（MEN_LZ 25 触顶）/ Elysium-rest（MEN_ELY 24）
- **下轮 mentions 轮转：** DogeEVM / BTC / Starknet / squeek / STARX
- **本轮静号：** Starknet（2199 % 11 = 10；SILENT_STARK 0 条）
- **下轮静号：** 打新
- **silentAccounts：** ran=true，seen=0，sentToReview=0，admitted=0，skipped=0（mentionQuery 兜底，0 命中）

## 薄栏 24h 回看

- 30m 命中：KW_LZ=0、KW_BTC=2、KW_STARK=1，均 <5；KW_TAPE=25、KW_GIWA=25、KW_DOGE=17，均 ≥5
- **做了：** KW_LZ_24（24）、KW_BTC_24（25 触顶）、KW_STARK_24（25 触顶）
- **没做：** KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（KW_MINT / KW_PAD / KW_GO 等）改成 24h。

## 新收录（DeepSeek 打分，dsFallback=false）

- 本轮 **无新收录**。`meta.round2199Added` = 顶层 `newThisRound` = `[]`

## 看见但未收录

- **@shhhhhdotfun**（显示名 shhhhh）：建号 2026-11-25 23:21:49 CST（约 0.02 天）、2 粉 / 1 帖。bio 自称 Solana 上由 Helius 驱动的 private memecoin launchpad。资料栏无官网。唯一帖是 X Article（https://x.com/i/article/2125613721787478016，标题 “shhhhh: trade the chart, not the wallet”），不是可互证站点。未再读 X，未收录。
- **@giwa_lauchpad**：空资料、0 粉，喊单/提及，与往轮一致，未收录。
- **@goge_sol**（https://yearofthegoat.lol）：约 6.3 天、220 粉，bio 自称 Doge 的山羊变体、CA 已在 pump.fun，不是新铸造窗，未收录。
- **@astituponi / @supersmoney** 等：转述 GAMA / @AscendLaunch，非可核验官号窗口，未收录。
- **@Oathlydotai**：约 0.1 天、无官网，自称可验证证明工具，无铸造窗，未收录。

## 必须通知的 ≤2h / 库内刷新

- **Fueltender @fueltenderagent：必须通知。** 23:15:33 CST 官帖（https://x.com/fueltenderagent/status/2125609342099750914）称 TENDER is live on Pons，CA `0x5250D8e65988BB3Ee6aDD53309BAE9BF102a7f0a`。23:18:55 CST 再发 “TENDER is live, and the tank was running before the token existed”。随后有首笔 burn、首笔 refuel、Crew pass 开通等官帖。官网 https://fueltender.agency 现已展示同一 CA 并可跳转 Pons / DexScreener（上轮仍写 CA at launch）。Pons 发射页标题 Fueltender (TENDER) | Pons。**不是免费 mint / 免费登记 / 免费 LIVE。** R2196 已收录，R2197/R2198 只报过即将上线（R2198 22:45 CST 官帖仍称 minutes away），本轮因确认上线再通知。
- **Ugly Puggies @uglypuggies：仍 LIVE，不重推。** 本轮已过 23:30 CST。合集 HTML SeaDrop：mintStatus 仍 **MINTING**，erc721.totalSupply=**211/777**（R2198 为 30/777；公开 API total_supply=205），持有 163，地板 0.00012 ETH。时间表：stageIndex 1 SIGNED_PRESALE 23:00–23:30 CST 已结束；**activeDropStage 现为 stageIndex=2，类型仍是 SIGNED_PRESALE**（23:30 CST–2026-11-26 13:30 CST）。stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 要到 2026-11-27 13:30 CST。阶段类型未变、规则未见变化，只是仍 LIVE 与进度推进。MUST 另见到 23:30:29 CST 回复短帖，不是关窗确认。R2198 已因确认开铸通知。
- **Agent Cards @agentcardshq：未见开铸确认，不重推。** 翻印窗仍是 23:00 CST 的 AGENTMINT（不写成免费 mint）。本轮 MUST_WIN3 25 条触顶未翻页，本页被 @tryopencom / @ajourneyboats 等占满，未见 @agentcardshq 官帖，未见开铸/改期。未额外读 X。R2195 已发首次 ≤2h。
- **deMiners @deMinersNft：不重推。** 付费公售仍 2026-11-26 00:30:04 CST 起、0.0002 ETH，OpenSea 时间表未改（activeDropStage 仍是 SIGNED_PRESALE stageIndex=2 至 00:30:04 CST）。OG 免费 mint 仍 LIVE 至同一时刻。OpenSea API 527/3333（drop 528；R2198 527）、持有 141、地板 0.00035 ETH。R2197 已发付费公售首次 ≤2h。
- **不提前告警** 2hourfun / Shielded Wizards 公售（均为 2026-11-26 05:00 CST）。extract 假 LE2H 已忽略。ORIPA 2h 窗已结束，不重推。
- **AGX @Agx_bsc：不重推。** 官网仍写演示版、铸造合约尚未部署、进度 0/5,000；本轮核到官网列出的铸造/代币/锁仓三份地址在 BSC 上均已有 bytecode（代币 CA `0x7F619A477ec52eb77Cc9922c616185e8E43304Bb` 也写入了 bio），与「尚未部署」文案仍不一致，未确认开铸 LIVE，不是免费 mint。R2198 已收录并提醒。
- 库内进度（无实质变化或不构成单独告警，不重推）：TRIFORGE 链上 662/3333（R2198 647），claims 24（R2198 23），付费预售 lpTotalMinted=1（上轮 0，本轮见到第 1 笔 0.003 BNB）；F0B90B 336/10000（R2198 332），mintOpen=true，MUST 再见到 22:31:37 CST 自称 304 的进度帖；Antopia 6253/8888（与 R2198 持平）、免费额度仍满；The Jacket 209/777（持平）、持有 133、地板 1.0 USDG；VALORIX Hero Cards 仍 11、fillSold=0/5500；Mopao 官网静态页仍未见 CA，MUST 再见到早于已记录 live 官帖的 21:32 CST 终端预告。

## discordPeekDeferred

- `/tmp/r2199/discord_peek.json` 已存在并合并进 `meta.discordAlphaPeek`。
- loginOk=false，loginWall=true，channelsPeeked=false，items=0。`discordPeekDeferred=true`。attemptedAt `2026-11-25 23:36:54 CST`。四频道 lastSeen 未改。

## 失败 / 限制

- X 搜索 29/29 成功，errors=[]。dsFallback=false。
- 首批 8 次搜索（UF1–UF3 / MUST_WIN–MUST_OFF）当时未设 `write_to_file`，大结果里 MUST_WIN2 / MUST_WIN4 有完整 asset，其余 6 份从当时完整 inline 工具回包重构落盘（未重搜、未再读 handle）。其后 21 次均 `write_to_file` 直存。
- MUST_WIN / MUST_WIN2 / MUST_WIN3 / MUST_WIN4 及多条 KW/MEN/24h 有 next_token，按规则未翻页。因此 @agentcardshq / @deMinersNft 未出现在 MUST_WIN3 本页，改用 OpenSea 核验，未额外读 X。ACRUX / TAIL 也被 MUST_WIN4 里密集的 Fueltender 官帖挤出本页，未额外补读。
- OpenSea `/drop` 会落到 collection 页，旧 `"drop":` 抽取失败；已从合集 HTML 中的转义 SeaDrop JSON 解析 mintStatus/stages（ugly / deminers / jacket 均成功）。
- flybrainterminal.fun HTTP 500 / HTTPS SSL EOF；thewishlist.site 本轮 SSL EOF；agent.cards 超时；tail.trades.xyz SSL EOF。公共 BSC RPC 与 Triforge RPC 成功。
- 未打开 Discord/浏览器，未改 `/workspace/early-scout/data.json`（mtime 仍为 2026-11-25 23:23:51 CST），未 git commit/push。

## notify

- **notify=true**
- 原因：Fueltender @fueltenderagent 确认 $TENDER 已上线 Pons；不是免费 mint。本轮无新收录。
- namedFreeMintOrRegistration：无
- namedPaidLe2h：无
- dsFallback：false
- alertMessage：

```
R2199：Fueltender @fueltenderagent 确认 $TENDER 已上线 Pons，CA 0x5250D8e65988BB3Ee6aDD53309BAE9BF102a7f0a，官网展示同一 CA；这是代币上线确认，不是免费 mint/免费登记/免费 LIVE。Ugly Puggies 免费 mint 仍 LIVE 但阶段未变不重推；Agent Cards 未见开铸确认不重推；deMiners 公售时间表未改不重推。面板：https://reboot7454.github.io/early-scout/ 本号不自动 mint。
```

## 写盘摘要（供父进程）

- dry-run：`/tmp/r2199/data.json`
- `meta.round2199Added` = 顶层 `newThisRound` = `[]`
- ufCursor **2061 @fendrofinance**，uf_total 2423，wrap=false
- mentionsCoverage / mentionsNext、silentLane=Starknet、silentNext=打新 已写
- Canton / Glaze / TokenWorks lastChecked 软刷到本轮
- 已合并 discord_peek.json，`discordPeekDeferred=true`
- 工作区 `/workspace/early-scout/data.json` 未改（mtime 仍为 2026-11-25 23:23:51 CST）
