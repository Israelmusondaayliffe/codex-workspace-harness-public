# Customization guide

Keep the starter small and add structure only when repeated work needs it.

## Global layer

Customize `examples/global/AGENTS.md` with defaults that should apply everywhere. Keep identity and stable policy concise.

## Workspace layer

Customize root `AGENTS.md` with shared folders, output rules, source routing, and safety boundaries.

## Project layer

Give each mature workstream a project folder, registry entry, `AGENTS.md`, and only the references required for that work.

## Capability layer

Use a skill for one reusable workflow. Use a plugin for a related set of skills or when distribution matters. Prefer existing capabilities before creating new ones.

## Enforcement layer

Move repeated exact requirements into scripts, command rules, reviewed hooks, templates, or validators. Keep hooks disabled until their code and authority are understood.

## Feedback layer

Define what proves success before execution. Keep machine checks separate from human judgment, and treat skipped or stale evidence as incomplete.
