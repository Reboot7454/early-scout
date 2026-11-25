# Early-scout R2192 结果

执行器只在 box 上工作，未改 /workspace/early-scout/data.json，未 commit / push。仓库仍停在 1bfe963（R2191）。本轮产物在 /tmp/r2192/，供 parent apply、提交 data.json + docs/data.json + RESULT_R2192.md，并决定推送。

开火约 2026-11-25 19:05 CST（Asia/Shanghai）。lastScout 源数据 2026-11-25 18:51:45 CST。常规增量轮，不是 08:00 CST 后首轮全量补扫（lastFullAfterReset=R2170）。dry-run lastScout=2026-11-25 19:19:37 CST。

## X 额度与预算

- 第一笔 UF1 后 remainingToday=396 / 1000。因此 remainingBefore=397/1000，与预期一致。
- `python3 /workspace/early-scout/scripts/x_budget.py 397` 建议 mode=pace、softCap=18、minSpend=18、silentCap=2。
- **覆盖**：remaining ≫ 200，且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185–R2191 相同）。UF1/UF2/UF3 是因为 50 户分片受 qlen 限制拆成三次 from:；MUST_WIN / MUST_WIN2 / MUST_WIN3 是计划内官号 from: 批次（MUST_WIN3 因必盯名单较长，含 R2191 新官号 @deMinersNft、@AnthroposAgents），不是探索性加读。
- 实际：xReads=28（main 27 + silent 1），remainingAfter=369/1000。无重复查询、无探索性加读、无分页。search_users 仍不可用。跳过已知 NF @starx_xlayer 的 from: 查找，未重试；MEN_STARX 仍搜该号 mentions，这是计划内，不是 user lookup 重试。
- 全部 28 次搜索均成功写入 /tmp/r2192/x_raw/，errors=[]。部分工具结果曾是预览，已用 save_xraw.py 还原完整文本，未重查同一搜索。

## 搜索执行

计划顺序已全部跑完一次：UF1/UF2/UF3 → MUST_WIN / MUST_WIN2 / MUST_WIN3（24h）→ MUST_OFF（30m）→ 10 栏 + KW_GAPS 30m → MEN_DOGE / MEN_BTC / MEN_STARK / MEN_SQUEEK / MEN_STARX → SILENT_GO。全部 10 栏独立 KW 与 KW_GAPS 均已跑。

30m 独立 KW 命中：LZ=4、TAPE=25、GIWA=25、DOGE=16、BTC=3、STARK=1、MINT=25、MINE=1、PAD=25、GO=25、ELY=15、GAPS=14。

**瘦栏 24h 回填**（仅 30m 独立 KW <5，每栏最多 +1）：

- 已跑：KW_LZ_24（25）、KW_BTC_24（25）、KW_STARK_24（25）。
- 未跑：KW_TAPE_24（25≥5）、KW_GIWA_24（25≥5）、KW_DOGE_24（16≥5）。
- MINE=1 但是核心栏，未加 24h。

其它命中：UF1=0、UF2=0、UF3=0；MUST_WIN=25 触顶、MUST_WIN2=25 触顶、MUST_WIN3=25 触顶、MUST_OFF=15；MEN_DOGE=9、MEN_BTC=25 触顶、MEN_STARK=5、MEN_SQUEEK=0、MEN_STARX=0；SILENT_GO=10。

UF 软刷：cursor 1661 @sonnaagent，50 户至 @bagholderfun，wrap=false，total 源 2404 / dry-run 后 2405（新挂 @secretwiz_rgb）；下轮 1711 @PyreOnchain。本分片无已知 NF，mustOverlap=0。因 qlen 拆成 UF1/UF2/UF3，三次均 0 帖。

MUST：MUST_WIN / MUST_WIN2 / MUST_WIN3 均 25 触顶。MUST_WIN3 里 @usehelipaid 占了大多数名额，本轮返回未见 @deMinersNft / @AnthroposAgents 新帖，未分页、未加读。MUST_OFF 已跳过已知 NF @starx_xlayer，未重试。

Mentions 本轮：DogeEVM（9）/ BTC（25 触顶）/ Starknet（5）/ squeek（0）/ STARX（0）。下轮应轮换 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest（本轮没有跑这些 mentions）。

静号：GO盘（2192 % 11 = 3），SILENT_GO 24h keyword fallback（search_users 不可用），10 帖，不占 softCap。命中全是无关「go launch」口语/噪音，没有新项目。下轮 silent：LayerZero（2193 % 11 = 4）。

## 关键核验

### Ugly Puggies @uglypuggies — 官帖倒计时 + OpenSea 首阶段指向 23:00 CST；本轮不按 21:00 报首次 ≤2h（须点名）

官帖 2026-11-25 19:00:30 CST（https://x.com/uglypuggies/status/2125545156292309490）：

> UPDATE: All wl has been added / T-4 hours / Collabs is closed / See you all at mint!!! Stay Pugged in

17:54:26 CST 另一则官帖只是抽奖获奖名单，不是开铸确认。

公开 OpenSea（https://opensea.io/collection/ugly-puggies-106253855 及 api.opensea.io）：

- twitter_username=uglypuggies。合约 0xe2be23fbffe892feb3677341765847b9309663c2（Robinhood Chain）本轮已由官方合集独立核到，不再只是转载。
- collection API total_supply/unique_item_count=0，owners=0，volume=0。
- drop.mintStatus=**MINTING_SOON**（不是 MINTING），maxSupply=777，totalSupply=0，activeDropStage=null。
- SeaDrop 阶段（已换算为 CST；阶段类型来自 OpenSea，**不是**官帖确认的 TEAM/GTD/FCFS 标签；本轮未从 drop 对象核到单价，不编造免费/付费数字）：
  1. SIGNED_PRESALE#1：2026-11-25 23:00–23:30 CST（15:00–15:30 UTC）
  2. SIGNED_PRESALE#2：2026-11-25 23:30 CST – 2026-11-26 13:30 CST
  3. SIGNED_PRESALE#3：2026-11-26 13:30 CST – 2026-11-27 13:30 CST
  4. PUBLIC_SALE：2026-11-27 13:30 CST – 2026-11-29 13:30 CST

官帖「T-4 hours」（19:00 CST 起约 4 小时）与 OpenSea 首阶段 23:00 CST（15:00 UTC）一致。此前卡片里的 21:00 CST（13:00 UTC）来自第三方镜像/打新板，**从未被官帖钟点确认**。本轮据此把 opensAt 改为 2026-11-25 23:00 CST，卡片 le2h=false。

这是须点名的日程纠正，但**不是**已确认开铸 LIVE，也**不是**按旧的 21:00 CST 口径发出的首次 ≤2h。按 23:00 CST 口径，首次 ≤2h 约 21:00 CST 才进入。自称免费 mint（777，Robinhood Chain）。不要把第三方分阶段规则写成官方。本号不自动 mint。已保持 freeMintWatch。

### SecretWiz @secretwiz_rgb — 新收录，官网 allowlist 已开（须点名）

官号建号 2026-11-24 21:40:05 CST，7 粉 / following 10 / 1 帖，xUserId 2125222368414949376，资料栏 https://secretwiz.xyz/ 。本轮 MEN_BTC 见到唯一官帖 2026-11-25 18:30:49 CST（https://x.com/secretwiz_rgb/status/2125537685389595123）：Wizards coming to haunt Nov 28；SecretWiz RGB UDA NFT collection is live；WL = Freemint；并让人留下 Unisat / RGBHorse / ratsonchain 的 Taproot 地址。

官网 HTTPS 200，标题 SecretWiz — RGB UDA NFT Collection，allowlist 登记已开（Follow / Repost / Like 后填写 handle 与收款地址）。资料栏指向官网；官网站内 X 链接是裸 https://x.com/，未写死 @secretwiz_rgb，互证不全。

这是免费白名单/登记已开，**不是**已确认开铸 LIVE，也不要把「collection is live」写成 mint LIVE。DeepSeek score=66（admit=true），focus=false。已挂 userFollowWatch + freeMintWatch + btcPrivacyWatch。本号不自动 mint。

### ORIPA @oripaxyz — 不重推

首包仍 2026-11-25 20:00 CST（8 PM GMT+8 / 12:00 UTC，不要误读成 12:00 CST），无改期。R2190 已发首次 ≤2h。本轮 MUST 24h 未见新官帖。开火时仍在 2 小时窗口内。不是免费 mint。卡片 le2h 保持 true，不重推。

### deMiners @deMinersNft — 不重推

OG list 免费 mint 仍 LIVE，至 2026-11-25 22:30:04 CST，0 ETH / 每钱包 3。MUST_WIN3 触顶，本轮返回未见该官号新帖。公开 OpenSea collection/deminers：collection API 约 481/3333，drop 页 totalSupply=482/3333，持有 125，地板 0.0007 ETH（二级市场，不是铸造价）；drop.mintStatus=MINTING，activeDropStage 仍为 OG list（SIGNED_PRESALE stageIndex=2）。相对 R2191 约 468/3333 为小幅进度，不是大额跳升/关窗/改规则，不重推。Public sale 仍 22:30:04 CST 起 0.0002 ETH，不是免费；公售首次 ≤2h 从 20:30 CST 才开始，本轮不提前告警。本号不自动 mint。

### The Jacket @TheJacket_NVDA — 不重推

MUST 再见到同一则 18:23:13 CST 供应削减官帖（R2191 已提醒）。持有人名单仍免费；公售仍 0.0003 ETH。OpenSea the-jacket-man collection API / drop 页约 173/777（R2191 约 170/777），持有约 123，地板仍 1.50 USDG，drop.mintStatus=MINTING，activeDropStage 仍为 PUBLIC_SALE。只是小幅进度，不因仍在 LIVE 重推。本号不自动 mint。

### ZeroGate @ZeroGate0G / Helipaid @usehelipaid / Anthropos @AnthroposAgents — 不重推

ZeroGate 本轮仍可见 18:03 CST live 官帖与 18:32 CST「Launch is failed because of snipers」回复，与 R2191 已记录内容相同，不能据此认定平台下线。Helipaid 本轮续发匿名 tip / Privacy Ring 产品说明，无改链/改价/新的免费窗。Anthropos 本轮 MUST_WIN3 触顶，返回未见新官帖。三者此前已提醒，本轮不重推。都不是免费 mint。

### Agent Cards @agentcardshq — 不提前告警

转载口径仍是 AGENTMINT 2026-11-25 23:00 CST（15:00 UTC），仅限 Agent ID。首次 ≤2h 21:00 CST 才进入。本轮未直接核到新官帖，不提前告警，也不按已进入 ≤2h 处理。

### 2hourfun @2hourfun / Shielded Wizards @ShieldedWizBTC — 不提前告警、不重推

2hourfun 官帖 19:07:36 CST（https://x.com/2hourfun/status/2125546944319660036）再确认 We open tonight anyway，21:00 UTC = 2026-11-26 05:00 CST，与既定第一场窗口一致，不要误读成今天 21:00 CST。

Shielded Wizards 官帖 18:50:30 CST 称已修复 bug、现在可用任意 Bitcoin 钱包铸造，并写 Public mint opens today at 21:00 UTC（= 2026-11-26 05:00 CST）。相对此前卡片记录的 21:10 UTC / 05:10 CST，官帖现写 21:00 UTC。官回 18:46:53 CST 称 allowlist mint is open now。WL 免费铸仍 LIVE，R2165 已提醒，不因仍在 LIVE 重推。公售首次 ≤2h 约 03:00 CST 才进入，不提前告警。本轮未用 JS 核到铸页新的已铸数字，不编造进度。

### TRIFORGE @TriForgeAgent

公共 BSC RPC（约 2026-11-25 19:12:33 CST，https://bsc-dataseed.binance.org/）：Forge Keys 免费铸仍 LIVE 未暂停，359/3333→363/3333，小幅增加，只更新卡片不重推。付费预售仍开，lpTotalMinted=0，lpTotalPaid=0；claimsOpen=true、totalClaimed=6（R2191 为 3）；miningShares=6；tokenTradingEnabled=false。本轮 MUST 返回中未见该官号新帖。

## 新收录

- **SecretWiz**（id=secretwiz-rgb，@secretwiz_rgb / https://secretwiz.xyz/）：见上。DeepSeek overall=66，admit=true。已挂 UF + freeMintWatch + btcPrivacyWatch。

## 看见但未收录

- **BLOCKPAY Genesis @BlockpayGenesis**：建号 2026-11-23 16:55:50 CST，21 粉 / 8 帖。资料栏只有 Discord，Bio 另有 Reddit。官帖 19:08:18 CST（https://x.com/BlockpayGenesis/status/2125547120086413650）自称免费 mint 已 LIVE，182/1,111，至 11-27 12:00 UTC，之后 0.001 BNB 付费至 Dec 1，Element Dec 2 开盘。本轮未独立核到官网或 CA（常见域名探测失败或无关；Element 合集名存在但页面需 JS）。DeepSeek overall=47，admit=false（缺官网/CA）。数字仅来自官帖。告警里已点名「看见但未收录」。
- **LAIKA Club @LaikaClubZH**：建号 2026-11-11 15:25:44 CST，7 粉 / 3 帖，资料栏 https://laika.club/ 。官网中英文页分别 twitter:site=@LaikaClubZH / @LaikaClubEN，与已有 Laika @LaikaSuperApp（laika-doge，DogeOS）不是同一项目。页面 Launchpad / AI Launch 仍 COMING SOON。不是免费 mint。DeepSeek overall=42，admit=false。
- **@launchxmaspad**：建号 2026-11-25 18:23:05 CST，0 粉 / 5 帖，自称「XMaspad is live」。无资料栏官网。https://xmaspad.fun twitter:site=@xmas_pad（站点 last-modified 约 2026-11-22），与 @launchxmaspad 未互证，不把该站当作其官网。未收录。
- 其它：@Mechalzem 空回复、@ManShingIsBored 转发 giveaway、@TooChillToSell 仅 Telegram + 自称 3 PM EST 开盘、@Raze_Fi 交易工具无铸造窗、SILENT_GO 十条均为无关「go launch」口语。均未送审收录。

## 库内更新（节选）

- ugly-puggies：opensAt 改为 2026-11-25 23:00 CST，le2h=false，CA 已核到，写入 OpenSea drop 阶段。
- oripa-xyz：le2h 保持 true，无改期。
- deminers：进度更新为约 481–482/3333。
- the-jacket：进度更新为约 173/777。
- triforge：359/3333→363/3333。
- 2hourfun / shielded-wizards：见上。
- zerogate / helipaid / anthropos：只刷记录，不重推。

## Discord Peek

discordPeekDeferred=true。执行器未自己做 Discord；/tmp/r2192/discord_peek.json 若存在，由 parent 合并。dry-run 默认留下 placeholder（APPLY_MERGE_DISCORD=1 时才合并）。该文件当前可见 loginOk=false、遇到登录墙、四频道未 peek、lastSeen 不变。

## 失败 / 限制

- X 搜索全部成功，errors=[]。MUST_WIN / MUST_WIN2 / MUST_WIN3 / 多条 KW 与 MEN_BTC 触顶 25，未分页。
- search_users 仍不可用，静号走 SILENT_GO 关键词回退。
- Shielded Wizards 铸页 brimhollow.app/mint 需 JS，未核到新的已铸数字。
- Discord Peek 登录墙，见上。
- DeepSeek 正常，dsFallback=false。判断/打分/文案均走 deepseek-flash（thinking on）。
- 本号不自动 mint。

## 通知

- notify=**true**
- 理由：Ugly Puggies 官方倒计时与 OpenSea 首阶段均指向 23:00 CST，须点名纠正此前第三方 21:00 CST 口径；尚未确认开铸 LIVE，本轮不按 21:00 报首次 ≤2h。新收录 SecretWiz 免费白名单/登记已开（score=66 也要点名）。BLOCKPAY Genesis 自称免费 mint LIVE 但未收录，仍在告警里点名。
- namedFreeMintOrRegistration：Ugly Puggies @uglypuggies（自称免费 mint，尚未确认开铸）；SecretWiz @secretwiz_rgb（官网 allowlist 已开，自称 WL=Freemint，不是开铸 LIVE）；BLOCKPAY Genesis @BlockpayGenesis（看见但未收录：官帖自称免费 mint LIVE）。
- dsFallback=false
- 告警文案见 /tmp/r2192/notify.json 的 alertMessage（已点名 @handles）。

## Parent 下一步

1. 如需合并 Discord Peek：APPLY_MERGE_DISCORD=1 再跑 apply（或 parent 自行合并 /tmp/r2192/discord_peek.json）。
2. 用 /tmp/r2192/apply_r2192.py 对仓库 data.json 做正式 apply（本执行器只对 /tmp/r2192/data.json.src 做了 dry-run，产出 /tmp/r2192/data.json）。
3. 提交 data.json + docs/data.json + RESULT_R2192.md，并按 notify=true 向用户推送告警。
