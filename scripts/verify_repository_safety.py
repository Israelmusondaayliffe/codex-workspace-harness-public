#!/usr/bin/env python3
"""Verify that the public harness contains only reusable, publishable material."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TOP_LEVEL = {
    ".agents",
    ".gitignore",
    "AGENTS.md",
    "CODEX-OUTPUTS",
    "CONTEXT",
    "CONTRIBUTING.md",
    "LICENSE",
    "PROJECTS",
    "README.md",
    "SECURITY.md",
    "TEMPLATES",
    "docs",
    "examples",
    "integrations",
    "plugins",
    "scripts",
}
DISALLOWED_PARTS = {
    ".claude",
    ".codex",
    ".env",
    ".impeccable",
    "ABOUT-ME",
    "auth.json",
    "credentials.json",
    "memories",
    "node_modules",
    "__pycache__",
}
ALLOWED_HIDDEN_PREFIXES = {
    PurePosixPath(".agents/plugins/marketplace.json"),
    PurePosixPath("plugins/harness-engineering/.codex-plugin/plugin.json"),
    PurePosixPath("integrations/claude-code-codex-bridge/template/.claude/settings.json"),
    PurePosixPath("integrations/claude-code-codex-bridge/template/.claude/hooks/session-start.sh"),
}
TEXT_SUFFIXES = {
    "",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
PATTERNS = {
    "private-key material": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic secret assignment": re.compile(
        r"(?i)(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"][A-Za-z0-9_./+=-]{12,}['\"]"
    ),
    "GitHub token": re.compile(r"\b(?:gh[opusr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "email address": re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    "macOS home path": re.compile(r"/Users/[A-Za-z0-9._-]+"),
    "Linux home path": re.compile(r"/home/[A-Za-z0-9._-]+"),
    "Windows home path": re.compile(r"(?i)[A-Z]:\\Users\\[A-Za-z0-9._-]+"),
}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        capture_output=True,
        check=False,
    )
    if result.returncode == 0 and result.stdout:
        return [ROOT / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]
    return sorted(path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts)


def hidden_path_allowed(relative: PurePosixPath) -> bool:
    if not any(part.startswith(".") for part in relative.parts):
        return True
    if relative == PurePosixPath(".gitignore"):
        return True
    return relative in ALLOWED_HIDDEN_PREFIXES


def main() -> int:
    problems: list[str] = []
    files = tracked_files()

    for path in files:
        relative = PurePosixPath(path.relative_to(ROOT).as_posix())
        if not relative.parts or relative.parts[0] not in ALLOWED_TOP_LEVEL:
            problems.append(f"outside allowlist: {relative}")
        if path.is_symlink():
            problems.append(f"tracked symbolic link: {relative}")
        if any(part in DISALLOWED_PARTS for part in relative.parts) and relative not in ALLOWED_HIDDEN_PREFIXES:
            problems.append(f"disallowed private path: {relative}")
        if not hidden_path_allowed(relative):
            problems.append(f"unexpected hidden path: {relative}")

        if relative.parts[0] == "CODEX-OUTPUTS" and relative != PurePosixPath("CODEX-OUTPUTS/README.md"):
            problems.append(f"generated output is tracked: {relative}")
        if relative.parts[0] == "CONTEXT" and relative.name != "README.md" and not relative.name.endswith(".template.md"):
            problems.append(f"completed context is tracked: {relative}")

        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                problems.append(f"{label} detected: {relative}")

    marketplace = ROOT / ".agents" / "plugins" / "marketplace.json"
    try:
        data = json.loads(marketplace.read_text(encoding="utf-8"))
        entry = data["plugins"][0]
        if data.get("name") != "codex-workspace-harness":
            problems.append("marketplace name is incorrect")
        if entry.get("name") != "harness-engineering":
            problems.append("bundled plugin entry is missing")
        plugin_path = entry.get("source", {}).get("path")
        if plugin_path != "./plugins/harness-engineering":
            problems.append("bundled plugin source path is incorrect")
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        problems.append(f"marketplace manifest is invalid: {exc}")

    required_files = {
        PurePosixPath("AGENTS.md"),
        PurePosixPath("README.md"),
        PurePosixPath(".agents/plugins/marketplace.json"),
        PurePosixPath("plugins/harness-engineering/.codex-plugin/plugin.json"),
        PurePosixPath("integrations/claude-code-codex-bridge/template/.claude/settings.json"),
        PurePosixPath("integrations/claude-code-codex-bridge/template/.claude/hooks/session-start.sh"),
    }
    tracked = {PurePosixPath(path.relative_to(ROOT).as_posix()) for path in files}
    for missing in sorted(required_files - tracked):
        problems.append(f"required file is not tracked: {missing}")

    if problems:
        for problem in sorted(set(problems)):
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    print(json.dumps({"status": "PASS", "files_checked": len(files), "symlinks": 0}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
