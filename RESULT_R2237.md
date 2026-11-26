# 早期打新雷达 RESULT_R2237

- lastScout: 2026-11-26 18:49:35 CST
- notify: false
- alert: （本轮不推送）
- newAdmits: 无
- liveFlips: 无
- firstLe2h: []
- xReads: 26（main 25 + silent 1 + extra 0）
- remainingBefore: 452
- remainingAfter: 426
- mode: ample（remainingBefore 452 ≫ 200；计划 softCap 18 / minSpend 18 / silentCap 2）；未砍栏，实际 xReads=26 是为保十栏+mentions+瘦栏 24h 全覆盖
- 十栏关键词: 全跑（含 KW_GAPS）。30m：LZ=0 TAPE=24 GIWA=12 DOGE=8 BTC=1 STARK=3 MINT=23 MINE=1 PAD=25 GO=25 ELY=14 GAPS=19
- userFollow: 已刷完。cursor 1347 @wilmacartemv2f → 1397 @Conquerors_Dao（end @soar_ag，wrap=false，kept 50，NF_skip=0）。UF1=0 UF2=0 UF3=0，无打新。
- mentions: GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25 触顶，MEN_TAPE=6，MEN_LZ24=25 触顶，MEN_ELY=25 触顶）
- mentionsNext: DogeEVM / BTC / Starknet / pads+squeek+STARX
- silent: 打新（has:mentions fallback，n=25 触顶，sentToReview=0，admitted=0）；silentNext: 挖矿
- 瘦栏 24h 补搜: LayerZero=23、BTC=25、Starknet=25（30m <5）。跳过 Tape/GIWA/DogeEVM（30m 已够）。
- MUST: MUST_WIN=25（触顶，未翻页）、MUST_WIN2=5、MUST_OFF=0。@starx_xlayer 本轮未 getUsers（长期 NF skip）。缺 referenced tweet 未重读。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek HTTP 401 api key invalid；判断/文案为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19–22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 窗口与在库刷新

- **QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）**：静态页仍 PRE-LAUNCH，公共 BSC RPC 再确认 mintOpen()=true、paused()=false、startTime=2026-11-26 18:00:00 CST；token totalSupply=198,000,000 = 12 次免费领取，约 12/555（R2236 为 7/555）。门费 0.0001 BNB，每 Agent ID 最多 2 次。MUST 未见新官帖、暂停或售罄。7/555→12/555 只是进度，不重推。合约未核实。
- Lamoryant：mint 页仍 0/1,356，倒计时按 JS 占位；BSC/ETH RPC 未核到 mintOpen（合约在 Robinhood Chain）。MUST 16:22 CST 官帖仍写 11:00 UTC / 19:00 CST 开铸，未见改期。R2234 已首次 ≤2h，未开铸，不重推。
- Crawlers Agent：官网/pages.dev 仍 MINT · OPENING SOON / LOCKED，开铸仍 2026-11-26 20:00 CST，付费 0.004 BNB。MUST 17:07 CST 口径未改；18:24 CST 新帖只解释无 Connect Wallet。R2236 已首次 ≤2h，未开铸，不重推。不是免费 mint。
- Wildlife Universe：官网仍 Launch 26 November 2026 · 7:00 PM IST（21:30 CST），OpenSea 供应/持有仍 0。官帖称 Today is the day / game opens at 1:30 PM UTC，不是已开铸 LIVE，也不是改期。写盘 2026-11-26 18:49:35 CST，距首窗 约 2.7h，未到首次 ≤2h，不重推。
- Vicehood：OpenSea vchood 供应仍 0，首窗仍 2026-11-27 01:00 CST，未到首次 ≤2h，不重推。
- Ugly Puggies：仍 Minting now，API 563/777（R2236 为 562）、持有 359、地板 0.0001 ETH，只是进度，不重推。
- 2hour.fun：窗关，traderCount=43，下一窗仍 2026-11-27 05:00–07:00 CST，不重推。
- RuninAI：日窗宣传口径未变，今日 20:00 CST 是重复日窗，R2226 已提醒，不重推。
- Hamste CombatHQ：仍 WL Launching Soon，未见开铸，不重推。
- TRIFORGE：903/3333（沿用值 873），claims 43，未暂停，预售仍开至 12-02。Antopia 6359/8888。F0B90B 552/10000。Shielded Wizards 150/3333。The Jacket 214/777。Guns of the Hood 112/10000。均为小幅进度，不重推。
- Canton/Glaze/TokenWorks lastChecked 已刷新，无新 admit。

## 盲捞未收录

- @Pangomeme：上轮已跳过。本轮自报 $PANGO LIVE ON MONTRA 并给出 CA 0xae450058fd59ca9c2305c7628d0b9c1acd0c53d5，但仍无官网、1 粉、无站点互证，不是免费 mint，不重复收录。
- @QQAgent_BNB：QQAI 后建姊妹/仿号，已记在 qqai 卡上，不另开新卡。
- @FamiliarsAI：仅作为 @RuninAI_com 回复对象出现，本轮无自身官帖。官网 https://familiars-app.pages.dev 与官推互链，但文案同时写 Altar opens soon 与 Sold out，未核到可操作的免费 mint LIVE，未另开 X 查询，未收录。
- @ShieldSuite_：X Layer 工具工作室，官帖推 Voxro 付费收件箱已 LIVE，不是打新/免费 mint/发射台，不收录。
- @justdukfun / @Oathlydotai：本轮无新证据，不重复收录。
- AURA Spirits / @ThebeliefNFT / @RebelianRH 等免费 mint 仅见第三方转述或已在库，本轮未核到需新收录的官号+站点互证，未另开 X 查询。
- @Kimchifunxyz / @GIWAForg：仅出现在第三方 GIWA 生态盘点，本轮无官帖，未另开查询，未收录。
- 空轮芯片未造。普通新卡未 focus。收藏未改。

## 面板

已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
