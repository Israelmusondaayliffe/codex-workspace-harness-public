---
name: harness-maintainer
description: Audit and update an existing Codex harness after model changes, Codex releases, plugin updates, repeated corrections, stale instructions, failed automations, or capability drift. Use for weekly, monthly, or quarterly harness reviews, model-jump audits, obsolete-skill removal, routing parity checks, maintenance planning, and safe in-place upgrades.
---

# Harness Maintainer

Treat maintenance as a new audit and plan. Do not assume the previous harness state is current.

## Cadence

- Weekly: review outputs, Goal stops, automation results, failed checks, and repeated corrections.
- Monthly: review instruction chains, memory staleness, plugin and skill use, hooks, rules, and output hygiene.
- Quarterly or after major Codex changes: verify official platform behavior, model-specific prompt blocks, connectors, Browser, Computer Use, discovery, and security boundaries.

## Workflow

1. Run `harness-audit` against fresh state.
2. Compare current behavior with the last verified receipt.
3. Classify drift as user change, product change, broken dependency, stale policy, or missing enforcement.
4. Remove dead weight before adding new instructions.
5. Freeze prompt, model, tool, routing, plugin, hash, scorer, and behavior conditions before subtracting context.
6. Produce a reversible update plan and approval groups.
7. Run subtraction and capability-policy changes in small waves, with behavior checks after every task-start context mutation.
8. Run the standard build and verification phases, including installed-state checks.

Follow `../../references/model-change-policy.md` after every major model change.
Run the subtraction test monthly and after model updates. Use `../../references/frontier-first-prompt-governance.md` for the evidence, stopping, and rollback contract.
