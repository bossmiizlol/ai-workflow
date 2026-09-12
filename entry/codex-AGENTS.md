## Goal workflow

For software-development requests invoking `$goal`, beginning with `Goal:` or
`/goal`, specifying `Mode: auto`, `solo`, `solo-reviewed`, or `team`, or explicitly
requesting a software team, subagents, delegation, or parallel agent work, load
and follow the installed `$goal` skill.

Use `$goal` as the source of truth for execution modes, delegation, verification,
and review. Default to `auto` and honor explicit modes without silent downgrade.
Do not activate the workflow merely to discuss or edit workflow settings.

This is a project-independent workflow. Read applicable repository and scoped
`AGENTS.md` instructions and load relevant available project skills. Keep domain
rules, architecture, commands, and project-specific requirements in their own
repositories. No additional orchestration skill or fixed model is required by
this global configuration. Follow explicit user and applicable project model
requirements when present; otherwise use the current lead model.

## Shared personal defaults

Read `{{WORKFLOW_MD}}` for shared working agreements.
