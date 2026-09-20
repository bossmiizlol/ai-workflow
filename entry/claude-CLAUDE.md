# Global instructions

Applies to every project. Repository instructions win over this file for domain
rules, architecture, commands, plan format, and language.

## Goal workflow

For software-development requests that begin with `Goal:` or `/goal`, specify
`Mode: auto`, `solo`, `solo-reviewed`, or `team`, or explicitly ask for a
software team, subagents, delegation, or parallel agent work, load and follow
the user-level `goal` skill.

Use the `goal` skill as the source of truth for execution modes, delegation,
verification, and review. Default to `auto` and honor an explicit mode without
silent downgrade.

**Do not activate the workflow merely to discuss, inspect, or edit workflow
settings.** Questions about the modes, edits to `~/.claude/CLAUDE.md`,
`~/.claude/skills/`, `~/.claude/agents/`, `~/.claude/settings.json`, or a
repository's agent docs are ordinary work — answer or edit directly.

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

## Models

No fixed lead model. Use the model and reasoning effort the user selected, and
never ask the user to switch models unless their own instructions or the
project's instructions require a specific one.

The `goal` skill owns delegation roles and their routing. Check the session's
own agent list rather than assuming a role exists.

## Shared personal defaults

@{{WORKFLOW_MD}}
