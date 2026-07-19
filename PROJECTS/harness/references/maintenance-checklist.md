# Harness maintenance checklist

## Every change

- Read the applicable `AGENTS.md` chain.
- Preserve unrelated files.
- Review the complete diff.
- Run `python3 scripts/verify_repository_safety.py`.
- Run plugin verification and tests when the plugin changes.
- Record any skipped or unavailable check as a failure or open item.

## Monthly

- Review global, workspace, and project instructions for duplication or drift.
- Confirm completed context and output files remain ignored.
- Review templates, project aliases, plugin metadata, and optional integrations.
- Remove stale examples before adding more instructions.

## After platform or model changes

- Check current official behavior before changing configuration.
- Re-run representative harness tasks.
- Test tool routing, approval behavior, output paths, and stop conditions.
- Keep stable policy separate from temporary model compensation.
