# 04 — Human–agent operating principles

## Productivity and understanding

AELC must avoid both extremes:

- **Human → agent → approve without understanding:** faster outputs may create cognitive dependency and hidden risks.
- **Human fully investigates → agent repeats work:** little productivity gain.

Preferred principle: **agents perform expensive investigation and guide the member; the member explains back the material mental model; the agent checks understanding and identifies gaps**. A challenge should target reasoning and failure modes rather than rote recall. Depth must match risk and the person's relevant knowledge. This is a principle, **not a finalized stage-by-stage workflow**.

## Agent responsibility: observable duties

Agent output must distinguish:

- **Observed/verified:** backed by identifiable source, command output, test result, or other relevant evidence.
- **Inferred:** a reasoned interpretation, with its assumptions and supporting/contradicting information.
- **Unknown/unverified:** explicitly surfaced for further checks or a human decision.

For material outputs, report what changed, why, assumptions, plausible alternatives and trade-offs where relevant, tests/checks actually run, tests/checks not run, residual risk, security/operational implications, and known technical debt. Escalate high-impact uncertainty; do not fabricate tool runs, citations, approvals, or guaranteed correctness.

“AI responsibility” means **required behavior and evidence within the method**; an AI agent is not a legal or organizational person accountable in place of a human/team.

## Human and organizational accountability

The authorized human/team decides whether remaining risk is acceptable and whether a change may merge/deploy under project policy. Accountability for production changes and any legal obligations follows actual organizational authority and applicable law; AELC cannot assign legal liability to an individual just by recording an approval.

Acceptance must not be inferred from an LLM-generated statement (“Alice approved”), a self-edited file, or a commit alone. Require a trustworthy human approval event for actions governed by approval policy. Knowledge is not permission: a member can understand a system without having deployment rights.

## Verification and technical debt

Human verification does not mean redoing every AI action. Review source evidence and independently inspect/verify areas where impact, uncertainty, or missing evidence warrants it. CI passing is evidence, not blanket proof of correctness. Unresolved debt should have description, reason, impact, owner/team, and a condition or plan for revisiting it if accepted.

## Short principles

> No unsupported AI claims. No unowned production changes. AI must justify; humans must own.

See [Knowledge and evidence](09-knowledge-and-evidence.md) for the difference between work activity and demonstrated member understanding.
