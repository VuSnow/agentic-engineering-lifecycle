# AELC — Agentic Engineering Lifecycle

> AI accelerates engineering; humans retain understanding, judgment, ownership, and accountability.

**AELC is a proposed, harness-agnostic engineering method** for integrating AI agents into software development and maintenance. It is not a new language model or a replacement for Claude Code, Codex, Copilot, or the engineers using them.

AELC is intended to help teams deliver software faster while preserving human understanding, making AI output evidence-based, and keeping project knowledge available across members and time.

## What AELC covers

- Greenfield development, including research into alternative solutions and explicit trade-offs.
- New features in existing (brownfield) projects.
- Bug investigation and resolution in existing projects.
- Role-aware codebase understanding and onboarding.
- Cross-cutting identity, project membership, human knowledge, evidence, accountability, and external-tool integrations.

The first implementation milestone is **v0.1 Foundation: global install + project initialization**, not all four development workflows. See [MVP scope](docs/11-mvp-v0.1.md).

## Start here

- **Coding agents:** read [AGENTS.md](AGENTS.md) first.
- **Project intent:** [Charter](docs/01-project-charter.md), [Objectives](docs/02-objectives.md), and [Scope](docs/03-scope-and-use-cases.md).
- **Architecture:** [System architecture](docs/05-system-architecture.md) and [Repository structure](docs/06-repository-structure.md).
- **Installation behavior:** [Install, init, and update](docs/07-installation-and-lifecycle.md).
- **Safety and ownership:** [Human–agent contract](docs/04-principles-and-responsibility.md).
- **All documents:** [Documentation index](docs/README.md).

## Status

This documentation is the agreed **design baseline**, not a claim that the software has already been implemented. Paths and CLI examples describe intended behavior. Where the team has not selected a concrete implementation, the documents label it *proposed* or *open*.

## Source-of-truth rule

`docs/` holds canonical project design and decision context. Harness-specific files should link to these documents, not duplicate or diverge from them. Project-specific knowledge belongs to a project's own `.aelc/` directory, not this framework repository.
