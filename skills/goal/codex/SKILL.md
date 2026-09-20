---
name: goal
description: "Project-independent software goal workflow. Use for $goal, software requests beginning with Goal: or /goal, explicit Mode: auto, solo, solo-reviewed, or team, or requests to delegate software work to agents. Do not activate merely to discuss or edit workflow settings."
---

# Goal Workflow

Complete the user's software objective using the current project's conventions.
This skill is self-contained: no named repository, framework, model family, or
additional orchestration skill is required.

Do not run this workflow for a request that only discusses or edits workflow
configuration — the mode table, the agent files, settings, or a repository's
agent docs. That is ordinary work.

## Project context

Read `{{WORKFLOW_MD}}` and apply its skill-selection rules.
Include this path and the selected skill paths in delegation packets.

- Read the repository's `AGENTS.md`, plus the scoped instruction file of every
  directory the task may touch. Do this even when the session started at the
  repository root. If scope expands mid-task, read the newly applicable ones
  before continuing.
- Discover the affected modules, existing uncommitted changes, build commands,
  and relevant tests before editing.
- Load the project skills its instructions require, plus any that are clearly
  relevant to the lane. A repository orchestration skill adds project rules but
  is not a prerequisite for this workflow.
- If no project instructions or extra skills exist, infer conventions from the
  repository and proceed. If an explicitly required dependency is missing, report
  that specific blocker; never invent its contents or silently waive it.
- Keep architecture, language, plan format, commands, and domain rules local to
  their project. Use the user's language unless project instructions require
  otherwise.

## Invocation boundary

Interpret explicit software delegation requests in the user's language, including
Thai requests such as “แบ่งงานให้ subagents ช่วยแก้บั๊ก”. Merely mentioning Goal,
quoting a mode, or asking to inspect or edit workflow settings does not activate it.

## Execution modes

State the selected mode and assurance level briefly before substantial work,
including what selected each. Default to `auto`; honor an explicit mode without
silently changing it.

| Mode | Implementation | Review |
| --- | --- | --- |
| `auto` | Lead by default; delegate a bounded lane when it materially helps and project instructions permit it | Standard, or final-strict when requested or required |
| `solo` | Lead only; no subagents at all | Standard self-review |
| `solo-reviewed` | Lead only; no implementation worker | Always final-strict, by a fresh independent reviewer |
| `team` | At least one bounded implementation worker, alongside useful lead work | Standard, or final-strict when requested or required |

The lead never delegates orchestration. Decomposition, conflict resolution,
integration, verification, and the user-facing summary stay with the lead in
every mode.

Assurance and mode are separate axes. `team` does **not** imply final-strict;
`solo-reviewed` always does. Every mode still honors the project's own review
requirements — if repository instructions require a review gate for the code in
play, apply it even in `auto` or `solo`, and if that conflicts with `solo`, raise
the conflict before implementing.

If a requested mode cannot be honored — delegation is unavailable, no reviewer
agent exists, or independent review conflicts with `solo` — explain the specific
limitation and ask for a compatible choice before doing dependent work. Never
report a different mode as satisfied, and never quietly downgrade one.

## Models

Use the current lead model and the user's selected reasoning effort. Do not
require a particular model identity, and do not ask the user to switch, unless
the user or the applicable project instructions say so.

When delegating, read [delegation](references/delegation.md) for role selection,
ownership, context isolation, and verification packets.

## Implementation and verification

1. Turn the request into observable acceptance criteria. Name assumptions and
   material uncertainty; resolve what you can without asking the user.
2. Follow the project's planning requirements when planning is requested.
   Otherwise use a brief plan proportional to complexity — `step → verify: check`
   — and proceed with authorized work.
3. For behavior changes, establish a focused failing test or reproducible failure
   before the fix when feasible; follow stricter project TDD requirements where
   they exist. For new behavior, test the acceptance criteria. Documentation and
   configuration changes use structural and behavioral checks instead of
   artificial tests.
4. Make focused changes, preserve unrelated work, and run relevant checks. Expand
   testing when shared behavior, failures, or unresolved risk justify it.
5. Review the integrated diff yourself against the acceptance criteria — a
   worker's report is a claim, not evidence. Report what changed, verification
   results, and any remaining blockers or unverified behavior.

## Final-strict review

For `solo-reviewed`, or when the user/project requires independent review, read
[the final-strict review procedure](references/final-strict-review.md). Preserve
fresh-context independence, the review-round budget, and the incomplete-gate
reporting rules. Self-review does not satisfy this assurance level.

## Finishing

Follow the project's completion rules — contract/doc updates, its documentation
check, and its "done" bar. Never report done without the project's own passing
check.
