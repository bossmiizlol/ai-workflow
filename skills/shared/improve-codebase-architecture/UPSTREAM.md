# Upstream provenance

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills/tree/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/skills/engineering/improve-codebase-architecture)
at commit `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d`. Installed 2026-09-20. MIT licensed; see LICENSE.
This is a pinned vendoring baseline, not an automatic-update subscription.

- Recorded upstream `SKILL.md` SHA-256: `552240a5ab5cec6b67c15dd1ad6e9f6962b1bca6ce870059a8c2713760c20392`
- Installed `SKILL.md` SHA-256: `72823497ca53a114d38283aa2692f7f11f957f68fc1b3b1bed2a75020bb8b3d6`
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
- Preserved upstream explicit-only invocation in Claude and Codex metadata; updated
  the description to match the adapted survey behavior.

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
