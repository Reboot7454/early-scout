# R2201 X-radar RESULT

- Round: **R2201**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-26 00:50:06 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170（保持，未改）
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2201/RESULT_R2201.md`、`/tmp/r2201/notify.json`、`/tmp/r2201/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2201/apply_r2201.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2201/data.json.src APPLY_DRY_OUT=/tmp/r2201/data.json` 已成功）

## X 预算与检索

- **remainingBefore=156/1000**（首搜 UF1 后脚注 155/1000，故开火前为 156；与 R2200 直播脚注 remainingAfter 一致。面板旧 `meta.remaining=286` 已弃用，本轮改写为 live remainingAfter。）
- **remainingAfter=143/1000**
- **xReads=13**（main 12 + silent 1；按已排 queries.json 13 次照跑，无计划外搜索）
- **十栏覆盖：** 六个薄栏独立 30m KW（LZ / TAPE / GIWA / DOGE / BTC / STARK）+ 核心栏与 GAPS 合并为一次 KW_CORE（30m）。MUST_OFF 本轮 tight 已跳过（官号 30m 延期），未补跑（live remainingBefore=156，未达 ≥250 阈值）。
- **mode=tight** / softCap=10 / minSpend=10 / silentCap=1。已写入 `meta.xBudgetMode=tight`。计划 13 次略高于 softCap 10，按已排 queries.json 照跑，未 override-full，未再加计划外搜索。
- 未对已知 NF `@starx_xlayer` 做 from: 重试；本轮 mentions 子集不含 MEN_STARX。search_users 仍不可用，静号用 mentionQuery 兜底。
- 有 next_token 的搜索均未翻页。同一 handle 本轮只读一次。

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 2（有 next_token，未翻页） | 155 |
| UF2 | 30m | 2（有 next_token，未翻页） | 154 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 153 |
| KW_LZ | 30m | 0 | 152 |
| KW_TAPE | 30m | 23（有 next_token，未翻页） | 151 |
| KW_GIWA | 30m | 25（触顶） | 150 |
| KW_DOGE | 30m | 14（有 next_token，未翻页） | 149 |
| KW_BTC | 30m | 9（有 next_token，未翻页） | 148 |
| KW_STARK | 30m | 1（有 next_token，未翻页） | 147 |
| KW_CORE | 30m | 25（触顶） | 146 |
| MEN_STARK | 24h | 6（有 next_token，未翻页） | 145 |
| MEN_SQUEEK | 24h | 0 | 144 |
| SILENT_MINE | 24h | 2（有 next_token，未翻页） | 143 |

## UF 分片 / 光标

- 本轮分片：cursor **2101 @woodlandz_xyz** 起 40 个到 **@jesterdotfun**，两次 from:（UF1 24 + UF2 16）
- UF1：2 帖（@SleeperDragons 回复、@ApeDenRH “Hood Morning”）；UF2：2 帖（@smooveoffsol 两条 $SMOOVE 相关）
- 无新官号窗口
- uf_skip / nf 跳过：无
- 写盘后 ufCursor **2141 @blackwater_z26**，uf_total 2426（新挂 3 个官号在名单末尾，cursor 指向不变），wrap=false

## Mentions 与静号

- **本轮 mentions：** Starknet（MEN_STARK 6）/ squeek（MEN_SQUEEK 0）
- **下轮 mentions 轮转：** 先补 STARX，再回到 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest
- **本轮静号：** 挖矿（2201 % 11 = 1；SILENT_MINE 2 条）
- **下轮静号：** 台子/Meme
- **silentAccounts：** ran=true，seen=2，sentToReview=0，admitted=0，skipped=2（mentionQuery 兜底；2 条均为上下文「GPU mine is…」闲聊，无官号级新窗口）

## 薄栏 24h 回看

- 30m 命中：KW_LZ=0、KW_STARK=1，均 <5；KW_TAPE=23、KW_GIWA=25、KW_DOGE=14、KW_BTC=9，均 ≥5
- 主计划跑完后 remainingToday=143，**低于**大致 ≥150 的门槛，**未做**薄栏 24h 补搜
- **没做：** KW_LZ_24（30m 虽为 0 且优先），KW_STARK_24 / KW_BTC_24。KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）。未把肥栏（尤其 KW_CORE）改成 24h。未为 24h 补搜翻页。

## 新收录（DeepSeek 打分，dsFallback=false）

`meta.round2201Added` = 顶层 `newThisRound` = `['chainbitz', 'cheoma-yield', 'cartoon-money']`。三卡均 focus=false，已同时挂 userFollowWatch（Cheoma 另挂 giwaWatch + miningWatch）。links 均写了 `x` 与 `twitter`。

- **Chainbitz @Chainbitz / https://www.chainbitz.xyz/**（打新，score=55）：建号 2026-09-28 04:24 CST，830 粉 / 17 帖。官网与官号互证，自称 10,000 pixel collectibles（Haunted Arcade），GTD 白名单需 Bitz Match 1,500 分后解锁申请。官网正文未见 free mint，无 CA、无明确链。不是免费 mint，也不是已确认免费登记或免费 LIVE。
- **Cheoma Yield @CheomaYield_xyz / https://www.cheomayield.xyz/**（挖矿，score=62）：建号 2026-07-21 14:37 CST，1,087 粉 / 138 帖。官网与官号互证，自称 GIWA Yield Layer（官号称 Backed by GIWA GASOK）。Wave 1 Pre-Deposit 已开：13% 固定利率 USDC，Sukuk-backed、托管 ADCB；积分/推荐空投。这是预存生息，不是 NFT mint，不是免费 mint，也不是免费登记。
- **Cartoon Money @JokerFaceCM / https://Cartoon-Money.com**（台子/Meme，score=42）：建号 2026-10-29 16:22 CST，128 粉 / 385 帖。官网与官号互证，自称 Solana Mainnet 上 own/launch/trade。官帖（https://x.com/JokerFaceCM/status/2125394121661546548，2026-11-25 09:00 CST）称 $CBUCKS Launch Day Dec 3rd 3pm EST（约 2026-12-04 04:00 CST）。未见 CA。不是免费 mint，也不是免费登记或免费 LIVE。

## 看见但未收录

- **@StylishLabss**：约 297 天、1,309 粉。仅见第三方 RT 其 FLASH GA，自称 3,333 NFT 即将登陆 Robinhood、FREE MINT。资料栏 OpenSea 是以太坊测试合集 BadTest（已 Minting now，945 items / 303 owners，og 写 unique test）。Robinhood 免费 mint 未核到官网/合约/开铸时间。DeepSeek skip（号龄偏长，窗口不像极早期，且免费 mint 未经官网核验）。
- **@0xstonkdad / Orbz**：约 19.8 天、524 粉。仍仅见第三方 @madamayo_ 转述 GTD 免费 mint（565 份）。未见官帖，未再读 X。与 R2200 相同，未收录。
- **@LawoftheAbyss / @CapricornH00D / @beavzclub / @VordaLaunch / @gamapadcom / @MMIX_io / @kangozro**：均为已收录项目的第三方转发或已知窗口，不新建卡。Capricorn 仅见第三方转述「取消 GTD/FCFS、改为 Public Mint」，未再读 X、未按已确认规则变化通知。
- **@LoLoCoding / Starknet.Build**：12 年 DevRel 个人号，产品是 Starknet 上的自然语言应用生成等待名单（tally 表），不是 mint/发射台窗口，未收录。
- **@Ekha0692 / GiwaCurve**：2 粉个人号，称在 GIWA Sepolia 用 Ammora SDK 做了测试网 launchpad，非正式官号窗口，未收录。
- **@Pax_Gothamista**：仅见第三方 GTD/FCFS 赠票，无官号资料，未再读 X，未收录。
- **@giwa_lauchpad**：6 天、1 粉、空资料 typo 号，未收录。
- 静号 2 条闲聊，未送审。

## 必须通知的 ≤2h / 库内刷新

- **deMiners @deMinersNft：公售已按点开出，不重推。** OpenSea 合集 HTML SeaDrop：时间表未改（SIGNED_PRESALE stageIndex 2 仍至 2026-11-26 00:30:04 CST；PUBLIC_SALE 仍 00:30:04–2026-11-28 00:30:04 CST）。核验时 activeDropStage 已切到 **PUBLIC_SALE（stageIndex=0）**，mintStatus 仍 **MINTING**。OG 免费 mint 已在同一时刻按点结束，不再 LIVE。OpenSea 531/3333（drop 531；R2200 为 528），持有 144，地板 0.000349 ETH（上轮 0.000349999）。合集标题「0.0003 ETH」是地板约数，不是改价证据；SeaDrop JSON 本轮仍无价格字段，官网未标价；沿用已核验公售价 0.0002 ETH，未见改价/改期/取消。MUST 本页未见 @deMinersNft（被 Fueltender / Agent Cards 等占满，未翻页）。R2197 已发付费公售首次 ≤2h。只是按点开售且未见必须通知的新事实，不单独重推。
- **Ugly Puggies @uglypuggies：仍 LIVE，不重推。** SeaDrop mintStatus 仍 **MINTING**，erc721.totalSupply=**243/777**（R2200 为 235/777；公开 API 241），持有 186，地板 0.000199 ETH。时间表未变：**activeDropStage 仍是 stageIndex=2 SIGNED_PRESALE** 至 2026-11-26 13:30 CST。stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 要到 2026-11-27 13:30 CST。MUST 仅见上轮已记过的 23:30:29 CST 短回复。R2198 已因确认开铸通知。
- **Agent Cards @agentcardshq：不重推。** 官网 `/api/mint/status` 仍 phase=open、fillSold=5000/5000，后又铸至 **5,427/1,007,493**（R2200 为 5,297；curveSold 427），现价仍约 **0.00198 BNB（约 $1.06）**，池内约 3.781 BNB。MUST 再见 00:07:15 CST 回购续帖（53.6M / 0.25 BNB 打入黑洞）以及上轮已通知的开铸/回购帖。R2200 已因确认开铸通知。本轮只是进度与回购续更，不是免费 mint，不重推。
- **不提前告警** 2hourfun / Shielded Wizards 公售（均为 2026-11-26 05:00 CST，首次 ≤2h 约 03:00 CST）。Shielded Wizards WL 免费铸仍按此前 LIVE 口径，本轮 MUST 未见该号，不因仍 LIVE 重推。
- **Fueltender @fueltenderagent：不重推。** MUST 本页 20/25 为该号产品续更（Orbit 2 / npm sponsor、telemetry 等）。R2199 已通知 $TENDER 上线。无新铸造窗口。
- **AGX @Agx_bsc：不重推。** 官网仍写演示版、合约尚未部署；三份地址在 BSC 上仍有 bytecode，与文案仍不一致，未确认开铸 LIVE，不是免费 mint。
- 库内进度（无实质变化或不构成单独告警，不重推）：TRIFORGE 链上 704/3333（R2200 680），claims 27（R2200 25），付费预售 lpTotalMinted=1；F0B90B 388/10000（R2200 355），mintOpen=true；Antopia 6253/8888（持平）、免费额度仍满；The Jacket 209/777（持平）、持有 133、地板 0.61 USDG；VALORIX Hero Cards 12（R2200 11），fillSold 仍 0/5500，MUST 再见到已记过的 23:46:29 CST 重申规则官帖。

## discordPeekDeferred

- `/tmp/r2201/discord_peek.json` 已存在（平行 Discord Peek 产物），已合并进 `meta.discordAlphaPeek`，供父进程复核。
- loginOk=false，loginWall=true，channelsPeeked=false，cardsRead=0。`discordPeekDeferred=true`。attemptedAt `2026-11-26 00:35:41 CST`。四频道 lastSeen 未改。本执行器未打开 Discord/浏览器。

## 失败 / 限制

- X 搜索 13/13 成功，errors=[]。dsFallback=false。MUST_OFF deferred（tight，未跑）。
- 全部 13 次均 `write_to_file` 直存。
- MUST_WIN 及多条 KW/MEN 有 next_token，按规则未翻页。因此 @deMinersNft / @twohourfun / @2hourfun / @ShieldedWizBTC / @TheJacket_NVDA / @F0B90Bclub / @antopia_xyz / @TriForgeAgent / @Agx_bsc 未出现在 MUST_WIN 本页（本页被 Fueltender 20 + Agent Cards 3 + VALORIX 1 + Ugly Puggies 1 占满）。改用 OpenSea / 官网 / 公共 RPC 核验，未额外读 X。
- OpenSea `/drop` 会落到 collection 页，旧 `"drop":` 抽取失败；已从合集 HTML 中的转义 SeaDrop JSON 解析 mintStatus/stages（ugly / deminers / jacket 均成功）。SeaDrop 对象不含价格字段，deMiners 公售价本轮无法从页面直接重读，未见改价证据。
- flybrainterminal.fun HTTP 500 / HTTPS SSL EOF；thewishlist.site 本轮 SSL EOF。OpenSea collection API 对 badtestofc 返回 401，已用合集 HTML 核验。playagentcards.com/mint status、agx.98stay.com、fueltender.agency、公共 BSC RPC 与 Triforge RPC 成功。
- 未打开 Discord/浏览器，未改 `/workspace/early-scout/data.json`（mtime 仍为 2026-11-26 00:19:37 CST，sha256 前缀与 data.json.src 一致），未 git commit/push。

## notify

- **notify=true**
- 原因：本轮新收录 3 项（真新）。三者都不是自称免费 mint / 免费登记 / 免费 LIVE，告警里已逐个点名并写明。deMiners 付费公售已按原时间表开出，不因此单独重推。Ugly Puggies 与 Agent Cards 无实质变化，不重推。
- namedFreeMintOrRegistration：无
- namedPaidLe2h：无
- dsFallback：false
- alertMessage：

```
R2201：新卡 Chainbitz @Chainbitz（10k 像素、GTD 白名单需打游戏申请、官网未写免费 mint）、Cheoma Yield @CheomaYield_xyz（GIWA 预存生息已开、不是免费 mint）、Cartoon Money @JokerFaceCM（$CBUCKS 自称 12-03 15:00 EST 开盘、未见 CA、不是免费 mint）均不是免费 mint/免费登记/免费 LIVE。deMiners 付费公售已按 2026-11-26 00:30:04 CST 原时间表开出，OG 免费 mint 同时按点结束，未见改价，不重推；Ugly Puggies 与 Agent Cards 无实质变化。面板：https://reboot7454.github.io/early-scout/。本号不自动 mint。
```

## 写盘摘要（供父进程）

- dry-run：`/tmp/r2201/data.json`
- `meta.round2201Added` = 顶层 `newThisRound` = `['chainbitz', 'cheoma-yield', 'cartoon-money']`
- ufCursor **2141 @blackwater_z26**，uf_total 2426，wrap=false
- mentionsCoverage / mentionsNext（下轮先补 STARX，再 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest）、silentLane=挖矿、silentNext=台子/Meme 已写
- Canton / Glaze / TokenWorks lastChecked 软刷到本轮
- 已合并 discord_peek.json，`discordPeekDeferred=true`
- 工作区 `/workspace/early-scout/data.json` 未改（mtime 仍为 2026-11-26 00:19:37 CST）
