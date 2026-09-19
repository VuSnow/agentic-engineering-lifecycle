# 05 — System architecture and ownership boundaries

## Conceptual layers

```text
AELC Method (principles, protocols, workflows, role definitions)
           |
AELC Python Runtime / CLI (identity, membership, sessions,
                           evidence, knowledge, accountability,
                           capabilities, installer)
           |
Harness adapters (Claude Code / Codex / Copilot / future harnesses)
           |
Existing agent harnesses + external systems (MCP, REST, local files)
```

This is an **ownership model**, not a requirement that all modules be implemented for v0.1. The adapters are thin entry points into the same runtime/method. Avoid a second implementation of identity or knowledge inside each skill.

## Storage/ownership boundaries

| Location | Canonical responsibility | Git policy |
|---|---|---|
| **AELC framework package** | Python runtime, shared method definitions, adapter resources and templates | Framework source repository |
| **Target project's `.aelc/`** | Project ID, shared policies, verified project knowledge, architectural decisions and shareable work artifacts | Commit reviewed, non-sensitive shared material only |
| **Harness-specific target config** | Per-harness pointers/instructions/settings needed for integration | May be global or project-local; never a competing project source of truth |
| **User-local AELC config/cache** | Active identity reference, selected project and local session/cache | Keep out of project Git; protect credentials separately |
| **Shared AELC backend (future)** | Member mapping across devices, controlled-access evidence, individual knowledge and team coverage, trustworthy approval records | Access-controlled service, not files in a shared repo |
| **GitHub/Jira/Confluence/etc.** | Their own authoritative repos/tickets/docs | Store references/version/provenance rather than pretending AELC owns the original objects |

**Important:** `.aelc/` is a proposed canonical *project* directory, not a location for all personal data. A self-declared name in a local file is not an authentication mechanism. Git commits are not a substitute for authenticated approvals.

## Dependency boundaries

- `identity/` authenticates/maps a member; `membership/` binds that member to a project and role; a role is not a global human identity field.
- `sessions/` attributes interactions to human, harness account, agent, and task with stated assurance/limitations.
- `evidence/` stores claims and verifiable provenance; `knowledge/` assesses demonstrated understanding based on evidence; neither should silently overwrite the other.
- `accountability/` records risk/debt/approval decisions with enforceable permissions where needed.
- `capabilities/` defines provider-neutral document/task/source-control interfaces; `integrations/` implements adapters such as MCP/REST/local.
- No agent may gain privileges by editing project documents or prompt text.

## Portability rule

A member must be able to use Claude Code for one session and Codex for another without producing two independent canonical project states or member identities. Harness-supported features may vary; adapters must report unsupported operations rather than silently claiming parity.
