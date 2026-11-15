# RESULT R1889

- time: 2026-11-16 07:07 CST (Asia/Shanghai)
- mode: near-exhausted（remainingBefore 34<50）
- lastFullAfterReset: R1843（08:09 CST 的 08:00 后首轮全量补扫；本轮非补扫轮）
- xReads: 8（main 8 + silent 0）
- remaining: 34 → 26 / 1000
- softCap: 8，minSpend: 6，silentCap: 0
- notify: false
- newIds: 无
- dsFallback: false（无合格新卡，跳过录取/打分 DS；文案一次 DeepSeek 回合法 JSON）

## 本轮做什么

独立例行 near-exhausted 扫。开跑 `git pull` 已与 origin/main 同步（起点 commit e9a1d28 R1888）。按硬顺序：UF 分片软刷 → MUST 合并 live/优先号。因 remaining 34<50，薄栏/核心栏 KW、mentions、THIN official、silent 全部延后。DC 不登录，discordPeekDeferred=true。本号不自动 mint。

## X 额度与查询

remainingBefore=34。8 次读取后 remaining=26。页脚依次 33/32/31/30/29/28/27/26。

- UF1–UF5：0-based 1502 wikifork 起 packed 5 片 kept 125（26+25+25+24+25），walk 中 NF_skip 0。walkScanned 125。lastKept zxoxocash。next 1627 knitxdex。未回绕。
- UF1 首次查询中间 handle 写错（首尾正确，中间误入 AIAgent_OSK / jacketagent 等非本片号）。已用 UF1b 只补扫漏掉的 18 个未读号，未重读已命中的 8 个重叠号；UF3 去掉已误读的 AIAgent_OSK，UF4 去掉已误读的 jacketagent。这是纠错补扫，不是「再确认」重拉。因此本轮主扫实际为 8 次，顶到 softCap 8（仍满足 minSpend 6）。
- MUST1：24 handles（live 窗口 + 部分优先号 + SunfallWorld），qlen 502。MUST2：3 个优先号（localbottomcom / NutshellMarkets / starx_xlayer），qlen 78。mustSkip=[AIAgent_OSK, jacketagent]（本轮已落入 UF 分片，未在 MUST 重读）。
- 薄栏六条 KW、核心栏 KW、THIN official、mentions 均因 near-exhausted 未跑。
- silentCap=0，未跑（本应 1889%11=8 DogeEVM）。
- 禁止额外/重复 X 查询：除上述 UF1 纠错补扫外，无「再确认」重拉、无雷达外探索、不翻页 next_token。search_users 仍不在 X 目录。max_results 按接口上限 25。

本窗官号有帖：@inklegions、@hoodicorns、@PortalToElysium、@aurbitdotfun、@raccoonslimestd、@Ringssol、@Artefact_btc、@Popo_oneth、@infamousScratch、@tmachinroBot、@wrapped__eth、@SunfallWorld。UF1b / UF3 / MUST2 本窗 0 帖。MUST1 同窗再次命中 POLYROB 费用说明、wrapped Explorer 上线、Sunfall Payout #5（均 R1888 已记）。

## 十栏 / mentions / UF

- 十栏关键词：near-exhausted 全部延后。tenLaneKeywordsComplete=false。
- userFollowWatch：本轮分配的 5 片刷完（kept 125），userFollowWatchComplete=true（整表仍按游标轮转，未在本轮扫完全表）。
- mentions 本轮：延后未跑。下一轮仍为 LayerZero / Elysium+kinetiq（若开跑仍 <50 则继续延后；08:00 CST 后首轮必须全量补扫）。
- silent 本轮：DogeEVM（1889%11=8）因 silentCap=0 未跑，ran=false。下一轮：BTC（1890%11=9）。
- fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。未刷四表 FAT 分片。
- Watch 漏挂扫描（round≥1840）：0 leaks。
- soft-debt lastChecked 已刷新：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch。

## 新收录

- 无。短名单均为在库官号本窗更新：Ringssol 实验发射台配对 hSOL 与基础设施/配置调整、raccoonslimestd 仍在选择发射台、Elysium Portals 互动问句、Ink Legions 社区回复，以及 R1888 已记的 POLYROB / Wrapped Explorer / Sunfall 同窗帖。

## 在库窗口

- DeadHood（@DeadHood_nft）：本窗官号无新帖。OpenSea HTTP 200：仍 777/777、remainingSupply=0、isMinting=false。价仍约 0.0005 ETH public。集合页 CA `0xcbda7f2e83fe2e9b2a2b53054e887d519728a144` 仍为 os-sourced，非官推核验 CA。上轮已按售罄提醒，不重推。
- Creedo（@UseCreedo）：本窗无新官帖。官网 HTTP 200，官方 CA 仍为 `5THxr2CziUhysD6Un7BctHqfv9uBcE6JasqKVCCREEDo`。空投仍写 Dec 2026 / Q1 未开始。同一份 LIVE+官方 CA，不重推。le2h=false。
- Plato / The Unseen（@PlatoUnseen）：本窗官号无新帖。OpenSea HTTP 200，仍 133/520 剩余 387。价仍 0 ETH+gas，1/钱包，至 2026-11-25T18:00:00Z（Nov 25 1 PM ET）。页面 isMinting=false 不作关闭依据。官推仍未公布 CA。OpenSea 集合页地址 `0x47fc75e1620437930d42607f1170cf92b2915217` 仅作 os-sourced 记录，不得写成官推已核验 CA。同进度，不重推。le2h=false。
- Q-TRON LAPTOPS（@qtronlaptops）：本窗官号无新帖。OpenSea HTTP 200，仍 51/4444 剩余 4393。价仍 0.000526 ETH、15/钱包。集合页 CA `0x39f2484ab88ccb03b8b0f947e72705116a88e07f` 未变。Public Stage 结束时间为 2026-11-17T19:15:00Z，非 ≤2h。付费公售，同价同进度，不重推。le2h=false。
- POLYROB（@tmachinroBot）：本窗再次命中 06:31 CST https://x.com/tmachinroBot/status/2122095134686720160 费用说明回复（R1888 已记）。官网 HTTP 200，仍 0.033 ETH、上限 504、售完为止、无截止。静态页 minted 为 JS 占位（0 of 504），不能当成已铸 0。官方已铸仍记 59。不是新 mint 窗口，不重推。粉仍 1510。
- Agent Life（@Agentlifebnb）：本窗官号无新帖。官网 / 与 /mint HTTP 200；/refund、/refunds、/claim 仍 404，首页无退款入口。官网链出 ALIFE `0x401667A68672A0B14A059B1a61b7d7181646D515` 仍非官推核验 CA。已按「倒计时退款公告、入口未开」提醒，不重推。
- Bitsigil（@PlayBitsigil）：仍售罄，OpenSea 3333/3333、remainingSupply=0。本窗无新 mint 窗口，不把同一份 SOLD OUT 再推。
- SpoxyFun（@SpoxyGang）：本窗官号无新帖。站点 HTTP 200。维持已记录的质押上线 0.001 BNB / 2222，不重推。
- pillowbook-rh：本窗官号无新帖。官网 pillowbook.pro 再次 TLS 失败（unexpected eof while reading），未见 CA/开盘证据，不得写成已开盘。已在 R1873 提醒，不重推。le2h=false。
- jacketagent：已提醒付费阶段，本窗无新官帖；站点 HTTP 200，NFT CA 仍 `0x70FdD1a7f382893708d00fC2eF9C38cAe7DEC92B`，marketCA 仍 `0x043d60d568456DE954D405cf69ABf65C624c4139`。不重推。
- ozero（@ozero_fun）：官网 HTTP 200，页面 meta 仍写 Base Sepolia Testnet live。未见主网 mint。同一份测试网，不重推。le2h=false。
- wrapped-eth（@wrapped__eth）：本窗再次命中 06:30 CST https://x.com/wrapped__eth/status/2122094802804355198 Explorer 上线帖（R1888 已记）。https://wrapped.wtf/explore HTTP 200，https://wrapped.wtf/claim 仍 404。首页与 docs / explore HTML 未解析出 0x 合约地址，不得写成已核验 CA。不是新的 claim 窗口，不重推。粉 40→41。
- Hokori（@HOKORI_QUANTUM）：本 1h 官窗无新帖。https://hokori.io HTTP 200。维持已记的「Bramble 钱包已在 hokori.io 上线」，不是新 mint/登记窗口，不重推。
- TapeMine（@tapemineworld）：本 1h 官窗无新帖，维持 Behemoth 二期进度（471/500 NAND），不重推。
- sunfall-world（@SunfallWorld）：已在库（R1620，live 城市场）。本窗再次命中 06:09 CST https://x.com/SunfallWorld/status/2122089671593246724（R1888 已记 Payout #5 与 Season 1 于 00:00 UTC / 08:00 CST 结束）。官网 sunfall.world HTTP 200，页面仍展示 $SUNFALL CA `0x49A591bEb2a77ddcF41758F4E99126bc0510EA40`（卡内已有）。这是已上线城市的赛季更新，不是新的 mint/登记窗口，le2h=false，不 notify。粉仍 150。
- Ringssol（@Ringssol）：已在库（R1754，watching）。06:11 CST https://x.com/Ringssol/status/2122090258292490622 称 Rings Launch now pairs with hSOL（t.co 展开为 https://launch.rings.run）；随后写网站流量大、升级基础设施，以及 OTC Desk / Launchpad / Dex 配置调整。rings.run HTTP 200；terminal.rings.run 本轮 TLS 失败。属已在库实验发射台/终端的产品更新，不是新的免费 mint 或 ≤2h 窗口，不 notify。粉 336→492。
- raccoonslimestd（@raccoonslimestd）：已在库。本窗官号回复称仍在权衡发射台（Robinhood 生态与 pump.fun），尚未选定、未开盘，不 notify。粉 14→46。
- Elysium Portals（@PortalToElysium）：已在库（R1744，announced）。06:51 CST https://x.com/PortalToElysium/status/2122100305861001544 只是互动问句。官网 https://elysiumportals.xyz/ HTTP 200，页面仍写 Free mint for everyone who bridged to Elysium，HTML 未见 0x 合约，未见合约上线，不 notify。
- Ink Legions（@inklegions）：已在库（upcoming）。06:01 CST https://x.com/inklegions/status/2122087705425158489 为社区回复，不是改期。开铸仍为 2026-11-17 03:00 CST，免费 mint，非 ≤2h，不重推。粉 74→146。

## silent / 候选

- silentAccounts.ran=false（silentCap=0）。seen=0，sentToReview=0，admitted=0。
- deferredHandles：hyperhaul / p2eabs / ZeroHoppersNFT 继续结转（第三方 @提及待解析，0 帖空壳无新证据，不重录）。不要把下一轮 silentCap 花在 bitcoincoreorg 或 StreetHoodMedia。

## 推送

- 只提交 data.json、docs/data.json、RESULT_R1889.md 到 main。收藏未改。未设 focus。空轮芯片未造。本号不自动 mint。
- notify=false：无新收录、无≤2h 可操作 mint/登记窗口、无新免费 LIVE，已提醒窗口仅同窗维持/产品说明或已上线功能更新，无改价/改入口/官推核验 CA/售罄等关键变化。Sunfall Season 1 结束属于已上线城市场的赛季更新，不按 mint 窗口 ≤2h 推送。Ringssol hSOL 配对与基础设施更新不按新 mint 窗口推送。

## 交接（R1890）

- lastFullAfterReset 保持 R1843。
- remaining 26 < 50，下一轮仍 near-exhausted（若开跑 remaining<50 则继续延后关键词/mentions/silent，但仍先查额度。08:00 CST 后首轮必须全量补扫）。
- UF next：0-based 1627 / handle knitxdex。
- mentions next：LayerZero / Elysium+kinetiq（本轮未跑，不推进轮换；若 remaining≥50 再跑这 2 组，否则继续延后至 08:00 CST 后首轮全量补扫）。
- silent next：BTC（1890%11=9）。search_users 仍不可用则只走 mentions；若 silentCap=0 则 ran=false。勿把 silentCap 花在 bitcoincoreorg；勿把 StreetHoodMedia 塞进 silentCap。
- fatNextStarts 不变。
- 已提醒窗口不要因同一变化再推：DeadHood 已按「OpenSea 售罄 777/777，价仍 0.0005 ETH，官号无新帖，CA 非官推核验」提醒，后续除非出现与已通知内容不同的关键变化（例如官推公布 CA 或新窗口），否则不重推；Agent Life 已按「倒计时退款公告、入口未开、官网链出 ALIFE 非官推核验 CA」提醒，后续除非退款入口真正开放、官推公布 CA、站点正式关铸、官方更新已售/退款进度，或出现与已通知内容不同的关键变化，否则不重推；Creedo 同一份 LIVE+官方 CA（空投仍写 Dec 2026 / Q1 未开始）不重推，除非改 CA、停盘或出现与已通知内容不同的关键变化；Plato 同一份「剩余铸免费」不重推（进度现仍 133/520），除非售罄、改价/改入口，或官推公布已核验 CA（OpenSea 集合地址不算官推核验 CA）；Q-TRON Public 已按同一时间表开始且同价（51/4444，0.000526 ETH，15/钱包已写入卡片），不重推，除非售罄、改价/改入口、官推已核验 CA，或出现与已通知内容不同的关键变化；POLYROB 同一份「维持开放 / 官方已铸仍记 59、上限 504」不重推，除非售罄或改价/改入口，勿用 JS 占位覆盖官方 59，同窗再次出现的 06:31 CST 费用说明回复也不构成重推；Bitsigil 同一售罄不重推；Spoxy 同一份质押上线不重推；pillowbook 同一未开盘窗口不重推，除非真正开盘并公布 CA；jacketagent 已提醒付费阶段无新变化不重推；ozero 同一份 Base Sepolia 测试网宣传不重推，除非出现主网 mint 或与已通知内容不同的关键变化；wrapped-eth 已按真新提醒，本轮再次命中的 06:30 CST Explorer 上线帖且 /claim 仍 404、HTML 未见核验 CA，后续若只是同一份包装台观察、文档或浏览器功能说明、无 CA/入口/claim 入口实质变化，不重推；Hokori 同一份「Bramble 钱包已在 hokori.io 上线」产品更新不重推，除非出现 mint/登记窗口或与已通知内容不同的关键变化；TapeMine 同一份 Behemoth 二期进度（现 471/500 NAND）不重推，除非二期完成、新一期开启，或出现与已通知内容不同的关键变化；sunfall-world 已是 live 城市场，Payout #5 与 Season 1 于 08:00 CST 结束的预告（R1888 已记）不重推，除非出现新的 mint/登记窗口、改 CA，或与已通知内容不同的关键变化；Ringssol 同一份已在库实验发射台/终端的 hSOL 配对与基础设施/配置更新不重推，除非出现新的可操作 mint/登记窗口或与已通知内容不同的关键变化；raccoonslimestd 仍在选择发射台、未开盘，不重推，除非真正选定并开盘；Elysium Portals 同一份 announced / 免费登记且未见合约上线不重推，除非合约上线或开铸时钟明确；Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期、开窗，或出现与已通知内容不同的关键变化。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint。
