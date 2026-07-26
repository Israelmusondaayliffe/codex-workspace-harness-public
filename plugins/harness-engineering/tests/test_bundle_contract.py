from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERSION_PATTERN = re.compile(r"^2\.1\.0$")


class BundleContractTests(unittest.TestCase):
    def test_manifest_and_marketplace_ready_shape(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "harness-engineering")
        self.assertRegex(manifest["version"], VERSION_PATTERN)
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(len(manifest["interface"]["defaultPrompt"]), 3)
        self.assertNotIn("apps", manifest)
        self.assertNotIn("mcpServers", manifest)

    def test_templates_have_no_unresolved_todo_markers(self) -> None:
        markers = ("[" + "TODO:", "__" + "REPLACE_ME__")
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".py"}:
                text = path.read_text(encoding="utf-8", errors="replace")
                for marker in markers:
                    self.assertNotIn(marker, text, str(path))

    def test_skill_descriptions_are_in_frontmatter(self) -> None:
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines[0], "---")
            self.assertTrue(any(line.startswith("name:") for line in lines[1:5]))
            self.assertTrue(any(line.startswith("description:") for line in lines[1:6]))

    def test_frontier_first_contract_is_owned_and_routed(self) -> None:
        reference = ROOT / "references" / "frontier-first-prompt-governance.md"
        self.assertTrue(reference.is_file())
        text = reference.read_text(encoding="utf-8")
        for phrase in (
            "compact context kernel",
            "delta-only overlays",
            "Evidence freeze before subtraction",
            "Behavior evaluation contract",
            "Front-door invocation policy",
            "source/cache parity",
            "pre-existing failures",
        ):
            self.assertIn(phrase, text)
        for skill in (
            "harness-engineering",
            "harness-maintainer",
            "harness-verifier",
            "agents-md-engineer",
            "plugin-engineer",
            "skill-engineer",
        ):
            skill_text = (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("frontier-first-prompt-governance.md", skill_text)


if __name__ == "__main__":
    unittest.main()
