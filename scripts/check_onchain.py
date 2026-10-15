#!/usr/bin/env python3
"""Soft on-chain mint probe for early-scout candidates.

Reads data.json, for EVM contracts tries public RPC eth_getCode + totalSupply().
Updates mintStatus / minted / totalSupply / lastCheckedAt when possible.
No API keys. Fail soft. Solana / unknown chains skipped.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data.json"
TZ = ZoneInfo("Asia/Shanghai")

# Public RPCs (no keys). Unknown / unsupported chains are skipped.
RPCS: dict[str, list[str]] = {
    "ethereum": [
        "https://ethereum.publicnode.com",
        "https://rpc.ankr.com/eth",
        "https://cloudflare-eth.com",
    ],
    "base": [
        "https://base.publicnode.com",
        "https://mainnet.base.org",
    ],
    # Ink / Robinhood may lack stable public RPC; try common endpoints, skip if fail
    "ink": [
        "https://rpc-gel.inkonchain.com",
        "https://ink.drpc.org",
    ],
    "robinhood": [
        # speculative / may fail — fail soft
        "https://rpc.robinhood.xyz",
        "https://robinhood-chain.drpc.org",
    ],
}

EVM_CHAINS = set(RPCS.keys())

# ERC721-ish totalSupply() selector
TOTAL_SUPPLY_SEL = "0x18160ddd"


def now_iso() -> str:
    return datetime.now(TZ).isoformat()


def rpc_call(url: str, method: str, params: list[Any], timeout: float = 8.0) -> Any:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "early-scout-check/1.0"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode())
    if "error" in payload and payload["error"]:
        raise RuntimeError(str(payload["error"]))
    return payload.get("result")


def try_rpcs(chain: str, method: str, params: list[Any]) -> Any | None:
    for url in RPCS.get(chain, []):
        try:
            return rpc_call(url, method, params)
        except Exception:
            continue
    return None


def hex_to_int(h: str | None) -> int | None:
    if not h or h == "0x":
        return None
    try:
        return int(h, 16)
    except Exception:
        return None


def check_contract(chain: str, address: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "codePresent": False,
        "totalSupply": None,
        "ok": False,
        "error": None,
    }
    if chain not in EVM_CHAINS:
        out["error"] = "unsupported_chain"
        return out
    if not address or not address.startswith("0x") or len(address) != 42:
        out["error"] = "bad_address"
        return out

    code = try_rpcs(chain, "eth_getCode", [address, "latest"])
    if code is None:
        out["error"] = "rpc_unavailable"
        return out
    out["codePresent"] = bool(code and code != "0x" and code != "0x0")
    if not out["codePresent"]:
        out["ok"] = True
        return out

    supply_hex = try_rpcs(chain, "eth_call", [{"to": address, "data": TOTAL_SUPPLY_SEL}, "latest"])
    supply = hex_to_int(supply_hex)
    # Guard absurd values (failed decode / non-ERC721)
    if supply is not None and supply < 10**12:
        out["totalSupply"] = supply
    out["ok"] = True
    return out


def derive_mint_status(oc: dict, code_present: bool, supply: int | None) -> str:
    max_s = oc.get("maxSupply")
    prev = oc.get("mintStatus") or "unknown"
    if not code_present:
        return "not_open" if prev in ("unknown", "not_open") else prev
    if supply is None:
        return "open" if prev in ("unknown", "not_open") else prev
    if max_s is not None and supply >= int(max_s):
        return "sold_out"
    if supply > 0:
        return "open"
    return "not_open" if prev == "not_open" else "open"


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    changes = {
        "checked": 0,
        "skipped": 0,
        "opened": [],
        "sold_out": [],
        "supply_deltas": [],
        "errors": [],
    }

    for c in data.get("candidates", []):
        oc = c.get("onchain")
        if not oc or not oc.get("contract"):
            continue
        chain = (oc.get("chainId") or "").lower()
        addr = oc["contract"]
        if chain not in EVM_CHAINS:
            changes["skipped"] += 1
            continue

        changes["checked"] += 1
        prev_status = oc.get("mintStatus")
        prev_supply = oc.get("totalSupply")
        result = check_contract(chain, addr)
        oc["lastCheckedAt"] = now_iso()

        if not result["ok"]:
            changes["errors"].append({"id": c["id"], "error": result.get("error")})
            continue

        if result["totalSupply"] is not None:
            new_supply = result["totalSupply"]
            oc["totalSupply"] = new_supply
            oc["minted"] = new_supply
            if prev_supply is not None and prev_supply != new_supply:
                changes["supply_deltas"].append(
                    {"id": c["id"], "from": prev_supply, "to": new_supply}
                )

        new_status = derive_mint_status(oc, result["codePresent"], result.get("totalSupply"))
        oc["mintStatus"] = new_status
        if prev_status != new_status:
            if new_status == "open" and prev_status in ("unknown", "not_open", None):
                changes["opened"].append(c["id"])
            if new_status == "sold_out":
                changes["sold_out"].append(c["id"])

    # bump meta.updated
    now = datetime.now(TZ)
    data.setdefault("meta", {})["updated"] = now.strftime("%Y-%m-%d %H:%M CST")
    if "features" not in data["meta"]:
        data["meta"]["features"] = ["schedule", "onchain"]

    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(changes, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
