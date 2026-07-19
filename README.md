# Codex Workspace Harness

This repository is a depersonalized, clone-ready reference harness for Codex. It shows how to organize instructions, user context, projects, templates, outputs, reusable capabilities, safety boundaries, and verification without publishing a real operator's private workspace.

The included Harness Engineering plugin can interview you, audit an existing setup, propose a reviewable plan, apply approved changes with backups, and verify the result from fresh evidence.

## What is included

- A layered `AGENTS.md` example for global, workspace, and project scopes.
- Private-context templates that are ignored after you fill them in.
- A project registry and example project contract.
- Reusable document, Goal, project, and verification templates.
- A dated output convention that keeps generated work out of Git.
- The complete Harness Engineering plugin under `plugins/harness-engineering/`.
- A local plugin marketplace manifest for installation from this clone.
- A repository safety validator and an optional, disabled Claude Code bridge template.

## Start here

Requirements: Git, Codex, and Python 3.9 or newer.

```bash
git clone https://github.com/OWNER/codex-workspace-harness-public.git
cd codex-workspace-harness-public
codex plugin marketplace add .
codex plugin add harness-engineering@codex-workspace-harness
```

Replace `OWNER` with the repository owner when cloning a fork. Then open the repository in Codex and ask:

```text
Use Harness Engineering to interview me, audit this workspace, propose a plan, and stop for review before changing files.
```

The plugin does not blindly copy this reference setup. It uses the repository as an example, learns your requirements, and builds the smallest harness that fits your work.

## Manual setup

1. Copy `examples/global/AGENTS.md` to `~/.codex/AGENTS.md` and customize it.
2. Customize the root `AGENTS.md` for this workspace.
3. Copy the files in `CONTEXT/` without the `.template` suffix and fill them in. The completed files are ignored by Git.
4. Replace `PROJECTS/example-project/` with a real project and register it in `PROJECTS/README.md`.
5. Keep finished work in `CODEX-OUTPUTS/YYYY-MM-DD/`.
6. Run `python3 scripts/verify_repository_safety.py` before every public push.

See [Getting Started](docs/getting-started.md), [Architecture](docs/architecture.md), [Privacy Model](docs/privacy-model.md), and [Customization Guide](docs/customization.md).

## Safety

This repository intentionally contains no completed personal context, credentials, generated outputs, local configuration, or absolute home paths. Filled context files, local Codex settings, and outputs are ignored. The validator rejects tracked symlinks, secret-like values, private-key material, unsafe paths, and disallowed private content.

The Claude bridge is an inactive template. Do not enable it or provide authentication material until you have reviewed and approved it for your own environment.

## License

MIT. See `LICENSE`. The vendored plugin also carries its own MIT license.
