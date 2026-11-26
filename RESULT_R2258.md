# 早期打新雷达 R2258

- lastScout: 2026-11-27 05:10:40 CST
- notify: true
- alert: 见面板 / 父代理转发。含：Vicehood 售罄、Babbles 付费公售开闸、2hour.fun Window two 开窗。无新收录。
- newAdmits: 无。
- liveFlips: Vicehood 售罄；Babbles 等待名单免费窗结束、付费公售 LIVE；2hour Window two 开窗。
- firstLe2h: 无。Lamoryant OpenSea 铸造仍 19:00 CST，远于 2h。
- xReads: 16（main 10 + silent 1 + 瘦栏 24h 5）
- remainingBefore: 57
- remainingAfter: 41
- mode: tight（remainingBefore 57 <200，softCap 10 / minSpend 10 / silentCap 1 / eveningReserve 80）；未把额度紧当成砍掉薄栏 KW 的借口。MUST_WIN 作为首读兼额度探测（确认 remaining 57→56）。实际主搜 10 = UF1 + MUST_WIN + 瘦栏 6 + mentions 2；kwCore=0 按预算顺延；另瘦栏 24h×5（GIWA 30m=9≥5，不补 24h）+ silent 1。
- 十栏关键词: 瘦栏 6 组 30m 全跑（LZ=0 TAPE=0 GIWA=9 DOGE=4 BTC=0 STARK=2）。因 LZ/TAPE/DOGE/BTC/STARK 均 <5，同一轮 24h 补搜这 5 组都跑了；GIWA 30m 已有 9 条，未做 24h。核心栏因 tight alloc.kwCore=0 全部顺延（挖矿/GO盘上次跑于 R2247，台子/Elysium/打新跑于 R2248），不是整栏跳过。BN Agent 未偏科独占。
- userFollow: 已刷完。cursor 2148 @glint_bnb → 2171 @vantaliquid（wrap=false，kept 24，total 2476）。下轮起点 2172 @gyeolmarkets。UF 1 次查询，命中 0 帖，无新收录。
- mentions: DogeEVM / BTC（90m；MEN_DOGE=11，MEN_BTC=25 触顶）。取 R2257 mentionsNext。各链本轮子集已扫，未偏科只扫 Elysium。下轮：Starknet / pads+squeek+STARX。
- mentionsNext: Starknet / pads+squeek+STARX
- silent: Starknet（has:mentions only，本客户端 connectors/x 无 search_users）。命中 2，多为误伤（Bramble 果酱/故事/游戏）及一条 Starknet L1 讨论，无新收录。silentNext: 打新。
- 瘦栏 24h 补搜: 5 组（LZ/TAPE/DOGE/BTC/STARK）全部补了，均 25 触顶。GIWA 因 30m≥5 未补。无把肥词改成 24h。
- MUST: MUST_WIN 已跑（窗口号合并探测，未为再确认翻页或另开 getPosts）。同一 handle 本轮只拉一次。30m 核到 Vicehood 售罄官帖、Babbles 公售开闸官帖、2hour Window two 开窗官帖；另见 Babbles 倒计时与 RuninAI 日常回复，未见 Lamoryant/Wildlife/Lanternhold/MaruTales 新官帖。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek 持续 HTTP 401，key 无效；告警/文案为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19-22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 新收录

- 无。
- 看见但未收：@TheEyesBTC 仍仅第三方称 free mint / Coming soon（与 R2253–R2257 相同口径），未另开核验读。@Spike__wtf 已在库（spike-wtf，R990）。第三方 @onchain_duke 称 Spike NFTs 10,000 份 LayerZero FREE mint、日期 TBA，本轮未见 @Spike__wtf 本号官帖，不按新免费 mint 重推、不另开核验读。@UnseenOrdo 已在库（unseen-ordo，R59，upcoming）；本轮 MEN_BTC 25 条均为第三方称白名单/免费名额，90m 窗未见官号自帖，不把第三方 CTA 写成官宣开登记，未另开核验读。@Omni_Hub / Giwa x OmniHub mint 仅见 0 粉号转发官帖节选（Giwa is now LIVE），库内无 OmniHub 卡，本轮未拉 @Omni_Hub 时间线（禁额外确认读），不收录。MEN_DOGE / 瘦栏 24h 多为已在库号（XofN、GiwaTerminal、SaePad、Onggi、Dogstarter、SecretWiz、Lingxi、GAMA、Numen 等）或 KOL / Bramble 误伤。

## 窗口与在库刷新

- Vicehood（@vicehood_rh）售罄，本轮提醒：官帖 04:57:01 CST 宣布 SOLD OUT / Open reveal。链上 totalSupply 与 OpenSea 供应均为 3333/3333，持有 2358，地板 9.101e-05 ETH（R2257 为链上 3298、OS 3225、持有 2367、地板 9.405e-05 ETH）。公售原定 05:00 CST，售罄发生在 FCFS 结束前约 3 分钟，未见单独公售开闸官帖。免费 mint 已结束。铸页 https://opensea.io/collection/vchood CA 0x0648b448fe7b0bf828445a63a44927932f95d839。官帖 https://x.com/Vicehood_RH/status/2126057660642631860
- Babbles（@babblesxyz）付费公售已 LIVE，本轮提醒：官帖 05:00:02 CST 宣布 0.002611 ETH、每钱包 11、持续 24 小时。等待名单免费 mint 已于 05:00 CST 结束。链上/OS 仍 127（尚未见公售增量），持有 17、地板 0.0047 ETH。R2256 已按公售首次 <=2h 提醒，本轮按开闸翻转提醒。铸页 https://opensea.io/collection/babbles CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B。官帖 https://x.com/babblesxyz/status/2126058421791400301
- 2hour.fun Window two 已开窗，本轮提醒：官帖 05:00:03 CST 宣布开窗，至 23:00 UTC（07:00 CST）。免费发币，手续费 100% 自留至赚满 $100，Refund Bot 赔率 x10，周赛同步开始。/api/window 仍无开窗字段，本窗 traderCount=42（R2257 旧窗为 243）且已有成交，结合官帖按已开窗处理。R2254 已按首次 <=2h 提醒。https://www.2hour.fun/ 官帖 https://x.com/2hourfun/status/2126058423254966454
- Wildlife Universe（@wildlifeuni_55）免费公售已售罄，不重推：链上/OpenSea 5555/5555，持有 2962、地板 9.97e-05 ETH（R2257 为持有 2964、地板 0.000123 ETH）。R2253 已按售罄提醒。
- Lamoryant（@Lamoryant）原合约仍 publicEnabled=True，链上 698/1356（与 R2257 相同）。OpenSea lamoryant- 合集供应仍为 0，旧合集持有/地板沿用 R2257：OS 697、持有 639，公售价 0.001 ETH。官宣 OpenSea 铸造仍定 2026-11-27 19:00 CST，尚未开铸，不重推。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。
- Lanternhold（@Lanternhold）已售罄，不重推：链上/OS 2222/2222，持有 1423、地板 0.26 USDG（与 R2257 相同）。
- MaruTales（@MaruTalesStudio）：MUST_WIN 未见新官宣，铸造尚未 LIVE（0/444）。白名单核验仍开。R2245 已提醒，不重推。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 236.42M/600M（与 R2257 相同）。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=445,500,000 = 约 27/555（与 R2257 相同）。
- Ugly Puggies：RPC/OS 612，持有 384、地板 0.00013 ETH（与 R2257 相同），只是进度，不重推。
- F0B90B：642/10000（与 R2257 相同），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2257 相同），只是进度，不重推。
- The Jacket：RPC/OS 214/777，持有 133、地板 0.45 USDG（与 R2257 相同）。只是进度，不重推。
- Guns of the Hood：链上/OS 126，持有 19（stats 接口本轮 401，持有沿用 R2257）。只是进度，不重推。
- Rumble Hood（@Rumblehoodrh）：付费公开售仍 LIVE，不重推。链上/OpenSea 3614（R2257 为 3611）、持有 921、地板 0.05 USDG。未核到 MAX_SUPPLY，不以口头 4000 覆盖此前 6000 记录。R2013 已提醒开售。
- Shielded Wizards（brimhollow）：API 仍报 mintOpen=true，phase=public，159/3333（与 R2257 相同），reserved=3（R2257 为 2）。不按开铸重推。
- RuninAI：MUST_WIN 再见日常回复式窗口宣传，R2226 已提醒，不重推。
- GoaTs：MUST_WIN 未见开铸官帖，仍 Coming soon / Drop wallet，不是 LIVE。R2245 已收录，不重推。
- Canton / Glaze / TokenWorks Playground Watch lastChecked 已刷新，无实质变化。

## 规则核对

- 本轮无新卡。空轮芯片未造。收藏未改。未把普通项目标 focus。
- 判断/文案为 dsFallback（DeepSeek 持续 401），未用高成本模型批量打分。
- 已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
