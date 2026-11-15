# RESULT R1878

- time: 2026-11-16 01:38 CST (Asia/Shanghai)
- mode: tight（remainingBefore 147<200）
- lastFullAfterReset: R1843（08:09 CST 的 08:00 后首轮全量补扫；本轮非补扫轮）
- xReads: 11（main 10 + silent 1）
- remaining: 147 → 136 / 1000
- softCap: 10，minSpend: 10，silentCap: 1
- notify: true
- newIds: 无（0 新收录）
- dsFallback: true（DeepSeek 文案两次未给出完整 JSON：一次推理溢出、一次截断；按同一已核验事实本地定稿。录取审核截断稿以 admit=[] 开头，shortlist 均为评论/市场/弱账号，无新卡需批量打分）

## 本轮做什么

独立例行 tight 扫。开跑 `git pull` 已与 origin/main 同步（起点 commit 103f5ba R1877）。按硬顺序：UF soft → MUST 合并 live/le2h+优先号 → 薄栏 6 条独立 KW → mentions 轮换子集 BTC / Starknet+DogeEVM → silent Elysium mentions。核心栏 KW 与 THIN official 因 tight 延后。DC 不登录，discordPeekDeferred=true。

## X 额度与查询

remainingBefore=147（UF1 首读后 remaining=146/1000 反推）。11 次读取后 remaining=136。

- UF1：0 条，remaining 146。0-based 1028 IgniteDotFun 起 packed 24（qlen 499），因 512 字上限 + alloc.uf=1 未拆第 2 次。walk 中 NF_skip 1：MOIbitcoin（1030）。walkScanned 25。lastKept 1052 KymaLiquidity。next 1053 beefdotfamily。
- MUST1：13 条，remaining 145。22 handles，qlen 464，mustSkip=[]。live/le2h + 7 个优先号（mobster_meme、machinedotfun、bscaidrop、PulseLaunchpad、localbottomcom、NutshellMarkets、starx_xlayer）合并为 1 次。
- KW_LZ：0；KW_TAPE：25；KW_GIWA：25；KW_DOGE：25；KW_BTC：18；KW_SN：7。薄栏六条全跑。
- MEN_BTC：1；MEN_SN_DOGE：0。
- SILENT_MEN（Elysium mentions，~24h）：25。
- 核心栏 KW、THIN official、其余 mentions（LayerZero / Elysium+kinetiq 等）延后。
- 禁止额外/重复 X 查询：本轮无补读、无「再确认」重拉、无雷达外探索。search_users 仍不在 X 目录，silent 只走 mentions，未把 silentCap 花在 bitcoincoreorg，也无第二轮 get_users_by_usernames。

## 十栏 / mentions / UF

- 十栏关键词：tight 只跑薄栏六条（LZ/Tape/GIWA/DogeEVM/BTC/Starknet）全到；核心栏 KW 延后。tenLaneKeywordsComplete=false。
- userFollowWatch：本轮分配的 1 片刷完（kept 24），userFollowWatchComplete=true（整表仍按游标轮转，未在本轮扫完全表）。
- mentions 本轮：BTC / Starknet+DogeEVM。下一轮：LayerZero / Elysium+kinetiq。
- silent 本轮：Elysium（按 R1878 任务书；1878%11=8）。下一轮：BTC（1879%11=9，按 R1870–R1876 与 x_budget.py 的 11 栏：0打新…7 GIWA、8 DogeEVM、9 BTC、10 Starknet）。注：R1877 交接把 8 写成 Elysium；本轮按任务书跑了 Elysium mentions，未跑 DogeEVM silent。
- fatNextStarts 保持 {agentPad:250, freeMint:277, bnAgent:114, elysium:197}。
- Watch 漏挂扫描（round≥1840）：0 leaks。
- soft-debt lastChecked 已刷新：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch。
- 勿把过期 nfSkipR1103 句柄当 NF（PulseLaunchpad、machinedotfun、mobster_meme、starx_xlayer 等仍在优先号里，本轮 MUST1 已覆盖）。

## 在库窗口（无新卡）

- **Bitsigil（@PlayBitsigil）——本轮通知事件**：官号 01:05 CST 宣布 SOLD OUT：https://x.com/playbitsigil/status/2122013244701475084 。OpenSea https://opensea.io/collection/bitsigil/overview HTTP 200，maxSupply=3333、totalSupply=3333、remainingSupply=0、isMinting=false。01:29 CST 官帖 FIRSTBOUND REVEALED，并指向 https://opensea.io/collection/bitsigil 。集合页 address `0x163cd6bbe7725a2e115af6777acfb4efd738ba3f`（Robinhood Chain）；官推本窗未亲自公布该 CA，按 OpenSea 页记录，标未验证。官网 bitsigil.xyz HTTP 200，仍为营销页、无 CA。FCFS 免费窗已在 R1875/R1876 通知；原定 02:00 CST 公售 $3 因已售罄未形成可打的付费公售，不要写成官方取消了 $3 政策。卡片 status=sold-out，le2h=false，focus=false，caUnverified=true。属已提醒窗口的售罄，须 notify。
- Q-TRON LAPTOPS（@qtronlaptops）：GTD 已按 R1877 已通知时间表开始（01:15–02:15 CST）。OpenSea HTTP 200，48/4444（剩余 4396；上一轮团队档结束为 44/4444），isMinting=false。分阶段时间、0.000526 ETH / 约 $0.95、allowlist 1806/2721、集合 CA `0x39f2484ab88ccb03b8b0f947e72705116a88e07f` 均未变。官号本窗仅有回复，无新规则。不重推。当前仍非公开免费 LIVE。FCFS/WL 02:15 CST，Public 03:15 CST。
- pillowbook-rh：01:00 CST 时钟已过。本窗官号无新帖。官网 pillowbook.pro 本轮 curl TLS unexpected EOF、WebFetch 500，未能复核页面；未见 CA/开盘证据，不得写成已开盘。已在 R1873 按首次 ≤2h 提醒，不重推。le2h=false。
- POLYROB：01:12 CST 关窗时钟已过。铸造页 https://6551.polyrob.dev/ HTTP 200，页面 “0 of 504” 仍视为 JS 占位，不覆盖此前 minted ~29–32；可见文案里的 sold out 只出现在失败原因说明，不能当成已售罄。本窗无新官帖。已在 R1873 提醒，不重推。le2h=false。
- DeadHood / jacketagent：已提醒窗口，本窗无新价格/CA/入口，不重推。
- DualForge / SpoxyFun / MicroFrens / osk-agent / hokiseries / ozero：仅刷新 lastChecked。
- animal-pharm：官号 @infamousScratch 01:09–01:10 CST 再次警告假号，并给出正统 OpenSea https://opensea.io/collection/animal-pharm-71884901 。不是新窗口，不通知。
- pipopad（@pipopadAPP，在库）：01:24 CST 官帖称官方代币 PIPO 已在 Elysium 主网上线，入口 https://pipopad.app/ 。推文写了 CA: 但短链解析为同一帖视频，正文未见 0x，不记录 CA。此为在库状态刷新，主通知事件仍是 Bitsigil 售罄，告警正文不展开。

## silent / 候选

- silent filter：seen=47，sentToReview=0，admitted=0，skipped=47（too_many_posts 34、already_in_library 10、no_product_signal 1、profile_unresolved 2=p2eabs / ZeroHoppersNFT）。
- deferredHandles：p2eabs、ZeroHoppersNFT 继续结转（0 帖空壳无新证据，不重录）。不要把下一轮 silentCap 花在 bitcoincoreorg。
- shortlist 28 及其他新作者：评论号、市场号、老号或弱账号（含 2.7h 新号 Emmanuel_Ogbe2，1 粉 1 帖，内容为转发）。无新官方项目卡。

## 推送

- 只提交 data.json、docs/data.json、RESULT_R1878.md 到 main。收藏未改。普通卡未设 focus。空轮芯片未造。本号不自动 mint。Bitsigil 售罄后 status 不再是 live，已写入 forcePanelIds，以免从精简面板掉出。

## 交接（R1879）

- lastFullAfterReset 保持 R1843。
- remaining 136 < 200，下一轮仍 tight（除非到 08:00 CST 后首轮全量补扫）。
- UF next：0-based 1053 / 1-based 1054 beefdotfamily。
- mentions next：LayerZero / Elysium+kinetiq（tight 先跑这 2 组）。
- silent next：BTC（1879%11=9）。search_users 仍不可用则只走 mentions；勿把 silentCap 花在 bitcoincoreorg。DogeEVM silent（canonical 8）本轮未跑。
- fatNextStarts 不变。
- 已提醒窗口不要因同一 ≤2h 再推：Bitsigil 本轮已通知售罄，不要把同一份 SOLD OUT/reveal/OpenSea CA 再推一遍；Q-TRON 分阶段+CA 已在 R1877 通知，GTD 按表进行中，FCFS/Public 若按同一时间表开始且无新规则则不重推，除非售罄、改价/改入口、官推已核验 CA，或出现与已通知内容不同的关键变化；pillowbook 同一未开盘窗口不重推，除非真正开盘并公布 CA；POLYROB、jacketagent、DeadHood 已提醒窗口无新变化不重推。
- DS 文案：本轮两次未给出完整 JSON 后本地定稿。下一轮判断/文案仍走 DeepSeek；失败才 dsFallback。
