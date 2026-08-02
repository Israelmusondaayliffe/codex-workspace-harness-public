---
name: plugin-engineer
description: Create, update, validate, install, or package a plugin required by an approved harness architecture, for Claude Code, Claude Cowork, or Codex. Use when several related skills need a public or team bundle, when the harness needs plugin metadata or a marketplace entry, when a Claude Cowork plugin must be packaged as a validated ZIP archive, or when an existing local plugin must be updated and reinstalled with source-cache and fresh-discovery proof.
---

# Plugin Engineer

The manifest schema is shared; the packaging, install, and proof paths are not. Resolve the platform first, then follow its branch. Update means new version, never a silent overwrite.

## Shared workflow

1. Confirm that a plugin is justified instead of a local skill.
2. Define owned skills, front door, external tools, hooks, agents, and explicit exclusions.
3. Keep the manifest at `.claude-plugin/plugin.json` (Codex historically used `.codex-plugin`; check what the installed version expects). Include only component fields backed by real files.
4. Validate every owned skill and the complete plugin.
5. Bump the semver version on every change.
6. Prove visibility from a new task or fresh capability inventory after install.

## Platform branches

- Claude Cowork: use `scripts/package_plugin.py build --output <archive>.zip` to create a ZIP with `.claude-plugin/plugin.json` at the archive root. The package script supplies static archive proof only. Install it through the custom-plugin upload in **Cowork** > **Customize** > **Plugins**, or add a marketplace from a GitHub repository or git URL. Do not claim a live installation, discovery result, chat install card, or directory upload unless that exact path has been tested in the current app.
- Claude Code: scaffold or validate with `claude plugin validate`, install with `/plugin` or `claude plugin install` (test via `--plugin-dir`), and compare source against the cache under `~/.claude/plugins/cache/` after marketplace installs.
- Codex: scaffold with the system `plugin-creator` skill, install through `codex plugin marketplace add` and `codex plugin add`, verify with `codex plugin list --json`, then run `scripts/verify_install.py <plugin-path> --marketplace <marketplace-name>`. The verifier derives the cache root from `CODEX_HOME` or `~/.codex` and accepts `--cache-root` for an explicit isolated cache.

For task-start policy, keep the personal plugin front door implicit and hide an owned specialist only after a deterministic front-door case proves reachability. Keep explicit-only plugin skills and exact loose mirrors out of default context. Preserve unrelated metadata, roll out in reversible waves, and run an actual explicit hidden-skill smoke. Follow `../../references/frontier-first-prompt-governance.md`.

Public repository creation and marketplace submission remain separate external actions on every platform.
