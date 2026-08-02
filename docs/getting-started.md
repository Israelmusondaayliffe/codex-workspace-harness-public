# Getting started

## 1. Install the bundled plugin

Install directly from the public GitHub repository:

```bash
codex plugin marketplace add Israelmusondaayliffe/harness-engineering-public --ref main
codex plugin add harness-engineering@harness-engineering-public
```

If you are working from a local clone or fork, add that repository root instead:

```bash
codex plugin marketplace add .
codex plugin add harness-engineering@harness-engineering-public
```

Confirm the plugin is listed and enabled:

```bash
codex plugin list --json
```

### Claude Cowork

Build a portable ZIP from the bundled plugin:

```bash
python3 plugins/harness-engineering/scripts/package_plugin.py build \
  --output plugins/harness-engineering/dist/harness-engineering.zip
```

The command validates the archive against the source before writing it. In Claude Desktop, open **Cowork**, then **Customize** > **Plugins**, choose the custom-plugin upload option, and select the generated ZIP. Do not upload the plugin folder or rely on a chat attachment install card.

You can also add this repository through **Customize** > **Plugins** > **+** > **Add marketplace** > **Add from a repository**, then install the plugin from that marketplace. The archive format and both UI paths are documented in Anthropic's [plugin guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) and [organization marketplace guide](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization); this local clone has static package proof only, not a live Cowork installation or fresh-task discovery result.

## 2. Create private context

Copy each file in `CONTEXT/` without the `.template` suffix. Completed context files are ignored by Git. Add only information that changes how work should be planned or executed.

## 3. Add a real project

Copy `PROJECTS/example-project/`, rename it with a short slug, replace its contract and references, then add an entry to `PROJECTS/README.md`.

## 4. Run Harness Engineering

Follow this sequence:

1. Start with the plugin's interview, or say `grill me`.
2. Ask it to audit the current setup. Keep this stage read-only.
3. Review the proposed plan and operation groups.
4. Approve only the changes you want.

Use approval-first permissions by default. Choose a manual, plan, or review-before-each-change mode when your host offers one. Do not begin with full access. Broader access should be a specific, reviewed decision for a known operation.

The core workflow is self-contained in this plugin. Optional integrations can be detected or added later, but they are not prerequisites for interview, audit, planning, approved changes, or verification.

## 5. Verify

Run:

```bash
python3 scripts/verify_repository_safety.py
python3 plugins/harness-engineering/scripts/verify_bundle.py plugins/harness-engineering
python3 -m unittest discover -s plugins/harness-engineering/tests -v
```

Test discovery from a fresh Codex task after installation. Filesystem presence alone does not prove that a plugin is usable.
