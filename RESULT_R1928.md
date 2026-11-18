# RESULT R1928

模式：ample（正常例行，非 post-reset-full；lastFullAfterReset 保持 R1926）
时间：2026-11-18 10:16 CST（Asia/Shanghai）
xReads：24（main 23 + silent 1 + EXTRA 0），remainingBefore 940 → remaining 916，softCap 28 / minSpend 20 / silentCap 2。

## 新收录

- Roobak（@roobak_xyz，台子/Meme，announced，overall 58 / risk 76）：09:59 CST 官帖宣布 Launchpad Testnet 即将上线，细节本周公布。账号 2026-11-17 19:19 CST 建号，抓取时粉 284、帖 24。官网 https://www.roobak.xyz/ HTTP 200，站点 JS 互链 https://x.com/roobak_xyz。定位是 Robinhood Chain 上的 Uniswap v4 返还 hook（同一笔 swap 内回补价差，已实现利润分给交易者和 LP）。前端已含 Robinhood Chain testnet（chainId 46630）swap/rebate 控制台；官网 JS 给出测试网 RebateHook 0x5940a85b69C5978FD7A7Fe6A0637d4C5DCDA90C0、SwapRouter 0x8bb678A9b9cc3d5F5Ce1bCbF9E9f057eB134A0bA，测试网夹具代币可 public mint，这不是项目发售免费 mint。无官方主网/发售代币 CA。app.roobak.xyz TLS 失败。不是免费 mint，也无 ≤2h 窗口。focus=false。DeepSeek 同意收录。

## 在库更新

- Bitmax $DOG CITY（@bitmaxdog）：10:09 CST 官网仍写 3 BLOCKS TO THE PUBLIC MINT，公开阶段仍自 Bitcoin block 976,368 开启；mempool.space 与 blockstream.info tip 均为 976365，还差 3 块（约 30 分钟）。mint.dogcity.space 写 ORDERS FOR THE PARTNERS ARE CLOSED · THE PUBLIC PHASE OPENS AT BLOCK 976,368 · IN 3 BLOCKS。公开尚未 LIVE。公开价仍约 US$2 起，单笔最多 10 个 lot、每 144 块每钱包上限 10。相对 R1927（tip 976358、约 10 块 / about 2 hours）只是更接近同一已提醒窗口，未 LIVE / 未售罄 / 未延期 / 未改价，不重推。状态保持 public-soon，le2h=true。
- Vice City Fund（@ViceCityFund_）：官网 www.vicecityfund.fun 与 /create 均 HTTP 404（Vercel DEPLOYMENT_NOT_FOUND）。官号本窗 08:55 CST 发帖仅一行地址 4owiqSSaq97Dy9eECDzSBYHNxk6FNMsfodcttidHcRr8（即 R1927 已排除的第三方所称地址）；资料栏网址已空、抓取时帖数显示 1。不把该裸地址当作新的官方开售或免费 mint 重推。
- ElysiumPyramids（@ElysiumPyramids）：本窗仅再次看到 08:47 CST 那条 Launching on @Enter_Elysium / Free mint / Drop your wallet 帖，仍无官网与已核验 CA，未见 @Enter_Elysium 背书，不按免费 LIVE 重推。
- Fistagent_ 本窗继续称 mint is live for Agent wallets（入口仍 fistagent.fun），未见本轮新核验官方 CA；EnterXLaunch / KukiVerse3D 本窗无新官帖。均仅刷新 lastChecked，不重推。

未收录：Lamoryant 免费 mint 仍仅第三方跟帖，延续 R1926/R1927 skip/defer，本轮未拉官号。AgentEcho 仅 @dali80801 第三方自称已免费 mint，无官号。$6STAR（@ParlayCrypto12）为已在 Elysium 上线的 meme，不是发射台/打新。CarsAsCards / @Grenadexcii 仅为第三方 GTD 转发，官号 @ChaoticorderNFT 已在库且无新核验窗口。silent GO盘 3 帖均为口语 “go launch” 噪音。

## 覆盖与额度

- 十栏关键词均已跑全。tenLanes=yes。
- UF 从 485 musterupfun 起 2 片 kept 50（musterupfun→dominioncoins），skip_already 0，NF_skip 4（Asciidogs,rheacatnear,magnitudeagent,bububullfun），wrap=false，walkScanned 54，next 539 streamlitmaker。
- mentions 本轮 4 组：LayerZero 25 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 6；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- silent GO盘（仅 SILENT_MEN，search_users 仍不在目录；3 帖 / seen 6，全部 too_many_posts），下一轮 LayerZero。
- fat cursors 未推进（agentPad 730 / freeMint 66 / bnAgent 169 / elysium 283）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- 新卡已进 Watch：userFollowWatch:@roobak_xyz。未把 Roobak 推进 freeMintWatch（非免费）。watchLeaksFixed=['beepz @beepzfun → userFollowWatch（库内无 Watch）','pangea @LaunchOnPangea → userFollowWatch+layerZeroWatch+zeroWatch（库内无 Watch）']。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset=R1926。

栏 rc：KW_BTC 10，KW_DOGE 25，KW_ELY 25，KW_GIWA 21，KW_GO 0，KW_LZ 0，KW_MINE 3，KW_MINT 25，KW_PAD 25，KW_SN 1，KW_TAPE 25，MEN_BN 6，MEN_ELY 25，MEN_LZ 25，MEN_SQ 0，MUST1 16，SILENT_MEN 3，THIN1 4，THIN2 1，THIN3 1，THIN4 0，THIN5 2，UF1 0，UF2 0。parse_errors 无；部分 write_to_file 预览截断已从 assets 完整副本恢复，未重拉 X。无 EXTRA 额外查询。

官方窗口：official 自 2026-11-18T00:43:00Z（约 90m，与 lastScout 01:13Z / 09:13 CST 重叠）；KW 与 mentions 自 2026-11-18T01:05:00Z（约 60 分钟起算）；silent 自 2026-11-17T02:05:00Z（约 24h）。本轮与上一成功轮仅隔约 52 分钟，未拉长补扫窗。

## notify

true。【早期打新雷达·第1928轮】新收录 Roobak（@roobak_xyz）：Robinhood Chain 上的 Uniswap v4 返还 hook，官网已开、含测试网 swap/rebate 控制台，官帖称 Launchpad Testnet 即将上线、本周公布细节；非免费 mint、无开闸钟点、无官方代币 CA。面板：https://reboot7454.github.io/early-scout/ 。本号不自动 mint / 不自动打。
