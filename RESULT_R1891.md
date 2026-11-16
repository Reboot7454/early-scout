# RESULT R1891

- time: 2026-11-16 08:03 CST (Asia/Shanghai)
- mode: near-exhausted（remainingBefore 19<50）
- lastFullAfterReset: R1843（08:09 CST 的 08:00 后首轮全量补扫；本轮非补扫轮，开跑时仍在 08:00 重置前）
- xReads: 6（main 6 + silent 0）
- remaining: 19 → 13 / 1000
- softCap: 8，minSpend: 6，silentCap: 0
- notify: false
- newIds: 无
- dsFallback: false（无合格新卡，跳过录取/打分 DS；文案一次 DeepSeek 回合法 JSON）

## 本轮做什么

独立例行 near-exhausted 扫。开跑 `git pull` 已与 origin/main 同步（起点 commit b5224c1 R1890）。按硬顺序：UF 分片软刷 → MUST 合并 live/优先号。因 remaining 19<50，薄栏/核心栏 KW、mentions、THIN official、silent 全部延后。DC 不登录，discordPeekDeferred=true。本号不自动 mint。

本轮开跑约 07:57–07:59 CST，仍在日额重置（08:00 CST）之前；读取过程页脚 remaining 19→13，重置未在本轮读数中发生。08:00 CST 后下一轮应做首轮全量补扫。

## X 额度与查询

remainingBefore=19。6 次读取后 remaining=13。页脚依次 18/17/16/15/14/13。

- UF1–UF5：0-based 1751 nihilo_fun 起 packed 5 片 kept 125（25+26+25+25+24），walk 中回绕到表头，NF_skip 7（safureload / Seethebsc / Charzardxpox / LuckyAgent_bsc / Agentrocksclub / sunrigfun / kaAgents）。walkScanned 132。lastKept Naru_giwa。next 28 elysianfieldnft。wrap=true。
- MUST1：19 handles（live 窗口剩余号 + 6 个未落入本轮 UF 分片的优先号：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[qtronlaptops, HoodTurtleRH, DeadHood_nft, Gloopix_, infamousScratch, ozero_fun, PlayBitsigil, SpoxyGang, wrapped__eth]（回绕后已落入本轮 UF 分片，未在 MUST 重读）。prioInShard=[mobster_meme]。
- 薄栏六条 KW、核心栏 KW、THIN official、mentions 均因 near-exhausted 未跑。
- silentCap=0，未跑（本应 1891%11=10 Starknet）；下一轮 lane=打新。
- 同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=6，打满 minSpend 6，未超 softCap 8。

## 信号与结论

本窗命中 11 帖，涉及已在库 7 个号，无新 handle、无新录取。

- hokori-quantum：07:47 CST 官帖宣布 Dev $HKR tokens burned，挂 Solana 交易 4QLLZqWtw7aWiURyxhh5QyRhcCyGWBaJynru7izKyxfwmD8wgH2QZyaJ8QQQotRAJtkqBqZz2ZESrtTttCMsSELP。链上日志 Convert+Burn 成功，mint 5DLMQuAJdQp4sWvPoNqNqLx8uEjWcFBaTLxLDRCBpump 余额 20,681,098.08675→0。官网 hokori.io HTTP 200，仍无用户可操作 mint/登记/兑换入口。R1890 已记「即将燃烧转换」预告；本次是预告落地，但不带来新的可操作入口，不重推。
- sapling：07:06 CST 官帖宣布官方 $SAPLING（CA BZFYNPeQAEW3HWQ4DNsTVahC1n4ZjTgn6jB2nnBbB96W）已在 Jupiter 核验。站点 sapling.cash 200，该 CA 即页面展示的官方代币（2026-09-25 已发射），非新打新窗口，不重推。已把官方 CA 写入卡片。
- dataloomsol：07:20 CST 官帖称 $DATALOOM 将进入 confidential AI checkout，结账费率已部署到生产；付费查询尚未开放。站点 200。非 mint/开盘窗口，不重推。
- wrapped-eth：07:44 CST 官帖为包装费会计示例。官网 200，/explore 200，/claim 仍 404，HTML 未见核验 CA，无入口实质变化，不重推。粉 41→42。
- elysiasealed：本窗 RAS（896 笔/24h）与 FRODO（356 笔/24h）Pons 成交播报。R1834 已收录该 live 窗口，不重推。
- animal-pharm：本窗三条社交回复，已售罄，无新打新窗口，不重推。
- pynki：本窗仅为 Elysium 讨论回复，非新开窗，不重推。
- sunfall-world：本 1h 官窗无新帖；站点 200，CA 未变。Season 1 原定 08:00 CST 结束为 R1888 已记，未见新 mint/登记窗口，不重推。

无 ≤2h 新窗口。Ink Legions 开铸仍为 2026-11-17 03:00 CST，非本轮 ≤2h。watchLeaks=0。

## 覆盖与延后

- 十栏关键词：未跑全（near-exhausted 延后）。
- userFollowWatch：本轮分片刷完（含回绕），complete=true，next 28 elysianfieldnft。
- mentions：未跑；下一轮仍 LayerZero / Elysium+kinetiq。08:00 CST 后首轮应全量补扫（UF 继续分片 + 十栏关键词 + 全链 mentions）。
- silent：未跑；deferredHandles 结转 hyperhaul / p2eabs / ZeroHoppersNFT。不要把下一轮 silentCap 花在 bitcoincoreorg 或 StreetHoodMedia。
- Discord Peek：deferred。

## 不重推（沿用并补充）

- Hokori 本次 Dev $HKR 链上燃烧/转换已发生，但官网仍无新的用户可操作入口，不重推；后续若出现 mint/登记窗口或用户可操作兑换入口，再提醒。
- sapling 同一份官方 $SAPLING 的 Jupiter 核验不重推，除非出现新的可操作发射/mint 窗口或改 CA。
- dataloomsol 同一份「付费查询开放后可用 $DATALOOM 结账」预告不重推，除非付费查询真正开放或出现 mint/开盘窗口。
- wrapped-eth 已按真新提醒；本轮会计示例且 /claim 仍 404、未见核验 CA，后续若只是同一份包装台说明、无 CA/入口/claim 实质变化，不重推。
- elysiasealed 同一份 Pons 成交播报不重推。
- animal-pharm 已售罄社交回复不重推。
- pynki 讨论回复不重推。
- sunfall-world 已是 live 城市场，Season 1 于 08:00 CST 结束的预告（R1888 已记）不重推，除非出现新的 mint/登记窗口、改 CA，或与已通知内容不同的关键变化。
- 其余已提醒窗口沿用 R1890：pillowbook 同一未开盘窗口不重推，除非真正开盘并公布 CA；jacketagent 已提醒付费阶段无新变化不重推；ozero 同一份 Base Sepolia 测试网宣传不重推，除非出现主网 mint；TapeMine 同一份 Behemoth 二期进度不重推，除非二期完成或新一期开启；raccoonslimestd 仍在选择发射台不重推；Elysium Portals 同一份 announced / 免费登记未见合约上线不重推；Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗；boxcars 已按免费驾照通知，进度/箱子奖励刷新不重推，除非预售开盘/改期、驾照售罄、改入口/改 CA。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint。
