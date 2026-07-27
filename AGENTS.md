# Workspace AGENTS.md

This file is the workspace contract for a reusable multi-host harness (Claude Code, Claude Cowork, Codex). A global contract may exist at `~/.codex/AGENTS.md` on Codex or `~/.claude/CLAUDE.md` on Claude Code; project contracts inside `PROJECTS/` add narrower instructions. On Claude Code the root `CLAUDE.md` defers to this file, so the contract is written once.

## Purpose

Use this workspace to turn repeated work into durable files, scripts, templates, projects, and verified outputs. Prefer the source of truth closest to the work.

## Working method

For non-trivial work, use four phases:

1. Explore: read the brief, applicable instruction chain, project registry, and relevant references.
2. Plan: define the sequence, allowed changes, success criteria, risks, and evidence.
3. Execute: make the smallest complete change within the approved boundary.
4. Verify: run deterministic checks and inspect the real output before reporting completion.

Ask only when missing information changes the result or safety boundary. Otherwise state assumptions and proceed.

## File layout

- `CONTEXT/`: private operator context. Completed files are ignored by Git.
- `PROJECTS/`: project registries, contracts, and references.
- `TEMPLATES/`: reusable output and workflow shapes.
- `OUTPUTS/YYYY-MM-DD/`: finished generated work. Contents are ignored by Git.
- `plugins/`: bundled, distributable capabilities.
- `integrations/`: optional templates that remain disabled until reviewed.

Do not commit credentials, authentication files, local settings, generated outputs, memories, caches, personal profiles, or absolute home paths.

## Context loading

Use progressive disclosure:

1. Read this file.
2. Read `PROJECTS/README.md` when a project or workstream is named.
3. Read the matching `PROJECTS/<slug>/AGENTS.md`.
4. Read only the referenced files required by the task.
5. Load a skill or plugin when its trigger matches the work.

The closest contract file (`AGENTS.md`, or `CLAUDE.md` on Claude Code) wins when instructions conflict.

## Outputs

Finished work belongs in `OUTPUTS/YYYY-MM-DD/` and uses `projectname_type_v1.ext`. Increment the version instead of silently overwriting an earlier deliverable. Source code for a real project belongs in its own project or repository, not in the output folder.

## Safety and authority

Technical access is not authority for unrelated writes, publication, messages, purchases, account changes, authentication, permission changes, or deletion. Keep external publication, hooks, connector authentication, and third-party installation as separate approvals.

Preserve unrelated work. Back up existing files before approved replacements. Prefer dry-runs, hash preconditions, atomic writes, and rollback manifests for broad changes.

## Verification

Before declaring completion:

- Check each requirement against current evidence.
- Run the narrowest relevant validator or test.
- Confirm files are at the intended paths.
- Mark unknown or untested claims plainly.
- Run `python3 scripts/verify_repository_safety.py` before publishing changes to this repository.
