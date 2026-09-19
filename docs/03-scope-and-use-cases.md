# 03 — Scope and primary use cases

## Supported scenarios (product intent)

| Scenario | Expected value | Human responsibility |
|---|---|---|
| **Greenfield development** | Assist across SDLC; research several viable solutions to a problem, check up-to-date framework/docs where available, compare assumptions, costs and trade-offs; support implementation and maintenance. | Choose requirements, architecture, risk, and accepted changes; understand important trade-offs. |
| **Brownfield feature** | Explore existing code and constraints, analyze impact, implement/test a new behavior, surface regressions and debt. | Ensure the behavior fits business intent and surrounding system; review material changes and risk. |
| **Brownfield bug fix** | Trace code/logs, reproduce when possible, propose root cause and fix, run available tests, report uncertainty. | Retain a working mental model of cause, failure conditions, fix and remaining risks; authorize accepted change. |
| **Role-based onboarding** | Adapt project discovery for AI Engineer, Backend Engineer, Tech Lead, BA, QA, etc.; shorten time to useful contribution and reduce repeated senior explanations. | Demonstrate understanding through scoped teach-back, scenarios, and real project work; seniors calibrate where necessary. |

**Codebase understanding** is a reusable capability underneath onboarding, feature work, and bug fixing. Do not conflate it with onboarding: onboarding selects a role-relevant slice and creates evidence of a member's understanding.

## Cross-cutting concerns

Human identity/project membership; agent activity attribution; shared project knowledge; per-member knowledge evidence; risk-based verification; accountability; technical debt; installation and versioning; integrations for documents, tickets, source control, and other tools.

## Deliberately not specified yet

No detailed stage-by-stage workflows, exact question banks, architecture selection rubric, mandatory approval matrix, knowledge score, or production automation policy has been agreed. Develop each workflow separately with explicit user/team decisions; do not invent one from this overview.

## First vertical slice

Begin with **global installation + project initialization**; later exercise identity, role, project context, teach-back, and evidence via codebase understanding/onboarding. This order is a proposed delivery approach, not a requirement to build all future architecture in v0.1.
