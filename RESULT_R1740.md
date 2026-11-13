# RESULT R1740

- time: 2026-11-13 08:44 CST（Asia/Shanghai）
- mode: ample（R1739 已完成 08:00 CST 后首轮全量补扫，本轮恢复正常节流）
- notify: true
- xReads: 26（main 24 + silent 1 + admitVerify 1）；remainingBefore 970 → remaining 944 / 1000；softCap 28，minSpend 20，silentCap 2；未超 softCap，高于 minSpend
- admitVerifyReads: 1（@sharkverse_ 与 @useCashme 合并一次 get_users_by_usernames；未再重读时间线。官网 / OpenSea / 链上只读无 X 成本）
- tenLanes: true（薄栏 6 条 KW + 核心 KW 打新/台子/GO/Elysium + KW_GAPS_MINE squeek/Nutshell/仓鼠链/STARX/Agent ID/AIDROP/Pulse/computeroll + 挖矿词全跑；BN Agent 靠 fat agentPad/bnAgent）
- userFollow: 刷完本片 1213→1263，kept 50，skip 0，下一轮从 1263 续（UF 全表扫后 1574，本轮不是整表一次扫完）
- mentions: 本轮轮换已覆盖 Tape、GIWA、LayerZero、BTC、Starknet、DogeEVM，以及 rest Elysium/kinetiq、flap/Irys/Full.fun/Arc、squeek/Nutshell、STARX、PulseLaunchpad、dotaipad；mentionsThinDeferred=[]
- fat shards: agentPad 734→762 kept 28 skip 0；freeMint 77→107 kept 28 skip 2；bnAgent 249→280 kept 28 skip 3；elysium 163→192 kept 28 skip 1
- thin official watches: 92 unique，2 个 from: 批次，skip 1；含 starknet/LZ/btcPrivacy/btcCrc20/dogeEvm/tape/tapeOut/giwa/zeroWatch
- silentAccounts: ran=true，search_users unavailable，改跑 mentions（台子/Meme lane：launchpad / bonding curve）；未另开用户搜索
- discordPeekDeferred: true（DC 不登录）
- lastFullAfterReset: R1739
- DS: deepseek-flash thinking-on，成功；未走 dsFallback。新卡 focus 均为 false。未编造 CA/官号/官网。

## 可操作 / 通知

1. **SharkVerse（@sharkverse_）** — **新收录**，免费 LIVE，le2h=true，score 56（<70，但免费 LIVE 必须推送）。官帖 08:36:15 CST 宣布 First mint FREE。官网 https://sharkverse-zeta.vercel.app/ 与资料栏互核。链上 08:41 CST 读 NFT `0x7f68011aFF2766dCA686A741dcE68418446ddF99`：name=SharkVerse、symbol=SHARK、totalMinted=20/4444、paused=false；totalSupply() 仍 revert。每钱包第 1 只只付 gas，其后按该钱包铸数 0.00015 / 0.0004 / 0.0008 BNB，最多 30。配套 $SHARK token / Claim / Market 均为站点提供，未独立审计。官号创建于 2022-08-20，仅 3 粉、23 帖，存在旧号复用风险；页面模板与同日 Zodiac Fortune / Arctic Bear 高度相似。进 userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch。
2. **Zodiac Fortune（@ZodiacFortune_N）** — 已有卡，仍免费 LIVE，le2h=true。链上 08:41 CST：mintOpen=true，remainingFree 290→191，totalMinted 43→142/3333，paidPrice=0.0005 BNB。08:07 CST 另有一条官宣 LIVE 帖。官网 https://zodiac-fortune-dp8.pages.dev/ ，NFT `0x3293b29372Cdf7F073E544Ce4b0f44777c317000`（站点提供，未独立审计）。
3. **Arctic Bear（@arcticbear_nft）** — 已有卡（R1739 新收），仍免费 LIVE，le2h=true。链上已铸 19→34/5555，freeMinted=34，forgeLive=true。paused() 本轮 revert，因铸数继续增加按未暂停处理。官网 https://arcticbear.fun/ 。同模板风险仍在。
4. **JPEG Monkes（@jpegmonkes）** — 已有卡（R1739 新收），免费窗口仍至约 10:30 CST（≤2h）。OpenSea supply 735→896、owners 582→675、sales 950、floor 约 0.00167 ETH。CA `0x7ef4b5f6384e0f2030c2768e60338f4c2cf68f96`（robinhood，未独立审计）。
5. **CashMe（@useCashme）** — **新收录**，Solana 发射台刚 LIVE，score 50，真新故推送。官帖 08:30 CST 称 CashMe is live。官网 https://usecashme.fun/ 与资料栏互核。任意帖下 tag @useCashme + launch + ticker，约 1 分钟后币在 pump.fun 上线，CA 以 ME 结尾。官号约 07:12 CST 创建，4 粉；无独立 mint 窗口，不是免费铸造。合约未核，营销/钓鱼风险高，仅观察。进 userFollowWatch。

## 仍在跟（非 ≤2h）

- hood-terminals：付费公售仍 LIVE，OS 520/777，floor 0.001 ETH，sales 628，owners 352。08:32 CST 仅社区配色帖。
- boatn-fish：付费 Genesis 仍 LIVE，529/2222，wallets 41，现价约 0.01816 SOL。
- polyrob：08:03 CST 官帖再确认 12:00 UTC（20:00 CST）白名单锁定，两小时后开铸（22:00 CST）；距开铸约 13.3h。
- batterydotfun / raeto / Ape_CityRH：本窗无新官帖，维持原记录。
- OUTY（https://outy.pages.dev/）：免费铸造仍 LIVE 至 11-14 03:03 CST 或 1500 名额；官网仍无官推，**未建卡**。

## 本轮 skip（不够早期 / 非新机会）

- Tokenry / @tokenrytools：仅第三方 “I am in on Tokenry” 提及，本轮无官帖，未另开 X 重确认。
- @Xus_cazo “Introducing Curve”：非新官方针射台证据。
- Ammora 候补宣传（@AmmoraHQ 已在库 ammora）。
- rtp_fun、SentElysium、MonkoCoin / packswap_xyz、ShieldedWizBTC 等已在库或社区回复。
- 关键词/mentions 路人、pump.fun 信号机器人、评论号未建卡。

## 其它

- 本号不自动 mint（打新仍交 BAW 打新号）。
- 面板：https://reboot7454.github.io/early-scout/
- 新卡 2、candidates 4107；UF accounts 1574（+@sharkverse_ +@useCashme）
