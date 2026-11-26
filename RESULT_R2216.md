# 早期打新雷达 R2216 RESULT

工作目录 /tmp/r2216/。本路完成 X 全量补扫（UF1–UF3 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 六薄栏 24h + 全链 mentions 24h + SILENT_STARK）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 08:05 CST。写盘 lastScout=2026-11-26 08:20:19 CST。这是 08:00 CST 后首轮全量补扫，lastFullAfterReset=R2216。时区 Asia/Shanghai (CST)。关键站点/API 核验约 08:07–08:15 CST。

## 额度与模式

- 开火前 remainingBefore=1000。首搜 UF1 之后今日剩余 999（脚注 remainingMinute=29 / remainingToday=999，todayReset=2026-11-27T00:00:00.000Z），确认 post-reset-full，继续全表 34 次。
- mode=post-reset-full，softCap=50，minSpend=24，silentCap=2。主扫 33 + silent 1 = 34，低于 softCap，已达 minSpend。未翻页（多组触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。
- xReads=34（main=33，silent=1），remainingBefore=1000，remainingAfter=966。
- 写盘 meta.xBudgetMode=post-reset-full。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 0/999，UF2 0/998，UF3 0/997，MUST_WIN 25/996（触顶有 next_token，未翻页），MUST_OFF 0/995，
KW_LZ 0/994，KW_TAPE 13/993，KW_GIWA 7/992，KW_DOGE 11/991，KW_BTC 2/990，KW_STARK 1/989，
KW_MINT 25/988（触顶），KW_MINE 0/987，KW_PAD 25/986（触顶），KW_GO 25/985（触顶），KW_ELY 6/984，KW_GAPS 6/983，
KW_LZ_24 23/982，KW_TAPE_24 25/981（触顶），KW_GIWA_24 25/980（触顶），KW_DOGE_24 25/979（触顶），KW_BTC_24 25/978（触顶），KW_STARK_24 25/977（触顶），
MEN_GIWA 25/976（触顶），MEN_TAPE 6/975，MEN_LZ24 25/974（触顶），MEN_DOGE 3/973，MEN_BTC 25/972（触顶），MEN_STARK 3/971，MEN_SQUEEK 0/970，MEN_STARX 0/969，MEN_ELY 20/968，MEN_PADS 21/967，
SILENT_STARK 0/966。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 13、GIWA 7、DOGE 11、BTC 2、STARK 1、MINT 25 触顶、MINE 0、PAD 25 触顶、GO 25 触顶、ELY 6、GAPS 6。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完。cursor 267 @auven_ai 起 80 号至 @DavidJohnsvcen；写盘后 cursor 347 @firstpadfun，wrap=false。预跳已知 NF 16 个（含用户点名但长期 NF 的 @starx_xlayer，未做 getUsers 重读），故 from: 实际 63 个（UF1–UF3）。@2hourfun 虽在本分片，已从 UF 30m 挪到 MUST_WIN 24h。UF1–UF3 均为 0 帖。写盘后 UF 总账户 2437（本轮新挂 3 个）。
- 瘦栏 24h 补搜: 是（重置后全量，6 组均跑）。LZ（30m=0→23）、Tape（30m=13→25 触顶）、GIWA（30m=7→25 触顶）、DogeEVM（30m=11→25 触顶）、BTC（30m=2→25 触顶）、Starknet（30m=1→25 触顶）。thin24hDeferred=false。
- mentions 覆盖: 全链 24h：GIWA 25 触顶 / Tape 6 / LZ 25 触顶 / Doge 3 / BTC 25 触顶 / Stark 3 / squeek 0 / STARX 0 / Elysium 20 / pads 21。下轮恢复轮换：GIWA / Tape / LayerZero / Elysium。mentionsDeferred=false。
- silent: Starknet（search_users 不可用，24h has:mentions 回退；result_count=0，seen=0，sentToReview=0，admitted=0，ran=true）。下轮：LayerZero。silentDeferred=false。

## 新收录

- OTC Rings（@OTCRings / https://otcrings.fun/）→ 栏「台子/Meme」。2026-11-26 05:40:30 CST 建号（约 0.1 天），16 粉 / 20 帖。官网 HTTP 200，/api/health mock=false，/api/config open=true、venue=pump.fun、hub=HouizpRQsad13qKJs4Fow1fDHjAwezqeis9CRNfVLmQw。发币费用约 0.0188+0.005 SOL。Desk 为付费 NFT（约 0.51206 SOL，另需燃烧 10 万枚平台币）。平台币 CA 31mAPrPsE4CQWP8akGNTRs6kwXuYiNkeMsr9hJ5Cpump（pump.fun，caLive=true）；/api/coins 列出 5 个币。官网 config.x 为空、无回链官推（siteXMutual=none）。本轮未见原创官帖（仅 includes + 转述 We are live）。config.privatePayouts 目前为 false。不是免费 mint。DS overall=74，admit=true。已进 UF + agentPadWatch。focus=false。
- ClankTube（@clanktube / https://clanktube.fun/）→ 栏「台子/Meme」。2026-11-12 22:18:17 CST 建号（约 13.4 天），10 粉 / 6 帖。官网 Early Access 页面称登记已开（关注+评论+赞转+验证帖+EVM 地址）。app.js 的 CONFIG.endpoint 已指向 Google Apps Script，不是空 endpoint 的纯 demo（页面仍残留 Demo 文案和模板注释；验证码前缀 AGNT- 与校验正则 CLANKTUBE- 不一致，实现有瑕疵）。本轮未见开登记官帖。免费早期登记看起来已开，不是已开铸 mint。DS overall=52，admit=true。已进 UF + freeMintWatch。focus=false。
- Famulus（@famulusai / https://famulusai.app/）→ 栏「台子/Meme」。2026-11-19 00:56:24 CST 建号（约 7.3 天），24 粉 / 15 帖。官帖 2026-11-25 16:15:11 CST（https://x.com/famulusai/status/2125624347977286020）称已 LIVE：Elysium 与 Hyperliquid 链上哨兵，Telegram 汇报，不签名不持钥。官网存活（小型 SPA），未回链官推。自称 Elysium 但未核到官方部署名单，不进 Elysium 栏。不是免费 mint，无开铸窗口。DS overall=61，admit=true。已进 UF。focus=false。

newThisRound=['otcrings','clanktube','famulusai']。

## 看见但未收

- zayro（@zayrotrade / https://zayro.trade/）：建号约 7.6 天、968 粉。官网称 GIWA 测试网合成永续已 live。本轮无原创官帖，仅生态盘点提及。DS overall=49，admit=false（测试网、无官帖、粉相对年龄偏热）。
- VardoBot（@VardoBot / https://test.vardo.gg/）：约 1.1 天、1 粉的机器人号，站点是 MegaETH 预测市场「private testing」。非正式项目官号，未送审。
- WorldsEndFarm：Starknet「Bramble」关键词误伤（农场清杂草），跳过。
- ShieldSuite / Voxro：工作室号约 227 天，Voxro 付费收件箱刚 live，不是极早期 mint/登记，未收。
- 其余 KW/mentions 多为已在库项目转载、KOL 互动或无站点无官帖的噪声。MUST_WIN 25 条均为已在库官号（2hourfun 11、另见 ShieldedWizBTC / 库内 leash 等），只做状态刷新。

## 关键刷新 — 库内无改期、无首次 ≤2h（不重推）

- 2hour.fun @2hourfun：第一场窗口仍关闭。RSC payload `open=false`；首页 SSR 仍可能显示 Window open 占位，不以该标签为准。下一窗仍为 2026-11-27 05:00–07:00 CST（约 21h，未到 ≤2h）。平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 14.4%（R2215 约 14.6%），约 $5.1k mcap，已筹约 16.13 SOL / 约 $1136，最后成交约 08:00:14 CST。关窗、第二窗时间与发币费改免费此前已通知，本轮只是进度，不重推。
- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=106/3333（R2215 为 91），reserved=6（上轮 3），mintOpen=true，price=0。公售页 https://brimhollow.app/mint 。R2210 已通知，本轮只是进度。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop mintStatus=MINTING，90/10000（与 R2215 持平），持有 13，地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d。R2210 已通知，只是进度。不是免费 mint。
- Ugly Puggies：仍 MINTING，310/777（持平），持有 237，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST（约 5h，未到首次 ≤2h）。
- deMiners：仍 MINTING，1364/3333（持平），持有 180，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（与 R2215 持平），现价约 0.00216 BNB。只是进度。
- TRIFORGE：链上 Forge Keys 782/3333（R2215 为 777），claims 32（持平）。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上 446/10000（R2215 为 433），mintOpen=True。只是进度。
- Antopia：链上仍 6253/8888，saleOpen=True，免费额度仍满。
- VALORIX：链上 Hero Cards 仍 15，fillSold=0/5500。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」。本轮 MUST 未见 @Agx_bsc，未做额外 X 重读。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 36h，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- BAD APE：OpenSea 供应仍为 0，未见开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：官网仍 Early List。SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍自 2026-11-27 01:00 CST 起，距首窗约 16.8h，未到首次 ≤2h。同名合集 vicehood（非该官号，本轮仍 209/3333 已在铸）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 13.3h，未到首次 ≤2h，不提前告警。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

notify=true。

- 原因：本轮新收录 3 项。其中 ClankTube 为免费早期登记（即便 score=52 也必须点名告警）。OTC Rings、Famulus 虽非免费 mint，但是真新收录。库内 2hour / Wizards / Guns / Vicehood / Wildlife 等无改期、无首次 ≤2h，不按进度重推。
- alertMessage：面板：https://reboot7454.github.io/early-scout/；本号不自动 mint：ClankTube 免费早期登记已开，另收录 OTC Rings（付费发射台/Desk，非免费 mint）和 Famulus（监控工具已 live，非免费 mint）。
- namedFreeMintOrRegistration=['ClankTube']，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=['otcrings','clanktube','famulusai']，le2h=[]。
- dsFallback=false。
- discordPeekDeferred=true：X 路径未打开 Discord/浏览器，只写占位，须父进程同一轮补 Peek。不要假装已 Peek。登录墙与此前轮次相同，不要重发登录表单，除非已有新会话。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 data.json + docs/data.json + RESULT_R2216.md 到 Reboot7454/early-scout main。
- 下轮：UF 从 cursor 347 @firstpadfun 继续；mentionsNext=GIWA / Tape / LayerZero / Elysium；静号=LayerZero。
