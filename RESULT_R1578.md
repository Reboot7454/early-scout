# R1578 early-scout RESULT（2026-11-10 16:48 CST）

- round: R1578
- pushSha/tip: TBD
- mode: ample softCap=28（lastFullAfterReset=R1555，非 post-reset-full）
- xReads: 13 | remainingBefore: 719 → remaining: 706 | ufCursor: 764→780
- lastFullAfterReset: R1555
- 编号说明：本轮主扫开跑时基线仍是 R1576；Discord alpha 补漏已于 16:27 CST 占用 R1577（新收 on-aether-app、thyrk、ticksdotcom、useleasehold、elyxpaid、longcat、usehedgefun）。主扫改记 R1578，保留上述 7 张卡，并将其 newThisRound 清掉；同时把这 7 号补进 UF（on-aether-app / ticksdotcom 另进 elysiumWatch）以修 watch-bug。
- newThisRound: ely-kitties（@ElyKitties，官网 https://elykitties.xyz/ ，16:26 CST 白名单已开，2,222 全链上 Kitties，Free Mint 未开闸、无 CA，Elysium 明确部署）；volta-gent（@VoltaGent_io，官网 https://voltagent.site/ ，16:05 CST 正式开 Mint，BSC CA 0x43cfeb5267125c4f3495d48dea202a7fc43bc5b1，智能体阶段 0.0001 BNB/个、前 1,000 个、每钱包最多 2 个、需币安 Agent ID，≤2h 至约 18:05，智能体阶段约至 23:03）；hamster-tower（@hamstertowersqk，官网 https://www.hamstertower.site/ ，Squeekchain/Sepolia 测试网爬塔，No Token、无铸造窗，非 Elysium）
- 状态升级：agentix-agx 16:22 CST 官帖公布 Token 0xC605d34A06B614224785f1119146a710A83C5A44、Minter 0x11a367d5E827132AC4CAD6a4C41c797C1e4D4E7A、Invite NFT 0x7a8134aBCb75FA7913194986c644457D2C1596e8，称 Minting is live now，窗至约 17:46（去掉暂无CA）；agent-feg 16:16 CST 官帖确认 17:00 CST 开铸、每 ID 10 份，CA 未变；dogeking-agent 16:23 CST 官帖确认 19:00 CST 开售，前 1,000 份 Agent ID 免费，之后 0.002 BNB；mint-condition / 99901-fun 本轮无新帖
- ≤2h 仍开：agentix-agx 至约 17:46 CST（Token CA 0xC605d34A06B614224785f1119146a710A83C5A44）；mint-condition 至约 17:22 CST（CA 0x44ae81d76bea638c52ed0ae71302d1a332a22577）；agent-feg 至约 17:00 CST（0.005 BNB/份，CA 0x8743fa8b279D1b85506c5cd223Bd40285d32a2dA）；volta-gent 至约 18:05 CST（CA 0x43cfeb5267125c4f3495d48dea202a7fc43bc5b1）
- 尚未≤2h：dogeking-agent 今晚 19:00 CST 开售（约 17:00 CST 起算入窗）；99901-fun 21:00 CST liftoff（约 19:00 CST 起算入窗）
- dsFallback: False（deepseek-flash thinking on；admit 3 / skip 3：postmark、hypelaunches、pipermeme；首次 admit 因思考占满 4096 无 JSON，已 8192 重试成功）
- discordPeekDeferred: False（本轮主扫跳过 Peek；R1575 已于 15:26 CST 做过一轮，且 R1577 Discord 补漏已于 16:27 CST 落地）
- docsSynced: True
- notify: True
- alert: 【R1578】三枚新收录：Ely Kitties（@ElyKitties）2,222 个全链上 Kitties、Free Mint，目前仅白名单申请开放，无 CA、铸造未开；Volta Gent（@VoltaGent_io）BSC 已开铸，CA 0x43cfeb5267125c4f3495d48dea202a7fc43bc5b1，智能体阶段 0.0001 BNB/个、限前 1,000 个、每钱包 2 个、需币安 Agent ID，≤2h 至约 18:05（之后所有者调用 endAgentPhase() 才进公开阶段，非整场 18:05 结束）；Hamster Tower（@hamstertowersqk）为 Squeekchain / Sepolia 测试网爬塔游戏，明确 No Token、无铸造窗。

库内升级：Agentix 官帖公布 Token 0xC605d34A06B614224785f1119146a710A83C5A44、Minter 0x11a367d5E827132AC4CAD6a4C41c797C1e4D4E7A、Invite NFT 0x7a8134aBCb75FA7913194986c644457D2C1596e8，称 Minting is live now，窗至约 17:46。仍在≤2h：mint-condition 至约 17:22（CA 0x44ae…2577）、agent-feg 17:00 开铸（CA 0x8743…a2dA）、Volta Gent 至约 18:05。尚未入窗：dogeking 19:00、99901 21:00。

面板：https://reboot7454.github.io/early-scout/
- HashDoge/Genius/Corla/Flap: STOPPED
- tenLanes: UF764→780 + must/≤2h 合并 from: + KW 九栏+BTC/Starknet + mentions Zero/@zerodotnetwork+LayerZero_Labs×1（窗内 0 命中，未探索性重读）；九栏+BTC/Starknet/GIWA 均跑
- UF shard 764–779：16 槽；skip NF/SUSP 不连刷：@mint_WRIT、@BinanceCanFly、@Meteorszmint、@AiPullpad；可见 12 槽全部已在库；本窗仅 @Nemotrontrade、@ElysiumPunks 有帖
- skips/noise: postmark（站点无官推、合约待部署）；HypeLaunches/@HypeLaunches（promo 号，链接通用 pump.fun）；pipermeme/@pipermeme_（仅第三方等名单，本窗无官推主帖）；Ammora GIWA 等名单噪音；个人 Kurogane 白名单喊单；globemkts 推荐噪音；通用 in a nutshell / UCO / circuit-board LLM 新闻假阳性
- watch 补进：ely-kitties → userFollowWatch + elysiumWatch；volta-gent → userFollowWatch + agentPadWatch + bnAgentWatch；hamster-tower → userFollowWatch（追加在表尾，不插入中段以免光标错位）
- softDebt lastChecked 已刷新：cantonWatch / cantonPadWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch
