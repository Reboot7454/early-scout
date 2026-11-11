# Early Scout 面板功能说明（给父 agent）

静态站：`/workspace/early-scout/` → 发布镜像 `/workspace/early-scout-pages/`  
永久 URL：https://reboot7454.github.io/early-scout/  
风险声明：高风险 · 非投资建议 · DYOR

## 1) 开售日程（schedule）

- 候选可选字段 `schedule`：`status`（confirmed|tentative|tba|live|ended）、`startsAt`（ISO8601）、`phases[]`、`source`、`note`（中文）。
- **只在有证据时写入**；模糊文案用 `tentative` + note，不编造精确时刻。
- 面板：卡片日程 chip（今晚/倒计时/进行中/TBA）、顶栏「日程」最多 12 条（主窗口 now−6h～now+72h；**保底入栏**=台子/Meme/Launchpad 的 upcoming/confirmed/tentative ≤72h，**或**任意 confirmed 且未来 startsAt ≤24h；余量优先未来时刻；live 台子可回看至 24h 作余量）、筛选「即将开售（24h）/有日程」、排序「开售时间（近→远）」；点击开推特。
- 倒计时按 Asia/Shanghai 展示；每 30s 刷新标签。

## 2) 链上 mint 盯盘（onchain）

- 可选字段 `onchain`：`chainId`、`contract`、`standard`、`mintStatus`、`minted`/`totalSupply`/`maxSupply`、`explorer`、`lastCheckedAt`。
- 有合约或 OpenSea 时卡片显示状态行（未开 / 进行中 / x/y / 合约链接）。
- 脚本：`python3 scripts/check_onchain.py`  
  - 读 `data.json`，对 EVM（ethereum/base/ink/robinhood）用公共 RPC `eth_getCode` + `totalSupply()`。  
  - 无 API key；失败软跳过；打印 JSON 变更摘要。  
  - **Solana / 无稳定 RPC 的链会 skip**；Robinhood 公共 RPC 常不可用。

## 3) 亮点 / 缺点 / 本轮新 / 评分

- `highlights[]`、`drawbacks[]`：各 2–4 条短中文要点（具体机制/窗口/风险，避免空话）。
- `whatsNew`：续更说明文案；**仅** `newThisRound: true`（= 当前 `roundNAdded`）显示「本轮新」徽章，其余有文案时显示「续更」。
- `round`：首次收录轮次（discovery），例行续更**不得**改写成当前 round；轮次筛选靠此字段。
- 例行交接：新收录写 `newThisRound:true` + `flag:"本轮新"` + `meta.roundNAdded`，并把 **`meta.newThisRound` 改成这一轮的 id**（先清上一轮，不要留上一轮 id）；上一轮新收录清 `newThisRound`/`本轮新`，可留 whatsNew 续更句。
- 推特链接：admit **写 `links.x`**。面板可见性与 X 按钮同时认 `links.x` 和 `links.twitter`（须含 `x.com/` 或 `twitter.com/`）。只写 `links.twitter` 时卡片和该轮芯片都不会出现。
- `scores`：`early` / `risk`（镜像 earlyScore/riskScore）、`novelty`、`actionable`、`overall`  
  - `overall = early*0.35 + actionable*0.25 + novelty*0.2 + (100-risk)*0.2`
- 面板：综合分大号 + 四条迷你条；亮点/缺点双列；排序「综合评分」。

## 维护脚本

| 脚本 | 用途 |
|------|------|
| `scripts/extract_schedules.py` | 日程/链上证据回填（幂等覆盖 schedule/onchain map） |
| `scripts/enrich_cards.py` | 全量亮点/缺点/whatsNew/scores |
| `scripts/check_onchain.py` | 公共 RPC 探测并写回 mint 状态 |

改完后：校验 JSON → 同步到 `early-scout-pages/` → 父 agent push `Reboot7454/early-scout` main。

## 4) 挖矿品类（GPU PoW / NFT 变异盘）

- 新品类 `category: "挖矿"`：GPU/PoW 币（PRL / QTC / NOID 风格）与 NFT 挖矿/变异盘。
- 可选字段 `miningType`：`gpu-pow` | `nft-mutation` | `nft-miner` | `other`；`tags` 含 `挖矿`/`PoW`/`变异盘`。
- 面板：重点/收藏为顶部横条；宽屏（≥1280px）九列 `.board`，顺序 **打新 | 挖矿 | 台子/Meme | GO盘 | LayerZero | Elysium 生态 | Tape/电路 | GIWA | DogeEVM**；列 min≈140px，≈1440px 起九列自适应收窄不横滑（1440 时每列≈149px、1600≈167px、1920≈201px），更窄才横向滚动；板内卡片为紧凑版（☆+轮次一行置顶、亮点/缺点单列）。窄屏纵向堆叠，顺序相同。
- 互斥归类（一条只进一列，**仅栏位分配、非搜刮权重**）：Elysium 生态 → **GIWA** → **DogeEVM** → **Tape/电路** → LayerZero → 挖矿 → GO盘 → 台子/Meme → 其余打新。重点横条（`focus: true` / `meta.focusIds` / tags 含 `重点`）默认不进其它列；**Elysium / Tape/电路 / GIWA / DogeEVM 栏例外**，可与重点条重复展示（TapeAI 等 `focus:true` 仍出现在 Tape 列）。例行搜刮对各栏同等努力，**加 Tape 列不得收缩打新/挖矿/台子/GO/LZ/Elysium/BTC**。
- **台子/Meme 归类**：以 `category` ∈ {台子/Meme, 新台, Meme, Launchpad} 为准；仅强 tag（`台子/Meme` / `新台`）可补判。NFT 打新上的零散 `Launchpad`/`Meme` tag **不得**挤进台子列。**GO盘**以 `category==="GO盘"` 或 tag `GO盘`/`go玩法` 等为准（勿漏检）。
- 「全部链」筛区有独立芯片 **Elysium 生态**（按 `isElysium`）、**Tape/电路**（按 `isTape`）、**GIWA**（按 `isGiwa`）、**DogeEVM**（按 `isDogeEvm`），不只看单链名。
- **GIWA 栏（第八栏 · 蓝）**：`isGiwa` = `ecosystem` / `tags` / `chain` 任一含 `giwa`（不区分大小写）。新项目打 tag `GIWA` 或 `ecosystem:"GIWA"` 即进栏。
- **DogeEVM 栏（第九栏 · 最右 · 青柠）**：`isDogeEvm` = `ecosystem` / `tags` / `chain` 去空格/下划线/连字符后含 `dogeevm` 或 `dogeos`（不区分大小写；`Doge EVM`、`DogeOS` 均可）。新项目打 tag `DogeEVM` 即进栏。
- 默认排序「最新信号」：有 `firstSeen` 或 `addedAt` 则新的在前，否则 `round` 降序；同轮 `whatsNew` 非空优先，再按 `scores.overall` / `earlyScore`。九列共用；下拉仍可改早期程度 / 综合 / 日程 / 风险 / 名称。
- 挖矿列保持紧凑 `.mining-row` + GPU PoW / NFT 变异 / Miner NFT / 其他。打新、台子/Meme、GO盘、LayerZero、Elysium、Tape/电路用完整卡片。点品类「挖矿」或顶栏药丸跳到对应列；LayerZero / Elysium / Tape 顶栏/芯片可跳对应栏。
- 例行搜刮需**同等努力**覆盖：打新（全部链）、挖矿（GPU/AI-PoW、NFT 变异/Miner）、台子·Meme、GO盘、LayerZero、BTC 生态，以及其它生态。Elysium 与 Tape/电路是加栏加盯，**不得**把搜刮收成只扫这两栏。
- **2026-11-11 起强制分栏查询**：LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet 每轮各至少一次独立关键词搜索，禁止并进 Elysium / BNB / Robinhood 的大搜索；薄栏 Watch 每轮全读，厚表分片。细则见 `scripts/x_budget.py` 的 `alloc` / `kwThinQueries` 与 HANDOFF「不要偏科」。2026-11-12 起在薄栏 KW 之后加静号补漏（`silentCap`，不占 softCap），见 §8b。

## 5) 重点横条（focus · 非栏位）

- **重点**是搜索/统计下方的顶部横条（`#focus-panel`），**不是**九列之一；与轮次筛选无关，常驻。
- 归入条件（任一即可）：`focus: true` · `id ∈ meta.focusIds` · `tags` 含 `重点`。视觉：玫粉/琥珀描边 + 「重点」chip。
- 默认**只上横条、不进九列**；**例外**：Elysium 生态本体、Tape/电路系列、GIWA、DogeEVM（`columnAllowsFocus`：`elysium` / `tape` / `giwa` / `dogeevm`），可同时出现在重点条与对应栏。
- 种子：`squeekchain`（首位）· `hamster-hour`。例行可把清晰早期 peer 以 `focus: true` 收入，或至少打 `重点` tag 并记入 `meta.focusWatch`。
- `meta.focusWatch`：accounts + categoryScan + admitRule；**每轮例行扫描本类**（非整账号时间线监控）。


## 6) 收藏（favorites · 客户端）

- 每张卡片 / 挖矿行有 ☆/★ 收藏按钮，一键切换。
- 「收藏」横条在「重点」下方、**九列**看板上方；**不依赖轮次筛选**（与重点条同为全局条）。
- 数据仅存浏览器 `localStorage` 键 `early-scout-favorites`（candidate id 数组）；不改 `data.json` schema。
- 收藏条展示日程倒计时（复用 `scheduleChip`，≈72h / LIVE）；点击条目或 X 打开 `links.x`（没有则用 `links.twitter`）。
- 空态：「点卡片上的☆收藏」。与系统「重点」（`focus:true`）互不混淆。


## 7) 例行扩展关注（非全量 X 监控）

- **TokenWorks Playground**：盯 `@Rhynotic`（兼 `@token_works`）与站 https://playground.token.works/ ——策展小组发射/分账台（ETH+Robinhood）；关注 `launchesEnabled`、首批想法（FWA 配对）、工厂公开部署。归台子/Meme，勿因跨链字样进 LayerZero。
- **实验玩具链 / 实体+链上（重点栏 standing watch）**：每轮扫同类信号——仓鼠/动物 PoW toychain、硬件矿机 novelty 链、实体物理装置上链验证、公平分配实验 L1/L2 且仍预发币/测试网。种子账号 `@squeekchain` `@squeektoshi` `@pillheadddd` `@hamsterhourgame`；同类有推特的清晰早期 peer → 重点栏（`squeekchain` 保持首位）。
- **Elysium 类生态（第六栏 · `meta.elysiumWatch`）**：**加栏加盯的一例，不收缩覆盖**。每轮在同等努力扫打新 / 挖矿 / 台子·Meme / GO盘 / LayerZero / Tape / BTC 的前提下，额外盯 `@Enter_Elysium` 及 AscendLaunch / Eloscape / Speculate / Montra / Aegis / kalos 等子项目，以及**同类新生态**（Hyperliquid 旁路 L2 / Orbit 玩具生态等）。有推特的清晰成员 → `ecosystem:"Elysium"` + tag `Elysium生态`，互斥进「Elysium 生态」栏；链筛「Elysium 生态」只显示该生态。**不得**把例行搜刮收成「只扫 Elysium」。电路/TapeOut 项目即使文案里出现别的链，也**不要**标 Elysium。
- **Elysium 收录门槛**：对照 https://elysium.kinetiq.xyz/ecosystem ，只有 **On testnet**，或 **Announced 且写明具体 Elysium 部署**，才可进 Elysium 栏 / 打 `Elysium生态`。**Exploring**、「considering」、仅在生态页露名、或只是靠近 Hyperliquid，一律不进该栏，按真实品类归 GO盘 / 台子 / 打新等。`perpme` 即使用户页上是 On testnet，也按用户决定留在台子/HyperEVM，不要因文案里提到 testnet 路径改回 Elysium。
- **X链/OKX 及同类极早期发射台（`meta.xChainPadWatch` / `meta.starcatWatch`）**：盯 `@StarcatOKX`（X Layer/Ignix，starcat.world）与 `@NinetailsTrade`（Solana 隐私多钱包兑换 peer，ninetails.trade）；归**台子/Meme**，**勿**进 Elysium/LZ。**同等努力七栏、不偏科只盯 Elysium 或 Tape**。非全量 X 时间线。
- **PaperBird 类极早期鸟/meme/发射（`meta.paperbirdWatch`）**：盯 `@paperbird_lol`（flappy bird 前端 × `@papertrade_xyz` / Hyperliquid 1000x）与站 https://paperbird.lol/；归**台子/Meme**，**勿**进 Elysium/LZ。**同等努力七栏、不偏科**。非全量 X 时间线；无精确日程不编造。
- **BTC 隐私 Ordinals / CRC20（`meta.btcPrivacyWatch` / `meta.btcCrc20Watch` / `meta.watches.btcOrdinals`）**：盯 `@ShieldedNaka` `@banknotes_btc` `@strangersolemn` `@mannequinsnft` 与 OrdDropz 圈，以及 CRC20 `@Satelite_CRC20` `@BONSonBTC` `@BTC_CRC30` `@BitcoinITMoney`——隐私 Ordinals / Shielded early mints 与 CRC20 发射**同等努力**（不偏科只盯其它栏）；有独立推特且极早期才收录；无精确日程不编造；发射台基建（OrdDropz）入 accounts 不单列 admit。
- **电路板 / TapeOut（第七栏 · `meta.blonskrWatch` / `meta.watches.tapeOut`）**：用户监视 `@TapeAIAgent` + `@Blonskr` 关注线——门级电路、电路 NFT、电路板叙事（TapeAI 检察官电路 mint、BEM PoD、TapeUP/DeWEB、Firsto、WAFER、TAPELIQUID、Fab X、TapeFi 等）。同类有**独立项目推特**且极早期可操作才收录；社区水军/纯个人号（如无项目号的 TapePack、bio 仅为 Team Member 的个人号）不收。行情/股票 “tape” 撞名（Pretape、Squeeze、ZECScreen、Folce、Tape Terminal、Tape Markets 等）**不进**本栏。
- **Tape/电路收录门槛**：`ecosystem` 为 TapeOut，或 `category`/tags 含 `TapeOut` / `电路板` / `电路NFT` / circuit-board，或命中已知 TapeOut 项目号 → `isTape` → 第七栏（在 Elysium 右侧）。`zoneOf` 优先级：**elysium > giwa > dogeevm > tape > lz > mining > go > meme > scout**。**勿标 Elysium**。Peek 标「淘汰」但 bio 仍是 TapeOut 协议且账号仍在的，可留栏；已在库的（如 BEM）不因淘汰标删除。
- 此类为品类扩展监视（与 LZ / 玩具链 / Peek 对账并列），**不是**恢复全量 X 账号时间线监控，也**不是**对其它栏的替代。


## 8) Peek/潜力榜对账（学习规则 · 非照搬）

每轮例行增加一次 **Peek / 潜力榜对账**，目的是**发现信源盲区并改进搜刮**，不是把榜单当收录清单。

- **只对照**：NFT·新台·AI 发射·极早期 DeFi/GameFi（Ink 算法艺术、Solana·HL 早期台、AI agent 盘等品类监视可扩）。
- **可补录条件**：有可核验推特 + 仍处极早期可观察/可操作窗口 + 我们主信源（Trencher/NorthBound/RobinXP/OpenSea/Web）漏掉。
- **禁止**：把 Peek 热度榜整表入库；收成熟协议 / Infra 空壳 / 疑似刷量 / 中后期 DeFi；为「对账完成」而扩容。
- **Discord `#alpha-1` Peek（`meta.discordAlphaPeek` / `meta.watches.discordAlphaPeek`）**：已挂入 **35m 例行**作 Peek对账补漏；只补漏且仍极早期的项；七栏归类；**不是**全量 X 时间线监控。主频道 alpha-1（Spidey Bot / X Follow Monitor / Captain Hook）；backup / smart-accounts-tracker / alpha-3-new-accounts 辅助。
- **仍非**全量 X 账号时间线监控；对账是品类学习扫描，执行端只拉信号/改 json/push，文案与打分走 deepseek-flash（thinking on）。

## 8b) 静号补漏（本仓自有 · 不依赖 Discord）

Discord `#alpha-1` 的关注监控是补漏，不是静号的唯一入口。0 帖官号不会出现在推文关键词结果里。本路径在薄栏独立 KW 之后、核心栏 KW 之前跑，Discord 挂了也照跑。

- 预算：`scripts/x_budget.py` 的 `silentCap` / `alloc.silent`。这几读**不占 softCap**，也不从 `userFollowWatch` 或六条薄栏 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）里扣。`silentCap=0`（零 X、near-exhausted、或 remaining 盖不住 softCap）时不调用 X，RESULT 仍写 `silentAccounts.ran=false`。
- 调用清单以 `python3 scripts/silent_accounts.py plan` 为准，不要翻页，不要把静号 query 并进 Elysium / BNB / Robinhood 大搜索。每轮只轮换一条 `search_users`（`silentRotation`，十一栏转圈）。`search_users` 对应 `GET /2/users/search`：query 只能是字母数字空格下划线撇号、最长 50，按名字/用户名/bio 做相关度匹配，**没有** `bio:` / `url:` / 帖数 / 注册时间算子；用户对象里的 `url` 才是资料栏网站。
- 第二读（仅 silentCap≥2）：没有待解析 handle 时，`search_posts_all` 用当轮 `mentionQuery`（`has:mentions`，抽别人帖子里的 @）。有上一轮 `deferredHandles` 时，改成一次 `get_users_by_usernames`。这一读**不算**该栏的薄栏 KW。
- `url:` 只命中帖子正文里的链接，不是资料栏网站。现有 X 客户端没有 following 列表工具，本路径不抓 Discord、也不另做关注图。
- 闸门在 `scripts/silent_accounts.py filter`：已在库、帖数 >3、账号老于 120 天、没有资料网站也没有产品 bio 的跳过。**0 帖且粉丝 ≥500、站点没有 HTTP 确认存活、也没有已确认的链上证据 → `shell_deferred`，不送审不收录**（R1623，@yumsdotfun 当时约 708 粉、0 帖、站未开）。站点确认存活或链上证据确认之后才送 deepseek-flash，脚本本身不收录。
- 送审包强制 `links.x` 且 `focus:false`。普通新卡不要写 `focus:true`。
- 每轮 RESULT 增加：

```json
"silentAccounts": {
  "ran": true,
  "seen": 0,
  "sentToReview": 0,
  "admitted": 0,
  "skipped": 0
}
```

`seen = sentToReview + skipped`。`admitted` 是其中真正写入的新卡数，过滤阶段为 0；DeepSeek 拒掉的仍算送审、不算 skipped。计数对不齐时 `silent_accounts.py result` 会直接退出。

残留缺口：资料网站为空、bio 既没有网址也不含当轮 query、又没有第三方帖子点名该 @ 的 0 帖号（@yumsdotfun 在 2026-11-11 07:35 CST 就是这种），用户搜索和推文搜索都看不到。Discord 关注监控之前能看到，是因为它看的是别人的新关注，不是帖子。这条缺口写在 `plan` 的 `residualGap` 里，不要用抓 Discord 来填。

## DeepSeek 省用量（硬卸载 · 2026-10-17）
- **必须**用 `deepseek-flash`（thinking **ON**，勿关闭）做全部判断类工作：admit / score / zone 文案草稿 / highlights / whatsNew / alert / summary / dedupe。
- **执行端只做**：拉信号、跑脚本、改 `data.json`、push、写 RESULT、notify 布尔；不做雷达文案或批量打分推理。
- **禁止**用高成本模型（含 SuperGrok 等）写雷达 copy 或做 batch scoring。
- 脚本：`scripts/deepseek_chat.py`、`scripts/ds_batch_score.py`。
