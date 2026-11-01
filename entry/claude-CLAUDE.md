# Global instructions

Applies to every project. Repository instructions win over this file for domain
rules, architecture, commands, plan format, and language.

## Workflow selection

An explicit request to use pstack or poteto-mode selects pstack. Keep it for
follow-ups until the user switches. Merely comparing or editing workflows does
not select it.

When pstack is selected, read
`{{WORKFLOW_DIR}}/pstack-compatibility.md` alongside its
installed instructions. Use pstack only when explicitly selected; keep automatic
routing off.

**Do not activate a workflow merely to discuss, inspect, or edit workflow
settings.** Edits to `~/.claude/CLAUDE.md`, `~/.claude/skills/`,
`~/.claude/settings.json`, or a repository's agent docs are ordinary work —
answer or edit directly.

## Project independence

This configuration is project-independent. Read the applicable repository
`AGENTS.md` / `CLAUDE.md` and every scoped instruction file for the directories
in play, and load the project skills they require or that are relevant. A
project orchestration skill may add rules, and is required when repository
instructions explicitly require it, but the global workflow never depends on
one. If a project has no extra skills, infer conventions from the repository
and proceed.

Keep domain rules, architecture, commands, and project-specific requirements in
their own repositories, not here.

## Browser

For any browsing, page reading or web-app check that needs a real browser, use
Claude's own built-in browser pane (the `mcp__Claude_Browser__*` tools, loading
the `anthropic-skills:built-in-browser` skill first). Never use Claude in Chrome
(`mcp__claude-in-chrome__*`) and never open or control the user's Chrome or any
other external browser; this user does not use Claude through Chrome, and the
Chrome integration is turned off on purpose. When the built-in browser is not
available in the session (a terminal without the desktop app), say so, then use
WebFetch for plain page content or a headless isolated browser session as
WORKFLOW.md describes. Orca's embedded browser applies only when the task runs
inside Orca through the orca-cli skill.

## Models

No fixed lead model. Use the model and reasoning effort the user selected, and
never ask the user to switch models unless their own instructions or the
project's instructions require a specific one. Check the session's own agent
list rather than assuming a role exists.

## Shared personal defaults

@{{WORKFLOW_MD}}
