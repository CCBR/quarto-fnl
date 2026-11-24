#!/usr/bin/env python3
"""Sync both Quarto extension versions from DESCRIPTION.

Usage:
    python3 .github/scripts/sync_extension_version.py
    python3 .github/scripts/sync_extension_version.py --check

R development versions (X.Y.Z.9000) become X.Y.Z-dev for Quarto's SemVer field.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
EXTENSION_NAMES = ("fnl", "fnl-report")
VERSION_LINE = re.compile(r"^version:.*$", re.MULTILINE)


def extension_version(description: str) -> str:
    """Read and validate the shared version, converting R development versions."""
    versions = re.findall(r"^Version:[ \t]*(.*)$", description, re.MULTILINE)
    if len(versions) != 1:
        raise ValueError("DESCRIPTION must contain exactly one Version field")
    version = versions[0].strip()
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(\.9000)?", version):
        raise ValueError(
            f"Unsupported DESCRIPTION version {version!r}; expected X.Y.Z or X.Y.Z.9000"
        )
    return version.removesuffix(".9000") + ("-dev" if version.endswith(".9000") else "")


def synced_extension_yml(content: str, version: str) -> str:
    """Replace the single top-level version field without altering other YAML."""
    if len(VERSION_LINE.findall(content)) != 1:
        raise ValueError("_extension.yml must contain exactly one top-level version field")
    return VERSION_LINE.sub(f"version: {version}", content, count=1)


def sync_extensions(repo_root: Path, check: bool = False) -> None:
    """Sync both manifests, or fail with all mismatches when checking."""
    version = extension_version((repo_root / "DESCRIPTION").read_text())
    updates = {}
    for name in EXTENSION_NAMES:
        path = repo_root / "_extensions" / name / "_extension.yml"
        current = path.read_text()
        updated = synced_extension_yml(current, version)
        if updated != current:
            updates[path] = updated

    if check and updates:
        paths = ", ".join(str(path.relative_to(repo_root)) for path in updates)
        raise ValueError(f"{paths} must match DESCRIPTION (Quarto version {version})")
    for path, content in updates.items():
        path.write_text(content)
        print(f"Updated {path.relative_to(repo_root)} to version {version}")


def main() -> None:
    """Run the synchronization CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without modifying files.")
    args = parser.parse_args()
    sync_extensions(REPO_ROOT, check=args.check)


if __name__ == "__main__":
    main()
