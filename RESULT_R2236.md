# 早期打新雷达 RESULT_R2236

- lastScout: 2026-11-26 18:16:46 CST
- notify: true
- alert: QQAI 免费 mint 链上 LIVE（约 7/555）+ Crawlers Agent 首次 ≤2h
- newAdmits: 无
- liveFlips: qqai 免费 mint 已开铸 LIVE（链上 mintOpen=true，totalSupply=115,500,000 = 7×16,500,000）
- firstLe2h: [{"id": "crawlers-agent", "handle": "@CrawlersAgent", "label": "Crawlers Agent 付费开铸", "at": "2026-11-26 20:00:00 CST", "hours": 1.72}]
- xReads: 27（main 26 + silent 1 + extra 0）
- remainingBefore: 479
- remainingAfter: 452
- mode: pace（softCap 18 / minSpend 18 / silentCap 2）；remaining ≫ 200，未砍栏，实际花费与软顶不一致是为保十栏+薄栏 24h+mentions 全覆盖
- 十栏关键词: 全跑（含 KW_GAPS）。30m：LZ=1 TAPE=16 GIWA=24 DOGE=2 BTC=2 STARK=1 MINT=25 MINE=0 PAD=25 GO=25 ELY=11 GAPS=25
- userFollow: 已刷完。cursor 1297 @makehoodxyz → 1347 @wilmacartemv2f（end @CashmereLabs，wrap=false，kept 50，NF_skip=0）。UF1=0 UF2=1 UF3=0；UF2 仅 @oxano_io CMC 互动，无打新。
- mentions: DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=3，MEN_BTC=25 触顶，MEN_STARK=3，MEN_PADS=25 触顶，含 @squeekchain @NutshellMarkets @starx_xlayer）
- mentionsNext: GIWA / Tape / LayerZero / Elysium
- silent: Tape（has:mentions fallback，n=1，sentToReview=0，admitted=0）；silentNext: 打新
- 瘦栏 24h 补搜: LayerZero=23、DogeEVM=25、BTC=25、Starknet=24（30m <5）。跳过 Tape/GIWA（30m 已够）。
- MUST: MUST_WIN=25（触顶，有一条 referenced tweet 缺失，未重读）、MUST_WIN2=6、MUST_OFF=2。@starx_xlayer 本轮未 getUsers（长期 NF skip）。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek HTTP 401 api key invalid；判断/文案为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19–22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 窗口与在库刷新

- **QQAI（@QQAI_BNB）免费 mint 已 LIVE（本轮必须提醒）**：静态页仍 PRE-LAUNCH，但公共 BSC RPC 确认 mintOpen()=true、paused()=false、startTime=2026-11-26 18:00:00 CST；token totalSupply=115,500,000 = 正好 7 次免费领取，约 7/555。门费 0.0001 BNB，每 Agent ID 最多 2 次。MUST 未见新官帖。合约未核实。R2232 已首次 ≤2h，本轮是开铸状态翻转，不是重复 ≤2h。
- **Crawlers Agent（@CrawlersAgent）首次进入 ≤2h（本轮必须提醒）**：官网/pages.dev 仍 MINT · OPENING SOON / LOCKED，开铸仍 2026-11-26 20:00 CST（12:00 UTC），付费 0.004 BNB，6000 份，仅限 Agent ID，24 小时窗。MUST 17:07 CST 官帖口径未改。不是免费 mint，不是已开铸 LIVE。
- Lamoryant：mint 页仍 0/1,356，倒计时按 JS 占位，RPC 未核到 mintOpen，开铸仍 19:00 CST。R2234 已首次 ≤2h，不重推。
- Wildlife Universe：OpenSea 仍 Minting soon、供应 0，首窗仍 21:30 CST，未到首次 ≤2h，不重推。
- Vicehood：OpenSea 仍 Minting soon、供应 0，首窗仍 2026-11-27 01:00 CST，不重推。
- Ugly Puggies：仍 Minting now，API 562/777（R2235 页记 558）、持有 359、地板 0.0001 ETH，只是进度，不重推。
- 2hour.fun：窗关，traderCount=43，下一窗仍 2026-11-27 05:00–07:00 CST，不重推。
- RuninAI：日窗宣传口径未变，今日 20:00 CST 是重复日窗，R2226 已提醒，不重推。
- Hamste CombatHQ：仍 WL Launching Soon，未见开铸，不重推。
- ROCKZERO / 其余软债与进度卡：无新核到的改期，不重推。

## 盲捞未收录

- @justdukfun（约 0.07 天，23 粉，http://duk.fun）：站点自称 meme coin，CA soon，未给出合约，不是免费 mint / 已开铸，未收录。
- @Oathlydotai / @Pangomeme：上轮已跳过（无互证站点或已判），本轮无新站点证据，不重复收录。
- AURA Spirits「Free mint is LIVE」仅见第三方转述，本轮未核到官号+站点互证，未另开 X 查询，未收录。
- 空轮芯片未造。普通新卡未 focus。收藏未改。

## 面板

已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
