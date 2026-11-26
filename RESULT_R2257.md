# 早期打新雷达 R2257

- lastScout: 2026-11-27 04:42:21 CST
- notify: true
- alert: 见面板 / 父代理转发。含：新收录 AiBTC.BOT、Anvora。Vicehood FCFS / Babbles 公售 / 2hour Window two 仍 <=2h，均已在前轮提醒，不重推。
- newAdmits: aibtc（@aibtc_bot）、anvora（@anvoraapp）。均非免费 mint。
- liveFlips: 无。既有免费 LIVE（Vicehood FCFS / Babbles 等待名单 / QQAI / brimhollow）同步刷新进度。
- firstLe2h: 无。Vicehood 免费公售、Babbles 付费公售与 2hour.fun Window two 仍 05:00 CST <=2h（距约 0.29h），均已在 R2254/R2256 提醒，不按同一事件重推。Lamoryant OpenSea 铸造 19:00 CST，仍远于 2h。
- xReads: 17（main 10 + silent 1 + 瘦栏 24h 6）
- remainingBefore: 74
- remainingAfter: 57
- mode: tight（remainingBefore 74 <200，softCap 10 / minSpend 10 / silentCap 1 / eveningReserve 80）；未把额度紧当成砍掉薄栏 KW 的借口。MUST_WIN 作为首读兼额度探测（确认 remaining 74→73）。实际主搜 10 = UF1 + MUST_WIN + 瘦栏 6 + mentions 2；kwCore=0 按预算顺延；另瘦栏 24h×6 + silent 1。
- 十栏关键词: 瘦栏 6 组 30m 全跑（LZ=0 TAPE=4 GIWA=2 DOGE=0 BTC=0 STARK=2）。因全部 <5，同一轮 24h 补搜 6 组都跑了。核心栏因 tight alloc.kwCore=0 全部顺延（挖矿/GO盘上次跑于 R2247，台子/Elysium/打新跑于 R2248），不是整栏跳过。BN Agent 未偏科独占。
- userFollow: 已刷完。cursor 2124 @Asklepion_tech → 2147 @listendotmoney（wrap=false，kept 24，total 2474）。下轮起点 2148 @glint_bnb。UF 1 次查询。UF 命中多为 @SMOOVEOFFSOL 闲聊与已在库 @casebookduel 产品帖，无新收录。
- mentions: LayerZero / Elysium（90m；MEN_LZ=25 触顶，MEN_ELY=25 触顶）。取 R2256 mentionsNext。各链本轮子集已扫，未偏科只扫 Elysium。下轮：DogeEVM / BTC。
- mentionsNext: DogeEVM / BTC
- silent: BTC（has:mentions only，本客户端 connectors/x 无 search_users）。命中 15，含官号 @aibtc_bot（本轮收录）。silentNext: Starknet
- 瘦栏 24h 补搜: 6 组全部补了（30m 均 <5），均 25 触顶：LayerZero、Tape/电路、GIWA、DogeEVM、BTC、Starknet。无跳过。
- MUST: MUST_WIN 已跑（窗口号合并探测，未为再确认翻页或另开 getPosts）。同一 handle 本轮只拉一次。30m 仅见 RuninAI 日常 20:00 CST 窗口宣传与一条回复 @babblesxyz，未见 Vicehood/2hour/Lamoryant 新官帖。Wildlife / Lanternhold / MaruTales 已合并进 MUST_WIN，未另开核验读。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek 持续 HTTP 401，key 无效；AiBTC / Anvora 录取/打分为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19-22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 新收录

- AiBTC.BOT（@aibtc_bot / https://aibtc.bot）：自称 Bitcoin L1 混合 DEX + 公平发射台已开（Launch/Swap/AMM，AIBRC / BRC-20 / Runes）。官号 2026-10-19 00:30 CST 建立，2454 粉 46 帖。官网 HTTP 200，页内回链 x.com/aibtc_bot，资料栏 URL 指向该站（siteXMutual=true）。有公开 GitHub（aibtcbot/aibtcbot）、文档与 Telegram。本轮官帖为回复向自述，合约/盘口未独立核验。归台子/Meme + BTC 标签，focus=false。非免费 mint。属静号 BTC 补漏，不是极早期 0 粉阶段。已挂 userFollowWatch + btcPrivacyWatch。官帖 https://x.com/aibtc_bot/status/2125924842155516109
- Anvora（@anvoraapp / https://anvora.vercel.app）：自称 GIWA Sepolia 测试网社区代币发射台已开（Ammora SDK bonding curve，曲线满后可毕业进池）。官号 2026-10-04 07:47 CST 建立，仅 6 粉 34 帖。官网 HTTP 200，twitter:site 为 @anvoraapp，资料栏 URL 指向该站（siteXMutual=true）。站点与 README 写明 testnet only、未独立审计、不要用真实资金。不是免费 mint，也不是主网 LIVE。归台子/Meme + GIWA 标签，focus=false。已挂 userFollowWatch + giwaWatch。
- 跳过：@TheEyesBTC 仍仅第三方称 free mint（与 R2253–R2256 相同口径），未另开核验读；@nomorelabs 第三方预告 Comrades of the Hood 即将 mint，本轮未见其官帖，不收录；@zerixdotfun 2026-11-25 建号、2 粉 1 帖、无官网，仅第三方 waitlist 提及，不收录；@ai_supergent 2026-11-25 建号、0 粉 3 帖，资料栏无网站，仅被 @runinai_ 提及且自称 “first one is free / Live on Mainnet”，本轮未见其官帖与站点，看见但不收录。MEN_LZ / MEN_ELY 与各瘦栏 24h 25 条多为已在库号（T0dotfun、Globe、XofN、Eloscape、GiwaTerminal、Zayro、Writ 等）或 KOL / Bramble 误伤。

## 窗口与在库刷新

- Vicehood（@vicehood_rh）FCFS 仍 LIVE，不重推：链上 3298/3333（R2256 为 2510），OpenSea 供应 3225、持有 2367、地板 9.405e-05 ETH。免费 mint 仍 LIVE。免费公售仍定 05:00 CST（距约 0.29h）。R2256 已按 FCFS 开闸提醒，R2254 已按公售首次 <=2h 提醒。铸页 https://opensea.io/collection/vchood CA 0x0648b448fe7b0bf828445a63a44927932f95d839。
- Babbles（@babblesxyz）付费公售仍定 05:00 CST，不重推：RPC/OS 127（R2256 为 126），持有 17、地板 0.0047 ETH。等待名单免费 mint 仍 LIVE，至 05:00 CST。R2256 已按付费公售首次 <=2h 提醒。铸页 https://opensea.io/collection/babbles CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B。
- Wildlife Universe（@wildlifeuni_55）免费公售已售罄，不重推：链上/OpenSea 5555/5555，持有 2964、地板 0.000123 ETH（R2256 为持有 2977、地板 0.000148 ETH）。R2253 已按售罄提醒。
- Lamoryant（@Lamoryant）原合约仍 publicEnabled=True，链上 698/1356（与 R2256 相同）。本轮 OpenSea 命中的 lamoryant- 合集供应为 0（官宣 19:00 CST 新铸页，尚未开铸），旧合集进度未在该路径返回，持有/地板沿用 R2256：OpenSea 697、持有 639，公售价 0.001 ETH。官宣 OpenSea 铸造仍定 2026-11-27 19:00 CST（距约 14.29h），尚未开铸，不重推。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。
- Lanternhold（@Lanternhold）已售罄，不重推：链上/OS 2222/2222，持有 1423、地板 0.26 USDG（R2256 为持有 1430）。
- MaruTales（@MaruTalesStudio）：MUST_WIN 未见新官宣，铸造尚未 LIVE（0/444）。白名单核验仍开。R2245 已提醒，不重推。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 236.42M/600M（与 R2256 相同）。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=445,500,000 = 约 27/555（与 R2256 相同）。
- Ugly Puggies：RPC/OS 612，持有 384、地板 0.00013 ETH（与 R2256 相同），只是进度，不重推。
- F0B90B：642/10000（R2256 为 641），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2256 相同），只是进度，不重推。
- The Jacket：RPC/OS 214/777，持有 133、地板 0.45 USDG。只是进度，不重推。
- Guns of the Hood：链上/OS 126，持有 19。只是进度，不重推。
- Rumble Hood（@Rumblehoodrh）：付费公开售仍 LIVE，不重推。链上/OpenSea 3611、持有 921、地板 0.05 USDG。本轮 MUST_WIN 未覆盖该号。未核到 MAX_SUPPLY，不以口头 4000 覆盖此前 6000 记录。R2013 已提醒开售。
- Shielded Wizards（brimhollow）：API 仍报 mintOpen=true，phase=public，159/3333（与 R2256 相同），reserved=2。不按开铸重推。
- 2hour.fun：Window two 仍定 05:00 CST（21:00 UTC）。/api/window 仍无开窗字段，traderCount=243（与 R2256 相同），不按已开窗重推。R2254 已按首次 <=2h 提醒。
- RuninAI：MUST_WIN 再见日常 20:00 CST 窗口宣传（并回复 @ai_supergent），R2226 已提醒，不重推。
- Canton / Glaze / TokenWorks Playground Watch lastChecked 已刷新，无实质变化。

## 规则核对

- 新卡 aibtc、anvora 未标 focus。空轮芯片未造。收藏未改。
- 入库同时写入 userFollowWatch，以及 btcPrivacyWatch（aibtc）/ giwaWatch（anvora），无只建卡不盯。
- 判断/文案为 dsFallback（DeepSeek 持续 401），未用高成本模型批量打分。
- 已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
