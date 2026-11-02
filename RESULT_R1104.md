# RESULT R1104 — 2026-11-02 ~10:16 CST

- mode: ample
- softCap: 28
- xReads: ≈21
- remainingBefore: 928
- remaining: ≈907
- resetAt: 2026-11-03 08:00 CST
- xQuota: softCap=28 用≈21余≈7；footer remainingBefore≈928→≈907；本轮非 08:00 后首轮（R1100 已是 post-reset-full）；ample pacing UF→必盯/≤2h→十栏KW全量→mentions轮换子集

- newIds: （无）
- admits: 无新收录
- skip:
  - Agent Wars / $AWARS（官网 agent-wars-tawny.vercel.app；CA 疑似 0xDbc7…bfa4；页面无官推；仅 @gami_imf 等个人号宣传）→ DS：无官推硬门槛不收
  - UF 新 NF/死号：battle_pad(suspended) / cabaldotfun / project_hoodmon → 记 NF_skip 不连刷
  - 点名 UF 中 PulseLaunchpad / machinedotfun / mobster_meme / starx_xlayer 仍 NF_skip 不连刷
  - Ptahtrade mentions 全为既有 #ProofOfAgent 互动，无新挂靠项目
  - Servobun 上轮已 skip，本轮不重复收
- updates:
  - agent-harvest(**关键** freeOpen 1→0；phase6 pause→14:34:48CST ≈4.3h **非≤2h**；tm≈3422 free=3000 paid≈422 phaseMinted≈500；较 R1103 freeOpen LIVE 状态跃迁 → notify=true)
  - nullsector(ts≈1963/4321 freeLIVE；较≈1600 续增)
  - onimaru(tm≈1000 freeMinted≈993/1000 近罄未变)
  - baoracle(tm≈7185；较≈6744 续增)
  - rootlinks(tm≈392 free≈390；较≈371 续增)
  - pixcade(tm≈1548 free罄1500 → paidLIVE)
  - jiepanfun(tm≈187)
  - shalinggou(watching；RPC sharesSold=0；距今晚19:00CST≈8.7h 非≤2h)
  - agent-yyds(watching；链上/config 开售戳=2026-11-02 20:30 CST；非≤2h)
  - agent2(upcoming；sold≈0；今晚20:00CST；非≤2h)

- le2h: false（Harvest pause≈4.3h；shalinggou/YYDS/AGENT2 均 >2h）
- notify: true
- alert: early-scout R1104告警：Harvest phase6 freeOpen=0 暂停→14:34CST；tm≈3422 free3000；nullsector≈1963；onimaru free≈993；baoracle≈7185；rootlinks≈392；shalinggou仍等19:00CST。面板 https://reboot7454.github.io/early-scout/

- ufCursor: 70→98（并同步修正 meta.ufCursor 与 userFollowWatch.cursor；清 R1102 滞留 6→42）
- userFollowShardDone: true（70→98；点名 @localbottomcom @NutshellMarkets @bscaidrop 软刷；@mobster_meme @machinedotfun @PulseLaunchpad @starx_xlayer 仍 NF_skip 不连刷仅记）
- tenLanesKeywords: true（合并十栏近30min：Agent mining/free mint/fair launch/Agent ID/AIDROP/bscaidrop/PulseLaunchpad/Local Bottom/Nutshell/squeek/STARX/X Layer/TapeOut/GIWA/DogeEVM/Starknet/Elysium/挖矿/打新/GO盘 等；AWARS 因无官推 skip；无强新录取）
- mentionsChains: Zero(@LayerZero_Core 近窗0) · DogeEVM(@DogeOS) · Starknet · BTC隐私(@ShieldedNaka 近窗0) · flap(@flapdotsh) · Irys(@irys_xyz 近窗0) · Full.fun(@fulldotfun 近窗0) · Arc(@arcxtrade 近窗0) · BN pads(@Ptahtrade) · 对照 Tape(@TapeAIAgent 近窗0)；无强新挂靠录取
- watchBugsFixed: 无（跟进卡均已在 Watch；本轮无新 admit 需接入）
- Discord: discordPeekDeferred=true（无登录，未尝试登录）
- push commit: (pending)
- NF_skip: TapeFractal; Leeonmort; computeroll; PulseLaunchpad; machinedotfun; mobster_meme; starx_xlayer; deadpacksol; blindfloor; trytoprint; PlayFarmFi; reynarlabs; world_ygg; +battle_pad; cabaldotfun; project_hoodmon
- softDebt: 已刷新各 Watch lastChecked（userFollowWatch/freeMintWatch/bnAgentWatch/agentPadWatch 及十栏相关 Watch + canton/glaze/tokenWorks）
- deferredFullScan: false（本轮 ample 常规轮，非重置后首轮）
- notes:
  ample 硬序：UF软刷(70→98) → 必盯 HTTP+RPC（Harvest 核验优先，发现 freeOpen1→0） → 十栏KW全量 → mentions 轮换子集（补 Zero/DogeEVM/Starknet/BTC隐私/flap·Irys·Full·Arc/BN-pad + Tape对照） → Discord deferred。
  Harvest freeOpen 再关 + 新 pause→14:34CST → notify=true（无新 admit 亦告警；非≤2h）。
  AWARS 因无官推硬门槛跳过（DS confirm）。
  建议下轮：盯 Harvest 14:34 freeOpen 恢复（入≤2h 升档）；onimaru free 是否罄；shalinggou→19:00 / AGENT2→20:00 / YYDS→20:30 临近≤2h；nullsector/baoracle/rootlinks 进度；meta.ufCursor 已与 ufw.cursor 对齐从 98 续。
