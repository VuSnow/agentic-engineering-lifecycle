# 11 — MVP v0.1: Global install and project initialization

## Outcome

A developer clones the AELC source, runs an OS-appropriate setup script, receives a working Python CLI plus selected global harness entry points, enters an arbitrary existing application repository, and initializes that project **without copying AELC source into it**. The process respects identity, project membership, existing files, and data persistence.

## In scope

1. Python package/CLI skeleton and packaging of the minimum method/adapter resources.
2. `setup.sh` and `setup.ps1` as thin wrappers for one shared Python installer.
3. Harness detection/selection and AELC-managed `aelc-init` entry point for **Claude Code and Codex**; other adapters may follow.
4. Basic human identity abstraction: authenticate via a selected provider where implemented (initial preference GitHub), or clearly mark a self-declared fallback; `whoami`/logout as needed.
5. Project detection, project ID/config initialization, member role context, and minimal session attribution.
6. Idempotent behavior, non-destructive file writes, managed-file manifest, diagnostic checks, and automated tests on relevant OS environments.
7. Clear version/schema metadata, with compatibility checks for formats v0.1 actually writes.

## Not in scope yet

- Full greenfield, feature, bug-fix, and onboarding stage-by-stage workflows.
- Automated individual knowledge assessments, team coverage dashboard, decay scoring, and central organization identity service.
- Full human approval/legal/compliance workflow or production deployment automation.
- Atlassian MCP, Jira ticket writes, Confluence synchronization, and generic orchestration engines.
- Every adapter/platform combination, full update/migration/rollback platform, or a custom LLM harness.

Documented command names like `aelc init`, `aelc install`, `aelc doctor`, and `/aelc-init` are intended interfaces. The **exact MVP command surface and options must be specified in code/tests** rather than assumed all implemented.

## Acceptance criteria

- Setup can be run on macOS/Linux and Windows (tested on supported environments) without modifying each target project's Python environment.
- AELC CLI resolves packaged resources after the cloned framework source directory is moved or removed.
- Selected harness skill is globally available by the invocation supported by that harness version, and calls the same Python CLI.
- Running init inside an existing repo creates only minimal intended project state; app files and pre-existing harness instructions remain unchanged.
- A second init does not duplicate project/member data, overwrite custom content, or re-prompt needlessly if identity/session is still valid.
- Different human members (where authentically distinguishable) and different harnesses can reference the same project while preserving distinct member/session attribution; explicitly disclose limitations of shared accounts/OS sessions.
- No OAuth token, individual knowledge profile, or private chat transcript appears in Git-tracked project artifacts.
- Installer can identify exactly which files AELC owns and detect user edits instead of silently overwriting.
- Tests show correct behavior and failures for at least: missing harness, existing project, existing custom config, failed login, repeated install/init, and unsupported schema.

## Suggested implementation sequence (not a finalized workflow)

CLI/package/resource loading → minimal installer and one harness adapter → project init and local state → identity + role/session attribution → second harness adapter → cross-platform tests and docs. Keep each change small and demonstrably testable.
