# Upstream provenance

Vendored from
[`juliusBrussee/skills`](https://github.com/juliusBrussee/skills/tree/8470b263d82579bd5b563b1e4e494472d3f0457f/skills/junior-to-senior)
at commit `8470b263d82579bd5b563b1e4e494472d3f0457f` (2026-08-07), MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

Installed on 2026-07-12. Upstream has not touched this skill since `bbce5fd`
(2026-06-11), so the baseline tree is identical at the vendoring tip `e8048f0`
and at the recorded commit above.

Local adaptations:

- `description` drops the implicit triggers ("when a plan feels hand-wavy",
  "before committing to any agent-written plan") and states that the skill is not
  invoked automatically for ordinary planning or implementation. The personal
  configuration keeps review workflows opt-in.
- Repository research reads declared versions in package manifests instead of
  lockfiles, so a project file-reading restriction is not violated to check a
  pinned API.
- The remainder is repository Prettier formatting: `*emphasis*` became
  `_emphasis_`, and a blank line follows each heading in the output-format block.
  The instruction text is otherwise unchanged.

- Recorded upstream `SKILL.md` SHA-256: `5fc658c5ff279aaa5f3b8cdd8857526d29806cf28e66f47c530a207207d9cfb6`
- Installed `SKILL.md` SHA-256: `3312777236dac7e6dd8bf60bae5ef6673a1210ee3248c545508348ac1adc9119`
- Recorded upstream `references/research-playbook.md` SHA-256: `b5e9e38a541aa73fd14527a37d08234352f2e664634946e4ecb8b0c1ae6b5c22`
- Installed `references/research-playbook.md` SHA-256: `c457aa73ff6c2c6747c17bde92e1e9019838774319242d91ca89bb468e97c389`
- Recorded upstream `references/review-rubric.md` SHA-256: `7d025c0a76a7e5fde4c6dca6b58885d74b43a5b0b054bd265cc78be5ec3c40de`
- Installed `references/review-rubric.md` SHA-256: `fd77761a91ccfa05fefc74920c292d2fa530f7bc6b682765f5d6314b2938322c`
- Copyright (c) 2026 Julius Brussee

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with this installation, preserve the local adaptations and license, and record the
new baseline and installed digests. No skills lockfile is required. Run
`~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v`
to check the installed digest and file connections; this does not check upstream freshness.
