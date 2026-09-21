---
name: aelc-init
description: Initialize AELC in the current software project when explicity requested by the user.
---

# AELC Project Initialization

You are invoking the AELC (Agentic Engineering Lifecycle) project initialization skill.

## Objective

Initialize AELC in the current software project by using the installed AELC Python CLI

## Instructions

1. Identify the current project directory.

2. Check whether the AELC CLI is available: `aelc --version`

3. If the CLI is unavailable, stop and explain that AELC must be installed before initialization.

4. Run the following command from the intended project directory: `aelc init`

5. Verify the initialization result: `aelc doctor`

6. Report the actual command results to the user.

## Safety rules

- Do **NOT** implement project initialization manually.
- Do **NOT** create or modify project files outside the AELC CLI initialization procedure.
- Do **NOT** overwrite existing project configuration.
- Do **NOT** modify AGENTS.md or CLAUDE.md.
- Do **NOT** fabricate user identity or human approval.
- Do **NOT** claim initialization succeeded if the CLI failed.
- Do **NOT** run initialization in a different project without explicit user authorization.

## Expected result

The project is initialized according to the installed AELC CLI's initialization contract.

The AELC CLI is the authoritative implementation of project initialization.