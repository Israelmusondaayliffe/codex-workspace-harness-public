# Claude Code Codex Bridge

This directory preserves the project-scoped setup that enables the OpenAI Codex plugin inside Claude Code web containers.

The files are stored under `template/`, so they are inactive in this repository. Do not move them to the repository root or trust the hook without reviewing the exact commands.

## Activation

1. Review `template/.claude/settings.json` and `template/.claude/hooks/session-start.sh`.
2. Copy the template's `.claude` directory into the intended Claude Code project.
3. Configure `CODEX_AUTH_JSON_B64` through the Claude Code secret store only if login restoration is required.
4. Never commit the encoded authentication value or the decoded `auth.json` file.
5. Review and trust the project hook through Claude Code before depending on it.

The hook exits without action outside Claude Code remote containers. In a remote container, it installs the Codex CLI when missing and restores authentication only when the approved secret is present.
