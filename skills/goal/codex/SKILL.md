---
name: goal
description: "Project-independent software goal workflow. Use for $goal, software requests beginning with Goal: or /goal, explicit Mode: auto, solo, solo-reviewed, or team, or requests to delegate software work to agents. Do not activate merely to discuss or edit workflow settings."
---

# Goal Workflow

Complete the user's software objective using the current project's conventions.
This skill is self-contained: no named repository, framework, model family, or
additional orchestration skill is required.

## Project context

Read `{{WORKFLOW_MD}}` and apply its skill-selection rules.
Include this path and the selected skill paths in delegation packets.

- Read applicable repository and scoped `AGENTS.md` instructions. Discover the
  affected modules, existing changes, build commands, and relevant tests before editing.
- Load available project skills when relevant or required by project instructions.
  A repository orchestrator may add project-specific rules but is not a prerequisite.
- If no project instructions or extra skills exist, infer conventions from the
  repository and proceed. If an explicitly required dependency is missing, report
  that specific blocker; do not invent its contents or silently waive it.
- Keep architecture, language, plan format, commands, and domain rules local to
  their project. Use the user's language unless project instructions require otherwise.

## Execution modes

State the selected mode and verification level briefly before substantial work.
Default to `auto`; honor an explicit mode without silently changing it.

| Mode | Implementation | Review |
| --- | --- | --- |
| `auto` | Lead by default; delegate a bounded task when it materially helps and applicable instructions permit it | Standard, or final-strict when requested or required |
| `solo` | Lead only; no subagents | Standard self-review |
| `solo-reviewed` | Lead only | Fresh independent final-strict reviewer |
| `team` | At least one bounded implementation worker, alongside useful lead work | Standard, or final-strict when requested or required |

If a requested mode cannot be honored because delegation is unavailable or an
independent review conflicts with `solo`, explain the conflict and ask for a
compatible choice before dependent work. Do not report a different mode as satisfied.

Use the current lead model and user-selected reasoning effort. Do not require a
particular model identity unless the user or applicable project instructions do.
For delegated work, prefer available `terra_worker` roles for coupled or ambiguous
implementation, `luna_worker` roles for fully specified mechanical edits, and the
`fresh_reviewer` role for independent review, when those roles fit the
project. Otherwise use an available general implementation or review agent.
Inherit model settings unless an applicable instruction specifies them.

## Implementation and verification

1. Turn the request into observable acceptance criteria. Identify assumptions and
   material uncertainty; investigate what can be resolved without user input.
2. Follow project planning requirements when planning is requested. Otherwise use
   a brief plan proportional to complexity and proceed with authorized work.
3. For behavior changes, establish a focused failing test or reproducible failure
   before the fix when feasible; follow stricter project TDD requirements. For new
   behavior, test the acceptance criteria. Documentation or configuration changes
   use appropriate structural and behavioral checks instead of artificial tests.
4. Make focused changes, preserve unrelated work, and run relevant checks. Expand
   testing when shared behavior, failures, or unresolved risks justify it.
5. Review the integrated diff against acceptance criteria. Report what changed,
   verification results, and any remaining blockers or unverified behavior.

## Delegation contract

When the spawn tool supports `fork_turns`, set `fork_turns: "none"` for
workers and reviewers so their context matches the self-contained packet.
For other runtimes, use their supported fresh-context mechanism. Do not assume
that a new agent automatically excludes the parent conversation.

Give each worker a bounded objective, owned files or responsibilities, acceptance
criteria, relevant project instructions, dependencies, and verification commands.
Tell workers they share the codebase and must preserve others' changes. Avoid
concurrent writes to the same files; sequence dependent work. Respect available
concurrency and keep the lead responsible for integration and verification.

## Final-strict review

Required for `solo-reviewed`, and when the user or project explicitly requires it.
Use a fresh read-only reviewer who did not implement the candidate; prefer the
`fresh_reviewer` role when it is available, otherwise another suitable
read-only review role or a general agent. Supply the request, applicable
instructions, candidate diff, and verification evidence. Review correctness,
regressions, scope, and missing acceptance evidence.

Resolve material findings, rerun affected checks, and have the reviewer reassess
changed areas. Keep follow-up review focused on findings and new changes.

Target one review round, with a hard maximum of three rounds per assurance unit
(the declared change scope being reviewed). A project may set a lower limit;
otherwise the limit is three. Count every review invocation that begins,
including a new reviewer spawn or a follow-up reassessment by an existing
reviewer. Fixes and retries within the same scope do not reset the budget, and
do not switch reviewers to obtain a more favorable verdict.

If material blockers remain when the budget is exhausted, or independent review
is unavailable, report that the gate is incomplete. A passing third round may
complete the gate; reaching the limit alone is never approval.
