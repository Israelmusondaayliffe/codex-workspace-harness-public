# Harness build contract

## Layers

1. Information: instructions, context, references, skills, plugins, connectors, and memory.
2. Execution: workspace boundaries, plans, scripts, rules, approvals, backups, and rollback.
3. Feedback: validators, receipts, reviews, failure records, and maintenance.

Keep all three layers present. More instructions do not compensate for missing execution controls or verification.

## Scope placement

- Global `AGENTS.md`: defaults that should apply across workspaces.
- Workspace `AGENTS.md`: layout, routing, output rules, and shared safety boundaries.
- Project `AGENTS.md`: project-specific inputs, workflows, tools, and success criteria.
- Skill: one reusable workflow.
- Plugin: a distributable bundle of related skills and optional tools.
- Script, rule, or hook: deterministic enforcement.

Place each requirement in the narrowest scope that must always see it.

## Reliability order

Prefer the least-free mechanism that fits:

1. Script
2. Command rule
3. Reviewed hook
4. Sandbox or permission setting
5. Template
6. Prompt instruction
7. `AGENTS.md`
8. Inference

## Public repository boundary

Track templates and examples, not completed personal context. Do not track generated outputs, local configuration, authentication data, connector payloads, memories, caches, or absolute user paths. Run the safety validator before every public push.
