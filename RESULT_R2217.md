# 早期打新雷达 R2217 RESULT

工作目录 /tmp/r2217/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_LZ）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 08:35 CST。写盘 lastScout=2026-11-26 08:50:25 CST。这是重置后的第二轮常规增量，不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。关键站点/API 核验约 08:39–08:44 CST。

## 额度与模式

- 开火前 remainingBefore=966。首搜 UF1 之后今日剩余 965（脚注 remainingMinute=29 / remainingToday=965，todayReset=2026-11-27T00:00:00.000Z），确认 ample，继续主计划 21 次 + 条件瘦栏 24h 4 次。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 24 + silent 1 = 25，低于 softCap，已达 minSpend。未翻页（多组触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。
- xReads=25（main=24，silent=1），remainingBefore=966，remainingAfter=941。
- 写盘 meta.xBudgetMode=ample。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 1/965，UF2 0/964，MUST_WIN 25/963（触顶有 next_token，未翻页），MUST_OFF 0/962，
KW_LZ 0/961，KW_TAPE 25/960（触顶），KW_GIWA 8/959，KW_DOGE 1/958，KW_BTC 2/957，KW_STARK 0/956，
KW_MINT 25/955（触顶），KW_MINE 0/954，KW_PAD 25/953（触顶），KW_GO 25/952（触顶），KW_ELY 10/951，KW_GAPS 11/950，
MEN_GIWA 25/949（触顶），MEN_TAPE 6/948，MEN_LZ24 25/947（触顶），MEN_ELY 20/946，
SILENT_LZ 25/945（触顶），
KW_LZ_24 23/944，KW_DOGE_24 25/943（触顶），KW_BTC_24 25/942（触顶），KW_STARK_24 25/941（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 25 触顶、GIWA 8、DOGE 1、BTC 2、STARK 0、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 10、GAPS 11。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完。cursor 347 @firstpadfun 起 50 号至 @bsc_bito；写盘后 cursor 397 @CarlettaRineb，wrap=false。预跳已知 NF 14 个（含分片起点 @firstpadfun；用户点名但长期 NF 的 @starx_xlayer 本分片未出现，未做 getUsers 重读），故 from: 实际 36 个（UF1 24 + UF2 12）。UF1 result_count=1（@1KArtGallery 回复 @ParisHilton，非项目动态），UF2 0 帖。写盘后 UF 总账户 2438（本轮新挂 1 个 @FOMO4NFT）。
- 瘦栏 24h：仅对 30m 命中 <5 的栏各补 1 次。已补 LZ（30m=0→23）、DogeEVM（30m=1→25 触顶）、BTC（30m=2→25 触顶）、Starknet（30m=0→25 触顶）。跳过 Tape（30m=25）、GIWA（30m=8），原因 30m>=5。未把肥栏改成 24h。thin24hDeferred=false。
- mentions 覆盖: GIWA 25 触顶 / Tape 6 / LayerZero 25 触顶 / Elysium 20（均为 24h 轮换）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。mentionsDeferred=false。
- silent: LayerZero（search_users 不可用，24h has:mentions 回退；result_count=25 触顶，seen=23 未知作者，sentToReview=0，admitted=0，ran=true）。第三方点到 @camelhoodwtf / @FrostHoodR，但 includes 无官号资料、无站点可核，未送审。下轮：Elysium。silentDeferred=false。

## 新收录

- FOMO4NFT（@FOMO4NFT / https://fomo4nft.com / https://launch.fomo4nft.com）→ 栏「台子/Meme」。2026-11-21 13:04:06 CST 建号（约 4.8 天），87 粉 / 19 帖。官网 HTTP 200，自称 Robinhood Chain 社交 NFT 交易；发射台 HTTP 200，标题 OnChain Launchpad，页面有 Minting now 分栏，自称 Fully onchain、OpenSea 交易、ERC-8004 agent。资料栏 URL 指向 OpenSea 合集 chain-society（1111/1111 已售完，twitterUsername=@MrBRC0，合约 0x42411286529e1da56c7c8c7535737961b2e06955）。官网未核到回链官推（siteXMutual=none）。本轮未见该号原创官帖，仅在讨论中被提及。不是免费 mint。DS overall=74，admit=true。已进 UF + agentPadWatch。focus=false。

newThisRound=['fomo4nft']。

## 看见但未收

- Hamster CombatHQ（@HamsteCombatHQ / 仅 Telegram https://t.me/hamster_combat_nfthub）：建号约 6.3 天、26 粉 / 3 帖。bio 与转推官宣自称 1,111 份 Robinhood 免费 mint，但 WL 仍 Launching Soon，无独立官网、无合集、无合约。DS overall=40，admit=false。
- @camelhoodwtf / @FrostHoodR：仅出现在 SILENT_LZ 第三方盘点帖（称 Camelz 3,333 份价格 TBA；Frost Hood 2,500 份免费 mint、GTD 刚开）。includes 无官号资料，未做额外 X 重读，未送审。
- @zayrotrade：R2216 已筛掉（GIWA 测试网永续、粉偏热、无官帖），本轮仍无原创帖、无新证据，不重审。
- WorldsEndFarm：Starknet「Bramble」关键词误伤（农场清杂草），跳过。
- 其余 KW/mentions 多为已在库项目转载（PlunderPort、LawoftheAbyss、Riftide、MMIX、Spike 等）、KOL 互动或无站点无官帖的噪声。MUST_WIN 25 条均为已在库官号（2hourfun 10、fueltenderagent 10、GunsOfTheHood 2、另见 ShieldedWizBTC / AgentCardsHQ / antopia_xyz），只做状态刷新。MUST_OFF 0 帖。

## 关键刷新 — 库内无改期、无首次 ≤2h（不重推）

- 2hour.fun @2hourfun：第一场窗口仍关闭。RSC payload `open=false`；首页 SSR 仍可能显示 Window open 占位，不以该标签为准。下一窗仍为 2026-11-27 05:00–07:00 CST（约 20.2h，未到 ≤2h）。平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 14.3%（R2216 约 14.4%），约 $5.1k mcap，已筹约 15.97 SOL / 约 $1132，最后成交约 08:37:49 CST。关窗、第二窗时间与发币费改免费此前已通知，本轮只是进度，不重推。
- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=113/3333（R2216 为 106），reserved=5（R2216 为 6），mintOpen=true，price=0。公售页 https://brimhollow.app/mint 。R2210 已通知，本轮只是进度。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop mintStatus=MINTING，90/10000（与 R2216 持平），持有 13，地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d。R2210 已通知，只是进度。不是免费 mint。
- Ugly Puggies：仍 MINTING，311/777（R2216 为 310），持有 238，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST（约 4.7h，未到首次 ≤2h；该阶段结束后仍是 SIGNED_PRESALE #3，公售 2026-11-27 13:30 CST）。不提前告警。
- deMiners：仍 MINTING，1364/3333（持平），持有 180，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（与 R2216 持平），现价约 0.00216 BNB。只是进度。
- TRIFORGE：链上 Forge Keys 788/3333（R2216 为 782），claims 33（R2216 为 32）。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上 450/10000（R2216 为 446），mintOpen=True。只是进度。
- Antopia：链上仍 6253/8888，saleOpen=True，免费额度仍满。
- VALORIX：链上 Hero Cards 仍 15，fillSold=0/5500。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」。本轮 MUST 未见 @Agx_bsc，未做额外 X 重读。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 35.7h，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：官网仍 Early List。SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍自 2026-11-27 01:00 CST 起，距首窗约 16.2h，未到首次 ≤2h。同名合集 vicehood（非该官号，本轮仍 209/3333 已在铸）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 12.7h，未到首次 ≤2h，不提前告警。
- Bons Genesis @bons_world：官网仍存活。OpenSea bons-genesis 仍 119/1111、持有 59、地板 0.4 USDG，SeaDrop 仍 MINTING，active PUBLIC_SALE 至 2026-12-22 01:00 CST。原免费 WL 窗已过，公售仍开；旧 le2h 文案已过期。不是免费 mint LIVE，不重推。
- CITYHOOD @appcityhood / cityhood.fun：官网仍 Minted 0/4,333，并残留已过期「Public mint opens today」。原 2026-11-23 窗口已过，无改期、无新开铸确认。勿与 @CityHood_NFT 合并。
- CITYHOOD @CityHood_NFT / cityhood.online：后端 /api/config 仍 chainId=46630 Robinhood Chain Testnet。市民登记仍开，主网铸造未确认，不是免费 mint LIVE。勿沿用过期「今晚 22:00」文案。
- ClankTube / OTC Rings / Famulus：R2216 新卡，本轮站点仍存活，状态未变（ClankTube 免费早期登记仍开、未见开铸），不重推。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

notify=true。

- 原因：本轮新收录 1 项 FOMO4NFT（Robinhood 链发射台/社交 NFT 交易已 live，非免费 mint）。库内 2hour / Wizards / Guns / Vicehood / Wildlife / Ugly Puggies / Bonebloom / Bons / CityHood 等无改期、无首次 ≤2h，不按进度重推。R2216 新卡无状态变化，不重推。
- alertMessage：FOMO4NFT（@FOMO4NFT）在 Robinhood 链的社交 NFT 发射台已上线，非免费 mint，详见面板 https://reboot7454.github.io/early-scout/ ，本号不自动 mint。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=['fomo4nft']，le2h=[]。
- dsFallback=false。
- discordPeekDeferred=true：X 路径未打开 Discord/浏览器，只写占位，须父进程同一轮补 Peek。不要假装已 Peek。登录墙与此前轮次相同，不要重发登录表单，除非已有新会话。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 data.json + docs/data.json + RESULT_R2217.md 到 Reboot7454/early-scout main。
- 下轮：UF 从 cursor 397 @CarlettaRineb 继续；mentionsNext=DogeEVM / BTC / Starknet / pads+squeek+STARX；静号=Elysium。
