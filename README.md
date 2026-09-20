# Bossmiiz

One portable source of truth for a personal AI development setup that Codex and
Claude Code share. Clone it on a new machine, run one installer, and both tools
come up with the same working agreements, the same generic skills, the same Goal
workflow and the same subagent roles as the machine you left.

## What it installs

| Repository path | Installed to | Read by |
| --- | --- | --- |
| `ai-workflow/WORKFLOW.md` | `~/.config/ai-workflow/WORKFLOW.md` | both, through each entry file |
| `skills/shared/<name>` | `~/.agents/skills/<name>` | both, through symlinks in their `skills/` directories |
| `skills/goal/codex/` | `~/.codex/skills/goal/` | Codex |
| `skills/goal/claude/` | `~/.claude/skills/goal/` | Claude Code |
| `agents/codex/*.toml` | `~/.codex/agents/` | Codex |
| `agents/claude/*.md` | `~/.claude/agents/` | Claude Code |
| `entry/codex-AGENTS.md` | a managed block in `~/.codex/AGENTS.md` | Codex |
| `entry/claude-CLAUDE.md` | a managed block in `~/.claude/CLAUDE.md` | Claude Code |
| `scripts/test_global_setup.py` | `~/.config/ai-workflow/test_global_setup.py` | you |

Two properties make this portable, and both are enforced by the checks:

- **One copy of every shared skill.** The eight generic skills live only in
  `~/.agents/skills`. Both tools reach them through symlinks, so a method is
  edited in exactly one place and never drifts between the two tools.
- **No absolute paths in the repository.** Every reference to the shared
  workflow is stored as the placeholder `{{WORKFLOW_MD}}` and rendered to the
  destination user's real home at install time. Nothing has to be hand-edited
  when the home directory changes.

Tool-specific pieces stay tool-specific by design: Codex pins worker models and
reasoning effort in TOML, Claude Code declares its roles in Markdown front
matter, and each tool gets its own `goal` skill.

`handoff` and `improve-codebase-architecture` are explicit-invocation only:
use `$handoff` / `$improve-codebase-architecture` in Codex or `/handoff` /
`/improve-codebase-architecture` in Claude Code. Their invocation metadata is
preserved during installation. The Codex Goal skill also includes reference
files for delegation and final-strict review.

## Install

```sh
git clone <this repository> bossmiiz && cd bossmiiz
python3 scripts/install.py --dry-run     # see exactly what would change
python3 scripts/install.py
```

The installer refuses to touch anything that already exists and differs; rerun
with `--upgrade` to back each conflicting path up under
`~/.config/ai-workflow/backups/<timestamp>/` before replacing it. Re-running on
an already-installed machine is a no-op, and merging the entry blocks preserves
whatever else those files contain.

Upgrading an older installation also retires definitions this setup no longer
ships: `--dry-run` lists them as `REMOVE`, and `--upgrade` backs each one up
before deleting it, so a stale role is not left behind for the tool to offer.

Useful flags: `--home` for a relocated or test installation, and
`--workflow-dir`, `--shared-skills-dir`, `--codex-home`, `--claude-home` when a
tool does not use its default directory (a custom `CODEX_HOME`, for example).

## Verify

```sh
python3 scripts/test_global_setup.py -v                 # the installed machine
python3 scripts/test_global_setup.py --repo . -v        # …and that it matches this checkout
```

Needs Python 3.11 or later and PyYAML. On Python 3.10, `pip install tomli`
enables the TOML checks; without it those two checks are skipped, not failed.

The checks are read-only and cover the shared workflow's reachability from both
entry files, unrendered placeholders, skill metadata and local links, Claude's
and Codex's symlinks, Goal metadata and references, explicit-only invocation,
both tools' agent definitions, disabled shared skills,
and the vendored SHA-256 provenance digests.

**They cannot prove a tool actually loaded any of it.** Finish with a fresh
session of each tool on an unrelated project: ask it to list the instruction and
skill source paths it really loaded, confirm the shared workflow is there and
that no other project's rules leaked in, then repeat on a project that has a
same-name skill and ask which source it selected. Record the tool version,
project, observed paths and result. Do not mark an unexecuted case passed.

## Move to another machine

1. Clone this repository and run the installer. That covers steps that used to
   be manual: copying skills, creating Claude's symlinks, rewriting the home
   prefix, and merging both entry files.
2. Install the tool versions you intend to use, then check their available
   models and agent roles. Preserve intentional model choices; if a configured
   role is unavailable, report that limitation rather than silently substituting
   one.
3. Run both verification passes above.

Credentials, account state, project trust settings and conversation history are
deliberately not in this repository. Do not copy whole tool profiles between
machines.

## Attribution

MIT licensed; see `LICENSE`. The shared workflow, both Goal skills and all six
agent role definitions are original to this repository. The shared skills are
vendored with their own licenses and `UPSTREAM.md` provenance preserved:
`test-driven-development` from [`obra/superpowers`](https://github.com/obra/superpowers),
`diagnosing-bugs`, `handoff`, and `improve-codebase-architecture` from
[`mattpocock/skills`](https://github.com/mattpocock/skills),
and `grill-me`, `deslopify`, `junior-to-senior` and `last-20-percent` from
[`juliusBrussee/skills`](https://github.com/juliusBrussee/skills). Each carries
local adaptations documented in its own `UPSTREAM.md`; the recorded digests are
checked on every run.
