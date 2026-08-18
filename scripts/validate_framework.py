#!/usr/bin/env python3
"""Validate taxonomy coverage, internal links, and common naming mistakes."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "taxonomy" / "alert-types.json"
MAPPED_FILES = (
    ROOT / "baselines" / "README.md",
    ROOT / "heuristics" / "Heuristics-full-framework.md",
    ROOT / "correlation-workflows" / "correlation-workflows-list.md",
    ROOT / "tuning" / "mapped-tuning-guidelines.md",
    ROOT / "workflow-guides" / "mapped-workflow-guides.md",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_registry(errors: list[str]) -> None:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Unable to read {REGISTRY.relative_to(ROOT)}: {exc}", errors)
        return

    categories = data.get("categories", [])
    ids = [entry.get("id") for entry in categories]
    names = [entry.get("name") for entry in categories]
    if not categories or len(ids) != len(set(ids)) or len(names) != len(set(names)):
        fail("Taxonomy categories must have unique, non-empty IDs and names", errors)

    for path in MAPPED_FILES:
        if not path.exists():
            fail(f"Missing mapped file: {path.relative_to(ROOT)}", errors)
            continue
        content = path.read_text(encoding="utf-8")
        for entry in categories:
            heading = f"## {entry['id']} — {entry['name']}"
            if heading not in content:
                fail(f"{path.relative_to(ROOT)} is missing heading: {heading}", errors)


def validate_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(content):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = unquote(target.split("#", 1)[0])
            if not local_target:
                continue
            resolved = (path.parent / local_target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{path.relative_to(ROOT)} links outside the repository: {target}", errors)
                continue
            if not resolved.exists():
                fail(f"Broken link in {path.relative_to(ROOT)}: {target}", errors)


def validate_names_and_content(errors: list[str]) -> None:
    misspelling = "ranso" + "meware"
    for path in ROOT.rglob("*"):
        if misspelling in path.name.lower():
            fail(f"Misspelled ransomware path: {path.relative_to(ROOT)}", errors)
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yml", ".yaml"}:
            content = path.read_text(encoding="utf-8").lower()
            if misspelling in content:
                fail(f"Misspelled ransomware content: {path.relative_to(ROOT)}", errors)


def main() -> int:
    errors: list[str] = []
    validate_registry(errors)
    validate_links(errors)
    validate_names_and_content(errors)

    if errors:
        print("Framework validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Framework validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
