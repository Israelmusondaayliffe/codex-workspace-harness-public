# Security

## Boundary

Harness Engineering treats technical access as separate from user authority. It reads only the sources relevant to the requested harness and changes only approved paths.

## Write controls

- Use dry-run before apply.
- Reject path traversal and targets outside approved roots.
- Reject writes through symbolic-link targets.
- Require the audited hash before updating an existing file.
- Back up every updated file before replacement.
- Use atomic replacement for file writes.
- Record every change and rollback action.

## Sensitive actions

Do not silently install third-party code, trust hooks, authenticate connectors, edit external accounts, create public repositories, or publish marketplace entries.

Report security issues through the repository's private security-reporting channel before public disclosure. Do not include credentials or private source material in a public issue.
