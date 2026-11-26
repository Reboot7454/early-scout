# 早期打新雷达 R2221 RESULT

工作目录 /tmp/r2221/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_DOGE）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 10:35 CST。写盘 lastScout=2026-11-26 10:46:01 CST。这是重置后的第六轮常规增量，不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。关键站点/API/链上核验约 10:38–10:42 CST。

## 额度与模式

- 开火前 remainingBefore=868。首搜 UF1 之后今日剩余 867（脚注 remainingMinute=29 / remainingToday=867，todayReset=2026-11-27T00:00:00.000Z），确认 ample，继续主计划 21 次 + 条件瘦栏 24h 3 次。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 23 + silent 1 = 24，低于 softCap，已达 minSpend。未翻页（多组触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读（KW_GAPS 查询里包含该 handle，仅作为关键词检索）。
- xReads=24（main=23，silent=1），remainingBefore=868，remainingAfter=844。
- 写盘 meta.xBudgetMode=ample。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 0/867，UF2 0/866，MUST_WIN 25/865（触顶有 next_token，未翻页），MUST_OFF 0/864，
KW_LZ 0/863，KW_TAPE 12/862，KW_GIWA 22/861，KW_DOGE 4/860，KW_BTC 1/859，KW_STARK 5/858，
KW_MINT 25/857（触顶），KW_MINE 2/856，KW_PAD 25/855（触顶），KW_GO 25/854（触顶），KW_ELY 9/853，KW_GAPS 11/852，
MEN_GIWA 25/851（触顶），MEN_TAPE 6/850，MEN_LZ24 23/849，MEN_ELY 20/848，
SILENT_DOGE 0/847，
KW_LZ_24 23/846，KW_DOGE_24 25/845（触顶），KW_BTC_24 25/844（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 12、GIWA 22、DOGE 4、BTC 1、STARK 5、MINT 25 触顶、MINE 2、PAD 25 触顶、GO 25 触顶、ELY 9、GAPS 11。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 547 @yeetr_fun → 写盘后 cursor 597 @agentic_pixels_，wrap=false，分片末端 @quadConnects。预跳已知 NF 13 个（@agentpunkai @stockcatsfun @Volitionxyz @tollsfun @whackyrh @bibiainft @AgentBoss_AI @Trysmolpadfun @obolworld @Elysium_Rocks @agents_estates @ClassifiedMRNG @Villagers_RH），from: 实际 37 个（UF1 24 + UF2 13）。UF1 result_count=0，UF2 result_count=0，本轮分片无帖。UF 总账户写盘后 2441（含本轮新挂的 @usePrivMine）。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（均为 24h；MEN_GIWA 25、MEN_TAPE 6、MEN_LZ24 23、MEN_ELY 20）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_DOGE_24（30m=4→24h=25）、KW_BTC_24（30m=1→24h=25）。TAPE 12、GIWA 22、STARK 5 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO）改成 24h。
- 静号：SILENT_DOGE，search_users 不可用，24h has:mentions 回退。ran=true，seen=0，sentToReview=0，admitted=0。上一轮无 queued handles，未做 getUsers 第二读。下轮静号指向 BTC。

## 新收录

- PrivMine @usePrivMine（id=usePrivMine），类别 挖矿，chain=Solana，focus=false，不是免费 mint/登记。
- 建号 2026-11-26 07:11:38 CST（约 0.15 天），4 粉 / 15 帖 / 0 关注，xUserId 2125728889963958272。
- 官帖 2026-11-26 10:25:29 CST（https://x.com/usePrivMine/status/2125777934174834758）宣布 PrivMine is live：发币即开通私有 hSOL 矿，浏览器可挖，The first mine is already live；随后 10:26:58 CST（https://x.com/usePrivMine/status/2125778307626959103）说明 WebGPU/CPU 挖矿与 Helius Privacy Rings 结算。官帖链接 http://privmine.fun。
- 官网 https://privmine.fun/ 本轮 HTTPS 200，标题 PrivMine · launch a coin, open a private mine，页面有 Open a mine / Dig / Live mines 与发币表单；$PRIVMINE Launching soon。X→站由官帖互证；站点 HTML 无 twitter:site，仅有泛化 https://x.com/ 链接（siteXMutual=partial）。
- DeepSeek admit：极早期且官宣已 live、官网可交互。score overall=62（early=95，actionable=55，novelty=60，risk=80）。已挂 userFollowWatch + miningWatch + agentPadWatch。

## 看见但未收

- Nether @nethercash：官网 https://nether.cash/ 存活且回链 @nethercash，自称 Tor 上的 Solana fork（Block 925、Validators 1）。建号约 42.7 天、32 粉 / 7 帖。本轮仅发一篇 X Article，无新 mint/发射/登记窗口。DeepSeek skip：更像已在运行的隐私链基础设施。
- MemePredictions @MemePredictfun：建号约 50.8 天。官帖称 prediction market contract is ready for launch，但明确等待行情转暖，未见已开盘入口。DeepSeek skip。
- Animalverse：本轮仅见到非官号 @skyyrh2xg 转发 https://animalverse.social/；官号 @Animalverse_NFT 本轮无官帖（未额外重读），不收录该转发号。
- RingPad：@Nostalgicgareth 称 RingPad is live（https://www.ringpad.bond/ SPA 200）。已在库 @theringpad（R1605），不新建卡，未额外重读官号。
- LumixPad / antwork / @HamsteCombatHQ：本轮未见，无需反复送审。
- 其余 KW/mentions 多为已在库项目转载、KOL 互动或无站点无官帖的噪声。MUST_WIN 25 条均为已在库官号（2hourfun、fueltenderagent、ShieldedWizBTC、uglypuggies、GunsOfTheHood、antopia_xyz、AgentCardsHQ），只做状态刷新。MUST_OFF 0 帖。UF 本轮 0 帖。

## 关键刷新 — 库内无改期、无首次 ≤2h（不因进度重推）

- 2hour.fun @2hourfun：第一场窗口仍关闭。RSC payload `open=false`；首页 SSR 仍可能显示 Window open 占位，不以该标签为准。下一窗仍为 2026-11-27 05:00–07:00 CST（约 18.2h，未到 ≤2h）。平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 18.2%，约 $6.0k mcap，已筹约 20.37 SOL / 约 $1449（R2220 约 14.3% / $5.2k / 16.03 SOL），最后成交约 2026-11-26 10:30:11 CST。关窗、第二窗时间与发币费改免费此前已通知，本轮 MUST 最新官帖仍是 07:07 CST，只是进度，不重推。
- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=118/3333（与 R2220 持平），reserved=7（R2220 为 6），mintOpen=true，price=0。公售页 https://brimhollow.app/mint 。R2210 已通知，只是进度。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop mintStatus=MINTING，100/10000（与 R2220 持平），持有 14，本轮 osstats 401，地板未从 API 取到。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d。R2210 已通知，只是进度。不是免费 mint。
- Ugly Puggies：仍 MINTING，312/777（与 R2220 持平），持有 239，地板 0.000167 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST（写盘时约 2.7h，未到首次 ≤2h；该阶段结束后仍是 SIGNED_PRESALE #3，公售 2026-11-27 13:30 CST）。MUST 再见到 2026-11-26 10:02:13 CST 官帖（R2220 已记录）承认 mint 不及预期；OpenSea 阶段表仍未改，不按改期重推，也未到首次 ≤2h。
- deMiners：仍 MINTING，1373/3333（R2220 为 1368），持有 181，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（与 R2220 持平），现价约 0.00216 BNB。MUST 再见到 08:06 CST 补偿方案官帖（R2220 已记录），不是改期或新开铸。
- TRIFORGE：链上 Forge Keys 822/3333（R2220 为 817），claims 38（持平）。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上 462/10000（R2220 为 458），mintOpen=True。只是进度。
- Antopia：链上 6315/8888（R2220 为 6305），saleOpen=True，免费额度仍满。MUST 再见到 08:19 CST 官帖（R2220 已记录）仍称付费窗至 2026-11-27 12:45 UTC（20:45 CST）关闭，Clash of Antopia 2026-11-26 13:00 UTC（21:00 CST）上线。距关停约 34.0h，距 Clash 约 10.2h，未到 ≤2h，不是改期，不重推。
- VALORIX：链上 Hero Cards 16（与 R2220 持平），fillSold=0/5500。只是进度。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」。本轮 MUST_WIN 24h 结果中未见 @Agx_bsc 帖，未做额外 X 重读。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 33.7h，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：官网仍 Early List。SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍自 2026-11-27 01:00 CST 起，距首窗约 14.2h，未到首次 ≤2h。同名合集 vicehood（非该官号，本轮仍 209/3333 已在铸）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 10.7h，未到首次 ≤2h，不提前告警。
- Bons Genesis @bons_world：官网仍存活。OpenSea bons-genesis 仍 119/1111，SeaDrop 仍 MINTING，active PUBLIC_SALE 至 2026-12-22 01:00 CST。本轮 osstats 再遇 401，改从 HTML 解析：持有 59，地板 0.4 USDG。原免费 WL 窗已过，公售仍开。不是免费 mint LIVE，不重推。
- CITYHOOD @appcityhood / cityhood.fun：官网仍 HTTP 200，页面仍残留已过期窗口文案。原 2026-11-21/23 窗口已过，无改期、无新开铸确认。勿与 @CityHood_NFT 合并。
- CITYHOOD @CityHood_NFT / cityhood.online：前端仍 200。市民登记/测试网状态未见改期或主网开铸确认，不是免费 mint LIVE。勿与 cityhood.fun 合并。
- ClankTube：https://clanktube.fun 仍 HTTP 200，标题 ClankTube — Early Access，页面仍写 early access open，免费早期登记仍开（关注+互动+EVM 地址），未见开铸，不重推。
- OTC Rings / Famulus：R2216 新卡，无状态变化，不重推。
- FOMO4NFT：R2217 新卡，官网 https://fomo4nft.com 与发射台 https://launch.fomo4nft.com 仍 HTTP 200，非免费 mint，状态未变，不重推。
- Heliring：R2218 新卡。本轮访问 https://heliring.app/ 仍遇到 TLS 错误（TLSV1_ALERT_INTERNAL_ERROR），未能重新打开页面。未见新官帖或改期/开铸证据（MUST 未覆盖该号，未额外重读）。非免费 mint，不按状态变化重推。
- Edict @edictink：R2220 新卡。官网 https://edict.ink/ 与 Launch 页仍 HTTPS 200，twitter:site 仍指向 @edictink，$EDICT 仍预告中。非免费 mint，无状态变化，不重推。
- Canton/Glaze/TokenWorks：本轮无新该类 admit，仅刷 lastChecked。

## notify 判定

- notify=true。
- alertMessage：新收录 PrivMine（@usePrivMine）：Solana 隐私挖矿发射台已开站，$PRIVMINE 即将发射；本轮无免费 mint/登记；本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
- 原因：真新收录 PrivMine。库内 2hour / Wizards / Guns / Vicehood / Wildlife / Ugly Puggies / Bonebloom / Bons / CityHood / FOMO4NFT / Heliring / ClankTube / Edict 等无改期、无首次 ≤2h，不按进度重推。Ugly Puggies 写盘时距 13:30 CST 约 2.7h，未到首次 ≤2h。R2216 / R2217 / R2218 新卡及 R2220 Edict 无状态变化，不重推。PrivMine 不是免费 mint/登记，告警已点名项目，未写成「入库 N 项见面板」。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=["usePrivMine"]，le2h=[]。

discordPeekDeferred=true（X 路径占位，未假装已 Peek）。dsFallback=false。

面板：https://reboot7454.github.io/early-scout/

## 交付

- 推送文件：data.json、docs/data.json、RESULT_R2221.md（仅这三项进 main）。
- notify.json 已写 /tmp/r2221/notify.json（通常不提交）。
