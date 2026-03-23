#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml", "requests", "python-dotenv"]
# ///
import argparse
import os
from dotenv import load_dotenv
load_dotenv()
import random
import re
import sys
import time
import warnings
import yaml
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
YAML_PATH = REPO_ROOT / "benchmarks.yaml"
README_PATH = REPO_ROOT / "README.md"

REQUIRED_FIELDS = ["name", "links"]


def validate(benchmarks):
    errors = []
    seen_names = {}

    for i, b in enumerate(benchmarks):
        label = f"Entry #{i + 1} ({b.get('name', '<no name>')})"

        for field in REQUIRED_FIELDS:
            if not b.get(field):
                errors.append(f"{label}: missing required field '{field}'")

        name = b.get("name")
        if name:
            if name in seen_names:
                errors.append(f"{label}: duplicate name '{name}' (first seen at entry #{seen_names[name] + 1})")
            else:
                seen_names[name] = i

        links = b.get("links") or {}
        if not isinstance(links, dict):
            errors.append(f"{label}: 'links' must be a mapping")
        else:
            valid_urls = [url for url in links.values() if url and str(url).startswith(("http://", "https://"))]
            if not valid_urls:
                errors.append(f"{label}: must have at least one valid http/https URL in 'links'")
            for key, url in links.items():
                if url and not str(url).startswith(("http://", "https://")):
                    errors.append(f"{label}: link '{key}' has invalid URL: {url!r}")

    return errors


HEADER = """\
<!-- DO NOT EDIT - this file is auto-generated. See CONTRIBUTING.md to add a benchmark. -->
# Awesome Agent Benchmarks

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![@BerkeleyRDI](https://img.shields.io/badge/@BerkeleyRDI-black?logo=x&logoColor=white)](https://x.com/BerkeleyRDI)
[![Discord](https://img.shields.io/discord/1280234300012494859?label=&logo=discord&logoColor=ffffff&color=5865F2&labelColor=4a5568)](https://discord.gg/uqZUta3MYa)

A curated list of agent benchmarks and evaluation frameworks.
"""


def anchor(text):
    """GitHub-compatible heading anchor slug."""
    result = ""
    for ch in text.lower():
        if ch.isalnum() or ch == "-":
            result += ch
        elif ch == " ":
            result += "-"
    return result


def arxiv_id(url):
    """Extract arXiv ID from an arxiv.org URL, or return None."""
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", str(url))
    return m.group(1) if m else None


def github_repo_path(url):
    """Return 'owner/repo' if URL is a github.com user/repo root, else None."""
    if not url:
        return None
    url = str(url).rstrip("/")
    if not (url.startswith("https://github.com/") or url.startswith("http://github.com/")):
        return None
    path = url.removeprefix("https://github.com/").removeprefix("http://github.com/")
    parts = path.split("/")
    if len(parts) == 2 and all(parts):
        return path
    return None


def fetch_counts(benchmarks):
    """Fetch citation counts (Semantic Scholar) and star counts (GitHub) for all entries.

    Returns ({name: {"citations": int, "stars": int, "pub_date": date|None}}, ok).
    """
    import requests

    counts = {b["name"]: {"citations": 0, "stars": 0, "pub_date": None} for b in benchmarks}
    ok = True

    # --- Semantic Scholar batch ---
    s2_ids = []      # parallel list of S2 paper IDs
    s2_names = []    # benchmark name for each ID
    for b in benchmarks:
        links = b.get("links") or {}
        paper_url = links.get("paper") or ""
        aid = arxiv_id(paper_url)
        if aid:
            s2_ids.append(f"arXiv:{aid}")
        elif paper_url.startswith(("http://", "https://")):
            s2_ids.append(f"URL:{paper_url}")
        else:
            s2_ids.append(None)
        s2_names.append(b["name"])

    valid_s2 = [(name, sid) for name, sid in zip(s2_names, s2_ids) if sid is not None]
    if valid_s2:
        headers = {}
        api_key = os.environ.get("S2_API_KEY")
        if api_key:
            headers["x-api-key"] = api_key

        def s2_post_with_retry():
            last_error = None
            for attempt in range(4):
                try:
                    resp = requests.post(
                        "https://api.semanticscholar.org/graph/v1/paper/batch",
                        params={"fields": "citationCount,publicationDate"},
                        json={"ids": [sid for _, sid in valid_s2]},
                        headers=headers,
                        timeout=30,
                    )
                    if resp.status_code in (429, 500, 502, 503, 504):
                        retry_after = resp.headers.get("Retry-After")
                        if attempt < 3:
                            delay = 5 * (2 ** attempt) if resp.status_code == 429 else 2 ** attempt
                            if retry_after:
                                try:
                                    delay = max(delay, float(retry_after))
                                except ValueError:
                                    pass
                            delay += random.uniform(0, 0.5)
                            time.sleep(delay)
                            continue
                    resp.raise_for_status()
                    return resp
                except requests.RequestException as e:
                    last_error = e
                    if attempt >= 3:
                        break
                    time.sleep((2 ** attempt) + random.uniform(0, 0.5))
            raise last_error if last_error is not None else RuntimeError("S2 request failed")

        try:
            resp = s2_post_with_retry()
            resp.raise_for_status()
            results = resp.json()
            found = 0
            for (name, sid), result in zip(valid_s2, results):
                if result is not None:
                    counts[name]["citations"] = result.get("citationCount") or 0
                    raw_date = result.get("publicationDate")
                    if raw_date:
                        try:
                            counts[name]["pub_date"] = date.fromisoformat(raw_date)
                        except ValueError:
                            pass
                    found += 1
            print(f"S2: got citation counts for {found}/{len(valid_s2)} papers.")
        except Exception as e:
            warnings.warn(f"S2 batch request failed: {e}")
            ok = False

    # --- GitHub GraphQL batch ---
    gh_repos = []  # (name, owner, repo)
    for b in benchmarks:
        links = b.get("links") or {}
        url = links.get("github")
        path = github_repo_path(url) if url else None
        if path:
            owner, repo = path.split("/")
            gh_repos.append((b["name"], owner, repo))

    token = os.environ.get("GITHUB_TOKEN")
    if gh_repos and not token:
        print("GitHub: GITHUB_TOKEN not set — skipping star counts.")
    if gh_repos and token:
        gh_headers = {"Authorization": f"bearer {token}"}

        # Build a single GraphQL query with aliased fields
        query_parts = []
        for i, (name, owner, repo) in enumerate(gh_repos):
            query_parts.append(
                f'r{i}: repository(owner: "{owner}", name: "{repo}") {{ stargazerCount }}'
            )
        graphql_query = "{ " + " ".join(query_parts) + " }"

        try:
            resp = requests.post(
                "https://api.github.com/graphql",
                json={"query": graphql_query},
                headers=gh_headers,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            gql_errors = data.get("errors")
            gql_data = data.get("data") or {}
            found = 0
            for i, (name, owner, repo) in enumerate(gh_repos):
                alias = f"r{i}"
                if gql_errors:
                    for err in gql_errors:
                        locs = [p.get("key") for p in err.get("path", [])]
                        if alias in locs:
                            warnings.warn(f"GitHub: error for {name!r} ({owner}/{repo}): {err.get('message')}")
                repo_data = gql_data.get(alias)
                if repo_data:
                    counts[name]["stars"] = repo_data.get("stargazerCount") or 0
                    found += 1
            print(f"GitHub: got star counts for {found}/{len(gh_repos)} repos.")
        except Exception as e:
            warnings.warn(f"GitHub GraphQL request failed: {e}")
            ok = False

    return counts, ok



def fmt_count(n):
    """Format a count for display: 1234 → '1.2k', 123 → '123'."""
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def generate(fetch=False):
    with open(YAML_PATH) as f:
        benchmarks = yaml.safe_load(f)

    errors = validate(benchmarks)
    if errors:
        print("Validation failed - README not generated:\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    if fetch:
        print("Fetching citation and star counts...")
        counts, ok = fetch_counts(benchmarks)
        if not ok:
            print("Metadata fetch failed; aborting without writing README.", file=sys.stderr)
            sys.exit(1)
    else:
        counts = {b["name"]: {"citations": 0, "stars": 0, "pub_date": None} for b in benchmarks}

    new_cutoff = date.today() - timedelta(days=90)
    def entry_date(b):
        pub = counts[b["name"]]["pub_date"]
        if pub:
            return pub
        raw = b.get("date")
        if raw:
            try:
                return date.fromisoformat(str(raw))
            except ValueError:
                return None
        return None

    new_names = {b["name"] for b in benchmarks if (d := entry_date(b)) and d > new_cutoff}

    by_category = defaultdict(list)
    for b in benchmarks:
        by_category[b.get("category") or "other"].append(b)

    categories = sorted(c for c in by_category if c != "other")
    if "other" in by_category:
        categories.append("other")

    for cat in categories:
        by_category[cat].sort(key=lambda b: b["name"].lower())

    lines = [HEADER]

    # Table of contents
    lines.append("## Table of Contents\n")
    for cat in categories:
        count = len(by_category[cat])
        lines.append(f"- [{cat.title()}](#{anchor(cat.title())}) ({count})")
    lines.append("\n---\n")

    # Sections
    for cat in categories:
        lines.append(f"## {cat.title()}\n")
        for b in by_category[cat]:
            name = b["name"]
            desc = (b.get("description") or "").strip()
            links = b.get("links") or {}
            entry_counts = counts[name]

            # Build badge string
            badges = []
            display_date = entry_date(b)
            if display_date:
                badges.append(f"*({display_date.strftime('%b %Y')})*")
            if entry_counts["citations"] > 0:
                badges.append(f"📄 {fmt_count(entry_counts['citations'])}")
            if entry_counts["stars"] > 0:
                badges.append(f"⭐ {fmt_count(entry_counts['stars'])}")

            # Header line
            new_prefix = "🆕 " if name in new_names else ""
            header_parts = [f"{new_prefix}**{name}**"]
            header_parts.extend(badges)

            # Links row
            link_parts = []
            for key, url in (links or {}).items():
                if not url:
                    continue
                link_parts.append(f"[{key.title()}]({url})")

            header = "- " + " ".join(header_parts)
            if link_parts:
                lines.append(header + "\\")
                lines.append("  " + " · ".join(link_parts))
            else:
                lines.append(header)

            # Description row
            if desc:
                lines.append(f"  > {desc}")

        lines.append("")

    README_PATH.write_text("\n".join(lines) + "\n")
    print(f"Generated README.md - {len(benchmarks)} benchmarks across {len(categories)} categories.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate README from benchmarks.yaml")
    parser.add_argument(
        "--fetch",
        action="store_true",
        help="Fetch live citation and star counts (requires network; uses S2_API_KEY and GITHUB_TOKEN env vars)",
    )
    args = parser.parse_args()
    generate(fetch=args.fetch)
