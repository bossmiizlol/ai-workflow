# Upstream provenance

Vendored from
[`mattpocock/skills`](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/handoff)
at commit `5beb35b040e3de97e54fa9e386d7e42d15c295c2`, MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

Installed on 2026-09-18. The current upstream baseline was reconciled on
2026-10-26; earlier local adaptations are retained.

Local adaptation on 2026-09-18: suggested skills include their source paths and
invocation syntax, with unavailable dependencies reported explicitly.
`disable-model-invocation: true` keeps the skill user-invoked only (`/handoff`).
On 2026-10-18 the setup became Claude Code only: the Codex invocation syntax and
upstream `agents/openai.yaml` were removed. On 2026-11-01 Codex support returned:
`agents/openai.yaml` is installed again with `allow_implicit_invocation: false`,
and `~/.codex/AGENTS.md` points at the shared workflow. The setup now serves both
Claude Code and Codex; `test_global_setup.py` checks both entry files.

- Recorded upstream `SKILL.md` SHA-256: `4cbb043950dad2ffd3662ff1a5a0b51ae676004b5cae10e3787e8ee7a4ee69d3`
- Installed `SKILL.md` SHA-256: `9395bcac66b3c64b6c3a83dd5be0824c71e5a93b483073fdbf85b1c13ef5b5f3`
- Copyright (c) 2026 Matt Pocock

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with this installation, and record the new baseline and installed digests. Run
`~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v`
to check the installed digest and file connections; this does not check upstream freshness.

## Upstream reconciliation — 2026-10-26

Baseline advanced to `5beb35b040e3de97e54fa9e386d7e42d15c295c2`. Only upstream SKILL.md changed
since the previous baseline. Adopted explicit OS temporary-directory resolution while preserving the local
description, suggested-skill source paths, invocation syntax and explicit-only metadata.
