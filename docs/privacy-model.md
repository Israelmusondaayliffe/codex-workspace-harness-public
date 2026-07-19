# Privacy model

The public repository stores structure, examples, templates, and reusable code. It does not store a real operator profile or working history.

## Keep local

- Completed context files.
- Generated outputs and media.
- Local Codex, Claude, editor, and tool settings.
- Credentials, tokens, cookies, private keys, environment files, and authentication data.
- Connector payloads, email, calendars, memories, caches, and transcripts.
- Absolute home paths and machine-specific configuration.
- Private project briefs, client information, and internal source material.

## Before publication

Run the repository validator, review `git diff --check`, inspect tracked paths, and scan the complete new history for names, email addresses, absolute paths, secret-like values, and private-key material.

If a private file is committed, removing it in a later commit does not remove it from history. Rewrite or replace the public history before publication and rotate any exposed credential.
