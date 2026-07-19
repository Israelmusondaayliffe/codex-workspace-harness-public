# Getting started

## 1. Install the bundled plugin

Install directly from the public GitHub repository:

```bash
codex plugin marketplace add Israelmusondaayliffe/codex-workspace-harness-public --ref main
codex plugin add harness-engineering@codex-workspace-harness
```

If you are working from a local clone or fork, add that repository root instead:

```bash
codex plugin marketplace add .
codex plugin add harness-engineering@codex-workspace-harness
```

Confirm the plugin is listed and enabled:

```bash
codex plugin list --json
```

## 2. Create private context

Copy each file in `CONTEXT/` without the `.template` suffix. Completed context files are ignored by Git. Add only information that changes how work should be planned or executed.

## 3. Add a real project

Copy `PROJECTS/example-project/`, rename it with a short slug, replace its contract and references, then add an entry to `PROJECTS/README.md`.

## 4. Run Harness Engineering

Ask the plugin to interview you and audit the workspace. Review the resulting plan before approving any file changes, hooks, authentication, installation, or publication.

## 5. Verify

Run:

```bash
python3 scripts/verify_repository_safety.py
python3 plugins/harness-engineering/scripts/verify_bundle.py plugins/harness-engineering
python3 -m unittest discover -s plugins/harness-engineering/tests -v
```

Test discovery from a fresh Codex task after installation. Filesystem presence alone does not prove that a plugin is usable.
