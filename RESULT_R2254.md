# 早期打新雷达 R2254

- lastScout: 2026-11-27 03:08:05 CST
- notify: true
- alert: 【早期打新雷达 R2254】1）Vicehood（@vicehood_rh）免费公售首次进入 <=2h：05:00 CST 开公售，距约 1.87h。当前仍为 01:00-04:00 CST 签名窗（免费 mint 仍 LIVE）。链上 2284/3333，OpenSea 供应 2284、持有 1961、地板 9.19e-05 ETH。R2250 已提醒开铸，本轮按公售首次 <=2h 提醒。铸页 https://opensea.io/collection/vchood  官网 https://www.vicehood.xyz/  CA 0x0648b448fe7b0bf828445a63a44927932f95d839（Robinhood）。2）2hour.fun（@2hourfun）Window two 首次进入 <=2h：05:00 CST（21:00 UTC）开窗，距约 1.87h。/api/window 仍无开窗字段，traderCount=44，窗口尚未打开。官帖 https://x.com/2hourfun/status/2126016645248307295 3）Lamoryant（@Lamoryant）官帖 02:32 CST 宣布改走 OpenSea 铸造：2026-11-27 19:00 CST（6:00 AM EST），供应 1,000；现持有人 Freemint（可铸数量等于现有持仓，即将快照）；白名单 0.001 ETH。尚未开铸。随后称 OpenSea checker 即将放出。原合约仍 publicEnabled，696/1356，公售价 0.001 ETH，铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。官帖 https://x.com/Lamoryant/status/2126021342663520455 本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
- newAdmits: 无。
- liveFlips: 无新的开铸翻转。既有免费 LIVE（Vicehood 签名窗 / Babbles / QQAI）只刷新进度。Lamoryant 为官方改走 OpenSea 的铸造计划变更，不是已开铸翻转。
- firstLe2h: Vicehood 免费公售 05:00 CST 首次进入 <=2h（距约 1.87h）；2hour.fun Window two 同步 05:00 CST 首次进入 <=2h（距约 1.87h）。Lamoryant OpenSea 铸造 19:00 CST，距开铸仍远于 2h。
- xReads: 13（main 10 + silent 1 + 瘦栏 24h 2）
- remainingBefore: 118
- remainingAfter: 105
- mode: tight（remainingBefore 118 <200，softCap 10 / minSpend 10 / silentCap 1 / eveningReserve 80）；未把额度紧当成砍掉薄栏 KW 的借口。MUST_WIN 作为首读兼额度探测（确认 remaining 118）。实际主搜 10 = UF1 + MUST_WIN + 瘦栏 6 + mentions 2；kwCore=0 按预算顺延；另 LZ/BTC 24h×2 + silent 1。
- 十栏关键词: 瘦栏 6 组 30m 全跑（LZ=1 TAPE=7 GIWA=7 DOGE=5 BTC=2 STARK=5）。核心栏因 tight alloc.kwCore=0 全部顺延（挖矿/GO盘上次跑于 R2247，台子/Elysium/打新跑于 R2248），不是整栏跳过。BN Agent 未偏科独占。
- userFollow: 已刷完。cursor 2051 @Octopusnfts1 → 2075 @crashdummyRH（end @scarf_ai，wrap=false，kept 24，total 2473）。UF 1 次查询（query 486 字，受约 512 上限）。UF 命中已在库 @sealdotarmy 产品更新（private SOL / Jupiter 相关），非 mint，不新收、不重推。
- mentions: LayerZero / Elysium（90m；两者均 25 触顶）。取 R2253 mentionsNext。各链本轮子集已扫，未偏科只扫 Elysium。下轮：DogeEVM / BTC（其后 Starknet / pads+squeek+STARX）。
- mentionsNext: DogeEVM / BTC
- silent: Tape/电路（has:mentions only，本客户端 connectors/x 无 search_users）。命中 25 触顶，未见须另收的未入库官号。silentNext: GIWA
- 瘦栏 24h 补搜: LayerZero（30m=1 <5）补了 24h（23 条）；BTC（30m=2 <5）补了 24h（25 触顶）。跳过 Tape/电路、GIWA、DogeEVM、Starknet（30m 已够：7/7/5/5）。
- MUST: MUST_WIN 已跑（窗口号合并探测，未为再确认翻页）。同一 handle 本轮只拉一次。命中 @Lamoryant 官帖宣布改走 OpenSea 铸造（02:32 CST，19:00 CST / 6:00 AM EST，供应 1000，持有人 Freemint，白名单 0.001 ETH）。未为核验全文另开 X 读，全文取自公开页镜像。Wildlife / Vicehood / Lanternhold / MaruTales 已合并进 MUST_WIN，未另开核验读。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek 持续 HTTP 401，key 无效；本轮无新候选需打分，判断/文案为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19-22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 新收录

- 无新收录。
- 跳过：@TheEyesBTC 仅第三方称 free mint（与 R2253 相同口径），未另开核验读；@precompilisium / @senductoelysium 仅第三方 Elysium 提及；@Kick0ff_ 为 X Layer 预测游戏（非 mint，约 1 年旧号）；@cheatGTAVI 自称将在 Elysium/Montra 上线，质量低；@spike__wtf 已在库 spike-wtf；$EARLY 仅见 KOL 转述 Montra，未见已核验官号，未另开 X 读；@t0dotfun 已在库 tzero-launchpad；@sealdotarmy 已在库 seal-army（UF 产品更新）；@rockzerodotlive 已在库 rockzero；@LaikaSuperApp 已在库 laika-doge。MEN_LZ/MEN_ELY 与 SILENT_TAPE 25 条多为已在库号、KOL 互动或误伤。

## 窗口与在库刷新

- Wildlife Universe（@wildlifeuni_55）免费公售已售罄，不重推：链上/OpenSea 5555/5555，持有 3003、地板 6.3e-05 ETH（R2253 为持有 3191、地板 0.00023 ETH）。写盘已过公售点约 0.65h。R2253 已按售罄提醒。CA 0xbbc8acefe610e09552df941e445a765f916f946f。
- Vicehood（@vicehood_rh）免费公售首次进入 <=2h：05:00 CST 开公售，距约 1.87h。当前仍为 01:00-04:00 CST 签名窗，免费 mint 仍 LIVE。链上 2284/3333（R2253 为 2265），OpenSea 供应 2284、持有 1961、地板 9.19e-05 ETH。R2250 已提醒开铸翻转，本轮按公售首次 <=2h 提醒。CA 0x0648b448fe7b0bf828445a63a44927932f95d839。
- Lamoryant（@Lamoryant）官帖宣布改走 OpenSea 铸造（官方计划变更，提醒一次）：2026-11-27 19:00 CST（6:00 AM EST），供应 1,000，现持有人 Freemint（可铸数量等于现有持仓，即将快照），白名单 0.001 ETH，尚未开铸。原合约仍 publicEnabled=True，链上 696/1356（R2253 为 695），OpenSea 696、持有 638，公售价 0.001 ETH。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。官帖 https://x.com/Lamoryant/status/2126021342663520455
- Lanternhold（@Lanternhold）已售罄，不重推：链上/OS 2222/2222，持有 1434、地板 0.31 USDG。
- MaruTales（@MaruTalesStudio）：铸造尚未 LIVE（MINTING_SOON，0/444，链上 0）。白名单核验仍开。R2245 已提醒，不重推。
- Babbles 等待名单免费 mint 仍 LIVE（不重推）：RPC/OS 126（与 R2253 相同），至 2026-11-27 05:00 CST。R2242 已提醒开窗。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 236.42M/600M（与 R2253 相同），未见新的开铸翻转。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=445,500,000 = 约 27/555（与 R2253 相同）。
- Ugly Puggies：RPC/OS 611、持有 384、地板 0.00013 ETH（与 R2253 相同），只是进度，不重推。
- F0B90B：637/10000（R2253 为 636），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2253 相同），只是进度，不重推。
- The Jacket：RPC/OS 214/777，持有 133、地板 0.45 USDG。只是进度，不重推。
- Guns of the Hood：链上/OS 126（与 R2253 相同），持有 19。只是进度，不重推。
- Rumble Hood（@Rumblehoodrh）：付费公开售仍 LIVE，不重推。链上 3611（与 R2253 相同），OpenSea 3611、持有 921、地板 0.05 USDG。本轮未见新官方进度帖。未核到 MAX_SUPPLY，不以口头 4000 覆盖此前 6000 记录。R2013 已提醒开售。
- Shielded Wizards（brimhollow）：API 仍报 mintOpen=true，phase=public，158/3333，reserved=3（R2253 为 reserved=2，供应仍 158）。供应无增加。不按开铸重推。
- 2hour.fun：Window two 首次进入 <=2h，05:00 CST（21:00 UTC）开窗，距约 1.87h。/api/window 仍无开窗字段，traderCount=44，窗口尚未打开。官帖 https://x.com/2hourfun/status/2126016645248307295
- RuninAI：MUST_WIN 仅见日常窗口/奖池宣传口径，R2226 已提醒，不重推。
- Hamster CombatHQ（@HamsteCombatHQ）：沿用 R2253 评论区送 GTD / winners，仍非开铸/独立登记页 LIVE。R2226 已提醒，不重推。
- GoaTs（@GoaTopiax）：仍 Coming soon / Drop wallet，不是 LIVE。R2245 已收录，不重推。
- Texel（@texelrun）：沿用 R2253 产品更新（agents 用 USDG/x402 付费调 GPU），非 mint，不重推。
- Seal Army（@sealdotarmy）：UF 见产品更新（private SOL / Jupiter），已在库，非 mint，不重推。
- HEPH（@heph_ai）：本轮未见新官帖。沿用 R2251 产品更新记录，不重推。
- Canton / Glaze / TokenWorks Watch lastChecked 已刷新，无实质变化。

## 规则核对

- 空轮芯片未造（无新收录）。未新标 focus。收藏未改。
- 无新卡，无只建卡不盯问题。
- 判断/文案为 dsFallback（DeepSeek 近期持续 401），未用高成本模型批量打分。
- 已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
