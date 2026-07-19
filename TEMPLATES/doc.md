# Document Template

Use this template for memos, briefs, operating docs, plans, specs, summaries, proposals, and other structured documents.

## Source Skills

Default skill chain:

- `business-writing-intent-enforcer` for reader intent, document job, structure, decisions, risks, and next steps.
- `writing-enforcer` for final quality checks, voice cleanup, and anti-AI pattern removal.
- `doc` only when the final artifact must become a `.docx` file with formatting or layout checks.

## Required Inputs

Before drafting, identify:

- Reader: `[who will read this]`
- Reader action: `[decide, approve, execute, review, align, respond, learn]`
- Document job: `[one sentence]`
- Document type: `[decision memo, operating spec, project plan, executive summary, proposal, brief, custom]`
- Source material: `[files, links, notes, transcript, Notion page, Drive file, email, chat context]`
- Evidence standard: `[provided context only, local files, connector sources, web citations, assumptions allowed]`
- Output destination: `CODEX-OUTPUTS/YYYY-MM-DD/[projectname]_doc_v1.md`

If the reader, document job, or source material is missing and cannot be inferred safely, ask one concise question before drafting.

## Document Type Map

Use the smallest structure that fits the job.

### Decision Memo

Use when the reader must approve, reject, or choose.

Sections:

1. Recommendation
2. Context
3. Options
4. Risks
5. Decision Needed

### Operating Spec

Use when the reader must execute consistently.

Sections:

1. Purpose
2. Rules
3. Workflow
4. Edge Cases
5. Acceptance Checks

### Project Plan

Use when the reader must understand sequence, ownership, or dependencies.

Sections:

1. Objective
2. Phases
3. Dependencies
4. Risks
5. Verification

### Executive Summary

Use when the reader needs fast comprehension.

Sections:

1. What Changed
2. Why It Matters
3. Recommended Action
4. Open Questions

## Drafting Workflow

1. Read the relevant source material and reference files.
2. State the reader and document job before drafting.
3. Select the document type map or create a custom section set.
4. Separate facts, assumptions, risks, and open questions.
5. Put the recommendation, action, or decision point near the top.
6. Remove generic context that does not help the reader act.
7. Add a verification section only when it helps the reader trust the work.
8. Save the final draft to `CODEX-OUTPUTS/YYYY-MM-DD/`.

## Output Contract

Every finished document should include:

- Clear title.
- Reader and document job when useful.
- Recommendation, decision, action, or purpose near the top.
- Evidence and assumptions separated.
- Concrete risks or tradeoffs.
- Open questions if anything remains unresolved.
- Next step or decision point.

Do not include:

- Decorative introductions.
- Generic business filler.
- Unsupported numbers or outcomes.
- Claims that do not trace to source material.
- A long summary when the reader needs a decision.

## Verification Checklist

Before delivery:

- Reader is explicit or obvious from the brief.
- Document job is explicit.
- The structure matches the job.
- Facts and assumptions are separated.
- Risks are concrete.
- Open questions are visible.
- Next step is clear.
- No em-dashes.
- No banned AI cliches.
- Final path follows `CODEX-OUTPUTS/YYYY-MM-DD/[projectname]_doc_v1.md`.

## Reuse Notes

When creating a `.docx`, first create the Markdown content, then convert or rebuild it using the `doc` skill. Render and inspect the final pages when layout matters.
