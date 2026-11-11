#!/usr/bin/env python3
"""Unit tests for the silent-account fallback and its budget slot."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import silent_accounts as sa  # noqa: E402
import x_budget  # noqa: E402

NOW = datetime(2026, 11, 11, 12, 0, tzinfo=x_budget.CST)
LANE_TOKENS = ("LayerZero", "Elysium", "TapeOut", "GIWA", "DogeEVM", "Starknet")


def yums_tweet(followers=708):
    return {
        "data": [{
            "id": "1",
            "author_id": "999",
            "text": "yums.fun is up @yumsdotfun",
            "entities": {
                "mentions": [{"username": "yumsdotfun", "id": "111"}],
                "urls": [{"expanded_url": "https://yums.fun", "url": "https://t.co/abc"}],
            },
        }],
        "includes": {
            "users": [
                {
                    "id": "999",
                    "username": "someone",
                    "name": "Someone",
                    "description": "gm",
                    "created_at": "2020-01-01T00:00:00.000Z",
                    "public_metrics": {"followers_count": 10, "tweet_count": 500},
                },
                {
                    "id": "111",
                    "username": "yumsdotfun",
                    "name": "Yums",
                    "description": "",
                    "created_at": "2026-11-08T00:00:00.000Z",
                    "public_metrics": {"followers_count": followers, "tweet_count": 0},
                },
            ]
        },
    }


def screen(payload, **kwargs):
    known = kwargs.pop("known", set())
    return sa.screen(payload, known=known, now=NOW, do_probe=False, **kwargs)


class BudgetTests(unittest.TestCase):
    def test_silent_is_outside_soft_cap_and_does_not_cut_lanes(self):
        ample = x_budget.allocate("ample", 40)
        self.assertEqual(ample["uf"], 2)
        self.assertEqual(ample["kwThin"], 6)
        self.assertEqual(ample["silent"], 2)
        lane_sum = sum(ample[k] for k in ("uf", "mustLe2h", "kwThin", "kwCore", "mentionsThin", "mentionsRest"))
        self.assertEqual(lane_sum, 18)
        self.assertNotIn("silent", ("uf", "kwThin"))
        tight_trim = x_budget.allocate("ample", 8)
        self.assertEqual(tight_trim["kwThin"], 6)
        self.assertEqual(tight_trim["silent"], 2)
        self.assertLessEqual(
            sum(tight_trim[k] for k in ("uf", "mustLe2h", "kwThin", "kwCore", "mentionsThin", "mentionsRest")),
            8,
        )

    def test_modes(self):
        self.assertEqual(x_budget.allocate("zero-x", 0)["silent"], 0)
        self.assertEqual(x_budget.allocate("near-exhausted", 8)["silent"], 0)
        self.assertEqual(x_budget.allocate("near-exhausted", 8)["kwThin"], 0)
        self.assertGreater(x_budget.allocate("near-exhausted", 8)["uf"], 0)
        self.assertEqual(x_budget.allocate("tight", 18)["silent"], 1)
        self.assertEqual(x_budget.allocate("tight", 18)["kwThin"], 6)
        self.assertEqual(x_budget.allocate("pace", 28)["silent"], 1)
        self.assertEqual(x_budget.allocate("post-reset-full", 50)["silent"], 2)
        self.assertEqual(x_budget.allocate("post-reset-full", 50)["uf"], 4)
        self.assertEqual(x_budget.allocate("post-reset-full", 50)["kwThin"], 6)

    def test_plan_keeps_thin_lanes_on_a_tight_day(self):
        out = x_budget.plan(180, NOW)
        self.assertEqual(out["mode"], "tight")
        self.assertEqual(out["alloc"]["kwThin"], 6)
        self.assertEqual(out["alloc"]["uf"], 1)  # trimmed to the floor, not to fund silent
        self.assertEqual(out["silentCap"], 1)
        self.assertTrue(out["silentOutsideSoftCap"])
        self.assertFalse(out["silentCountsTowardMinSpend"])
        self.assertNotIn(out["silentCap"], range(0))
        lane_sum = out["laneAllocSum"]
        self.assertLessEqual(lane_sum, out["softCap"])
        self.assertEqual(
            lane_sum,
            sum(out["alloc"][k] for k in ("uf", "mustLe2h", "kwThin", "kwCore", "mentionsThin", "mentionsRest")),
        )

    def test_rotation_covers_every_lane_without_merging(self):
        from datetime import timedelta
        base = datetime(2026, 11, 11, 8, 30, tzinfo=x_budget.CST)
        seen_user = set()
        for step in range(11):
            moment = base + timedelta(minutes=35 * step)
            picks = x_budget.select_silent_queries(moment, 2)
            self.assertEqual(len(picks), 2)
            self.assertEqual({p["kind"] for p in picks}, {"user", "url"})
            self.assertNotEqual(picks[0]["lane"], picks[1]["lane"])
            seen_user.add(picks[0]["lane"])
            for pick in picks:
                self.assertEqual(pick["countsAgainst"], "silentCap")
                tokens = [token for token in LANE_TOKENS if token in pick["query"]]
                self.assertLessEqual(len(tokens), 1, pick)
            self.assertRegex(picks[0]["query"], x_budget.USER_QUERY_RE)
        self.assertEqual(seen_user, {lane["lane"] for lane in x_budget.SILENT_LANES})

    def test_user_queries_cannot_express_a_domain(self):
        for lane in x_budget.SILENT_LANES:
            self.assertRegex(lane["user"], x_budget.USER_QUERY_RE)
            self.assertNotIn(".", lane["user"])
            self.assertNotIn("url:", lane["user"])
            self.assertNotIn("bio:", lane["user"])


class ScreenTests(unittest.TestCase):
    def test_yums_profile_with_no_surface_is_not_reviewed(self):
        payload = {
            "data": [{
                "username": "yumsdotfun",
                "name": "Yums",
                "description": "",
                "created_at": "2026-11-08T00:00:00.000Z",
                "public_metrics": {"followers_count": 708, "tweet_count": 0},
            }]
        }
        out = screen(payload)
        acct = out["silentAccount"]
        self.assertTrue(acct["ran"])
        self.assertEqual(acct["sentToReview"], 0)
        self.assertEqual(acct["admitted"], 0)
        self.assertEqual(acct["skipReasons"].get("no_product_surface"), 1)
        self.assertIn("yums", acct["residualGap"])

    def test_yums_mention_stays_deferred_until_the_site_is_live(self):
        dead = screen(yums_tweet(), site_probe={"https://yums.fun": False})
        acct = dead["silentAccount"]
        self.assertEqual(acct["sentToReview"], 0)
        self.assertEqual(acct["admitted"], 0)
        self.assertGreaterEqual(acct["deferred"], 1)
        self.assertEqual(acct["skipReasons"].get("shell_site_not_live"), 1)
        self.assertIn("@yumsdotfun", acct["deferredHandles"])
        self.assertEqual(acct["seen"], acct["sentToReview"] + acct["skipped"])

        live = screen(yums_tweet(), site_probe={"https://yums.fun": True})
        review = live["review"]
        self.assertEqual(len(review), 1)
        card = review[0]
        self.assertEqual(card["handle"], "@yumsdotfun")
        self.assertFalse(card["focus"])
        self.assertEqual(card["links"]["x"], "https://x.com/yumsdotfun")
        self.assertEqual(card["links"]["web"], "https://yums.fun")
        self.assertEqual(live["silentAccount"]["sentToReview"], 1)
        self.assertEqual(live["silentAccount"]["admitted"], 0)
        self.assertNotIn("shell_site_not_live", live["silentAccount"]["skipReasons"])

    def test_url_without_a_handle_is_not_admitted(self):
        payload = {
            "data": [{
                "id": "2",
                "author_id": "999",
                "text": "check https://yums.fun",
                "entities": {"urls": [{"expanded_url": "https://yums.fun"}]},
            }],
            "includes": {"users": [{
                "id": "999",
                "username": "someone",
                "name": "Someone",
                "description": "daily calls",
                "created_at": "2020-01-01T00:00:00.000Z",
                "public_metrics": {"followers_count": 20, "tweet_count": 400},
            }]},
        }
        out = screen(payload)
        self.assertEqual(out["silentAccount"]["sentToReview"], 0)
        self.assertEqual(out["silentAccount"]["skipReasons"].get("url_without_mentioned_handle"), 1)

    def test_known_handle_is_skipped(self):
        out = screen(yums_tweet(), known={"yumsdotfun"}, site_probe={"https://yums.fun": True})
        self.assertEqual(out["silentAccount"]["sentToReview"], 0)
        self.assertEqual(out["silentAccount"]["skipReasons"].get("already_in_library"), 1)

    def test_low_follower_product_bio_does_not_need_a_live_site(self):
        payload = {
            "username": "basemint",
            "name": "Base Mint",
            "description": "Building a fair mint on Base. Official protocol site soon.",
            "created_at": "2026-11-10T00:00:00.000Z",
            "public_metrics": {"followers_count": 12, "tweet_count": 0},
        }
        out = screen(payload)
        self.assertEqual(out["silentAccount"]["sentToReview"], 1)
        self.assertFalse(out["review"][0]["focus"])
        self.assertTrue(out["review"][0]["links"]["x"].startswith("https://x.com/"))

    def test_inflated_shell_with_only_a_bio_stays_deferred(self):
        payload = {
            "username": "farmpad",
            "name": "Farm Pad",
            "description": "Building a fair mint protocol. Official launchpad.",
            "created_at": "2026-11-10T00:00:00.000Z",
            "public_metrics": {"followers_count": 900, "tweet_count": 0},
        }
        out = screen(payload)
        self.assertEqual(out["silentAccount"]["sentToReview"], 0)
        self.assertEqual(out["silentAccount"]["skipReasons"].get("shell_site_unconfirmed"), 1)

    def test_onchain_evidence_can_pass_the_shell_rule(self):
        payload = {
            "username": "farmpad",
            "name": "Farm Pad",
            "description": "",
            "created_at": "2026-11-10T00:00:00.000Z",
            "onchainConfirmed": True,
            "public_metrics": {"followers_count": 900, "tweet_count": 0},
        }
        out = screen(payload)
        self.assertEqual(out["silentAccount"]["sentToReview"], 1)
        self.assertFalse(out["review"][0]["focus"])

    def test_admitted_count_only_includes_reviewed_handles(self):
        out = screen(
            yums_tweet(),
            site_probe={"https://yums.fun": True},
            admitted=["yumsdotfun", "not-reviewed"],
        )
        self.assertEqual(out["silentAccount"]["admitted"], 1)
        self.assertEqual(out["silentAccount"]["admittedIgnored"], ["not-reviewed"])
        self.assertLessEqual(out["silentAccount"]["admitted"], out["silentAccount"]["sentToReview"])


class CliTests(unittest.TestCase):
    def test_filter_cli_emits_the_result_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "raw.json"
            library = Path(tmp) / "lib.json"
            raw.write_text(json.dumps(yums_tweet()), encoding="utf-8")
            library.write_text(json.dumps({"candidates": []}), encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "silent_accounts.py"),
                    "filter",
                    str(raw),
                    "--library",
                    str(library),
                    "--no-probe",
                    "--site-probe",
                    json.dumps({"https://yums.fun": True}),
                    "--remaining",
                    "800",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        body = json.loads(proc.stdout)
        acct = body["silentAccount"]
        for key in ("ran", "seen", "sentToReview", "admitted", "skipped"):
            self.assertIn(key, acct)
        self.assertTrue(acct["ran"])
        self.assertEqual(acct["sentToReview"], 1)
        self.assertFalse(body["review"][0]["focus"])

    def test_queries_cli_does_not_claim_it_ran(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "silent_accounts.py"), "queries", "--remaining", "0"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        acct = json.loads(proc.stdout)["silentAccount"]
        self.assertFalse(acct["ran"])
        self.assertEqual(acct["silentCap"], 0)
        self.assertEqual(acct["seen"], 0)


if __name__ == "__main__":
    unittest.main()
