# RESULT R1961

- time: 2026-11-19 10:49:38 CST
- mode: ample（R1956 为 08:00 CST 后首轮全量补扫；本轮为其后第五轮正常节流，lastFullAfterReset 仍为 R1956）
- xReads: 21（main 19 + silent 1 + EXTRA 1）
- remainingBefore: 886 → remaining: 865
- softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50
- tenLanes: yes（11 条关键词全跑：LZ 1 / TAPE 20 / GIWA 8 / DOGE 14 / BTC 3 / SN 1 / MINT 25 / MINE 0 / PAD 16 / GO 25 / ELY 17。MINT/GO 触顶，未翻页。部分 write_to_file 预览中段省略，已从完整 companion 文件回收全部帖，未重查）
- userFollow: 刷完本分片，wrap=false。start 426 agentrybaw，kept 50（agentrybaw→Ptahtrade），walkScanned 67，NF_skip 17（grepfi / torpor_si / SwarmHiveBNB / twinmetahq / astrispace / Fairagent_bnb / ChyAI_Official / AIDOGagentai / snakeidbnb / halfhook / Fruits_by_Amy / cardstockfun / potionrh / beatmissapp / sharpsheet_rh / safufundbnb / Asciidogs），skip_already 0。next 493 OmbrelloNFT。prio_folded：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。prio_skipped：mobster_meme。MUST 把 @INMATES_RH 并进 UF1；窗口号 yuange99988852 / Oathbots / spiritsHOOD / Vice6fun 另 1 次 from:。本分片 UF 帖 UF1=0 / UF2=0，MUST=0。
- mentions: 本轮轮换子集 4 组 Tape 5 / GIWA 5 / BTC 5 / Starknet+DogeEVM 5。下一轮子集 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent: GO盘（1961%11=3；SILENT_MEN result_count=11，约 24h 窗；search_users 仍不可用）。11 条未见需新收录的官方项目送审（@useFeely 已在库同窗口不重推）。下一轮 silent=LayerZero。
- watchLeaksFixed: []（新卡 augent 已进 userFollowWatch + freeMintWatch + bnAgentWatch）
- fat cursors：agentPad 730→755（本轮 1 次 from: 分片，kept 25，帖 0，next ReceiptHash）；freeMint 66 / bnAgent 169 / elysium 283 未动
- discordPeekDeferred: true（DC 未登录）
- thinOfficialDeferred: true（本轮 ample 不打 THIN1–5 薄栏官号 from:）
- newThisRound: ["augent"]
- statusFlipThisRound: []
- le2hThisRound: []
- notify: true（真新收录 AUGENT，免费 claimFree 已 LIVE，overall 72。无≤2h）
- xReadsExtra: 1（get_users_by_usernames 核验 @AugentFun）。主扫 19 + silent 1 达到 minSpend 20、低于 softCap 28。开跑前 remaining 886，读后 865。

## 本轮判定

- **真新收录 AUGENT（@AugentFun，augent，overall 72，status=live，focus=false）。** 官网 https://augent.fun/ 与官推互证（资料栏 t.co 解析为 augent.fun；官网硬编码 https://x.com/AugentFun，meta twitter:site=@AugentFun）。账号 2026-11-18 22:08 CST 创建，4 粉、4 帖，bio「专为 Binance Agent ID 持有者打造 | 免费份额领取中，11月21日 12:52 UTC 开池，LP 销毁」。最近官帖（https://x.com/AugentFun/status/2123100156338024514，11-19 01:04 CST）写 $AUGENT is ive / free mint。config.js 已填合约 0xAAdD9058b3DaaB00439457D82c2C508a5cc1c393（BSC，token+sale 同一合约）。链上 getCode 有代码，name/symbol=AUGENT，totalSupply=100 亿；freeClaimed=292/2999，paid sold=1（raised 0.001 BNB），phase=1，paused=0，pair=0。持 .ai Agent ID 可 claimFree 免费 1 份（20 万 AUGENT，只付 gas）；付费 0.001 BNB/份、每钱包最多 10 份。开池/截止 2026-11-21 20:52:53 CST，约 58.1 小时后（le2h=false）。官网称买卖各 3% 税、到期无论售罄与否自动开池。由本窗 KW_MINT 第三方 KOL @nhutqui2309 喊单发现。DeepSeek admit=true，overall 72，DS zoneHint=打新，卡片按 Agent ID 销售记入 BN Agent 钱包。非仓鼠/toychain，focus=false。按免费 LIVE 规则必须 notify。本号不自动 mint。
- **skip LineZero / @LineZero_NFT**：linezero.xyz 仍跳 /lander 空壳，无真实官网互证，不建卡。
- **skip GTADOTMOD / @GTADOTMOD**：gtamods.fun 本轮改为 HTTP 200（上轮 500），页面是 GTAMOD / RUGR（GTA V 内游戏发射台+钱包），不是可打 mint，不建卡。
- **skip U_R_LEGENDARY / legendary.fun**：官网仍 Coming soon，未到可操作窗口。
- **skip / 不重推 Fistagent / @Fistagent_（bonkagent）**：同一已提醒 mint LIVE，本窗继续营销，链上合约 0x4a6E3f6d464f44D6F0809a3B08b02045E5d7bA29 totalMinted 仍为 4，不重推。
- **skip / 不重推 thedawgzrh / @Thedawgzrh**：本窗见到官号被转发称 Minting on Nov 19th Fully FREE，并带 OpenSea 合集链接；OpenSea 页仍写 Minting soon / No items found，官网 meta 仍为申请白名单。维持 watching，不视为已核验免费 mint LIVE，不重推。
- **skip / defer StrateFai / @StrateFai_HQ**：仅出现在 KW_MINT 转发里的 Genesis free mint 话术，本轮未核到官网与官推互证，不建卡。
- **skip / 不重推 useFeely / @useFeely**：已在库的 LIVE 发币代理，静号 24h 窗再出现教学帖，同窗口不重推。
- **skip 已在库 KOL 赠票**：ETA / SyndicateRHC / Gloopix 等免费 mint 赠票转帖，官方未宣布新的 LIVE 翻转，不重推。
- **skip OrdDropz / crc20.garden**：比特币 / CRC-20 工具与市场评论，不是新打新项目。
- **skip KW_GO GTA 6 / Vice City 游戏新闻**：与加密打新无关；@ViceClubX 与 vice6fun 不是同一项目。
- **skip KW_SN Bramble**：检索命中为猫 / 游戏噪音。
- **The Notties / @thenottiesworld**：官网仍 COLLECTION LOCKED；白名单域名申请页 HTML 与上轮完全一致，不视为新的免费登记翻转，不重推。
- **8BITS HOOD / @8bitshood**：官网仍 MINTING SOON ON OPENSEA，维持 announced，不重推。
- **Unicorn Grand Prix / @UnicornGPrix**：白名单接口仍 open=true、phase=FCFS，count 519/15000（上轮 518，+1，剩 14781），不视为新翻转，免费 mint 日期仍 TBA，不重推。
- **Dead Zone / @DeadZonecrypto**：同一已提醒付费 mint LIVE，API 仍 open=true，minted=118/4500（与上轮相同），VIP pack sold 仍 3，0.01 SOL/份，不重推。
- **VICE6 / @Vice6fun**：仍 PRE-LAUNCH，距 2026-11-20 08:00 CST 约 21.2 小时，le2h=false，CA 未公布，不重推。
- **the one（@yuange99988852）**：仍 announced。距 2026-11-19 19:00 CST 约 8.2 小时，le2h=false，尚未 LIVE，不重推。
- **SpiritsRH**：免费 mint 窗口 2026-11-20 00:00 CST，距约 13.2 小时，le2h=false，不重推。
- **Oathbots**：代币窗口 2026-11-19 22:00 CST，距约 11.2 小时，le2h=false；官网仍跳 /lander。不重推。
- **Just Headz / @JustheadzHQ**：同一已提醒白名单已开窗口，本窗未见 mint LIVE，不重推。
- **GTAFounder / @GTAFounder**：同一已提醒 LIVE 窗口，仍以已核验平台币 CA ALtBh7RxCc98sp6vG4EmMQ1VFWfvoWSTvUPqyFwmGTA6 为准，不重推。
- **Zolk / @zolkdotio**：同一已提醒森林寻卡白名单窗口，官网仍可登录寻卡，Nothing on chain yet，未见 mint/CA，不重推。
- **rooms.fun / @shroomsdotfun**：同一已提醒 LIVE 发射台，本窗未强制再读官号，未见新翻转，不重推。
- **INMATES / @INMATES_RH**：同一已提醒窗口。GTD 申请窗仍 2026-11-19 09:00–19:00 CST，约 8.2 小时后关，le2h=false；表单仍只写本机 localStorage，页面仍写明不向团队提交，暂无 CA。不重推。
- **Agent Miner / @AIMMinerBSC**：同一已提醒免费 LIVE，链上 totalMinted 716（上轮 715，+1），不重推。
- **AONE / @aone_agent**：同一已提醒开池/抽干窗口。链上 freeMinted 仍 10000/10000、hero 仍 22864；Pancake V2 对约 0.0097 BNB（与上轮相同），不重推。
- **All in crypto / @allincrypto_ai**：同一已提醒开池窗口。链上 totalMinted 11297（上轮 11136，+161），opened=1，paused=0；本轮 nextPrice()/currentPrice() eth_call 仍回退，下档价按价格曲线本地估算约 0.0024 BNB；Pancake V2 官方对约 52.05 BNB（上轮约 33.85）；LB totalShares=11318、holderCount=1022（上轮 11131 / 892；updatedAt 2026-11-19 10:43:46 CST，接口已刷新，略高于链上）。不重推。
- **Bsc Cat / @Bobkjyj**：同一已提醒免费 LIVE，freeMinted 550/800（与上轮相同），paid=0，pair 仍为 0，不重推。

## 覆盖与节流

- 判断/文案/打分一律 DeepSeek（deepseek-flash，思考开启）。DS 对 AUGENT admit=true、overall 72、zoneHint 打新。无 DS fallback。
- 本号不自动 mint。
- 下一轮 mentions：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；silent=LayerZero；UF next=493 OmbrelloNFT。
