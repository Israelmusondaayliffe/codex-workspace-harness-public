# Goal Template

Use this when work is sustained, bounded, and has a clear evidence surface. Do not use it for one-line edits, simple explanations, or single-answer questions.

```text
/goal <desired end state> verified by <specific evidence> while preserving <constraints>. Use <allowed inputs, tools, files, repos, connectors, Browser, Computer Use, and boundaries>. Between iterations, <how to choose the next action>. If waiting is required, <what scheduled follow-up should inspect and when it should stop>. If blocked or no valid paths remain, <what to report and what would clear the block>.
```

Every Goal must define:

1. Outcome: what should be true when done.
2. Verification surface: test, artifact, command output, source material, report, or review that proves it.
3. Constraints: what must not regress or change.
4. Boundaries: allowed files, tools, data, repos, connectors, and network use.
5. Iteration policy: how to decide what to try next after each attempt.
6. Blocked stop condition: when to stop and report instead of running to budget.
7. Surface plan: which source-owned connector, Browser, Chrome session, native app, or Computer Use flow is required, and why.
8. Loop plan: what to inspect on each pass, what counts as change, when to report nothing, and when to stop.

For Browser or Computer Use work, every iteration follows observe, act, re-observe, verify. Fresh rendered page state, DOM state, screenshot evidence, or app state can be part of the Goal's verification surface. A click, keystroke, or typed value is not evidence by itself.

If the Goal needs polling or a later continuation, schedule work back into the current task so it keeps the same context. Use a standalone scheduled task only when each run should be independent.

Before marking a Goal complete:

- Confirm the evidence surface exists.
- Confirm the constraints still hold.
- Confirm no protected path was changed.
- Confirm any output files live in `CODEX-OUTPUTS/YYYY-MM-DD/`.
- Run the relevant verification script or artifact-specific check.
- Confirm Browser or Computer Use actions were checked against fresh state after the action.
