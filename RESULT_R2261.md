# 早期打新雷达 R2261

- lastScout: 2026-11-27 06:42:13 CST
- notify: false
- alert: 无。无新收录，无新窗口翻转，无首次 ≤2h。
- newAdmits: 无。
- liveFlips: 无。
- firstLe2h: 无。Lamoryant OpenSea 铸造仍 19:00 CST，距约 12.30h。2hour Window two 仍至 07:00 CST（距约 0.30h），R2258 已按开窗提醒，不重推。
- xReads: 2（MUST_WIN 1 + UF1 1）
- remainingBefore: 37
- remainingAfter: 35
- mode: near-exhausted（remainingBefore 37 <50，softCap 8 / minSpend 6 / silentCap 0）。MUST_WIN 作为首读兼额度探测（确认 remaining 37→36）。实际主搜 2 = 合并 MUST 窗口号一次 + UF 24 号分片一次。未为凑 minSpend 另开关键词/mentions/翻页。关键词、mentions、静号全部按规则顺延，不是额度够时砍栏。
- 十栏关键词: 本轮未跑（near-exhausted 规则：仅 UF 优先片 + ≤2h/MUST）。瘦栏 6 组与核心栏（挖矿/GO盘上次 R2247，台子/Elysium/打新上次 R2248）全部顺延至额度回升或 08:00 CST 后首轮全量补扫。未把肥词改成 24h。BN Agent 未偏科独占。
- userFollow: 已刷完。cursor 2220 @brainex__ai → 2243 @midorihood（wrap=false，kept 24，total 2476）。下轮起点 2244 @snoozehighrh。UF 1 次查询，45 分钟窗 result_count=0，无新收录。
- mentions: 因 near-exhausted 整组顺延，未跑。R2258 的 mentionsNext（Starknet / pads+squeek+STARX）保留到下轮或 08:00 后全量补扫，不跳过轮换。
- mentionsNext: Starknet / pads+squeek+STARX
- silent: silentCap=0，ran=false。silentNext 仍为 打新。
- 瘦栏 24h 补搜: 未做（30m 关键词本身未跑）。
- MUST: MUST_WIN 已跑（窗口号合并探测，未翻页、未为再确认另开 getPosts）。同一 handle 本轮只拉一次。30m 见 @RuninAI_com 日常 20:00 CST 挖矿窗宣传（06:17 / 06:23 / 06:29 CST）；官网 https://runinai.com One-Click Launch 仍 COMING SOON / 按钮 disabled，不是新台 LIVE。见 @nullfamily 两则短帖（06:20:57 CST「Notis on…」、06:25:21 CST「Only 2400」）；官网 https://www.nullfamily.fun/ 仍是测试网任务/积分页，铸造仍非 LIVE，不重推。见 @ShieldedWizBTC 06:10:20 CST 客服向回复（确认 Bitcoin 铸造到账、引导金库），不是新开铸/改期官宣。未见 Wildlife / Vicehood / Babbles / 2hourfun / Lanternhold / MaruTales / GoaTs / Frost Hood / Lamoryant 新官帖。
- lastFullAfterReset: R2216
- dsFallback: true（本轮无新候选需打分；DeepSeek 近轮持续 HTTP 401，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19-22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 新收录

- 无。
- 看见但未收：无新号候选。UF 分片 45 分钟窗 0 帖。@nullfamily 已在库（R2239），短帖+官网仍为测试网任务，不另建卡、不按开铸收录。RuninAI One-Click Launch 官网站内仍 Coming Soon，不按已开新台收录或重推。

## 窗口与在库刷新

- Vicehood（@vicehood_rh）售罄后复核，不重推：链上仍 3333/3333。MUST 未见新官帖。代币 CA 仍为 0x358015a2deed583b9b8f2bbcd0cd0f882e26b0f0（VICEHOOD/VCHOOD，10 亿枚），R2260 已补记。持有/地板沿用 R2259：2358、8e-05 ETH（本轮 OpenSea 仅核到供应量，未刷新持有/地板）。R2258 已按 04:57:01 CST 售罄提醒。铸页 https://opensea.io/collection/vchood NFT CA 0x0648b448fe7b0bf828445a63a44927932f95d839。
- Babbles（@babblesxyz）付费公售仍 LIVE，不重推：链上仍 127（仍未见公售增量）。持有/地板沿用 R2259：17、0.0047 ETH。R2258 已按开闸翻转提醒。铸页 https://opensea.io/collection/babbles CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B。
- 2hour.fun Window two 仍按开窗处理，不重推：MUST_WIN 无新官帖；官宣仍至 2026-11-27 07:00 CST（距约 0.30h）。/api/window 仍无显式开窗字段；本轮 traderCount=244，perCoin 同时出现旧窗 54PSWdi（traders=244）和新地址 0x5f8d1a0df7（traders=1）。不以 API 计数当作关窗。R2258 已按开窗翻转提醒。https://www.2hour.fun/
- Wildlife Universe（@wildlifeuni_55）免费公售已售罄，不重推：链上仍 5555/5555。持有/地板沿用 R2259：2958、0.00011 ETH。R2253 已按售罄提醒。
- Lamoryant（@Lamoryant）原合约仍 publicEnabled=True，链上 698/1356（与 R2260 相同）。官宣 OpenSea 铸造仍定 2026-11-27 19:00 CST（距约 12.30h），尚未开铸，不重推。OpenSea 集合 lamoryant- 本轮仍报 total_supply=0（合约 0xc5387a072ae4ae191424189f5d7f3c7b46edf375），与原铸合约不是同一地址，不以该页 0 供应覆盖链上 698。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。
- Lanternhold（@Lanternhold）已售罄，不重推：链上仍 2222/2222。持有/地板沿用 R2259：1423、0.26 USDG。
- MaruTales（@MaruTalesStudio）：MUST_WIN 未见新官宣，铸造尚未 LIVE（链上仍 0/444）。白名单核验仍开。R2245 已提醒，不重推。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 236.42M/600M（与 R2260 相同）。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：token totalSupply=478,500,000 = 约 29/555（与 R2260 相同），只是进度。
- Ugly Puggies：RPC 仍 612/777。持有/地板沿用 R2259：384、0.00013 ETH。只是进度，不重推。
- F0B90B：643/10000（与 R2260 相同），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2260 相同），paused=false，只是进度，不重推。
- The Jacket：RPC 仍 214/777。持有/地板沿用 R2259：133、0.45 USDG。只是进度，不重推。
- Guns of the Hood：链上仍 126。持有沿用 R2259：19（本轮未刷新 OpenSea 持有/地板）。只是进度，不重推。
- Rumble Hood（@Rumblehoodrh）：付费公开售仍 LIVE，不重推。链上仍 3614/4000。持有/地板沿用 R2259：921、0.05 USDG。R2013 已提醒开售。
- Shielded Wizards（brimhollow）：MUST 见 06:10:20 CST 客服向回复，不是新开铸官宣。本轮未刷新 brimhollow API（上次 2026-11-26 20:35 CST 报 mintOpen=true，phase=public，159/3333，reserved=2）。投票截止远于 2h。不按开铸重推。
- RuninAI：One-Click Launch 官网仍 Coming Soon，不是新台 LIVE。每日窗口宣传 R2226 已提醒，不重推。
- GoaTs：MUST_WIN 未见开铸官帖，仍 Coming soon / Drop wallet，不是 LIVE。R2245 已收录，不重推。
- Null（@nullfamily）：已在库。MUST 见两则短帖，官网仍为测试网任务/积分，铸造仍非 LIVE。R2239 已收录，不重推。
- Canton / Glaze / TokenWorks Watch lastChecked 已刷新，无实质变化。本轮抽查近期窗口卡均已在 Watch；未做全库 4000+ 漏挂大修。本轮未刷新 OpenSea 持有/地板，相关数字沿用 R2259。

## 规则核对

- 本轮无新卡。空轮芯片未造。收藏未改。未把普通项目标 focus。
- 判断/文案为 dsFallback，未用高成本模型批量打分。
- 已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
