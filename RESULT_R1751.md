# RESULT R1751

- time: 2026-11-13 14:04 CST（Asia/Shanghai）
- mode: ample（R1739 已完成 08:00 CST 后首轮全量补扫，本轮为正常节流，不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true（the-syndicate-rh 仍 ≤2h 约至 14:37 CST。本轮无新收录，无新的免费 LIVE/登记卡）
- xReads: 25（main 24；silent 1；admitVerify 0）；remainingBefore 689 → remaining 664 / 1000；softCap 28，minSpend 20，silentCap 2；未超 softCap，高于 minSpend
- admitVerifyReads: 0（无新收录，未另做 get_users 核验。Hardline（@hardline_01）再次出现在本轮 MN_STARK_TAPE / KW_Tape 中，R1750 已 DeepSeek admit=false，本轮未为再确认重读，也未重打分。Unvault Genesis Bugz 来自第三方帖 @0xStephen_，官网 unvault.com/bugz 可见 checker/免费 7500 但未找到官推，未为补全作者另耗 X 读。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 计入 main 24，已与本轮 used-handle 去重。部分 KW/mentions 回包被截断，已用清洗后的 raw 回收文本，未为修复解析另耗 X 读）
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet + 核心 KW 打新/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom + 挖矿词全跑；API 从词面去掉 `$` 字符，$PULSE 按 PULSE 跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。KW_LayerZero、MN_BTC_DOGE 回包为空；部分其它 KW/mentions 回包被截断，已 salvage，未重拉）
- userFollow: 刷完本片 202→262，kept 50，skip 10（DubbllePadX / SealzHood / BNBS_ai / keccaklings / ponzihooks / swiprdotxyz / GlitchOnHood / rh_ofsherwood / wildlife_uni / layertrade，已知 NF），下一轮从 262 续（UF 全表 1589；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、GIWA、BTC、DogeEVM、Starknet、Tape；rest 实际查询官号为 @irys_xyz / @arcxtrade / @arcpump_ / @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @dotaipad / @flapdotsh / @fulldotfun。MN_BTC_DOGE 解析成功为 0 帖；部分 mentions 回包被截断，未另耗 X 重拉，不宣称精确帖数。mentionsThinDeferred=[]。均已跑，不翻页
- fat shards: agentPad 298→341 kept 28 skip 15 NF；freeMint 22→65 kept 28 skip 15 NF（查询 11，17 个已用 handle 去重，未绕回）；bnAgent 54→92 kept 28 skip 10 NF；elysium 201→229 kept 28 skip 0
- thin official watches: 94 unique，与本轮已用 handle 去重 7 个（acmeonbtc / TapeId_AI / owlgatecli / GiwaPumpPad / GiwaGasok / GIWAForge / GenPad_Ai）并跳过已知 NF TapeFractal 后查询 86，2 个 from: 批次（43+43）。已知 NF FoundryTape 留在同一批 OR，未另耗读。两批本窗 result_count 均为 0
- silentAccounts: ran=true，lane=台子/Meme，search_users unavailable，改跑 mentions（窗从 2026-11-12T05:58:28Z 起，softCap 外，query: has:mentions (launchpad OR "bonding curve") -is:retweet）；回包 result_count=20，正文截断后清洗回收；未见可建卡的新官号。未做第二读
- discordPeekDeferred: true（DC 不登录）
- DS: deepseek-flash thinking-on，成功；本轮无新收录，未再跑 Hardline 打分。alert 按仍有效 ≤2h 与 OpenSea 已铸 799→802 写短中文，并含面板链接。未走 dsFallback。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: from:TheSyndicateRH OR Elysium_Pepes OR AscendLaunch OR GateCerberus OR giraffies_nft（已与 used-handle 去重）。@TheSyndicateRH 本窗仍见多条官帖（Mint is Live / Freemint For GTD & OG；以及 13:23 CST EXCLUSIVE 供应 1,888→1,000、官帖称 798 minted already）。其余本窗无新官帖。GateCerberus 发售仍为 20:00 CST，尚未进入 ≤2h。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Elysium Pepes 仍为 Announced，不把 11-13 预告写成已开盘。$DROID 窗已于 12:35 CST 结束。
- watch-bug: 本轮扫描 round≥1740 卡片，无新的在库却不在任何 Watch 的漏挂。firsttake-xyz 已在 R1749 补进 UF+freeMint。

## 可操作 / 通知

1. **The Syndicate（@TheSyndicateRH）** — 仍免费 GTD/OG + Public LIVE，且仍在 ≤2h 窗（约至 14:37 CST）。MUST_TODAY 本窗仍见多条官帖写 Mint is Live / Freemint For GTD & OG；13:23 CST 的 EXCLUSIVE 帖仍在（供应 1,888→1,000 final，Public 0.00005 ETH、每钱包最多 44，官帖写 798 minted already）。OpenSea thesyndicate- total_supply 799→802、owners 356→358、sales 765→767、floor 仍约 0.31 USDG。官网仍 200。公开 Robinhood RPC 仍失败，未独立上链复核。GTD/OG 上限官帖与官网此前不一致的风险仍在；官号新（约 10 粉）；站点为 accio.ai 子域。本号不自动 mint。

## 仍在跟（非 ≤2h）

- Riftera Rifters（@RifteraPixel）：不是新收录。本轮 freeMint 分片未覆盖该官号，未再拉时间线。官网 https://riftera.net/ 仍 200。BSC 链上约 14:02 CST mintOpen=true，totalMinted 仍为 446（与 R1750 相同，本轮未见新增）。免费已售罄，付费 0.001 BNB 仍开。le2h=false。不要与 Rifera First Take 混淆。本号不自动 mint。
- Rifera First Take（@firsttake_xyz）：仍为首枚免费 LIVE。官网 https://rifera.xyz/ 仍 200。链上约 14:02 CST mintOpen=true，totalMinted 仍为 194/7620。本轮 freeMint 分片未覆盖该官号，未再拉时间线。不是新收录，le2h=false。
- $DROID：窗约 12:35 CST 已过，le2h=false。本轮未把 @droidzone_ 列入 MUST。官网仍 200。公开 Elysium RPC 仍失败，CA 仍未独立复核。不是免费铸造。
- Momo Mochi：仍免费 LIVE。链上约 14:02 CST mintOpen=true，totalMinted 仍为 291，totalSupply=291。maxSupply 选择器本轮仍 revert，仍按此前记录 2222。官网 https://puzzlehave.fun/ 仍 200。本轮未再拉该官号时间线。≤2h 窗约 11:51 CST 已过。
- Cento：官网仍 200。不是免费铸造。本轮未再拉该官号时间线。≤2h 窗约 11:58 CST 已过。
- Clause Protocol：仍视为免费 LIVE。链上约 14:02 CST Clause Genesis totalMinted 仍为 5/7777（totalSupply=5）；本轮 MAX_SUPPLY 选择器读到 7777（R1750 该选择器曾 revert，当时按此前记录沿用 7777，现已独立复核）。ClauseMint paused=false。isMintLive 与 mintEnd 选择器本轮仍 revert，不新报为 true。官网仍 200。本轮未再拉该官号时间线。窗约 11:19 CST 已过。
- Elysium Portals：仍为免费登记。官网仍 200。本轮未再拉该官号时间线，未见合约已上线证据。无新开铸时钟，le2h=false。
- MemeFunds（@MemeFunds_）：延迟上线公告仍按 R1750 官帖（认为当下不适合在 Elysium 上线）。本轮未再拉该官号时间线。不是免费 mint 窗口，不进入 ≤2h，保持 announced，不改写成已开盘。
- Zodiac Fortune：免费额度已尽。链上约 14:02 CST mintOpen=true，remainingFree 仍为 0，totalMinted 仍为 335/3333，paidPrice 仍为 0.0005 BNB。窗约 10:04 CST 已过，铸造仍 LIVE。官网仍 200。本轮未再拉该官号时间线。
- SharkVerse：仍免费 LIVE，链上已铸仍为 21/4444。paused_shark 选择器本轮读到 false（常规 paused 仍 revert）。官网仍 200。窗约 10:36 CST 已过。同模板风险仍在。本轮未再拉该官号时间线。
- Arctic Bear：仍免费 LIVE，已铸仍为 73/5555，totalSupply=73，freeMinted=73，forgeLive=true。窗约 10:02 CST 已过。同模板风险仍在。本轮未再拉该官号时间线。
- JPEG Monkes：免费窗约 10:30 CST 已过，集合仍 LIVE。本轮未再拉该官号时间线。OpenSea jpegmonkes total_supply 1396→1405、owners 905→887、sales 1614→1655、floor 约 0.00119 ETH。
- CashMe：发射台官网 usecashme.fun 本轮仍 200。不是免费铸造。本轮未改卡内进度。
- Zero Guys：仍为免费 WL 登记。官网仍 200。11-30 开铸、价 TBD、供 3444。本轮 mentions 见第三方仍在讨论申请/白名单，无新开铸时钟。本轮未再单独拉该官号时间线。le2h=false。
- hood-terminals：付费公售仍 LIVE。官网仍 200。本轮 OpenSea hoodterminals 集合详情 200（R1750 曾 401）：total_supply=527，owners 仍 352，sales 仍 644，floor 约 0.000996 ETH。不是免费窗。本轮未再拉官号时间线。
- clover-rh：OS 仍 888 供、owners 503→502、sales 1679→1680、floor 约 0.002378 ETH。官网 clover.family 本轮 HTTP 403，未据此改写铸造状态。本轮未再拉官号时间线。
- Boatn Fish：付费 Genesis 仍 LIVE。https://boatnfish.fun/api/stats 本轮 minted 1028→1037/2222，wallets 79→80，现价约 0.02472 SOL。不是免费铸造，也不是新收录。本轮未再拉该官号时间线。
- Dividends / Law of the Abyss：官网均仍 200，申请/白名单仍开，无新开铸时钟，不重复收录。本轮 freeMint 分片未覆盖这两家官号。le2h=false。
- Shift Forever：官网仍 200。不以主网开铸处理。本轮未再拉该官号时间线。不进入 ≤2h，不新开卡。
- lil-giraffies：本窗 MUST_TODAY 无新官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。
- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），≤2h 自 18:00 CST 起，尚未进入。本窗无新官帖。公开 Elysium RPC 仍未能复核卡内 CA。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把 11-13 预告写成已开盘。
- AscendLaunch：MUST_TODAY 本窗无新官帖。不是免费铸造。按首条官宣计算的 ≤2h 此前已过。本轮未把未经卡内确认的域名写成官网 200。
- QUBITFOX：链上 mintOpen=true，totalSupply 150→151；仍无官推，未建卡。qubitfox.pages.dev 仍 200。
- agent402 / SiBai / Robot Arm Prophets / Neon Vice：站点仍在，均无官推，未建卡。

## 跳过 / 不建卡

- Unvault Genesis Bugz：本轮 KW_台子 见到第三方帖（@0xStephen_）称 unvault genesis bugz checker is live，供应 7500、免费、每钱包 1，并写 mint time: no official date yet。t.co 指向 https://www.unvault.com/bugz（200）与一张图。站点确认 FREE / 1 per wallet / 7500 / 多链 wallet checker；bugz 页与首页均未找到官推。库内无 Unvault 卡。硬规则新收录必须有推特，本轮不建卡，也未为猎号另耗 X 读。
- Hardline（@hardline_01）：再现于本轮 MN_STARK_TAPE / KW_Tape。R1750 已 DeepSeek admit=false（github.io 过薄），本轮未当新机会、未重审、未另耗 X。粉数可见从 1→2、帖数 1→6，仍过薄。
- 其它新作者噪音（@ARCYResearch / @Tollxyz_ / @lumora_agent / @bankrbot / @Spindrift76 / @grok / @_Mr_Water_01 等）：UF/fat/Starknet 关键词误伤、随机部署或无关回复，跳过。
- 截断 KW 中未完整解析作者的 WFit/Companions、Rebel kin WL、onlystreetsfun 等：已在库或不是今日新 LIVE，未为补全作者另耗 X 读，本轮跳过。
