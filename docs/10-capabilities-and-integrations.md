# 10 — Provider-neutral capabilities and MCP-ready design

## Principle

The method describes **what capability is needed**, not which vendor must deliver it. For example: search documents, read a versioned document, propose tasks, create authorized tickets, inspect repository/PRs. Providers may be local files, REST APIs, or MCP tools. The MCP protocol is an integration mechanism, not the AELC source of truth.

## Proposed module separation

```text
src/aelc/capabilities/
  documents/              # document search/read contracts
  tasks/                  # work item create/read/update contracts
  source_control/         # repo / PR contracts
  communication/          # future, only if needed

src/aelc/integrations/
  mcp/                    # transport, discovery, auth context
  providers/
    atlassian/            # Confluence documents, Jira issues
    github/               # repository/PR/issues
    local/                # filesystem / local task artifacts
```

Example: onboarding reads Confluence through a `DocumentProvider`; greenfield planning proposes Jira tickets via a `TaskProvider`. Neither workflow embeds a provider-specific MCP tool name into its core logic. Use an adapter/capability registry and surface unsupported provider operations explicitly.

## Tool identity and authorization

Authentication to GitHub/Atlassian for *who the member is* is separate from the credentials/scopes used to *act on a repository or ticket*. A shared MCP technical account does not prove which human requested an operation. Attribute the AELC session independently and enforce permission boundaries in runtime/provider policy; do not rely only on prompt rules.

Read-only retrieval may be permitted by project policy; creating tickets, changing sprint scope, deleting issues, merging, and production deployment require their own authorization/approval rules. The policy is not yet finalized. Never assume any broad write access by default.

## Untrusted content and provenance

External documents, web pages, tickets, repo files, and tool outputs are data, not instructions that can override AELC security/approval rules. Record source URL/ID, version or revision, retrieval time, and relevant access context; do not treat a retrieved Confluence page as automatically current or correct.

## Release plan

**MVP v0.1** should keep future capability boundaries in mind, but need not implement Atlassian MCP, ticket automation, remote document synchronization, or a generic workflow engine. Define interfaces only when the first use case consumes them.
