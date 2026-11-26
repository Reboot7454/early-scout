# 早期打新雷达 R2218 RESULT

工作目录 /tmp/r2218/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_ELY）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 09:00 CST。写盘 lastScout=2026-11-26 09:16:06 CST。这是重置后的第三轮常规增量，不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。关键站点/API/链上核验约 09:05–09:10 CST。

## 额度与模式

- 开火前 remainingBefore=941。首搜 UF1 之后今日剩余 940（脚注 remainingMinute=29 / remainingToday=940，todayReset=2026-11-27T00:00:00.000Z），确认 ample，继续主计划 21 次 + 条件瘦栏 24h 3 次。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 23 + silent 1 = 24，低于 softCap，已达 minSpend。未翻页（多组触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=24（main=23，silent=1），remainingBefore=941，remainingAfter=917。
- 写盘 meta.xBudgetMode=ample。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 4/940，UF2 1/939，MUST_WIN 25/938（触顶有 next_token，未翻页），MUST_OFF 0/937，
KW_LZ 1/936，KW_TAPE 25/935（触顶），KW_GIWA 7/934，KW_DOGE 7/933，KW_BTC 4/932，KW_STARK 0/931，
KW_MINT 25/930（触顶），KW_MINE 0/929，KW_PAD 25/928（触顶），KW_GO 25/927（触顶），KW_ELY 21/926，KW_GAPS 7/925，
MEN_DOGE 3/924，MEN_BTC 25/923（触顶），MEN_STARK 3/922，MEN_PADS 25/921（触顶），
SILENT_ELY 25/920（触顶），
KW_LZ_24 23/919，KW_BTC_24 25/918（触顶），KW_STARK_24 25/917（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 1、TAPE 25 触顶、GIWA 7、DOGE 7、BTC 4、STARK 0、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 21、GAPS 7。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完。cursor 397 @CarlettaRineb 起 50 号至 @SigilsGuru；写盘后 cursor 447 @ElysiumDegens，wrap=false。预跳已知 NF 19 个（用户点名但长期 NF 的 @starx_xlayer 本分片未做 getUsers 重读，仅可出现在 mentions 查询里），故 from: 实际 31 个（UF1 25 + UF2 6）。UF1 result_count=4（均为已在库 @onlydotmeme 客服回复），UF2 1 帖（已在库 @zaplonl Catalogue note：1,103 Passes issued / 260 settled / 843 unclaimed）。写盘后 UF 总账户 2439（本轮新挂 1 个 @heliring_app）。
- 瘦栏 24h：仅对 30m 命中 <5 的栏各补 1 次。已补 LZ（30m=1→23）、BTC（30m=4→25 触顶）、Starknet（30m=0→25 触顶）。跳过 Tape（30m=25）、GIWA（30m=7）、DogeEVM（30m=7），原因 30m>=5。未把肥栏改成 24h。thin24hDeferred=false。
- mentions 覆盖: DogeEVM 3 / BTC 25 触顶 / Starknet 3 / pads+squeek+STARX 25 触顶（均为 24h 轮换）。下轮：GIWA / Tape / LayerZero / Elysium。mentionsDeferred=false。
- silent: Elysium（search_users 不可用，24h has:mentions 回退；result_count=25 触顶，seen=19 未知作者，sentToReview=0，admitted=0，ran=true）。看见 @playdunkem 介绍 FrenGame（站点 https://frengame.xyz 本轮 HTTPS 200），但账号 2023-11-27 建立、946 粉，非极早期，未送审、未额外重读。下轮：Tape/电路。silentDeferred=false。

## 新收录

- Heliring（@heliring_app / https://heliring.app/）→ 栏「台子/Meme」。2026-11-26 08:31:55 CST 建号（约 0.02 天），0 粉 / 1 帖，xUserId 2125749225136746496。官帖 08:52:40 CST（https://x.com/heliring_app/status/2125754578540879884）宣布 Heliring is live：用 Helius Privacy Rings 的加密 ring 余额和一次性新钱包在 pump.fun 发币与首买。官网 HTTPS 200，标题 Heliring · private pump.fun trading，页面有 Launch / Explore / Connect wallet，展示 CA 4GyoxBumvdsYoTMZTbQsu4z5ZsdtQX1YCtq7GjBApump（本轮未做持有与流动性复核）。官网 HTML 未核到回链官推（siteXMutual=none）。不是免费 mint。DS overall=64，admit=true。已进 UF + agentPadWatch。focus=false。

newThisRound=['heliring']。

## 看见但未收

- TRIPWIRE（@tripwireorders / https://settripwire.fun）：建号约 0.25 天、44 粉 / 32 帖。官网 HTTP 200，站点回链 @tripwireorders，bio 含 CA Cqojv7y5HokxxjRGcBLNMdMgerVyQyu2SMbGoAbiWire。产品是 Solana 上的事件触发条件单，不是 mint/发射台。DS admit=false。
- Closari（@closari_rh / https://closari.net/）：建号约 2.71 天、12 粉 / 28 帖。自称 Coming to Robinhood Chain 的股票收盘市场，官网描述为 paper position / 开发中，不是已确认免费 mint 或已开铸 LIVE。DS admit=false。
- antwork（@antworkdotfun / https://antwork.fun）：建号约 0.42 天、169 粉 / 87 帖。官网 HTTP 200，twitter:site=@antworkdotfun，页面仍 setting up the Hill。本轮仅 mentions 命中、无第一手官帖（未额外重读），相对建号时长偏热。DS admit=false。
- @playdunkem / FrenGame（https://frengame.xyz）：SILENT_ELY 见到「Mint a pixel pet… Fully on-chain on @Enter_Elysium」。站点 HTTPS 200，但账号 2023 年建立、946 粉，非极早期，未送审。
- @Oathlydotai：建号约 0.49 天，无官网、本轮 0 帖，defer，不送审。
- WorldsEndFarm：Starknet「Bramble」关键词误伤（农场清杂草），跳过。
- 其余 KW/mentions 多为已在库项目转载、KOL 互动或无站点无官帖的噪声。MUST_WIN 25 条均为已在库官号（fueltenderagent 10、2hourfun 8、ShieldedWizBTC 3、GunsOfTheHood 2、antopia_xyz 1、AgentCardsHQ 1），只做状态刷新。MUST_OFF 0 帖。

## 关键刷新 — 库内无改期、无首次 ≤2h（不重推）

- 2hour.fun @2hourfun：第一场窗口仍关闭。RSC payload `open=false`；首页 SSR 仍可能显示 Window open 占位，不以该标签为准。下一窗仍为 2026-11-27 05:00–07:00 CST（约 19.7h，未到 ≤2h）。平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 14.3%（与 R2217 持平），约 $5.1k mcap，已筹约 15.97 SOL / 约 $1132，最后成交约 08:37:49 CST。关窗、第二窗时间与发币费改免费此前已通知，本轮只是进度，不重推。
- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=114/3333（R2217 为 113），reserved=6（R2217 为 5），mintOpen=true，price=0。公售页 https://brimhollow.app/mint 。官帖仍称 public mint is still open，并预告明日加 staking / Voting tab。R2210 已通知，本轮只是进度。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop mintStatus=MINTING，90/10000（与 R2217 持平），持有 13，地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d。R2210 已通知，只是进度。不是免费 mint。
- Ugly Puggies：仍 MINTING，311/777（与 R2217 持平），持有 238，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST（约 4.2h，未到首次 ≤2h；该阶段结束后仍是 SIGNED_PRESALE #3，公售 2026-11-27 13:30 CST）。不提前告警。
- deMiners：仍 MINTING，1364/3333（持平），持有 180，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（与 R2217 持平），现价约 0.00216 BNB。只是进度。
- TRIFORGE：链上 Forge Keys 797/3333（R2217 为 788），claims 34（R2217 为 33）。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上仍 450/10000，mintOpen=True。只是进度。
- Antopia：链上仍 6253/8888，saleOpen=True，免费额度仍满。本轮 MUST 官帖称付费窗至 2026-11-27 12:45 UTC（20:45 CST）关闭，Clash of Antopia 今日 13:00 UTC（21:00 CST）上线（gameAtCST 此前已记）。距关停约 35h，未到 ≤2h，不是改期，不重推。
- VALORIX：链上 Hero Cards 16（R2217 为 15），fillSold=0/5500。只是进度。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」。本轮 MUST 未见 @Agx_bsc，未做额外 X 重读。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 35.2h，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：官网仍 Early List。SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍自 2026-11-27 01:00 CST 起，距首窗约 15.7h，未到首次 ≤2h。同名合集 vicehood（非该官号，本轮仍 209/3333 已在铸）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起（官网 Launch 26 November 2026 · 7:00 PM IST，与该时间一致）。距首窗约 12.2h，未到首次 ≤2h，不提前告警。
- Bons Genesis @bons_world：官网仍存活。OpenSea bons-genesis 仍 119/1111，SeaDrop 仍 MINTING，active PUBLIC_SALE 至 2026-12-22 01:00 CST。原免费 WL 窗已过，公售仍开；旧 le2h 文案已过期。不是免费 mint LIVE，不重推。本轮 osstats 401，持有/地板未刷新，供应与阶段与上轮一致。
- CITYHOOD @appcityhood / cityhood.fun：官网仍 Minted 0/4,333，并残留已过期「Public mint opens today」。原 2026-11-23 窗口已过，无改期、无新开铸确认。勿与 @CityHood_NFT 合并。
- CITYHOOD @CityHood_NFT / cityhood.online：后端 /api/config 仍 chainId=46630 Robinhood Chain Testnet。市民登记仍开，主网铸造未确认，不是免费 mint LIVE。勿沿用过期「今晚 22:00」文案。
- ClankTube / OTC Rings / Famulus：R2216 新卡，本轮站点仍存活，状态未变（ClankTube 免费早期登记仍开、未见开铸），不重推。
- FOMO4NFT：R2217 新卡，官网与发射台仍 HTTP 200，OpenSea chain-society 仍 1111/1111 售完，非免费 mint，状态未变，不重推。
- zaplonl：UF2 官帖更新为 1,103 Passes issued、260 settled、843 unclaimed，已在库进度，不重推。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

notify=true。

- 原因：本轮新收录 1 项 Heliring（Helius Privacy Rings 上的隐私 pump.fun 发射台自称已 live，非免费 mint）。库内 2hour / Wizards / Guns / Vicehood / Wildlife / Ugly Puggies / Bonebloom / Bons / CityHood / FOMO4NFT / ClankTube 等无改期、无首次 ≤2h，不按进度重推。R2216 / R2217 新卡无状态变化，不重推。
- alertMessage：Heliring（@heliring_app）在 Helius Privacy Rings 上的隐私发射台自称已上线，非免费 mint，详见面板 https://reboot7454.github.io/early-scout/ ，本号不自动 mint。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=['heliring']，le2h=[]。
- dsFallback=false。
- discordPeekDeferred=true：X 路径未打开 Discord/浏览器，只写占位，须父进程同一轮补 Peek。不要假装已 Peek。登录墙与此前轮次相同，不要重发登录表单，除非已有新会话。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 data.json + docs/data.json + RESULT_R2218.md 到 Reboot7454/early-scout main。
- 下轮：UF 从 cursor 447 @ElysiumDegens 继续；mentionsNext=GIWA / Tape / LayerZero / Elysium；静号=Tape/电路。
