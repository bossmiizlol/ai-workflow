# Personal pstack compatibility

Applies when the user selects pstack, poteto-mode, or a named pstack skill. Keep this supplement
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

Use the delegation tools actually exposed by the host (for example,
`collaboration.spawn_agent`), rather than assuming an `Agent` tool exists.
Pass only parameters in the exposed schema; do not infer `run_in_background`
or foreground behavior from another runtime. Wait for completion before using
an agent's final result. Follow the host's context-inheritance and model-override
constraints, and its concurrency limit. Tool availability alone does not authorize
delegation; follow the user's request and applicable session instructions.

For current Codex, inspect `[agents]` before following the vendor mapping's
`features.multi_agent` example. `agents.enabled` controls availability;
`agents.max_concurrent_threads_per_session` counts children, excluding the lead.
The live host limit still wins. Do not add a second toggle just because the
vendor example uses another supported setting. Official reference:
https://learn.chatgpt.com/docs/config-file/config-reference

The vendor statement that Codex has no structured-choice tool is not universal.
Use `request_user_input_async` when exposed, or `request_user_input` only when
the host permits it in the current mode. Otherwise ask in text. A pending
required answer is not permission to proceed.

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

On hosts exposing `fork_turns`, follow the actual schema: a full-history fork
may inherit both model and effort and reject overrides. If selecting a role
model requires `fork_turns="none"`, send a self-contained task with the relevant
file paths, constraints, and validation requirements. For `default effort:
session`, use the host's documented inheritance behavior when it guarantees
inheritance for that dispatch; otherwise resolve the current turn's effort
using the vendor helper or request an explicit effort. Never infer active effort
from `config.toml` defaults or a previous turn.

## Maintenance

For Codex, keep `session hook: off` in `$CODEX_HOME/pstack-models.md`
(default `~/.codex/pstack-models.md`). Keep the role rows and default effort in
sync with the Codex home `AGENTS.md` when the plugin adds or changes roles.
Claude Code reads its own sheet in its configuration directory.
Do not modify vendor cache files to apply these adaptations. After updating the
plugin, compare its runtime mapping with current tool schemas and remove local
adaptations that are no longer needed. Check named skill dependencies when a
playbook needs them; installation alone does not establish their availability.
