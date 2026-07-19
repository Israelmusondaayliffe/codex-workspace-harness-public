# Project registry

This is the routing index for active workstreams. Add one entry per real project so Codex can find the correct contract and references without repeated explanation.

## Example project

Aliases:

- Example Project
- `example-project`

Path:

`PROJECTS/example-project/`

Use when:

- The request is a demonstration of project routing.
- You are testing the harness before adding a real workstream.

Load in this order:

1. `PROJECTS/example-project/AGENTS.md`
2. `PROJECTS/example-project/references/workflow.md`

Finished artifacts write to:

`CODEX-OUTPUTS/YYYY-MM-DD/example-project_[type]_v1.ext`

## Harness maintenance

Aliases:

- Harness Maintenance
- `harness`

Path:

`PROJECTS/harness/`

Use when:

- Updating instruction files, project patterns, templates, plugins, safety rules, or verification.
- Reviewing harness drift after a Codex or model change.

Load in this order:

1. `PROJECTS/harness/AGENTS.md`
2. `PROJECTS/harness/references/build-contract.md`
3. `PROJECTS/harness/references/maintenance-checklist.md`
