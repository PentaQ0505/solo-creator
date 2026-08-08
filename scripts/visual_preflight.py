#!/usr/bin/env python3
"""Detect optional visual engines used by Solo Creator.

This script never installs or modifies dependencies. It reports filesystem-visible
Skills and a local Cover checkout; host-managed plugins may still be available.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable


ENGINE_META = {
    "guizang": {
        "skill_names": {"guizang-social-card-skill"},
        "license": "AGPL-3.0",
        "install": "npx skills add https://github.com/op7418/guizang-social-card-skill --skill guizang-social-card-skill",
        "repository": "https://github.com/op7418/guizang-social-card-skill",
    },
    "kami": {
        "skill_names": {"kami"},
        "license": "MIT (check bundled font terms separately)",
        "install": "npx skills add tw93/kami/plugins/kami -a universal -g -y",
        "repository": "https://github.com/tw93/Kami",
    },
}


def frontmatter_name(path: Path) -> str | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()[:30]
    except (OSError, UnicodeError):
        return None
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            break
        if stripped.startswith("name:"):
            return stripped.split(":", 1)[1].strip().strip("'\"").lower()
    return None


def unique_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        normalized = str(path.expanduser().resolve(strict=False))
        if normalized not in seen:
            seen.add(normalized)
            result.append(Path(normalized))
    return result


def candidate_roots(extra: list[str]) -> list[Path]:
    current = Path.cwd()
    skill_dir = Path(__file__).resolve().parent.parent
    roots = [
        current / ".agents" / "skills",
        current / ".claude" / "skills",
        Path.home() / ".agents" / "skills",
        Path.home() / ".claude" / "skills",
        skill_dir.parent,
    ]
    roots.extend(Path(value) for value in extra)
    return unique_paths(roots)


def skill_files(root: Path) -> Iterable[Path]:
    if not root.is_dir():
        return []
    candidates = list(root.glob("*/SKILL.md"))
    candidates.extend(root.glob("*/plugins/*/SKILL.md"))
    candidates.extend(root.glob("plugins/*/SKILL.md"))
    if (root / "SKILL.md").is_file():
        candidates.append(root / "SKILL.md")
    return candidates


def detect_skill(names: set[str], roots: list[Path]) -> str | None:
    for root in roots:
        for path in skill_files(root):
            if frontmatter_name(path) in names:
                return str(path.parent)
    return None


def detect_cover(explicit_path: str | None) -> str | None:
    values: list[Path] = []
    if explicit_path:
        values.append(Path(explicit_path))
    configured = os.environ.get("SOLO_CREATOR_COVER_PATH")
    if configured:
        values.append(Path(configured))
    values.extend([Path.cwd() / "cover", Path.cwd().parent / "cover"])
    for path in unique_paths(values):
        package = path / "package.json"
        if package.is_file():
            try:
                data = json.loads(package.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError):
                continue
            text = json.dumps(data, ensure_ascii=False).lower()
            if "next" in text and ("cover" in text or path.name.lower() == "cover"):
                return str(path)
    return None


def build_report(args: argparse.Namespace) -> dict[str, object]:
    roots = candidate_roots(args.root)
    engines: dict[str, object] = {}
    for key, meta in ENGINE_META.items():
        path = detect_skill(meta["skill_names"], roots)
        engines[key] = {
            "available": path is not None,
            "path": path,
            "license": meta["license"],
            "repository": meta["repository"],
            "install_hint": meta["install"],
            "note": "A host-managed plugin can be available even when no filesystem path is visible.",
        }

    cover_path = detect_cover(args.cover_path)
    engines["cover"] = {
        "available": cover_path is not None,
        "path": cover_path,
        "mode": "local-web-app" if cover_path else "hosted-or-manual",
        "license": "MIT (check external font and image terms separately)",
        "repository": "https://github.com/weizwz/cover",
        "web_url": "https://cover.weizwz.com",
        "note": "Cover is a web application, not an Agent Skill or documented CLI/API.",
    }
    return {"search_roots": [str(path) for path in roots], "engines": engines}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--root", action="append", default=[], help="Add a Skill search root.")
    parser.add_argument("--cover-path", help="Path to a local weizwz/cover checkout.")
    parser.add_argument("--require", choices=["guizang", "kami", "cover"], help="Exit non-zero if an engine is unavailable.")
    args = parser.parse_args()
    report = build_report(args)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for name, info in report["engines"].items():
            status = "available" if info["available"] else "not detected"
            location = f" — {info['path']}" if info.get("path") else ""
            print(f"{name}: {status}{location}")

    if args.require and not report["engines"][args.require]["available"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
