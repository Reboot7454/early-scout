# RESULT R1000

```json
{
  "round": 1000,
  "mode": "tight-quota-full-scan",
  "completedAt": "2026-10-31 19:01 CST",
  "timezone": "Asia/Shanghai",
  "xReads": 33,
  "remainingBefore": "177/1000",
  "remaining": "144/1000",
  "notify": true,
  "notifyReason": "newAdmit×1 bsc-ququ; SAFU≤2h(~2.0h); Frogs距≈2.5h未≤2h",
  "alertMessage": "R1000告警：新收录1个——BSC QUQU(@BSCQUQU) BNB回合制蛐蛐链游；.ai Agent ID硬门槛；挖矿约1U领盲盒/约4U购盒；盲盒终身24444；粉≈2（score71，付费只报）。≤2h：SAFU Fund今日21:00CST开铸（距≈2.0h，Tier1≈1USDT，付费只报）。库内：Bitcoin Frogs@frogsagent 今晚21:30CST开铸（前2000免费，CA已核，距≈2.5h未≤2h）；$MEH续fair mint付费只报。面板 https://reboot7454.github.io/early-scout/",
  "alert": "R1000告警：新收录1个——BSC QUQU(@BSCQUQU) BNB回合制蛐蛐链游；.ai Agent ID硬门槛；挖矿约1U领盲盒/约4U购盒；盲盒终身24444；粉≈2（score71，付费只报）。≤2h：SAFU Fund今日21:00CST开铸（距≈2.0h，Tier1≈1USDT，付费只报）。库内：Bitcoin Frogs@frogsagent 今晚21:30CST开铸（前2000免费，CA已核，距≈2.5h未≤2h）；$MEH续fair mint付费只报。面板 https://reboot7454.github.io/early-scout/",
  "newAdmits": [
    {
      "id": "bsc-ququ",
      "handle": "@BSCQUQU",
      "name": "BSC QUQU",
      "score": 71,
      "note": "BSC蛐蛐链游；.ai门槛；挖矿约1U/购盒约4U；粉≈2；付费只报"
    }
  ],
  "newIds": [
    "bsc-ququ"
  ],
  "newCount": 1,
  "skipped": [
    {
      "id": "zerodrift-ai",
      "why": "DS skip：链不明、无清晰mint窗"
    },
    {
      "id": "syntax-souls",
      "why": "DS skip：官号粉≈0疑似刷量"
    },
    {
      "id": "avatweet-private",
      "why": "DS skip：私有轮非公平mint"
    },
    {
      "id": "starx_xlayer",
      "why": "handle Not Found；改用@lumora_agent mentions"
    },
    {
      "id": "mobster_meme",
      "why": "handle Not Found this round"
    },
    {
      "id": "giwa-deuslaunch-noise",
      "why": "GIWA mentions多为deuslaunch testnet跟风"
    },
    {
      "id": "starknet-kol-noise",
      "why": "Starknet mentions全是KOL互动无新挂靠mint"
    },
    {
      "id": "doge-halloween-noise",
      "why": "DogeOS mentions万圣节/梗图噪音"
    },
    {
      "id": "squeek-community-noise",
      "why": "squeek mentions社区互动无新挂靠官号"
    }
  ],
  "coverage": {
    "tenLanes": true,
    "userFollowSoft": true,
    "keywords": true,
    "keywordsTenCols": true,
    "mentionsChains": [
      "Tape",
      "squeek/Nutshell",
      "STARX/XLayer(lumora)",
      "BN/gangdotfun",
      "BTC/ShieldedNaka",
      "GIWA",
      "DogeEVM",
      "Starknet",
      "Zero/Arc/flap",
      "Elysium(抽1)"
    ],
    "notes": "额度紧模式：UF soft→必盯/≤2h→关键词合并→mentions轮换子集；Discord deferred；R999 honest/punk/liquidit补入UF+Watch；SAFU入le2h；Frogs CA核验0xd9e0…0131；软债lastChecked已刷"
  },
  "watchBugs": [
    "honest-coin→UF+freeMintWatch+agentPadWatch",
    "punkonelysium→UF+elysiumWatch+freeMintWatch",
    "liquidit-x→UF+elysiumWatch+miningWatch",
    "bsc-ququ→UF+bnAgentWatch+agentPadWatch+agentMiningWatch+miningWatch"
  ],
  "discordPeekDeferred": true,
  "dsFallback": false,
  "dsModel": "deepseek-flash",
  "thinking": true,
  "push": true,
  "pushSha": "e09d3f6",
  "dataSha": "e09d3f6",
  "panel": "https://reboot7454.github.io/early-scout/",
  "le2h": [
    {
      "id": "snailings",
      "note": "LIVE first free"
    },
    {
      "id": "famuli",
      "note": "Mint LIVE"
    },
    {
      "id": "nocturn-companions",
      "note": "Mint LIVE"
    },
    {
      "id": "safu-fund-bnb",
      "note": "SAFU mint 21:00CST ≤2h (~2.0h); paid report-only"
    }
  ]
}
```
