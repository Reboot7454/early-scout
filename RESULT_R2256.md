# 早期打新雷达 R2256

- lastScout: 2026-11-27 04:09:53 CST
- notify: true
- alert: 见面板 / 父代理转发。含：Vicehood FCFS LIVE、Babbles 付费公售首次 <=2h、新收录 XofN。
- newAdmits: xofn（@XofNProtocol）。
- liveFlips: Vicehood FCFS 阶段开启（免费 mint 已在签名窗 LIVE，本轮是第二段 FCFS 窗开闸）。既有免费 LIVE（Vicehood / Babbles 等待名单 / QQAI）同步刷新进度。
- firstLe2h: Babbles 付费公售 05:00 CST 首次进入 <=2h。Vicehood 免费公售与 2hour.fun Window two 仍 <=2h，均已在 R2254 提醒，不按同一事件重推。Lamoryant OpenSea 铸造 19:00 CST，仍远于 2h。
- xReads: 15（main 10 + silent 1 + 瘦栏 24h 4）
- remainingBefore: 89
- remainingAfter: 74
- mode: tight（remainingBefore 89 <200，softCap 10 / minSpend 10 / silentCap 1 / eveningReserve 80）；未把额度紧当成砍掉薄栏 KW 的借口。MUST_WIN 作为首读兼额度探测（确认 remaining 89）。实际主搜 10 = UF1 + MUST_WIN + 瘦栏 6 + mentions 2；kwCore=0 按预算顺延；另瘦栏 24h×4 + silent 1。
- 十栏关键词: 瘦栏 6 组 30m 全跑（LZ=4 TAPE=5 GIWA=2 DOGE=6 BTC=0 STARK=2）。核心栏因 tight alloc.kwCore=0 全部顺延（挖矿/GO盘上次跑于 R2247，台子/Elysium/打新跑于 R2248），不是整栏跳过。BN Agent 未偏科独占。
- userFollow: 已刷完。cursor 2100 @auroveil → 2123 @Zerovo_io（end @Zerovo_io，wrap=false，kept 24，total 2473）。UF 1 次查询。UF 命中已在库 @Zerovo_io 产品说明帖（曲线/virtual ZRO），不是开铸翻转，不新收、不重推。
- mentions: Starknet / pads+squeek+STARX（90m；MEN_STARK=3，MEN_PADS=25 触顶）。取 R2255 mentionsNext。各链本轮子集已扫，未偏科只扫 Elysium。下轮：LayerZero / Elysium。
- mentionsNext: LayerZero / Elysium
- silent: DogeEVM（has:mentions only，本客户端 connectors/x 无 search_users）。命中 4，未见须另收的未入库官号。silentNext: BTC
- 瘦栏 24h 补搜: LayerZero（30m=4 <5）补了 24h（25 触顶）；GIWA（30m=2 <5）补了 24h（25 触顶）；BTC（30m=0 <5）补了 24h（25 触顶）；Starknet（30m=2 <5，且多为 Bramble 误伤）补了 24h（25 触顶）。跳过 Tape/电路（30m 已够：5）、DogeEVM（30m 已够：6）。
- MUST: MUST_WIN 已跑（窗口号合并探测，未为再确认翻页或另开 getPosts）。同一 handle 本轮只拉一次。命中 @Vicehood_RH 官帖 FCFS IS LIVE、@babblesxyz 官帖宣布 05:00 CST 付费公售；@2hourfun 03:34 周竞赛帖已在 R2255 记录窗口。Wildlife / Lanternhold / MaruTales 已合并进 MUST_WIN，未另开核验读。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek 持续 HTTP 401，key 无效；XofN 录取/打分为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19-22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 新收录

- XofN（@XofNProtocol / https://xofnprotocol.com/）：自称 Robinhood 主网 LayerZero V2 OFT 发射台已 LIVE。官号 2026-11-18 08:28 CST 建立，8 粉 5 帖。官网 HTTP 200，页内回链官推，资料栏 URL 指向该站（siteXMutual=true）。官帖称每笔发射从第一天起就是 LZ V2 OFT，合约层拒绝 1-of-1 DVN；bonding curve，约 4 ETH graduate() 进 Uniswap v4；Base/Arbitrum 尚未上线；未审计，真实资金。自称 CA 0xa81286df8525ee53b8a0436d9941473b3b8935e5，未独立核验。lzVerified=false，归台子/Meme，focus=false。非免费 mint。已挂 userFollowWatch + layerZeroWatch。官帖 https://x.com/XofNProtocol/status/2126038926779695422
- 跳过：@TheEyesBTC 仍仅第三方称 free mint（与 R2253/R2254/R2255 相同口径），未另开核验读；@spontan199 称在 GIWA Sepolia 用 Ammora SDK 上了 MANTOKEN 发射，非独立官号项目；MEN_PADS / SILENT_DOGE 与各瘦栏 24h 25 条多为已在库号（GAMA、Vorda、Numen、Ammora、madang、Shielded Naka 等）、KOL 互动或 Bramble 动物/游戏误伤。

## 窗口与在库刷新

- Vicehood（@vicehood_rh）FCFS 已 LIVE（本轮提醒）：官帖 04:00:37 CST 宣布 FCFS IS LIVE。对应 OpenSea 既有第二段 SIGNED_PRESALE 04:00–05:00 CST。免费 mint 仍 LIVE。链上 2510/3333（R2255 为 2320），OpenSea 供应 2338、持有 2030、地板 7.9e-05 ETH。免费公售仍定 05:00 CST。R2254 已按公售首次 <=2h 提醒，本轮按 FCFS 开闸提醒一次。铸页 https://opensea.io/collection/vchood CA 0x0648b448fe7b0bf828445a63a44927932f95d839。官帖 https://x.com/Vicehood_RH/status/2126043469357400548
- Babbles（@babblesxyz）付费公售首次进入 <=2h：官帖 04:00 CST 称 21:00 UTC / 05:00 CST 开公售，0.002611 ETH、每钱包最多 11。等待名单免费 mint 仍 LIVE，至 05:00 CST。RPC/OS 126，持有 16、地板 0.0047 ETH。R2242 已提醒等待名单开窗。铸页 https://opensea.io/collection/babbles CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B。官帖 https://x.com/babblesxyz/status/2126043312175874093
- Wildlife Universe（@wildlifeuni_55）免费公售已售罄，不重推：链上/OpenSea 5555/5555，持有 2977、地板 0.000148 ETH（R2255 为持有 2980、地板 7e-05 ETH）。R2253 已按售罄提醒。CA 0xbbc8acefe610e09552df941e445a765f916f946f。
- Lamoryant（@Lamoryant）原合约仍 publicEnabled=True，链上 698/1356（R2255 为 697），OpenSea 697、持有 639，公售价 0.001 ETH。官宣 OpenSea 铸造仍定 2026-11-27 19:00 CST，尚未开铸，不重推。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。
- Lanternhold（@Lanternhold）已售罄，不重推：链上/OS 2222/2222，持有 1430、地板 0.26 USDG（R2255 为持有 1429、地板 0.28 USDG）。
- MaruTales（@MaruTalesStudio）：MUST_WIN 仅见感恩节祝福，铸造尚未 LIVE（0/444）。白名单核验仍开。R2245 已提醒，不重推。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 236.42M/600M（与 R2255 相同）。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=445,500,000 = 约 27/555（与 R2255 相同）。
- Ugly Puggies：RPC/OS 612，持有 384、地板 0.00013 ETH（与 R2255 相同），只是进度，不重推。
- F0B90B：641/10000（R2255 为 640），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2255 相同），只是进度，不重推。
- The Jacket：RPC/OS 214/777，持有 133、地板 0.45 USDG（本轮 OpenSea stats 401，持有/地板沿用 R2255）。只是进度，不重推。
- Guns of the Hood：链上/OS 126，持有 19。只是进度，不重推。
- Rumble Hood（@Rumblehoodrh）：付费公开售仍 LIVE，不重推。链上 3611，OpenSea 3611、持有 921、地板 0.05 USDG。本轮 MUST_WIN 未覆盖该号。未核到 MAX_SUPPLY，不以口头 4000 覆盖此前 6000 记录。R2013 已提醒开售。
- Shielded Wizards（brimhollow）：API 仍报 mintOpen=true，phase=public，159/3333（R2255 为 158），reserved=2。供应 +1。不按开铸重推。
- 2hour.fun：Window two 仍定 05:00 CST（21:00 UTC）。/api/window 仍无开窗字段，traderCount=243（R2255 为 44），不按已开窗重推。R2254 已按首次 <=2h 提醒。官帖 https://x.com/2hourfun/status/2126036808592953493
- RuninAI：MUST_WIN 再见日常 20:00 CST 窗口宣传，R2226 已提醒，不重推。
- Zerovo（@Zerovo_io）：UF 见产品说明帖，已在库，非 mint/LIVE 翻转，不重推。
- GoaTs / Hamster CombatHQ / Texel / HEPH：本轮 MUST_WIN 未见须重推的新官宣，沿用此前记录。
- Canton / Glaze / TokenWorks Watch lastChecked 已刷新，无实质变化。

## 规则核对

- 新卡 xofn 未标 focus。空轮芯片未造。收藏未改。
- 入库同时写入 userFollowWatch 与 layerZeroWatch，无只建卡不盯。
- 判断/文案为 dsFallback（DeepSeek 持续 401），未用高成本模型批量打分。
- 已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
