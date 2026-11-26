# 早期打新雷达 R2219 RESULT

工作目录 /tmp/r2219/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_TAPE）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 09:34 CST。写盘 lastScout=2026-11-26 09:45:15 CST。这是重置后的第四轮常规增量，不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。关键站点/API/链上核验约 09:37–09:42 CST。

## 额度与模式

- 开火前 remainingBefore=917。首搜 UF1 之后今日剩余 916（脚注 remainingMinute=29 / remainingToday=916，todayReset=2026-11-27T00:00:00.000Z），确认 ample，继续主计划 21 次 + 条件瘦栏 24h 4 次。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 24 + silent 1 = 25，低于 softCap，已达 minSpend。未翻页（多组触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=25（main=24，silent=1），remainingBefore=917，remainingAfter=892。
- 写盘 meta.xBudgetMode=ample。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 0/916，UF2 1/915，MUST_WIN 25/914（触顶有 next_token，未翻页），MUST_OFF 0/913，
KW_LZ 0/912，KW_TAPE 18/911，KW_GIWA 16/910，KW_DOGE 2/909，KW_BTC 3/908，KW_STARK 2/907，
KW_MINT 25/906（触顶），KW_MINE 1/905，KW_PAD 25/904（触顶），KW_GO 25/903（触顶），KW_ELY 8/902，KW_GAPS 7/901，
MEN_GIWA 25/900（触顶），MEN_TAPE 6/899，MEN_LZ24 24/898，MEN_ELY 20/897，
SILENT_TAPE 1/896，
KW_LZ_24 23/895，KW_DOGE_24 25/894（触顶），KW_BTC_24 25/893（触顶），KW_STARK_24 25/892（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 18、GIWA 16、DOGE 2、BTC 3、STARK 2、MINT 25 触顶、MINE 1、PAD 25 触顶、GO 25 触顶、ELY 8、GAPS 7。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完。cursor 447 @ElysiumDegens 起 50 号至 @elysiumbrokers；写盘后 cursor 497 @rheacatnear，wrap=false。预跳已知 NF 9 个（用户点名但长期 NF 的 @starx_xlayer 本分片未做 getUsers 重读，仅可出现在 mentions 查询里），故 from: 实际 41 个（UF1 24 + UF2 17）。UF1 result_count=0。UF2 1 帖（已在库 @FloorFeed：Chef's Kiss Frenzy 免费报名说明，非新开铸）。写盘后 UF 总账户 2439（本轮无新挂号）。
- 瘦栏 24h：仅对 30m 命中 <5 的栏各补 1 次。已补 LZ（30m=0→23）、DogeEVM（30m=2→25 触顶）、BTC（30m=3→25 触顶）、Starknet（30m=2→25 触顶）。跳过 Tape（30m=18）、GIWA（30m=16），原因 30m>=5。未把肥栏改成 24h。thin24hDeferred=false。
- mentions 覆盖: GIWA 25 触顶 / Tape 6 / LayerZero 24 / Elysium 20（均为 24h 轮换）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。mentionsDeferred=false。
- silent: Tape/电路（search_users 不可用，24h has:mentions 回退；result_count=1，seen=1 未知作者 @XiaoMei_laika，sentToReview=0，admitted=0，ran=true）。该号是 TapeOut 中文汇总，非新项目，未送审。下轮：GIWA。silentDeferred=false。

## 新收录

无。newThisRound=[]。

DeepSeek admit 初审曾建议收录 Hamster CombatHQ（@HamsteCombatHQ），但随后 score 明确 admit=false（overall=38），最终未入库。详见「看见但未收」。

## 看见但未收

- Hamster CombatHQ（@HamsteCombatHQ / Telegram https://t.me/hamster_combat_nfthub）：建号 2026-11-20 02:34:18 CST（约 6.29 天），29 粉 / 3 帖，xUserId 2123484663654014976。资料栏自称 1,111 Unique Characters、100% FREE MINT、Coming to @RobinhoodApp。资料栏链接是 Telegram 群而非官网。本轮该号无原创帖（未额外重读），只在 KW_MINT 见到 @Yuuto86294 转发其官帖（https://x.com/Yuuto86294/status/2125765286536335716）：Free Mint / Robinhood Chain / WL Launching Soon / GTD。无独立官网、无合约、无 OpenSea 集合。不是已确认免费 mint LIVE。DS admit 初审为 true，但 score 为 admit=false、overall=38，理由包括无官网/合约可核、链接仅 Telegram、名称借用 Hamster Kombat、仅白名单预告；最终未收录。
- Velmar（@velmarstocks / https://www.velmarstocks.xyz/）：建号约 3.98 天、18 粉 / 8 帖。官网 HTTPS 200，是 Robinhood Chain stock token 链上价格跟踪器，不是 mint/发射台。DS admit=false。
- Zayro Perps（@zayrotrade / https://zayro.trade/）：建号约 7.67 天、970 粉 / 21 帖。官网 HTTPS 200 且回链 @zayrotrade，GIWA 测试网永续合约，不是免费 mint；粉数相对建号时长偏热。DS admit=false。
- @LexKora：建号约 0.02 天，只是报名 @LawoftheAbyss 免费 mint，不是项目方。
- @WorldsEndFarm：Starknet「Bramble」关键词误伤（农场清杂草），跳过。
- @0xRein：自称 building @rushrtrade，本轮只发了一篇 X article 链接，无独立官网，未送审。
- @XiaoMei_laika：SILENT_TAPE 见到的 TapeOut 中文汇总号，非新项目，未送审。
- 其余 KW/mentions 多为已在库项目转载、KOL 互动或无站点无官帖的噪声。MUST_WIN 25 条均为已在库官号（fueltenderagent 10、2hourfun 8、ShieldedWizBTC 3、GunsOfTheHood 2、antopia_xyz 1、AgentCardsHQ 1），只做状态刷新。MUST_OFF 0 帖。UF2 仅已在库 @FloorFeed。

## 关键刷新 — 库内无改期、无首次 ≤2h（不重推）

- 2hour.fun @2hourfun：第一场窗口仍关闭。RSC payload `open=false`；首页 SSR 仍可能显示 Window open 占位，不以该标签为准。下一窗仍为 2026-11-27 05:00–07:00 CST（约 19.2h，未到 ≤2h）。平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 14.3%（与 R2218 持平），约 $5.1k mcap，已筹约 15.98 SOL / 约 $1130，最后成交约 09:35:23 CST。关窗、第二窗时间与发币费改免费此前已通知，本轮只是进度，不重推。
- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=114/3333（与 R2218 持平），reserved=6，mintOpen=true，price=0。公售页 https://brimhollow.app/mint 。官帖仍称 public mint is still open，并预告明日加 staking / Voting tab。R2210 已通知，本轮只是进度。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop mintStatus=MINTING，90/10000（与 R2218 持平），持有 13，地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d。R2210 已通知，只是进度。不是免费 mint。
- Ugly Puggies：仍 MINTING，312/777（R2218 为 311），持有 239，地板 0.000168 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST（约 3.7h，未到首次 ≤2h；该阶段结束后仍是 SIGNED_PRESALE #3，公售 2026-11-27 13:30 CST）。不提前告警。
- deMiners：仍 MINTING，1364/3333（持平），持有 180，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（与 R2218 持平），现价约 0.00216 BNB。只是进度。
- TRIFORGE：链上 Forge Keys 812/3333（R2218 为 797），claims 38（R2218 为 34）。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上 457/10000（R2218 为 450），mintOpen=True。只是进度。
- Antopia：链上 6264/8888（R2218 为 6253），saleOpen=True，免费额度仍满。本轮 MUST 官帖仍称付费窗至 2026-11-27 12:45 UTC（20:45 CST）关闭，Clash of Antopia 今日 13:00 UTC（21:00 CST）上线（gameAtCST 此前已记）。距关停约 35h，未到 ≤2h，不是改期，不重推。
- VALORIX：链上 Hero Cards 16（与 R2218 持平），fillSold=0/5500。只是进度。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」。本轮 MUST 未见 @Agx_bsc，未做额外 X 重读。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 34.7h，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：官网仍 Early List。SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍自 2026-11-27 01:00 CST 起，距首窗约 15.2h，未到首次 ≤2h。同名合集 vicehood（非该官号，本轮仍 209/3333 已在铸）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 11.7h，未到首次 ≤2h，不提前告警。
- Bons Genesis @bons_world：官网仍存活。OpenSea bons-genesis 仍 119/1111，SeaDrop 仍 MINTING，active PUBLIC_SALE 至 2026-12-22 01:00 CST。原免费 WL 窗已过，公售仍开；旧 le2h 文案已过期。不是免费 mint LIVE，不重推。本轮 osstats 401，持有/地板未刷新，供应与阶段与上轮一致。
- CITYHOOD @appcityhood / cityhood.fun：官网仍 Minted 0/4,333，并残留已过期「Public mint opens today」。原 2026-11-23 窗口已过，无改期、无新开铸确认。勿与 @CityHood_NFT 合并。
- CITYHOOD @CityHood_NFT / cityhood.online：前端 /api/config 本轮返回 SPA HTML；后端 https://cityhoodbackend-production.up.railway.app/api/config 仍 chainId=46630 Robinhood Chain Testnet，合约地址与此前相同。市民登记仍开，主网铸造未确认，不是免费 mint LIVE。勿沿用过期「今晚 22:00」文案。
- ClankTube：免费早期登记仍开（关注+互动+EVM 地址），未见开铸，不重推。
- OTC Rings / Famulus：R2216 新卡，本轮站点仍存活，状态未变，不重推。
- FOMO4NFT：R2217 新卡，官网与发射台仍 HTTP 200，非免费 mint，状态未变，不重推。
- Heliring：R2218 新卡，官网仍 HTTP 200，仍展示 CA 4GyoxBumvdsYoTMZTbQsu4z5ZsdtQX1YCtq7GjBApump，非免费 mint，状态未变，不重推。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

notify=false。

- 原因：本轮无新收录。库内 2hour / Wizards / Guns / Vicehood / Wildlife / Ugly Puggies / Bonebloom / Bons / CityHood / FOMO4NFT / Heliring / ClankTube 等无改期、无首次 ≤2h，不按进度重推。R2216 / R2217 / R2218 新卡无状态变化，不重推。HamsteCombatHQ 仅白名单预告且 score 拒绝，未入库、不告警。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=[]，le2h=[]。
- dsFallback=false。
- discordPeekDeferred=true：X 路径未打开 Discord/浏览器，只写占位，须父进程同一轮补 Peek。不要假装已 Peek。登录墙与此前轮次相同，不要重发登录表单，除非已有新会话。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 data.json + docs/data.json + RESULT_R2219.md 到 Reboot7454/early-scout main。
- 下轮：UF 从 cursor 497 @rheacatnear 继续；mentionsNext=DogeEVM / BTC / Starknet / pads+squeek+STARX；静号=GIWA。
