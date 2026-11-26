# 早期打新雷达 R2247

- lastScout: 2026-11-26 23:42:52 CST
- notify: false
- alert: （无，不向用户推送）
- newAdmits: 无
- liveFlips: 无。Lanternhold 官宣 SOLD OUT（23:05:33 CST）是 R2246 已报 LIVE/接近售罄的后续确认，不重推。Wildlife / Babbles / QQAI / Shielded Wizards 等既有免费 LIVE 只刷新进度。
- firstLe2h: 无。Vicehood 仍 <=2h（11-27 01:00 CST，约 1.3h）但 R2246 已提醒，不重推。Wildlife 公售 11-27 02:29 CST 尚未进入首次 <=2h。
- xReads: 20（main 17 + silent 1 + 瘦栏 24h 2）
- remainingBefore: 230
- remainingAfter: 210
- mode: pace（remainingBefore 230 >> 200；计划 softCap 18 / minSpend 18 / silentCap 2 / eveningReserve 0）；未砍栏。MUST_WIN 作为首读兼额度探测，未另开探测读。实际主搜 17 = UF2 + MUST_WIN + MUST_PRI + 瘦栏 6 + 核心 3 + mentions 4；另 LZ 24h×1 + BTC 24h×1 + silent 1。
- 十栏关键词: 瘦栏 6 组 30m 全跑（LZ=0 TAPE=13 GIWA=22 DOGE=10 BTC=3 STARK=5）。核心轮换 3/5：挖矿 / GO盘 / 打新（KW_MINE=1，KW_GO=24，KW_MINT=25），补上轮顺延的挖矿、GO盘；台子/Meme、Elysium 按 pace 轮换顺延至下轮，不是整栏跳过。
- userFollow: 已刷完。cursor 1833 @PlayBitsigil → 1881 @Fistagent_（end @hoodfrenz，wrap=false，kept 48，total 2471）。UF1 n=0、UF2 n=9（UnicornGPrix / Forg3rApp / oaaprotocol，均为库内已收），未见须新收录的打新窗。
- mentions: GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25 触顶，MEN_TAPE 有命中，MEN_LZ=25 触顶，MEN_ELY=25 触顶）。各链本轮子集已扫，未偏科只扫 Elysium。
- mentionsNext: DogeEVM / BTC / Starknet / pads+squeek+STARX
- silent: Starknet（has:mentions only，本客户端 connectors/x 无 search_users；24h，n=25 触顶）。silentAccounts.ran=true，seen=25，sentToReview=0，admitted=0，skipped=多为 @Starknet 互动与 Bramble 噪声。silentNext: 打新
- 瘦栏 24h 补搜: LayerZero（30m=0 <5）补了 24h，LZ24=25 触顶，多为 WBTC/OFT/USDY 与第三方，未见未入库可操作新官号。BTC（30m=3 <5）补了 24h，BTC24=25 触顶，几乎全是 ShieldedNaka / RGB 生态二级市场与转帖，无新官号。跳过 Tape/GIWA/DogeEVM/Starknet（30m 已够：13/22/10/5）。
- MUST: MUST_WIN 已跑（n=4，有下一页未翻；页内仅 RuninAI 日常宣传与 Lanternhold SOLD OUT 官帖，下一页窗口仅约 32 秒，未翻）。MUST_PRI 已跑（0）。同一 handle 本轮只拉一次。Lanternhold / MaruTales / GoaTs 已合并进 MUST_WIN，未另开核验读。
- lastFullAfterReset: R2216
- dsFallback: true（DeepSeek 近期持续 HTTP 401，key 无效；判断/文案为本机 dsFallback，未改用高成本模型批量打分）
- discordPeekDeferred: true，loginOk=false。登录墙与约 R2206 起相同，本轮未开浏览器、不重发登录表单。lastSeen 未改，仍停在 2026-11-23 22:19–22:56 CST。须父代理在同一轮视会话情况补 Peek；若无新登录会话，勿再弹登录表。补扫若出现免费 mint/登记再通知。

## 窗口与在库刷新

- Lanternhold（@Lanternhold）已售罄，不重推：官帖 23:05:33 CST（https://x.com/Lanternhold/status/2125969212011126984）宣布 SOLD OUT（All 2,222 Founder's Lanterns are lit）。写盘链上 totalSupply=2222/2222，OpenSea 供应 2222、持有 1699、地板 0.28 USDG。11-27 00:00 CST Public 窗无剩余可铸。R2246 已提醒 LIVE/接近铸完。
- Vicehood（@vicehood_rh）仍 <=2h 但不是首次：首窗仍 2026-11-27 01:00 CST，写盘距约 1.3h。OpenSea vchood 供应 0、持有 0，状态仍 MINTING_SOON；链上 totalSupply=0。R2246 已提醒，不重推。
- MaruTales（@MaruTalesStudio）：铸造尚未 LIVE（MINTING_SOON，0/444，链上 0）。白名单核验仍开，日程不变。R2245 已提醒，不重推。
- Wildlife Universe（@wildlifeuni_55）免费 mint 仍 LIVE（不重推）：链上 3343/5555（R2246 为 3264），OpenSea 供应 3337、持有 1896、地板 0.00012 ETH，以链上为准。公售 11-27 02:29 CST 尚未到首次 <=2h。R2243 已提醒开窗。
- Babbles 等待名单免费 mint 仍 LIVE（不重推）：RPC/OS 125（与 R2246 相同），持有 15、地板 0.0088 ETH，至 2026-11-27 05:00 CST。R2242 已提醒开窗。
- Lamoryant 公售仍 LIVE（不重推）：RPC 689/1356，OS 689、持有 634，公售价 0.001 ETH（R2246 为 682/632）。R2241 已提醒公售开窗。
- Crawlers Agent：付费仍 LIVE，不重推。token 约 235.72M/600M，未见新的开铸翻转。
- Frost Hood：仍 GTD 免费登记、开铸自称 12-25。R2240 已提醒，不重推。
- QQAI（@QQAI_BNB）免费 mint 仍 LIVE（不重推）：paused=false，token totalSupply=445,500,000 = 约 27/555（与 R2246 相同）。
- Ugly Puggies：RPC/OS 602、持有 379、地板 0.00015 ETH（R2246 为 601/378），只是进度，不重推。
- F0B90B：608/10000（R2246 为 603），只是进度，不重推。
- Antopia：totalMinted 6438/8888（与 R2246 相同），只是进度，不重推。
- The Jacket：RPC/OS 214/777，持有 134、地板 0.45 USDG，只是进度，不重推。
- Guns of the Hood：OS 116、持有 18（与 R2246 相同），不重推。
- Shielded Wizards（brimhollow）：158/3333，reserved=1，phase=public（R2246 为 157），只是进度，不重推。
- 2hour.fun：/api/window 仍无开窗字段，traderCount=44，下一窗仍 2026-11-27 05:00–07:00 CST，不重推。
- RuninAI：每日 20:00 CST 窗口已过，R2226 已提醒，不重推。本轮官帖仍是日常窗口宣传。
- GoaTs（@GoaTopiax）：仍 Coming soon，不是 LIVE。R2245 已收录，不重推。
- Canton/Glaze/TokenWorks lastChecked 已刷新，无新 admit。

## 盲捞未收录

- 本轮无新收录。库内已见不重复建卡：UnicornGPrix、Forg3rApp、oaaprotocol、SaePadKR、famulusai、hoodbitio、artnesh/BAD APE、AntHood、VordaLaunch、Giwaterminal、T0dotfun、globemkts、x_MemeFactory_x、bark_swap、PairMineAI、CryptoSociety_L 等。
- @perpsonx / @NFTHUB_Drops 仅见第三方转赠 GTD 免费 mint 帖，本轮未核到官号主帖，未另开 X 核验读，未收录。
- @CminerB0x x @artnesh Bad Ape 赠送帖：@artnesh 库内已有 badape 卡，仍非已确认免费 mint LIVE，不重推。
- @Omni_Hub 第三方称 Giwa NFT mint LIVE，仅转帖未见官号主帖，未收录。
- KW_STARK 30m 5 条几乎全是 Bramble 服饰/刺猬/游戏噪声，无 Starknet 新项目。
- 空轮芯片未造。普通新卡未 focus。收藏未改。

## 面板

已写入 data.json 与 docs/data.json，推送 main 后见 https://reboot7454.github.io/early-scout/
