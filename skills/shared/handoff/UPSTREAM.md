# Upstream provenance

Vendored from
[`mattpocock/skills`](https://github.com/mattpocock/skills/tree/74ca5fe077456a0b3b2f5310cf9430999fd0b5fd/skills/productivity/handoff)
at commit `74ca5fe077456a0b3b2f5310cf9430999fd0b5fd` (2026-09-17), MIT licensed;
see `LICENSE`. This is the recorded vendoring baseline, not a claim of latest upstream.

Installed on 2026-09-18. Upstream last changed this skill in `d28dfdc`
(2026-08-15), so the tree is identical at the recorded commit.

Local adaptation on 2026-09-18: suggested skills include their source paths and
the invocation syntax for Claude Code or Codex, with unavailable dependencies
reported explicitly. `agents/openai.yaml` remains byte-identical to upstream.
`disable-model-invocation: true` and `allow_implicit_invocation: false` keep the
skill user-invoked only (`/handoff` in Claude Code, `$handoff` in Codex).

- Recorded upstream `SKILL.md` SHA-256: `7c62de979fdc7ac32fb5ddb2146156c917f80ee070d30fadc9d40343c4b6ed25`
- Installed `SKILL.md` SHA-256: `415376e48fbbe55d311f09283ee65eaf42e644842a692f7a1a40e94c0a0adf62`
- Copyright (c) 2026 Matt Pocock

To update, retrieve the source at an explicitly chosen upstream commit, compare it
with this installation, and record the new baseline and installed digests. Run
`~/.config/ai-workflow/.venv/bin/python ~/.config/ai-workflow/test_global_setup.py -v`
to check the installed digest and file connections; this does not check upstream freshness.
