# 早期打新雷达 R2259

- lastScout: 2026-11-27 05:39:36 CST
- notify: false
- alert: 无。无新收录，无新窗口翻转，无首次 ≤2h。
- newAdmits: 无。
- liveFlips: 无。
- firstLe2h: 无。Lamoryant OpenSea 铸造仍 19:00 CST，距约 13.34h。2hour Window two 仍至 07:00 CST（距约 1.34h），R2258 已按开窗提醒，不重推。
- xReads: 2（MUST_WIN 1 + UF1 1）
- remainingBefore: 41
- remainingAfter: 39
- mode: near-exhausted（remainingBefore 41 <50，softCap 8 / minSpend 6 / silentCap 0）。MUST_WIN 作为首读兼额度探测（确认 remaining 41→40）。实际主搜 2 = 合并 MUST 窗口号一次 + UF 24 号分片一次。未为凑 minSpend 另开关键词/mentions/翻页。关键词、mentions、静号全部按规则顺延，不是额度够时砍栏。
- 十栏关键词: 本轮未跑（near-exhausted 规则：仅 UF 优先片 + ≤2h/MUST）。瘦栏 6 组与核心栏（挖矿/GO盘上次 R2247，台子/Elysium/打新上次 R2248）全部顺延至额度回升或 08:00 CST 后首轮全量补扫。未把肥词改成 24h。BN Agent 未偏科独占。
- userFollow: 已刷完。cursor 2172 @gyeolmarkets → 2195 @rebelianrh（wrap=false，kept 24，total 2476）。下轮起点 2196 @stinkbid_app。UF 1 次查询，命中 2 帖（@Solvyren 节点最终性说明、@theossuary_ 叙事卡文），无新收录。
- mentions: 因 near-exhausted 整组顺延，未跑。R2258 的 mentionsNext（Starknet / pads+squeek+STARX）保留到下轮或 08:00 后全量补扫，不跳过轮换。
- mentionsNext: Starknet / pads+squeek+STARX
- silent: silentCap=0，ran=false。silentNext 仍为 打新。
- 瘦栏 24h 补搜: 未做（30m 关键词本身未跑）。
- MUST: MUST_WIN 已跑（窗口号合并探测，未翻页、未为再确认另开 getPosts）。同一 handle 本轮只拉一次。30m 见 @RuninAI_com 日常 20:00 CST 挖矿窗宣传，以及 One-Click Launch 预告；官网 https://runinai.com 该功能仍 COMING SOON / 按钮 disabled，不是新台 LIVE。@ShieldedWizBTC 称 public mint 仍开，并提醒投票截止 2026-11-27 18:00 UTC（2026-11-28 02:00 CST，远于 2h）。未见 Lamoryant / Wildlife / Vicehood / Babbles / 2hourfun / Lanternhold / MaruTales / GoaTs / Frost Hood 新官帖。
- lastFullAfterReset: R2216
- dsFallback: true（本轮无新候选需打分；DeepSeek 近轮持续 HTTP 401，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19-22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 新收录

- 无。
- 看见但未收：无新号候选。UF @Solvyren / @theossuary_ 均为已在库关注号日常帖。RuninAI One-Click Launch 官网站内仍 Coming Soon，不按已开新台收录或重推。

## 窗口与在库刷新

- Vicehood（@vicehood_rh）售罄后复核，不重推：链上/OpenSea 仍 3333/3333，持有 2358，地板 8e-05 ETH（R2258 地板 9.101e-05 ETH）。R2258 已按 04:57:01 CST 售罄提醒。铸页 https://opensea.io/collection/vchood CA 0x0648b448fe7b0bf828445a63a44927932f95d839。
- Babbles（@babblesxyz）付费公售仍 LIVE，不重推：链上/OS 仍 127（仍未见公售增量），持有 17、地板 0.0047 ETH。R2258 已按开闸翻转提醒。铸页 https://opensea.io/collection/babbles CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B。
- 2hour.fun Window two 仍按开窗处理，不重推：MUST_WIN 无新官帖；官宣仍至 2026-11-27 07:00 CST（距约 1.34h）。/api/window 仍无显式开窗字段；本轮 traderCount 字段回到 243，perCoin 同时出现旧窗 54PSWdi（traders=243）和新地址 0x5f8d1a0df7（traders=1）。不以 API 回摆当作关窗。R2258 已按开窗翻转提醒。https://www.2hour.fun/
- Wildlife Universe（@wildlifeuni_55）免费公售已售罄，不重推：链上/OpenSea 5555/5555，持有 2958、地板 0.00011 ETH（R2258 为持有 2962、地板 9.97e-05 ETH）。R2253 已按售罄提醒。
- Lamoryant（@Lamoryant）原合约仍 publicEnabled=True，链上 698/1356（与 R2258 相同）。OpenSea lamoryant- 合集供应仍为 0。官宣 OpenSea 铸造仍定 2026-11-27 19:00 CST（距约 13.34h），尚未开铸，不重推。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。
- Lanternhold（@Lanternhold）已售罄，不重推：链上/OS 2222/2222，持有 1423、地板 0.26 USDG（与 R2258 相同）。
- MaruTales（@MaruTalesStudio）：MUST_WIN 未见新官宣，铸造尚未 LIVE（0/444）。白名单核验仍开。R2245 已提醒，不重推。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 236.42M/600M（与 R2258 相同）。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=445,500,000 = 约 27/555（与 R2258 相同）。
- Ugly Puggies：RPC/OS 612，持有 384、地板 0.00013 ETH（与 R2258 相同），只是进度，不重推。
- F0B90B：643/10000（R2258 为 642），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2258 相同），只是进度，不重推。
- The Jacket：RPC/OS 214/777，持有 133、地板 0.45 USDG（与 R2258 相同）。只是进度，不重推。
- Guns of the Hood：链上/OS 126，持有 19（stats 接口本轮 401，持有沿用 R2258）。只是进度，不重推。
- Rumble Hood（@Rumblehoodrh）：付费公开售仍 LIVE，不重推。链上/OpenSea 3614（与 R2258 相同）、持有 921、地板 0.05 USDG。未核到 MAX_SUPPLY。R2013 已提醒开售。
- Shielded Wizards（brimhollow）：API 仍报 mintOpen=true，phase=public，159/3333（与 R2258 相同），reserved=2（R2258 写 3，本轮以 API 为准）。投票截止远于 2h。不按开铸重推。
- RuninAI：One-Click Launch 官网仍 Coming Soon，不是新台 LIVE。每日窗口宣传 R2226 已提醒，不重推。
- GoaTs：MUST_WIN 未见开铸官帖，仍 Coming soon / Drop wallet，不是 LIVE。R2245 已收录，不重推。
- Canton / Glaze / TokenWorks Watch lastChecked 已刷新，无实质变化。本轮抽查近期新卡均已在 Watch；未做全库 4000+ 漏挂大修。

## 规则核对

- 本轮无新卡。空轮芯片未造。收藏未改。未把普通项目标 focus。
- 判断/文案为 dsFallback，未用高成本模型批量打分。
- 已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/

