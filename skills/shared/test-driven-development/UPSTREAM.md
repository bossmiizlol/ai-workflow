# Upstream provenance

Current upstream baseline
[`obra/superpowers`](https://github.com/obra/superpowers/tree/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/test-driven-development)
at commit `8ca22dba9a94f28898bbce59f2537ff4d87c747d`.
This is the recorded vendoring baseline, not a claim of latest upstream.

Local adaptations affect both metadata and instructional text: the trigger includes
refactors and behavior changes, documentation/configuration/generated output use
appropriate validation, and exception handling respects existing user authorization.
Local recovery rules preserve existing work, allow documented reproducible fallback
evidence when automation is infeasible, and distinguish that evidence from TDD.
Stricter repository TDD requirements still apply. The exception list was clarified
to avoid listing configuration and generated output as both exempt and approval-required.

- Recorded upstream `SKILL.md` SHA-256: `64b03fce4aee5a97a93160cea8111f3ba13a17b7c001db4bd5836d67fd10705d`
- Installed `SKILL.md` SHA-256: `078e11ee988249190e6833ebd494c7ae7c38fd8c27b584f5a86cf1b4092f07c3`
- `writing-good-tests.md` SHA-256: `51471c853306ff92ca8bb41dcaea05f31c0e46b03651f8f3c99754b7172f4ae1`
- Copyright (c) 2025 Jesse Vincent
- License: MIT; see `LICENSE`.

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with the installed files, preserve and document local adaptations, and retain the
copyright and license. Recompute installed digests and run
`python3 ~/.config/ai-workflow/test_global_setup.py -v`.
The checks verify the local installation, not upstream freshness or TDD behavior.

## Installed-content audit — 2026-09-20

Compared the installed SKILL.md with the recorded upstream commit and verified
the downloaded upstream SHA-256 before reviewing the diff. The upstream baseline
was not upgraded. This records current local adaptations, not their original
edit dates.

The body is a condensed local rewrite preserving focused failing acceptance tests before behavior changes. Pure refactors use passing regression coverage; documentation, configuration and mechanical changes use appropriate validation. Existing implementation and collaborator work are preserved. Repeatable manual evidence is distinguished from automated TDD, stricter repository requirements remain binding, and test effort scales with affected behavior and evidence.

## Upstream reconciliation — 2026-10-06

Baseline advanced to `8ca22dba9a94f28898bbce59f2537ff4d87c747d`. Compared all files in
the upstream skill directory; SKILL.md is the only changed upstream file.
Supporting resources and licenses are retained.

Upstream added a requirement to run the whole project test suite and name every
observed failure. The personal adaptation requires the project completion gates,
distinguishes focused checks from a passing full suite, and explicitly reports
blocked suites and all observed failures. It retains risk-based expansion where
the project does not require a full suite; unconditional full-suite execution
is not adopted. Existing work preservation and documentation-only validation
remain in force.
