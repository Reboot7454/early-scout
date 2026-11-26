# 早期打新雷达 RESULT R2235

- 时间：2026-11-26 17:42:35 CST（Asia/Shanghai）
- 面板：https://reboot7454.github.io/early-scout/
- 仓库：Reboot7454/early-scout，本轮只推 data.json + docs/data.json + RESULT_R2235.md 到 main
- lastFullAfterReset：R2216（本轮是增量，非 08:00 CST 后首轮全量补扫）
- notify：false（无新收录、无首次 ≤2h、推送若成功则不告警）
- dsFallback：true（DeepSeek HTTP 401，api key invalid；未用高成本模型批量筛）
- discordPeekDeferred：true；loginOk=false；本轮未打开浏览器（登录墙与约 R2206 起相同，不重发登录表单，除非已有新会话）。lastSeen 未改，仍停在 2026-11-23 22:19–22:56 CST。

## X 额度

- remainingBefore：506
- xReads：27（计划主查询 26 + 静号 1；另因 MUST_WIN 首次写盘失败而重拉 1 次，计入本轮）
- remainingAfter：479
- 模式：pace（scripts/x_budget.py softCap/minSpend 18；remaining ≫ 200，未砍栏）
- 重置：约 2026-11-27 08:00 CST
- mustWinRefetch：true（只此一次补拉，未为「再确认」重读其它 handle）
- starx_xlayer：长期 NF skip，本轮未 getUsers 重读

## 覆盖

- userFollow：已刷完本片 50 号。cursor 1247 @trenchingdotfun → 下一 cursor 1297 @makehoodxyz，wrap=false，NF_skip=0。UF1/UF2/UF3 均为 0 帖。
- 十栏关键词：已跑全（LZ / Tape / GIWA / DogeEVM / BTC / Starknet / mint / mine / pad / GO / Elysium + KW_GAPS）。必盯 MUST_WIN + MUST_WIN2 + MUST_OFF 已跑。
- mentions（本轮轮换）：GIWA / Tape / LayerZero（24h）/ Elysium。下轮：DogeEVM / BTC / Starknet / pads+squeek+STARX。
- 静号：GIWA（has:mentions fallback，search_users 不可用），命中触顶 25，送审 0、新收 0。下轮静号：Tape。
- 瘦栏 24h 补搜：LayerZero（30m=0）、BTC（30m=0）、Starknet（30m=4）。跳过 24h：Tape（22）、GIWA（25）、DogeEVM（8），因 30m≥5。
- 未偏科；未整栏跳过。

## 新收录 / 告警

- 新收录：无
- 首次 ≤2h：无
  - QQAI：距 18:00 CST 约 17 分钟，站点仍 PRE-LAUNCH、合约锁定，R2232 已提醒，不重推
  - Lamoryant：距 19:00 CST 约 1.3h，mint 页仍 0/1356、倒计时按 JS 占位，R2234 已提醒，不重推
  - Crawlers Agent：距 20:00 CST 约 2.3h，仍 MINT · OPENING SOON，未到首次 ≤2h
  - Wildlife Universe：距 21:30 CST 约 3.8h

## 窗口核验（不重推）

- **QQAI**：官网仍 PRE-LAUNCH，写明 sale is not open yet / minting locked until 18:00 CST。555 份自称免费 mint（门费 0.0001 BNB）。不是已开铸 LIVE。
- **Lamoryant**：mint 页仍 0/1,356，OG Phase 仍 11:00 UTC / 19:00 CST。倒计时全零按 JS 占位，不以 LIVE 计。
- **Crawlers Agent**：crawlersagent.com 与 pages.dev 仍 MINT · OPENING SOON，开铸仍 20:00 CST（0.004 BNB / Agent ID）。不是免费 mint。
- **Wildlife Universe**：17:30 CST 官帖称 Today is the day、$Tigeruniverse is live on Robinhood chain，并给出 OpenSea 合集；同时写 game opens at 1:30 PM UTC（仍 21:30 CST）。官网倒计时未改，OpenSea tiger-universe-415604972 仍 Minting soon。这是「今天开窗」提醒+合集已上架，不是已开铸 LIVE，也不是改期。
- **Vicehood**：OpenSea 仍 Minting soon，首窗仍 2026-11-27 01:00 CST。
- **Ugly Puggies**：OpenSea 仍 Minting now，可见 558/777（R2234 为 549/777），地板 0.0001 ETH。只是进度。
- **2hour.fun**：/api/window 仍 traderCount=43，窗关；下一窗仍 2026-11-27 05:00–07:00 CST。
- **RuninAI**：MUST 再见每日 20:00 CST $RMINE 窗口宣传，口径未变，不按新 LIVE 重推。
- **HamsteCombatHQ**：仍 1,111 Free Mint / WL Launching Soon + Collabs open，未见开铸，R2226 已提醒。

## 看见但跳过

- **@thedarkpoolfun**（thedarkpool.fun）：建号约 8.05 天、85 粉 / 15 帖。站点是 Solana 隐私 OTC/暗池（JS SPA，v2.2.1-mainnet），bio 已有 pump.fun CA；本轮无自有官帖。已上线交易产品+已发币，不是免费 mint/新开台，未达极早期可操作打新门槛。
- **@cloakxdotfun**（cloakx.fun）：建号约 21.59 天、157 粉 / 34 帖。核心是 Solana 隐私支付（Send/OTC/Swap）；页面 Launch 文案仍 Coming soon。官帖称今日推 Launchpad / Meteora 集成，发射台未确认 LIVE，龄期偏晚。
- 其余短名单沿用既有判断，不重开：Oathlydotai、EvilsApe、yeriyaps、FamiliarsAI、ElysiumHubHB、LOJchronicles、Pangomeme（无站点）、Kimchifunxyz（仅第三方列表）、GiwaPump（约 119 天）、Svarogofficial（交易/捆绑工具）、babblesxyz（waitlist 已结束）、GAMA_GIWA / gamatiles（库内）、spike__wtf（库内）。mentions 多为 giveaway 农场。

## Watch / 其它

- 本轮无新卡，无漏挂补进。UF / 各 *Watch lastChecked 已软刷。Canton / Glaze / TokenWorks lastChecked 已刷新。
- 下轮 mentions：DogeEVM / BTC / Starknet / pads+squeek+STARX；下轮静号：Tape。
