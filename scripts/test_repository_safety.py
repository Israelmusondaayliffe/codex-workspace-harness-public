from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("verify_repository_safety.py")
SPEC = importlib.util.spec_from_file_location("verify_repository_safety", SCRIPT)
assert SPEC and SPEC.loader
safety = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(safety)


class RepositorySafetyTests(unittest.TestCase):
    def make_minimal_public_tree(self, root: Path) -> None:
        (root / ".agents" / "plugins").mkdir(parents=True)
        (root / ".claude-plugin").mkdir()
        (root / "plugins" / "harness-engineering" / ".codex-plugin").mkdir(parents=True)
        (root / "plugins" / "harness-engineering" / ".claude-plugin").mkdir(parents=True)
        bridge = root / "integrations" / "claude-code-codex-bridge" / "template" / ".claude"
        bridge.mkdir(parents=True)
        (bridge / "hooks").mkdir()
        files = {
            "AGENTS.md": "public workspace\n",
            "CLAUDE.md": "read AGENTS.md\n",
            "README.md": "public harness\n",
            ".claude-plugin/marketplace.json": json.dumps(
                {
                    "name": "community-agent-plugins",
                    "owner": {"name": "Community Maintainers"},
                    "metadata": {"description": "Public harness"},
                    "plugins": [{"name": "harness-engineering", "source": "./plugins/harness-engineering", "version": "2.1.2"}],
                }
            ),
            ".agents/plugins/marketplace.json": json.dumps(
                {
                    "name": "community-agent-plugins",
                    "interface": {"displayName": "Community Agent Plugins"},
                    "plugins": [{"name": "harness-engineering", "source": {"path": "./plugins/harness-engineering"}}],
                }
            ),
            "plugins/harness-engineering/.codex-plugin/plugin.json": "{}\n",
            "plugins/harness-engineering/.claude-plugin/plugin.json": "{}\n",
            "integrations/claude-code-codex-bridge/template/.claude/settings.json": "{}\n",
            "integrations/claude-code-codex-bridge/template/.claude/hooks/session-start.sh": "#!/bin/sh\n",
        }
        for relative, content in files.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def run_safety(self, root: Path) -> tuple[int, str]:
        original_root = safety.ROOT
        safety.ROOT = root
        stdout = io.StringIO()
        stderr = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = safety.main()
        finally:
            safety.ROOT = original_root
        return result, stdout.getvalue() + stderr.getvalue()

    def test_intentional_cross_platform_files_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_minimal_public_tree(root)
            result, output = self.run_safety(root)
            self.assertEqual(result, 0, output)

    def test_unapproved_private_path_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_minimal_public_tree(root)
            private_file = root / ".claude" / "settings.json"
            private_file.parent.mkdir()
            private_file.write_text("{}\n", encoding="utf-8")
            result, output = self.run_safety(root)
            self.assertEqual(result, 1)
            self.assertIn("unexpected hidden path", output)

    def test_sensitive_content_scan_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_minimal_public_tree(root)
            email = "owner" + "@" + "example.com"
            (root / "README.md").write_text(email + "\n", encoding="utf-8")
            result, output = self.run_safety(root)
            self.assertEqual(result, 1)
            self.assertIn("email address detected", output)


if __name__ == "__main__":
    unittest.main()
