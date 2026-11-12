# RESULT R1726

时间：2026-11-13 02:49:56 CST（Asia/Shanghai）
仓库：Reboot7454/early-scout
面板：https://reboot7454.github.io/early-scout/
notify=true
discordPeekDeferred=true（本机未登录 Discord，Peek 跳过）

## 与 R1725 的关系
并行 tight R1725 已于 02:46 CST 推送（sha a464e8e / verified 36d3757），采用 remainingBefore=91、softCap=10，推迟核心 KW / mentions / 厚表分片，结论为「无新收录」，并因 clover-rh ≤2h 将 notify=true。
本会话（本例行 02:34 CST 开火）开跑时官方 footer remainingBefore=975，按 ample 跑完全栏，已核到 ORYN 免费 mint LIVE 等 4 张新卡。不以 91 为日额结论。本轮以 R1726 补收，不改写 RESULT_R1725.md。下一轮开跑必须重核官方 footer。

## xQuota
- xReads: 31（主路径 30；静号 1 次，不占 softCap）——为本会话 ample 扫描计数，不含 tight R1725 的 10 次
- remainingBefore: 975（官方 footer，ample）
- remaining: 944（主路径结束后 945，静号后再 944）
- mode: ample-supplement
- softCap: 40
- minSpend: 20（已满足）
- silentCap: 2
- ufCursor: 记为 420→454（本会话实际从 380 扫到 454，与 R1725 的 380→420 重叠，不回退；kept 50，skip 24 已知坏号不重读；下一轮从 454 续）
- tenLanes: yes（薄栏 6 + 核心 KW 5 全跑）
- kwCoreRan: 打新, 挖矿, 台子/Meme, GO盘, Elysium
- kwCoreDeferred: 无
- mentionsThin: GIWA, Tape/电路（0）, LayerZero, DogeEVM（0）, Starknet（0）
- mentionsRest: Enter_Elysium, squeekchain, NutshellMarkets, starx_xlayer, PulseLaunchpad, flapdotsh
- mentionsRestOmitted: irys_xyz, fulldotfun, arcxtrade（本轮合并 rest 未单独扫）
- fatShards: 已推进（R1725 未推进）agentPad 301→326 / freeMint 65→90 / bnAgent 128→153 / elysium 86→111
- nAccounts 写入后：agentPad 763 / freeMint 375 / bnAgent 284 / elysium 270
- userFollow 软刷完成
- search_users_unavailable: true（未伪造用户搜索）
- 无探索性重试、无翻页、无同号重读
- lastFullAfterReset: 仍为 R1692
- userOrderedFull: 仍为 R1715

## silentAccounts
- ran: true
- lane: BTC
- index: 9
- search_users_unavailable: true；第二槽 BTC mentions：`has:mentions (Ordinals OR CRC20 OR ShieldedNaka) (mint OR launch) -is:retweet`，start_time 约 2026-11-11T18:37:40Z，result_count=15，未翻页
- admitted: 0
- 跳过：Bitcoin Cyborgs 为长时间运行的 Ordinals mint「最后一天」，非早期；BLOCKFOLK 为第三方约 11 小时前宣传；RGBHorse / ShieldedWizards / BabySealsCRC 已在库，无新精确窗
- 注：tight R1725 因 silentCap=1 未跑第二槽

## 新收录（4）——补收
- oryn-family / @oryndotfamily / score 86 / zone BN Agent 钱包 / status live / le2h=false
  官网 https://oryn.family/：$ORYN 在 BSC mint LIVE。免费路径：每 Agent ID 本轮 1 次领取（仅 gas），已领 10/5,000；付费路径：0.0014 BNB/lot，1 lot=1,100,000 ORYN，每 ID 最多 9 lot，本轮 0/2,000 售出。Token 0x9599fd07ad1de244ede8e11680102d96988702f8，Mint(OrynSafuMintV2) 0x96135a41fa155752dc7154cdcaa480f2fbec1493（站点标注，未独立审计）。页脚 last verified on-chain 11 Nov 2026，不能认定开窗≤2h，但免费 mint 确为 LIVE → 必须 notify。focus=false。因本轮部分 X 结果落盘截断，未写入官帖 status id，链到官网与官号主页。
- soom / @soomdotfun / score 58 / zone GIWA / status announced
  建号约 11/13 00:21 CST，粉 1。自称 GIWA 全量发射台，官帖仅 Soon。soom.fun / soomdot.fun 本轮超时或 TLS 失败，不编造官网。
- chain-pad / @ChainPadApp / score 67 / zone 台子/Meme / status live
  建号约 11/13 01:56 CST，粉 0。官网 https://www.chainpad.one/ 已上线：pump.fun 发射 + 约 60 链代币背书，自称无平台费。无 mint 窗、无已核发射案例。官帖 https://x.com/ChainPadApp/status/2120940941565714832
- elyzor / @Elyzor_nft / score 65 / zone Elysium 生态 / status live / 付费 mint（非免费）
  官帖 Mint Alive，0.0031 HYPE，5555，即时 Reveal，链 Elysium。官网 elyzor.xyz 极薄。OS 合集 created 2026-11-12，合约 0xe26c39d60709b870fce8e7ee359ad52fe6b7861a，当前约 20 枚。不能证明开窗≤2h。https://x.com/Elyzor_nft/status/2120947264302555551

## skip
- peg-launch / @PegLaunch：官网 peg.cx 近乎空页，除 bio 外无可验证产品，DS admit=false（overall 30）
- Bitcoin Cyborgs / BLOCKFOLK：非早期或非官号一手，见 silentAccounts
- launchonmono / Talus_Pad 等弱第三方线索未收录

## 更新
- clover-rh：仍 ≤2h，窗口至约 04:00 CST。01:51 CST 后无新官帖。官帖 CA 与旧 CA 及 DexScreener 差异同 R1725 再核（官帖 CA 仍 0 对；旧 CA 仍见 4 池）。粉丝 KEEP 3994。
- zerva / @ZERVA_HQ：官号称今日 launch 失败、代币暂扣、团队处理中。窗口已过，le2h=false，粉 KEEP 54。
- farm-filch：窗口已过，仅刷 lastChecked，le2h=false。
- Canton/Glaze/TokenWorks：soft-touch lastChecked，无新 admit。
- 保留 tight R1725 已写入的粉丝上调（globemkts 775 等），本轮不再下调。

## 监控 bug 修复
clover-rh / @cloverdotfamily 与 farm-filch / @FarmFilch 已在库但不在任何 Watch。本轮补进 userFollowWatch + freeMintWatch。
新卡 Watch：oryn-family → userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch；soom → userFollowWatch + giwaWatch；chain-pad → userFollowWatch + xChainPadWatch；elyzor → userFollowWatch + elysiumWatch。

## 粉丝上调（仅升不降）
不回退 R1725 已写入的 globemkts 765→775、solz-money 4→106、tokentunes 2985→3069、madang-fun 519→520、gasokfun=189。clover-rh KEEP 3994。新卡按本轮可见粉丝写入：oryn 19、soom 1、chain-pad 0、elyzor 3。

## 本轮结论
R1726 为 ample 补收。新收 4 张卡，其中 oryn-family 为免费 mint LIVE（另有付费批次须写明），必须 notify；clover-rh 仍在约 04:00 CST 的 ≤2h 窗口。elyzor 为付费 mint。candidateCount 4065→4069。新卡 focus=false。未自动 mint。已同步 docs/data.json。

## dsNote
deepseek-flash thinking-on。第一次经 ds_batch_score.py 的解析失败（模型输出未能被 extract_json 吃进）；第二次直接 deepseek_chat 得到完整可解析 JSON，未走 dsFallback。admits=oryn-family 86、chain-pad 67、elyzor 65、soom 58；skip peg-launch 30。新卡文案以 DS highlights/drawbacks/reason 为准，ORYN 双路径与 Elyzor 付费属性按证据保留。

## alertMessage
🔔 R1726 补收：ORYN 免费领取已 LIVE（每 Agent ID 本轮 1 次、仅 gas，已领 10/5000；另有付费 0.0014 BNB/lot）。Clover $CLV 窗口仍至约 04:00 CST，官帖 CA 与旧 CA 不一致、DexScreener 暂只索引到旧地址的池。另新收 soom（GIWA 预告）、Chain Pad、Elyzor（Elysium 付费 NFT 0.0031 HYPE）。面板：https://reboot7454.github.io/early-scout/
