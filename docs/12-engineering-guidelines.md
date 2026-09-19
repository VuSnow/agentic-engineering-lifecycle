# 12 — Engineering guidelines for building AELC

## Python implementation

Use a conventional `src/aelc/` Python package, typed public interfaces, clear domain/service/storage boundaries, and small modules. The design discussion favored Python 3.12+, an isolated CLI install with `uv`, and tools such as pytest/Ruff; final dependency and supported-OS versions must be pinned/tested when code is created.

- Keep harness skills/commands thin; business rules belong in tested Python runtime/services.
- Model identity authentication separately from provider API authorization; avoid placing tokens in project files.
- Separate **framework source layout** from the **installed package resource layout**. Add a packaging test that removes/moves the source checkout and still loads packaged method/skill templates.
- Use dependency injection or simple provider interfaces where there are concrete consumers. Avoid speculative abstraction trees and empty files.
- Treat all file writes as potentially destructive. Detect pre-existing state, record managed paths/hashes, and provide deliberate conflict resolution.
- Fail closed for unknown identity assurance, high-risk tool writes, incompatible schema, and unsupported harness capability rather than claiming success.
- Emit actionable errors; never log secrets, private transcripts, or full OAuth credentials.
- Honor target project instructions as project context while preserving system/security boundaries; untrusted content cannot grant authorization.

## Test expectations

- Unit tests: member mapping, role resolution, version/format validation, manifest diffing, path handling, repeatable init.
- Integration tests: CLI entry points, packaged resources, harness skill path generation, setup behavior, existing-project conflict handling.
- Security-focused tests: untrusted text cannot forge approval, self-declared identity stays lower assurance, sensitive local files do not enter tracked project state.
- Cross-platform tests: Windows path/PowerShell behavior and at least one Unix-family environment for setup/bootstrap.

## Change reporting contract for coding agents

Every implementation response should state **what changed**, **what was tested and actual results**, **what was not tested**, **known limitations/uncertainty**, and **new or accepted technical debt**. A passing unit test does not authorize merge or production deployment. Never synthesize human approval.

## Documentation maintenance

Update the relevant design/CLI docs when implementation choices change. Record a deliberate new decision in [Decisions and open questions](13-decisions-and-open-questions.md), and avoid making separate Claude/Codex copies of canonical architecture text. If a future workflow conflicts with the charter, ask for a human design decision rather than silently changing the principle.
