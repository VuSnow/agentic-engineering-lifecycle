# 01 — Project charter

## Definition

**AELC (Agentic Engineering Lifecycle)** is a harness-agnostic engineering method for bringing AI agents into the software development lifecycle while retaining human understanding, judgment, ownership, and accountability. It combines method definitions, a Python runtime, a global installer, and thin adapters to third-party agent harnesses.

AELC is **not** an AI model, an agent harness built from scratch, an employee performance scoring product, or an automatic license to merge AI-produced code. Existing harnesses perform agent work; AELC governs context, responsibility, verification, knowledge, and project integration.

## Central promise

> Minimize duplicated work while maximizing retained understanding.

Agents should do time-consuming exploration, research, tracing, implementation assistance, and verification where technically possible. Humans must still understand enough of the material change to challenge conclusions, assess trade-offs, and own accepted system risk. Human verification does **not** mean routinely repeating all agent work.

## Beneficiaries

- Engineers: faster exploration and implementation without passive acceptance of outputs.
- New project members: role-aware onboarding and a demonstrable project mental model.
- Tech leads/seniors: less repetitive basic explanation/review and visibility into knowledge concentration.
- Teams/organizations: lower dependence on one or two knowledge holders and auditable change ownership.

## Product shape

One **global** AELC installation can support many projects and multiple agent harnesses. The project stores only project-specific shared context/configuration and optional harness integration; private member identity/session state is separate. AELC methods and resources are updated centrally, with project-schema migrations kept separate.

## Outcomes, not promises of automation

Success means faster useful engineering work, richer exploration of solution alternatives, retained human understanding, traceable evidence, explicit risk/debt decisions, and more resilient team knowledge distribution. It does not mean all work is fully autonomous or that all AI errors can be eliminated.

See [Objectives](02-objectives.md) and [MVP scope](11-mvp-v0.1.md) for what is expected eventually versus first.
