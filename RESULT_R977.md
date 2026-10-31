# RESULT R977

```json
{
  "round": 977,
  "mode": "full-scan",
  "completedAt": "2026-10-31 12:39 CST",
  "xReads": 39,
  "remaining": "619/1000",
  "remainingBefore": "658/1000",
  "notify": true,
  "alertMessage": "🔔新增：Homer（@homer_fi）Elysium day-one 流动性层 staking LIVE，$HOMER CA 已出粉26；Derpagent（@Derpagent_）BNB 4444 Agent 卡 LIVE（2222 free+2222 paid，只打免费，合约未核）——面板：https://reboot7454.github.io/early-scout/",
  "newAdmits": [
    {
      "id": "homer-fi",
      "name": "Homer",
      "handle": "@homer_fi",
      "why": "Elysium day-one 流动性枢纽；官推2026-10-30新建粉26；站homer.finance；staking LIVE fee用HYPE；$HOMER CA 0x365Be…399A；DS overall72 admit",
      "score": 72,
      "focus": false,
      "le2h": false
    },
    {
      "id": "derpagent",
      "name": "Derpagent",
      "handle": "@Derpagent_",
      "why": "BNB 4444像素Agent卡 LIVE：2222 free+2222 paid；站derpagent.pro；官推粉≈48；合约未核实；付费只报；DS overall68 admit",
      "score": 68,
      "focus": false,
      "le2h": true
    }
  ],
  "skipped": [
    {"id": "free-agent-mint", "why": "DS admit:false overall28；无官推+pages.dev低信誉；付费1U推广页"},
    {"id": "CodexAgentic", "why": "已在库 codex-agentic R900；本轮再刷LIVE不重复告警"},
    {"id": "FISTAgent", "why": "已在库 fistagent R964"},
    {"id": "DualForgeBSC", "why": "已在库 dualforge-bsc R853"},
    {"id": "DeusTrdng", "why": "NutshellMarkets 个人建造者号，非独立项目；Nutshell已在UF"},
    {"id": "known-NF", "why": "mobster_meme/starx_xlayer/TapeFractal/Leeonmort/Glaze_xyz 本轮跳过或NF"},
    {"id": "flap-compromise-PSA", "why": "flapdotsh/stonk.fun 前端疑似被攻击安全提示，非新项目"}
  ],
  "coverage": {
    "userFollowSoftBrush": ["machinedotfun","bscaidrop","PulseLaunchpad","localbottomcom","NutshellMarkets","squeekchain","gangdotfun","pipfun_xyz","Ptahtrade","ComputeRollLabs","flapdotsh","dotaipad","yinghubnb","Enter_Elysium","kinetiq_xyz","AgentKinetiq","GIWA_by_Upbit","DogeOS","ShieldedNaka","listendotmoney","homer_fi","Derpagent_"],
    "userFollowSkippedNF": ["mobster_meme","starx_xlayer","TapeFractal","Leeonmort"],
    "requiredWatches": ["userFollowWatch","agentPadWatch","kinetiqWatch","miningWatch","tapeWatch","giwaWatch","btcPrivacyWatch","starknetWatch","flapPadWatch","bnAgentWatch","freeMintWatch"],
    "keywordsTenCols": true,
    "mentionsCoverage": ["Elysium/kinetiq","Tape","GIWA","Zero/DogeEVM","Starknet","BTC privacy","flap/Irys/Full.fun/Arc","BN Agent pads","squeek/Nutshell","STARX/X Layer"],
    "bnAgentWeb": ["launch.suan.bid","bnagent.onrender.com","agentcity.uk","derpagent.pro","fistagent.onrender.com","free-agent-mint.pages.dev"]
  },
  "keywordsTenCols": true,
  "userFollowDone": true,
  "mentionsCoverage": ["Elysium/kinetiq","Tape","GIWA","Zero/DogeEVM","Starknet","BTC privacy","flap","BN Agent pads","squeekchain/NutshellMarkets","STARX/X Layer"],
  "discordPeekDeferred": true,
  "dsUsage": {
    "model": "deepseek-flash",
    "batchScore": 3,
    "admitted": 2,
    "alert": 1,
    "fallback": false
  },
  "watchBugsFixed": [
    "day-zero-drop @dayzerodrop → UF/freeMint",
    "3f3rwefwf @3f3rwefwf → UF",
    "usetagpay @usetagpay → UF",
    "agentsgofirst @agentsgofirst → UF",
    "getblessed-fun @getblessed_fun → UF",
    "homer-fi @homer_fi → UF/kinetiq/elysium",
    "derpagent @Derpagent_ → UF/freeMint/agentPad/bnAgent"
  ],
  "notes": [
    "full-scan remaining≫200 (started ~658 → 619)",
    "paid Agent ID mint report-only; no auto-mint (derpagent paid half report-only)",
    "no re-alert R971–R976 items (hyperliqpad/monster-rh/agentcity-uk/cappybara/fistagent/…)",
    "soft-debt Canton/Glaze/TokenWorks + softDebtWatches lastChecked bumped",
    "Nutshell mentions: Deus@NutshellMarkets tokenised stocks+$SQK — builder already known via Nutshell UF",
    "flap frontend compromise PSA noted (not admit)",
    "remote main still R976 at pull; no concurrent DC-alpha this round"
  ]
}
```
