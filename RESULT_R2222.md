# 早期打新雷达 R2222 RESULT

工作目录 /tmp/r2222/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_BTC）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 11:05 CST。写盘 lastScout=2026-11-26 11:20:50 CST。这是重置后的第七轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=844。首搜 UF1 之后今日剩余 843（脚注 remainingMinute=29 / remainingToday=843，todayReset=2026-11-27T00:00:00.000Z），确认 ample，继续主计划 + 条件瘦栏 24h。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 25 + silent 1 = 26，低于 softCap，已达 minSpend。未翻页（MUST_WIN / GIWA / MINT / PAD / GO / MEN_BTC / 多组 24h 触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=26（main=25，silent=1），remainingBefore=844，remainingAfter=818。额度 delta=26；已保存检索 25 次，另有 1 次未入文件的额外读发生在 MEN_STARK（remainingToday=825）与 MEN_PADS（823）之间，RESULT 按 delta 记 26。
- 写盘 meta.xBudgetMode=ample。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 2/843，UF2 0/842，MUST_WIN 25/841（触顶有 next_token，未翻页），MUST_OFF 0/840，
KW_LZ 1/839，KW_TAPE 19/838，KW_GIWA 25/837（触顶），KW_DOGE 0/836，KW_BTC 3/835，KW_STARK 2/834，
KW_MINT 25/833（触顶），KW_MINE 2/832，KW_PAD 25/831（触顶），KW_GO 25/830（触顶），KW_ELY 8/829，KW_GAPS 12/828，
MEN_DOGE 3/827，MEN_BTC 25/826（触顶），MEN_STARK 2/825，MEN_PADS 19/823（中间剩余 824 对应 1 次未入文件的额外读），
SILENT_BTC 14/822，
KW_LZ_24 23/821，KW_DOGE_24 25/820（触顶），KW_BTC_24 25/819（触顶），KW_STARK_24 25/818（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 1、TAPE 19、GIWA 25 触顶、DOGE 0、BTC 3、STARK 2、MINT 25 触顶、MINE 2、PAD 25 触顶、GO 25 触顶、ELY 8、GAPS 12。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 597 @agentic_pixels_ → 写盘后 cursor 647 @sablexisv1，wrap=false，分片末端 @onbeatfun。预跳已知 NF 13 个（@agentcityuk @MonsterRH_ @Derpagent_ @Proxisfun @ramencoinmeme @letswinhood @agentharvest_ai @seatworkcells @NidavellirBSC @frogsagent @Honestcoin60 @DropMinters @onbeatfun），from: 实际 37 个（UF1 24 + UF2 13）。UF1 result_count=2（仅已入库 @DayZeroDrop 互动，无新 mint），UF2 result_count=0。UF 总账户写盘后 2443（含本轮新挂的 @holdpadonray 与 @CrawlersAgent）。
- mentions 本轮轮换：DogeEVM / BTC / Starknet / pads+squeek+STARX（均为 24h；MEN_DOGE 3、MEN_BTC 25、MEN_STARK 2、MEN_PADS 19）。下轮：GIWA / Tape / LayerZero / Elysium。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=1→24h=23）、KW_DOGE_24（30m=0→24h=25）、KW_BTC_24（30m=3→24h=25）、KW_STARK_24（30m=2→24h=25）。TAPE 19、GIWA 25 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO）改成 24h。
- 静号：SILENT_BTC，search_users 不可用，24h has:mentions 回退。ran=true，result_count=14，未见需新收的静号作者，sentToReview=0，admitted=0。未做 getUsers 第二读。下轮静号指向 Starknet。

## 新收录

### HOLD @holdpadonray（id=holdpadonray）

- 类别 台子/Meme，chain=Solana，focus=false，不是免费 mint/登记。
- 建号 2026-11-26 10:06:09 CST（约 0.04 天），2 粉 / 7 帖 / 0 关注，xUserId 2125772510461366272。
- 官帖 2026-11-26 10:59:31 CST（https://x.com/holdpadonray/status/2125786502219309137）宣布 $HOLD is live，CA LT1TjrEtDiLGDFuRNMbLodpPr2KW2Aij41vhBmxJM3t，并链接 https://launchonhold.xyz。
- 官网 HTTPS 200，标题 HOLD · Hold longer. Get paid. 自称 Solana / Raydium LaunchLab 发射台，手续费按持仓时长加权分给持有人。config.js 中 CA 与官帖一致；X_URL 为空（siteXMutual=partial）。分成 draft；VAULT.live=false。本轮 Dexscreener 无 pairs、Jupiter token/price 404，CA 尚未在这些 API 独立核到已开盘。
- DeepSeek admit + score overall=68（early=95，actionable=58，novelty=62，risk=26）。已挂 userFollowWatch + agentPadWatch。
- 勿与库内 @theholdpad / https://theholdpad.fun/（R2028，Solana/Meteora 买墙发射台）合并。

### Crawlers Agent @CrawlersAgent（id=crawlers-agent）

- 类别 BN Agent 钱包，chain=BNB Chain，focus=false，付费 mint，不是面向全员的免费 mint（仅宣称 20 个 TRINE 亏损钱包免费份额）。
- 建号 2026-02-05（约 293 天），87 粉 / 仅 3 帖 / 23 关注，xUserId 2019514308166840321，资料栏无官网。
- 本轮首次官宣 2026-11-26 10:42:27 CST（https://x.com/CrawlersAgent/status/2125782203670135245）宣布今晚 20:00 CST 开铸：6,000 份，每份 0.004 BNB，每钱包最多 10，仅限 Agent ID。
- 临时站点 https://crawlers-agent.pages.dev HTTPS 200，状态 MINT · OPENING SOON；Agent ID 注册表 0x60B9262456dE011F7d15a54CdD8c48bAaa8B022F；页面写 CA 合约尚未部署。siteXMutual=none。距 20:00 CST 开铸写盘时仍约 8.7h，不是首次 ≤2h，不提前告警。
- 高风险：老号长期沉默、pages.dev 临时站、合约未部署。DeepSeek admit + score overall=55（early=58，actionable=52，novelty=50，risk=30）。已挂 userFollowWatch + agentPadWatch + bnAgentWatch。
- 勿与库内 clawlers / @Clawlers_（R986）合并。

## 看见但未收

- OTCRings @otcrings：已在库，官帖/站点自称 live 是进度，不重收、不重推。
- MythicMint_NFT Sherwood panda giveaway：非本轮官宣可操作窗口，不收录。
- Spike__wtf / Lamoryant / Riftide / GAMA（gama-giwa / gamapad）：已在库，未见新的改期或新开铸，不重收。
- ChainDNAapp 仅询问在哪发射；theinscriboors / SocialGruff 仅被提及、本轮无自有官帖；VardoBot 无帖；GetCorbel 评论；TapeOut_X 黑客松投票；Carcosa ERP 噪声；DayZeroDrop 仅 UF 互动。均不新建卡。
- 未把 @theholdpad 或 @Clawlers_ 与本轮新号合并。

## 库内刷新（只是进度，不重推）

- 2hour.fun：窗口仍关（RSC payload open=false；首页 SSR 仍可能显示 Window open 占位，不以该标签为准）。下一窗仍 2026-11-27 05:00–07:00 CST（约 17.7h，未到 ≤2h）。平台币进度约 16.9%，约 $5.7k mcap，已筹约 18.94 SOL / $1346（R2221 约 18.2% / $6.0k / 20.37 SOL），最后成交约 2026-11-26 11:03:43 CST。MUST 再见到关窗+免费发射+第二窗明天 21:00 UTC 的说明，与已记录时间一致，不按改期重推。
- Shielded Wizards：免费公售仍 LIVE，125/3333（R2221 为 118），reserved=5（R2221 为 7），mintOpen=true，price=0。R2210 已通知，不重推。
- Ugly Puggies：仍 MINTING，312/777，持有 239，地板 0.000167 ETH。SIGNED_PRESALE #2 仍至 2026-11-26 13:30 CST。写盘时距结束约 2.15h，未到首次 ≤2h，不提前告警。10:02 CST「mint didn’t go as expected」官帖 R2220 已记录，OpenSea 阶段表未改，不按改期重推。下轮若在 11:30 CST 之后写盘，须按首次 ≤2h 通知。
- Guns Of The Hood：付费公售仍 LIVE，OpenSea API total_supply=100/10000（与 R2221 持平）。本轮 osstats 401，未改写持有/地板。不是免费 mint。R2210 已通知，不重推。
- deMiners：仍 MINTING，1373/3333（R2221 为 1373），持有 181，地板 0.000107 ETH。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG。
- Agent Cards：phase=open，fillSold=5000/5000，curveSold=533，sold=5533，现价约 0.00216 BNB，与 R2221 持平。
- TRIFORGE：链上 Forge Keys 837/3333（R2221 为 822），claims 39（R2221 为 38），未暂停。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：mintOpen=true，462/10000，与 R2221 持平。
- Antopia：6336/8888（R2221 为 6315），saleOpen=true，免费额度仍满（4000/4000）。付费窗仍至 2026-11-27 20:45 CST，Clash 仍 21:00 CST，未到 ≤2h，不是改期，不重推。
- VALORIX：Hero Cards 16，fillSold=0/5500，与 R2221 持平。
- AGX：官网仍「官网维护中，即将回来 / Under maintenance. Back soon.」。
- Vicehood official vchood / Wildlife（tiger-universe 首窗仍 2026-11-26 21:30 CST，约 10h）/ Bonebloom（首窗仍 2026-11-27 20:30 CST）/ Slime：阶段表时间与上轮一致，未到首次 ≤2h，不提前告警。
- Bons Genesis / CityHood / ClankTube / OTC Rings / FOMO4NFT / Heliring / Edict / PrivMine：本轮未再打开这些页面（或仅 MUST 未见新窗口），只刷 lastChecked，不重推、不把未核到的站点写成新的 200。

## Watch / 漏挂

- 新卡入库同时挂 Watch，无「只建卡不盯」。WATCH_LEAK_RECENT=0。
- 普通新收录 focus=false（非 squeek 类）。

## Discord

- 本路未做 computerUse / Discord Peek。loginOk=false（沿用近几轮登录墙，不要重发登录表单，除非已有新会话）。discordPeekDeferred=true。父代理必须同一轮补 Peek；若补扫出现免费 mint/登记须再通知。lastSeen 未改。

## notify

- notify=true。新收录 HOLD 与 Crawlers Agent，均非面向全员的免费 mint/登记，须在本聊天点名提醒。
- Ugly Puggies 未到首次 ≤2h。Crawlers 开铸 20:00 CST 也未到 ≤2h。
- 无推送失败项需在写盘时重报。
- alert：新增收录 HOLD（@holdpadonray，Solana Raydium LaunchLab，官帖称已 live 并给 CA，Dexscreener/Jupiter 暂未核到交易对）与 Crawlers Agent（@CrawlersAgent，今晚 20:00 CST 付费开铸 0.004 BNB、6000 份、仅 Agent ID，合约未部署）。本轮无面向全员的免费 mint/登记；本号不自动 mint。面板：https://reboot7454.github.io/early-scout/

## 下轮指针

- UF cursor=647 @sablexisv1（wrap=false）。
- mentionsNext：GIWA / Tape / LayerZero / Elysium。
- silentNext：Starknet。
- Ugly Puggies 首次 ≤2h 约从 2026-11-26 11:30 CST 起（#2 至 13:30 CST）。
- Crawlers Agent 开铸 2026-11-26 20:00 CST（首次 ≤2h 约 18:00 CST）。
- Wildlife 首窗 2026-11-26 21:30 CST；Antopia 付费窗至 2026-11-27 20:45 CST；2hour 第二窗 2026-11-27 05:00 CST。
