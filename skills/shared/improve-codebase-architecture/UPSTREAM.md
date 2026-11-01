# Upstream provenance

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills/tree/4ae2317/skills/engineering/improve-codebase-architecture)
at commit `4ae2317` (2026-10-31). Installed 2026-09-20. MIT licensed; see LICENSE.
This is a pinned vendoring baseline, not an automatic-update subscription.

- Recorded upstream `SKILL.md` SHA-256: `35b03a3db61e0f5aa333ea59b54963e45a3d2ace6649b2ef4f9576603e2582a6`
- Installed `SKILL.md` SHA-256: `34f54645bca300d35cc882a8b91fcbd4eb2136ea5cf028a0c9f1ad4e8c123b77`
- Installed `HTML-REPORT.md` SHA-256: `ca17b187f2052940061575b9b589c0aa733458fa172e574ee03d0ebeca1e3589`

Local adaptations:

- Report-first survey with optional discussion after candidate selection; no
  automatic production, domain-document or issue-tracker changes.
- Repository-specific document discovery, file restrictions and established vocabulary.
- Tool-neutral exploration without mandatory agents or external skill dependencies.
- Evidence, tradeoffs, regression criteria and a legitimate no-refactor outcome.
- Offline inline CSS/SVG report, escaped source content, responsive accessibility
  and explicit static/visual verification boundaries.
- Output location follows user/host requirements, otherwise the OS temporary directory.
- Preserved upstream explicit-only invocation in Claude metadata; updated the
  description to match the adapted survey behavior. Upstream `agents/openai.yaml`
  (Codex metadata) was removed on 2026-10-18 when the setup became Claude Code only,
  and reinstated on 2026-11-01 with `allow_implicit_invocation: false` when Codex
  support returned alongside `~/.codex/AGENTS.md`.

For updates, choose an upstream commit, review its changes against these adaptations,
retain the license and record new digests. Run the global setup validator and the
skill-creator validator; neither alone proves behavior in a fresh agent session.

## Upstream reconciliation — 2026-10-06

Baseline advanced to `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d`. Compared all files in
the upstream skill directory; SKILL.md is the only changed upstream file.
Supporting resources and licenses are retained.

Upstream changed its domain-document references from CONTEXT.md to GLOSSARY.md.
The installed skill continues to discover the actual project glossary and now
states the filename-independent rule without singling out an old filename.
The report-first workflow and explicit-only invocation remain unchanged.

## Upstream reconciliation — 2026-11-01

Baseline advanced from `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d` to `4ae2317`
(upstream HEAD, 2026-10-31). Compared all files in the upstream skill directory;
SKILL.md is the only changed file, in one line (commit `7739eae`, 2026-10-29):
the exploration sub-agent must start with a fresh context window, not a fork.
Adopted as a rule for the optional, separately authorized delegate: start it with
a fresh context window so it does not inherit this conversation's conclusions.
Direct exploration by default, report-first output and explicit-only invocation
are unchanged.
