---
name: improve-codebase-architecture
description: Survey an existing codebase for worthwhile architecture improvements when the user requests an architecture audit or refactoring assessment; deliver an evidence-backed offline HTML report before optional discussion.
disable-model-invocation: true
---

# Improve Codebase Architecture

Find changes that concentrate useful behavior behind a smaller, stable interface.
A deep module hides substantial complexity; a shallow module makes callers manage
nearly as much complexity as its implementation. This is a survey and decision aid.
Deliver the report first. Do not refactor production code or edit repository docs,
issues, configuration, or dependencies as a side effect of the review.

## Scope and evidence

- Read applicable repository and scoped instructions before exploring. Discover the
  project's actual glossary, architecture records, contracts and test conventions;
  do not assume CONTEXT.md, an ADR directory, or a particular framework exists.
  Respect file-reading restrictions and protected/read-only documents.
- Use the area, pain point or upcoming feature the user supplied. When none is
  supplied, inspect a bounded recent Git history and prioritize recurring changes.
  History is a prioritization signal, not proof of bad design. If Git history is
  unavailable, say so and use the visible code structure and callers.
- Inspect implementations, representative callers and existing tests together.
  Trace enough of a real flow to distinguish architectural friction from naming
  preferences. Keep the scope proportional and report coverage gaps.
- Use the current tool's available search and file-reading tools. Explore directly
  by default. Delegate only when separately authorized by the user or applicable
  workflow and useful; use actual available read-only agent capabilities rather
  than assuming Claude's Agent tool or a specific agent name exists. This skill
  does not itself request delegation or activate Goal.

## Evaluate candidates

Look for behavior scattered across modules, leaking implementation details,
interfaces that force callers to coordinate internals, and missing test seams.
Small files, many layers or missing unit tests alone do not establish a problem.

Apply the deletion test: would removing or consolidating the suspected abstraction
concentrate complexity behind a simpler interface, or merely spread it among callers?
Only the former supports a deepening proposal. Preserve abstractions that isolate
real volatility, security/trust boundaries, independent ownership, or external systems.
Do not invent a second adapter or future use case to justify new infrastructure.

For each worthwhile candidate establish:

- Source evidence: precise files and line numbers, relevant callers/tests, and
  the observed friction. Separate observed facts from inferred future benefits.
- A plain-language change and before/after responsibility sketch. Leave detailed
  interface design until the candidate is chosen.
- Concrete payoff for the user's work: fewer coordinated edits, behavior testable
  through an existing public interface, or complexity hidden from actual callers.
- Costs, affected contracts, migration risks and the focused checks that would
  establish unchanged behavior after an eventual refactor. Do not invent metrics.
- Relevant prior decisions. Surface an ADR conflict only with evidence that
  revisiting it is worthwhile; explain the tradeoff without modifying the ADR.

Use the project's established domain names, including service/API terminology when
that is what the project uses. Explain unfamiliar design terms briefly. No separate
codebase-design, grilling, domain-modeling or tracker setup skill is required.

Label candidates Strong, Worth exploring or Speculative according to the evidence.
Do not fill a candidate quota. Keep weak hypotheses in a short uncertainties section.
If nothing has a demonstrated payoff, report that no worthwhile refactor was found
within the reviewed scope; do not manufacture a top recommendation.

## Deliver the report

Follow [HTML-REPORT.md](HTML-REPORT.md) for a single offline HTML report with inline
CSS and SVG. Use the user's requested output location or the host's required artifact
folder; otherwise use a unique file in the OS temporary directory. Do not write the
report into a repository by default. Include scope, revision when available and
coverage limitations, so readers can assess how current the findings are.

Check the generated report for external resource dependencies. When a browser or
renderer is available, inspect it with networking disabled for clipping, readable
labels and correctly rendered diagrams. If rendering is unavailable, perform static
checks and state explicitly that visual rendering was not verified.

Show the report using the host's file/preview tools when available and provide a
usable link. Summarize the strongest finding, or the no-refactor conclusion. If the
user requested only a report, stop. Otherwise invite them to select a candidate;
do not start an interview or implementation without their selection/instruction.

## Optional follow-up

After the user selects a candidate, use context already supplied and discuss only
unresolved constraints, responsibilities, alternatives and verification. Use the
available personal grill-me skill if the user requests a grilling interview;
ordinary discussion does not require another skill or repeated calibration.

Keep resulting decisions in the conversation/report. Edit a glossary, ADR, spec or
issue only when the user separately authorizes that deliverable, using the project's
actual conventions and existing authorization. Do not create CONTEXT.md automatically.
A candidate selection authorizes discussion, not a production refactor. When the
user asks to implement, proceed under the normal project workflow and regression
requirements; no particular issue-tracker pipeline is mandatory.
