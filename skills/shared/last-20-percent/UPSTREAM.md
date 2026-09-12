# Upstream provenance

Vendored from
[`juliusBrussee/skills`](https://github.com/juliusBrussee/skills/tree/8470b263d82579bd5b563b1e4e494472d3f0457f/skills/last-20-percent)
at commit `8470b263d82579bd5b563b1e4e494472d3f0457f` (2026-08-07), MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

Installed on 2026-07-12. Upstream has not touched this skill since `3dee1f1`
(2026-07-08), so the baseline tree is identical at the vendoring tip `e8048f0`
and at the recorded commit above.

Local adaptations:

- `description` drops the implicit triggers ("when planning any build", "before
  calling any build done", "when a solution works but feels like a demo") and
  states that the skill is not invoked automatically for ordinary builds or
  completion checks. The personal configuration keeps audit workflows opt-in.
- The remainder is repository Prettier formatting: `*emphasis*` became
  `_emphasis_`. The instruction text is otherwise unchanged.

- Recorded upstream `SKILL.md` SHA-256: `3eceb2337621e8d57598cc16951c4b08d6fdd0d658a72c00c340121780f77491`
- Installed `SKILL.md` SHA-256: `81755198c70993b480e8c6caba1ed1dc22564c9cdb1c71ff4ed11443401e64c1`
- Recorded upstream `references/last-20-catalog.md` SHA-256: `48d81c24baaf621156c21770c24416316ddfbf1139f03cf94568c4606e0c3872`
- Installed `references/last-20-catalog.md` SHA-256: `b87dd7b2a4e643bee21c64163269e0aeb6292e27508e832f9f871e6ac24d05fc`
- Copyright (c) 2026 Julius Brussee

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with this installation, preserve the local adaptations and license, and record the
new baseline and installed digests. No skills lockfile is required. Run
`~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v`
to check the installed digest and file connections; this does not check upstream freshness.
