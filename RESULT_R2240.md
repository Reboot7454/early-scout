# 早期打新雷达 R2240

- lastScout: 2026-11-26 20:18:38 CST
- notify: true
- alert: 早期打新雷达 R2240：Lamoryant（@Lamoryant）白名单/FCFS 已 LIVE，免费 OG 已结束（官帖 20:00:12 CST 宣布 WHITELIST MINT IS LIVE，本阶段约 30 分钟后进公售）。链上 2026-11-26 20:18:38 CST 核到 gtdEnabled=false、fcfsEnabled=true、publicEnabled=false，622/1356，FCFS 0.0018 ETH / 每钱包最多 10，公售价 0.002 ETH。铸页 https://lamoryant.com/mint  CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。Crawlers Agent（@CrawlersAgent）官帖 20:00:05 CST 宣布 Mint is open / $CA live；无网页 mint 按钮、不用连钱包，需把站点提示词交给 Agent 铸造。6000 份，0.004 BNB，每钱包最多 10，仅限 Agent ID。付费，不是免费 mint。新收录 Babbles（@babblesxyz）官方 waitlist 免费 mint 将于 21:00 CST（13:00 UTC）开，每钱包 1 份、仅 gas；以太坊 CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B，OpenSea collection/babbles 此刻供应仍 0，不是已开铸。新收录 Frost Hood（@FrostHoodR）GTD 免费登记已开（经官网申请并在评论丢钱包），自称 2500 份 Genesis 免费 mint，开铸自称 2026-12-25，不是今天已开铸 LIVE。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
- newAdmits: Babbles（@babblesxyz）— waitlist 免费 mint 21:00 CST，尚未 LIVE；Frost Hood（@FrostHoodR）— GTD 免费登记已开，开铸自称 12-25
- liveFlips: Lamoryant 白名单/FCFS LIVE（免费 OG 结束，622/1356）；Crawlers Agent 官帖宣布 Mint is open（付费 0.004 BNB，不是免费 mint）
- firstLe2h: Babbles waitlist 免费 mint 21:00 CST（OS 供应仍 0）。Wildlife 仍 ≤2h（21:30 CST）但 R2239 已提醒，不重推。
- xReads: 22（searchPostsAll 21 + getUsersByUsernames 1；其中 silent 1、24h 补搜 3、新号核验 1）
- remainingBefore: 376
- remainingAfter: 354
- mode: pace（remainingBefore 376 ≫ 200；计划 softCap 18 / minSpend 18 / silentCap 2 / eveningReserve 80）；未砍栏。实际 22 是 17 次主搜 + 3 次瘦栏 24h + 1 silent + 1 次新候选 getUsersByUsernames（babbles/FrostHood 等），略超 softCap。
- 十栏关键词: 瘦栏 6 组 30m 全跑（LZ=2 TAPE=25 GIWA=23 DOGE=7 BTC=1 STARK=1）。核心轮换 3/5：打新(KW_MINT=25) / 台子/Meme(KW_PAD=25) / Elysium(KW_ELY=22)；挖矿、GO盘按 pace 轮换顺延至下轮。不是整栏跳过。
- userFollow: 已刷完。cursor 1497 @eslashacc → 1545 @corporation_sh（end @Ponstier_vip，wrap=false，kept 48）。UF1=0、UF2=1（仅已在库 Elypx402），无新打新。
- mentions: DogeEVM / BTC / Starknet / pads+squeek+STARX（MEN_DOGE=8，MEN_BTC=25 触顶且多为 UnseenOrdo/RGBHorse 拉人垃圾，MEN_STARK=5 无新打新，MEN_PADS=25 触顶多为 flap 闲聊）。各链本轮子集已扫，未偏科只扫 Elysium。
- mentionsNext: GIWA / Tape / LayerZero / Elysium
- silent: GO盘（has:mentions only，本客户端 connectors/x 无 search_users；n=3，全是英文 launch 误伤，无新收录）。silentNext: LayerZero
- 瘦栏 24h 补搜: LayerZero=23、BTC=25、Starknet=25（30m 均 <5：2/1/1）。跳过 Tape/GIWA/DogeEVM（30m 已够：25/23/7）。
- MUST: MUST_WIN=17、MUST_OFF=2。同一 handle 本轮只拉一次。为收录核验对 @babblesxyz / @FrostHoodR 等做了 1 次 getUsersByUsernames（非重复确认）。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek HTTP 401，key 无效；判断/文案为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19–22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 窗口与在库刷新

- **Lamoryant（@Lamoryant）白名单/FCFS 已 LIVE（必须提醒）**：官帖 2026-11-26 20:00:12 CST（https://x.com/Lamoryant/status/2125922567362121748）宣布 WHITELIST MINT IS LIVE，本阶段约 30 分钟后进公售。免费 OG 已结束。RPC 2026-11-26 20:18:38 CST：totalMinted()=622 / MAX_SUPPLY()=1356（R2239=372；OpenSea 20:10=616）；gtdEnabled=false，fcfsEnabled=true，publicEnabled=false；FCFS 0.0018 ETH、每钱包最多 10，公售价 0.002 ETH。静态 mint 页倒计时可能仍是 JS 占位，不以静态 HTML 为准。铸页 https://lamoryant.com/mint CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。本号不自动 mint。
- **Crawlers Agent（@CrawlersAgent）首次开铸 LIVE（必须提醒，付费）**：官帖 2026-11-26 20:00:05 CST（https://x.com/CrawlersAgent/status/2125922539033497705）宣布 Mint is open / $CA is live now。无网页 mint 按钮、不用连钱包，需把站点提示词交给 Agent 铸造。6,000 shares · 0.004 BNB · 每钱包最多 10 · 仅限 Agent ID。官网静态仍可能显示 OPENING SOON，以官帖为准。自称 CA 0x5c92D8b2aa748722D7855CD4493F208f66757fd6，本轮 getCode 为空，不把 token totalSupply 当作已铸份额。不是免费 mint。R2236 已首次 ≤2h，本轮是开窗翻转。
- **Babbles（@babblesxyz）新收录 + 首次 ≤2h 免费 waitlist mint（必须提醒）**：官帖 20:00:02 CST 称 21:00 CST（13:00 UTC）开，免费、每钱包 1、仅 gas。官网 https://beltek.xyz/babbles ，以太坊 CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B，OpenSea collection/babbles 供应仍 0，不是已开铸 LIVE。置顶已提醒仿盘。已进 userFollowWatch + freeMintWatch。focus=false。
- **Frost Hood（@FrostHoodR）新收录，GTD 免费登记已开（必须点名）**：官帖 2026-11-25 22:36:30 CST 宣布 GTD 申请已开，官网 https://frosthood.framer.ai/，自称 2500 份 Genesis 免费 mint，开铸自称 2026-12-25，不是今天已开铸。R2239 仅见转推未核验故未收，本轮已核验。已进 userFollowWatch + freeMintWatch。focus=false。不要回复地址。
- Wildlife Universe（@wildlifeuni_55）仍 ≤2h（不重推）：官网仍 21:30 CST（7:00 PM IST），OpenSea/链上供应仍 0，不是已开铸。写盘距首窗约 1.2h。R2239 已首次提醒，未开铸不重推。勿与旧卡 wildlife-uni（@wildlife_uni）混淆。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=214,500,000 = 约 13/555（与 R2239 相同）。不重推。
- Ugly Puggies：RPC/OpenSea 577/777（R2239=571），只是进度，不重推。持有本轮未新核，沿用 362。
- F0B90B：572/10000（R2239=558），只是进度，不重推。
- Antopia：totalMinted 6364/8888（R2239 沿用 6359），totalSupply() 仍回退，只是进度，不重推。
- The Jacket：RPC 214/777（与 R2239 相同），持有/地板未新核，不重推。
- Vicehood 本轮未重拉 OpenSea，首窗仍 2026-11-27 01:00 CST，写盘距首窗约 4.7h，未到首次 ≤2h，不重推。
- 2hour.fun / RuninAI / TRIFORGE / Shielded Wizards / Guns of the Hood 本轮未重核，沿用 R2239，不重推。
- Canton/Glaze/TokenWorks lastChecked 已刷新，无新 admit。

## 新收录

- **Babbles（@babblesxyz）**：2026-10-18 04:26:11 CST 建号，69 粉 / 54 帖。官帖 2026-11-26 20:00:02 CST 宣布 waitlist 免费 mint 21:00 CST 开，每钱包 1、仅 gas。官网 https://beltek.xyz/babbles HTTP 200；OpenSea 官集与 CA 0x8bCF53fF0c709Aa63c93E7bCF1A8f4Df9F3D173B 互证，本轮供应 0。siteXMutual=true。已进 UF + freeMintWatch。dsFallback 评分 early 82 / overall 80 / risk 58。focus=false。
- **Frost Hood（@FrostHoodR）**：2026-11-22 17:44:01 CST 建号，36 粉 / 3 帖。官帖 2026-11-25 22:36:30 CST 宣布 GTD 申请已开，Genesis 自称免费 mint，开铸自称 2026-12-25。官网 https://frosthood.framer.ai/ HTTP 200。siteXMutual=partial，未见 CA。已进 UF + freeMintWatch。dsFallback 评分 early 92 / overall 72 / risk 80。focus=false。

## 盲捞未收录

- @Thenoonesnft：第三方 @Cryptoh89269075 24h 抽奖式给 GTD/FCFS，不是已确认开铸，未收录。
- @lumixpad / lumixpad.fun：自称 0% fee Solana 发射台，账号 2023-09-05 建但仅 22 粉 / 3 帖；本轮无官帖宣布已 LIVE，仅见 @coachchesterlee 称 $LUMIX 后 12-24h 上线，过薄且非官方开台确认，未收录。
- @DeSpellApp：GIWA First Wave 应用层，2026-07-26 建号，不是免费 mint / 开台窗口，本轮不建卡。
- @Poly1Protocol、@betraying_ai：无独立开铸/免费登记官帖，未收录。
- @AmmoraEco：已在库 Ammora 生态号，不另开新卡。
- @beavzclub / @thenottiesworld / @Niblekins / @AI_SlopRH / @wiseguyzRH：均已在库。Beavz 仍是丢钱包 GTD、无官网无 CA，不重推；Notties Lab Escape 是赚积分小游戏，官网集合仍未开铸翻转，不重推；Niblekins 白名单此前已记，本轮仅 1 粉路人复述，不重推。
- Buzzchain「主网可访问」来自 10 粉 @Parkseojungi，不是 @buzzchain_io 官帖，不翻转 LIVE。
- 空轮芯片未造。普通新卡未 focus。收藏未改。

## 面板

已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
