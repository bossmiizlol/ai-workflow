# Delegation

For delegated work, prefer these roles when the session offers them:

- **`terra_worker`** — coupled, ambiguous, multi-file, or judgment-heavy
  implementation. This is the default when routing is not obvious.
- **`luna_worker`** — fully specified mechanical edits: a rename, a formatting
  or lint sweep, one already-chosen pattern applied across many files. Its
  failure mode is guessing plausibly on an ambiguous packet, so a blocker report
  from it is the lane working.
- **`fresh_reviewer`** — independent read-only review. The reviewer must never
  be the agent that wrote the code.

If those are unavailable, use a general implementation or review agent the
session actually has. Inherit model settings unless an instruction specifies
them.

## Delegation contract

Give each worker a bounded objective, owned files or responsibilities,
acceptance criteria with the exact command that proves them, the project
instructions its lane touches, dependencies, and verification commands. A worker
must receive a self-contained packet; do not assume it inherits files the lead
has read. When the spawn tool supports `fork_turns`, set `fork_turns: "none"` for
workers and reviewers so their context matches the packet. For other runtimes,
use their supported fresh-context mechanism. Do not assume that a new agent
automatically excludes the parent conversation.

Do not integrate, verify, or review a lane before that agent has finished, and
never predict or summarize a result that has not arrived. To continue an agent
with its context intact — sending review findings back to the original
implementer, or asking a reviewer to reassess — send a follow-up to that existing
agent rather than spawning a new one, which would start with no memory of the lane.

Tell workers they share the codebase and must preserve others' changes. Avoid
concurrent writes to the same files; sequence dependent work. Prefer one worker
and add a second only for genuinely independent lanes with disjoint write scope.
Respect available concurrency, and keep the lead responsible for integration and
verification.

Write packets and worker reports in English. Everything the user reads follows
the user's language and the project's communication rules.
