#!/usr/bin/env python3
"""
Rebuild a story's characters/catalog.json from the individual files in
that story's characters/data/ folder.

Run this any time you add, remove, or edit a character JSON file so the
catalog app (catalog/index.html) picks up the change.

Usage (from the repo root):
    python3 scripts/build_catalog.py            # rebuilds Valkorath (default)
    python3 scripts/build_catalog.py pantheon    # rebuilds Pantheon
    python3 scripts/build_catalog.py <folder>    # rebuilds any story folder
"""
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

story = sys.argv[1] if len(sys.argv) > 1 else "."
ROOT = os.path.join(REPO_ROOT, story)
DATA_DIR = os.path.join(ROOT, "characters", "data")
OUT_PATH = os.path.join(ROOT, "characters", "catalog.json")

REQUIRED_FIELDS = ["slug", "name", "epithet", "faction", "status", "tags", "bio", "art"]


def main():
    if not os.path.isdir(DATA_DIR):
        sys.exit(f"Couldn't find {DATA_DIR}")

    entries = []
    for fname in sorted(os.listdir(DATA_DIR)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(DATA_DIR, fname)
        with open(path, encoding="utf-8") as f:
            try:
                entry = json.load(f)
            except json.JSONDecodeError as e:
                sys.exit(f"Invalid JSON in {fname}: {e}")

        missing = [k for k in REQUIRED_FIELDS if k not in entry]
        if missing:
            sys.exit(f"{fname} is missing required field(s): {', '.join(missing)}")

        entries.append(entry)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(entries)} characters to {os.path.relpath(OUT_PATH, REPO_ROOT)}")


if __name__ == "__main__":
    main()
