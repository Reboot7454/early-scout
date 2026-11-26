# 早期打新雷达 R2233 RESULT

工作目录 /tmp/r2233/。本路完成 X 常规增量（UF1–UF3 + MUST_WIN 24h 因查询过长拆成 MUST_WIN+MUST_WIN2 + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_BTC）、站点核验、写盘并推送面板。新收录 1 项：ROCKZERO / @rockzerodotlive（免费白名单申请已开，铸造未开始）。DeepSeek HTTP 401，admit/score/alert 走 dsFallback。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek；登录墙与此前相同，不要重发登录表单，除非已有新会话）。

开跑约 2026-11-26 16:26 CST。写盘 lastScout 以 data.json meta.lastScout 为准（2026-11-26 16:45:15 CST）。这是重置后的第十八轮常规增量（R2216 全量补扫之后），不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。

## 额度与模式

- 开火前 remainingBefore=562（首搜脚注 remainingToday=561，+1 回溯）。todayReset 约 2026-11-27 08:00 CST。remaining<600 会标 pace/softCap 18，但 remaining≫200，本轮仍跑完全量增量，未砍栏、未缩盲捞。
- mode=pace（未执行砍栏），softCap=18，minSpend=18，silentCap=2。独立查询 26（主扫 25 + silent 1），另因写盘失败补拉 5 次（MUST_WIN 额外 3、KW_GIWA 额外 2），合计 API 调用 31。未翻页。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读。
- xReads=31，remainingBefore=562，remainingAfter=531。额度 delta=31，与 API 调用次数一致。
- 写盘 meta.xBudgetMode=pace。

各次检索（id / result_count）：
UF1 0，UF2 2，UF3 0，MUST_WIN 25（触顶未翻页），MUST_WIN2 6，MUST_OFF 2，
KW_LZ 0，KW_TAPE 15，KW_GIWA 25（触顶），KW_DOGE 4，KW_BTC 15，KW_STARK 0，KW_MINT 25（触顶），KW_MINE 3，KW_PAD 25（触顶），KW_GO 25（触顶），KW_ELY 16，KW_GAPS 19，
MEN_GIWA 25（触顶），MEN_TAPE 6，MEN_LZ24 25（触顶），MEN_ELY 22，
SILENT_BTC 13，
KW_LZ_24 23，KW_DOGE_24 25（触顶），KW_STARK_24 25（触顶）。KW_BTC_24 / KW_TAPE_24 / KW_GIWA_24 因 30m≥5 跳过。

## 十栏 / UF / mentions / 静号 / 瘦栏 24h

- 十栏已跑全（30m）：LZ 0、TAPE 15、GIWA 25 触顶、DOGE 4、BTC 15、STARK 0、MINT 25 触顶、MINE 3、PAD 25 触顶、GO 25 触顶、ELY 16、GAPS 19。MUST_WIN 24h 25 触顶 + MUST_WIN2 6、MUST_OFF 30m 2。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完本轮 50 号分片：cursor 1147 @guppofish → 写盘后 cursor 1197 @BabyDoge_Agent_，wrap=false，分片末端 @PipAgentWorld。预跳已知 NF 0 个，from: 实际 50 个。UF1=0，UF2=2（@PairMineAI 产品说明，非新开盘），UF3=0。UF 总账户写盘后 2464（+@rockzerodotlive）。
- mentions 本轮轮换：GIWA / Tape / LayerZero / Elysium（MEN_GIWA=25，MEN_TAPE=6，MEN_LZ24=25，MEN_ELY=22）。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 瘦栏 24h：因 30m 命中 <5，追加 KW_LZ_24（30m=0→24h=23）、KW_DOGE_24（30m=4→24h=25）、KW_STARK_24（30m=0→24h=25）。TAPE 15、GIWA 25、BTC 15 均 ≥5，跳过对应 24h。未把肥栏（MINT/PAD/GO/ELY/MINE）改成 24h。
- 静号：SILENT_BTC，search_users 不可用，24h has:mentions 回退，命中 13。下轮静号：Starknet。

## 新收录

- **ROCKZERO（@rockzerodotlive / https://rockzero.live/）**：建号 2026-11-08 11:20:37 CST（约 18.2 天），32 粉 / 1 帖，未认证，xUserId 2119268636166918145，资料栏无 URL。官帖 2026-11-26 15:50:50 CST（https://x.com/rockzerodotlive/status/2125859812122697866）宣布 Whitelist is live，3,333 ROCK on @LayerZero_Core soon。官网 HTTP 200，标题 ROCKZERO Whitelist；/api/config 返回 open=true、x=rockzerodotlive、postUrl 指向同一官帖、closesAt=null，官帖 t.co 跳转官网，siteXMutual=mutual。/api/stats 本轮 applied=4、approved=3、day=4。白名单申请已开且自称免费、无需链上交易：连钱包签 EIP-191 消息（不发送交易）+ 关注官推 + 上传带手写校验码的真实石头照片，每钱包/每个 X 号限一次。铸造时间、价格、主网日期尚未公布，本轮未见合约，lzVerified=false。**免费登记已开，不是已开铸免费 mint LIVE。** 栏：LayerZero，focus=false，status=whitelist-open，dsFallback overall 78。已进 userFollowWatch + layerZeroWatch。

因真新收录且状态为免费登记，notify=true。告警已点名 ROCKZERO。

## 看见但未收

- @Oathlydotai：约 0.80 天、23 粉，本轮仍 0 自有官帖、无官网，R2232 已跳过，不额外 getUsersPosts，继续跳过。
- @yeriyaps：约 2.15 天，GIWA 项目盘点号，不是项目本体，跳过。
- @FamiliarsAI：约 29+ 天，官网仍写售罄，R2231/R2232 已跳过，本轮仍不收录。
- @QikLaunch：R2232 已作 SEO 噪音跳过，本轮再见，仍不收录。
- @foilvaultapp：Pokemon 卡牌收集应用，不是加密 mint，跳过。
- @LOLOnCanton：约 9.5 天、98 粉，$CLOL 已在 Canton 发射台 live 的 meme 币，不是极早期新台，跳过。
- @UseAvalon：约 15.5 天，仅被提及、本轮无自有官帖，提及语境靠近 Elysium 但 Exploring ≠ Elysium 栏，不额外拉帖，跳过。
- @ElysiumHubHB：约 28 天聚合号，无官网，跳过。
- @Nerosmall* 等 0 粉转发号、@LOJchronicles 圣经经文（Stark 关键词误伤），跳过。
- @Kimchifunxyz：仅出现在第三方 GIWA 盘点，无本轮官帖/官网核验，不额外 getUsers，暂不收录。@gasokfun / @hamrdotfun / @Gazuaxyz / @GIWAForge / @SaePadKR / @VordaLaunch / @MMIX_io / @PlunderPort / @PairMineAI 等已在库。

## 库内刷新（不重推）

- QQAI（@QQAI_BNB）：开铸仍 2026-11-26 18:00 CST，站点仍写销售未开、合约锁定。距开铸约 1.2h。R2232 已首次 ≤2h 提醒，不重推。
- Lamoryant（@Lamoryant）：官帖 2026-11-26 16:22:48 CST（https://x.com/Lamoryant/status/2125867857237971289）确认 OG Mint 于 11:00 UTC / 19:00 CST 开始，并公布 CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c。官网 mint 页仍 0 / 1,356，倒计时按 JS 占位，不是已开铸 LIVE。距开铸约 2.2h，未到首次 ≤2h，不提前告警。
- Ugly Puggies：OpenSea 页解析约 539/777、持有 343、地板 0.0001 ETH（R2232 为 531/777、338、0.000159 ETH）。官帖称还剩 243。SIGNED_PRESALE #3 时间表未改。只是进度，不重推。
- Crawlers Agent：官网仍 MINT · OPENING SOON，开铸仍 20:00 CST（约 3.2h），未到首次 ≤2h。
- RuninAI：官网与官帖均称 $RUNINAI Round 2 铸造已结束并在 PancakeSwap 交易；$RMINE 挖矿自 2026-11-25 20:00:19 CST Day 0 起已 LIVE，每日 20:00 CST 为重复日窗。不是新的免费 mint，不重推。
- Wildlife Universe：官网仍 26 Nov 2026 · 7:00 PM IST（21:30 CST，约 4.7h），未到首次 ≤2h。
- Vicehood：官网仍 Early List，首窗仍 2026-11-27 01:00 CST（约 8.2h）。
- 2hour.fun：/api/window 仍是交易者统计（traderCount=43），窗口仍关，下一窗仍 2026-11-27 05:00–07:00 CST。
- HamsteCombatHQ：仍是 1,111 free mint / WL Launching Soon，R2226 已提醒，不重推。
- PairMine：UF 软刷见产品说明，非新开盘，不重推。
- TriForge / F0B90B / Antopia / Jacket / deMiners / Guns / Agent Cards / Valorix / Shielded Wizards / Bonebloom：本轮未新拉对应 OS/RPC，沿用 R2232 进度，MUST 未见改期，不重推。

## Discord

未打开 Discord/浏览器。discordPeekDeferred=true，discordLoginOk=false。须父进程同一轮补 Peek；登录墙与约 R2206 起相同，不要重发登录表单，除非已有新会话。补扫若出现免费 mint/登记再通知。

## notify

notify=true。原因：真新收录 ROCKZERO，且状态为免费登记已开。告警已点名 ROCKZERO。无新的首次 ≤2h（QQAI 已在 R2232 提醒）。
