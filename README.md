# Harness Engineering Public

This repository is a depersonalized, clone-ready reference harness for Claude Code, Claude Cowork, and Codex. It shows how to organize instructions, user context, projects, templates, outputs, reusable capabilities, safety boundaries, and verification without publishing a real operator's private workspace.

The included Harness Engineering plugin can interview you, audit an existing setup, propose a reviewable plan, apply approved changes with backups, and verify the result from fresh evidence.

## Install Harness Engineering

On Claude Code:

```bash
claude plugin marketplace add Israelmusondaayliffe/harness-engineering-public
claude plugin install harness-engineering@harness-engineering-public
```

Or inside a session: `/plugin install harness-engineering@harness-engineering-public`.

On Claude Cowork: upload the `plugins/harness-engineering/` folder through My Uploads, or hand Cowork this repository URL and ask it to install the plugin.

On Codex, copy this block:

```text
Install the Harness Engineering plugin from the public repository.

Run:
codex plugin marketplace add Israelmusondaayliffe/harness-engineering-public --ref main
codex plugin add harness-engineering@harness-engineering-public

Then confirm that Harness Engineering is enabled and that all 13 namespaced skills are visible. After installation, use Harness Engineering to interview me, audit my current setup, propose a plan, and stop for review before changing files.
```

Or run the installation commands directly:

```bash
codex plugin marketplace add Israelmusondaayliffe/harness-engineering-public --ref main
codex plugin add harness-engineering@harness-engineering-public
```

## Recommended first run

Use this order after installation:

1. Start with the plugin's interview, or say `grill me`, so it can learn what you need.
2. Ask it to audit your current setup. The audit should be read-only.
3. Read the proposed plan and operation groups.
4. Approve only the changes you actually want.

Use approval-first permissions by default. Choose a manual, plan, or review-before-each-change mode when your host offers one. Do not start with full access. Grant broader access only for a specific reviewed operation when you understand the files, permissions, and external actions involved.

The core Harness Engineering workflow works as one installed plugin. Optional integrations may be detected or used later, but they are not required for the core interview, audit, planning, approved-build, and verification flow.

## What is included

- A layered `AGENTS.md` example for global, workspace, and project scopes.
- Private-context templates that are ignored after you fill them in.
- A project registry and example project contract.
- Reusable document, Goal, project, and verification templates.
- A dated output convention that keeps generated work out of Git.
- The complete Harness Engineering plugin under `plugins/harness-engineering/`.
- A local plugin marketplace manifest for installation from this clone.
- A repository safety validator and an optional, disabled Claude Code bridge template.

## Clone the reference harness

Requirements: Git, Python 3.9 or newer, and at least one host (Claude Code, Claude Cowork, or Codex).

```bash
git clone https://github.com/OWNER/harness-engineering-public.git
cd harness-engineering-public
codex plugin marketplace add .
codex plugin add harness-engineering@harness-engineering-public
```

Replace `OWNER` with the repository owner when cloning a fork. Then open the repository in your host (Claude Code, Cowork, or Codex) and ask:

```text
Use Harness Engineering to interview me, audit this workspace, propose a plan, and stop for review before changing files.
```

The plugin does not blindly copy this reference setup. It uses the repository as an example, learns your requirements, and builds the smallest harness that fits your work.

## Manual setup

1. On Codex, copy `examples/global/AGENTS.md` to `~/.codex/AGENTS.md` and customize it. On Claude Code, use it as the model for `~/.claude/CLAUDE.md`.
2. Customize the root `AGENTS.md` for this workspace. Claude Code sessions load the root `CLAUDE.md`, which defers to the same contract.
3. Copy the files in `CONTEXT/` without the `.template` suffix and fill them in. The completed files are ignored by Git.
4. Replace `PROJECTS/example-project/` with a real project and register it in `PROJECTS/README.md`.
5. Keep finished work in `OUTPUTS/YYYY-MM-DD/`.
6. Run `python3 scripts/verify_repository_safety.py` before every public push.

See [Getting Started](docs/getting-started.md), [Architecture](docs/architecture.md), [Privacy Model](docs/privacy-model.md), and [Customization Guide](docs/customization.md).

## Safety

This repository intentionally contains no completed personal context, credentials, generated outputs, local configuration, or absolute home paths. Filled context files, local Codex settings, and outputs are ignored. The validator rejects tracked symlinks, secret-like values, private-key material, unsafe paths, and disallowed private content.

The Claude bridge is an inactive template. Do not enable it or provide authentication material until you have reviewed and approved it for your own environment.

## License

MIT. See `LICENSE`. The vendored plugin also carries its own MIT license.
