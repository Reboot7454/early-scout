# R2193 Early Scout X-radar Result

- Round: **R2193** (meta.round 2192 + 1)
- lastScout written: **2026-11-25 19:53:32 CST** (Asia/Shanghai)
- Fire window: about 2026-11-25 19:38–19:53 CST
- lastFullAfterReset: **R2170** (normal incremental; not 08:00 CST first full backfill)
- Panel: https://reboot7454.github.io/early-scout/
- Dry-run data: `/tmp/r2193/data.json` (source `/tmp/r2193/data.json.src`; **did not** modify `/workspace/early-scout/data.json`; no commit/push)
- notify.json: `/tmp/r2193/notify.json`
- This file: `/tmp/r2193/RESULT_R2193.md`

## X budget and reads

- Live remainingBefore (first X footer, trust remainingToday after first read 368): **369/1000**
- remainingAfter (last footer, KW_STARK_24): **341/1000**
- **xReads = 28** (main 27 + silent 1)
  - Planned incremental: 24 main + 1 silent = 25 (UF1/UF2/UF3, MUST_WIN/MUST_WIN2/MUST_WIN3, MUST_OFF, 10 lanes + KW_GAPS, MEN_PADS/MEN_GIWA/MEN_TAPE/MEN_LZ/MEN_ELY, SILENT_LZ)
  - Justified thin-lane 24h backfills: **+3** (`KW_LZ_24`, `KW_BTC_24`, `KW_STARK_24`)
- `x_budget.py 369` suggested mode=**pace**, softCap=18, minSpend=18, silentCap=2
- **Override (same as R2185–R2192):** remaining ≫ 200 and the user forbids cutting lanes when quota is ample, so the full incremental plan in queries.json was run (24 main + 1 silent, plus thin-lane 24h when 30m independent KW < 5). UF1/UF2/UF3 exist because the 50-account shard needed three `from:` batches (qlen cap; UF3 is a short leftover `@Scintillamine`). MUST_WIN/MUST_WIN2/MUST_WIN3 are planned official `from:` batches (MUST_WIN3 exists because the must-win list is long, including R2192 new official handle `@secretwiz_rgb`), not exploratory reads.
- Minute limit: stayed under 30/min; no retries, no pagination, no extra exploration.
- All planned searches in queries.json ran **once**. No NF retries. `@starx_xlayer` was already skipped in MUST_OFF.

### Lane coverage

- All **10 keyword lanes + KW_GAPS** ran (30m): yes
- Mentions this round: **pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest** (MEN_PADS, MEN_GIWA, MEN_TAPE, MEN_LZ, MEN_ELY)
- Next-round mentions should rotate to: **DogeEVM / BTC / Starknet / squeek / STARX** (those mention sets were not run this round)
- Silent this round: **LayerZero** (`SILENT_LZ`, 24h, 14 hits, outside softCap). Next silent lane: **Elysium** (2194 % 11 = 5)
- UF shard: cursor **1711 @PyreOnchain**, 50 accounts through **@Scintillamine**, wrap=false, next **1761 @reelsliq**, library UF total after apply **2409** (was 2405; +4 new official handles appended)

### Thin-lane 24h backfill

30m independent KW hit counts and decisions:

| Lane | 30m id | 30m hits | 24h backfill |
|------|--------|----------|--------------|
| LayerZero | KW_LZ | **0** (<5) | **yes** KW_LZ_24 (25, capped) |
| Tape | KW_TAPE | **19** | no |
| GIWA | KW_GIWA | **25** | no |
| DogeEVM | KW_DOGE | **9** | no |
| BTC | KW_BTC | **3** (<5) | **yes** KW_BTC_24 (25, capped) |
| Starknet | KW_STARK | **4** (<5) | **yes** KW_STARK_24 (25, capped) |

- KW_MINE 30m = 1; MINE is a core lane — **no** 24h added just because it is low.
- Core/fat lanes MINT/PAD/GO/ELY/GAPS were already ≥5 (KW_ELY=5, not <5) — no 24h.

### Per-search result counts (after ingest, SILENT_LZ included)

UF1 0, UF2 0, UF3 0, MUST_WIN 25 (capped, next_token), MUST_WIN2 25 (capped), MUST_WIN3 25 (capped), MUST_OFF 0, KW_LZ 0, KW_TAPE 19, KW_GIWA 25, KW_DOGE 9, KW_BTC 3, KW_STARK 4, KW_MINT 25, KW_MINE 1, KW_PAD 24, KW_GO 25, KW_ELY 5, KW_GAPS 16, MEN_PADS 16, MEN_GIWA 25, MEN_TAPE 8, MEN_LZ 25, MEN_ELY 24, SILENT_LZ 14, KW_LZ_24 25, KW_BTC_24 25, KW_STARK_24 25.

Unique posts flattened: 401 (418 rows). Errors: none.

## New admits (DeepSeek score/admit, focus=false)

DeepSeek (`deepseek-flash`, thinking on, `dsFallback=false`) scored five shortlisted items. Admitted four; skipped BLOCKPAY Genesis.

1. **F0B90B @F0B90Bclub** — id `f0b90b`, score 78 (early 92 / actionable 70 / novelty 75 / risk 60). Site https://f0b90b.pages.dev/ (HTTPS 200, title “F0B90B - Proof of Gold on BNB”, footer X @F0B90Bclub, site↔handle mutual). Account created **2026-11-25 18:20:25 CST**, 5 followers / 1 post, xUserId 2125534623484542976. Official post **2026-11-25 19:09:12 CST** (https://x.com/F0B90Bclub/status/2125547346511716649): 10,000 yellow squares on BNB; First 3 FREE; then 0.0003 BNB; max 10/wallet; Binance Agent ID. Official site: CONTRACTS DEPLOYING · MINT OPENS SOON; no CA this round; ERC-721 + ERC-6551; 10,000 $F0B90B per square wallet. **Not confirmed mint LIVE.** Watches: userFollowWatch + bnAgentWatch + freeMintWatch.

2. **Antopia @antopia_xyz** — id `antopia`, score 62. Site https://antopia.xyz/ (HTTPS 200, site lists https://x.com/antopia_xyz). Account created **2026-11-23 11:40:38 CST**, 947 followers / 40 posts, xUserId 2124709495016177664, display name Antopia Bsc. Official post this round only said Clash of Antopia goes live tomorrow (https://x.com/antopia_xyz/status/2125540105943187796), not a mint announcement. Official `AN_CFG`: NFT `0x7e2bD45CD95d6603f347C5310Ee1Ce9Dd145c70B`, TOKEN `0x73BAcE4461E9bFD686E73994a91Dd1e4c01Ad6C9` (ANTZ, 1,000,000,000 × 1e18), MARKET `0xe45e1870306Ec1E6D488cDFCf02Dec43819d30Cd`; PRICE 0.00088 BNB; MAX_SUPPLY 8888. BSC public RPC: saleOpen=true, totalMinted=**5889**, MAX_SUPPLY=8888, freeClaimed=**4000**, FREE_CAP=4000, freeRemaining=**0**, X_FREE_CAP=500 (X-free remainder not independently confirmed). Site still shows a Claim Free button, but the on-chain free cap is exhausted. **Paid mint still open; not a currently claimable free mint LIVE.** Watches: userFollowWatch only.

3. **Oneshot @OneshotExchange** — id `oneshot-exchange`, score 60, zone LayerZero. Site https://oneshot.exchange (HTTPS 200, thin SPA; no CA extracted). Account created **2026-11-01 23:55:45 CST**, 39 followers / 17 posts. Official posts point to https://oneshot.exchange/airdrop (tier check + social tasks, then launch a token). **Not a free mint.** Watches: userFollowWatch + layerZeroWatch.

4. **IndexIt @indexitcash** — id `indexit-cash`, score 52, zone 台子/Meme. Site https://indexit.cash/ → https://www.indexit.cash/. Account created **2026-10-28 09:56:51 CST**, 914 followers / 10 posts. Official/bio CA `$INDEX` `0x7ebd34bd7479f2e5b38dac8593b038fd70137777`. Flap-based index-token launchpad. **Not a free mint.** Watches: userFollowWatch + flapPadWatch.

## Seen but not admitted

- **BLOCKPAY Genesis @BlockpayGenesis** — already named and skipped in R2192 (self-claimed free mint LIVE, no independent site/CA). New official post **2026-11-25 19:39:28 CST** (https://x.com/BlockpayGenesis/status/2125554962403062251) claims an NFT Calendar listing, free mint until Nov 27 12:00 UTC, 182/1,111 claimed, Element trading Dec 2. Profile still only Discord; NFT Calendar page returned Cloudflare 403 this round. Still **no independent official site or CA**. DeepSeek admit=false. Do not force-admit, do not re-push as a new find.

Other mention-only / shill / already-in-library items were not sent to admit (e.g. @AscendLaunch already known; third-party giveaway RTs; @owlhood_rh / @deuslaunch / @RebelianRH already known).

## Library updates (no re-alert without material change)

- **Ugly Puggies @uglypuggies** — official window still **2026-11-25 23:00 CST** (15:00 UTC). Same 19:00:30 CST “T-4 hours” official post already used in R2192. OpenSea collection API this round: total_supply **0**, owners **0**, volume 0, CA `0xe2be23fbffe892feb3677341765847b9309663c2` (robinhood). Card `le2h=false`. First ≤2h starts **21:00 CST**; this fire is before that. Not LIVE. **No re-push, no early first ≤2h.**
- **ORIPA @oripaxyz** — first pack still **2026-11-25 20:00 CST** (8 PM GMT+8 / 12:00 UTC, not 12:00 CST). Official site still shows paid pack pools (not free mint). R2190 already sent first ≤2h; still inside 2h at fire; no new official post / delay. Card `le2h=true`. **No re-push.**
- **deMiners @deMinersNft** — no new official post in MUST_WIN3 (capped). OpenSea API: **492/3333**, 128 owners, floor **0.0006 ETH** (R2192 ~481–482). OG free mint still LIVE until 22:30:04 CST (0 ETH, 3/wallet). Public sale 22:30 CST at 0.0002 ETH; first ≤2h for public starts 20:30 CST — **not yet, do not early-alert, public is not free**. Small progress only. **No re-push.**
- **The Jacket @TheJacket_NVDA** — same “Mint is open / 4444→777 / holder free” official post already alerted. OpenSea API: **194/777**, 126 owners, floor **0.48 USDG** (R2192 ~173/777, floor then recorded 1.50 USDG). Holder allowlist still free; public still 0.0003 ETH. Small progress / secondary floor move only. **No re-push.**
- **ZeroGate @ZeroGate0G** — 18:03 CST “zero-gravity:native is live” post (CA `0xca2E57985A339E130775597332fc55ea0f917777`) was already in the R2192 window; R2192 also recorded the 18:32 CST sniper-failure reply as not a confirmed shutdown. **No re-push.**
- **Helipaid @usehelipaid** — many product posts about Privacy Ring routing; no chain/price/free-window change. **No re-push.**
- **Anthropos @AnthroposAgents** — 12:43 CST product post (Flap swap/bridge/launch with wallet approval). Not a new mint window. **No re-push.**
- **SecretWiz @secretwiz_rgb** — no new official post this round. Allowlist still as admitted in R2192. **No re-push.**
- **2hourfun @2hourfun** — same 19:07 CST official post already recorded in R2192: “We open tonight anyway”, **21:00 UTC = 2026-11-26 05:00 CST**. Do not read as today 21:00 CST. **No early alert.**
- **Shielded Wizards @ShieldedWizBTC** — same 18:50 CST official post already recorded in R2192 (any Bitcoin wallet; public 21:00 UTC = 2026-11-26 05:00 CST). WL free mint still LIVE (R2165). Public first ≤2h ~03:00 CST. **No early alert, no re-push only for still being LIVE.**
- **Agent Cards @agentcardshq** — no direct official post this round. Reprint window still 23:00 CST; first ≤2h at 21:00 CST, **not yet**. **No early alert.**
- **TRIFORGE @TriForgeAgent** — public BSC RPC at **2026-11-25 19:45:33 CST**: Forge Keys **364/3333**, paused=false (R2192 363/3333). lpMintOpen true, lpTotalMinted 0, claimsOpen true, totalClaimed 6, miningShares 6, tradingEnabled false. Small progress, card updated, **no re-push.**
- Other MUST posts (mskdfun spaces/OTC, atlaspad utilities, sleighpad $SLEIGH already had a CA from earlier rounds, etc.) were not material new mint windows.

## discordPeekDeferred

Placeholder left for parent merge. `/tmp/r2193/discord_peek.json` is already present (loginOk=false, loginWall=true, channelsPeeked=false, attemptedAt 2026-11-25 19:39:07 CST). Apply did **not** auto-merge (`APPLY_MERGE_DISCORD` unset). Parent should merge the real peek JSON if desired. This executor did not spend time on Discord itself.

## Failures / limits

- All planned + justified searches succeeded; no X tool errors; remaining was never 0.
- MUST_WIN / MUST_WIN2 / MUST_WIN3 / several KW and mention searches hit max_results=25 with next_token. No pagination (per rules). deMiners official posts may have been crowded out of MUST_WIN3 by @usehelipaid / @tryopencom; progress was refreshed via OpenSea, not a second X read.
- Some write_to_file X assets were mid-truncated previews; full sibling asset files were restored via `save_xraw.py` without re-querying.
- `ingest_direct.py` initially omitted `SILENT_LZ` from its ORDER list; the helper was patched in `/tmp/r2193/ingest_direct.py` and ingest was re-run. Usage is xReads 28 / main 27 / silent 1.
- OpenSea HTML pages were large; collection + stats APIs were used for Ugly Puggies / deMiners / The Jacket. NFT Calendar (Blockpay) returned 403. Oneshot/Overdrive official sites are thin SPAs (little extractable body).
- Antopia NFT `totalSupply()` reverts; `totalMinted()` / `MAX_SUPPLY()` / `freeClaimed()` / `freeRemaining()` / `saleOpen()` were used instead.
- Beware extract.py LE2H notes that treat some UTC clock fields as CST (2hourfun firstWindowAtUTC, Shielded publicMintAtUTC). Official conversions used here: 21:00 UTC = 2026-11-26 05:00 CST.
- This bot does not auto-mint.

## Notify

- **notify = true**
- Reason: four true new admits this round, including F0B90B (self-claimed first-3 free, not LIVE) and Antopia (paid LIVE, free cap exhausted). No pre-committed must-notify item (Ugly Puggies first ≤2h is not due yet). No re-alert for Ugly Puggies / ORIPA / deMiners / The Jacket / ZeroGate / Helipaid / Anthropos / SecretWiz / BLOCKPAY Genesis without a new material change. No early first ≤2h for Ugly Puggies, Agent Cards, deMiners public sale, 2hourfun, or Shielded Wizards public.
- Alert names each @handle. Named free mint/registration items: F0B90B (upcoming, not LIVE) and Antopia (free cap exhausted; not currently claimable free LIVE).
- `dsFallback=false`. DeepSeek alert draft was too short (“详见 PANEL”); the executor expanded it so every new admit is named with handles and key facts, and the panel URL is spelled out.

Alert copy is in `/tmp/r2193/notify.json` (`alertMessage`).


## Parent apply / Discord Peek merge

- Applied to repo data.json at **2026-11-25 19:56:07 CST** (APPLY_ALLOW_WORKSPACE=1, APPLY_MERGE_DISCORD=1). lastScout/updated stamped at apply time.
- Discord Peek this same round: computerUse hit login wall at 2026-11-25 19:39:07 CST; loginOk=false, channelsPeeked=false, lastSeen unchanged (alpha-1 2026-11-23 22:19 CST etc.). nag=false (R2158 already asked the user to re-login). Do not re-peek or nag this round.
- docsSynced and lastPushSha are set at push time.
