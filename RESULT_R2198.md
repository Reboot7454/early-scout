# R2198 X-radar RESULT

- Round: **R2198**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-25 23:21:56 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2198/RESULT_R2198.md`、`/tmp/r2198/notify.json`、`/tmp/r2198/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2198/apply_r2198.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2198/data.json.src APPLY_DRY_OUT=/tmp/r2198/data.json` 已成功）

## X 预算与检索

- **remainingBefore=229/1000**（首搜 UF1 后脚注 228/1000，故开火前为 229，与 R2197 remainingAfter 一致）
- **remainingAfter=200/1000**
- **xReads=29**（main 28 + silent 1）
- **十栏关键词全部跑完**（LZ / TAPE / GIWA / DOGE / BTC / STARK / MINT / MINE / PAD / GO / ELY + KW_GAPS，均为 30m）
- **Override：** remaining >> 200，按用户额度充裕时不得砍栏的规则，跑满 queries.json 已排好的增量计划（25 主搜 + 1 静号），并在薄栏 30m KW <5 时加 24h 回看。与 R2185–R2197 相同 override。已写入 `meta.xBudgetMode=pace-override-full`
- 未对已知 NF `@starx_xlayer` 做 from: 重试；本轮 MEN_STARX 为允许的 mentions。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 0 | 228 |
| UF2 | 30m | 0 | 227 |
| UF3 | 30m | 0 | 226 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 225 |
| MUST_WIN2 | 24h | 25（触顶） | 224 |
| MUST_WIN3 | 24h | 23（有 next_token，未翻页） | 223 |
| MUST_WIN4 | 24h | 21（有 next_token，未翻页） | 222 |
| MUST_OFF | 30m | 5 | 221 |
| KW_LZ | 30m | 1 | 220 |
| KW_TAPE | 30m | 25 | 219 |
| KW_GIWA | 30m | 25 | 218 |
| KW_DOGE | 30m | 6 | 217 |
| KW_BTC | 30m | 2 | 216 |
| KW_STARK | 30m | 3 | 215 |
| KW_MINT | 30m | 25 | 214 |
| KW_MINE | 30m | 3 | 213 |
| KW_PAD | 30m | 23 | 212 |
| KW_GO | 30m | 25 | 211 |
| KW_ELY | 30m | 19 | 210 |
| KW_GAPS | 30m | 22 | 209 |
| MEN_DOGE | 24h | 9 | 208 |
| MEN_BTC | 24h | 25（触顶） | 207 |
| MEN_STARK | 24h | 4 | 206 |
| MEN_SQUEEK | 24h | 0 | 205 |
| MEN_STARX | 24h | 0 | 204 |
| SILENT_BTC | 24h | 11 | 203 |
| KW_LZ_24 | 24h | 24 | 202 |
| KW_BTC_24 | 24h | 25（触顶） | 201 |
| KW_STARK_24 | 24h | 25（触顶） | 200 |

## UF 分片 / 光标

- 本轮分片：cursor **1961 @lpstationxyz** 起 50 个到 **@yumirbh**（UF3 短尾巴），三次 from:，全部 0 帖
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2011 @goodlauncher**，uf_total 2423（源 2422，因新卡 @Agx_bsc 挂入 userFollowWatch +1），wrap=false

## Mentions 与静号

- **本轮 mentions：** DogeEVM（MEN_DOGE 9）/ BTC（MEN_BTC 25 触顶）/ Starknet（MEN_STARK 4）/ squeek（MEN_SQUEEK 0）/ STARX（MEN_STARX 0）
- **下轮 mentions 轮转：** pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- **本轮静号：** BTC（2198 % 11 = 9；SILENT_BTC 11 条）
- **下轮静号：** Starknet

## 薄栏 24h 回看

- 30m 命中：KW_LZ=1、KW_BTC=2、KW_STARK=3，均 <5；KW_TAPE=25、KW_GIWA=25、KW_DOGE=6，均 ≥5
- **做了：** KW_LZ_24（24）、KW_BTC_24（25 触顶）、KW_STARK_24（25 触顶）
- **没做：** KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）

## 新收录（DeepSeek 打分，dsFallback=false）

- **AGX @Agx_bsc**（https://agx.98stay.com）：建号 2026-11-23 10:41:31 CST，1012 粉 / 5 帖。官网 HTTPS 200，与官推互证。自称 BNB Chain 上仅限 .ai Agent ID 的铸造台，开池前 T1 3 USDT/份，首期 5,000 份。官网写演示版、合约尚未部署，进度 0/5,000；bio 也写 Contract not live yet。官帖飞轮文案称 contracts verified on BscScan，与「尚未部署」不一致，记为风险。**不是免费 mint / 免费登记 / LIVE。** DeepSeek overall=56，admit=true。已挂 userFollowWatch + agentPadWatch + bnAgentWatch，focus=false。

## 看见但未收录

- **@LongyuNetwork**（https://longyu.network）：约 4.4 天、3070 粉，官网与号互证，自称可挖矿、结算在 BNB Chain 的 L2。本轮仅在 KW_GAPS 被 @maulana00778417 提及（good aidrop），无该号原创帖，未再读 X，未收录。
- **@stargaze_fit**（https://www.stargaze.fit）：约 6.2 天、12 粉，站点互证，自称 Base/Hyperliquid 代币筛查工具并介绍 $STGENT。DeepSeek admit=false（无铸造窗）。
- **@Denytholelp / @LedgerGank / @giwa_lauchpad** 等极新或无官网号：喊单、提及或空资料，未收录。
- **@zerrrxyz**：提及 Bitcoin RGB 白名单与 300 free mint，非可核验官号窗口，未收录。

## 必须通知的 ≤2h / 库内刷新

- **Ugly Puggies @uglypuggies：必须通知。** 本轮开火已过 23:00 CST。23:01 CST 官帖（https://x.com/uglypuggies/status/2125605878850298248）称 Mint is lived!!，自称 777 份免费 mint、Robinhood Chain、走 OpenSea。公开 collection+stats：CA 0xe2be23fbffe892feb3677341765847b9309663c2，30/777（上轮 0/777），持有 1，地板 0。合集 HTML SeaDrop JSON：mintStatus=**MINTING**（上轮 MINTING_SOON），erc721.totalSupply=30/777，activeDropStage stageIndex=1（SIGNED_PRESALE 23:00–23:30 CST）。页面可见 “Minting now”。R2195 已发首次 ≤2h，本轮因确认开铸再通知。不要把已否定的非官方 21:00 CST 窗当成开铸时间。
- **Agent Cards @agentcardshq：未见开铸确认，不重推。** 翻印窗仍是 23:00 CST 的 AGENTMINT（不写成免费 mint）。本轮 MUST 24h 未见官帖（MUST_WIN3 23 条触顶未翻页，未额外补读 X）。R2195 已发首次 ≤2h。
- **deMiners @deMinersNft：不重推。** 付费公售仍 2026-11-26 00:30:04 CST 起、0.0002 ETH，OpenSea 时间表未改（activeDropStage 仍是 SIGNED_PRESALE stageIndex=2 至 00:30:04 CST）。OG 免费 mint 仍 LIVE 至同一时刻。OpenSea 527/3333（R2197 515）、持有 140、地板 0.00035 ETH。R2197 已发付费公售首次 ≤2h。
- **不提前告警** 2hourfun / Shielded Wizards 公售（均为 2026-11-26 05:00 CST）。extract 把 2hourfun teaserAtUTC 误标成 23:00 CST 假 LE2H，已忽略。ORIPA 2h 窗已结束，不重推。
- 库内进度（无实质变化，不重推）：TRIFORGE 链上 647/3333（R2197 610），claims 23；F0B90B 332/10000（R2197 308），mintOpen=true；Antopia 6253/8888、免费额度仍满，本轮有游戏排行榜/USDT 奖励官帖；The Jacket 209/777（R2197 207）、持有 133、地板 1.0 USDG；VALORIX Hero Cards 仍 11、fillSold=0/5500；Fueltender 22:45 CST 官帖仍称 TENDER minutes away，官网 CA 仍写 at launch；Mopao 22:06:42 CST 官帖称 $MOPAO is live，官网静态页仍未见 CA，R2197 已提醒发射预告。

## discordPeekDeferred

- `/tmp/r2198/discord_peek.json` 已存在并合并进 `meta.discordAlphaPeek`。
- loginOk=false，loginWall=true，channelsPeeked=false，items=0。`discordPeekDeferred=true`。attemptedAt `2026-11-25 23:08:38 CST`。四频道 lastSeen 未改。

## 失败 / 限制

- X 搜索 29/29 成功，errors=[]。dsFallback=false。
- MUST_WIN / MUST_WIN2 / MUST_WIN3 / MUST_WIN4 及多条 KW/MEN/24h 有 next_token，按规则未翻页。因此 @agentcardshq / @deMinersNft 未出现在 MUST_WIN3 本页，改用 OpenSea 核验，未额外读 X。
- OpenSea `/drop` 会落到 collection 页，旧 `"drop":` 抽取失败；已从合集 HTML 中的转义 SeaDrop JSON 解析 mintStatus/stages（ugly / deminers / jacket 均成功）。
- flybrainterminal.fun HTTP 500 / HTTPS SSL EOF；thewishlist.site 本轮 SSL EOF。公共 BSC RPC 与 Triforge RPC 成功。
- 未打开 Discord/浏览器，未改 `/workspace/early-scout/data.json`，未 git commit/push。

## notify

- **notify=true**
- 原因：Ugly Puggies 确认免费 mint 已开铸 LIVE；新收录 AGX @Agx_bsc
- namedFreeMintOrRegistration：`uglypuggies`（AGX 不是免费 mint/登记）
- namedPaidLe2h：无（deMiners 付费公售首次 ≤2h 已在 R2197 发出）
- dsFallback：false
- alertMessage：

```
R2198：Ugly Puggies @uglypuggies 官宣免费 mint 已开铸 LIVE。23:01 CST 官帖称 Mint is lived!!，777 份、Robinhood Chain、走 OpenSea；合集 SeaDrop mintStatus=MINTING（上轮仍是 MINTING_SOON / 0/777），30/777，当前 SIGNED_PRESALE 至 23:30 CST。R2195 已发首次 ≤2h，本轮因确认开铸再通知。新收录 AGX @Agx_bsc（https://agx.98stay.com）自称 BNB Chain .ai Agent ID 铸造台，官网与官推互证，官网写演示版、合约尚未部署，开池前 T1 3 USDT/份，不是免费 mint LIVE。Agent Cards @agentcardshq 翻印窗仍是 23:00 CST 的 AGENTMINT，本轮 MUST 未见官帖、未见开铸确认，R2195 已发首次 ≤2h，不重推、不写成免费 mint。deMiners @deMinersNft 付费公售仍 2026-11-26 00:30:04 CST、0.0002 ETH，OpenSea 时间表未改，R2197 已发首次 ≤2h，不重推。2hourfun / Shielded Wizards 公售均为 2026-11-26 05:00 CST，不提前告警。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
```

## 写盘摘要（供父进程）

- dry-run：`/tmp/r2198/data.json`
- `meta.round2198Added` = 顶层 `newThisRound` = `['agx']`
- ufCursor **2011 @goodlauncher**，uf_total 2423，wrap=false
- mentionsCoverage / mentionsNext、silentLane=BTC、silentNext=Starknet 已写
- Canton / Glaze / TokenWorks lastChecked 软债刷到本轮
- 已合并 discord_peek.json，`discordPeekDeferred=true`
- 工作区 `/workspace/early-scout/data.json` 未改（mtime 仍为 2026-11-25 22:51 CST）
