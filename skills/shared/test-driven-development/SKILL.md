---
name: test-driven-development
description: Guide test-first behavior changes and regression validation for refactors before production implementation.
---

# Test-driven development

Follow repository requirements and existing user authorization. For new behavior
or a bug fix, write a focused test of the acceptance criterion and run it before
implementation. Confirm the expected assertion fails because the behavior is
missing; resolve setup errors before treating the result as evidence. Implement
the smallest change, rerun the test, and preserve relevant regression coverage.

For a pure refactor, establish passing regression coverage before editing and
rerun it afterward. Add missing coverage of existing behavior first. Do not
manufacture failures for unchanged behavior.

Documentation, research, generated output, configuration-only work, and mechanical
changes without behavior changes use appropriate validation. Honor stricter
repository rules for generated code, prototypes, and other exceptions.

## Test quality

Assert observable behavior and relevant boundary cases. A test should distinguish
the expected outcome from a plausible regression. Keep test-only helpers outside
production code and understand dependency side effects before mocking them.
Read [writing good tests](writing-good-tests.md) when designing a new test strategy,
adding mocks or test utilities, or reviewing whether existing tests catch regressions.
For routine tests, follow the established local pattern.

## Evidence and recovery

If automation is infeasible, investigate the limitation and use a repeatable manual
reproduction or direct check with recorded inputs and before/after outcomes.
Report the coverage gap and any unmet repository gate. This fallback does not waive
a stricter project requirement or count as automated TDD.

If implementation already exists, preserve it and all user or collaborator work.
Add a regression test from the acceptance criteria and demonstrate it catches the
original failure in an isolated copy or by reversibly changing only your work.
Report validation performed after implementation accurately.

Run affected checks first. Expand testing for shared behavior, failures, or
unresolved risk. Fix regressions introduced by the change and report unrelated
failures. Once checks pass, rerun only after further changes or new evidence.
Report commands, results, and remaining gaps without claiming unperformed checks.
