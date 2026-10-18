# Personal pstack compatibility

Applies only when the user selects pstack or poteto-mode. Keep this supplement
outside plugin caches so marketplace updates preserve it. It adapts runtime
mechanics; the installed pstack skills still define their workflows. Resolve
conflicts in favor of explicit user requirements and applicable instruction
precedence.

## Runtime capabilities

Treat the tools and agent definitions exposed in the current session as the
source of truth. Plugin tool mappings are guidance, not proof of availability.
Use a structured user-input tool when it is available and permitted in the
current mode; otherwise ask in text. Check current agent status and use the
supported wait, follow-up, or interrupt operation for the intended action. Use
available task tracking, or the playbook's local checklist fallback.

Inspect the Agent schema before passing `run_in_background`.
Fork mode may remove this option and run spawned agents in the background.
Await actual completion rather than assuming a foreground call is available.

## Overlapping skills

When pstack is selected, use pstack's own skill for a method it covers, even
when a personal global skill covers the same method. This replaces the shared
"prefer the personal global skill" rule for that task only. Current overlaps:
`pstack:tdd` over `test-driven-development`, `pstack:unslop` over `deslopify`,
and `pstack:interrogate` over `junior-to-senior`. Global skills with no pstack
equivalent (`diagnosing-bugs`, `grill-me`, `handoff`, `last-20-percent`,
`improve-codebase-architecture`) stay available under their usual triggers.

## Models and delegation

Preserve the user's selected lead model and effort. For delegates, explicit user
or project requirements take precedence over pstack defaults. Otherwise use
pstack's role defaults and runtime mapping only for models available in that
session; example model names do not establish availability. Do not silently
substitute for an unavailable required model or independent-review capability.
Use a compatible supported alternative when the existing instructions allow it,
or report the specific limitation before dependent work.

Check restrictions on model overrides and inherited context before spawning.
Keep independent reviewers separate from implementation context. Pass this
supplement and applicable personal/project instruction paths in delegate packets.

## Maintenance

Keep `session hook: off` in `~/.claude/pstack-models.md`.
Do not modify vendor cache files to apply these adaptations. After updating the
plugin, compare its runtime mapping with current tool schemas and remove local
adaptations that are no longer needed. Check named skill dependencies when a
playbook needs them; installation alone does not establish their availability.
