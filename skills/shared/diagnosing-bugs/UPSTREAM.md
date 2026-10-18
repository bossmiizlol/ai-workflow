# Upstream provenance

Current upstream baseline
[`mattpocock/skills`](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/diagnosing-bugs)
at commit `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d` (2026-10-05), MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

The personal installation replaces the repository-specific documentation instruction
with discovery of the current project's instructions and architecture or decision
records. It does not require `CONTEXT.md`, `AGENTS.md`, or `SPEC.md` to exist.
The six diagnosis phases are retained.

- Recorded upstream `SKILL.md` SHA-256: `9168404abda0967a5d32977e3498cd95fda6807018852f3de736a78357c82b40`
- Installed `SKILL.md` SHA-256: `30457f7802a155e1bb56d8f895037b6349c8042884ec40eff198fe1829274f9b`

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

## Upstream reconciliation — 2026-10-06

Baseline advanced to `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d`. Compared all files in
the upstream skill directory; SKILL.md is the only changed upstream file.
Supporting resources and licenses are retained.

Upstream now names GLOSSARY.md instead of CONTEXT.md. The installed skill explicitly
includes the project domain glossary while retaining discovery of actual project
documents, file-reading restrictions, and the existing diagnosis adaptations.

## Claude Code only — 2026-10-18

Upstream `agents/openai.yaml` (Codex metadata) was removed when the setup became
Claude Code only. Other supporting resources and the license are retained.
