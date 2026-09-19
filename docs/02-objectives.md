# 02 — AELC objectives

The following are **agreed target outcomes**, not a claim that implementation or numerical targets have been finalized. Measurement design remains open.

## Delivery and decisions

1. **Increase engineering productivity:** let agents carry expensive repository exploration, code search, tracing, research, test assistance, and repetitive execution; do not require full human redo.
2. **Expand the solution space at lower research cost:** for one problem, let agents research multiple viable architectures/libraries/patterns, current documentation and compatibility, assumptions, proof-of-concept evidence, and trade-offs. Humans decide; do not repeatedly apply a familiar framework/pattern without checking whether it still fits.
3. **Support four lifecycle scenarios:** greenfield development, brownfield feature work, brownfield bug fixes, and role-aware onboarding built on codebase understanding.

## Human capability and responsibility

4. **Preserve mental models:** maintain enough understanding to explain material behavior, failure modes, impacts, and trade-offs.
5. **Limit cognitive dependency:** use scoped teach-back and targeted challenges rather than passive approval or mandatory reproduction of all agent exploration.
6. **Make AI responsibility explicit:** every material AI claim has traceable evidence or is marked as an assumption/inference/unknown; disclose validation actually run, limitations, and uncertainty requiring human review.
7. **Preserve human/organizational accountability:** human-authorized change and risk acceptance remain human/organizational responsibilities; actual legal liability depends on applicable law, role, and contractual context, not a framework declaration.
8. **Make technical debt explicit:** surface workarounds, duplication, coupling, limitations, follow-up work, and the accountable decision to accept or reject residual debt.
9. **Adapt verification to risk:** depth depends on criticality, complexity, novelty, blast radius, security/business impact, uncertainty, and knowledge gap.

## Knowledge and team resilience

10. **Treat project knowledge as a first-class asset:** record and maintain shared domain/architecture/operations/decision context.
11. **Maintain individual knowledge state:** distinguish what each member actually demonstrates from what their role is expected to know.
12. **Detect knowledge staleness:** earlier competence or documentation can become outdated after code/design changes.
13. **Map team knowledge coverage:** identify single-person dependencies, gaps, and critical subsystems with insufficient coverage.
14. **Reduce senior training and routine review bottlenecks:** agent-guided discovery and pre-review checks should let seniors focus on high-risk design, mentoring, and judgment; do not eliminate human review.
15. **Shorten role-aware onboarding:** help new members reach demonstrable working understanding, not simply read generated summaries.
16. **Reduce organizational knowledge concentration:** preserve rationale, business rules, known failure modes, and context when senior engineers, tech leads, PMs, or other key members leave.
17. **Separate knowledge assessment from performance assessment:** no employee rankings or general competence scores based on knowledge-map status.
18. **Provide role-aware assistance:** adapt scope, explanations, and challenge depth to the member's project role and demonstrated knowledge, without withholding essential information.

## Trust and extensibility

19. **Maintain reliable human identity and attribution:** distinguish human member, harness/platform account, and acting agent even with shared harness accounts.
20. **Prefer verified identity:** company SSO or project-used providers such as GitHub/Atlassian when available; self-declared fallback is explicitly lower assurance.
21. **Preserve evidence provenance:** source, timestamp/version, actor/session, actual verification, approval origin, and uncertainty must be traceable.
22. **Stay harness- and provider-agnostic:** method logic survives changes in Claude Code, Codex, Copilot, MCP servers, and ticket/document providers.
23. **Make installation/update safe:** install once, use across projects, update centrally, never silently overwrite project/user data or approvals.

## Non-goals

AELC is not intended to replace engineers or seniors, guarantee correctness, make agent-authored claims authoritative, turn knowledge tracking into surveillance/performance ranking, duplicate all external systems as a new source of truth, or require every project to carry a copy of framework source.
