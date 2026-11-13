# RESULT R1749

- time: 2026-11-13 13:15 CST（Asia/Shanghai）
- mode: ample（R1739 已完成 08:00 CST 后首轮全量补扫，本轮为正常节流，不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true（1）真新收录 Riftera Rifters，即使免费档可能已满也按真新推送；（2）已在库 firsttake-xyz 监控漏挂刚补上，且确认首枚免费 LIVE；（3）the-syndicate-rh 仍 ≤2h 约至 14:37 CST）
- xReads: 26（main 24；silent 1；admitVerify 1）；remainingBefore 740 → remaining 714 / 1000；softCap 28，minSpend 20，silentCap 2；未超 softCap，高于 minSpend
- admitVerifyReads: 1（get_users_by_usernames 一次核验 RifteraPixel；未为再确认重读时间线。官网 / 链上 / HTTP / OpenSea / MCP 只读无 X 成本。MUST_TODAY 计入 main 24，已与本轮 used-handle 去重。firsttake-xyz 已在库，本轮不重读该官号时间线。agent402.surge.sh / SiBai / Robot Arm Prophets / Neon Vice / QUBITFOX 因无官推未建卡，未为补搜官号另耗 X 读）
- tenLanes: true（薄栏 6 条独立 KW + 核心 KW 打新/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom + 挖矿词 GPU PoW/NFT miner/mint miner 全跑；API 从 KW_GAPS 去掉了 `$` 字符，$PULSE 按 PULSE 跑，挖矿词实际已跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。部分 KW/mentions 回包被截断，已用清洗后的 raw 回收文本，未为修复解析另耗 X 读）
- userFollow: 刷完本片 100→150，kept 50，skip 0，下一轮从 150 续（UF 全表本轮末 1589，含新补 @RifteraPixel 与漏挂补挂 @FirstTake_xyz；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、GIWA、BTC、DogeEVM、Starknet、Tape；rest 实际查询官号为 @irys_xyz / @arcxtrade / @arcpump_ / @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @dotaipad / @flapdotsh / @fulldotfun。MN_BTC_DOGE 与 MN_STARK_TAPE 解析成功均为 0 帖；MN_LZ_GIWA 与 MN_REST 回包被截断，未另耗 X 重拉，不宣称精确帖数。mentionsThinDeferred=[]。均已跑，不翻页
- fat shards: agentPad 239→270 kept 28 skip 3（huntfieldrh / ciowworld / hahastage）；freeMint 361→389 kept 28 skip 0；bnAgent 277→16 wrapped=True kept 28 skip 1（HashOre_BNB；查询 22，elybirds / oryndotfamily / ZodiacFortune_N / arcticbear_nft / sharkverse_ / clause_protocol 已在本轮去重）；elysium 145→173 kept 28 skip 0
- thin official watches: 91 unique，与本轮已用 handle 去重 3 个（ZeroGuysNFT、Tapemonkeworld、PunkOnGiwa）、再跳过已知 NF 2 个（TapeFractal、FoundryTape）后 86，2 个 from: 批次（43+43）
- silentAccounts: ran=true，lane=打新，search_users unavailable，改跑 mentions（窗从 2026-11-12T05:04:45Z 起，softCap 外，query 含 fair mint / free mint / whitelist）；回包截断后清洗回收约 7 帖；Riftera 线索亦出现在该路径与 KW，官方 handle 来自官网而非 search_users；未做第二读
- discordPeekDeferred: true（DC 不登录）
- DS: deepseek-flash thinking-on，成功；新卡打分 + First Take 重评分 + alert 走 DS。alert 按真新 / 漏挂免费 LIVE / ≤2h 规则补上 handle、score 与面板链接。未走 dsFallback。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: from:TheSyndicateRH OR Elysium_Pepes OR AscendLaunch OR GateCerberus OR giraffies_nft（已与 used-handle 去重，本轮未再拉 droidzone_ / RuninAI_com）。@TheSyndicateRH 本窗仍有帖（Mint is Live / Freemint For GTD & OG）。其余本窗无新官帖。GateCerberus 发售仍为 20:00 CST，尚未进入 ≤2h。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Elysium Pepes 仍为 Announced，不把 11-13 预告写成已开盘。$DROID 窗已于 12:35 CST 结束。
- watch-bug: firsttake-xyz / @firsttake_xyz 自 R1340 已在库，但不在任何 Watch，本轮已补进 userFollowWatch + freeMintWatch，并把卡片从 watching 更新为 mint LIVE。不是新收录。

## 可操作 / 通知

1. **Riftera Rifters（@RifteraPixel）** — 本轮新收，score 58，BSC mint LIVE。官号已核验：显示名 Chibi Pixel，2026-07-19 注册，4 粉、1 帖、未认证；资料栏官网 https://riftera.net/ 与站点一致。官网 200，twitter:site/creator 与页内链接均为 @RifteraPixel，写明唯一官方合约 `0x36fE923C449F6163a601058626dEf6c83a8f23AE`。链上有代码，name=Riftera Rifters，symbol=RIFT，mintOpen=true，totalMinted=444，owner=`0x182f0bdbdc5afaa165ce5a58103fde6141b8b025`。官网：独特供应 1,111；免费档 444 枚 Common（编号 1–444），0 BNB，每钱包最多 3，需 Agent ID；付费档 0.001 BNB，每钱包最多 5，为 Rare/Legendary 与 Rift Shards 的唯一路径。链上已铸 444 与免费池 444 一致，免费额度可能已满；本轮未能用独立选择器拆出付费已铸数量，不要写成免费一定还能打。未独立审计。没有本轮独立开铸时钟，le2h=false。不要与已在库的 Rifera First Take（@firsttake_xyz / https://rifera.xyz/ / `0x0Cd348360109dd7f966B94a37Ff9BB0542b07Ec3`）混淆。本号不自动 mint。

2. **Rifera First Take（@firsttake_xyz）** — 不是新收录。R1340 已建卡，但此前不在任何 Watch（监控 bug），本轮已补进 userFollowWatch + freeMintWatch。官网 https://rifera.xyz/ 本轮 200，确认铸造已开：CA `0x0Cd348360109dd7f966B94a37Ff9BB0542b07Ec3`，固定供应 7,620，每钱包首枚免费（只付 gas），额外 0.002 BNB，升级到 5 级每级 0.002 BNB，需 Binance Agent ID。链上 name=Rifera First Take，symbol=RIFERA，mintOpen=true，totalMinted=194。本轮未再拉该官号时间线，没有独立开铸时钟，le2h=false。DeepSeek 重评分 overall 61（0–100）。未独立审计。

3. **The Syndicate（@TheSyndicateRH）** — 仍免费 LIVE，且仍在 ≤2h 窗（约至 14:37 CST）。MUST_TODAY 本窗仍见官帖 Mint is Live / Freemint For GTD & OG。OpenSea thesyndicate- total_supply 619→762、owners 306→339、sales 约 695–697→762、floor 仍约 0.31 USDG。官网仍 200。公开 Robinhood RPC 仍不可用，未独立上链复核。规则与风险同 R1748（GTD/OG 上限官帖与官网不一致；官号新、粉少；accio.ai 子域）。

## 仍在跟（非 ≤2h）

- $DROID：窗约 12:35 CST 已过，le2h=false。本轮未再拉 @droidzone_ 时间线。官网仍 200。公开 RPC 仍失败，CA 仍未独立复核。不是免费铸造。
- Momo Mochi：仍免费 LIVE。链上约 13:06 CST mintOpen=true，totalMinted 287→289，totalSupply=289。maxSupply 选择器本轮 revert，仍按此前记录 2222。官网 https://puzzlehave.fun/ 仍 200。本轮未再拉该官号时间线。≤2h 窗约 11:51 CST 已过。
- Cento：官网仍 200。不是免费铸造。本轮未再拉该官号时间线。≤2h 窗约 11:58 CST 已过。
- Clause Protocol：仍视为免费 LIVE。链上约 13:06 CST Clause Genesis totalMinted 1→2/7777；ClauseMint paused=false。isMintLive 与 mintEnd 选择器本轮 revert，不新报为 true。官网仍 200。本轮未再拉该官号时间线。窗约 11:19 CST 已过。
- Elysium Portals：仍为免费登记，官网仍 200，页面仍有 waitlist，并写合约尚未上线。无开铸时钟，le2h=false。本轮未再拉该官号时间线。
- Zodiac Fortune：免费额度已尽。链上约 13:06 CST mintOpen=true，remainingFree 仍为 0，totalMinted 仍为 334/3333，现为 0.0005 BNB 付费。窗约 10:04 CST 已过，铸造仍 LIVE。本轮未再拉该官号时间线。
- SharkVerse：仍免费 LIVE，链上已铸仍为 21/4444。paused_shark 选择器本轮读到 false（常规 paused 仍 revert）。官网仍 200。窗约 10:36 CST 已过。同模板风险仍在。本轮未再拉该官号时间线。
- Arctic Bear：仍免费 LIVE，已铸 69→70/5555，totalSupply=70，freeMinted=70，forgeLive=true。窗约 10:02 CST 已过。同模板风险仍在。本轮未再拉该官号时间线。
- JPEG Monkes：免费窗约 10:30 CST 已过，集合仍 LIVE。本轮未再拉该官号时间线。OpenSea supply 1293→1356、owners 910→907、sales 1470→1549、floor 约 0.00147799 ETH。
- CashMe：发射台官网仍 200。本轮未再拉该官号时间线。按首条官宣至约 10:30 CST 的 ≤2h 已过。不是免费铸造。
- Zero Guys：仍为免费 WL 登记。本轮未再单独拉 from:ZeroGuysNFT 时间线（与本轮已用 handle 去重）。11-30 开铸、价 TBD、供 3444。官网仍 200。
- hood-terminals：付费公售仍 LIVE。OS 仍 527/777，owners 352，sales 644，floor 约 0.000999 ETH。不是免费窗。本轮未再拉官号（只刷新 OpenSea）。
- clover-rh：OS 仍 888 供、owners 504、sales 1679、floor 约 0.0024048 ETH。官网 clover.family 本轮 HTTP 失败，未据此改写铸造状态。本轮未再拉官号时间线。
- Dividends / Law of the Abyss：官网均仍 200，申请/白名单仍开，无新开铸时钟，不重复收录。本轮未再拉这两家官号时间线。le2h=false。
- Shift Forever：官网仍 200。不以主网开铸处理。本轮未再拉该官号时间线。不进入 ≤2h，不新开卡。
- lil-giraffies：本窗 MUST_TODAY 无新官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。
- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），≤2h 自 18:00 CST 起，尚未进入。本窗无新官帖。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把 11-13 预告写成已开盘。
- osk-agent：本轮 fat bnAgent 扫到 @AIAgent_OSK 仍有帖。免费席此前已尽，付费 0.008 BNB，deadline 仍为 11-15 18:00 CST。保持 failed，不重新收录为免费 mint。
- QUBITFOX：链上 mintOpen=true，totalSupply=150；仍无官推，未建卡。
- agent402 / SiBai / Robot Arm Prophets / Neon Vice：站点仍在，均无官推，未建卡。

## 跳过 / 不建卡

- Hoodicorns：公售仍 LIVE，但是付费，且已在库，不按新免费 mint 处理。
- UBIdotFUN / slymzcrew / HOKORI_QUANTUM / Ammora / BEM-TapeOut 等：已在库或非新的可打免费窗。
- HoodJesters + RASyndicate：即将白名单赠送，尚未 LIVE，本轮不建卡。
- furbi59360「DEADPOOL NINJA TURTLE」Ordinals 免费 mint：无已核验官号，跳过。
- bitcoinfoxclub / unvault 路人免费 mint 线索：跳过。
