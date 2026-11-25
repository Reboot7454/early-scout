# R2200 X-radar RESULT

- Round: **R2200**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-26 00:16:22 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2200/RESULT_R2200.md`、`/tmp/r2200/notify.json`、`/tmp/r2200/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2200/apply_r2200.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2200/data.json.src APPLY_DRY_OUT=/tmp/r2200/data.json` 已成功）

## X 预算与检索

- **remainingBefore=171/1000**（首搜 UF1 后脚注 170/1000，故开火前为 171，与 R2199 remainingAfter 一致；开火前预期也是 171）
- **remainingAfter=156/1000**
- **xReads=15**（main 14 + silent 1；计划 13 + 薄栏 24h 2）
- **十栏覆盖：** 六个薄栏独立 30m KW（LZ / TAPE / GIWA / DOGE / BTC / STARK）+ 核心栏与 GAPS 合并为一次 KW_CORE（30m）。MUST_OFF 本轮 tight 已跳过（官号 30m 延期），未补跑。
- **mode=tight** / softCap=10 / minSpend=10 / silentCap=1。已写入 `meta.xBudgetMode=tight`。计划 13 次略高于 softCap 10，按已排 queries.json 照跑，未 override-full，未再加计划外搜索（仅按规则补了 2 次薄栏 24h）。
- 未对已知 NF `@starx_xlayer` 做 from: 重试；本轮 mentions 子集不含 MEN_STARX。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 0 | 170 |
| UF2 | 30m | 0 | 169 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 168 |
| KW_LZ | 30m | 0 | 167 |
| KW_TAPE | 30m | 25（触顶） | 166 |
| KW_GIWA | 30m | 19（有 next_token，未翻页） | 165 |
| KW_DOGE | 30m | 25（触顶） | 164 |
| KW_BTC | 30m | 4（有 next_token，未翻页） | 163 |
| KW_STARK | 30m | 3（有 next_token，未翻页） | 162 |
| KW_CORE | 30m | 25（触顶） | 161 |
| MEN_DOGE | 24h | 9（有 next_token，未翻页） | 160 |
| MEN_BTC | 24h | 25（触顶） | 159 |
| SILENT_MINT | 24h | 25（触顶） | 158 |
| KW_LZ_24 | 24h | 24（有 next_token，未翻页） | 157 |
| KW_BTC_24 | 24h | 25（触顶） | 156 |

## UF 分片 / 光标

- 本轮分片：cursor **2061 @fendrofinance** 起 40 个到 **@auroveil**，两次 from:（UF1 25 + UF2 15）
- UF1 / UF2 全部 0 帖
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2101 @woodlandz_xyz**，uf_total 2423（无新卡，数量未变），wrap=false

## Mentions 与静号

- **本轮 mentions：** DogeEVM（MEN_DOGE 9）/ BTC（MEN_BTC 25 触顶）
- **下轮 mentions 轮转：** 先补本轮剩余 Starknet / squeek / STARX，再回到 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- **本轮静号：** 打新（2200 % 11 = 0；SILENT_MINT 25 条触顶）
- **下轮静号：** 挖矿
- **silentAccounts：** ran=true，seen=25，sentToReview=0，admitted=0，skipped=25（mentionQuery 兜底；25 条均为第三方申请/转发，无官号级新窗口）

## 薄栏 24h 回看

- 30m 命中：KW_LZ=0、KW_BTC=4、KW_STARK=3，均 <5；KW_TAPE=25、KW_GIWA=19、KW_DOGE=25，均 ≥5
- 主计划跑完后 remainingToday=158，大致 ≥150，允许最多 2 次薄栏 24h
- **做了：** KW_LZ_24（24，优先），KW_BTC_24（25 触顶）
- **没做：** KW_STARK_24（30m 虽 <5，但已用满 2 次额度；优先 LZ 其次 BTC）。KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（尤其 KW_CORE）改成 24h。未为 24h 补搜翻页。

## 新收录（DeepSeek 打分，dsFallback=false）

- 本轮 **无新收录**。`meta.round2200Added` = 顶层 `newThisRound` = `[]`
- DeepSeek admit：仅将 borderline `@RAJA_KING_COIN` 送审，结果 skip（CA 仍是俄文占位符，非已核验开盘，不是免费 mint）。

## 看见但未收录

- **@RAJA_KING_COIN**（https://raja-king.fun）：约 12.7 天、3 粉 / 5 帖。bio 自称 Solana joke memecoin、无预售；本轮帖称 bonding curve 已 LIVE，但正文 CA 仍是占位符「[ВСТАВИТЬ_СЮДА_АДРЕС_КОНТРАКТА]」。DeepSeek skip，未收录。
- **@DumpMonkeyCrew**：约 1027 天、2.4 万粉，KW_CORE 第三方 RT 称 OpenSea 1,000 Genesis Keys 免费 mint 即将开。不是极早期官号窗口，未再读 X，未收录。
- **@0xstonkdad / Orbz**：约 19.7 天、517 粉，仅见第三方 @madamayo_ 转述 GTD 免费 mint（565 份）。未见官帖，未再读 X，未收录。
- **@alnazimi420 / @Denytholelp / @Coco0vli** 等：新建空资料喊单/转发 GAMA、@RGBHorse 等已知项目，未收录。
- 静号车道大量 @LawoftheAbyss / @MMIX_io / @thenottiesworld / @Zero_Kitties 申请帖，申请者本身不是官号，未收录。

## 必须通知的 ≤2h / 库内刷新

- **Agent Cards @agentcardshq：必须通知（确认开铸，不是免费 mint）。** MUST_WIN 见到 2026-11-25 23:37:54 CST 官帖（https://x.com/AgentCardsHQ/status/2125614966258413665）：AGENTMINT 5,000 份 fill 以 0.0018 BNB 在 20 分钟内售罄（15:20 UTC / 23:20 CST），537 个 Agent ID 已铸；PancakeSwap 池已开，错过 fill 仍可按池价 99% 继续铸造。23:57:23 CST 续帖（https://x.com/AgentCardsHQ/status/2125619867449512337）称用金库 1 BNB 回购 AGENTMINT 并打入黑洞。官网 https://playagentcards.com/mint（资料栏互证）核到 phase=open、fillSold=5000/5000、后又铸 297 份，合计 **5,297/1,007,493**，现价约 **0.00198 BNB（约 $1.06）**，池内约 3.827 BNB。铸造合约 `0xA013Ad2D38fec3A2851cec573F20D8792e23267f`，代币 `0xb1247d0727c06423b123729C12fEF2f5Fd5e09b5`，交易对 `0x37bC8B5EAd2f14B785b4B5aC4E0659A6AD772bB0`。R2195 已发首次 ≤2h；R2198/R2199 因 MUST 触顶未见官帖。本轮因确认开铸再通知。不得写成免费 mint。
- **Ugly Puggies @uglypuggies：仍 LIVE，不重推。** 合集 HTML SeaDrop：mintStatus 仍 **MINTING**，erc721.totalSupply=**235/777**（R2199 为 211/777；公开 API total_supply=223），持有 177，地板 0.00019 ETH。时间表未变：**activeDropStage 仍是 stageIndex=2 SIGNED_PRESALE**（2026-11-25 23:30 CST–2026-11-26 13:30 CST）。stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 要到 2026-11-27 13:30 CST。阶段类型未变、规则未见变化，只是仍 LIVE 与进度推进。MUST 本页仅见上轮已记过的 23:30:29 CST 短回复。R2198 已因确认开铸通知。
- **deMiners @deMinersNft：不重推。** 付费公售仍 2026-11-26 00:30:04 CST 起、0.0002 ETH，OpenSea 时间表未改（activeDropStage 仍是 SIGNED_PRESALE stageIndex=2 至 00:30:04 CST）。核验时（约 00:10–00:16 CST）公售尚未开始。OG 免费 mint 仍 LIVE 至同一时刻。OpenSea API 528/3333（drop 528；R2199 API 527 / drop 528）、持有 143、地板 0.00035 ETH。R2197 已发付费公售首次 ≤2h。未因“即将到点”单独重推。
- **不提前告警** 2hourfun / Shielded Wizards 公售（均为 2026-11-26 05:00 CST，首次 ≤2h 约 03:00 CST）。extract 假 LE2H（如 rpcCheckedAt）已忽略。ORIPA 2h 窗已结束，不重推。
- **Fueltender @fueltenderagent：不重推。** R2199 已通知 $TENDER 上线 Pons。本轮续见 00:00:03 CST 官帖称任何项目今天可在 Robinhood Chain 开 tank，以及更早的 Crew pass / burn / refuel 续帖。官网仍展示同一 CA。上线后产品续更，无实质变化。
- **AGX @Agx_bsc：不重推。** 官网仍写演示版、合约尚未部署；首期进度仍 0/5,000（总进度展示 0/2,000,000），T1 仍 3 USDT/份。三份地址在 BSC 上仍有 bytecode，与「尚未部署」文案仍不一致，未确认开铸 LIVE，不是免费 mint。
- 库内进度（无实质变化或不构成单独告警，不重推）：TRIFORGE 链上 680/3333（R2199 662），claims 25（R2199 24），付费预售 lpTotalMinted=1；F0B90B 355/10000（R2199 336），mintOpen=true；Antopia 6253/8888（持平）、免费额度仍满；The Jacket 209/777（持平）、持有 133、地板 0.61 USDG（R2199 为 1.0 USDG，二级市场价格）；VALORIX Hero Cards 仍 11、fillSold=0/5500，MUST 再见到 23:46:29 CST 重申规则官帖。

## discordPeekDeferred

- `/tmp/r2200/discord_peek.json` 已存在并合并进 `meta.discordAlphaPeek`。
- loginOk=false，loginWall=true，channelsPeeked=false，items=0。`discordPeekDeferred=true`。attemptedAt `2026-11-26 00:05:02 CST`。四频道 lastSeen 未改。

## 失败 / 限制

- X 搜索 15/15 成功，errors=[]。dsFallback=false。MUST_OFF deferred（tight，未跑）。
- 全部 15 次均 `write_to_file` 直存。
- MUST_WIN 及多条 KW/MEN/24h 有 next_token，按规则未翻页。因此 @deMinersNft / @twohourfun / @2hourfun / @ShieldedWizBTC / @TheJacket_NVDA / @F0B90Bclub / @antopia_xyz / @TriForgeAgent / @Agx_bsc 未出现在 MUST_WIN 本页（本页被 Fueltender / Agent Cards / VALORIX / Ugly Puggies 占满）。改用 OpenSea / 官网 / 公共 RPC 核验，未额外读 X。
- OpenSea `/drop` 会落到 collection 页，旧 `"drop":` 抽取失败；已从合集 HTML 中的转义 SeaDrop JSON 解析 mintStatus/stages（ugly / deminers / jacket 均成功）。
- agent.cards 本轮超时；flybrainterminal.fun HTTP 500 / HTTPS SSL EOF；thewishlist.site 本轮 SSL EOF。playagentcards.com/mint、agx.98stay.com、fueltender.agency、公共 BSC RPC 与 Triforge RPC 成功。
- 未打开 Discord/浏览器，未改 `/workspace/early-scout/data.json`（mtime 仍为 2026-11-25 23:57:01 CST），未 git commit/push。

## notify

- **notify=true**
- 原因：Agent Cards @agentcardshq 确认付费 AGENTMINT 已开铸（fill 售罄、池已开、仍可按池价续铸）；不是免费 mint。本轮无新收录。
- namedFreeMintOrRegistration：无
- namedPaidLe2h：无
- dsFallback：false
- alertMessage：

```
R2200：@AgentCardsHQ 确认付费 AGENTMINT 已开铸：5,000 份 fill 以 0.0018 BNB 在 20 分钟内售罄（23:20 CST），537 个 Agent ID；PancakeSwap 池已开，错过 fill 仍可按池价 99% 继续铸。官网 playagentcards.com/mint 核到 phase=open、fillSold=5000/5000，后又铸 297 份，合计 5,297/1,007,493，现价约 0.00198 BNB（约 $1.06）；合约 0xA013Ad2D38fec3A2851cec573F20D8792e23267f。不是免费 mint，也不是免费登记或免费 LIVE。Ugly Puggies 免费 mint 与 deMiners 付费公售均未变，不重推。面板：https://reboot7454.github.io/early-scout/ 本号不自动 mint。
```

## 写盘摘要（供父进程）

- dry-run：`/tmp/r2200/data.json`
- `meta.round2200Added` = 顶层 `newThisRound` = `[]`
- ufCursor **2101 @woodlandz_xyz**，uf_total 2423，wrap=false
- mentionsCoverage / mentionsNext（下轮 Starknet / squeek / STARX）、silentLane=打新、silentNext=挖矿 已写
- Canton / Glaze / TokenWorks lastChecked 软刷到本轮
- 已合并 discord_peek.json，`discordPeekDeferred=true`
- 工作区 `/workspace/early-scout/data.json` 未改（mtime 仍为 2026-11-25 23:57:01 CST）
