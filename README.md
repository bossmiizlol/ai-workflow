# Bossmiiz

One portable source of truth for a personal Claude Code setup. Clone it on a new
machine, run one installer, and Claude Code comes up with the same working
agreements and the same generic skills as the machine you left.

## What it installs

| Repository path | Installed to | Read by |
| --- | --- | --- |
| `ai-workflow/WORKFLOW.md` | `~/.config/ai-workflow/WORKFLOW.md` | Claude Code, through the entry file |
| `ai-workflow/pstack-compatibility.md` | `~/.config/ai-workflow/pstack-compatibility.md` | Claude Code, when pstack is selected |
| `skills/shared/<name>` | `~/.agents/skills/<name>` | Claude Code, through symlinks in `~/.claude/skills/` |
| `entry/claude-CLAUDE.md` | a managed block in `~/.claude/CLAUDE.md` | Claude Code |
| `scripts/test_global_setup.py` | `~/.config/ai-workflow/test_global_setup.py` | you |

Two properties make this portable, and both are enforced by the checks:

- **One copy of every shared skill.** The eight generic skills live only in
  `~/.agents/skills`. Claude reaches them through symlinks, so a method is
  edited in exactly one place.
- **No absolute paths in the repository.** Every reference to the shared
  workflow is stored as the placeholder `{{WORKFLOW_MD}}` (its directory as
  `{{WORKFLOW_DIR}}`) and rendered to the
  destination user's real home at install time. Nothing has to be hand-edited
  when the home directory changes.

`handoff` and `improve-codebase-architecture` are explicit-invocation only:
use `/handoff` or `/improve-codebase-architecture`. Their invocation metadata is
preserved during installation.

## Install

```sh
git clone <this repository> bossmiiz && cd bossmiiz
python3 scripts/install.py --dry-run     # see exactly what would change
python3 scripts/install.py
```

The installer refuses to touch anything that already exists and differs; rerun
with `--upgrade` to back each conflicting path up under
`~/.config/ai-workflow/backups/<timestamp>/` before replacing it. Re-running on
an already-installed machine is a no-op, and merging the entry block preserves
whatever else `~/.claude/CLAUDE.md` contains.

Upgrading an older installation also retires definitions this setup no longer
ships: `--dry-run` lists them as `REMOVE`, and `--upgrade` backs each one up
before deleting it, so a stale skill or role is not left behind for Claude to offer.

Useful flags: `--home` for a relocated or test installation, and
`--workflow-dir`, `--shared-skills-dir`, `--claude-home` when a directory is not
the default.

## Verify

```sh
python3 scripts/test_global_setup.py -v                 # the installed machine
python3 scripts/test_global_setup.py --repo . -v        # …and that it matches this checkout
```

Needs Python 3.11 or later and PyYAML.

The checks are read-only and cover the shared workflow's reachability from
`~/.claude/CLAUDE.md`, unrendered placeholders, skill metadata and local links,
Claude's symlinks, explicit-only invocation, removal of retired Goal skills and
agent roles, and the vendored SHA-256 provenance digests.

**They cannot prove Claude actually loaded any of it.** Finish with a fresh
session on an unrelated project: ask it to list the instruction and
skill source paths it really loaded, confirm the shared workflow is there and
that no other project's rules leaked in, then repeat on a project that has a
same-name skill and ask which source it selected. Record the Claude Code version,
project, observed paths and result. Do not mark an unexecuted case passed.

## Move to another machine

1. Clone this repository and run the installer. That covers steps that used to
   be manual: copying skills, creating Claude's symlinks, rewriting the home
   prefix, and merging the entry file.
2. Install the Claude Code version you intend to use, then check its available
   models. Preserve intentional model choices; if a configured model is
   unavailable, report that limitation rather than silently substituting one.
3. Run both verification passes above.

Credentials, account state, project trust settings and conversation history are
deliberately not in this repository. Do not copy a whole `~/.claude` profile
between machines.

## Attribution

MIT licensed; see `LICENSE`. The shared workflow is original to this repository.
The shared skills are vendored with their own licenses and `UPSTREAM.md` provenance preserved:
`test-driven-development` from [`obra/superpowers`](https://github.com/obra/superpowers),
`diagnosing-bugs`, `handoff`, and `improve-codebase-architecture` from
[`mattpocock/skills`](https://github.com/mattpocock/skills),
and `grill-me`, `deslopify`, `junior-to-senior` and `last-20-percent` from
[`juliusBrussee/skills`](https://github.com/juliusBrussee/skills). Each carries
local adaptations documented in its own `UPSTREAM.md`; the recorded digests are
checked on every run.
