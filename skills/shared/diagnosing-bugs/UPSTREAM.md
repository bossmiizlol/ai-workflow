# Upstream provenance

Originally vendored from
[`mattpocock/skills`](https://github.com/mattpocock/skills/tree/321658273cb1d20b76026717d027d505790106d4/skills/engineering/diagnosing-bugs)
at commit `321658273cb1d20b76026717d027d505790106d4` (2026-08-19), MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

The personal installation replaces the repository-specific documentation instruction
with discovery of the current project's instructions and architecture or decision
records. It does not require `CONTEXT.md`, `AGENTS.md`, or `SPEC.md` to exist.
The six diagnosis phases are retained.

- Recorded upstream `SKILL.md` SHA-256: `77f3cf31bc99b2f49af943222526531fcc9fc41d047626d3640e875e85af3e84`
- Installed `SKILL.md` SHA-256: `d627d2cb4fad750677aae3c98061064fa221535e0129733e054fd9a51a278e24`

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with this installation, preserve the local adaptation and license, and record the
new baseline and installed digest. No repository Git alias or skills lockfile is
required. Run `~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v` to check the
installed digest and file connections; this does not check upstream freshness.

## Installed-content audit — 2026-09-20

Compared the installed SKILL.md with the recorded upstream commit and verified
the downloaded upstream SHA-256 before reviewing the diff. The upstream baseline
was not upgraded. This records current local adaptations, not their original
edit dates.

The trigger is narrowed to unclear causes, hard-to-reproduce bugs and performance regressions. Existing reproducers are reused; experiment cost and repetitions are bounded by the evidence. Read-only hypothesis formation remains possible without a reproducer, uncertainty is explicit, and minimization and hypothesis counts are proportional. A repeatable human checklist can replace the bundled HITL script. Repository document discovery is generic; the six diagnosis phases remain.
