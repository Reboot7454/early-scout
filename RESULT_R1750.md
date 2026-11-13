# RESULT R1750

- time: 2026-11-13 13:44 CST（Asia/Shanghai）
- mode: ample（R1739 已完成 08:00 CST 后首轮全量补扫，本轮为正常节流，不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true（the-syndicate-rh 仍 ≤2h 约至 14:37 CST，且官宣供应从 1,888 砍到 1,000、官帖称已铸约 798 / OpenSea 已铸 799。本轮无新收录，无新的免费 LIVE/登记卡）
- xReads: 25（main 24；silent 1；admitVerify 0）；remainingBefore 714 → remaining 689 / 1000；softCap 28，minSpend 20，silentCap 2；未超 softCap，高于 minSpend
- admitVerifyReads: 0（无新收录，未另做 get_users 核验。Hardline 官号对象来自本轮 search_posts_all includes，DeepSeek admit=false，未为再确认重读。官网 / 链上 / HTTP / OpenSea / MCP 只读无 X 成本。MUST_TODAY 计入 main 24，已与本轮 used-handle 去重。部分 KW/mentions 回包被截断，已用清洗后的 raw 回收文本，未为修复解析另耗 X 读）
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet + 核心 KW 打新/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom + 挖矿词全跑；API 从词面去掉 `$` 字符，$PULSE 按 PULSE 跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。KW_LayerZero、KW_BTC、MN_BTC_DOGE、SILENT_MINE 回包为空；部分其它 KW/mentions 回包被截断，已 salvage，未重拉）
- userFollow: 刷完本片 150→202，kept 50，skip 2（HashOre_BNB / usejackbay，已知 NF），下一轮从 202 续（UF 全表 1589；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、GIWA、BTC、DogeEVM、Starknet、Tape；rest 实际查询官号为 @irys_xyz / @arcxtrade / @arcpump_ / @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @dotaipad / @flapdotsh / @fulldotfun。MN_BTC_DOGE 解析成功为 0 帖；部分 mentions 回包被截断，未另耗 X 重拉，不宣称精确帖数。mentionsThinDeferred=[]。均已跑，不翻页
- fat shards: agentPad 270→298 kept 28 skip 0；freeMint 389→22 wrapped=True kept 28 skip 1（WhackyRH；查询 23，TheSyndicateRH / BNBanksAgentic / CataONsahara_RH / aliienid / flaggies_world 已在本轮去重）；bnAgent 16→54 kept 28 skip 10 NF（bsc_bito / tikitotemsbnb / Nonce_CTO / claudesprotocol / wedowtf / TurboKartBNB / SwarmHiveBNB / WuseAgent / Fairagent_bnb / ChyAI_Official；查询 26，AgentWorldBNB / HIRELINGSAI 已在本轮去重）；elysium 173→201 kept 28 skip 0
- thin official watches: 94 unique，与本轮已用 handle 去重 3 个（tapekeyofficial、Giwatron、mimdotcash）后 91，2 个 from: 批次（46+45）。已知 NF TapeFractal / FoundryTape 留在同一批 OR，未另耗读、也未单独跳过
- silentAccounts: ran=true，lane=挖矿，search_users unavailable，改跑 mentions（窗从 2026-11-12T05:36:01Z 起，softCap 外，query: has:mentions ("GPU mine" OR "NFT miner" OR "PoW mine") -is:retweet）；回包 0 帖；未做第二读
- discordPeekDeferred: true（DC 不登录）
- DS: deepseek-flash thinking-on，成功；Hardline 打分（overall 43，admit=false）+ alert 走 DS。alert 按仍有效 ≤2h 与供应砍仓写短中文，并含面板链接。未走 dsFallback。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: from:TheSyndicateRH OR Elysium_Pepes OR AscendLaunch OR GateCerberus OR giraffies_nft（已与 used-handle 去重）。@TheSyndicateRH 本窗有多条官帖（Mint is Live / Freemint For GTD & OG；以及 13:23 CST EXCLUSIVE 供应 1,888→1,000、官帖称 798 minted already）。其余本窗无新官帖。GateCerberus 发售仍为 20:00 CST，尚未进入 ≤2h。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Elysium Pepes 仍为 Announced，不把 11-13 预告写成已开盘。$DROID 窗已于 12:35 CST 结束。
- watch-bug: 本轮扫描 round≥1740 卡片，无新的在库却不在任何 Watch 的漏挂。firsttake-xyz 已在 R1749 补进 UF+freeMint。

## 可操作 / 通知

1. **The Syndicate（@TheSyndicateRH）** — 仍免费 GTD/OG + Public LIVE，且仍在 ≤2h 窗（约至 14:37 CST）。MUST_TODAY 见多条官帖：仍在写 Mint is Live / Freemint For GTD & OG；13:23 CST 另发 EXCLUSIVE，称供应 1,888→1,000（Limited, final, no reprints），Public 0.00005 ETH、每钱包最多 44，并写 798 minted already。稍早 13:08 CST 官帖仍写 1,888 entities minting now。OpenSea thesyndicate- total_supply 762→799、owners 339→356、sales 762→765、floor 仍约 0.31 USDG。官网仍 200。公开 Robinhood RPC 仍失败，未独立上链复核。GTD/OG 上限官帖与官网此前不一致的风险仍在；官号新、粉少；站点为 accio.ai 子域。本号不自动 mint。

## 仍在跟（非 ≤2h）

- Riftera Rifters（@RifteraPixel）：不是新收录。本轮 freeMint 分片覆盖该官号，官帖确认 FREE MINT SOLD OUT：444 枚免费 Rifters 在 18 分钟内领完。付费档仍开：0.001 BNB，667 paid spots，Rare 167 / Legendary 33，Rift Shards 仅能经付费档获得。BSC 链上约 13:36 CST mintOpen=true，totalMinted 444→446（免费池已满，多出的 2 枚更像付费开始铸造，仍无法用独立选择器拆出付费已铸数）。官网 https://riftera.net/ 仍 200。le2h=false。不要与 Rifera First Take 混淆。本号不自动 mint。
- Rifera First Take（@firsttake_xyz）：仍为首枚免费 LIVE。官网 https://rifera.xyz/ 仍 200。链上约 13:36 CST mintOpen=true，totalMinted 仍为 194/7620。本轮 freeMint 分片覆盖了该官号，未见新的铸造规则变化。不是新收录，le2h=false。
- $DROID：窗约 12:35 CST 已过，le2h=false。本轮未把 @droidzone_ 列入 MUST。官网仍 200。公开 Elysium RPC 仍失败，CA 仍未独立复核。不是免费铸造。
- Momo Mochi：仍免费 LIVE。链上约 13:36 CST mintOpen=true，totalMinted 289→291，totalSupply=291。maxSupply 选择器本轮仍 revert，仍按此前记录 2222。官网 https://puzzlehave.fun/ 仍 200。本轮未再拉该官号时间线。≤2h 窗约 11:51 CST 已过。
- Cento：官网仍 200。不是免费铸造。本轮未再拉该官号时间线。≤2h 窗约 11:58 CST 已过。
- Clause Protocol：仍视为免费 LIVE。链上约 13:36 CST Clause Genesis totalMinted 2→5/7777（本轮 maxSupply 选择器 revert，供应上限仍按此前记录 7777）；ClauseMint paused=false。isMintLive 与 mintEnd 选择器本轮仍 revert，不新报为 true。官网仍 200。本轮未再拉该官号时间线。窗约 11:19 CST 已过。
- Elysium Portals：仍为免费登记。官网仍 200。本轮 freeMint 分片见到官帖仍在宣传 waitlist is open。未见合约已上线证据。无开铸时钟，le2h=false。
- MemeFunds（@MemeFunds_）：官帖 13:32 CST 宣布延迟上线，称市场波动大，尤其认为现在不适合在 Elysium 上线，稍后另发新公告。不是免费 mint 窗口，不进入 ≤2h，保持 announced，不改写成已开盘。
- Zodiac Fortune：免费额度已尽。链上约 13:36 CST mintOpen=true，remainingFree 仍为 0，totalMinted 334→335/3333，paidPrice 仍为 0.0005 BNB。窗约 10:04 CST 已过，铸造仍 LIVE。官网仍 200。本轮未再拉该官号时间线。
- SharkVerse：仍免费 LIVE，链上已铸仍为 21/4444。paused_shark 选择器本轮读到 false（常规 paused 仍 revert）。官网仍 200。窗约 10:36 CST 已过。同模板风险仍在。本轮未再拉该官号时间线。
- Arctic Bear：仍免费 LIVE，已铸 70→73/5555，totalSupply=73，freeMinted=73，forgeLive=true。窗约 10:02 CST 已过。同模板风险仍在。本轮未再拉该官号时间线。
- JPEG Monkes：免费窗约 10:30 CST 已过，集合仍 LIVE。本轮未再拉该官号时间线。OpenSea supply 1356→1396、owners 907→905、sales 1549→1614、floor 约 0.00132 ETH。
- CashMe：发射台官网 usecashme.fun 本轮仍 200。不是免费铸造。本轮未改卡内进度。
- Zero Guys：仍为免费 WL 登记。官网仍 200。11-30 开铸、价 TBD、供 3444。本轮未再单独拉该官号时间线。
- hood-terminals：付费公售仍 LIVE。官网仍 200。OpenSea hoodterminals 集合详情本轮 401，仅 stats 成功：owners 仍 352，sales 仍 644，floor 约 0.000996 ETH。本轮未能独立刷新 total_supply，不把此前 527 当作本轮核实值。不是免费窗。本轮未再拉官号时间线。
- clover-rh：OS 仍 888 供、owners 504→503、sales 仍 1679、floor 约 0.0023961 ETH。官网 clover.family 本轮 HTTP 403，未据此改写铸造状态。本轮未再拉官号时间线。
- Boatn Fish：付费 Genesis 仍 LIVE。https://boatnfish.fun/api/stats 本轮 minted 609→1028/2222，wallets 56→79，现价约 0.02372 SOL。不是免费铸造，也不是新收录。本轮未再拉该官号时间线。
- Dividends / Law of the Abyss：官网均仍 200，申请/白名单仍开，无新开铸时钟，不重复收录。本轮 freeMint 分片覆盖了这两家官号。le2h=false。
- Shift Forever：官网仍 200。不以主网开铸处理。本轮未再拉该官号时间线。不进入 ≤2h，不新开卡。
- lil-giraffies：本窗 MUST_TODAY 无新官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。
- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），≤2h 自 18:00 CST 起，尚未进入。本窗无新官帖。公开 Elysium RPC 仍未能复核卡内 CA。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把 11-13 预告写成已开盘。
- AscendLaunch：MUST_TODAY 本窗无新官帖。发射台官网仍 200。不是免费铸造。
- QUBITFOX：链上 mintOpen=true，totalSupply 仍为 150；仍无官推，未建卡。
- agent402 / SiBai / Robot Arm Prophets / Neon Vice：站点仍在，均无官推，未建卡。

## 跳过 / 不建卡

- Hardline（@hardline_01 / hardline-xlayer）：本轮从 Tape/X Layer mentions 盲捞到新号（2026-11-12 注册，1 粉、1 帖）。站点 https://k58v2hbzkk-del.github.io/hardline/ 200，是把规则编译成逻辑芯片、经 TapeOut 铸到 X Layer 的工具页，不是传统免费 NFT mint。页内写自有 processor `0x1f09daefa827f02cbb40967cc91b259763760761`。DeepSeek overall 43，admit=false（窗口不明、github.io 个人页过薄）。未建卡，未为再确认另耗 X 读。
- 其它新作者噪音（@grok / @Spindrift76 / @GiftofMan 等）：Starknet/Bramble 等关键词误伤或无关，跳过。
- 截断 KW 中未完整解析作者的 WFit/Companions（称 11-17 免费 mint）与 PlayPixelora land raffle：不是今日 LIVE，未为补全作者另耗 X 读，本轮跳过。
