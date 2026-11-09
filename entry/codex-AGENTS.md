# Global Codex instructions

<!-- BEGIN PSTACK MODEL CONFIGURATION -->
## pstack model configuration

Apply these role overrides only when pstack is explicitly selected. These are
local role assignments adapted from OpenAI guidance, checked 2026-11-04:
https://learn.chatgpt.com/docs/models#recommended-models
Use GPT-6.1 Sol for coding and analysis, Luna for bounded repeatable tooling,
and Astra for the strongest-judgment role. Panel composition is a local pstack
choice. Check the executing session's model availability before dispatch and
respect its concurrency limit. Preserve the main-chat model and effort.
`default effort: session` preserves the parent session reasoning effort.

For a delegated task limited to prose drafting or rewriting, image or screen
interpretation, or supported browser/app interaction, prefer GPT-6.1 Terra
(`gpt-6.1-terra`) when the session supports that model and the required tools.
Keep Sol for coding, analysis, and mixed judgment-and-prose tasks; keep Astra
for the most demanding judgment. This task-specific preference does not change
the role defaults or review panels below and does not authorize extra delegation
or switching the user's main-chat model. Terra requires Codex CLI 0.159.0 or later.

feature, refactoring: gpt-6.1-sol
bug-fix: gpt-6.1-sol
perf-issue: gpt-6.1-sol
hillclimb: gpt-6.1-sol
judgment and prose: gpt-6.1-sol
strongest judgment: gpt-6-astra
how explorer: gpt-6.1-sol
how explainer: gpt-6.1-sol
why investigators: gpt-6.1-sol
why synthesizer: gpt-6.1-sol
reflect tooling: gpt-6-luna
reflect judgment, divergent, synthesizer: gpt-6.1-sol
arena runners: gpt-6-astra, gpt-6.1-sol, gpt-6-luna
arena cross-judge pool: gpt-6-astra, gpt-6.1-sol, gpt-6-luna
swarm workers: gpt-6.1-sol
architect runners: gpt-6-astra, gpt-6.1-sol, gpt-6-luna
interrogate reviewers: gpt-6-astra, gpt-6.1-sol, gpt-6-luna
thermos reviewers: gpt-6.1-sol
no-comments reviewer: gpt-6.1-sol

default effort: session
<!-- END PSTACK MODEL CONFIGURATION -->

<!-- BEGIN PSTACK WORKFLOW SELECTION -->
## pstack workflow selection

Use pstack only when the user explicitly requests pstack, poteto-mode, or a named
pstack skill. Keep the selected workflow for follow-ups until the user switches.
Do not activate pstack automatically based on task size, design choices, bugs,
or performance issues. Discussing, inspecting, or editing workflow settings does
not select the workflow. Keep automatic session routing off.

When pstack is selected, read
`{{WORKFLOW_DIR}}/pstack-compatibility.md` for the local
runtime and skill-selection adaptations. Reading that supplement does not
authorize additional delegation.
<!-- END PSTACK WORKFLOW SELECTION -->

## OpenAI documentation

For OpenAI API, ChatGPT, and Codex questions or implementation work, use the OpenAI developer documentation MCP server when available to search and read current official documentation. If its tools are unavailable, use official OpenAI documentation through web search.

## Shared personal workflow

Read and follow `{{WORKFLOW_MD}}` at the start
of each session. It contains shared defaults for communication, skill selection,
testing, and browser verification and cleanup. The pstack activation rules above
still apply; reading the shared workflow does not activate pstack.

## Browser preference

Use the app's built-in browser (`iab`, `@Browser`) for interactive browsing and
manual browser verification. This Codex-specific preference takes precedence over
the shared workflow's default browser selection. Do not use Chrome, other external
browsers, or their extensions unless the user explicitly requests them.
Prefer a hidden built-in browser tab when supported; show it when visual feedback
or authentication is needed. If the built-in browser is unavailable, report the
limitation instead of silently switching to an external browser. Existing automated
headless test suites may still run as project checks. Follow the shared workflow's
cleanup rules for task-owned tabs, processes, and test artifacts.

## Codex maintenance

When updating Codex instructions, skills, or configuration, edit the active
files without creating backup copies, backup directories, or dated snapshots.
During requested cleanup, remove existing maintenance backups and confirmed
unused installation artifacts. Verify references and active process use before
deleting files; preserve credentials, conversation history, maintained checks,
and skills or runtimes still used by Codex or other tools.
This preference does not require disabling Codex's own recovery mechanisms.
