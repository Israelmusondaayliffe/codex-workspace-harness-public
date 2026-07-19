# Architecture

The harness is a layered operating system for Codex work.

## Instruction chain

```text
Thread request
  -> global ~/.codex/AGENTS.md
  -> workspace AGENTS.md
  -> PROJECTS/<slug>/AGENTS.md
  -> project references and templates
  -> selected skill or plugin
  -> scripts and validators
  -> verified output
```

Global instructions hold durable defaults. Workspace instructions define shared layout and routing. Project instructions define the closest contract. Skills and plugins hold reusable workflows. Scripts, rules, and reviewed hooks enforce exact behavior. Verification closes the loop.

## Repository map

| Path | Purpose | Public rule |
| --- | --- | --- |
| `AGENTS.md` | Workspace contract | Generic and tracked |
| `examples/global/` | Global contract example | Generic and tracked |
| `CONTEXT/` | Operator context templates | Only templates tracked |
| `PROJECTS/` | Registry, contracts, references | Generic examples tracked |
| `TEMPLATES/` | Reusable output shapes | Tracked |
| `CODEX-OUTPUTS/` | Generated work | Contents ignored |
| `plugins/` | Reusable capabilities | Tracked and validated |
| `integrations/` | Optional inactive templates | Tracked only after review |

## Why the plugin is included

The repository shows one mature structure. The plugin prevents that example from becoming a rigid prescription. It interviews the operator, audits the actual environment, proposes a right-sized plan, applies only approved changes, and verifies the resulting setup.
