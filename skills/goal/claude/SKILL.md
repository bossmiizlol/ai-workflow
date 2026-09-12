---
name: goal
description: "Project-independent software goal workflow. Use for requests beginning with Goal: or /goal, for an explicit Mode: auto, solo, solo-reviewed, or team, or when asked to delegate software work to subagents, a team, or parallel workers. Do not activate merely to discuss or edit workflow settings."
argument-hint: "[Mode: auto|solo|solo-reviewed|team] <what to build, fix, or change>"
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

- Read the repository's `AGENTS.md` and/or `CLAUDE.md`, plus the scoped
  instruction file of every directory the task may touch. Do this even when the
  session started at the repository root. If scope expands mid-task, read the
  newly applicable ones before continuing.
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

For delegated work, prefer these agents when the session offers them:

- **`sonnet-worker`** — coupled, ambiguous, multi-file, or judgment-heavy
  implementation. This is the default when routing is not obvious.
- **`haiku-worker`** — fully specified mechanical edits: a rename, a formatting
  or lint sweep, one already-chosen pattern applied across many files. Its
  failure mode is guessing plausibly on an ambiguous packet, so a blocker report
  from it is the lane working.
- **`fresh-reviewer`** — independent read-only review. Pick its model to fit the
  change; the reviewer must never be the agent that wrote the code.

If those are unavailable, use a general implementation or review agent the
session actually has. Inherit model settings unless an instruction specifies
them.

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

## Delegation contract

Give each worker a bounded objective, owned files or responsibilities,
acceptance criteria with the exact command that proves them, the project
instructions its lane touches, dependencies, and verification commands. A worker
must receive a self-contained packet. Use the current runtime's supported
fresh-context mechanism; do not assume it inherits files the lead has read.
Do not copy Codex-only spawn parameters into Claude tool calls.

Tell workers they share the codebase and must preserve others' changes. Avoid
concurrent writes to the same files; sequence dependent work. Prefer one worker
and add a second only for genuinely independent lanes with disjoint write scope.
Respect available concurrency, and keep the lead responsible for integration and
verification.

Write packets and worker reports in English. Everything the user reads follows
the user's language and the project's communication rules.

## Final-strict review

Required for `solo-reviewed`, and whenever the user or the project explicitly
requires it. Use a fresh read-only reviewer that did not implement the candidate;
running the same model as the lead is fine, because independence comes from the
empty context, not a different model. A parent self-review is never an
independent review. Start a new reviewer with the current runtime's supported
fresh-context mechanism, without the implementation conversation or the lead's
private reasoning. If that isolation is unavailable, report the review gate as
incomplete. Reuse that reviewer only for reassessing its findings.

Freeze the candidate and get the project's full verification pass green first.
Supply the reviewer with the request, the applicable instructions, the complete
change manifest — staged, unstaged, untracked, and any locally excluded or
`skip-worktree` files — and the verification evidence you already have.

A review returns `ship`, `fix-first`, or `rethink`. Resolve material findings
with the original implementer of that lane, rerun the affected checks, refreeze,
and have the reviewer reassess the changed areas. Keep follow-up review focused
on findings and new changes.

Target one review round, with a hard maximum of three rounds per assurance unit
(the declared change scope being reviewed). A project may set a lower limit;
otherwise the limit is three. Count every review invocation that begins,
including a new reviewer spawn or a follow-up reassessment by an existing
reviewer. Fixes and retries within the same scope do not reset the budget, and
do not switch reviewers to obtain a more favorable verdict.

If material blockers remain when the budget is exhausted, or independent review
is unavailable, report that the gate is incomplete. A passing third round may
complete the gate; reaching the limit alone is never approval.

## Finishing

Follow the project's completion rules — contract/doc updates, its documentation
check, and its "done" bar. Never report done without the project's own passing
check.
