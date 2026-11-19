# RESULT R1960

- time: 2026-11-19 10:09:22 CST
- mode: ample（R1956 为 08:00 CST 后首轮全量补扫；本轮为其后第四轮正常节流，lastFullAfterReset 仍为 R1956）
- xReads: 21（main 19 + silent 1 + EXTRA 1）
- remainingBefore: 907 → remaining: 886
- softCap 28 / minSpend 20 / silentCap 2 / ufAccountShard 50
- tenLanes: yes（11 条关键词全跑：LZ 0 / TAPE 25 / GIWA 12 / DOGE 25 / BTC 3 / SN 1 / MINT 25 / MINE 0 / PAD 25 / GO 25 / ELY 25。TAPE/DOGE/MINT/PAD/GO/ELY 触顶，未翻页。部分 write_to_file 中段省略，只回收头部较新帖，未重查）
- userFollow: 刷完本分片，wrap=false。start 353 MedalBeasts，kept 50（MedalBeasts→kingdomflash），walkScanned 73，NF_skip 23（tickupfun / darkllartech / Headroom_X / bnAgent_ / AgentID_AI / PrinterAi_BNB / telefees_pump / agentkin_ / AgenticHive / pitpadfun / torpornet / bsc_bito / tikitotemsbnb / seppidev / CachetDotFun / Nonce_CTO / claudesprotocol / wedowtf / manekinecoinft / stonkaxyz / BabelAgent / TurboKartBNB / wuseagent），skip_already 0。next 426 agentrybaw。prio_folded：machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets。prio_skipped：mobster_meme / starx_xlayer。MUST 另加 @shroomsdotfun。本分片 UF 帖 UF1=0 / UF2=0。
- mentions: 本轮轮换子集 4 组 LayerZero 2 / Elysium+kinetiq 6 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 0。下一轮子集 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent: 台子/Meme（1960%11=2；SILENT_MEN result_count=25，约 24h 窗；search_users 仍不可用）。25 条（部分文件截断仅回收头部）未见需新收录的官方项目送审。下一轮 silent=GO盘。
- watchLeaksFixed: []（新卡 inmates 已进 userFollowWatch + freeMintWatch）
- fat cursors 未动：agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283
- discordPeekDeferred: true（DC 未登录）
- thinOfficialDeferred: true（本轮 ample 不打 THIN1–5）
- newThisRound: ["inmates"]
- statusFlipThisRound: []
- le2hThisRound: []
- notify: true（真新收录 INMATES，自称免费 mint / GTD 窗展示开放；虽 overall 47 且表单只写本机、并非确认后端登记，按免费 mint/登记规则必须提醒。无≤2h）
- xReadsExtra: 1（get_users_by_usernames 核验 @INMATES_RH 等一批）。主扫+silent=20，达到 minSpend 20、低于 softCap 28。开跑前 remaining 907，读后 886。

## 本轮判定

- **真新收录 INMATES（@INMATES_RH，inmates，overall 47，status=announced，focus=false）。** 官网 https://www.inmates.online/ 与官推互证（官帖 t.co 解析为 inmates.online；官网硬编码 https://x.com/INMATES_RH）。账号 2026-11-18 08:19 CST 创建，246 粉、6 帖，bio「999 inmates tomorrow on @robinhoodapp. Free Mint.」。官帖称 Mint tomorrow claim your GTD / Close in 10 hours（https://x.com/INMATES_RH/status/2123233962432553326）。GTD 申请窗 JS 计时 2026-11-19 09:00–19:00 CST，当前已开，约 8.8 小时后关闭（le2h=false）。任务为关注/点赞/转发后填 X 用户名 + EVM 钱包；但表单只写入本机 localStorage（key=inmates-local-registrations-v1），页面写明「This page does not send registrations to the team.」，并非确认后端白名单登记。页脚 Independent NFT project，未见 CA，与 Robinhood 官方无关。DeepSeek admit=true，栏目打新，overall 47。按免费 mint/免费登记规则必须 notify，并如实写明表单无效。本号不自动 mint。
- **skip LineZero / @LineZero_NFT**：本窗再次出现在 MEN_LZ「LFG free mint」话语中。linezero.xyz 仍是空壳/Afternic 售域页，无真实官网互证，不建卡。
- **skip GTADOTMOD / @GTADOTMOD**：账号 2026-11-13 创建、34 粉，站点 gtamods.fun 本轮 HTTP 500；内容是 NASDUCK 仓库点评，不是可打 mint。
- **skip FlazeCoin / @flazepad**：2022 年起的 BNB 代币及较旧发射台（flaze.org / Hashlock 审计），不是本轮早期新项目。
- **skip U_R_LEGENDARY / legendary.fun**：仅第三方发射台喊单，官网 Coming soon，未到可操作窗口。
- **skip Koajo / koajodotfun**：Koajo 是 2009 年个人账号；koajodotfun 查无此号。bonding-curve 推文不是新项目官号。
- **skip / 不重推 Fistagent / @Fistagent_（bonkagent）**：同一已提醒 mint LIVE，本窗继续营销，链上合约 0x4a6E3f6d464f44D6F0809a3B08b02045E5d7bA29 totalMinted 仍为 4，不重推。
- **rooms.fun / @shroomsdotfun**：同一已提醒 LIVE 发射台。09:33 CST 官帖 PSA（https://x.com/shroomsdotfun/status/2123228192735740047）称平台没有自身代币，改为战略投资首个 room/token $SMOOR（0x0c4cb3d13067bd5d86a857f3344a47ecc7160c02）。只更新卡片，不重推。
- **skip OrdDropz**：比特币 Ordinals 工具/市场评论，不是新打新项目。
- **skip 已在库 KOL 赠票**：Enter The Anime / SyndicateRHC 等免费 mint 赠票转帖，官方未宣布新的 LIVE 翻转，不重推。
- **skip KW_GO GTA 6 游戏上市新闻**：与加密打新无关。
- **skip KW_SN Bramble**：检索命中为游戏 / Yu-Gi-Oh 噪音。
- **Unicorn Grand Prix / @UnicornGPrix**：白名单接口仍 open=true、phase=FCFS，count 仍 518/15000（剩 14782），与 R1957–R1959 相同，不视为新翻转，免费 mint 日期仍 TBA，不重推。
- **Dead Zone / @DeadZonecrypto**：同一已提醒付费 mint LIVE，API 仍 open=true，minted=118/4500（上轮 104，+14），VIP pack sold 仍 3，0.01 SOL/份、买 10 送 1，游戏与 $DZ 未上线。进度更新不视为状态翻转，不重推。
- **The Notties / @thenottiesworld**：官网仍 COLLECTION LOCKED / COMING SOON；口径与前轮相同，官方未宣布开放，不视为免费登记翻转，不重推。
- **8BITS HOOD / @8bitshood**：官网 HTTP 200，本轮页面抓取未见 mint LIVE 文案，维持 announced，不重推。
- **VICE6 / @Vice6fun**：仍 PRE-LAUNCH，距 2026-11-20 08:00 CST 约 21.8 小时，le2h=false，CA 未公布，不重推。
- **the one（@yuange99988852）**：仍 announced。距 2026-11-19 19:00 CST 约 8.8 小时，le2h=false，尚未 LIVE，不重推。
- **SpiritsRH**：免费 mint 窗口 2026-11-20 00:00 CST，距约 13.8 小时，le2h=false，不重推。
- **Oathbots**：代币窗口 2026-11-19 22:00 CST，距约 11.8 小时，le2h=false；官网跳 /lander。不重推。
- **Just Headz / @JustheadzHQ**：同一已提醒白名单已开窗口，本窗未见 mint LIVE，不重推。
- **GTAFounder / @GTAFounder**：同一已提醒 LIVE 窗口，仍以已核验平台币 CA ALtBh7RxCc98sp6vG4EmMQ1VFWfvoWSTvUPqyFwmGTA6 为准，不重推。
- **Zolk / @zolkdotio**：同一已提醒森林寻卡白名单窗口，官网仍可登录寻卡，Nothing on chain yet，未见 mint/CA，不重推。
- **Agent Miner / @AIMMinerBSC**：同一已提醒免费 LIVE，链上 totalMinted 715（上轮 712，+3），不重推。
- **AONE / @aone_agent**：同一已提醒开池/抽干窗口。链上 freeMinted 仍 10000/10000、hero 仍 22864；Pancake V2 对约 0.0097 BNB（与上轮相同），不重推。
- **All in crypto / @allincrypto_ai**：同一已提醒开池窗口。链上 totalMinted 11136（上轮 11131，+5），opened=1，paused=0；本轮 nextPrice()/currentPrice() eth_call 仍回退，下档价按价格曲线本地估算约 0.0024 BNB；Pancake V2 官方对约 33.85 BNB（上轮约 33.22）；LB totalShares 仍 11131（落后链上 5 份，updatedAt 仍为 2026-11-19 09:33:52 CST，接口偏旧）、holderCount=892。不重推。
- **Bsc Cat / @Bobkjyj**：同一已提醒免费 LIVE，freeMinted 550/800（上轮 548，+2），paid=0，pair 仍为 0，不重推。

## 覆盖与节流

- 判断/文案/打分一律 DeepSeek（deepseek-flash，思考开启）。DS 对 INMATES admit=true、overall 47、栏目打新。无 DS fallback。
- 本号不自动 mint。
- 下一轮 mentions：Tape / GIWA / BTC / Starknet+DogeEVM；silent=GO盘；UF next=426 agentrybaw。
