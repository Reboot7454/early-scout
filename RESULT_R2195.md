# R2195 Early Scout X-radar Result

- Round: **R2195** (meta.round 2194 + 1)
- lastScout written (dry-run apply): **2026-11-25 21:24:21 CST** (Asia/Shanghai)
- Fire window: about 2026-11-25 21:04–21:24 CST
- lastFullAfterReset: **R2170** (normal incremental; not 08:00 CST first full backfill)
- Panel: https://reboot7454.github.io/early-scout/
- Dry-run data: `/tmp/r2195/data.json` (source `/tmp/r2195/data.json.src`; **did not** modify `/workspace/early-scout/data.json`; no commit/push)
- notify.json: `/tmp/r2195/notify.json`
- apply script: `/tmp/r2195/apply_r2195.py`
- This file: `/tmp/r2195/RESULT_R2195.md`

## X budget and reads

- Live remainingBefore (first X footer: UF1 remainingToday=312, so before that read): **313/1000**
- remainingAfter (last footer, KW_STARK_24 remainingToday=286): **286/1000**
- **xReads = 27** (main 26 + silent 1)
  - Planned incremental: 24 main + 1 silent = 25 (UF1/UF2/UF3, MUST_WIN/MUST_WIN2/MUST_WIN3, MUST_OFF, 10 lanes + KW_GAPS, MEN_PADS/MEN_GIWA/MEN_TAPE/MEN_LZ/MEN_ELY, SILENT_TAPE)
  - Justified thin-lane 24h backfills: **+2** (`KW_LZ_24`, `KW_STARK_24`)
- `x_budget.py 313` suggested mode=**pace**, softCap=18, minSpend=18, silentCap=2
- **Override (same as R2185–R2194):** remaining ≫ 200 and the user forbids cutting lanes when quota is ample, so the full incremental plan in queries.json was run (24 main + 1 silent, plus thin-lane 24h when 30m independent KW < 5). UF1/UF2/UF3 exist because the 50-account shard needed three `from:` batches (qlen cap; UF3 is a short leftover `@TapeExit`). MUST_WIN/MUST_WIN2/MUST_WIN3 are planned official `from:` batches (MUST_WIN3 exists because the must-win list is long, including R2193/R2194 official handles `@F0B90Bclub` `@antopia_xyz` `@OneshotExchange` `@indexitcash` `@agentcardshq` `@TheWishListSol` `@Interflylaunch`), not exploratory reads.
- Minute limit: stayed under 30/min; no retries, no pagination, no extra exploration.
- All planned searches in queries.json ran **once**. No NF retries. `@starx_xlayer` was already skipped in MUST_OFF `from:`.

### Lane coverage

- All **10 keyword lanes + KW_GAPS** ran (30m): yes
- Mentions this round: **pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest** (MEN_PADS, MEN_GIWA, MEN_TAPE, MEN_LZ, MEN_ELY)
- Next-round mentions should rotate to: **DogeEVM / BTC / Starknet / squeek / STARX** (those mention sets were not run this round)
- Silent this round: **Tape/电路** (`SILENT_TAPE`, 24h, 0 hits, outside softCap). Next silent lane: **GIWA** (2196 % 11 = 7)
- UF shard: cursor **1811 @usegnomon**, 50 accounts through **@TapeExit**, wrap=false, next **1861 @pumptoksocial**, library UF total after apply **2415** (was 2412; +@freakapesnft +@CityHood_NFT +@OUTLAWSxNFT)

### Thin-lane 24h backfill

30m independent KW hit counts and decisions:

| Lane | 30m id | 30m hits | 24h backfill |
|------|--------|----------|--------------|
| LayerZero | KW_LZ | **0** (<5) | **yes** KW_LZ_24 (25, capped) |
| Tape | KW_TAPE | **25** | no |
| GIWA | KW_GIWA | **25** | no |
| DogeEVM | KW_DOGE | **13** | no |
| BTC | KW_BTC | **10** | no |
| Starknet | KW_STARK | **2** (<5) | **yes** KW_STARK_24 (25, capped) |

- KW_MINE 30m = 0; MINE is a core lane — **no** 24h added just because it is low.
- Core/fat lanes MINT/PAD/GO/ELY/GAPS were already ≥5 (KW_ELY=17) — no 24h.

### Per-search result counts (after ingest, SILENT_TAPE included)

UF1 1, UF2 0, UF3 0, MUST_WIN 25 (capped, next_token), MUST_WIN2 25 (capped), MUST_WIN3 25 (capped), MUST_OFF 1, KW_LZ 0, KW_TAPE 25, KW_GIWA 25, KW_DOGE 13, KW_BTC 10, KW_STARK 2, KW_MINT 25, KW_MINE 0, KW_PAD 25, KW_GO 25, KW_ELY 17, KW_GAPS 25, MEN_PADS 17, MEN_GIWA 25, MEN_TAPE 8, MEN_LZ 25, MEN_ELY 24, SILENT_TAPE 0, KW_LZ_24 25, KW_STARK_24 25.

## New admits (DeepSeek score/admit, focus=false)

DeepSeek `ds_batch_score.py` (deepseek-flash, thinking on) scored three candidates. All three were admitted. focus=false. `links.x` and `links.twitter` both written as `https://x.com/<handle>`. candidate.round=2195. Each was hooked to **userFollowWatch + freeMintWatch** in the same apply.

1. **FREAKAPES @freakapesnft** — id `freakapes`, score **77** (early 92 / actionable 78 / novelty 66 / risk 55). Site https://freakapes.com/ (HTTPS 200, title FREAKAPES — 1,234 generative pixel apes). Account created **2026-11-16 20:57:05 CST**, 568 followers / following 76 / 74 posts, xUserId 2122312606769922048. JSON-LD `sameAs` and `twitter:site` are `@freakapesnft` (siteXMutual). Official site: 1,234 generative pixel apes on Robinhood Chain; **MINT PRICE / MINT DATE both TBA** (FAQ: “Date: Not decided yet. Price: TBA. The list hears first.”). Whitelist page https://wl.freakapes.com/ (title FREAKGUY whitelist) is open this round: connect X, finish follow/like/repost/post tasks, drop wallet. This is **free registration / allowlist open**, **not mint LIVE**, and **not a confirmed free mint**. No official post from this handle this round (profile only in KW_MINT includes). No OpenSea collection URL, no CA. Watches: userFollowWatch + freeMintWatch.

2. **CITYHOOD @CityHood_NFT** — id `cityhood-nft`, score **68** (early 88 / actionable 70 / novelty 72 / risk 45). Site https://cityhood.online/ (HTTPS 200). Account created **2026-11-12 16:56:43 CST**, 894 followers / following 397 / 8 posts, xUserId 2120802580511019009. Frontend JS hardcodes `VITE_X_URL=https://x.com/CityHood_NFT` (siteXMutual). **This is a different project from the already-admitted `cityhood` / @appcityhood / https://cityhood.fun**; the existing card already says not to merge them. Frontend targets Robinhood mainnet (chain id 4663), `VITE_LAND_MAX_SUPPLY=5000`, contracts CITY `0x19016d3022f1Ff285657e41fDbC7432F26b80A13`, LAND `0x9a22e0189FCEFf28c0c8c87D2BbC3b2E61F901f6`, SALE `0xa54020EA91e8Ff79c859C5095115f8F04a1673D0`. Backend `https://cityhoodbackend-production.up.railway.app/api/config` this round returns **chainId=46630, chainName=Robinhood Chain Testnet** with the same addresses, so these contracts must **not** be treated as confirmed mainnet mint LIVE. Citizenship registration is open (`citizenship_open=true`). Grab Land copy says 5,000 $CITY packs at 0.0009 ETH for a land key, then “free land mint with a key,” plus “Grab Land opens soon / Practise on the demo island.” Third-party claims of a 3,333 free mint do **not** match the official 5,000 land cap and are not used as official wording. No official post from this handle this round. **Not confirmed mainnet free mint LIVE.** Watches: userFollowWatch + freeMintWatch.

3. **OUTLAWS @OUTLAWSxNFT** — id `outlawsxnft`, score **72** (early 58 / actionable 86 / novelty 48 / risk 62). Account created **2022-12-19 22:55:38 CST**, 5,025 followers / following 4 / 16,259 posts, xUserId 1604852914614595584. Profile URL https://opensea.io/collection/outlawsxnft/overview. Bio self-claims 6,666 supply, Free Mint on OpenSea, Nov 27 | 1:30 PM UTC. OpenSea collection API: name OUTLAWSxNFT, `twitter_username` empty (weaker mutual proof), CA `0xf5be4d8c1ae8f281297dedf337e93940e8a59b81` (Robinhood Chain), total_supply/unique_item_count=**0**. Drop page `mintStatus=MINTING_SOON`, maxSupply=6666, totalSupply=0, activeDropStage=null. SeaDrop stages (Asia/Shanghai CST): SIGNED_PRESALE 1 **2026-11-27 21:30–22:30 CST**; SIGNED_PRESALE 2 **22:30–23:30 CST**; PUBLIC_SALE **2026-11-27 23:30 CST to 2026-11-28 21:30 CST**. First stage matches the bio’s 1:30 PM UTC. No official post this round; drop page did not independently show a unit price, so the **public stage must not be called free**. **Not LIVE**, first ≤2h starts about **2026-11-27 19:30 CST**. Watches: userFollowWatch + freeMintWatch.

## Seen but not admitted

- **Tine @TineProtocol** (https://tine.money/, account created 2026-11-24 21:38:57 CST, 6 followers / 5 posts). Official site mutual with the handle; ETH savings / TINE farm, public security review dated 25 November 2026, Telegram + X links. This is a pre-launch/DeFi protocol, not a mint or launchpad window. Not admitted.
- **Kimchi @kimchi_giwa** (https://usekimchi.xyz/, created 2026-11-23 21:18:51 CST, 0 followers). GIWA testnet market-making bench; site returned HTTP 403 this round; no official post in-round. Not admitted.
- **Loosh Protocol @LooshProtocol** (https://loosh-protocol.netlify.app, 36d, 1 follower). Self-described fair launch, CA still `TBA_DEPLOYING_SOON`; also shilled @pumpdotfun. High-risk / no CA. Not admitted.
- **TAIL @tailtradesxyz** (https://tailtrades.xyz/, 6.35d, 10 followers). Already-live Hyperliquid/Elysium trading desk with published CA `0xC6333959D096f151dee397AC56c9259a1127B870`. Not a mint. Not admitted.
- **Valhist** (site https://valhistgame.space/ lists official @valhist; aggregator @TheronHale87 claimed an invitation NFT free mint of 200 on Base, GTD then FCFS, URL https://valhistgame.space/invitation). Official handle was **not** an author this round. OpenSea collection API for `valhist-game` returned **401** this round, so mint LIVE / supply could not be independently verified. Token CA on the homepage: `0xC082bc6B887238A999bB754819a6beD5e314EAD7` (Base). **Not admitted** pending an official post or a verified OpenSea/on-chain mint status. Do not treat the aggregator as official.
- **BLOCKPAY Genesis @BlockpayGenesis** — still no independent official site/CA this round (not in MUST 24h hits either). Do not force-admit, do not re-push.
- Third-party / giveaway / watcher noise skipped (no official handle+site loop to admit): `@supersmoney` (already-known @AscendLaunch, “not open yet”), Cityhood free-mint RTs that actually point at **@CityHood_NFT** (now admitted separately; the 3,333 figure is unofficial), Spike / GearVault giveaway RTs (already in library), `@OUTLAWSxNFT` was admitted from official bio + OpenSea drop rather than third-party RTs.

## Library updates (re-alert only on material change or first ≤2h)

- **Ugly Puggies @uglypuggies — first ≤2h, notify.** Official open still **2026-11-25 23:00 CST** (15:00 UTC). Same 19:00 CST “T-4 hours / All wl has been added” official post (https://x.com/uglypuggies/status/2125545156292309490). OpenSea collection API: total_supply/unique_item_count **0**, twitter_username=uglypuggies, CA `0xe2be23fbffe892feb3677341765847b9309663c2` (robinhood), owners 0. Drop page `mintStatus=MINTING_SOON`, activeDropStage=null, maxSupply=777; first SIGNED_PRESALE still 23:00–23:30 CST, later signed stages and PUBLIC_SALE 2026-11-27 13:30 CST unchanged. Card `le2h=true`. Self-claimed free mint (777, Robinhood), **not confirmed LIVE**. Do not treat the unofficial 21:00 CST window as the open time.

- **Agent Cards @agentcardshq — first ≤2h, notify.** The recorded reprint window is still **2026-11-25 23:00 CST** (15:00 UTC) AGENTMINT (Agent ID fair mint, First 5,000 shares, from the prior reprint note). MUST 24h had **zero** posts from @agentcardshq; no move or cancellation seen. Card `le2h=true`. **Do not call this free mint** — no official source this round says the 23:00 window is free. Existing CARDS presale / Agent ID hero-card freeLIVE is a previously alerted line, not this new reminder.

- **deMiners @deMinersNft — material schedule change, notify; do not send a stale 22:30 public first ≤2h.** MUST 24h had no official posts. OpenSea collection API: **505/3333** (R2194 499/3333), owners **134** (was 130), floor **0.00059 ETH**. Drop page: `mintStatus=MINTING`, activeDropStage still stageIndex=2 (OG list), erc721.totalSupply **508/3333**. **Times changed on the live drop page:** OG SIGNED_PRESALE now ends **2026-11-25T16:30:04.000Z = 2026-11-26 00:30:04 CST** (previously stored 2026-11-25 22:30:04 CST / 14:30:04 UTC). Paid PUBLIC_SALE now starts at the same 00:30:04 CST stamp, price still **0.0002 ETH (NOT free)**, through 2026-11-28 00:30:04 CST. OG free mint (0 ETH, 3/wallet) is **still LIVE and extended**. First ≤2h for the **new** public time starts at **22:30 CST**; this fire (~21:04–21:16 CST) is still early, so do **not** send a public first ≤2h, and do **not** use the old 22:30 CST open time. Card `le2h=false`.

- **ORIPA @oripaxyz** — still live and inside 2h (until 22:00 CST). Official posts continue ripping progress (20:58 CST 10K packs / 14K USDC to stakers; 20:39 CST reloading inventory; 20:23 CST 100K USDC in 23 min). Not free mint. R2190 already sent first ≤2h. **No re-push.** Card `le2h` stays true.

- **The Jacket @TheJacket_NVDA** — holder free mint still LIVE; public still 0.0003 ETH. OpenSea the-jacket-man collection API **205/777** (R2194 204/777), owners 129 (was 128), floor **0.81 USDG** (was 1.0 USDG). MUST again saw the already-alerted 18:23 CST “Mint is open” post. **No re-push.**

- **F0B90B @F0B90Bclub** — still mint LIVE, no rule change. Public BSC RPC about **2026-11-25 21:15:59 CST**: mintOpen=true, totalMinted **215/10000** (R2194 177), remaining 9785. MUST 24h had no official posts. **No re-push.**

- **Antopia @antopia_xyz** — public BSC RPC about **2026-11-25 21:15:59 CST**: saleOpen=true, totalMinted still **6244/8888**, freeClaimed 4000/4000, freeRemaining 0, totalSupply() still reverts. Official 18:40 CST reply previews Clash of Antopia “goes live tomorrow,” not a mint-rule change. **No re-push.**

- **TRIFORGE @TriForgeAgent** — public BSC RPC about **2026-11-25 21:15:23 CST**: Forge Keys **409/3333** (R2194 367/3333; official 20:15 CST post still said 364/3,333), paused=false; lpMintOpen=true, lpTotalMinted=0; claimsOpen=true, totalClaimed **8** (was 6); miningShares still 6; tradingEnabled=false. Small/progress-only. **No re-push.**

- **Interfly @Interflylaunch** — same already-alerted 20:29 CST official post also names native `$IF` CA `0x2B8Fc1D31B1fe556587656ac2DFbc510B88733f0`; site footer still points at factory `0xb9bb1d7b714c649df9e3a70f00b17ccc4624b887`; page stats still 0 tokens / $0 volume. 20:52 CST post explains unsold-holder 2x weight. Not free mint. Card updated with the token CA. **No re-push.**

- **WishList @TheWishListSol** — MUST again saw the already-admitted 20:30 CST official post; site still has no CA. **No re-push.**

- **ZeroGate @ZeroGate0G** — 18:03 CST official post says zero-gravity:native is live, CA `0xca2E57985A339E130775597332fc55ea0f917777`. Still treated as previously alerted live launchpad, not a shutdown. **No re-push.**

- **2hourfun @2hourfun** — official posts again confirm **21:00 UTC = 2026-11-26 05:00 CST** (https://x.com/2hourfun/status/2125546944319660036 and https://x.com/2hourfun/status/2125575505353039959). **No early alert.**

- **Shielded Wizards @ShieldedWizBTC** — no official post in MUST 24h. Public mint still **2026-11-26 05:00 CST** (21:00 UTC). WL free mint still previously alerted LIVE. **No early alert, no re-push only for still being LIVE.**

- Helipaid, Oneshot, IndexIt, SecretWiz, Anthropos and other already-alerted names: no material change that the user has not heard. **No re-push.**

## discordPeekDeferred

Placeholder left for the parent to merge `/tmp/r2195/discord_peek.json` if present. This executor did not spend time on Discord. A file was already in the workdir at fire (`loginOk=false`, `loginWall=true`, `channelsPeeked=false`, attemptedAt **2026-11-25 21:07:46 CST**); dry-run apply did **not** auto-merge it (`APPLY_MERGE_DISCORD` unset), and `meta.discordPeekDeferred=true`.

## Failures / limits

- OpenSea drop list endpoints returned 401/404 without an API key; stage times and mintStatus were taken from the public collection HTML drop pages plus collection/stats APIs (those collection/stats calls succeeded this round, including Ugly Puggies stats).
- `usekimchi.xyz` HTTP 403.
- OpenSea collection API for `valhist-game` returned 401 (not retried as an extra X read; not used as a second OpenSea key hunt).
- MUST_WIN / MUST_WIN2 / MUST_WIN3 / several KW and MEN searches capped at 25 with next_token; no pagination, per rules.
- SILENT_TAPE returned 0 posts.
- DeepSeek scoring succeeded (`dsFallback=false`).
- No X tool errors. remainingToday never hit 0.

## Notify

- **notify=true**
- Reason: Ugly Puggies first ≤2h (official 23:00 CST still holds, not LIVE); Agent Cards first ≤2h (reprint 23:00 CST window still holds, no official post this round, not called free mint); deMiners paid-public time moved to 2026-11-26 00:30 CST (material change; OG free extended; do not send stale 22:30 first ≤2h); new admits FREAKAPES (free WL registration), CITYHOOD @CityHood_NFT (citizenship open, not mainnet free mint LIVE), OUTLAWS (self-claimed free mint dated 2026-11-27 21:30 CST, not LIVE).
- namedFreeMintOrRegistration: FREAKAPES @freakapesnft (WL open, mint TBA); CITYHOOD @CityHood_NFT (citizenship open, not mainnet free mint LIVE); Ugly Puggies @uglypuggies (self-claimed free mint, first ≤2h, not confirmed LIVE); deMiners @deMinersNft (OG free still LIVE, already alerted R2191, window extended; public is not free); OUTLAWS @OUTLAWSxNFT (self-claimed free mint, not yet open).
- dsFallback: false
- alertMessage is in `/tmp/r2195/notify.json` (handles named).

> R2195：Ugly Puggies @uglypuggies 首次 ≤2h，官窗仍 2026-11-25 23:00 CST（15:00 UTC），OpenSea 仍 0/777、MINTING_SOON，尚未开铸；自称免费 mint，不是已确认 LIVE。Agent Cards @agentcardshq 翻印窗仍 23:00 CST 的 AGENTMINT，本轮未见新官帖、未见改期，发首次 ≤2h，不写成免费 mint。deMiners @deMinersNft 实质改期：OpenSea drop 把 OG 截止和付费公售开始从 22:30:04 CST 改到 2026-11-26 00:30:04 CST；OG 免费 mint 仍 LIVE 并被延长，公售仍是 0.0002 ETH（不是免费）。不要按旧的 22:30 CST 发公售首次 ≤2h；新窗首次 ≤2h 从今晚 22:30 CST 才开始。OpenSea collection API 505/3333（drop 页 508）。新收录 FREAKAPES @freakapesnft（https://freakapes.com / https://wl.freakapes.com），免费白名单登记已开（连 X、做任务、交钱包），mint 日期和价格仍 TBA，不是已开铸。新收录 CITYHOOD @CityHood_NFT（https://cityhood.online，不是已收录的 @appcityhood / cityhood.fun），市民登记已开；后端仍报 Robinhood Chain Testnet，不是已确认的主网免费 mint LIVE。新收录 OUTLAWS @OUTLAWSxNFT，简介自称免费 mint，OpenSea 合集 0xf5be4d8c1ae8f281297dedf337e93940e8a59b81、0/6666，首阶段 2026-11-27 21:30 CST，尚未开铸。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
