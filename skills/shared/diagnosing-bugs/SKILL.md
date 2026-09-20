---
name: diagnosing-bugs
description: "Diagnose unclear bugs, hard-to-reproduce failures, or performance regressions; reuse an existing reproducer when available."
---

# Diagnosing Bugs

Use this workflow for hard-to-reproduce bugs, unclear causes, and performance regressions. For an already-reproduced local failure, use the existing signal and investigate the affected path directly.

Read the current repository instructions and locate its relevant architecture or decision records. Follow that project's file-reading policy; do not assume a particular documentation filename.

## Redact

This skill has you show commands, outputs and captured artifacts. **Redact every secret first**: write `<REDACTED>` in its place. Build loops against env vars, so the credential stays in the environment rather than in what you show. Captured artifacts carry auth headers: quote only the lines that carry the signal.

If the redacted output is not enough to diagnose the bug, say so and ask the user.

## Phase 1: Build a feedback loop

**This is the skill.** Everything else is mechanical. If you have a **tight** pass/fail signal for the bug (one that goes red on _this_ bug), you will find the cause; bisection, hypothesis-testing, and instrumentation all just consume it. If you don't have one, no amount of staring at code will save you.

Reuse an existing signal when it reaches the failure. Choose a reproduction method and effort budget proportionate to the problem; report a missing signal rather than repeating an uninformative attempt indefinitely.

### Ways to construct one, in roughly this order

1. **Failing test** at whatever seam reaches the bug: unit, integration, e2e.
2. **Curl / HTTP script** against a running dev server.
3. **CLI invocation** with a fixture input, diffing stdout against a known-good snapshot.
4. **Headless browser script** (Playwright / Puppeteer) that drives the UI and asserts on DOM/console/network.
5. **Replay a captured trace.** Save a real network request / payload / event log to disk; replay it through the code path in isolation.
6. **Throwaway harness.** Spin up a minimal subset of the system (one service, mocked deps) that exercises the bug code path with a single function call.
7. **Property / fuzz loop.** If the bug is "sometimes wrong output", sample relevant inputs with a recorded seed and a bounded run/time budget. Preserve a failing input when found.
8. **Bisection harness.** If the bug appeared between two known states (commit, dataset, version), automate "boot at state X, check, repeat" so you can `git bisect run` it.
9. **Differential loop.** Run the same input through old-version vs new-version (or two configs) and diff outputs.
10. **HITL checklist.** Last resort. If a human must click, give them exact numbered actions and capture the redacted result so the loop remains repeatable.

Use the feedback loop to distinguish causes and verify the eventual fix.

### Tighten the loop

Treat the loop as a product. Once you have _a_ loop, **tighten** it:

- Can I make it faster? (Cache setup, skip unrelated init, narrow the test scope.)
- Can I make the signal sharper? (Assert on the specific symptom, not "didn't crash".)
- Can I make it more deterministic? (Pin time, seed RNG, isolate filesystem, freeze network.)

Prefer the fastest reliable check that still exercises the failure. A slower integration or E2E reproducer is valid when narrowing it would lose the bug.

### Non-deterministic bugs

Choose repetitions and a time budget from the observed failure frequency and
cost per attempt. Record the trigger, relevant conditions, attempts, failures,
and elapsed time. Use stress, concurrency, or timing controls only when they test
a concrete hypothesis in an authorized environment.

Stop the current experiment when it captures enough evidence to discriminate the
cause, reaches its run/time budget, or repeated attempts add no useful information.
Then change the experiment or report the limitation. A clean batch does not prove
an intermittent bug absent; compare before/after under comparable conditions and
report the sample size and remaining uncertainty.

### When you genuinely cannot build a loop

Report attempts and the missing evidence. Continue read-only inspection of relevant code, logs, and existing tests to form provisional hypotheses and find a reproducer. Ask for environment access or redacted artifacts only when necessary to progress. Production instrumentation requires authorization. Label unverified causes as hypotheses and do not claim a fix is verified without supporting evidence.

### Completion criterion: a tight loop that goes red

Phase 1 is done when the loop is **tight** and **red-capable**: you can name **one command** (a script path, a test invocation, a curl) that you have **already run at least once** (show the invocation and its output, redacted), and that is:

- [ ] **Red-capable**: it drives the actual bug code path and asserts the **user's exact symptom**, so it can go red on this bug and green once fixed. Not "runs without erroring"; it must be able to _catch this specific bug_.
- [ ] **Repeatable conditions**: control relevant inputs and environment; for intermittent bugs, record the observed failure rate and uncertainty.
- [ ] **Proportionate cost**: fast enough to inform the investigation within its budget; longer integration/E2E runs are acceptable when necessary.
- [ ] **Agent-runnable**: you can run it unattended; if a human is unavoidable, use a documented, repeatable checklist and capture the result.

Reading relevant code and logs is part of building the feedback loop. Use provisional hypotheses to design a discriminating check; validate them before concluding the cause. If a repeatable signal remains unavailable, report the limitation and continue independent investigation without speculative production edits.

## Phase 2: Reproduce + minimise

Run the loop. Watch it go red as the bug appears.

Confirm:

- [ ] The loop produces the failure mode the **user** described, not a different failure that happens to be nearby. Wrong bug = wrong fix.
- [ ] The evidence supports the reported failure; for intermittent bugs, record reproduction conditions and observed frequency rather than imposing a minimum rate.
- [ ] You have captured the exact symptom (error message, wrong output, slow timing) so later phases can verify the fix actually addresses it.

### Minimise

Once it's red, shrink the repro to the **smallest scenario that still goes red**. Cut inputs, callers, config, data, and steps **one at a time**, re-running the loop after each cut, and keep only what's load-bearing for the failure.

Why bother: a minimal repro shrinks the hypothesis space in Phase 3 (fewer moving parts left to suspect) and becomes the clean regression test in Phase 5.

A useful minimal reproducer isolates the cause well enough to discriminate it and protect the fix; further shrinking is optional when it no longer improves that evidence.

Minimise further when it helps distinguish causes or build regression coverage. An existing reproducer that already isolates the failure is sufficient; do not delay a supported fix to remove every incidental detail.

## Phase 3: Hypothesise

When the cause is unclear, compare plausible hypotheses and choose a check that
distinguishes them. Use as many as the evidence warrants; do not invent alternatives
to fill a quota. If a reproducer and direct evidence already point to a cause,
test that hypothesis immediately and broaden the search if it does not hold.

Each hypothesis must be **falsifiable**: state the prediction it makes.

> Format: "If <X> is the cause, then <changing Y> will make the bug disappear / <changing Z> will make it worse."

If you cannot state the prediction, the hypothesis is a vibe: discard or sharpen it.

Share material uncertainty and the next discriminating check in progress updates. Ask for domain knowledge when it changes the investigation, and continue independent checks while waiting.

## Phase 4: Instrument

Each probe must map to a specific prediction from Phase 3. **Change one variable at a time.**

Tool preference:

1. **Debugger / REPL inspection** if the env supports it. One breakpoint beats ten logs.
2. **Targeted logs** at the boundaries that distinguish hypotheses.
3. Never "log everything and grep".

**Tag every debug log** with a unique prefix, e.g. `[DEBUG-a4f2]`. Cleanup at the end becomes a single grep. Untagged logs survive; tagged logs die.

**Perf branch.** For performance regressions, logs are usually wrong. Instead: establish a baseline measurement (timing harness, `performance.now()`, profiler, query plan), then bisect. Measure first, fix second.

## Phase 5: Fix + regression test

Write the regression test **before the fix**, but only if there is a **correct seam** for it.

A correct seam is one where the test exercises the **real bug pattern** as it occurs at the call site. If the only available seam is too shallow (single-caller test when the bug needs multiple callers, unit test that can't replicate the chain that triggered the bug), a regression test there gives false confidence.

**If no correct seam exists, that itself is the finding.** Note it. The codebase architecture is preventing the bug from being locked down. Flag this for the next phase.

If a correct seam exists:

1. Turn the minimised repro into a failing test at that seam.
2. Watch it fail.
3. Apply the fix.
4. Watch it pass.
5. Re-run the Phase 1 feedback loop against the original (un-minimised) scenario.

## Phase 6: Cleanup

Required before declaring done:

- [ ] Original repro no longer reproduces (re-run the Phase 1 loop)
- [ ] Regression test passes (or absence of seam is documented)
- [ ] All `[DEBUG-...]` instrumentation removed (`grep` the prefix)
- [ ] Throwaway prototypes deleted (or moved to a clearly-marked debug location)
- [ ] The hypothesis that turned out correct is stated in the commit / PR message, so the next debugger learns
