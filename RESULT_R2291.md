# RESULT R2291

- 时间：2026-11-27 19:10:00 CST（Asia/Shanghai）
- 仓库：Reboot7454/early-scout，面板 https://reboot7454.github.io/early-scout/
- 模式：X 雷达（tight）。写盘前 git pull，远程仍是 R2290（ba60a11），本路升为 R2291。开火时钟按 19:00 CST 计算 ≤2h，不因写盘稍晚提前报窗。
- notify=true（库内 Lamoryant 官宣本轮 1000 份 OpenSea 铸造已 LIVE。无新收录。Bonebloom / BlockPay / RuninAI 窗口仍在，此前已提醒，不重报。）
- DeepSeek：本跑仍 HTTP 401 invalid api key（request_id 691d9039-eb3f-45d2-8b53-c39ca479d3ea），判断/文案/打分为本地兜底（dsFallback=true），未改用高成本模型，未再重试 DeepSeek。
- X 额度：remainingBefore=177，remainingAfter=158，xReads=19（UF 优先片 1 + UF 分片 2 + MUST 1 + 核心合并 KW 1 + 瘦栏 30m 6 + 瘦栏 24h 2 + mentions 4 + 静号 1 + 官号核验 1）。mode=tight，softCap 10，minSpend 10，177<200。十栏仍覆盖：瘦栏 6 条独立 30m + 核心栏（打新/挖矿/台子/GO/Elysium/BN Agent/STARX）合并 1 条，未整栏跳过。未刷厚表分片（agentPad/bnAgent/elysium/freeMint nextStart 未动）。已知 NF 的 @mobster_meme / @starx_xlayer 跳过不连刷。无分钟顶重试浪费。
- UF：优先片查询 5 个（@machinedotfun @bscaidrop @PulseLaunchpad @localbottomcom @NutshellMarkets）；已知 NF 的 @mobster_meme / @starx_xlayer 跳过不连刷。优先片 45m result_count=0。分片 944 @GardenEcosystem 起 walk 43 kept 40 至 986 @SuperAgentPass，2 批 20+20；跳过 3 个已知 NF：kpin_ai / LostGodsOnRH / topaaafun。与优先片去重。kept=40，queried=40，NF_skip=3，wrap=false。分片命中：@UnseenOrdo 多则 RGBStone/UNSEEN 白名单回复（已在库，不按新免费 LIVE 处理）；@VoidCashio 终端仍 live（已在库，不重推）。下轮起点 987 @GLOAMMAIL。UF_LEN=2586。userFollow 本片已刷完。
- 十栏关键词：核心栏 tight 下合并为 1 次 30m（打新/挖矿/台子/GO/Elysium/BN Agent，STARX/X Layer 折入），瘦栏 30m 六组均已跑。瘦栏 30m 命中 LayerZero 0、Tape 15、GIWA 25、DogeEVM 10、BTC 0、Starknet 5。LayerZero/BTC 均 <5，同轮各补 1 次 24h（均为 25；有 next_token 未再翻页）。Tape/GIWA/DogeEVM/Starknet 未补 24h。
- mentions 本轮：Elysium+kinetiq / LayerZero / pads+squeek+STARX / BN+STARX（命中 25/23/25/2）。下一轮：Tape / GIWA / BTC / Starknet+DogeEVM。
- 静号：按 R2290 silentNext 跑 BTC。本连接器无 search_users，ran SILENT_MEN_BTC 24h（n=23，ok，未再翻页）。本地筛 sentToReview=0，admitted=0（均为已在库转发、个人号或非极早期）。未为未解析档案再开探索读。silentNext=Starknet。
- 新收录：无。meta.newThisRound == 顶层 newThisRound == round2291Added == []。
- 状态更新（非新卡；仅 Lamoryant 开铸官宣计入本轮 notify，其余不重推）：
  - lamoryant / @Lamoryant：官帖 2026-11-27 19:00:04 CST（https://x.com/Lamoryant/status/2126269824334495760）宣布 LAMORYANT MINT IS LIVE，1000 份，instant reveal；随后一则称昨日铸造资金将回流承接今日铸造。OpenSea https://opensea.io/collection/lamoryant- 显示 Minting now，128/1000，持有 75。阶段：Team Free（allowlist，10/钱包）、OG Free（allowlist，1/钱包）、白名单 0.001 ETH（10/钱包）、公售 0.0012 ETH。不是面向全部钱包的免费公售。官网铸页仍显示倒计时与 0/1000，以官帖和 OpenSea 为准。此 1000 份与此前 Robinhood 原合约 698/1356（CA 0x3F296B91132aa82B84b116Cf31a15e957a958B2c）分开记录，不以 128 覆盖旧链上数字。计入本轮 notify。
  - bonebloom / @AbyssLabsNFTCol：预售仍 2026-11-27 20:30 CST，开火 19:00 CST 计约 1.5h，MUST 本窗无新官帖，未见改期，不是免费 mint，尚未开铸。R2290 已按首次进入 ≤2h 提醒，不重推。
  - blockpay-genesis / @BlockpayGenesis：免费 mint 仍 LIVE，截止仍 2026-11-27 20:00 CST，开火 19:00 CST 计约 1.0h，本窗无新官帖，R2269 已提醒，不重推。
  - runin-ai / @RuninAI_com：本窗多则官帖仍预告每日 20:00 CST $RMINE，CA 仍 0xfB50746BCc9D585AEb49cd410Fa0100b657ce9e6，开火 19:00 CST 计约 1.0h。每日窗 R2226 已提醒，不重推。
  - outlawsxnft / @OUTLAWSxNFT：本窗多为资格查询回复，未见改期/开铸。首阶段仍 2026-11-27 21:30 CST，开火 19:00 CST 计约 2.5h，未到首次 ≤2h，不是免费 mint LIVE，不重推。
  - outrider / @outrider_fi：本窗无新官帖。$OUTR 仍 2026-11-27 23:00 CST，开火 19:00 CST 计约 4.0h，不重推。
  - lumixpad / @lumixpad：本窗无新官帖。既有窗口仍约至 2026-11-28 00:33 CST，开火 19:00 CST 计约 5.5h，未见改期/开铸，不重推。
  - enter-the-manga / @EnterTheManga：本窗 MUST 无新官帖。白名单免费铸造仍按 R2288 记录，公开轮仍 2026-11-28 16:30 CST，不重推。
- 拒收/推迟（dsFallback 从紧，不确定不收）：@polysiumevm（今日建号，0 粉 / 1 帖，资料栏无官网，仅视频自称 Elysium 预测市场，过瘦不收，不进 Elysium 栏）；@privacycashfun / privacycash.fun（官网互证官号 2026-06-22 建号、523 粉 / 70 帖、已认证，非极早期；本轮关键词命中的是小号 @privacycashdotf，未张冠李戴建卡）；@TheEyesBTC（第三方称 Ordinals free mint，本轮未核官帖/官网，未另开探索读）；Agent Operators（cryptoplay.guide/nft 自称 .ai Agent ID 免费登记已开、截止 11-28 20:00 CST，本轮未见独立可核官推，未收）。打新栏多为已在库项目的 KOL 转发（Bad Ape @artnesh、KISMO、NULLKIN、FOOME、The Boys 无独立官号）。LaunchZero / XofN 已在库。UNSEEN/RGBStone 已在库，不按新免费 LIVE 处理。
- Discord：discordPeekDeferred=true。本轮 X 雷达未开浏览器（优先写盘推送 Lamoryant 开铸）。沿用 R2288 lastSeenByChannel（alpha-3 17:58、backup 17:55、smart 17:24、alpha-1 17:55）。积压缺口仍在：alpha-3 11-23 22:55→11-27 05:20；smart 11-23 22:56→11-25 00:25；alpha-1 11-23 22:19→11-25 20:50。backup 已过 cutoff。本轮未改 lastSeen，未补扫积压。父代理须同一轮补 Peek。
- 监控补挂：无新卡。状态更新卡均已在 UF 及对应栏 Watch。未加入 forcePanelIds（未改 focus/focusIds）。Canton/Glaze/TokenWorks 软债 lastChecked 已刷新。厚表 nextStart 未因未读而改动。在库 Watch 漏挂 r>=2200 检查为 0。

- 推送：见 commit（本文件与 data.json / docs/data.json 一并推送）
