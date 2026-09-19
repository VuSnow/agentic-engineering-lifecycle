# 06 — Proposed repository and installed layouts

The following is a **target tree**, not a command to generate every directory and placeholder in v0.1. Source code is Python. The method is principally Markdown/YAML and must be packaged as runtime-accessible resources, not assumed to live next to a user-cloned repository forever.

## Framework repository (target)

```text
aelc/
├── README.md
├── AGENTS.md
├── setup.sh                      # macOS/Linux bootstrap
├── setup.ps1                     # Windows PowerShell bootstrap
├── pyproject.toml
├── uv.lock                       # if uv locking is adopted
├── .python-version               # if pinned
├── src/
│   └── aelc/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core/                  # configuration, context, domain types
│       ├── identity/              # canonical member, provider mapping
│       ├── membership/            # project member roles and access
│       ├── sessions/              # attribution and session context
│       ├── knowledge/             # member states, freshness, coverage
│       ├── evidence/              # claim provenance and verification
│       ├── accountability/        # risk, debt, human approval
│       ├── capabilities/          # provider-neutral documents/tasks/etc.
│       ├── integrations/          # MCP / REST / local adapters
│       ├── harness/               # adapter contracts and context builder
│       ├── installer/             # detection, manifest, install/update
│       ├── storage/               # SQLite and future remote interface
│       └── cli/                   # aelc commands
├── method/
│   ├── principles/
│   ├── protocols/
│   ├── workflows/
│   │   ├── codebase_understanding/
│   │   ├── onboarding/
│   │   ├── greenfield/
│   │   ├── feature/
│   │   └── bugfix/
│   ├── roles/
│   ├── agents/
│   └── templates/
├── harnesses/
│   ├── claude_code/
│   ├── codex/
│   └── copilot/
├── templates/project/            # minimal .aelc/ templates
├── schemas/                      # versioned public data formats
├── tests/unit/
├── tests/integration/
├── docs/
└── scripts/
```

Recommended module names inside each Python domain module are `models.py`, `service.py`, `repository.py`, and provider-specific files **only as needed**. Do not generate empty modules just to match a target tree.

**Packaging decision to resolve before build:** If `method/`, `harnesses/`, and `templates/` stay at repository root, `pyproject.toml` must explicitly bundle/install them as package resources. Alternative: store runtime resources under `src/aelc/resources/` and keep human-facing docs at root. Both meet the agreed requirement; see [Open decisions](13-decisions-and-open-questions.md).

## Target project after `aelc init` (illustrative)

```text
payment-service/
├── existing-application-files...
├── .aelc/
│   ├── project.yaml              # canonical project config
│   ├── knowledge/                # shareable verified knowledge
│   ├── roles/                    # project role expectations
│   ├── policies/                 # human/team-approved constraints
│   ├── work/                     # shareable decisions/evidence references
│   └── local/                    # gitignored, if local repo state is needed
├── .claude/                      # optional: only needed harness config
└── .agents/                      # optional: only needed harness config
```

Do **not** copy `src/aelc/`, `method/`, or the whole framework source into a user's project. Do not overwrite pre-existing `AGENTS.md`, `CLAUDE.md`, `.claude/`, or other project settings. Global skills may be sufficient without creating any project harness directory.

## User machine (illustrative)

```text
USER_CONFIG_DIR/aelc/           # config + identity/session references
USER_DATA_DIR/aelc/             # SQLite/cache, if used
USER_CREDENTIAL_STORE           # access/refresh tokens; separate
HARNESS_USER_SKILL_DIR/...      # generated globally installed skills
```

Resolve platform paths with standard OS conventions and the adapter's supported harness locations; Unix `~/.config/aelc` is illustrative, not a hard-coded Windows path.

## MVP subset

Implement only the CLI, minimal installer, identity/provider interface (GitHub + explicitly lower-assurance fallback if selected), membership, session context, local storage, minimal project template, and `aelc-init` adapter(s). Extend the target tree incrementally once end-to-end behavior and tests warrant it. See [MVP](11-mvp-v0.1.md).
