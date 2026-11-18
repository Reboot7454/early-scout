# RESULT R1938

- time: 2026-11-18 20:11:26 CST
- mode: ample（正常例行，非 post-reset-full；lastFullAfterReset 仍为 R1926）
- xReads: 25（main 23 + silent 1 + EXTRA 1）
- remainingBefore: 693 → remaining: 668
- softCap 30 / minSpend 20 / silentCap 2
- tenLanes: yes（11 条关键词全跑：LZ 1 / TAPE 25 / GIWA 25 / DOGE 25 / BTC 10 / SN 16 / MINT 25 / MINE 19 / PAD 25 / GO 25 / ELY 25）
- userFollow: 刷完本分片。start 1084 hyperlendx，kept 49（hyperlendx→hermeslaunchbot），NF_skip 0，walkScanned 49，wrap=false，无尾部 NF。next 1133 0RV1A。mobster_meme 因多次 NF 本轮未连刷（关键词侧已覆盖）。本分片 UF 帖 UF1=2 / UF2=0。
- mentions: 本轮 4 组 LayerZero 25 / Elysium+kinetiq 25 / mining-squeek+Nutshell 2 / BN Agent pads+STARX 9。下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent: LayerZero（SILENT_MEN 25；search_users 仍不可用）。下一轮 Tape/电路。
- watchLeaksFixed: []
- fat cursors 未动：agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283
- discordPeekDeferred: true（DC 未登录）
- newThisRound: [agentseat]
- notify: true（真新收录 AgentSeat/$SEAT 付费 LIVE）

## 本轮判定

DeepSeek（deepseek-flash，思考开启）admit AgentSeat（$SEAT / @agentseatlol），overall 72，focus=false。notify=true。

- **AgentSeat / $SEAT（@agentseatlol）**：真新收录，付费 LIVE，非免费 mint。官号 2026-11-09 创建、0 粉、仅 1 帖；首帖 20:01 CST（https://x.com/agentseatlol/status/2123023695182512288）公布 CA。官网 https://agentseat.lol/ HTTP 200，资料栏 URL 展开后与官网互证（页面无 twitter:site meta）。产品是 flap.sh / gang.fun「仅 Agent ID 可参与」发射的前排座位拍卖：1 个出借的 Agent ID=1 个座位，后面最多 5 名出资人；一次 BNB 支付=买入额+溢价，落选全额退款，出借人拿该排 50% 溢价；持有 ≥1,000,000 $SEAT 可获点名场次优先出价窗。链上代币 0xe0cabe31be5f7f5c84b5f6a5169565724f057777 name=AgentSeat / symbol=SEAT，总量 10 亿，bytecode 约 45 字节（像最小代理），owner 0xe2ce6ab80874fa9fa2aae65d277dd6b8e65c9de0。Flap 可买：https://flap.sh/bnb/0xe0cabe31be5f7f5c84b5f6a5169565724f057777?lang=en 。API config chainId=56，escrow 0x82c2aa0a229288caffacd64e696a39c214402679，vault 0x25f60A78755AC4883eBC3901b57b7d54669DcBd9，agentId 注册 0x60B9262456dE011F7d15a54CdD8c48bAaa8B022F；minBuy 0.01 / maxBuy 2 / minPremium 0.001 BNB。/api/drops 显示两场自 18:15 CST 开放的「下一场」坑：flap 1 笔 pending 0.01+0.001 BNB，gang.fun 0 笔，尚未绑定具体发射。合约未完整审计，caUnverified=true。已进 agentPadWatch + bnAgentWatch。本号不自动 mint。
- **AONE / @aone_agent**：同一已提醒免费 LIVE 窗口，只更新进度，不重推。链上 freeMinted=5584/10000（上轮 2926），hero totalSupply=5593（上轮 2936），openedAt=0，池未开。规则/CA 未变。入口 https://aoneai.lol/ 。本号不自动 mint。
- **All in crypto / $AIC（@allincrypto_ai）**：同一已提醒付费 LIVE 窗口，只更新进度，不重推。链上 totalMinted=1461/10000（上轮 323），paused=0，价格仍 0.002 BNB/份，池未开。API/LB 约 totalShares=1335、holderCount=130。官帖 19:59 CST 自称 1000/10000。本号不自动 mint。
- **Bsc Cat / $BSC（@Bobkjyj）**：链上 freeMinted 仍 533/800，paidMinted=0，pair=0x0，CA 未变。未售罄、未开池。不重推。
- **$DOG CITY（@bitmaxdog）**：mint.dogcity.space HTTP 200，仍 PUBLIC MINT · OPEN。tip 976429，424 DEEDS CLAIMED · 423 ON BITCOIN（上轮 976420 / 423 / 421）。同一已提醒付费公开窗口，不重推。
- **Doyak Fun（@DoyakFun）**：doyak.fun HTTP 200，页面仍写 Launching soon on GIWA，launching and trading are switched off，No launches yet。无开闸钟点，尚未 LIVE。不重推。
- **Kismo Seekers（@Kismonft）**：快照今日 21:00 CST，核验时距约 0.8 小时。这是持仓快照（每 Seeker=2 GTD），不是 mint/open，不推。
- **GTA GIWA**：www.gtagiwa.xyz HTTP 200，倒计时仍为 Nov 18 · 21:00 ET（2026-11-19 10:00 CST），尚未 LIVE。距开闸约 13.8 小时，le2h=false，不新建卡、不重推。
- **FIST / fistagent.fun**：同一已提醒窗口，规则/CA 未见翻盘，不重推。
- **Aurum Desk（@AurumworId）**：同一已提醒付费 NFT 窗口，不重推。
- **PXIO / pxio.fun**：站点 HTTP 200，页面链到 https://x.com/pxiofun，有用户称 Agent-ID 门槛免费 miner NFT；但 getUsersByUsername("pxiofun") 返回 Not Found。硬规则：有 handle 须 X 核验通过才能收录，本轮不建卡。未再连刷其它候选号。待官号可核验后再议。

跳过未新收录：@AmmoraEco（已在库 @AmmoraHQ 的生态号，本窗为 KRWQ 合作宣布，不是新 mint 窗口）；@blonskr（已在 tapeWatch/tapeOutWatch，本窗仅加油回复，无独立候选卡）。

## 读取与覆盖

- UF 2 批 + MUST 1 + THIN 5 official 批 + KW 11 + mentions 4 + silent 1 = 23 main + 1 silent；另 EXTRA 1（getUsersByUsername pxiofun）。
- 车道 rc：UF1 2 / UF2 0 / MUST 25（作者 allincrypto_ai, aone_agent, bitmaxdog, Fistagent_, Kismonft）/ THIN1 2 / THIN2 4 / THIN3 5 / THIN4 7 / THIN5 0 / KW_LZ 1 / KW_TAPE 25 / KW_GIWA 25 / KW_DOGE 25 / KW_BTC 10 / KW_SN 16 / KW_MINT 25 / KW_MINE 19 / KW_PAD 25 / KW_GO 25 / KW_ELY 25 / MEN_LZ 25 / MEN_ELY 25 / MEN_MINE 2 / MEN_BN 9 / SILENT_MEN 25。
- 软债 lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch，以及 agentPadWatch / bnAgentWatch / kinetiqWatch 等。
- 官方窗约 90 分钟（自 2026-11-18T10:33:21Z）；KW/mentions 约 60 分钟（自 11:03:21Z）；silent 约 24 小时（自 2026-11-17T12:03:21Z）。

面板已同步推送：https://reboot7454.github.io/early-scout/
