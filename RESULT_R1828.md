# RESULT R1828（独立例行 pace）

时间：2026-11-15 02:05 CST。mode=pace。Discord 未占轮。notify=true（新收录 CoinFin 免费 Pass mint LIVE、0pad 免费 Early ID 登记；另收 KyCabal / Dogstarter / giwagmi）。未自动 mint。dsFallback=false。discordPeekDeferred=true（按惯例 DC 不登录）。

## 额度与覆盖

- xReads 24（main 22 + silent 1 + admitVerify 1），remainingBefore 245 → remaining 221/1000。开跑 x_budget 曾报 388，以首读工具回包为准：UF1 后 remaining 244，故 remainingBefore=245。开跑模式 pace（softCap 25，minSpend 18，silentCap 2）。因 remaining 245≫200，十栏+必扫链关键词跑全，并刷了薄栏官号 from:×4。
- 分解：UF shard×2 + MUST×1 + 薄栏 Watch from:×4 + 薄栏 KW×6 + 核心栏 KW×5 + mentions×4 + silent×1 + admitVerify×1。官网 / HTTP / 链外只读无 X 成本。同一 handle 本轮只拉一次，未为再确认重读。write_to_file 对部分 KW/silent 大结果截断，已从邻近完整工具回包按 remaining + 首条 author_id 恢复，未因此重拉同一查询。
- UF / MUST / 关键词 / mentions start_time=2026-11-14T17:20:00Z；薄栏 Watch from: start_time=2026-11-14T17:35:00Z；silent mention start_time=2026-11-13T17:58:25Z。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。search_users 本轮仍不在 X 工具目录，silent 仅 mention 路径。
- lastFullAfterReset 仍为 R1792。十栏关键词已跑全。fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。未刷四表 FAT 分片。
- UF 库表 walk 从 cursor 388 kept 48 skip 17 已知 NF（bsc_bito / tikitotemsbnb / seppidev / CachetDotFun / Nonce_CTO / claudesprotocol / wedowtf / manekinecoinft / stonkaxyz / BabelAgent / TurboKartBNB / wuseagent / grepfi / SwarmHiveBNB / twinmetahq / astrispace / ChyAI_Official），next cursor 453，未回绕。优先软刷 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer / mobster_meme 折入本轮。UF 两批 512 字溢出，将分片末三号 IdentideXYZ / daimonsHQ / mimiai_web3 折入 MUST，未开第三趟 UF 读。新卡补挂后 UF 账户数随 5 个官号增加。
- mentions 轮换本轮：Tape / GIWA / BTC / Starknet+DogeEVM（Tape 0、GIWA 1、BTC 0、SN+Doge 1）。SN+Doge 命中 dogstarter 挂靠 @DogeOS，已收录。下轮轮换子集：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent 栏 1828%11=2 → 台子/Meme；search_users 仍不在工具目录，仅 mentions。hits 20，sentToReview=kycabal / 0pad / coinfin，三张均收录（kycabal 为官号盲捞；0pad、coinfin 由第三方领取/评论线索补核验，admitVerify 消耗 1 次 get_users_by_usernames）。
- Watch：coinfin 进 UF + agentPadWatch + bnAgentWatch + freeMintWatch；0pad 进 UF + layerZeroWatch；kycabal 进 UF；dogstarter 进 UF + dogeEvmWatch；giwagmi 进 UF + giwaWatch。round≥1790 卡均已在至少一个 Watch。软债 canton/glaze/tokenWorks/flap lastChecked 刷到 02:05 CST。

## 本轮收录

- **coinfin**（@coinfinfun，打新，BNB Chain，live，overall 84，focus=false）— 官号 2026-10-31 10:27 CST 建立，未认证，12 粉 12 帖。官网 coinfin.fun HTTP 200，与官推互链。Pass NFT CA 0x5877D2bb9F226cC3E438F4d656cAeb27DEAFC576（Sourcify exact match，name=CoinFin Pass）。链上 mintOpen/claimOpen 均为 true，totalMinted=1650/10000，launchCount=0。官网页写 FIRST MINT FREE，档位 0 / 0.0002 / 0.0004 / 0.0008 BNB，每钱包最多 20，需 Agent ID。$FIN CA 0xB4C9efA5f217a75f48F3f58508ca1D70Df0d8CF4。本轮关键词未直接扫到官号，由 silent 评论线索+官网+链上核验补收。免费 Pass mint 已 LIVE，必须通知。合约仍按站点+Sourcify 标注 caUnverified。未自动 mint。
- **0pad**（@0padfun，LayerZero，live，overall 74，lzVerified=true，focus=false）— 官号 2026-10-17 03:01 CST 建立，未认证，8 粉、0 帖（静号）。官网 0pad.fun HTTP 200 与官推互链；bio 与官网均写 built on LayerZero。免费 Early ID 领取已开（0 IDs verified，Mythic 剩 50、Legendary 剩 100），主网倒计时 SOON、无具体日期。无代币 CA。属于免费登记窗口，必须通知。由 silent 领取帖提及后 get_users 核验补收。
- **kycabal**（@kycabal，台子/Meme，NEAR，testnet，overall 55，focus=false）— 官号 2026-11-13 09:41 CST 新建，未认证，0 粉 4 帖。官帖 01:54:11 CST 宣布 NEAR memecoin launchpad（黑客松项目）。官网 kycabal.fun HTTP 200，页面写明仅 NEAR 测试网、主网数据为模拟；官网 HTML 未回链官推。silent 栏盲捞到官号。DeepSeek 原判 skip，按极早期官方新台以 testnet/watching 收录。
- **dogstarter**（@dogstarter，台子/Meme，DogeOS / zoneHint=DogeEVM，testnet，overall 62，focus=false）— 官号 2026-10-19 14:21 CST 建立，未认证，203 粉 2 帖。官网 dogstarter.dog HTTP 200，测试网可交互（水龙头 + 发币/ape），毕业到 DogSwap 并锁 LP。资料栏指向官网，静态 HTML 未见回链。本轮同时命中 DogeEVM / 台子关键词和 @DogeOS mentions。DeepSeek 原判 skip，按极早期官方新台以 testnet 收录。
- **giwagmi**（@giwagmi，GIWA，watching，overall 60，focus=false）— 官号 2026-09-27 00:00 CST 建立，未认证，15 粉 5 帖。官网 giwagmi.fun HTTP 200 与官推互链。页面明确 Coming soon，opens after GIWA mainnet；Sepolia 合约已开源验证，主网日期未公布。GIWA 关键词盲捞。DeepSeek 原判 skip，按极早期官方新台以 watching 收录。

## 在库进度（不重推）

- shinob-rh：官帖 01:48:03 CST 宣布供应 10,000→4,000，称 only about 100 left。OpenSea 核验 total_supply=3883、owners=283、floor=0.000144 ETH。已按 R1827 首次免费 LIVE 通知，本轮仅减供/进度，不重推。
- punchin：官帖 01:41:52 CST 称 105/500 MINTED，免费 Pass 仍 LIVE、每钱包 1 份、需 Agent ID。已按 R1815 通知，仅进度 96→105，不重推。
- jacketagent：仍 117/500、免费剩余 383、免费结束 11-16 00:00 CST，与 R1827 相同，不重推。
- puppet-pro：官方 CA 仍为 0x8665c107cbc661d314635b37a12f93fbfb419129，不重推。
- polyrob：一口价 0.033 ETH 仍至 2026-11-16 01:12 CST，不重推。
- meow-cards / qtronlaptops：无新的首次可操作窗口（qtron 时钟仍 11-16 01:00 CST），不重推。

## 关键词 / mentions 摘记

- 薄栏与核心栏 KW 均已跑（部分回包经 Full text 恢复）。新号 dogstarter 由 DogeEVM/台子 KW 与 mentions 交叉命中；giwagmi 由 GIWA KW 独立盲捞。0pad / coinfin 官号本窗无自帖，靠 silent 第三方线索补收。过滤：已在库 PunchIn / Jacket / Puppet / Shinob / Polyrob 进度帖；VelixaWeb3 仅 RT 抽奖、无本轮官方核验；TheGlowinGold 指向已在库 PlayPixelora，不预推；RebootOnBase 为已上线 Base 币；评论/垃圾号未收。
- mentions：Tape / GIWA / BTC / Starknet+DogeEVM 本轮已扫；LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX 按轮换留给下轮。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1828.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：请父代理向用户转发 CoinFin 免费 Pass mint LIVE、0pad 免费 Early ID 登记，以及 KyCabal / Dogstarter / giwagmi 三张新台。shinob-rh / punchin / jacketagent / puppet-pro / polyrob / meow-cards / qtronlaptops 不重推。

## 未做 / 交接

- 未自动 mint。
- search_users 仍不可用，silent 仅 mention。
- lastFullAfterReset 仍 R1792；下轮保持 pace，08:00 CST 后第一轮仍须全量补扫。
- 下轮 mentions 轮换：LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。UF cursor=453。silent 下轮 1829%11=3。
