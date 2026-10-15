(() => {
  const state = {
    data: null,
    category: "all",
    chain: "all",
    round: "all",
    layerzero: "all",
    miningFilter: "all", // all | on
    scheduleFilter: "all", // all | soon24 | hasSchedule | onchain
    query: "",
    sort: "earlyness",
    nowMs: Date.now(),
  };

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => [...document.querySelectorAll(sel)];

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

  function whatsNewBlock(c) {
    const t = (c.whatsNew || "").trim();
    if (!t) return "";
    return (
      '<div class="whats-new"><span class="whats-new-badge">本轮新</span><span>' +
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

  function isLayerZero(c) {
    const tags = (c.tags || []).map((t) => String(t).toLowerCase());
    if (tags.some((t) => t.includes("layerzero") || t === "lz" || t === "oft" || t === "zro")) {
      return true;
    }
    const chain = String(c.chain || "").toLowerCase();
    if (chain === "layerzero" || chain === "zero") return true;
    const blob = `${c.name} ${c.whyWatch || ""} ${c.background || ""}`.toLowerCase();
    return blob.includes("layerzero") || blob.includes("layer zero");
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


  function parseTime(iso) {
    if (!iso) return null;
    const t = Date.parse(iso);
    return Number.isFinite(t) ? t : null;
  }

  function scheduleStartMs(c) {
    const s = c.schedule;
    if (!s) return null;
    return parseTime(s.startsAt);
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
    const start = parseTime(s.startsAt);
    let text = "TBA";
    let cls = "sched-tba";

    if (status === "ended") {
      text = "已结束";
      cls = "sched-ended";
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
      } else if (delta <= 24 * 3600 * 1000) {
        text = `暂定 ${formatCountdown(delta)}`;
        cls = "sched-soon";
      } else {
        text = `暂定 ${formatShanghai(s.startsAt)}`;
        cls = "sched-tent";
      }
    } else {
      // confirmed
      const delta = start - state.nowMs;
      if (delta <= 0) {
        text = "进行中";
        cls = "sched-live";
      } else if (delta <= 24 * 3600 * 1000) {
        if (isTodayShanghai(start)) {
          const hm = formatShanghai(s.startsAt).split(" ")[1] || "";
          text = delta <= 6 * 3600 * 1000 ? `倒计时 ${formatCountdown(delta)}` : `今晚 ${hm}`;
        } else {
          text = `倒计时 ${formatCountdown(delta)}`;
        }
        cls = "sched-soon";
      } else {
        text = formatShanghai(s.startsAt);
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
    const lzClass = lz ? "card-lz" : "";
    const hasFlag = Boolean(flagClass);
    const x = c.links?.x;
    const site = c.links?.site;
    const riskLevelKey = String(c.riskLevel || "medium");
    const extraTags = (c.tags || [])
      .filter((t) => !["LayerZero"].includes(t))
      .slice(0, 3)
      .map((t) => `<span class="tag tag-extra">${escapeHtml(t)}</span>`)
      .join("");
    const sched = scheduleChip(c);
    const onchain = onchainLine(c);
    const scores = scoreRow(c);
    const pc = prosCons(c);
    const wn = whatsNewBlock(c);
    const newBadge = (c.whatsNew || "").trim()
      ? '<span class="whats-new-badge" style="margin-left:6px;vertical-align:middle">本轮新</span>'
      : "";

    return `
      <article class="card ${riskClass} ${flagClass} ${lzClass}" data-id="${escapeHtml(c.id)}">
        <div class="card-top ${hasFlag ? "" : "has-no-flag"}">
          <div>
            <div class="name">${escapeHtml(c.name)}${lz ? '<span class="lz-chip" title="LayerZero 相关">LZ</span>' : ""}${sched}${newBadge}</div>
            <div class="tags">
              <span class="tag tag-cat-${escapeHtml(c.category)}">${escapeHtml(c.category)}</span>
              <span class="tag tag-chain">${escapeHtml(c.chain)}</span>
              ${lz ? '<span class="tag tag-lz">LayerZero</span>' : ""}
              ${isMining(c) ? '<span class="tag tag-mining">挖矿</span>' : ""}
              ${extraTags}
            </div>
          </div>
          <span class="round-badge r${c.round}">轮次 ${c.round}</span>
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

  function filtered() {
    const q = state.query.trim().toLowerCase();
    let list = state.data.candidates.slice();

    if (state.category !== "all") {
      list = list.filter((c) => c.category === state.category);
    }
    if (state.chain !== "all") {
      list = list.filter((c) => c.chain === state.chain);
    }
    if (state.round !== "all") {
      list = list.filter((c) => String(c.round) === String(state.round));
    }
    if (state.layerzero === "on") {
      list = list.filter(isLayerZero);
    }
    if (state.miningFilter === "on") {
      list = list.filter(isMining);
    }
    if (state.scheduleFilter === "soon24") {
      list = list.filter(within24h);
    } else if (state.scheduleFilter === "hasSchedule") {
      list = list.filter(hasSchedule);
    } else if (state.scheduleFilter === "onchain") {
      list = list.filter(hasOnchainWatch);
    }
    if (q) {
      list = list.filter((c) => {
        const blob = [
          c.name,
          c.category,
          c.chain,
          c.whyWatch,
          c.background,
          c.risk,
          c.flag,
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
      });
    }

    if (state.sort === "risk") {
      list.sort(
        (a, b) =>
          (b.riskScore ?? RISK_RANK[b.riskLevel] * 20) -
            (a.riskScore ?? RISK_RANK[a.riskLevel] * 20) ||
          b.earlyScore - a.earlyScore
      );
    } else if (state.sort === "overall") {
      list.sort(
        (a, b) =>
          (b.scores?.overall ?? 0) - (a.scores?.overall ?? 0) ||
          (b.earlyScore ?? 0) - (a.earlyScore ?? 0)
      );
    } else if (state.sort === "name") {
      list.sort((a, b) => a.name.localeCompare(b.name, "zh"));
    } else if (state.sort === "schedule") {
      list.sort((a, b) => {
        const sa = scheduleStartMs(a);
        const sb = scheduleStartMs(b);
        const fa = sa == null ? Number.POSITIVE_INFINITY : sa;
        const fb = sb == null ? Number.POSITIVE_INFINITY : sb;
        return fa - fb || (b.earlyScore ?? 0) - (a.earlyScore ?? 0);
      });
    } else {
      list.sort(
        (a, b) =>
          (b.earlyScore ?? 0) - (a.earlyScore ?? 0) ||
          (b.riskScore ?? 0) - (a.riskScore ?? 0)
      );
    }
    return list;
  }

  function uniqueChains(candidates) {
    return [...new Set(candidates.map((c) => c.chain))].sort((a, b) => {
      const rank = (ch) => (ch === "LayerZero" ? 0 : ch === "Zero" ? 1 : 2);
      return rank(a) - rank(b) || a.localeCompare(b);
    });
  }

  function renderSchedSoon() {
    const host = $("#sched-soon");
    const listHost = $("#sched-soon-list");
    if (!host || !listHost) return;

    const items = state.data.candidates
      .filter((c) => {
        const s = c.schedule;
        if (!s || !s.startsAt) return false;
        if (!["confirmed", "tentative", "live"].includes(s.status)) return false;
        const t = parseTime(s.startsAt);
        if (t == null) return false;
        // show upcoming or recently live
        return t >= state.nowMs - 6 * 3600 * 1000;
      })
      .sort((a, b) => scheduleStartMs(a) - scheduleStartMs(b))
      .slice(0, 8);

    if (!items.length) {
      host.hidden = true;
      listHost.innerHTML = "";
      return;
    }
    host.hidden = false;
    listHost.innerHTML = items
      .map((c) => {
        const s = c.schedule;
        const t = parseTime(s.startsAt);
        const delta = t - state.nowMs;
        let when =
          s.status === "live" && delta <= 0
            ? "进行中"
            : delta <= 0
              ? "已到点"
              : delta <= 24 * 3600 * 1000
                ? `倒计时 ${formatCountdown(delta)}`
                : formatShanghai(s.startsAt);
        const warn = delta > 0 && delta <= 2 * 3600 * 1000 ? "soon-alert" : "";
        return `<button type="button" class="sched-soon-item ${warn}" data-jump="${escapeHtml(c.id)}" title="${escapeHtml(s.note || "")}">
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
    catHost.innerHTML = cats
      .map(
        (c) =>
          `<button type="button" class="chip ${c.cls} ${state.category === c.id ? "active" : ""}" data-group="category" data-value="${c.id}">${c.label}</button>`
      )
      .join("");

    const chains = [
      { id: "all", label: "全部链" },
      ...uniqueChains(state.data.candidates).map((ch) => ({
        id: ch,
        label: ch,
      })),
    ];
    chainHost.innerHTML = chains
      .map(
        (c) =>
          `<button type="button" class="chip ${c.id === "LayerZero" || c.id === "Zero" ? "chip-lz" : ""} ${state.chain === c.id ? "active" : ""}" data-group="chain" data-value="${escapeHtml(c.id)}">${escapeHtml(c.label)}</button>`
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
    roundHost.innerHTML = rounds
      .map(
        (c) =>
          `<button type="button" class="chip ${state.round === c.id ? "active" : ""}" data-group="round" data-value="${c.id}">${c.label}</button>`
      )
      .join("");

    if (schedHost) {
      const soonN = state.data.candidates.filter(within24h).length;
      const schedN = state.data.candidates.filter(hasSchedule).length;
      const onN = state.data.candidates.filter(hasOnchainWatch).length;
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
      const lzCount = state.data.candidates.filter(isLayerZero).length;
      lzHost.innerHTML = `
        <button type="button" class="chip chip-lz ${state.layerzero === "all" ? "active" : ""}" data-group="layerzero" data-value="all">全部（含非 LZ）</button>
        <button type="button" class="chip chip-lz ${state.layerzero === "on" ? "active" : ""}" data-group="layerzero" data-value="on">LayerZero 监控 · ${lzCount}</button>
      `;
    }

    const miningHost = $("#mining-chips");
    if (miningHost) {
      const mCount = state.data.candidates.filter(isMining).length;
      miningHost.innerHTML = `
        <button type="button" class="chip chip-mining ${state.miningFilter === "all" ? "active" : ""}" data-group="miningFilter" data-value="all">全部（含非挖矿）</button>
        <button type="button" class="chip chip-mining ${state.miningFilter === "on" ? "active" : ""}" data-group="miningFilter" data-value="on">挖矿监控 · ${mCount}</button>
      `;
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
    if (!watch) return;
    const n = state.data.candidates.filter(isLayerZero).length;
    if (desc) {
      const focus = (watch.focus || []).join(" · ");
      desc.textContent = `${watch.label || "LayerZero 监控中"} · ${n} 条相关 · ${focus}`;
    }
    if (pill) {
      pill.textContent = `LayerZero 监控 · ${n}`;
      pill.classList.add("pill-lz");
    }
  }

  function render() {
    state.nowMs = Date.now();
    renderSchedSoon();
    const list = filtered();
    const grid = $("#grid");
    if (!list.length) {
      const emptyLz =
        state.layerzero === "on"
          ? `<div class="empty empty-lz"><div class="lz-badge-lg">LZ</div><div><b>LayerZero 监控已开启</b><br/>当前筛选下暂无匹配项。开链/新台信号出现后会自动入库；可点「显示全部候选」或清空筛选。</div></div>`
          : `<div class="empty">没有匹配的候选。试试清空筛选或换个关键词。</div>`;
      grid.innerHTML = emptyLz;
    } else {
      grid.innerHTML = list.map(cardHtml).join("");
    }

    const total = state.data.candidates.length;
    const lzN = state.data.candidates.filter(isLayerZero).length;
    const soonN = state.data.candidates.filter(within24h).length;
    const schedN = state.data.candidates.filter(hasSchedule).length;
    $("#stats").innerHTML = `
      显示 <b>${list.length}</b> / ${total} ·
      即将开售 <b>${soonN}</b> ·
      有日程 <b>${schedN}</b> ·
      LayerZero <b>${lzN}</b> ·
      更新日期 <b>${escapeHtml(state.data.meta.updated)}</b> CST
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
      const jump = e.target.closest("[data-jump]");
      if (jump) {
        const id = jump.dataset.jump;
        const card = document.querySelector(`.card[data-id="${CSS.escape(id)}"]`);
        if (card) {
          card.scrollIntoView({ behavior: "smooth", block: "center" });
          card.classList.add("card-flash");
          setTimeout(() => card.classList.remove("card-flash"), 1200);
        } else {
          // clear filters that may hide it, then jump
          state.scheduleFilter = "all";
          state.category = "all";
          state.miningFilter = "all";
          state.chain = "all";
          state.round = "all";
          state.layerzero = "all";
          state.query = "";
          const search = $("#search");
          if (search) search.value = "";
          renderChips();
          render();
          const card2 = document.querySelector(`.card[data-id="${CSS.escape(id)}"]`);
          if (card2) {
            card2.scrollIntoView({ behavior: "smooth", block: "center" });
            card2.classList.add("card-flash");
            setTimeout(() => card2.classList.remove("card-flash"), 1200);
          }
        }
        return;
      }

      const chip = e.target.closest(".chip, .lz-filter-btn");
      if (!chip) return;
      const group = chip.dataset.group;
      let value = chip.dataset.value;
      if (!group) return;

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
      state.nowMs = Date.now();
      $("#updated").textContent = state.data.meta.updated;
      $("#count").textContent = String(state.data.candidates.length);
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
