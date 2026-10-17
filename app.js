(() => {
  const state = {
    data: null,
    category: "all",
    chain: "all",
    round: "all",
    roundPage: null, // 0-based; null = auto (prefer newest page)
    layerzero: "all",
    elysium: "all",
    miningFilter: "all", // unused for main; mining lives in panel
    miningTypeFilter: "all", // all | gpu-pow | nft-mutation | nft-miner | other
    scheduleFilter: "all", // all | soon24 | hasSchedule | onchain
    query: "",
    sort: "newest",
    nowMs: Date.now(),
    favorites: [], // candidate ids, client-only (localStorage)
  };

  /** localStorage key for personal favorites (array of candidate id strings). */
  const FAV_STORAGE_KEY = "early-scout-favorites";

  function loadFavorites() {
    try {
      const raw = localStorage.getItem(FAV_STORAGE_KEY);
      const arr = JSON.parse(raw || "[]");
      if (!Array.isArray(arr)) return [];
      return [...new Set(arr.map((id) => String(id)).filter(Boolean))];
    } catch {
      return [];
    }
  }

  function saveFavorites(ids) {
    state.favorites = [...ids];
    try {
      localStorage.setItem(FAV_STORAGE_KEY, JSON.stringify(state.favorites));
    } catch {
      /* quota / private mode — keep in-memory only */
    }
  }

  function isFavorite(id) {
    return state.favorites.includes(String(id));
  }

  function toggleFavorite(id) {
    const sid = String(id);
    let next = state.favorites.slice();
    if (next.includes(sid)) next = next.filter((x) => x !== sid);
    else next.push(sid);
    saveFavorites(next);
    return next;
  }

  function favBtnHtml(id) {
    const on = isFavorite(id);
    return `<button type="button" class="fav-btn${on ? " is-fav" : ""}" data-fav-toggle="${escapeHtml(String(id))}" title="${on ? "取消收藏" : "收藏"}" aria-label="${on ? "取消收藏" : "收藏"}" aria-pressed="${on ? "true" : "false"}">${on ? "★" : "☆"}</button>`;
  }

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => [...document.querySelectorAll(sel)];

  /** Round filter chips per page (~1–1.5 rows; keeps vertical space down). */
  const ROUND_PAGE_SIZE = 16;

  const RISK_RANK = {
    extreme: 4,
    high: 3,
    "medium-high": 2,
    medium: 1,
    low: 0,
  };

  const RISK_LABEL = {
    extreme: "极高",
    high: "高",
    "medium-high": "中高",
    medium: "中",
    low: "低",
  };

  const MINT_STATUS_LABEL = {
    unknown: "链上未知",
    not_open: "未开",
    open: "Mint 进行中",
    paused: "已暂停",
    sold_out: "已售罄",
  };

  function overallClass(n) {
    if (n >= 70) return "hi";
    if (n >= 55) return "mid";
    return "lo";
  }

  function scoreRow(c) {
    const s = c.scores;
    if (!s) return "";
    const minis = [
      ["早期", s.early],
      ["可动手", s.actionable],
      ["新鲜", s.novelty],
      ["风险", s.risk],
    ];
    const bars = minis
      .map(([lab, v]) => {
        const w = Math.max(4, Math.min(100, v));
        return (
          '<div class="score-mini" title="' +
          escapeHtml(lab) +
          ": " +
          v +
          '"><div class="score-mini-label"><span>' +
          escapeHtml(lab) +
          "</span><span>" +
          v +
          '</span></div><div class="score-mini-bar"><div class="score-mini-fill" style="width:' +
          w +
          '%"></div></div></div>'
        );
      })
      .join("");
    return (
      '<div class="score-row"><div class="score-overall ' +
      overallClass(s.overall) +
      '" title="综合评分">' +
      s.overall +
      '</div><div class="score-minis">' +
      bars +
      "</div></div>"
    );
  }

  function prosCons(c) {
    const hi = (c.highlights || []).slice(0, 4);
    const lo = (c.drawbacks || []).slice(0, 4);
    if (!hi.length && !lo.length) return "";
    const hiLis = hi.map((t) => "<li>" + escapeHtml(t) + "</li>").join("");
    const loLis = lo.map((t) => "<li>" + escapeHtml(t) + "</li>").join("");
    return (
      '<div class="pros-cons"><div class="pc-col hi"><div class="pc-title">亮点</div><ul>' +
      (hiLis || "<li>—</li>") +
      '</ul></div><div class="pc-col lo"><div class="pc-title">缺点</div><ul>' +
      (loLis || "<li>—</li>") +
      "</ul></div></div>"
    );
  }

  /** True only for candidates newly admitted this scout round (not mere whatsNew updates). */
  function isNewThisRound(c) {
    if (c && c.newThisRound === true) return true;
    const meta = state.data && state.data.meta;
    if (!meta || !c) return false;
    const r = Number(meta.round) || 0;
    const added = meta[`round${r}Added`];
    return Array.isArray(added) && added.includes(c.id);
  }

  function whatsNewBlock(c) {
    const t = (c.whatsNew || "").trim();
    if (!t) return "";
    const badge = isNewThisRound(c)
      ? '<span class="whats-new-badge">本轮新</span>'
      : '<span class="whats-new-badge whats-new-update">续更</span>';
    return (
      '<div class="whats-new">' +
      badge +
      "<span>" +
      escapeHtml(t) +
      "</span></div>"
    );
  }

  function xIcon() {
    return `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.727-8.835L1.254 2.25H8.08l4.253 5.622L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>`;
  }
  function siteIcon() {
    return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>`;
  }

  function escapeHtml(s) {
    return String(s ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  /** Display / filter canonical chain labels (merge case + synonym variants). */
  const CHAIN_CANON_MAP = {
    layerzero: "LayerZero",
    elysium: "Elysium",
    "elysium/hl": "Elysium",
    "elysium·hl": "Elysium",
    "elysium · hl": "Elysium",
    enter_elysium: "Elysium",
    "enter_elysium": "Elysium",
    "hyperliquid l2 / enter_elysium": "Elysium",
    zero: "LayerZero",
    "layerzero / zero": "LayerZero",
    "layerzero/zero": "LayerZero",
    "zero (layerzero)": "LayerZero",
    "zero(layerzero)": "LayerZero",
    tba: "TBA",
    tbd: "TBA",
    "未知 / tba": "TBA",
    "未知/tba": "TBA",
    未知: "TBA",
    robinhood: "Robinhood",
    "robinhood chain": "Robinhood",
    solana: "Solana",
    injective: "Injective",
    multi: "Multi",
    "multi-chain": "Multi",
    multichain: "Multi",
    "solana/multi": "Multi",
    "multi (solana / rh / bnb)": "Multi",
    "multi / robinhood chain": "Multi",
    "robinhood/solana": "Robinhood / Solana",
    "base / robinhood / arc": "Base / Robinhood / Arc",
    "ethereum / base": "Ethereum / Base",
    "bnb chain": "BNB Chain",
    ethereum: "Ethereum",
    base: "Base",
    bitcoin: "Bitcoin",
    monero: "Monero",
    ink: "Ink",
    arc: "Arc",
    giwa: "GIWA",
    icp: "ICP",
    canton: "Canton",
    interlink: "InterLink",
    nacre: "NACRE",
    omnichain: "Omnichain",
    "pearl l1": "Pearl L1",
    quantus: "Quantus",
    vearl: "Vearl",
    vela: "Vela",
    parano1d: "Parano1d",
  };

  function chainKey(ch) {
    return String(ch || "")
      .trim()
      .toLowerCase()
      .replace(/\s+/g, " ");
  }

  function canonicalChain(ch) {
    const raw = String(ch || "").trim();
    if (!raw) return "TBA";
    const key = chainKey(raw);
    if (CHAIN_CANON_MAP[key]) return CHAIN_CANON_MAP[key];
    // Title-case simple tokens; keep known separators
    return raw
      .split(/(\s*\/\s*|\s+)/)
      .map((part) => {
        if (/^\s*\/\s*$/.test(part) || /^\s+$/.test(part)) return part.replace(/\s*\/\s*/, " / ").replace(/^\s+$/, " ");
        if (!part) return part;
        if (/^[A-Z0-9]{2,}$/.test(part)) return part; // acronyms like ICP, GIWA, NACRE
        return part.charAt(0).toUpperCase() + part.slice(1);
      })
      .join("")
      .replace(/\s*\/\s*/g, " / ")
      .trim();
  }

  function chainsMatch(candidateChain, selectedCanon) {
    if (!selectedCanon || selectedCanon === "all") return true;
    return canonicalChain(candidateChain) === selectedCanon;
  }

  /** True only with clear LayerZero / Zero ecosystem evidence — not merely OFT/Omnichain in the name. */
  function isLayerZero(c) {
    // Self-claimed OFT/bridge without verification must NOT land here (→ 台子/Meme).
    if (c && c.lzVerified === false) return false;
    const tags = (c.tags || []).map((t) => String(t).toLowerCase());
    // Explicit layerzero / lz tag only when not marked unverified.
    if (tags.some((t) => t.includes("layerzero") || t === "lz" || t === "layer-zero")) {
      return true;
    }
    const canon = canonicalChain(c.chain);
    if (canon === "LayerZero") return true;
    const chain = String(c.chain || "").toLowerCase();
    if (chain === "layerzero" || chain === "zero" || chain.includes("layerzero")) return true;
    // Official-ecosystem wording only if lzVerified === true (avoid self-claim in background).
    if (c && c.lzVerified === true) {
      const blob = `${c.name} ${c.whyWatch || ""} ${c.background || ""}`.toLowerCase();
      return blob.includes("layerzero") || blob.includes("layer zero");
    }
    return false;
  }

  function isMining(c) {
    if (!c) return false;
    if (c.category === "挖矿") return true;
    const tags = (c.tags || []).map((x) => String(x).toLowerCase());
    if (tags.some((x) => ["挖矿", "mining", "pow", "gpu-pow", "nft变异", "变异盘", "miner"].includes(x) || x.includes("mining") || x.includes("pow"))) {
      return true;
    }
    if (c.miningType) return true;
    return false;
  }

  /** Location / AR / walk-to-earn launches. Mining is decided first, so this never steals a mining row. */
  function isGoPlay(c) {
    if (!c) return false;
    if (String(c.playStyle || "").toLowerCase() === "go") return true;
    const idn = `${c.id || ""} ${c.name || ""}`.toLowerCase().replace(/[^a-z0-9]+/g, "");
    if (idn.includes("pumpgo") || idn.includes("stokn")) return true;
    for (const raw of c.tags || []) {
      const s = String(raw);
      const low = s.toLowerCase();
      if (s.includes("定位") || low.includes("go玩法") || s.includes("地图") || s.includes("走路挖矿")) {
        return true;
      }
      if (/(^|[^a-z])ar([^a-z]|$)/i.test(s)) return true;
    }
    return false;
  }

  // Include "台子/Meme" (DS / skill canonical) alongside legacy 新台/Meme/Launchpad.
  const PLATFORM_CATS = new Set(["新台", "Meme", "Launchpad", "台子/Meme"]);

  /** Focus/重点 strip membership (not a board column). */
  function isFocus(c) {
    if (!c) return false;
    if (c.focus === true) return true;
    const focusIds = (state.data && state.data.meta && state.data.meta.focusIds) || [];
    if (focusIds.includes(c.id)) return true;
    const tags = c.tags || [];
    if (tags.some((t) => String(t) === "重点" || String(t).toLowerCase() === "focus")) return true;
    return false;
  }

  /** Elysium / Enter_Elysium ecosystem — mutual-exclusive 6th column (like LayerZero). */
  function isElysium(c) {
    if (!c) return false;
    const eco = String(c.ecosystem || "").toLowerCase();
    if (eco === "elysium") return true;
    const tags = (c.tags || []).map((t) => String(t).toLowerCase().replace(/\s+/g, ""));
    if (tags.some((t) => t === "elysium生态" || t === "elysiumeco" || t.includes("elysium生态"))) {
      return true;
    }
    const canon = canonicalChain(c.chain);
    if (canon === "Elysium") return true;
    const chain = String(c.chain || "").toLowerCase();
    if (chain.includes("elysium") || chain.includes("enter_elysium")) return true;
    const idn = String(c.id || "").toLowerCase();
    if (idn === "enter-elysium" || idn === "elysium") return true;
    return false;
  }

  /** Six board columns: Elysium > LayerZero > mining > GO > 台子/Meme > 打新.
   *  Focus candidates are strip-only (excluded from columns via isFocus),
   *  except Elysium hub may also show in the Elysium column. */
  /** CSS-safe category class (slash in 台子/Meme breaks tag-cat-* selectors). */
  function catClassOf(category) {
    const s = String(category || "");
    if (PLATFORM_CATS.has(s) || s === "台子/Meme") return "Meme";
    return s.replace(/[\/\s]+/g, "-");
  }

  function isPlatformMeme(c) {
    if (!c) return false;
    if (PLATFORM_CATS.has(c.category)) return true;
    const tags = (c.tags || []).map((t) => String(t));
    if (tags.some((t) => PLATFORM_CATS.has(t) || t === "台子/Meme" || t === "新台")) return true;
    return false;
  }

  function zoneOf(c) {
    if (isElysium(c)) return "elysium";
    if (isLayerZero(c)) return "lz";
    if (isMining(c)) return "mining";
    if (isGoPlay(c)) return "go";
    if (isPlatformMeme(c)) return "meme";
    return "scout";
  }


  function parseTime(iso) {
    if (!iso) return null;
    const t = Date.parse(iso);
    return Number.isFinite(t) ? t : null;
  }

  function scheduleStartMs(c) {
    const s = c.schedule;
    if (!s) return null;
    const direct = parseTime(s.startsAt);
    if (direct != null) return direct;
    const phases = s.phases || [];
    for (const p of phases) {
      const t = parseTime(p.startsAt);
      if (t != null) return t;
    }
    return null;
  }

  function scheduleResumeMs(c) {
    const s = c.schedule;
    if (!s) return null;
    const phases = s.phases || [];
    for (const p of phases) {
      const t = parseTime(p.endsAt);
      if (t != null) return t;
    }
    return parseTime(s.endsAt);
  }

  function formatCountdown(ms) {
    if (ms <= 0) return "已到点";
    const sec = Math.floor(ms / 1000);
    const d = Math.floor(sec / 86400);
    const h = Math.floor((sec % 86400) / 3600);
    const m = Math.floor((sec % 3600) / 60);
    if (d > 0) return `${d}天${h}h`;
    if (h > 0) return `${h}h${String(m).padStart(2, "0")}m`;
    return `${m}m`;
  }

  /** Compact China-friendly time label in Asia/Shanghai */
  function formatShanghai(iso) {
    const ms = parseTime(iso);
    if (ms == null) return "";
    const d = new Date(ms);
    const parts = new Intl.DateTimeFormat("zh-CN", {
      timeZone: "Asia/Shanghai",
      month: "numeric",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).formatToParts(d);
    const get = (t) => parts.find((p) => p.type === t)?.value || "";
    return `${get("month")}/${get("day")} ${get("hour")}:${get("minute")}`;
  }

  function isTodayShanghai(ms) {
    const fmt = new Intl.DateTimeFormat("en-CA", {
      timeZone: "Asia/Shanghai",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });
    return fmt.format(new Date(ms)) === fmt.format(new Date(state.nowMs));
  }

  function scheduleChip(c) {
    const s = c.schedule;
    if (!s) return "";
    const status = s.status || "tba";
    const start = scheduleStartMs(c);
    const startIso = s.startsAt || (s.phases || []).find((p) => p.startsAt)?.startsAt;
    let text = "TBA";
    let cls = "sched-tba";

    if (status === "ended") {
      text = "已结束";
      cls = "sched-ended";
    } else if (status === "pause") {
      const resume = scheduleResumeMs(c);
      if (resume != null && resume > state.nowMs) {
        text = `暂停 ${formatCountdown(resume - state.nowMs)}`;
        cls = "sched-soon";
      } else {
        text = "暂停";
        cls = "sched-tent";
      }
    } else if (status === "live") {
      text = "进行中";
      cls = "sched-live";
      if (start != null && start > state.nowMs) {
        text = `倒计时 ${formatCountdown(start - state.nowMs)}`;
        cls = "sched-soon";
      }
    } else if (status === "tba" || start == null) {
      text = "TBA";
      cls = "sched-tba";
    } else if (status === "tentative") {
      const delta = start - state.nowMs;
      if (delta <= 0) {
        text = "暂定·已到点";
        cls = "sched-live";
      } else if (delta <= 72 * 3600 * 1000) {
        text = `暂定 ${formatCountdown(delta)}`;
        cls = "sched-soon";
      } else {
        text = `暂定 ${formatShanghai(startIso)}`;
        cls = "sched-tent";
      }
    } else {
      // confirmed / upcoming / watch with time
      const delta = start - state.nowMs;
      if (delta <= 0) {
        text = "进行中";
        cls = "sched-live";
      } else if (delta <= 72 * 3600 * 1000) {
        if (isTodayShanghai(start) && delta > 6 * 3600 * 1000) {
          const hm = formatShanghai(startIso).split(" ")[1] || "";
          text = `今晚 ${hm} · ${formatCountdown(delta)}`;
        } else {
          text = `倒计时 ${formatCountdown(delta)}`;
        }
        cls = "sched-soon";
      } else {
        text = formatShanghai(startIso);
        cls = "sched-ok";
      }
    }

    const title = escapeHtml([s.note, s.source ? `来源:${s.source}` : ""].filter(Boolean).join(" · "));
    return `<span class="sched-chip ${cls}" title="${title}">${escapeHtml(text)}</span>`;
  }

  function onchainLine(c) {
    const o = c.onchain;
    if (!o) return "";
    const status = o.mintStatus || "unknown";
    const parts = [];
    parts.push(MINT_STATUS_LABEL[status] || status);

    const minted = o.minted ?? o.totalSupply;
    const maxS = o.maxSupply;
    if (minted != null && maxS != null) {
      parts.push(`${minted}/${maxS}`);
    } else if (minted != null) {
      parts.push(`已铸 ${minted}`);
    } else if (maxS != null) {
      parts.push(`上限 ${maxS}`);
    }

    const explorer = o.explorer;
    const contract = o.contract;
    let link = "";
    if (explorer) {
      link = `<a class="onchain-link" href="${escapeHtml(explorer)}" target="_blank" rel="noopener noreferrer">合约</a>`;
    } else if (contract) {
      link = `<span class="onchain-addr" title="${escapeHtml(contract)}">${escapeHtml(contract.slice(0, 6))}…${escapeHtml(contract.slice(-4))}</span>`;
    }

    return `
      <div class="onchain-line status-${escapeHtml(status)}">
        <span class="onchain-dot" aria-hidden="true"></span>
        <span>${escapeHtml(parts.join(" · "))}</span>
        ${link}
      </div>
    `;
  }

  function cardHtml(c) {
    const flagClass =
      c.flag === "high_domain_risk"
        ? "flag-domain"
        : c.flag === "borderline"
          ? "flag-borderline"
          : "";
    const riskClass = c.riskLevel === "extreme" ? "risk-extreme" : "";
    const lz = isLayerZero(c);
    const focus = isFocus(c);
    const lzClass = lz ? "card-lz" : "";
    const focusClass = focus ? "card-focus" : "";
    const hasFlag = Boolean(flagClass);
    const x = c.links?.x;
    const site = c.links?.site;
    const riskLevelKey = String(c.riskLevel || "medium");
    // Dedup: category chip already shows zone name; never repeat it (or PLATFORM_CATS aliases) as extra tags.
    const extraTags = (c.tags || [])
      .filter((t) => {
        const s = String(t);
        if (s === c.category) return false;
        if (["LayerZero", "重点", "focus"].includes(s)) return false;
        if (PLATFORM_CATS.has(c.category) && PLATFORM_CATS.has(s)) return false;
        return true;
      })
      .slice(0, 3)
      .map((t) => `<span class="tag tag-extra">${escapeHtml(t)}</span>`)
      .join("");
    const sched = scheduleChip(c);
    const onchain = onchainLine(c);
    const scores = scoreRow(c);
    const pc = prosCons(c);
    const wn = whatsNewBlock(c);
    const newBadge = isNewThisRound(c)
      ? '<span class="whats-new-badge" style="margin-left:6px;vertical-align:middle">本轮新</span>'
      : "";

    return `
      <article class="card ${riskClass} ${flagClass} ${lzClass} ${focusClass}" data-id="${escapeHtml(c.id)}">
        <div class="card-top ${hasFlag ? "" : "has-no-flag"}">
          <div>
            <div class="name">${escapeHtml(c.name)}${focus ? '<span class="focus-chip" title="重点关注">重点</span>' : ""}${lz ? '<span class="lz-chip" title="LayerZero 相关">LZ</span>' : ""}${isGoPlay(c) ? '<span class="go-chip" title="GO盘">GO</span>' : ""}${sched}${newBadge}</div>
            <div class="tags">
              <span class="tag tag-cat-${escapeHtml(catClassOf(c.category))}">${escapeHtml(c.category)}</span>
              <span class="tag tag-chain">${escapeHtml(canonicalChain(c.chain))}</span>
              ${focus ? '<span class="tag tag-focus">重点</span>' : ""}
              ${lz ? '<span class="tag tag-lz">LayerZero</span>' : ""}
              ${isGoPlay(c) ? '<span class="tag tag-go">GO</span>' : ""}
              ${isMining(c) ? '<span class="tag tag-mining">挖矿</span>' : ""}
              ${extraTags}
            </div>
          </div>
          <div class="card-top-right">
            ${favBtnHtml(c.id)}
            <span class="round-badge r${c.round}">轮次 ${c.round}</span>
          </div>
        </div>
        ${scores}
        ${wn}
        ${onchain}
        ${pc}
        <div class="field">
          <div class="label">为什么值得蹲</div>
          <div class="value">${escapeHtml(c.whyWatch)}</div>
        </div>
        <div class="field">
          <div class="label">背景</div>
          <div class="value">${escapeHtml(c.background)}</div>
        </div>
        <div class="field risk level-${escapeHtml(riskLevelKey)}">
          <div class="label">风险 · ${escapeHtml(RISK_LABEL[riskLevelKey] || riskLevelKey)}</div>
          <div class="value">${escapeHtml(c.risk)}</div>
        </div>
        <div class="actions">
          ${favBtnHtml(c.id)}
          <a class="btn ${x ? "" : "disabled"}" href="${x || "#"}" target="_blank" rel="noopener noreferrer">${xIcon()} X</a>
          <a class="btn ${site ? "" : "disabled"}" href="${site || "#"}" target="_blank" rel="noopener noreferrer">${siteIcon()} 官网</a>
        </div>
      </article>
    `;
  }

  function within24h(c) {
    const start = scheduleStartMs(c);
    if (start == null) return false;
    const status = c.schedule?.status;
    if (status === "ended") return false;
    const delta = start - state.nowMs;
    // include live / already started within last few hours as "soon" alert zone
    if (status === "live") return true;
    return delta >= -2 * 3600 * 1000 && delta <= 24 * 3600 * 1000;
  }

  function hasSchedule(c) {
    return Boolean(c.schedule);
  }

  function hasOnchainWatch(c) {
    const o = c.onchain;
    return Boolean(o && (o.contract || o.explorer));
  }

  function matchesQuery(c, q) {
    if (!q) return true;
    const blob = [
      c.name,
      c.id,
      c.category,
      c.chain,
      c.whyWatch,
      c.background,
      c.risk,
      c.flag,
      c.playStyle,
      c.schedule?.note,
      c.onchain?.note,
      c.whatsNew,
      ...(c.highlights || []),
      ...(c.drawbacks || []),
      ...(c.tags || []),
    ]
      .join(" ")
      .toLowerCase();
    return blob.includes(q);
  }

  /** Hard gate: a card is visible only with a real X/Twitter profile URL. */
  function hasTwitter(c) {
    const x = c.links && c.links.x;
    return typeof x === "string" && x.length > 0 && /x\.com\/|twitter\.com\//i.test(x);
  }

  function passesShared(c) {
    if (state.category !== "all" && state.category !== "挖矿" && c.category !== state.category) {
      return false;
    }
    if (state.chain === "Elysium 生态") {
      if (!isElysium(c)) return false;
    } else if (state.chain !== "all" && !chainsMatch(c.chain, state.chain)) {
      return false;
    }
    if (state.round !== "all" && String(c.round) !== String(state.round)) return false;
    if (state.layerzero === "on" && !isLayerZero(c)) return false;
    if (state.elysium === "on" && !isElysium(c)) return false;
    if (state.scheduleFilter === "soon24" && !within24h(c)) return false;
    if (state.scheduleFilter === "hasSchedule" && !hasSchedule(c)) return false;
    if (state.scheduleFilter === "onchain" && !hasOnchainWatch(c)) return false;
    return matchesQuery(c, state.query.trim().toLowerCase());
  }

  function updatedLabel() {
    const u = String(state.data?.meta?.updated || "");
    if (!u) return "—";
    return /CST|UTC|\+\d{2}/.test(u) ? u : `${u} CST`;
  }

  function discoveredMs(c) {
    return parseTime(c.firstSeen) ?? parseTime(c.addedAt);
  }

  /** Newest discovered signal first. Timestamp wins; otherwise higher round is newer. */
  function compareNewest(a, b) {
    const ta = discoveredMs(a);
    const tb = discoveredMs(b);
    if (ta != null && tb != null && ta !== tb) return tb - ta;
    if ((ta != null) !== (tb != null)) return ta != null ? -1 : 1;
    const rd = (Number(b.round) || 0) - (Number(a.round) || 0);
    if (rd) return rd;
    const ntr = (isNewThisRound(b) ? 1 : 0) - (isNewThisRound(a) ? 1 : 0);
    if (ntr) return ntr;
    const wn =
      ((b.whatsNew || "").trim() ? 1 : 0) - ((a.whatsNew || "").trim() ? 1 : 0);
    if (wn) return wn;
    const ob = b.scores?.overall ?? b.earlyScore ?? 0;
    const oa = a.scores?.overall ?? a.earlyScore ?? 0;
    if (ob !== oa) return ob - oa;
    return String(a.name || "").localeCompare(String(b.name || ""), "zh");
  }

  function sortList(list) {
    const arr = list.slice();
    const mode = state.sort || "newest";
    if (mode === "risk") {
      arr.sort(
        (a, b) =>
          (b.riskScore ?? RISK_RANK[b.riskLevel] * 20) -
            (a.riskScore ?? RISK_RANK[a.riskLevel] * 20) ||
          (b.earlyScore ?? 0) - (a.earlyScore ?? 0)
      );
    } else if (mode === "overall") {
      arr.sort(
        (a, b) =>
          (b.scores?.overall ?? 0) - (a.scores?.overall ?? 0) ||
          (b.earlyScore ?? 0) - (a.earlyScore ?? 0)
      );
    } else if (mode === "name") {
      arr.sort((a, b) => a.name.localeCompare(b.name, "zh"));
    } else if (mode === "schedule") {
      arr.sort((a, b) => {
        const sa = scheduleStartMs(a);
        const sb = scheduleStartMs(b);
        const fa = sa == null ? Number.POSITIVE_INFINITY : sa;
        const fb = sb == null ? Number.POSITIVE_INFINITY : sb;
        return fa - fb || (b.earlyScore ?? 0) - (a.earlyScore ?? 0);
      });
    } else if (mode === "earlyness") {
      arr.sort(
        (a, b) =>
          (b.earlyScore ?? b.scores?.early ?? 0) - (a.earlyScore ?? a.scores?.early ?? 0) ||
          (b.riskScore ?? 0) - (a.riskScore ?? 0)
      );
    } else {
      arr.sort(compareNewest);
    }
    return arr;
  }

  function matchesMiningType(c, typ) {
    if (!typ || typ === "all") return true;
    const mt = c.miningType || "";
    const tags = c.tags || [];
    if (typ === "nft-miner") {
      return mt === "nft-miner" || tags.some((x) => String(x).toLowerCase().includes("miner"));
    }
    if (typ === "nft-mutation") {
      return mt === "nft-mutation" || tags.some((x) => String(x).includes("变异"));
    }
    if (typ === "gpu-pow") {
      return (
        mt === "gpu-pow" ||
        tags.some((x) =>
          ["pow", "gpu", "prl-like", "qtc-like", "noid-like"].includes(String(x).toLowerCase())
        )
      );
    }
    return mt === typ || mt === "" || mt === "other";
  }

  function columnItems(zone) {
    let list = state.data.candidates.filter(
      (c) =>
        zoneOf(c) === zone &&
        (zone === "elysium" || !isFocus(c)) &&
        passesShared(c)
    );
    if (zone === "mining") list = list.filter((c) => matchesMiningType(c, state.miningTypeFilter));
    list = list.filter(hasTwitter);
    list = sortList(list);
    return list;
  }

  /** Focus strip is global: all focus:true / isFocus items, independent of round (and other chip filters).
   *  Round/category/chain/LZ/schedule filters apply only to the five daily columns via passesShared. */
  function focusItems() {
    let list = state.data.candidates.filter((c) => isFocus(c) && hasTwitter(c));
    list = sortList(list);
    const focusIds = (state.data.meta && state.data.meta.focusIds) || [];
    if (focusIds.length) {
      const rank = (id) => {
        const i = focusIds.indexOf(id);
        return i >= 0 ? i : focusIds.length + 50;
      };
      list = [...list].sort((a, b) => rank(a.id) - rank(b.id));
    }
    return list;
  }

  function focusMiniHtml(c) {
    const why = escapeHtml((c.whyWatch || c.oneLiner || "").slice(0, 90));
    const chain = escapeHtml(canonicalChain(c.chain) || "—");
    const xUrl = (c.links && (c.links.twitter || c.links.x)) || "";
    const site = (c.links && (c.links.website || c.links.site)) || "";
    const x = xUrl
      ? `<a href="${escapeHtml(xUrl)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">X</a>`
      : "";
    const web = site
      ? `<a href="${escapeHtml(site)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">站</a>`
      : "";
    return `<article class="focus-mini card-focus" data-id="${escapeHtml(c.id)}" data-x="${escapeHtml(xUrl || "")}">
      <div class="focus-mini-top">
        <div class="focus-mini-name">${escapeHtml(c.name)}<span class="focus-chip" title="重点关注">重点</span></div>
      </div>
      <div class="focus-mini-meta">${chain}${c.category ? " · " + escapeHtml(c.category) : ""}</div>
      ${why ? `<div class="focus-mini-why">${why}</div>` : ""}
      <div class="focus-mini-links">${x}${web}</div>
    </article>`;
  }

  /** Favorites strip: user pins from localStorage; independent of round/chip filters (like focus). */
  function favItems() {
    if (!state.data || !state.data.candidates) return [];
    const byId = new Map(state.data.candidates.map((c) => [c.id, c]));
    const list = [];
    // Most recently favorited first (array append order → reverse)
    for (let i = state.favorites.length - 1; i >= 0; i--) {
      const c = byId.get(state.favorites[i]);
      if (c) list.push(c);
    }
    return list;
  }

  function favMiniHtml(c) {
    const chain = escapeHtml(canonicalChain(c.chain) || "—");
    const xUrl = (c.links && (c.links.twitter || c.links.x)) || "";
    const sched = scheduleChip(c);
    const why = escapeHtml((c.whyWatch || c.oneLiner || "").slice(0, 72));
    const xLink = xUrl
      ? `<a class="fav-x" href="${escapeHtml(xUrl)}" target="_blank" rel="noopener noreferrer" onclick="event.stopPropagation()" title="打开 X">${xIcon()} X</a>`
      : `<span class="fav-x disabled" title="无推特">X</span>`;
    return `<article class="fav-mini${isFavorite(c.id) ? " is-fav" : ""}" data-id="${escapeHtml(c.id)}" data-x="${escapeHtml(xUrl || "")}">
      <div class="fav-mini-top">
        <div class="fav-mini-name">${escapeHtml(c.name)}</div>
        ${favBtnHtml(c.id)}
      </div>
      <div class="fav-mini-meta">${chain}${c.category ? " · " + escapeHtml(c.category) : ""} ${sched}</div>
      ${why ? `<div class="fav-mini-why">${why}</div>` : ""}
      <div class="fav-mini-links">${xLink}</div>
    </article>`;
  }

  function uniqueChains(candidates) {
    return [...new Set(candidates.map((c) => canonicalChain(c.chain)))].sort((a, b) => {
      const rank = (ch) => (ch === "LayerZero" ? 0 : 1);
      return rank(a) - rank(b) || a.localeCompare(b);
    });
  }

  /** Sort key for top-bar日程: pause→resume, live无时刻→now, else startsAt. */
  function schedBarSortMs(c) {
    const s = c.schedule;
    if (!s) return Number.POSITIVE_INFINITY;
    if (s.status === "pause") return scheduleResumeMs(c) ?? Number.POSITIVE_INFINITY;
    const t = scheduleStartMs(c);
    if (t != null) return t;
    if (s.status === "live" && isPlatformMeme(c)) return state.nowMs;
    return Number.POSITIVE_INFINITY;
  }

  /**
   * 顶栏「日程」选条（不排除台子/Meme）：
   * - 状态 confirmed/tentative/upcoming/live/pause
   * - 主窗口：[now−6h, now+72h]（有 startsAt / pause resume）
   * - 台子/Meme 加宽：live 且开台在 now−24h～now−6h，或 live 无时刻（进行中）— 仅作余量填充
   * - upcoming/confirmed/tentative 且 ≤72h 的台子/Meme **保底入栏**（挤掉最远的非保底项）
   * - 近→远排序，上限 12；点击仍开推特
   */
  function qualifiesSchedBarPrimary(c) {
    if (!hasTwitter(c)) return false;
    const s = c.schedule;
    if (!s) return false;
    if (!["confirmed", "tentative", "live", "upcoming", "pause"].includes(s.status)) return false;
    const horizon = 72 * 3600 * 1000;
    const lookback = 6 * 3600 * 1000;
    if (s.status === "pause") {
      const resume = scheduleResumeMs(c);
      return resume != null && resume >= state.nowMs - lookback && resume <= state.nowMs + horizon;
    }
    const t = scheduleStartMs(c);
    if (t == null) return false;
    return t >= state.nowMs - lookback && t <= state.nowMs + horizon;
  }

  function qualifiesSchedBarPlatformExtra(c) {
    if (!isPlatformMeme(c)) return false;
    if (!hasTwitter(c)) return false;
    const s = c.schedule;
    if (!s || s.status !== "live") return false;
    const t = scheduleStartMs(c);
    if (t == null) return true; // live 台子无精确时刻 → 进行中
    const horizonBack = 24 * 3600 * 1000;
    const primaryBack = 6 * 3600 * 1000;
    // 仅 6h～24h 前开台的 live 台子（主窗口已覆盖近 6h）
    return t >= state.nowMs - horizonBack && t < state.nowMs - primaryBack;
  }

  function isMustPlatformSched(c) {
    if (!isPlatformMeme(c)) return false;
    const s = c.schedule;
    if (!s) return false;
    if (!["confirmed", "tentative", "upcoming"].includes(s.status)) return false;
    const t = scheduleStartMs(c);
    if (t == null) return false;
    return t > state.nowMs && t <= state.nowMs + 72 * 3600 * 1000;
  }

  function renderSchedSoon() {
    const host = $("#sched-soon");
    const listHost = $("#sched-soon-list");
    if (!host || !listHost) return;

    const MAX = 12;
    const primary = state.data.candidates.filter(qualifiesSchedBarPrimary);
    const extraPlat = state.data.candidates.filter(
      (c) => qualifiesSchedBarPlatformExtra(c) && !primary.some((p) => p.id === c.id)
    );
    const must = primary.filter(isMustPlatformSched);
    const mustIds = new Set(must.map((c) => c.id));

    const byTime = (a, b) => schedBarSortMs(a) - schedBarSortMs(b);
    const byProximity = (a, b) => {
      const da = Math.abs(schedBarSortMs(a) - state.nowMs);
      const db = Math.abs(schedBarSortMs(b) - state.nowMs);
      return da - db || byTime(a, b);
    };
    // 占位：主窗口非保底项按距现在近→远取；余量再填 6h～24h live 台子
    const restPrimary = primary.filter((c) => !mustIds.has(c.id)).sort(byProximity);
    const extras = extraPlat.sort(byProximity);
    const fillN = Math.max(0, MAX - must.length);
    const fillers = [...restPrimary, ...extras]
      .filter((c, i, arr) => arr.findIndex((x) => x.id === c.id) === i)
      .slice(0, fillN);
    let items = [...must, ...fillers].sort(byTime);

    if (!items.length) {
      host.hidden = true;
      listHost.innerHTML = "";
      return;
    }
    host.hidden = false;
    listHost.innerHTML = items
      .map((c) => {
        const s = c.schedule;
        const xUrl = (c.links && c.links.x) || "";
        let when = "";
        let delta = 0;
        if (s.status === "pause") {
          const resume = scheduleResumeMs(c);
          delta = resume != null ? resume - state.nowMs : 0;
          when = delta > 0 ? `暂停 ${formatCountdown(delta)}` : "暂停结束";
        } else {
          const t = scheduleStartMs(c);
          if (t == null && s.status === "live") {
            delta = 0;
            when = "进行中";
          } else {
            delta = t - state.nowMs;
            const startIso = s.startsAt || (s.phases || []).find((p) => p.startsAt)?.startsAt;
            when =
              s.status === "live" && delta <= 0
                ? "进行中"
                : delta <= 0
                  ? "已到点"
                  : delta <= 72 * 3600 * 1000
                    ? `倒计时 ${formatCountdown(delta)}`
                    : formatShanghai(startIso);
          }
        }
        const warn = delta > 0 && delta <= 2 * 3600 * 1000 ? "soon-alert" : "";
        const tip = [s.note, xUrl ? "点击打开推特" : "无推特·点击定位卡片"].filter(Boolean).join(" · ");
        const jumpAttr = xUrl
          ? `data-x="${escapeHtml(xUrl)}"`
          : `data-jump="${escapeHtml(c.id)}"`;
        return `<button type="button" class="sched-soon-item ${warn}" ${jumpAttr} title="${escapeHtml(tip)}">
          <span class="ssi-name">${escapeHtml(c.name)}</span>
          <span class="ssi-when">${escapeHtml(when)}</span>
          <span class="ssi-status">${escapeHtml(s.status)}</span>
        </button>`;
      })
      .join("");
  }

  function renderChips() {
    const catHost = $("#cat-chips");
    const chainHost = $("#chain-chips");
    const roundHost = $("#round-chips");
    const lzHost = $("#lz-chips");
    const schedHost = $("#sched-chips");

    const cats = [
      { id: "all", label: "全部品类", cls: "" },
      { id: "新台", label: "新台", cls: "cat-platform" },
      { id: "Meme", label: "Meme", cls: "cat-meme" },
      { id: "NFT", label: "NFT", cls: "cat-nft" },
      { id: "挖矿", label: "挖矿", cls: "cat-mining" },
      { id: "Launchpad", label: "Launchpad", cls: "cat-platform" },
    ];
    catHost.innerHTML =
      cats
        .map(
          (c) =>
            `<button type="button" class="chip ${c.cls} ${state.category === c.id ? "active" : ""}" data-group="category" data-value="${c.id}">${c.label}</button>`
        )
        .join("") +
      `<button type="button" class="chip chip-focus" data-group="zoneJump" data-value="focus-panel">重点</button>` +
      `<button type="button" class="chip cat-go" data-group="zoneJump" data-value="go-panel">GO盘</button>` +
      `<button type="button" class="chip cat-meme-jump" data-group="zoneJump" data-value="meme-panel">台子/Meme</button>` +
      `<button type="button" class="chip chip-lz" data-group="zoneJump" data-value="lz-panel">LayerZero</button>` +
      `<button type="button" class="chip chip-ely" data-group="zoneJump" data-value="ely-panel">Elysium 生态</button>`;

    const elyCount = state.data.candidates.filter((c) => hasTwitter(c) && isElysium(c)).length;
    const rawChains = uniqueChains(state.data.candidates.filter(hasTwitter)).filter(
      (ch) => ch !== "Elysium 生态"
    );
    const chains = [
      { id: "all", label: "全部链" },
      { id: "Elysium 生态", label: `Elysium 生态 · ${elyCount}`, cls: "chip-ely" },
      ...rawChains.map((ch) => ({
        id: ch,
        label: ch,
        cls: ch === "LayerZero" ? "chip-lz" : ch === "Elysium" ? "chip-ely" : "",
      })),
    ];
    chainHost.innerHTML = chains
      .map(
        (c) =>
          `<button type="button" class="chip ${c.cls || ""} ${state.chain === c.id ? "active" : ""}" data-group="chain" data-value="${escapeHtml(c.id)}">${escapeHtml(c.label)}</button>`
      )
      .join("");

    const maxRound = Math.max(
      1,
      ...state.data.candidates.map((c) => Number(c.round) || 1)
    );
    const rounds = [
      { id: "all", label: "全部轮次" },
      ...Array.from({ length: maxRound }, (_, i) => ({
        id: String(i + 1),
        label: `轮次 ${i + 1}`,
      })),
    ];
    const totalRoundPages = Math.max(1, Math.ceil(rounds.length / ROUND_PAGE_SIZE));
    if (state.roundPage == null) {
      // Prefer page that shows the selected round; otherwise newest rounds (last page).
      if (state.round !== "all") {
        const idx = rounds.findIndex((r) => r.id === String(state.round));
        state.roundPage =
          idx >= 0 ? Math.floor(idx / ROUND_PAGE_SIZE) : totalRoundPages - 1;
      } else {
        state.roundPage = totalRoundPages - 1;
      }
    }
    state.roundPage = Math.max(0, Math.min(state.roundPage, totalRoundPages - 1));
    const roundStart = state.roundPage * ROUND_PAGE_SIZE;
    const pageRounds = rounds.slice(roundStart, roundStart + ROUND_PAGE_SIZE);
    roundHost.innerHTML = pageRounds
      .map(
        (c) =>
          `<button type="button" class="chip ${state.round === c.id ? "active" : ""}" data-group="round" data-value="${c.id}">${c.label}</button>`
      )
      .join("");
    const pager = $("#round-pager");
    const prevBtn = $("#round-prev");
    const nextBtn = $("#round-next");
    const pageLabel = $("#round-page-label");
    if (pager && prevBtn && nextBtn && pageLabel) {
      const showPager = totalRoundPages > 1;
      pager.hidden = !showPager;
      pageLabel.textContent = `${state.roundPage + 1}/${totalRoundPages}`;
      prevBtn.disabled = state.roundPage <= 0;
      nextBtn.disabled = state.roundPage >= totalRoundPages - 1;
    }

    if (schedHost) {
      const soonN = state.data.candidates.filter((c) => hasTwitter(c) && within24h(c)).length;
      const schedN = state.data.candidates.filter((c) => hasTwitter(c) && hasSchedule(c)).length;
      const onN = state.data.candidates.filter((c) => hasTwitter(c) && hasOnchainWatch(c)).length;
      const opts = [
        { id: "all", label: "全部日程" },
        { id: "soon24", label: `即将开售（24h）· ${soonN}` },
        { id: "hasSchedule", label: `有日程 · ${schedN}` },
        { id: "onchain", label: `链上可盯 · ${onN}` },
      ];
      schedHost.innerHTML = opts
        .map(
          (c) =>
            `<button type="button" class="chip chip-sched ${state.scheduleFilter === c.id ? "active" : ""}" data-group="scheduleFilter" data-value="${c.id}">${c.label}</button>`
        )
        .join("");
    }

    if (lzHost) {
      const lzCount = state.data.candidates.filter((c) => hasTwitter(c) && isLayerZero(c)).length;
      lzHost.innerHTML = `
        <button type="button" class="chip chip-lz ${state.layerzero === "all" ? "active" : ""}" data-group="layerzero" data-value="all">全部（含非 LZ）</button>
        <button type="button" class="chip chip-lz ${state.layerzero === "on" ? "active" : ""}" data-group="layerzero" data-value="on">LayerZero 监控 · ${lzCount}</button>
      `;
    }

    const miningTypeHost = $("#mining-type-chips");
    if (miningTypeHost) {
      const types = [
        { id: "all", label: "全部挖矿" },
        { id: "gpu-pow", label: "GPU PoW" },
        { id: "nft-mutation", label: "NFT 变异盘" },
        { id: "nft-miner", label: "Miner NFT" },
        { id: "other", label: "其他" },
      ];
      miningTypeHost.innerHTML = types
        .map(
          (c) =>
            `<button type="button" class="chip chip-mining ${state.miningTypeFilter === c.id ? "active" : ""}" data-group="miningTypeFilter" data-value="${c.id}">${c.label}</button>`
        )
        .join("");
    }

    const btn = $("#lz-filter-btn");
    if (btn) {
      btn.classList.toggle("active", state.layerzero === "on");
      btn.textContent =
        state.layerzero === "on" ? "显示全部候选" : "只看 LayerZero";
    }
  }

  function renderLzWatch() {
    const watch = state.data.meta?.layerZeroWatch;
    const desc = $("#lz-watch-desc");
    const pill = $("#lz-pill");
    if (watch) {
      const n = state.data.candidates.filter((c) => hasTwitter(c) && isLayerZero(c)).length;
      if (desc) {
        const focus = (watch.focus || []).join(" · ");
        desc.textContent = `${watch.label || "LayerZero 监控中"} · ${n} 条相关 · ${focus}`;
      }
      if (pill) {
        pill.textContent = `LayerZero 监控 · ${n}`;
        pill.classList.add("pill-lz");
      }
    }
    const elyWatch = state.data.meta?.elysiumWatch;
    const elyPill = $("#ely-pill");
    if (elyWatch && elyPill) {
      const en = state.data.candidates.filter((c) => hasTwitter(c) && isElysium(c)).length;
      elyPill.textContent = `Elysium 生态 · ${en}`;
      elyPill.classList.add("pill-ely");
      elyPill.title = (elyWatch.focus || []).join(" · ") || "跳到 Elysium 生态列";
    }
  }

  function miningTypeLabel(c) {
    const mt = c.miningType || "";
    if (mt === "gpu-pow") return "GPU PoW";
    if (mt === "nft-mutation") return "NFT 变异";
    if (mt === "nft-miner") return "Miner NFT";
    if ((c.tags || []).some((x) => String(x).includes("变异"))) return "NFT 变异";
    if ((c.tags || []).some((x) => String(x).toLowerCase().includes("miner"))) return "Miner NFT";
    if ((c.tags || []).some((x) => ["pow", "gpu"].includes(String(x).toLowerCase()))) return "GPU PoW";
    return "挖矿";
  }

  function miningRowHtml(c) {
    const score = c.scores?.overall ?? c.earlyScore ?? "—";
    const x = c.links?.x
      ? `<a href="${escapeHtml(c.links.x)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">X</a>`
      : "";
    const site = c.links?.site
      ? `<a href="${escapeHtml(c.links.site)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">站点</a>`
      : "";
    const why = escapeHtml((c.whyWatch || "").slice(0, 72));
    return `<div class="mining-row" data-id="${escapeHtml(c.id)}" title="${why}">
      ${favBtnHtml(c.id)}
      <div class="mining-row-name">${escapeHtml(c.name)}</div>
      <div class="mining-row-meta">${escapeHtml(canonicalChain(c.chain))}</div>
      <span class="mining-row-type">${escapeHtml(miningTypeLabel(c))}</span>
      <span class="mining-row-score">${escapeHtml(String(score))}</span>
      <div class="mining-row-links">${x}${site}</div>
    </div>`;
  }

  const ZONES = [
    { id: "scout", grid: "#grid", count: "#scout-count", label: "打新", cards: true },
    { id: "mining", grid: "#mining-grid", count: "#mining-count", label: "挖矿", cards: false },
    { id: "meme", grid: "#meme-grid", count: "#meme-count", label: "台子 / Meme", cards: true },
    { id: "go", grid: "#go-grid", count: "#go-count", label: "GO盘", cards: true },
    { id: "lz", grid: "#lz-grid", count: "#lz-count", label: "LayerZero", cards: true },
    { id: "elysium", grid: "#ely-grid", count: "#ely-count", label: "Elysium 生态", cards: true },
  ];

  function emptyColumnHtml(label, zoneId) {
    if (zoneId === "lz") {
      return `<div class="empty empty-lz"><div class="lz-badge-lg">LZ</div><div>暂无 LayerZero 相关候选</div><div class="empty-sub">盯 Zero 开链 · ATLAS · OFT 发射 · 生态极早期</div></div>`;
    }
    if (zoneId === "elysium") {
      return `<div class="empty empty-ely"><div class="ely-badge-lg">ELY</div><div>暂无 Elysium 生态候选</div><div class="empty-sub">盯 Enter_Elysium · Ascend · 挖矿/台子/预测</div></div>`;
    }
    if (state.layerzero === "on") {
      return `<div class="empty empty-lz"><div class="lz-badge-lg">LZ</div><div>当前筛选下暂无${escapeHtml(label)}</div></div>`;
    }
    if (state.elysium === "on" || state.chain === "Elysium 生态") {
      return `<div class="empty empty-ely"><div class="ely-badge-lg">ELY</div><div>当前筛选下暂无${escapeHtml(label)}</div></div>`;
    }
    return `<div class="empty">暂无匹配的${escapeHtml(label)}</div>`;
  }

  function renderFocusStrip() {
    const host = $("#focus-grid");
    const countEl = $("#focus-count");
    const panel = $("#focus-panel");
    const all = state.data.candidates.filter((c) => isFocus(c) && hasTwitter(c));
    const list = focusItems();
    if (host) {
      if (!list.length) {
        host.innerHTML = `<div class="focus-strip-empty">暂无重点候选 · 仓鼠/实体 PoW 玩具链 · 预发币测试网</div>`;
      } else {
        host.innerHTML = list.map(focusMiniHtml).join("");
      }
    }
    if (countEl) {
      countEl.textContent = String(list.length);
    }
    if (panel) {
      // Always keep strip visible under search (user-requested placement); empty state if no focus items.
      panel.hidden = false;
    }
    return { shown: list.length, total: all.length };
  }

  function renderFavStrip() {
    const host = $("#fav-grid");
    const countEl = $("#fav-count");
    const panel = $("#fav-panel");
    const list = favItems();
    if (host) {
      if (!list.length) {
        host.innerHTML = `<div class="fav-strip-empty">点卡片上的☆收藏</div>`;
      } else {
        host.innerHTML = list.map(favMiniHtml).join("");
      }
    }
    if (countEl) countEl.textContent = String(list.length);
    if (panel) panel.hidden = false;
    return { shown: list.length, total: state.favorites.length };
  }

  function renderColumn(zone) {
    const host = $(zone.grid);
    const countEl = $(zone.count);
    const all = state.data.candidates.filter(
      (c) =>
        zoneOf(c) === zone.id &&
        (zone.id === "elysium" || !isFocus(c)) &&
        hasTwitter(c)
    );
    const list = columnItems(zone.id);
    if (host) {
      if (!list.length) {
        host.innerHTML =
          zone.id === "mining"
            ? `<div class="empty-mining">挖矿暂无匹配项</div>`
            : emptyColumnHtml(zone.label, zone.id);
      } else {
        host.innerHTML = zone.cards ? list.map(cardHtml).join("") : list.map(miningRowHtml).join("");
      }
    }
    if (countEl) {
      countEl.textContent = list.length === all.length ? String(list.length) : `${list.length}/${all.length}`;
    }
    return { shown: list.length, total: all.length };
  }

  function render() {
    state.nowMs = Date.now();
    renderSchedSoon();
    const counts = {};
    counts.focus = renderFocusStrip();
    counts.fav = renderFavStrip();
    for (const zone of ZONES) counts[zone.id] = renderColumn(zone);

    const pool = state.data.candidates.filter(hasTwitter);
    const total = pool.length;
    const soonN = pool.filter(within24h).length;
    const favPill = $("#fav-pill");
    const focusPill = $("#focus-pill");
    const minePill = $("#mining-pill");
    const goPill = $("#go-pill");
    const lzPill = $("#lz-pill");
    const elyPill = $("#ely-pill");
    if (favPill) favPill.textContent = `收藏 · ${counts.fav.shown}`;
    if (focusPill) focusPill.textContent = `重点 · ${counts.focus.total}`;
    if (minePill) minePill.textContent = `挖矿 · ${counts.mining.total}`;
    if (goPill) goPill.textContent = `GO盘 · ${counts.go.total}`;
    if (lzPill) lzPill.textContent = `LayerZero · ${counts.lz.total}`;
    if (elyPill) elyPill.textContent = `Elysium · ${counts.elysium.total}`;
    $("#stats").innerHTML = `
      重点 <b>${counts.focus.shown}</b> ·
      收藏 <b>${counts.fav.shown}</b> ·
      打新 <b>${counts.scout.shown}</b> ·
      挖矿 <b>${counts.mining.shown}</b> ·
      台子/Meme <b>${counts.meme.shown}</b> ·
      GO盘 <b>${counts.go.shown}</b> ·
      LayerZero <b>${counts.lz.shown}</b> ·
      Elysium <b>${counts.elysium.shown}</b> ·
      共 <b>${total}</b> ·
      即将开售 <b>${soonN}</b> ·
      <b>仅显示有推特</b> ·
      更新 <b>${escapeHtml(updatedLabel())}</b>
    `;
  }

  function bind() {
    $("#search").addEventListener("input", (e) => {
      state.query = e.target.value;
      render();
    });
    $("#sort").addEventListener("change", (e) => {
      state.sort = e.target.value;
      render();
    });

    document.addEventListener("click", (e) => {
      const favBtn = e.target.closest("[data-fav-toggle]");
      if (favBtn) {
        e.preventDefault();
        e.stopPropagation();
        const id = favBtn.dataset.favToggle;
        if (id) {
          toggleFavorite(id);
          render();
        }
        return;
      }

      const openX = e.target.closest("[data-x]");
      if (openX && openX.dataset.x) {
        // Don't steal clicks on nested links / fav buttons
        if (e.target.closest("a, button, [data-fav-toggle]")) return;
        window.open(openX.dataset.x, "_blank", "noopener");
        return;
      }

      const jump = e.target.closest("[data-jump]");
      if (jump) {
        const id = jump.dataset.jump;
        const findTarget = () =>
          document.querySelector(
            `.card[data-id="${CSS.escape(id)}"], .mining-row[data-id="${CSS.escape(id)}"], .focus-mini[data-id="${CSS.escape(id)}"], .fav-mini[data-id="${CSS.escape(id)}"]`
          );
        const flash = (el) => {
          el.scrollIntoView({ behavior: "smooth", block: "center" });
          el.classList.add("card-flash");
          setTimeout(() => el.classList.remove("card-flash"), 1200);
        };
        const card = findTarget();
        if (card) {
          flash(card);
        } else {
          // clear filters that may hide it, then jump
          state.scheduleFilter = "all";
          state.category = "all";
          state.miningFilter = "all";
          state.miningTypeFilter = "all";
          state.chain = "all";
          state.round = "all";
          state.layerzero = "all";
          state.elysium = "all";
          state.query = "";
          const search = $("#search");
          if (search) search.value = "";
          renderChips();
          render();
          const card2 = findTarget();
          if (card2) flash(card2);
        }
        return;
      }

      const zoneBtn = e.target.closest("[data-jump-zone]");
      if (zoneBtn) {
        const panel = document.getElementById(zoneBtn.dataset.jumpZone);
        if (panel) panel.scrollIntoView({ behavior: "instant", block: "start" });
        return;
      }

      const pageBtn = e.target.closest("[data-round-page]");
      if (pageBtn) {
        const dir = pageBtn.dataset.roundPage;
        if (dir === "prev" && !pageBtn.disabled) state.roundPage = (state.roundPage || 0) - 1;
        if (dir === "next" && !pageBtn.disabled) state.roundPage = (state.roundPage || 0) + 1;
        renderChips();
        return;
      }

      const chip = e.target.closest(".chip, .lz-filter-btn");
      if (!chip) return;
      const group = chip.dataset.group;
      let value = chip.dataset.value;
      if (!group) return;

      if (group === "zoneJump" || (group === "category" && value === "挖矿")) {
        const id = group === "zoneJump" ? value : "mining-panel";
        const panel = document.getElementById(id);
        if (panel) panel.scrollIntoView({ behavior: "instant", block: "start" });
        return;
      }

      if (group === "layerzero" && chip.id === "lz-filter-btn") {
        state.layerzero = state.layerzero === "on" ? "all" : "on";
      } else {
        state[group] = value;
      }
      renderChips();
      render();
    });

    // refresh countdown labels every 30s
    setInterval(() => {
      if (!state.data) return;
      render();
    }, 30000);
  }

  async function boot() {
    try {
      const res = await fetch("./data.json?t=" + Date.now(), { cache: "no-store" });
      if (!res.ok) throw new Error("data.json load failed");
      state.data = await res.json();
      state.favorites = loadFavorites();
      state.nowMs = Date.now();
      $("#updated").textContent = updatedLabel();
      $("#count").textContent = String(state.data.candidates.filter(hasTwitter).length);
      renderLzWatch();
      renderChips();
      bind();
      render();
    } catch (err) {
      $("#grid").innerHTML = `<div class="empty">无法加载 data.json：${escapeHtml(err.message)}</div>`;
    }
  }

  boot();
})();
