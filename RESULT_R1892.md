# RESULT R1892

- time: 2026-11-16 08:36 CST (Asia/Shanghai)
- mode: post-reset-full（08:00 CST 后首轮全量补扫）
- lastFullAfterReset: **R1892**（取代 R1843；此后恢复正常节流，不得连续再跑第二次 post-reset-full）
- xReads: 30（main 29 + silent 1）
- remaining: 1000 → 970 / 1000
- softCap: 50，minSpend: 24，silentCap: 2（实际 silent 1 次，因 search_users 仍不在目录）
- notify: true
- newIds: cipher-syndicate
- dsFallback: false（录取/打分/文案一次 DeepSeek 回合法 JSON）

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit 5dd978e R1891）。R1891 在 08:00 重置前 near-exhausted（19→13）未做补扫；本轮约 08:28 CST 开火，是重置后第一轮，按 HANDOFF 强制 post-reset-full（`x_budget.py` 因 minute≥25 不会自动切到该模式，已手工覆盖）。

硬顺序：UF 分片软刷 → MUST live/优先号 → THIN official → 十栏关键词（薄栏+核心栏）全跑 → 全链 mentions 补扫 → silent 打新栏。DC 不登录，discordPeekDeferred=true。本号不自动 mint。

## X 额度与查询

remainingBefore=1000（UF1 后页脚 999/1000，确认日额已重置）。30 次读取后 remaining=970。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=29，打满 minSpend 24，未超 softCap 50。

- UF1–UF3：0-based 28 elysianfieldnft 起 packed 3 片 kept 76（25+25+26；hint 80，512 字上限只装下 3 批），wrap=false，walkScanned 94。NF_skip 14（ElysiumOutlaws / deadpacksol / blindfloor / blobsdotmeme / trytoprint / PlayFarmFi / reynarlabs / world_ygg / rektazhy59942 / 0xvernull / pearsdotfamily / battle_pad / cabaldotfun / project_hoodmon）。lastKept NookPadfun。next 118 BibblesHQ。
- MUST1：24 个 live+优先号；MUST2：仅 @starx_xlayer。mustSkip=[]。prio_in_shard=machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom；prio_folded=mobster_meme / NutshellMarkets / starx_xlayer。
- THIN official：5 片 106 号全读（THIN5=zerolotl / Zeroportalfun）。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-15T23:00:00Z；薄栏 KW 自 21:30Z（补 R1886 之后）；核心栏 KW 自 15:30Z（补 R1874 之后）；mentions 自 20:00Z（补 R1883 之后）。
- mentions 8 组全链补扫：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX / Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：1892%11=0 打新，SILENT_MEN 1 次 25 帖，sentToReview 0。下一轮 lane=挖矿。deferredHandles 结转 hyperhaul / p2eabs / ZeroHoppersNFT。不要把下一轮 silentCap 花在 bitcoincoreorg 或 StreetHoodMedia。

## 信号与结论

新录取 1：cipher-syndicate（@ciphersyndi）。跳过 WelcomeGTA6（Grok 托管 demo、无 CA、无真实 mint）、spek_on_sol（官网 PAPER/LIVE 均未开放，且为模拟盘）、Sent_moneyy（sent.money 已是在库 sent / @SentElysium）。

- **cipher-syndicate**（新收录，打新 / announced，overall 74）：官帖 08:31 CST 宣布 2026-11-17 00:00 CST（16:00 UTC）开铸。Stage 1 AL 免费 mint（444 cap）；Stage 2 与 Public 低于 0.0001 ETH。官网 ciphersyndicate.vercel.app、OpenSea 集合与 bio 均为 1,234 个 Robinhood 链动画像素实体；官帖写 10,000，以官网/OpenSea/bio 为准。OpenSea twitter_username 与 @ciphersyndi 互证；集合页合约 0xb89e3d465aa677e89cdf46b47db8d2b832e3fb97（非官推核验 CA），已有 total_supply 280。与已入库 @ciphersaints（ICP）不是同一项目。距开铸约 15.4h，非 ≤2h、尚未 LIVE。已进 userFollowWatch + freeMintWatch。按真新收录 notify。
- deadhood：08:27 CST 官帖 “Mint Out”，确认 R1885 起 777/777 售罄，不重推。
- hooja-fun：07:07 CST 回复 “Not yet, soon”，仍未开，不重推。
- shielded-wizards：07:52 CST “The Hoard of Ledgermaw is live” 为 R1873 已预告的 raid 任务上线，仍非公开免费 mint，不重推。
- hokori-quantum / wrapped-eth / animal-pharm：本窗为 R1891 已记内容（燃烧落地、会计示例、社交回复），不重推。
- zerolotl：08:09 CST 韩语介绍，称 Zero 主网在即，与 R1844 同一 announced 口径，非 LIVE，不重推。
- banknotes_btc / BROISAFREAK / Jumak_app：社交回复，无新窗口，不重推。

无 ≤2h 新窗口。Ink Legions 开铸仍为 2026-11-17 03:00 CST，非本轮 ≤2h。watchLeaks=0。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 118 BibblesHQ。
- mentions：全链 8 组已补扫；下一轮恢复正常轮换 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent：已跑打新；下一轮挖矿。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap。

## 不重推（沿用并补充）

- Cipher Syndicate 已按真新提醒；后续若只是同一份 11-17 00:00 CST AL/公售时间表、无改期/改价/改入口，不重推。临近 ≤2h 或开窗 LIVE 再提醒。
- deadhood 售罄确认不重推。
- hooja-fun 同一份 “Not yet, soon” 不重推，除非真正开窗。
- shielded-wizards 同一份 Ledgermaw raid 上线（非公开 mint）不重推。
- 沿用 R1891：Hokori 燃烧已落地但官网无用户入口、sapling 同一份 Jupiter 核验、$DATALOOM 付费查询尚未开放、wrapped-eth 会计示例且 /claim 仍 404、animal-pharm 已售罄社交回复、sunfall-world Season 1 结束预告。
- 其余已提醒窗口沿用 R1890：pillowbook 同一未开盘窗口不重推，除非真正开盘并公布 CA；jacketagent 已提醒付费阶段无新变化不重推；ozero 同一份 Base Sepolia 测试网宣传不重推，除非出现主网 mint；TapeMine 同一份 Behemoth 二期进度不重推，除非二期完成或新一期开启；raccoonslimestd 仍在选择发射台不重推；Elysium Portals 同一份 announced / 免费登记未见合约上线不重推；Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗；boxcars 已按免费驾照通知，进度/箱子奖励刷新不重推，除非预售开盘/改期、驾照售罄、改入口/改 CA。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint。
