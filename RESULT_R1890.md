# RESULT R1890

- time: 2026-11-16 07:35 CST (Asia/Shanghai)
- mode: near-exhausted（remainingBefore 26<50）
- lastFullAfterReset: R1843（08:09 CST 的 08:00 后首轮全量补扫；本轮非补扫轮）
- xReads: 7（main 7 + silent 0）
- remaining: 26 → 19 / 1000
- softCap: 8，minSpend: 6，silentCap: 0
- notify: false
- newIds: 无
- dsFallback: false（无合格新卡，跳过录取/打分 DS；文案一次 DeepSeek 回合法 JSON）

## 本轮做什么

独立例行 near-exhausted 扫。开跑 `git pull` 已与 origin/main 同步（起点 commit c918d76 R1889）。按硬顺序：UF 分片软刷 → MUST 合并 live/优先号。因 remaining 26<50，薄栏/核心栏 KW、mentions、THIN official、silent 全部延后。DC 不登录，discordPeekDeferred=true。本号不自动 mint。

## X 额度与查询

remainingBefore=26。7 次读取后 remaining=19。页脚依次 25/24/23/22/21/20/19。

- UF1–UF5：0-based 1627 knitxdex 起 packed 5 片 kept 124（25+25+25+24+25），walk 中 NF_skip 0。walkScanned 124。lastKept pillowbookRH。next 1751 nihilo_fun。未回绕。
- MUST1：24 handles（live 窗口 + 部分优先号）。MUST2：4 个优先号（PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[pillowbookRH]（本轮已落入 UF5，未在 MUST 重读）。
- 薄栏六条 KW、核心栏 KW、THIN official、mentions 均因 near-exhausted 未跑。
- silentCap=0，未跑（本应 1890%11=9 BTC）。
- 禁止额外/重复 X 查询：无「再确认」重拉、无雷达外探索、不翻页 next_token。search_users 仍不在 X 目录。max_results 按接口上限 25。本轮实际使用 search_posts_all（目录无 search_posts_recent）并带 start_time 限 1h 官窗。

本窗官号有帖：@BoxcarsHQ、@rushrtrade、@OrreryNode、@Conway_IA、@Cyra_Dex、@foodcoinpf、@hwandotio、@infamousScratch、@HOKORI_QUANTUM、@tmachinroBot、@wrapped__eth。MUST2 本窗 0 帖。

## 十栏 / mentions / UF

- 十栏关键词：near-exhausted 全部延后。tenLaneKeywordsComplete=false。
- userFollowWatch：本轮分配的 5 片刷完（kept 124），userFollowWatchComplete=true（整表仍按游标轮转，未在本轮扫完全表）。
- mentions 本轮：延后未跑。下一轮仍为 LayerZero / Elysium+kinetiq（若开跑仍 <50 则继续延后；08:00 CST 后首轮必须全量补扫）。
- silent 本轮：BTC（1890%11=9）因 silentCap=0 未跑，ran=false。下一轮：Starknet（1891%11=10）。
- fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。未刷四表 FAT 分片。
- Watch 漏挂扫描（round≥1840）：0 leaks。
- soft-debt lastChecked 已刷新：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch。

## 新收录

- 无。短名单均为在库官号本窗更新：Boxcars 开盘箱子奖励说明与驾照进度 179→321/1000；Hokori 即将燃烧并转换 2000 万已解锁开发者 Solana $HKR 至 Starknet $HKR；Rushr 白皮书/团队钱包说明；Orrery 本地路由产品说明；Conway-01 主网支付安全长帖；以及 R1888 已记的 POLYROB 费用说明与 Wrapped Explorer 上线同窗帖。Cyra_Dex / foodcoinpf / hwandotio / infamousScratch 本窗仅为互动或既有产品说明，无新 mint 窗口。

## 在库窗口

- DeadHood（@DeadHood_nft）：本窗官号无新帖。OpenSea HTTP 200：仍 777/777、remainingSupply=0、isMinting=false。价仍约 0.0005 ETH public。集合页 CA `0xcbda7f2e83fe2e9b2a2b53054e887d519728a144` 仍为 os-sourced，非官推核验 CA。上轮已按售罄提醒，不重推。
- Creedo（@UseCreedo）：本窗无新官帖。官网 HTTP 200，官方 CA 仍为 `5THxr2CziUhysD6Un7BctHqfv9uBcE6JasqKVCCREEDo`。空投仍写 Dec 2026 / Q1 未开始。同一份 LIVE+官方 CA，不重推。le2h=false。
- Plato / The Unseen（@PlatoUnseen）：本窗官号无新帖。OpenSea HTTP 200，现 134/520 剩余 386（上轮 133/520 剩余 387）。价仍 0 ETH+gas，1/钱包，至 2026-11-25T18:00:00Z（Nov 25 1 PM ET）。页面 isMinting=false 不作关闭依据。官推仍未公布 CA。OpenSea 集合页地址 `0x47fc75e1620437930d42607f1170cf92b2915217` 仅作 os-sourced 记录，不得写成官推已核验 CA。进度 +1，不重推。le2h=false。
- Q-TRON LAPTOPS（@qtronlaptops）：本窗官号无新帖。OpenSea HTTP 200，仍 51/4444 剩余 4393。价仍 0.000526 ETH、15/钱包。集合页 CA `0x39f2484ab88ccb03b8b0f947e72705116a88e07f` 未变。Public Stage 结束时间为 2026-11-17T19:15:00Z，非 ≤2h。付费公售，同价同进度，不重推。le2h=false。
- POLYROB（@tmachinroBot）：本窗再次命中 06:31 CST https://x.com/tmachinroBot/status/2122095134686720160 费用说明回复（R1888 已记）。官网 HTTP 200，仍 0.033 ETH、上限 504、售完为止、无截止。静态页 minted 为 JS 占位（0 of 504），不能当成已铸 0。官方已铸仍记 59。不是新 mint 窗口，不重推。粉仍 1510。
- Agent Life（@Agentlifebnb）：本窗官号无新帖。官网 / 与 /mint HTTP 200；/refund、/refunds、/claim 仍 404，首页无退款入口。官网链出 ALIFE `0x401667A68672A0B14A059B1a61b7d7181646D515` 仍非官推核验 CA。已按「倒计时退款公告、入口未开」提醒，不重推。
- Bitsigil（@PlayBitsigil）：仍售罄，OpenSea 3333/3333、remainingSupply=0。本窗无新 mint 窗口，不把同一份 SOLD OUT 再推。
- SpoxyFun（@SpoxyGang）：本窗官号无新帖。站点 HTTP 200。维持 0.001 BNB / 2222；免费 800/800 已售罄、付费仍开放。已记录的质押/付费窗口不重推。
- pillowbook-rh：本窗官号无新帖（本轮落入 UF5，未在 MUST 重读）。官网 pillowbook.pro 再次 TLS 失败（unexpected eof while reading），未见 CA/开盘证据，不得写成已开盘。已在 R1873 提醒，不重推。le2h=false。
- jacketagent：已提醒付费阶段，本窗无新官帖；站点 HTTP 200，NFT CA 仍 `0x70FdD1a7f382893708d00fC2eF9C38cAe7DEC92B`，marketCA 仍 `0x043d60d568456DE954D405cf69ABf65C624c4139`。页面进度为 JS 占位，不覆盖已记进度。不重推。
- ozero（@ozero_fun）：官网 HTTP 200，页面仍含 Base Sepolia Testnet。未见主网 mint。同一份测试网，不重推。le2h=false。
- wrapped-eth（@wrapped__eth）：本窗再次命中 06:30 CST https://x.com/wrapped__eth/status/2122094802804355198 Explorer 上线帖（R1888 已记）。https://wrapped.wtf/explore HTTP 200，https://wrapped.wtf/claim 仍 404。首页与 docs / explore HTML 未解析出 0x 合约地址，不得写成已核验 CA。不是新的 claim 窗口，不重推。粉仍记 41。
- Hokori（@HOKORI_QUANTUM）：07:11 CST https://x.com/HOKORI_QUANTUM/status/2122105289461895486 称即将把 2000 万已解锁开发者 Solana $HKR 燃烧并转换为 Starknet $HKR。https://hokori.io HTTP 200。这是代币燃烧/跨链转换预告，不是 mint/登记窗口，不重推。粉 304→305。
- TapeMine（@tapemineworld）：本 1h 官窗无新帖，维持 Behemoth 二期进度（471/500 NAND），不重推。
- sunfall-world（@SunfallWorld）：已在库（R1620，live 城市场）。本 1h 官窗无新帖。官网 sunfall.world HTTP 200，页面仍展示 $SUNFALL CA `0x49A591bEb2a77ddcF41758F4E99126bc0510EA40`（卡内已有）。Season 1 于 08:00 CST 结束为 R1888 已记赛季更新，不是新的 mint/登记窗口，le2h=false，不 notify。粉仍 150。
- Boxcars（@BoxcarsHQ）：已在库（R1766 已按免费驾照通知）。06:59 CST https://x.com/BoxcarsHQ/status/2122102141800034803 宣布开盘箱子：领驾照得 1 个免费箱，预售每投 0.05 BNB 加 1 箱（最多 4），邀请并成交的好友再加 1 箱（最多 4），10 个零件合成一辆车。官网 playboxcars.com HTTP 200。BSC 链上驾照 NFT `0x4084d67c1D7EdAA609DF0c860C57454f46219217` totalSupply 179→321/1000。预售仍 11-17 21:00 CST，非≤2h。箱子是已通知免费驾照+预售上的奖励机制，不是新的独立 mint 窗口；进度刷新不重推。粉 29→100。

## silent / 候选

- silentAccounts.ran=false（silentCap=0）。seen=0，sentToReview=0，admitted=0。
- deferredHandles：hyperhaul / p2eabs / ZeroHoppersNFT 继续结转（第三方 @提及待解析，0 帖空壳无新证据，不重录）。不要把下一轮 silentCap 花在 bitcoincoreorg 或 StreetHoodMedia。

## 推送

- 只提交 data.json、docs/data.json、RESULT_R1890.md 到 main。收藏未改。未设 focus。空轮芯片未造。本号不自动 mint。
- notify=false：无新收录、无≤2h 可操作 mint/登记窗口、无新免费 LIVE，已提醒窗口仅同窗维持/产品说明或已上线功能更新，无改价/改入口/官推核验 CA/售罄等关键变化。Boxcars 开盘箱子属于已通知免费驾照+预售上的奖励机制，驾照 179→321/1000 仅进度刷新，预售尚未进入 ≤2h，不重推。Hokori 燃烧/跨链转换预告不是 mint/登记窗口。Sunfall Season 1 结束属于已上线城市场的赛季更新，不按 mint 窗口 ≤2h 推送。

## 交接（R1891）

- lastFullAfterReset 保持 R1843。
- remaining 19 < 50，下一轮仍 near-exhausted（若开跑 remaining<50 则继续延后关键词/mentions/silent，但仍先查额度。08:00 CST 后首轮必须全量补扫）。
- UF next：0-based 1751 / handle nihilo_fun。
- mentions next：LayerZero / Elysium+kinetiq（本轮未跑，不推进轮换；若 remaining≥50 再跑这 2 组，否则继续延后至 08:00 CST 后首轮全量补扫）。
- silent next：Starknet（1891%11=10）。search_users 仍不可用则只走 mentions；若 silentCap=0 则 ran=false。勿把 silentCap 花在 bitcoincoreorg；勿把 StreetHoodMedia 塞进 silentCap。
- fatNextStarts 不变。
- 已提醒窗口不要因同一变化再推：DeadHood 已按「OpenSea 售罄 777/777，价仍 0.0005 ETH，官号无新帖，CA 非官推核验」提醒，后续除非出现与已通知内容不同的关键变化（例如官推公布 CA 或新窗口），否则不重推；Agent Life 已按「倒计时退款公告、入口未开、官网链出 ALIFE 非官推核验 CA」提醒，后续除非退款入口真正开放、官推公布 CA、站点正式关铸、官方更新已售/退款进度，或出现与已通知内容不同的关键变化，否则不重推；Creedo 同一份 LIVE+官方 CA（空投仍写 Dec 2026 / Q1 未开始）不重推，除非改 CA、停盘或出现与已通知内容不同的关键变化；Plato 同一份「剩余铸免费」不重推（进度现 134/520），除非售罄、改价/改入口，或官推公布已核验 CA（OpenSea 集合地址不算官推核验 CA）；Q-TRON Public 已按同一时间表开始且同价（51/4444，0.000526 ETH，15/钱包已写入卡片），不重推，除非售罄、改价/改入口、官推已核验 CA，或出现与已通知内容不同的关键变化；POLYROB 同一份「维持开放 / 官方已铸仍记 59、上限 504」不重推，除非售罄或改价/改入口，勿用 JS 占位覆盖官方 59，同窗再次出现的 06:31 CST 费用说明回复也不构成重推；Bitsigil 同一售罄不重推；Spoxy 同一份质押上线/付费仍开放不重推；pillowbook 同一未开盘窗口不重推，除非真正开盘并公布 CA；jacketagent 已提醒付费阶段无新变化不重推；ozero 同一份 Base Sepolia 测试网宣传不重推，除非出现主网 mint 或与已通知内容不同的关键变化；wrapped-eth 已按真新提醒，本轮再次命中的 06:30 CST Explorer 上线帖且 /claim 仍 404、HTML 未见核验 CA，后续若只是同一份包装台观察、文档或浏览器功能说明、无 CA/入口/claim 入口实质变化，不重推；Hokori 同一份「即将把 2000 万已解锁开发者 Solana $HKR 燃烧并转换为 Starknet $HKR」预告不重推，除非出现 mint/登记窗口、转换实际发生并带来新的可操作入口，或出现与已通知内容不同的关键变化；TapeMine 同一份 Behemoth 二期进度（现 471/500 NAND）不重推，除非二期完成、新一期开启，或出现与已通知内容不同的关键变化；sunfall-world 已是 live 城市场，Payout #5 与 Season 1 于 08:00 CST 结束的预告（R1888 已记）不重推，除非出现新的 mint/登记窗口、改 CA，或与已通知内容不同的关键变化；Ringssol 同一份已在库实验发射台/终端的 hSOL 配对与基础设施/配置更新不重推，除非出现新的可操作 mint/登记窗口或与已通知内容不同的关键变化；raccoonslimestd 仍在选择发射台、未开盘，不重推，除非真正选定并开盘；Elysium Portals 同一份 announced / 免费登记且未见合约上线不重推，除非合约上线或开铸时钟明确；Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期、开窗，或出现与已通知内容不同的关键变化；boxcars 已按免费驾照通知，本轮开盘箱子奖励与驾照 321/1000 进度刷新不重推，除非预售开盘/改期、驾照售罄、改入口/改 CA，或出现与已通知内容不同的关键变化。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint。
