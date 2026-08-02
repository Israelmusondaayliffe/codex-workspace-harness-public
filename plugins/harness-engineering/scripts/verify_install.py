#!/usr/bin/env python3
"""Verify a Codex plugin installation and source-cache parity."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Optional


EXCLUDES = {".DS_Store", "__pycache__"}


def file_map(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file() or any(part in EXCLUDES for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        result[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def default_cache_root() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
    return codex_home / "plugins" / "cache"


def select_installation(
    listing: dict[str, Any], plugin_name: str, version: str, marketplace: Optional[str]
) -> tuple[dict[str, Any], str]:
    matches = [
        item
        for item in listing.get("installed", [])
        if item.get("name") == plugin_name
        and item.get("version") == version
        and item.get("enabled") is True
    ]
    if marketplace:
        matches = [item for item in matches if item.get("marketplaceName") == marketplace]
    if not matches:
        target = marketplace or "any configured marketplace"
        raise RuntimeError(f"no enabled {plugin_name} {version} installation found in {target}")
    if len(matches) > 1:
        choices = sorted({str(item.get("marketplaceName")) for item in matches})
        raise RuntimeError("multiple matching installations found; pass --marketplace: " + ", ".join(choices))
    selected_marketplace = matches[0].get("marketplaceName")
    if not isinstance(selected_marketplace, str) or not selected_marketplace:
        raise RuntimeError("matching installation has no marketplaceName")
    return matches[0], selected_marketplace


def verify_install(
    source: Path,
    listing: dict[str, Any],
    marketplace: Optional[str] = None,
    cache_root: Optional[Path] = None,
) -> dict[str, Any]:
    source = source.resolve()
    manifest_path = source / ".claude-plugin" / "plugin.json"
    if not manifest_path.is_file():
        manifest_path = source / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    plugin_name = manifest["name"]
    version = manifest["version"]
    _, selected_marketplace = select_installation(listing, plugin_name, version, marketplace)
    cache_base = (cache_root or default_cache_root()).expanduser().resolve()
    cache = cache_base / selected_marketplace / plugin_name / version
    if not cache.is_dir():
        raise RuntimeError(f"installed cache is missing: {cache}")
    source_files = file_map(source)
    cache_files = file_map(cache)
    if source_files != cache_files:
        missing = sorted(set(source_files) - set(cache_files))
        extra = sorted(set(cache_files) - set(source_files))
        changed = sorted(path for path in set(source_files) & set(cache_files) if source_files[path] != cache_files[path])
        raise RuntimeError(f"source-cache mismatch missing={missing} extra={extra} changed={changed}")
    return {
        "plugin": plugin_name,
        "marketplace": selected_marketplace,
        "version": version,
        "cache": str(cache),
        "files": len(source_files),
        "parity": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Plugin source directory",
    )
    parser.add_argument(
        "--marketplace",
        help="Marketplace name from `codex plugin list --json`; required when matching installs are ambiguous",
    )
    parser.add_argument(
        "--cache-root",
        type=Path,
        help="Base Codex plugin cache directory; defaults to $CODEX_HOME/plugins/cache or ~/.codex/plugins/cache",
    )
    args = parser.parse_args()
    listing = subprocess.run(["codex", "plugin", "list", "--json"], check=True, capture_output=True, text=True)
    result = verify_install(args.source, json.loads(listing.stdout), args.marketplace, args.cache_root)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"install verification failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
