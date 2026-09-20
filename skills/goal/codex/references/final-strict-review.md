## Final-strict review

Required for `solo-reviewed`, and whenever the user or the project explicitly
requires it. Use a fresh read-only reviewer that did not implement the candidate;
running the same model as the lead is fine, because independence comes from the
empty context, not a different model. A parent self-review is never an
independent review. Start a new reviewer with fresh context, without the
implementation conversation or the lead's private reasoning. If that isolation
is unavailable, report the review gate as incomplete. Reuse that reviewer, by
following up with the existing agent, only for reassessing its findings.

Freeze the candidate and get the project's full verification pass green first;
report blocked checks rather than implying they passed. Supply the reviewer with
the request, the applicable instructions, the complete change manifest — staged,
unstaged, untracked, and any locally excluded or `skip-worktree` files — and the
verification evidence you already have.

A review returns `ship`, `fix-first`, or `rethink`, with evidence for material
findings. Resolve material findings with the original implementer of that lane,
rerun the affected checks, refreeze, and have the reviewer reassess the changed
areas. Keep follow-up review focused on findings and new changes.

Target one review round, with a hard maximum of three rounds per assurance unit
(the declared change scope being reviewed). A project may set a lower limit;
otherwise the limit is three. Count every review invocation that begins,
including a new reviewer spawn or a follow-up reassessment by an existing
reviewer. Fixes and retries within the same scope do not reset the budget, and
do not switch reviewers to obtain a more favorable verdict.

If material blockers remain when the budget is exhausted, or independent review
is unavailable, report that the gate is incomplete. A passing third round may
complete the gate; reaching the limit alone is never approval.
