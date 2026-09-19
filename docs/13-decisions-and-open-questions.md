# 13 — Design baseline and open questions

This file separates **agreed intent** from **implementation choices** still requiring decisions. Do not silently promote a proposal to a binding contract.

## Agreed design baseline

- AELC is Python-based, harness-agnostic, and globally installed; application projects do not need a copy of AELC source.
- `setup.sh` (macOS/Linux) and `setup.ps1` (Windows) bootstrap a common Python installer/CLI.
- Global harness entry points delegate to AELC runtime; canonical project context is not duplicated across `.claude/`, `.agents/`, and other harness directories.
- Project `.aelc/` holds shareable project configuration/knowledge; private local identity and individual evidence stay outside tracked shared project content.
- External authentication preferred; self-declared identity is an explicitly lower-trust fallback. Role/membership is project-specific.
- Agents supply evidence, disclose uncertainty/debt, and escalate risks; authorized humans/organizations accept changes and remaining risks.
- Four long-term use cases: greenfield, brownfield feature, brownfield bug fixing, and role-based onboarding; codebase understanding is their shared foundation.
- MVP v0.1 proves global install and project init before building detailed workflows, dashboards, or MCP automations.

## Proposed, not finalized

- CLI tool distribution via `uv tool`; Python 3.12+; exact dependencies, release channel, and update transport.
- Local SQLite first, shared backend later; storage backend/schema and identity assurance policy details.
- Default harness skill paths and invocation syntax; adapters must check version/OS and actual supported locations.
- Names of individual Python modules, schema file formats, project ID generation, and specific role taxonomy.
- Technique and scoring criteria for teach-back, freshness, knowledge coverage thresholds, and approval gates.

## Open decisions before relevant implementation

1. **Packaging:** keep `method/` and `harnesses/` at repository root and explicitly bundle resources, or relocate runtime templates under `src/aelc/resources/`?
2. **Identity:** what is the first supported provider flow; how do member records link across devices/organizations, and what assurance is required for each action?
3. **Project ID and membership:** how are IDs generated and roles verified; how do multiple repos map to one project?
4. **Harness scope:** which precise Claude/Codex versions and installations will v0.1 test? How will unsupported features be reported?
5. **Manifest/conflicts:** what install/update policy applies to user-edited skills and pre-existing AGENTS/CLAUDE project instructions?
6. **Update/migration:** pinned release strategy, rollback semantics, compatibility ranges, and first schema migration procedure.
7. **Evidence privacy:** retention, member consent/visibility, source access, challenge/correction, and central-storage access roles.
8. **Workflows:** detailed stage contracts and acceptance criteria must be developed one flow at a time with humans, beginning after foundation.
9. **MCP tool policies:** what Jira/Confluence actions are read-only vs approved writes, and which human role may authorize them?

## How to close a decision

Document selected option, alternatives/trade-offs, owner/decision date, impacted modules and migration needs; then update the canonical design doc and tests. Avoid calling historical chat examples hard requirements when they were illustrative.
