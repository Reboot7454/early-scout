# R2194 Early Scout X-radar Result

- Round: **R2194** (meta.round 2193 + 1)
- lastScout written (dry-run apply): **2026-11-25 20:46:09 CST** (Asia/Shanghai)
- Fire window: about 2026-11-25 20:26–20:46 CST
- lastFullAfterReset: **R2170** (normal incremental; not 08:00 CST first full backfill)
- Panel: https://reboot7454.github.io/early-scout/
- Dry-run data: `/tmp/r2194/data.json` (source `/tmp/r2194/data.json.src`; **did not** modify `/workspace/early-scout/data.json`; no commit/push)
- notify.json: `/tmp/r2194/notify.json`
- apply script: `/tmp/r2194/apply_r2194.py`
- This file: `/tmp/r2194/RESULT_R2194.md`

## X budget and reads

- Live remainingBefore (first X footer: UF1 remainingToday=340, so before that read): **341/1000**
- remainingAfter (last footer, KW_STARK_24 remainingToday=313): **313/1000**
- **xReads = 28** (main 27 + silent 1)
  - Planned incremental: 24 main + 1 silent = 25 (UF1/UF2/UF3, MUST_WIN/MUST_WIN2/MUST_WIN3, MUST_OFF, 10 lanes + KW_GAPS, MEN_DOGE/MEN_BTC/MEN_STARK/MEN_SQUEEK/MEN_STARX, SILENT_ELY)
  - Justified thin-lane 24h backfills: **+3** (`KW_LZ_24`, `KW_BTC_24`, `KW_STARK_24`)
- `x_budget.py 340` suggested mode=**pace**, softCap=18, minSpend=18, silentCap=2
- **Override (same as R2185–R2193):** remaining ≫ 200 and the user forbids cutting lanes when quota is ample, so the full incremental plan in queries.json was run (24 main + 1 silent, plus thin-lane 24h when 30m independent KW < 5). UF1/UF2/UF3 exist because the 50-account shard needed three `from:` batches (qlen cap; UF3 is a short leftover `@Gloopix_`). MUST_WIN/MUST_WIN2/MUST_WIN3 are planned official `from:` batches (MUST_WIN3 exists because the must-win list is long, including R2193 new official handles `@F0B90Bclub` `@antopia_xyz` `@OneshotExchange` `@indexitcash` and reprint-window `@agentcardshq`), not exploratory reads.
- Minute limit: stayed under 30/min; no retries, no pagination, no extra exploration.
- All planned searches in queries.json ran **once**. No NF retries. `@starx_xlayer` was already skipped in MUST_OFF `from:`; MEN_STARX mentions of `@starx_xlayer` were allowed (mentions, not `from:`).

### Lane coverage

- All **10 keyword lanes + KW_GAPS** ran (30m): yes
- Mentions this round: **DogeEVM / BTC / Starknet / squeek / STARX** (MEN_DOGE, MEN_BTC, MEN_STARK, MEN_SQUEEK, MEN_STARX)
- Next-round mentions should rotate to: **pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest** (those mention sets were not run this round)
- Silent this round: **Elysium** (`SILENT_ELY`, 24h, 11 hits, outside softCap). Next silent lane: **Tape/电路** (2195 % 11 = 6)
- UF shard: cursor **1761 @reelsliq**, 50 accounts through **@Gloopix_**, wrap=false, next **1811 @usegnomon**, library UF total after apply **2412** (was 2409; +@TheWishListSol +@Interflylaunch +@Keelfunapp appended to the existing Keelfun watch)

### Thin-lane 24h backfill

30m independent KW hit counts and decisions:

| Lane | 30m id | 30m hits | 24h backfill |
|------|--------|----------|--------------|
| LayerZero | KW_LZ | **1** (<5) | **yes** KW_LZ_24 (25, capped) |
| Tape | KW_TAPE | **25** | no |
| GIWA | KW_GIWA | **25** | no |
| DogeEVM | KW_DOGE | **25** | no |
| BTC | KW_BTC | **3** (<5) | **yes** KW_BTC_24 (25, capped) |
| Starknet | KW_STARK | **1** (<5) | **yes** KW_STARK_24 (25, capped) |

- KW_MINE 30m = 1; MINE is a core lane — **no** 24h added just because it is low.
- Core/fat lanes MINT/PAD/GO/ELY/GAPS were already ≥5 (KW_ELY=17) — no 24h.

### Per-search result counts (after ingest, SILENT_ELY included)

UF1 3, UF2 0, UF3 0, MUST_WIN 25 (capped, next_token), MUST_WIN2 25 (capped), MUST_WIN3 25 (capped), MUST_OFF 1, KW_LZ 1, KW_TAPE 25, KW_GIWA 25, KW_DOGE 25, KW_BTC 3, KW_STARK 1, KW_MINT 25, KW_MINE 1, KW_PAD 25, KW_GO 25, KW_ELY 17, KW_GAPS 25, MEN_DOGE 8, MEN_BTC 25, MEN_STARK 4, MEN_SQUEEK 0, MEN_STARX 0, SILENT_ELY 11, KW_LZ_24 25, KW_BTC_24 25, KW_STARK_24 25.

## New admits (DeepSeek score/admit, focus=false)

DeepSeek `ds_batch_score.py` (deepseek-flash, thinking on) scored three candidates. **WishList** and **Interfly** were admitted. **KeelFun @Keelfunapp was not admitted as a new project** (see seen-but-not-admitted): the same site `keelfun.app` is already in the library as `keelfun` / `@Keelfunxyz` (R2017).

1. **WishList @TheWishListSol** — id `wishlist-sol`, score **56** (early 95 / actionable 42 / novelty 72 / risk 78). Site https://thewishlist.site/ (HTTPS 200, title WishList, og:title WishList ($WISH)). Account created **2026-11-25 15:51:13 CST**, 0 followers / following 3 / 1 post, xUserId 2125496969825300480. Site JS and `/config.json` hardcode `xUrl` https://x.com/TheWishListSol (siteXMutual). Official post **2026-11-25 20:30:41 CST** (https://x.com/TheWishListSol/status/2125567850173911297): prize-catalog launchpad (118 prizes; official post examples include a $10 Starbucks card to a Rolex); trading fees fill a wish pot; one holder gets the gift. Frontend shows “CA: coming at launch”; pump.fun/coin/{mint} link template only. No CA this round. **Not a free mint.** Watches: userFollowWatch. focus=false.

2. **Interfly @Interflylaunch** — id `interfly`, score **54** (early 90 / actionable 52 / novelty 48 / risk 72). Site https://interfly.fun/ → https://www.interfly.fun/ (HTTPS 200, title Interfly · Token launchpad on Base). Account created **2026-11-24 12:18:54 CST**, 1 follower / following 5 / 5 posts, xUserId 2125081259810451456. Footer X https://x.com/Interflylaunch (siteXMutual). Site Contract points to https://basescan.org/address/0xb9bb1d7b714c649df9e3a70f00b17ccc4624b887. Official post **2026-11-25 20:29:14 CST** (https://x.com/Interflylaunch/status/2125567486829658130) says Interfly is live on Base: no bonding curve / graduation, each coin opens in its own Uniswap V4 pool. Page stats this round: 0 tokens, $0 volume, $0 fees, 0 trades. Platform self-claimed LIVE, **not a free mint**. Watches: userFollowWatch. focus=false.

## Seen but not admitted

- **BLOCKPAY Genesis @BlockpayGenesis** — still no independent official site/CA this round (not in MUST 24h hits either). Do not force-admit, do not re-push.
- **@Keelfunapp** — official-looking Base fair-launch pad, site https://keelfun.app/ (HTTPS 200, Tokens launched 0, Volume $0; docs + GitHub https://github.com/keelfun/keelfun). This is **not a new project**: the same site is already card `keelfun` with official handle **@Keelfunxyz** (admitted R2017). The live site now lists https://x.com/keelfunapp (account created 2026-11-22 07:09:35 CST, 30 followers / 8 posts, xUserId 2124278821306163201), which is a **different account** from @Keelfunxyz. No official post from @Keelfunapp this round (it appeared only as a keyword-result profile). Apply updates the existing `keelfun` card and hooks `@Keelfunapp` onto that card’s userFollowWatch. Does not change the primary handle. Not a new admit, no re-push, not a free mint.
- **@luppfun** (https://lupp.fun/) — BNB AI-agent token launchpad in bio; official site **HTTP 503** “Under maintenance” this round, and no official post in-round (`post_count_in_round=0`). Skipped.
- **@stargaze_fit** (https://www.stargaze.fit) — official post introducing STARGAZIUM / $STARIUM; bio CA `0x169b8866164ed45bcf658606c1c5f7346f58d0e9`. Site still has template Placeholders, “Factory not deployed”, and a Sepolia launch form. Not admitted.
- Third-party / giveaway / watcher noise skipped (no official handle+site loop): `@supersmoney` (talking about already-known @AscendLaunch), RT giveaway accounts, KOLs, `@JokerFaceCM` (~27d, $CBUCKS Dec 3 teaser), `@NLYRAProject` (~40d points season).

## Library updates (no re-alert without material change except F0B90B LIVE)

- **F0B90B @F0B90Bclub** — **material change, notify.** R2193 admitted it as contracts still deploying / mint opening soon / no CA. This round official `https://f0b90b.pages.dev/config.js` now fills NFT `0xa5d6ed5a0b50F97e94Cfc13618da24EEF8d28Cce`, Token `0x27958278e28623EE8D1fD89d2ab1a4706f2e50B0`, ACCOUNT_IMPL `0x2DaDf10Eb36EC45e1cFdFa11E9E09987EbB57F83` (R2193 HTML did not yet have the footer contract links). Public BSC RPC (about **2026-11-25 20:40:28 CST**, https://bsc-dataseed.binance.org/): both NFT and Token `name()=F0B90B` with bytecode; NFT `mintOpen()=true`, `totalMinted()=177`, `MAX_SUPPLY()=10000`, `remaining()=9823`. Rules unchanged: first 3 FREE, then 0.0003 BNB, max 10/wallet, Binance Agent ID gate. **Newly confirmed mint LIVE, including the free first-3.** Card status `live`, `freeLIVE/freeMintLIVE=true`. This bot does not auto-mint.
- **Ugly Puggies @uglypuggies** — official window still **2026-11-25 23:00 CST** (15:00 UTC). Same 19:00 CST “T-4 hours / All wl has been added” official post (https://x.com/uglypuggies/status/2125545156292309490). OpenSea collection API: total_supply/unique_item_count **0**, twitter_username=uglypuggies, CA `0xe2be23fbffe892feb3677341765847b9309663c2` (robinhood). Stats endpoint returned 401 (no API key); supply came from the collection endpoint. Card `le2h=false`. First ≤2h starts **21:00 CST**; this fire started ~20:26, before that. Not LIVE. **No re-push, no early first ≤2h.**
- **ORIPA @oripaxyz** — official post **20:01 CST** (https://x.com/oripaxyz/status/2125560380592435230) says “is live / Let the ripping begin”, matching the already-known first-pack time **2026-11-25 20:00 CST** (8 PM GMT+8 / 12:00 UTC, not 12:00 CST). Another 20:01 CST post: missed allowlist can mint an Early Bird badge for tomorrow 8 PM GMT+8. Official site HTTPS 200, page text “4 pools open now”. Not free mint. Card status set to `live`, `le2h` stays **true** (still inside 2h). R2190 already sent first ≤2h. **No re-push.**
- **deMiners @deMinersNft** — no new official post in MUST 24h. OpenSea collection API: **499/3333** (R2193 492/3333), 130 owners (was 128), floor **0.00059 ETH**. OG free mint still LIVE until 22:30:04 CST (0 ETH, 3/wallet). Public sale 22:30 CST at 0.0002 ETH; first ≤2h for public starts 20:30 CST — fire started ~20:26, **slightly before 20:30**. Card `le2h=false`. **Do not early-alert; public is not free.** Small progress only. **No re-push.**
- **The Jacket @TheJacket_NVDA** — same already-alerted “Mint is open / 4444→777 / holder free” official post. OpenSea collection API: **204/777** (R2193 194/777), 128 owners (was 126), floor **1.0 USDG** (R2193 0.48 USDG; secondary market). Holder allowlist still free; public still 0.0003 ETH. Progress / floor move only. **No re-push.**
- **Antopia @antopia_xyz** — no new official post in MUST 24h. Public BSC RPC (about **2026-11-25 20:38:18 CST**): `saleOpen()=true`, `totalMinted()=6244` (R2193 5889), `MAX_SUPPLY()=8888`, `freeClaimed()=4000`, `FREE_CAP()=4000`, `freeRemaining()=0`, `X_FREE_CAP()=500`; `totalSupply()` still reverts. Paid mint still open at 0.00088 BNB; free cap still exhausted. **No re-push only for still being paid-LIVE or progress.**
- **TRIFORGE @TriForgeAgent** — official post 20:15 CST still wrote 364/3,333. Public BSC RPC about **2026-11-25 20:36:19 CST**: Forge Keys **367/3333**, paused=false, lpMintOpen=true, lpTotalMinted=0, claims=6, miningShares=6, tradingEnabled=false. Small +3 vs R2193 364. Update card only, **no re-push**.
- **ZeroGate @ZeroGate0G** — MUST 24h still shows the already-recorded 18:03 CST “zero-gravity:native is live” post (CA `0xca2E57985A339E130775597332fc55ea0f917777`). Not a confirmed shutdown. Not free mint. **No re-push.**
- **Helipaid @usehelipaid** — many Privacy Ring product posts; no chain/price/free-window change. **No re-push.**
- **2hourfun @2hourfun** — official post 19:07 CST (https://x.com/2hourfun/status/2125546944319660036) again says open at **21:00 UTC = 2026-11-26 05:00 CST**. Do not read as today 21:00 CST. **No early alert.**
- **Shielded Wizards @ShieldedWizBTC** — same 18:50 CST official post: public mint **21:00 UTC = 2026-11-26 05:00 CST**. WL free mint still LIVE (already alerted R2165). Public first ≤2h ~03:00 CST. **No early alert, no re-push only for still being LIVE.**
- **Agent Cards @agentcardshq** — no official post in MUST 24h this round. Reprint window still 23:00 CST; first ≤2h at 21:00 CST. Fire started ~20:26, **not yet**. Card `le2h` stays false. **No early alert.**
- **Oneshot @OneshotExchange** — MUST_WIN3 included 19:39 CST $ONE tokenomics / airdrop-task posts, which were already inside the R2193 window (lastScout 19:56:07 CST). Still not a free mint. **No re-push.**
- **IndexIt @indexitcash / Anthropos / SecretWiz** — no new material change requiring a re-push.

False LE2H from extract.py were ignored: `2hourfun` `firstWindowAtUTC` and `ShieldedWizBTC` `publicMintAtUTC` showing “2026-11-25 21:00 CST” are 21:00 **UTC** = **2026-11-26 05:00 CST**. `ugly-puggies` `priorThirdPartyOpenCST` 21:00 remains the unofficial window already rejected in R2192. `firstLe2hAtCST` 21:00 is the correct start of the official ≤2h window, but this fire was still before 21:00.

## discordPeekDeferred

Placeholder left for parent. `/tmp/r2194/discord_peek.json` may already exist from the parallel computerUse path; this executor did **not** run Discord and did **not** merge it (`APPLY_MERGE_DISCORD` unset). `meta.discordPeekDeferred=true` in the dry-run file. Parent should merge the real peek JSON if present.

## Failures / limits

- X: no tool errors; all 28 planned+justified searches wrote complete `x_raw` JSON (truncated previews restored via `save_xraw.py` full-text siblings, no re-query).
- `search_users` still unused / unavailable; silent path used planned `SILENT_ELY` mention+links fallback only (1 silent read).
- `lupp.fun` official site HTTP 503 this round.
- OpenSea collection stats for Ugly Puggies returned **401** (API key required); `total_supply=0` still came from `GET /api/v2/collections/ugly-puggies-106253855`. deMiners / The Jacket stats endpoints succeeded.
- DeepSeek: no fallback (`dsFallback=false`).
- This bot does not auto-mint.

## Notify

- **notify = true**
- Reason: F0B90B @F0B90Bclub is newly confirmed mint LIVE (first 3 still free, then 0.0003 BNB), which the user has not been told; also two new admits (WishList, Interfly) that are **not** free mints but must be named. No pre-committed first ≤2h this fire (Ugly Puggies / Agent Cards first ≤2h not due yet; deMiners public first ≤2h not due at fire ~20:26).
- namedFreeMintOrRegistration: **F0B90B @F0B90Bclub** (confirmed LIVE, first 3 free, then 0.0003 BNB)
- dsFallback: false
- alertMessage (also in `/tmp/r2194/notify.json`):

> R2194：F0B90B @F0B90Bclub 已确认开铸 LIVE。官网 config.js 现写入 NFT CA 0xa5d6ed5a0b50F97e94Cfc13618da24EEF8d28Cce、Token CA 0x27958278e28623EE8D1fD89d2ab1a4706f2e50B0；公共 BSC RPC 核到 mintOpen=true，totalMinted 177/10000，remaining 9823。规则未变：首 3 份免费，其后每份 0.0003 BNB，每钱包最多 10，需 Binance Agent ID。新收录 WishList @TheWishListSol（https://thewishlist.site/），Solana 奖品发射台，CA 尚未公布，不是免费 mint。新收录 Interfly @Interflylaunch（https://interfly.fun/），Base Uniswap V4 发射台已开，合约 0xb9bb1d7b714c649df9e3a70f00b17ccc4624b887，页面统计仍 0 发币，不是免费 mint。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/

## Parent apply / Discord Peek merge

- Applied to repo data.json at **2026-11-25 20:48:34 CST** (APPLY_ALLOW_WORKSPACE=1, APPLY_MERGE_DISCORD=1). lastScout/updated stamped at apply time. meta.xRemaining/remaining aligned to live remainingAfter **313/1000**; meta.silentLane=Elysium, silentNext=Tape/电路.
- Discord Peek this same round: computerUse hit login wall at 2026-11-25 20:30:39 CST; loginOk=false, loginWall=true, channelsPeeked=false, lastSeen unchanged (alpha-1 2026-11-23 22:19 CST etc.). nag=false (R2158 already asked the user to re-login). Do not re-peek or nag this round.
- docsSynced and lastPushSha are set at push time.
