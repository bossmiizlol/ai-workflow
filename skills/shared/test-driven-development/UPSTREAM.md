# Upstream provenance

Originally vendored from
[`obra/superpowers`](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/skills/test-driven-development)
at commit `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`.
This is the recorded vendoring baseline, not a claim of latest upstream.

Local adaptations affect both metadata and instructional text: the trigger includes
refactors and behavior changes, documentation/configuration/generated output use
appropriate validation, and exception handling respects existing user authorization.
Local recovery rules preserve existing work, allow documented reproducible fallback
evidence when automation is infeasible, and distinguish that evidence from TDD.
Stricter repository TDD requirements still apply. The exception list was clarified
to avoid listing configuration and generated output as both exempt and approval-required.

- Recorded upstream `SKILL.md` SHA-256: `bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54`
- Installed `SKILL.md` SHA-256: `10c62fa841b2923d3fa04cebb55b62ef84d8c563fc007d0db8131834ebcb7b79`
- `writing-good-tests.md` SHA-256: `51471c853306ff92ca8bb41dcaea05f31c0e46b03651f8f3c99754b7172f4ae1`
- Copyright (c) 2025 Jesse Vincent
- License: MIT; see `LICENSE`.

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with the installed files, preserve and document local adaptations, and retain the
copyright and license. Recompute installed digests and run
`~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v`.
The checks verify the local installation, not upstream freshness or TDD behavior.

## Installed-content audit — 2026-09-20

Compared the installed SKILL.md with the recorded upstream commit and verified
the downloaded upstream SHA-256 before reviewing the diff. The upstream baseline
was not upgraded. This records current local adaptations, not their original
edit dates.

The body is a condensed local rewrite preserving focused failing acceptance tests before behavior changes. Pure refactors use passing regression coverage; documentation, configuration and mechanical changes use appropriate validation. Existing implementation and collaborator work are preserved. Repeatable manual evidence is distinguished from automated TDD, stricter repository requirements remain binding, and test effort scales with affected behavior and evidence.
