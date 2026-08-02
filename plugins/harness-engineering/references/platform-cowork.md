# Platform: Claude Cowork

Cowork is the Claude desktop app's task workspace. Tasks run in a managed cloud sandbox or in a local VM on the user's computer. The session filesystem is ephemeral. This changes harness design more than any other platform difference.

## Where the harness actually lives

Nothing durable lives inside the session. A Cowork harness is distributed across:

1. Global instructions and user preferences set in the app. These arrive in every session and are the equivalent of a global instruction file. They are edited by the user in settings, not by writing a file.
2. Connected folders on the user's device. Contract files at a folder root (for example `CLAUDE.md` plus companion files the contract imports by instruction) are the workspace and project layer. The user's global instructions must tell Claude to read them, since Cowork does not auto-load folder files.
3. Installed plugins and skills. Plugin skills appear namespaced as `plugin:skill` and are cached into each session under `~/.claude/plugins/synced/`.
4. Connectors (MCP servers) managed in the app, reaching Gmail, Notion, and similar systems.
5. Memory and past-chat retrieval, where the user has them enabled.

Design rule: any state the harness needs next week must land in a connected folder, a connector-backed system, or app-level instructions before the session ends. Sandbox-only files die with the session.

## Session mechanics that shape harness work

- Uploads and staged device files appear under `/mnt/user-data/uploads/`, read-only.
- Files reach the user only through explicit delivery (file send) or by committing back to a connected folder. A file merely written in the sandbox has not shipped.
- Folder access is granted at session start; new folders cannot be assumed mid-task.
- Scheduled tasks are the automation surface. Hooks are effectively unavailable to end users, and subagent definitions are uncommon; do not design a Cowork harness around them.
- Deterministic enforcement is achieved with validator scripts stored in a connected folder and run by contract, not with lifecycle hooks.

## Plugins and skills

- Anthropic documents two supported distribution paths: upload a custom plugin file in **Customize** > **Plugins**, or add a plugin marketplace from a GitHub repository or git URL. For a manually uploaded release candidate, use a valid ZIP with `.claude-plugin/plugin.json` at the archive root. Do not claim that a folder, repository URL pasted into chat, or a `.plugin` extension alone is an install method without live proof from the current app. See Anthropic's [plugin guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) and [marketplace guide](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).
- Plugin structure follows the shared schema: `skills/*/SKILL.md`, optional `agents/`, optional `.mcp.json`, manifest in `.claude-plugin/`.
- Skills use progressive disclosure: lean SKILL.md, depth in `references/`.
- Namespaced plugin skills outrank loose copies of the same skill when both exist.

## Verification

- Structural: manifest parses, every skill directory has a valid SKILL.md, no placeholders.
- Behavioral: the plugin appears in the user's plugin list after install, and a fresh task lists the namespaced skills in its capability inventory. Static ZIP validation does not establish either result.
- Contract files: prove they exist at the connected folder root and that the session actually read them, not that they merely exist.
- There is no CLI validator inside a Cowork session. Verify structure with scripts in the sandbox and behavior from the live app surface.

## Harness placement guidance

- Personal policy: app-level global instructions, kept short.
- Workspace and project truth: contract files at the connected folder root.
- Exact behavior: validator scripts in the folder, invoked by contract.
- Reusable workflows: plugin skills, installed once, versioned deliberately.
- Continuity: dated output folders and living artifacts inside the connected folder.
