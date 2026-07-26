# Harness Engineering

Harness Engineering is a local-first Codex plugin that turns a rough operating brief into a personalized, installed, and verified Codex harness.

It does not copy one person's setup. It interviews the user, inspects the current environment, proposes the smallest useful architecture, and applies only approved changes after creating backups.

## Main workflow

1. Run `harness-interview` to establish needs, constraints, and success criteria.
2. Run `harness-audit` to inspect the current Codex home and workspace without changing them.
3. Run `harness-planner` to produce a decision-complete operations plan.
4. Review and approve operation groups.
5. Run `harness-builder` or `harness-runner` to apply the plan with durable state.
6. Run `harness-verifier` against fresh files and live discovery evidence.

The `harness-engineering` front door routes an end-to-end request through those phases.

## Safety model

- Audit and planning are read-only.
- Dry-run is the default for file operations.
- Every update requires an expected file hash and a backup.
- New files and updates are written atomically.
- Hooks, authentication, external publication, and third-party installs require separate approval.
- Reports record configuration keys and capability state, never secret values.

## Frontier-first maintenance

Harness Engineering treats model-visible instructions as a compact context kernel with delta-only overlays. It keeps personal plugin front doors in default context, loads specialists only when relevant, and moves examples plus exact checks beside the task that owns them. Prompt reductions are accepted only against frozen behavior, routing, installed-state, and rollback evidence.

See `references/frontier-first-prompt-governance.md` for the complete subtraction, invocation-policy, skill-pilot, and post-model-update contract.

## Included skills

- `harness-engineering`
- `harness-interview`
- `harness-audit`
- `harness-planner`
- `agents-md-engineer`
- `harness-builder`
- `skill-engineer`
- `plugin-engineer`
- `model-prompt-engineer`
- `harness-runner`
- `harness-verifier`
- `harness-maintainer`

## Local tooling

`scripts/harnessctl.py` uses only the Python standard library. It provides environment audit, schema validation, dry-run, approved apply, backup manifests, verification, and rollback.

Python 3.9 or newer is required for deterministic apply and rollback. Interview, reasoning, and plan generation can still run when Python is unavailable, but the plugin must stop before changing files.

## Data handling

The plugin has no telemetry or hosted service. It stores run state locally under the user's selected run directory. See `PRIVACY.md` and `SECURITY.md`.
