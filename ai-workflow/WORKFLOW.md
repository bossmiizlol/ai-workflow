# Personal working agreements

These defaults apply across projects. Follow the current repository's instructions
for architecture, commands, contracts and data. User instructions take precedence.
Read the root and relevant scoped AGENTS.md or CLAUDE.md before changing files.
Do not import assumptions, paths, database names or workflows from another project.

## Work and communication

- Use Thai with this user unless they request another language. Keep code, paths,
  identifiers and repository artifacts in the project's conventions.
- State assumptions briefly, inspect evidence before diagnosing, and make focused
  changes. Preserve unrelated work and existing public contracts.
- Reuse existing components and utilities; add abstractions when real reuse warrants it.
- For behavior changes, use the project's tests and the personal
  test-driven-development skill together with any required repository supplement.
  For failures, use diagnosing-bugs to establish a reproducible signal first.
- Documentation and configuration-only work needs relevant validation, not invented
  application tests. Run focused checks and report what they do and do not prove.
- Review tools such as grill-me, junior-to-senior and last-20-percent apply when the
  user asks for their kind of review. Do not attach a review workflow to every task.
- Keep secrets and credentials out of responses, logs and committed files. Read only
  what the task requires and follow any repository file-reading restrictions.
- Complete authorized reversible work without repeated permission questions. Confirm
  destructive or external actions only when existing authorization does not cover them.

## Git and local configuration

Keep tracked edits visible. Do not use skip-worktree, assume-unchanged, custom
merge drivers or hooks to conceal changes. Use normal Git status and diffs.
Store personal reusable instructions and skills outside repositories. Share team
rules through reviewed tracked files when requested. Commit and push only when asked.
Before a destructive reset, verify a durable backup of changes and local-only data.

## Tool integration

Use the Goal workflow when the user explicitly invokes Goal or requests its modes
or delegation, if that tool has the installed goal skill. Configuration inspection
and edits alone do not activate Goal. Preserve the user's selected model and mode;
report missing capabilities rather than silently substituting another workflow.

## Skill selection

Use personal global skills as the source for reusable working methods. Keep
repository skills focused on domain rules, architecture, commands, and additional
project requirements. Update shared methods in the global source instead of
copying them into each repository.

When multiple skills cover the same method, use the exact path or source the user
explicitly selected. Otherwise prefer the personal global skill, unless applicable
repository instructions require a particular source. Always load required project
supplements as well; their domain constraints and stricter requirements still apply.
A project supplement adds local requirements to the shared method.

Resolve the global skill from the current tool's available skills and read that
source explicitly. Do not assume Codex and Claude discover the same directories.
Same-name skills are not automatically merged or overridden. This selection rule
does not change the tool's instruction precedence or skill discovery behavior.
If the global skill is unavailable, use an applicable repository skill or its
stated fallback and report the limitation. If neither provides the required
workflow, report the missing dependency before running it.

For tool-specific Goal integrations, use the Goal skill installed for the current
tool unless the user or repository explicitly selects another compatible source.
