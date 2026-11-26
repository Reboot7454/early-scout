# 早期打新雷达 R2223 RESULT

工作目录 /tmp/r2223/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_STARK）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。dsFallback=false。

开跑约 2026-11-26 11:28 CST。写盘 lastScout=2026-11-26 11:47:09 CST。这是重置后的第八轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=818（首搜 UF1 脚注 remainingToday=817，+1 回溯）。todayReset=2026-11-27T00:00:00.000Z。确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 22 + silent 1 = 23，低于 softCap，已达 minSpend。未翻页（MUST_WIN / MINT / PAD / GO / MEN_GIWA / KW_STARK_24 等触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=23（main=22，silent=1），remainingBefore=818，remainingAfter=795。额度 delta=23，与检索次数一致。
- 写盘 meta.xBudgetMode=ample。

各次检索（id / result_count；error=None；多数 remainingToday 仅能从首尾脚注回溯，不逐条捏造中间剩余）：
UF1 0，UF2 0，MUST_WIN 25（触顶未翻页），MUST_OFF 0，
KW_LZ 0，KW_TAPE 23，KW_GIWA 23，KW_DOGE 6，KW_BTC 6，KW_STARK 0，
KW_MINT 25（触顶），KW_MINE 1，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 5，KW_GAPS 15，
MEN_GIWA 25（触顶未翻页），MEN_TAPE 6，MEN_LZ24 23，MEN_ELY 20，
SILENT_STARK 0，
KW_LZ_24 23，KW_STARK_24 25（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 23、GIWA 23、DOGE 6、BTC 6、STARK 0、MINT 25 触顶、MINE 1、PAD 25 触顶、GO 25 触顶、ELY 5、GAPS 15。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 647 @sablexisv1 → 写盘后 cursor 697 @Trexionbsc，wrap=false，分片末端 @cadencebnb。预跳已知 NF 8 个（@lettucegrow_rh @beatdotfamily @nonamespnft @heyribbid @inkwellonbnb @certuna_rh @miuadotfun @origopad），from: 实际 42 个。UF1 result_count=0，UF2 result_count=0。UF 总账户写盘后 2447（含本轮新挂的 @taxmandotrun @flintlaunchfun @LongyuNetwork @zayrotrade）。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（均为 24h；MEN_GIWA=25 触顶未翻页，MEN_TAPE=6，MEN_LZ24=23，MEN_ELY=20）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_STARK_24（30m=0→24h=25）。TAPE 23、GIWA 23、DOGE 6、BTC 6 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO）改成 24h。
- 静号：SILENT_STARK，search_users 不可用，24h has:mentions 回退。ran=true，result_count=0，未见需新收的静号作者，sentToReview=0，admitted=0。未做 getUsers 第二读。下轮静号指向 LayerZero。

## 新收录

### TAXMAN @taxmandotrun（id=taxmandotrun）

- 类别 台子/Meme，chain=Solana，focus=false，不是免费 mint/登记。
- 建号 2026-11-26 07:00:34 CST（约 0.19 天），25 粉 / 25 帖，xUserId 2125726061333983232。
- 官帖 2026-11-26 11:30:03 CST（https://x.com/taxmandotrun/status/2125794185748045895）讨论把股票代币装入 TAXMAN 基金。官网 https://taxman.run HTTPS 200，与官推互链（siteXMutual=yes）。
- CA BAijHvUiHCoCxApyYAUnz5g6LnizZXVYoHwdMarqTWtw。Raydium LaunchLab 09:19:11 CST 毕业，firstPool 07:36:32 CST。Dexscreener Raydium CPMM 对 12P5P4h3KuhcT5Wze3PpxVuJhWxjaZLc8HwXcdMq2P9U，价格约 $0.00002527，mcap/fdv 约 $25.3k，流动性约 $13.7k，约 6h 成交约 $98.2k。Jupiter mcap 约 $17.0k，流动性约 $6.9k，持有人 223，mint/freeze 已关，organicScore 约 50.8 medium，6 位小数、供应 10 亿。市值/流动性都很小，rug 与波动风险高。
- DeepSeek admit + score overall=74（early=95，actionable=78，novelty=65，risk=88）。已挂 userFollowWatch + agentPadWatch。

### Flint @flintlaunchfun（id=flintlaunchfun）

- 类别 台子/Meme，chain=Solana，focus=false，不是免费 mint/登记。
- 建号 2026-11-20 18:06:43 CST（约 5.73 天），0 粉 / 3 帖，xUserId 2123719414486884352。
- 官帖 2026-11-26 11:29:15 CST（https://x.com/flintlaunchfun/status/2125793984500891693）自称以 PUMP 为报价的 Solana 发射台。官网 https://flintlaunch.fun HTTPS 200，标题 FLINT；可在主网创建 Pump.fun 币，只收 SOL 网络费、无初始买入。站点仍用 x.com/your-project 占位，siteXMutual=none。第三方前端同质化强，暂无自身代币/空投抓手。
- DeepSeek 默认筛卡曾因「第三方前端、0 粉」倾向跳过；十栏补审按极早期发射台收录。score overall=48（early=86，actionable=45，novelty=38，risk=86）。已挂 userFollowWatch + agentPadWatch。

### Longyu Network @LongyuNetwork（id=longyu-network）

- 类别 挖矿，chain=BNB，focus=false（不是仓鼠/toychain），不是免费 mint/登记。
- 建号 2026-11-21 14:12:59 CST（约 4.89 天），4071 粉 / 仅 5 帖，xUserId 2124022886587678720。本轮无自有官帖，由 KW_MINE 命中。
- 官网 https://longyu.network HTTPS 200，与官推互链（siteXMutual=yes）。自称 BNB 上可挖矿 L2 主网 LIVE，250ms，gas 为 BNB，chainId 668800；RPC https://rpc.longyu.network，浏览器 https://explorer.longyu.network，挖矿 https://mine.longyu.network HTTPS 200。官方 LONG 0xc6D2B2483EC93C15109FCe43d21Ac05919031655，挖出的 LONG 锁至 TGE。5 帖/4071 粉异常，风险高。
- DeepSeek admit + score overall=62（early=90，actionable=72，novelty=56，risk=87）。已挂 userFollowWatch + miningWatch。

### Zayro @zayrotrade（id=zayrotrade）

- 类别 GIWA，chain=GIWA，focus=false，不是免费 mint/登记。仅测试网，非主网。
- 建号 2026-11-18 17:30:12 CST（约 7.75 天），974 粉 / 21 帖，xUserId 2122985020222480384。本轮无自有官帖，由 MEN_GIWA 第三方生态盘点命中。
- 官网 https://zayro.trade HTTPS 200，meta 写 Testnet live on GIWA，twitter:site=@zayrotrade，siteXMutual=partial。自称最高 1000x，对手盘中间价，无订单簿/点差/资金费。代币/空投路径不明确。
- DeepSeek admit + score overall=57（early=78，actionable=55，novelty=62，risk=76）。已挂 userFollowWatch + giwaWatch。

## 首次 ≤2h / 库内刷新（不另作改期）

- **Ugly Puggies @uglypuggies**：仍 MINTING，313/777（R2222 为 312），持有 240（R2222 为 239），地板 0.000167 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30:00 CST。写盘时距结束约 1.7h，**已进入该窗结束的首次 ≤2h，按规则 notify=true**。R2220 官帖承认 mint 不及预期，OpenSea 阶段表仍未改，不按改期重推。随后 stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 2026-11-27 13:30 CST。本号不自动 mint。
- Shielded Wizards：免费公售仍 LIVE，138/3333（R2222 为 125），reserved=4（R2222 为 5），mintOpen=true，price=0。R2210 已通知，只是进度，不重推。
- Antopia：链上 6342/8888（R2222 为 6336），saleOpen=true，免费额度仍满 4000/4000。付费窗仍至 2026-11-27 20:45 CST，未到 ≤2h，不重推。
- TRIFORGE：Forge Keys 840/3333（R2222 为 837），claims 40（R2222 为 39），预售仍开至 2026-12-02 10:01:25 CST，挖矿仍开，只是进度。
- F0B90B：仍 mintOpen=true，462/10000，与 R2222 持平。
- VALORIX：Hero Cards 16、fillSold=0/5500，与 R2222 持平。
- Agent Cards：phase=open，fillSold=5000，curveSold=563，sold=5563/1,007,493（R2222 为 5533 / 533），现价约 0.00216 BNB。只是进度，不重推。
- Guns Of The Hood：仍 MINTING，100/10000，持有 14，付费公售仍 LIVE，不重推。
- The Jacket：仍 214/777，持有 136，地板 0.61 USDG，与上轮持平。
- deMiners：仍 1373/3333，持有 181，地板约 0.000107 ETH，公售仍至 2026-11-28 00:30 CST。
- 2hour.fun：第一场窗口仍按已关闭处理（本轮 HTML 未重解析到 RSC open 字段）。下一窗仍为 2026-11-27 05:00–07:00 CST，未到 ≤2h。平台币曲线进度本轮未重拉。不重推。
- Wildlife / tiger-universe：仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起，未到首次 ≤2h。
- Vicehood / vchood：仍 MINTING_SOON 0/3333，首窗仍 2026-11-27 01:00 CST，未到首次 ≤2h。
- Bonebloom：仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，未到首次 ≤2h。
- Crawlers Agent：开铸仍预告 2026-11-26 20:00 CST，未到首次 ≤2h（约 18:00 CST 起算），不提前告警。
- HOLD @holdpadonray：未见新开铸/改期，不重推。

看见但未收（节选）：Oathlydotai（安全 SaaS）、Sidoorxyz（非早期）、已在库 Frenzz/freakapes/Owltopia/GetTroopers/Lamoryant 等；ugly puggies 10:02 CST「mint 不及预期」官帖已在 R2220 记录。

## Watch / 漏挂

- 新卡均同时进 Watch（见上）。近期（round≥2100）Watch 漏挂检查 0，无需补挂。
- 软债 lastChecked 已刷新（含 canton/glaze/tokenWorks 与各必盯 Watch）。

## notify

- notify=true。原因：四项真新收录 + Ugly Puggies SIGNED_PRESALE #2 结束窗首次 ≤2h。
- 本轮没有面向全员的免费 mint / 免费登记新收录，告警里已写明。
- namedPaidLe2h=['ugly-puggies']。namedFreeMintOrRegistration=[]。
- 面板 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。

## Discord

discordPeekDeferred=true。X 路径未打开 Discord/浏览器，只写占位。登录墙与 R2206/R2222 相同（Welcome back / Email/Password / Log In / QR / passkey），loginOk=false，四频道 lastSeen/cutoff 仍停在 2026-11-23 22:19–22:56 CST。用户此前已被告知用已有表单再登。同一未登录会话无法翻过登录墙，本轮不重复开浏览器、不重发登录表单。须父代理在同一轮补 Peek；补扫若出现免费 mint/登记再通知。
