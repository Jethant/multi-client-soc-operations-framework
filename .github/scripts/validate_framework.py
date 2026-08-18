#!/usr/bin/env python3
"""Validate taxonomy, playbook coverage, internal links, and naming."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "taxonomy" / "alert-types.json"
TAXONOMY_INDEX = ROOT / "taxonomy" / "README.md"
REQUIRED_SHARED_FILES = (
    ROOT / "client-profile" / "README.md",
    ROOT / "tuning" / "README.md",
)
PLAYBOOK_DIRECTORY = ROOT / "playbooks"
PLAYBOOK_SECTIONS = (
    "## Scope",
    "## Required telemetry",
    "## Client baseline checks",
    "## Investigation and correlation",
    "## Decision guidance",
    "## Containment and follow-up",
    "## Tuning",
    "## Closure record",
)
CATEGORY_ID = re.compile(r"^SOC-\d{3}$")
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
    if not isinstance(categories, list) or not categories:
        fail("Taxonomy must contain a non-empty categories list", errors)
        return

    ids: list[str] = []
    names: list[str] = []
    index_entries: list[tuple[str, str, str]] = []
    registered_playbooks: set[Path] = set()

    for entry in categories:
        if not isinstance(entry, dict):
            fail("Every taxonomy category must be an object", errors)
            continue

        category_id = entry.get("id")
        name = entry.get("name")
        playbook = entry.get("playbook")
        if not isinstance(category_id, str) or not CATEGORY_ID.fullmatch(category_id):
            fail(f"Invalid taxonomy category ID: {category_id!r}", errors)
            continue
        if not isinstance(name, str) or not name.strip():
            fail(f"{category_id} must have a non-empty name", errors)
            continue
        if not isinstance(playbook, str) or not playbook.strip():
            fail(f"{category_id} must have a playbook path", errors)
            continue

        ids.append(category_id)
        names.append(name)
        playbook_path = (ROOT / playbook).resolve()
        try:
            playbook_path.relative_to(PLAYBOOK_DIRECTORY.resolve())
        except ValueError:
            fail(f"{category_id} playbook must be inside playbooks/: {playbook}", errors)
            continue

        registered_playbooks.add(playbook_path)
        index_entries.append((category_id, name, playbook))
        if not playbook_path.exists():
            fail(f"Missing playbook for {category_id}: {playbook}", errors)
            continue

        content = playbook_path.read_text(encoding="utf-8")
        expected_title = f"# {category_id} — {name}"
        if expected_title not in content:
            fail(f"{playbook} is missing title: {expected_title}", errors)
        for section in PLAYBOOK_SECTIONS:
            if section not in content:
                fail(f"{playbook} is missing section: {section}", errors)

    if len(ids) != len(set(ids)) or len(names) != len(set(names)):
        fail("Taxonomy categories must have unique IDs and names", errors)

    actual_playbooks = set(PLAYBOOK_DIRECTORY.glob("SOC-*.md"))
    for unregistered in sorted(actual_playbooks - registered_playbooks):
        fail(f"Unregistered playbook: {unregistered.relative_to(ROOT)}", errors)

    if not TAXONOMY_INDEX.exists():
        fail(f"Missing taxonomy index: {TAXONOMY_INDEX.relative_to(ROOT)}", errors)
    else:
        index_content = TAXONOMY_INDEX.read_text(encoding="utf-8")
        for category_id, name, playbook in index_entries:
            if f"| {category_id} | {name} |" not in index_content:
                fail(f"Taxonomy index is missing {category_id} — {name}", errors)
            if f"(../{playbook})" not in index_content:
                fail(f"Taxonomy index has no playbook link for {category_id}: {playbook}", errors)

    for path in REQUIRED_SHARED_FILES:
        if not path.exists():
            fail(f"Missing shared framework file: {path.relative_to(ROOT)}", errors)


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
