# Project AGENTS.md: Harness Maintenance

This project maintains the reusable Codex harness in this repository.

## Purpose

Keep the instruction chain, workspace layout, plugin, privacy boundary, and verification surface usable and current.

## Inputs

- `references/build-contract.md`: architecture and placement rules.
- `references/maintenance-checklist.md`: recurring review surface.
- `plugins/harness-engineering/`: the bundled build and verification workflow.

## Workflow

1. Audit current files and behavior without changing them.
2. Separate verified facts, risks, and decisions.
3. Produce a reversible plan with explicit operation groups.
4. Back up affected existing files.
5. Apply only approved changes.
6. Run the repository safety validator and relevant plugin tests.
7. Record changed files, commands, results, and any unverified items.

## Success criteria

- No private context or secret material is tracked.
- The instruction chain resolves from global to workspace to project.
- Reusable workflows live in templates, scripts, skills, or plugins rather than repeated chat guidance.
- Completion has fresh structural and behavioral evidence.
