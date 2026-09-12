# Upstream provenance

Vendored from
[`juliusBrussee/skills`](https://github.com/juliusBrussee/skills/tree/8470b263d82579bd5b563b1e4e494472d3f0457f/skills/grill-me)
at commit `8470b263d82579bd5b563b1e4e494472d3f0457f` (2026-08-07), MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

Installed on 2026-07-12. Upstream has not touched this skill since `7861899`
(2026-06-08), so the baseline tree is identical at the vendoring tip `e8048f0`
and at the recorded commit above.

Local adaptations add document-backed review, which upstream does not have:

- `description` gains the sentence directing document-backed review to the
  domain reference.
- `SKILL.md` gains a `## Document-backed review` section above `## Core Rules`,
  linking that reference. The calibration and question loop is unchanged.
- `references/domain-review.md` is local, not vendored. It is written to be
  project-independent: it locates whatever domain definitions, contracts and
  decision records the current project keeps, rather than assuming a filename,
  and it respects read-only files.

- Recorded upstream `SKILL.md` SHA-256: `fb51ed1c9ade960e75ce781c4da411939c24a61a06d21c04060ee0e7660e673b`
- Installed `SKILL.md` SHA-256: `28e97f1e30be0b98d2899be0e9a56d2f479be4128c07a7c7d29b744df2987d4a`
- Installed `references/domain-review.md` SHA-256 (local, no upstream counterpart): `d817207186893e0ddd4557f1944b048003a3bb6e1c9c066ef1fee3f444bb594f`
- Copyright (c) 2026 Julius Brussee

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with this installation, preserve the local adaptations, the local reference and the
license, and record the new baseline and installed digests. No skills lockfile is
required. Run
`~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v`
to check the installed digest and file connections; this does not check upstream freshness.
