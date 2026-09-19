# 09 — Knowledge model, evidence, and team coverage

## Three different knowledge layers

1. **Project knowledge:** shared domain rules, architecture, codebase maps, operational lessons, decision rationale; reviewed/versioned as appropriate.
2. **Role expectations:** which parts of the system a role needs to understand and to what depth.
3. **Individual knowledge:** demonstrated understanding of specific project areas by a specific member; two people with the same role need not have the same state.

A generic skill checklist (“knows Kafka”) is insufficient. The relevant question is how *this project* uses Kafka, how it retries, how it can fail, and why design choices were made.

## Knowledge dimensions

Suggested understanding levels: **Unknown**, **Aware**, **Working**, **Deep**. **Stale is a separate freshness/status dimension**, not a level above Deep. A member can have “Deep, revalidation required” after a subsystem redesign. The exact assessment rubric and decay algorithm are open decisions.

- **Aware:** knows the component/purpose and can locate relevant information.
- **Working:** can contribute safely to the area under normal review.
- **Deep:** can reason through key design choices, trade-offs, and failure modes and review others' work in that area.

## Evidence is not activity count

“Member asked an agent to implement ten payment tickets” is evidence of activity, **not automatic proof of Payment Deep knowledge**. Understanding evidence could include a member's own teach-back, scenario reasoning, correct tracing, independent diagnosis, explanation of failure paths, or reviewed changes with identifiable human contribution.

An agent can propose an assessment and cite evidence; the member/authorized lead must be able to inspect, correct, contest, and calibrate it. Do not generate person-to-person rankings, generic performance scores, or surveillance reports.

## Teach-back without productivity loss

Agents may investigate, trace, research, and guide first. Ask the member to reconstruct the *material mental model*, then challenge gaps with a focused scenario. A small low-risk task may need little/no formal teach-back; a high-risk architectural or production change can require deeper review. Do not demand that a member reproduce all agent commands and searches.

## Evidence provenance (conceptual fields)

```text
claim + scope + status (observed/inferred/unverified)
source reference + version/commit + retrieved/observed at
human/agent/session + identity assurance
verification method + actual result + limitations
knowledge assertion supported (if applicable)
review/calibration/approval actor and time (if required)
```

A generated summary or successful CI run is **not** proof of an individual's understanding. An external Confluence page can be outdated; reference original versions and flag downstream shared knowledge as potentially stale when the source/code changes.

## Team coverage

Tech leads need an individual view (“what can this member safely work on?”) and a team view (“where is critical knowledge concentrated?”). Coverage targets might require more than one member with demonstrated working knowledge of a critical subsystem, but **specific thresholds are a project policy decision**, not a universal default.

## Privacy/access

Keep individual evidence and session content under suitable access control, with retention and contestability policies decided before centralizing them. Do not commit personal profiles, raw private agent conversations, secrets, or unverifiable approvals into shared project Git. Verified shared project knowledge can be committed when approved for that audience.

## Delivery status

This file defines intended semantics. Full assessment, decay, team dashboard, and shared backend are **beyond MVP v0.1**.
