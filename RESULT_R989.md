# RESULT R989

```json
{
  "round": 989,
  "mode": "full-scan",
  "completedAt": "2026-10-31 16:05 CST",
  "timezone": "Asia/Shanghai",
  "xReads": 38,
  "remaining": "395/1000",
  "remainingBefore": "433/1000",
  "notify": true,
  "notifyReason": "newAdmits×4 + LIVE续 + $MAOAI开池≤2h",
  "alertMessage": "R989告警：新收录4个——CRT Codes LIVE奇数免费(~2760/10101)、ROCKS CLUB今日预告免费mint(粉0)、币安人LIVE付费0.002BNB(付费只报)、Heroes of Elysium(Elysium Announced)；库内续LIVE：Snailings/Famuli/Nocturn/Seatwork；$MAOAI池约14:28开仍≤2h（付费只报）；面板 https://reboot7454.github.io/early-scout/",
  "alert": "R989告警：新收录4个——CRT Codes LIVE奇数免费(~2760/10101)、ROCKS CLUB今日预告免费mint(粉0)、币安人LIVE付费0.002BNB(付费只报)、Heroes of Elysium(Elysium Announced)；库内续LIVE：Snailings/Famuli/Nocturn/Seatwork；$MAOAI池约14:28开仍≤2h（付费只报）；面板 https://reboot7454.github.io/early-scout/",
  "newAdmits": [
    {
      "id": "crt-codes",
      "handle": "@CRTCodes",
      "name": "CRT Codes",
      "score": 69,
      "note": "LIVE奇数免费~2760/10101；站crtcodes.pages.dev；Element地板0.0059BNB；粉≈36"
    },
    {
      "id": "rocks-club",
      "handle": "@Agentrocksclub",
      "name": "ROCKS CLUB",
      "score": 62,
      "note": "今日新建官推预告免费mint需Agent ID+ROCKS CODE；2222供；粉0"
    },
    {
      "id": "bianren",
      "handle": "@BiAnRen_AI",
      "name": "币安人",
      "score": 60,
      "note": "LIVE付费0.002BNB公平铸满1万开池；站binanciansai.meme；付费只报；粉≈72"
    },
    {
      "id": "heroes-elysium",
      "handle": "@HeroesElysium",
      "name": "Heroes of Elysium",
      "score": 55,
      "note": "Elysium Announced；Nov4收Obol；主网2026-11-09；粉≈4"
    }
  ],
  "newIds": [
    "crt-codes",
    "rocks-club",
    "bianren",
    "heroes-elysium"
  ],
  "newCount": 4,
  "skipped": [
    {
      "id": "agent-bi",
      "why": "官推称LIVE但官网写未部署/即将开铸，DS skip 高风险"
    },
    {
      "id": "uagent",
      "why": "仅一条官宣无站无时间，DS skip"
    },
    {
      "id": "mobster_meme/starx_xlayer/TapeFractal",
      "why": "NF skip dead lookups"
    },
    {
      "id": "agentmao",
      "why": "非newAdmit（库内刷新开池≤2h）"
    },
    {
      "id": "famuli/nocturn-companions/snailings/seatwork-cells",
      "why": "库内续LIVE，非newAdmit"
    },
    {
      "id": "suan/bnagent/proxis/swarm/bibiai/lanterns/jager/goldtoad",
      "why": "已在库 BN Agent pads；HTTP探活；付费只报"
    },
    {
      "id": "flap.cool",
      "why": "DNS劫持新闻续；非新项目admit"
    }
  ],
  "admissions": [
    {
      "id": "crt-codes",
      "admit": true,
      "score": 69,
      "reason": "可立即免费参与且有地板价"
    },
    {
      "id": "rocks-club",
      "admit": true,
      "score": 62,
      "reason": "今日新建粉0最早期预告"
    },
    {
      "id": "bianren",
      "admit": true,
      "score": 60,
      "reason": "链上可操作中文meme打新（付费只报）"
    },
    {
      "id": "heroes-elysium",
      "admit": true,
      "score": 55,
      "reason": "Elysium早期NFT Announced可跟"
    },
    {
      "id": "agent-bi",
      "admit": false,
      "reason": "官网与官推矛盾"
    },
    {
      "id": "uagent",
      "admit": false,
      "reason": "信息量极低无可操作窗口"
    }
  ],
  "coverage": {
    "userFollowSoftBrush": [
      "machinedotfun",
      "bscaidrop",
      "PulseLaunchpad",
      "localbottomcom",
      "NutshellMarkets",
      "squeekchain",
      "Enter_Elysium",
      "kinetiq_xyz",
      "GIWA_by_Upbit",
      "DogeOS",
      "ShieldedNaka",
      "agentmao_",
      "Proxisfun",
      "flapdotsh",
      "dotaipad",
      "gangdotfun",
      "FamuliAI",
      "NocturnCompanio",
      "CRTCodes",
      "Agentrocksclub",
      "BiAnRen_AI",
      "HeroesElysium",
      "SnailingsNFTs",
      "seatworkcells"
    ],
    "userFollowSkippedNF": [
      "mobster_meme",
      "starx_xlayer",
      "TapeFractal"
    ],
    "requiredWatches": [
      "userFollowWatch",
      "agentPadWatch",
      "kinetiqWatch",
      "miningWatch",
      "tapeWatch",
      "giwaWatch",
      "zeroWatch",
      "dogeEvmWatch",
      "elysiumWatch",
      "btcPrivacyWatch",
      "starknetWatch",
      "flapPadWatch",
      "irysPadWatch",
      "fullFunWatch",
      "arcPadWatch",
      "bnAgentWatch",
      "freeMintWatch",
      "agentTradingWatch",
      "xChainPadWatch",
      "agentMiningWatch"
    ],
    "keywordsTenCols": true,
    "mentionsCoverage": [
      "Elysium/kinetiq",
      "Tape",
      "GIWA",
      "Zero/DogeEVM",
      "Starknet",
      "BTC privacy",
      "flap",
      "BN Agent pads/SUAN",
      "squeek/Nutshell",
      "STARX/X Layer(keywords)"
    ],
    "bnAgentWeb": [
      "launch.suan.bid",
      "bnagent.onrender.com",
      "agentmao.fun",
      "goldtoad.fun",
      "proxis.fun",
      "binanciansai.meme",
      "crtcodes.pages.dev",
      "moomoo.cloud"
    ]
  },
  "keywordsTenCols": true,
  "userFollowDone": true,
  "mentionsCoverage": [
    "Elysium/kinetiq",
    "Tape",
    "GIWA",
    "Zero/DogeEVM",
    "Starknet",
    "BTC privacy",
    "flap",
    "BN Agent pads/SUAN",
    "squeek/Nutshell",
    "STARX/X Layer"
  ],
  "discordPeekDeferred": true,
  "dsUsage": {
    "model": "deepseek-flash",
    "batchScore": 1,
    "admitted": 4,
    "skipped": 2,
    "alertCopy": 1,
    "thinking": true
  },
  "watchBugsFixed": [
    "crt-codes @CRTCodes → UF+agentPad+bnAgent+freeMint",
    "rocks-club @Agentrocksclub → UF+agentPad+bnAgent+freeMint",
    "bianren @BiAnRen_AI → UF+agentPad+bnAgent+freeMint",
    "heroes-elysium @HeroesElysium → UF+elysiumWatch"
  ],
  "refreshed2hOrLive": [
    {
      "id": "agentmao",
      "note": "$MAOAI池约14:28开仍≤2h（至~16:28）付费只报；粉≈332"
    },
    {
      "id": "snailings",
      "note": "LIVE续 ~1543/4444"
    },
    {
      "id": "seatwork-cells",
      "note": "PoW挖矿续"
    },
    {
      "id": "famuli",
      "note": "LIVE续"
    },
    {
      "id": "nocturn-companions",
      "note": "LIVE续"
    }
  ],
  "notes": [
    "R988→R989 full-scan remainingBefore 433≥200",
    "Paid Agent ID mint = report-only / no auto",
    "Soft-debt: Canton/Glaze/TokenWorks lastChecked bumped",
    "agent-bi/moomoo.cloud site vs X contradiction → skip",
    "xReads ~38; remaining 395≫200",
    "discordPeekDeferred=true (no DC login)"
  ]
}
```
