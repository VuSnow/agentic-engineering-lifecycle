# 08 — Human identity, project membership, session attribution

## Identity boundaries

- **Human identity:** canonical AELC `member_id` for an actual member.
- **Platform identity:** account used for Claude Code, Codex, Copilot, or another provider; may be shared.
- **Agent identity:** the acting agent/sub-agent or tool execution identity.

A shared harness account does **not** establish who the human operator is. Any knowledge or accountability attribution must retain the actual session's assurance limitations.

## External authentication and canonical mapping

Prefer organization-controlled authentication (for example company SSO when available) or a project-used provider (GitHub/Atlassian) over user-entered identity. After a valid authentication flow, link a stable **provider subject ID plus provider/tenant context** to an internal canonical member ID. Usernames, display names, and email are mutable and must not be the sole database key.

One member may link several authenticated external identities. Linking, unlinking, and switching identities must require explicit authenticated action; **never silently change a member by editing a JSON file**. OAuth provider scopes should be minimized; authentication identity must be distinct from the permissions used to read/write Jira, GitHub, etc.

A self-declared fallback can support prototypes or unaffiliated teams but must be visibly labeled **unverified/lower assurance**; its activity must not masquerade as a strong authentication record.

## Global identity versus project membership

Canonical member ID answers **who is this human?** Membership answers **who are they in this project?** One person may be backend engineer in project A and AI engineer or team lead in project B. Role changes do not recreate identity or erase knowledge history. Knowledge level does not imply permission or seniority.

## Local state is not proof of identity

An illustrative local cache may include `member_id`, provider reference, and assurance status. Such a file is a cache/reference, **not independently trustworthy authentication evidence**. Use short-lived authenticated sessions, re-authentication where needed, and platform-secure credential storage. Shared OS users, copied caches, compromised accounts, and shared provider tokens still pose impersonation risk; external login *reduces* risk but does not eliminate it.

## Attribution record (conceptual)

```text
human_member_id
identity_provider_subject_ref + assurance
project_id + project_role(s)
aelc_session_id
harness_name + platform_account_ref
agent_id + work_item_ref
activity_timestamp + evidence_refs
```

Identity, role, tool authorization, and human approval are distinct facts. An LLM must never be permitted to create a trusted human approval by generating text or modifying a local file.

## MVP boundary

Provide a small provider interface, local canonical member reference, login/`whoami`/logout where implemented, project membership context, and traceable session attribution. An enterprise SSO service, cross-machine identity reconciliation, central access control, and robust approval auditing can follow later, but do not falsely claim their guarantees in the MVP.
