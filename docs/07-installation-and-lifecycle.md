# 07 — Global installation, project initialization, updates

## Agreed user experience

A member clones the **framework** once, uses `setup.sh` on macOS/Linux or `setup.ps1` on Windows, and gains an `aelc` CLI plus chosen harness entry points. The member can then enter **any** project and invoke an `aelc-init` skill/command (or run `aelc init`) without copying framework source into that project.

Illustrative commands (not implemented merely by documenting them):

```bash
git clone <AELC_REPOSITORY_URL>
cd aelc
./setup.sh
# In an application repository:
aelc init
```

```powershell
git clone <AELC_REPOSITORY_URL>
cd aelc
.\setup.ps1
```

`<AELC_REPOSITORY_URL>` is a placeholder, not a published repository address.

## Setup scripts versus Python installer

`setup.sh` and `setup.ps1` should be **thin bootstrap wrappers**: check prerequisites, prepare an isolated Python execution environment, install the CLI/resources, then invoke the same Python installer. Avoid separate Unix and Windows business logic. Use a supported project-pinned Python version; initial design suggests Python 3.12+ and an isolated `uv tool` environment, but choose and test distribution mechanics before finalizing.

The installer detects installed harnesses, offers explicit selection, installs/updates only AELC-owned entry points, records installation manifest/version/hash, and validates installation. CLI must remain usable if a harness is absent. A user may choose one or multiple supported harnesses.

## Global versus per-project

- **Global:** CLI, method resources, harness skills/commands; one installation can serve multiple repositories.
- **Per project:** `.aelc/` configuration and shared project knowledge, plus optional minimal harness-specific settings.
- **Per member:** identity/session/cache outside versioned shared project data, with secure credential handling.

Harness invocation syntax/location is adapter-specific and **must be verified against installed harness versions**. Intended names include Claude Code `/aelc-init` and a corresponding Codex skill; do not assume every harness implements slash commands or reads the same directory on every OS/version.

## `aelc init` responsibilities

- Detect the current repository and any existing `.aelc/project.yaml`.
- Resolve an authenticated member identity when available or explicitly mark a self-declared fallback.
- Resolve the member's project membership/role (do not infer trust/role from an editable prompt alone).
- Initialize only missing, non-conflicting project configuration and local context.
- Preserve existing project state when another member initialized it. Explain what is shared versus private and never write private tokens/member knowledge into Git-tracked files.
- Initialize harness-specific context **only if needed**, without overwriting project instructions.

Initialization is **idempotent**: subsequent runs should detect and reuse existing project data without duplicating state. It must not silently import a project into an AELC backend or enable broad MCP access.

## Update model: three separate operations

1. **Framework/runtime update:** replace AELC executable and packaged method resources using a selected/pinned release source.
2. **Harness integration update:** reconcile AELC-owned skill files and manifests; if users edited a managed file, warn and resolve explicitly rather than overwrite.
3. **Project/data migration:** compare project schema and knowledge/evidence schema, preview/back up and migrate only through an explicit, safe process; a global update must not silently rewrite every repository.

Examples of intended commands: `aelc update`, `aelc doctor`, `aelc project migrate`, `aelc uninstall`. Precise flags, package feed, rollback implementation, and migration mechanism are **not yet finalized**.

## Safety invariants

- Install and init can run repeatedly without duplicate skills, member identities, or destructive file replacement.
- Update should be atomic or recoverable as practical, verify compatibility, and preserve member/project data.
- Project schemas, framework versions, and knowledge/evidence schemas are distinct; compatible ranges/pinning require a later explicit decision.
- Remove only installer-managed files during uninstall; preserve user project knowledge and individual history by default.
- Never commit secrets, token caches, or personal assessment logs; installation manifest hashes are for change detection, not proof of user authentication.
