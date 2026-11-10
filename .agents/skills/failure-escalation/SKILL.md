---
name: failure-escalation
description: Triage observed failures, repair the immediate problem, and conduct a process investigation—defaulting to Five Whys—to add durable prevention gates and update governing documents.
---

# Failure Escalation

Use this skill whenever a user-visible failure, broken release, validation miss, incorrect claim of completion, unsafe operation, or repeated defect is observed.

## Purpose

Treat a failure as three linked tasks:

1. **Triage** — establish impact, containment, and the smallest reproducible observation.
2. **Investigate and fix the problem** — identify the technical/content defect and restore correct behavior.
3. **Investigate and fix the process** — determine why the existing process did not prevent or detect the defect; default to Five Whys; change durable checks, gates, documents, or ownership so the same failure class is less likely to recur.

Do not call an implementation hotfix a process patch. A **hotfix** restores the artifact or output. A **process patch** changes the workflow, verification gates, automated tests, acceptance criteria, or governing documents.

## Required behavior

### 0. Preserve workflow state before requesting help

Before asking the user for clarification, delegating, or pausing, record:

- active objective and task-list position;
- observed failure and user impact;
- affected files/artifacts/releases;
- containment state;
- exact next diagnostic action;
- unresolved decision or input needed.

Use the project handoff or issue location.

### 1. Triage

Record an incident with:

- **Observed behavior:** exact message, screenshot description, failed result, or reproducible steps;
- **Expected behavior:** what should have happened;
- **Impact:** user-visible, data integrity, scientific/content correctness, release status, scope;
- **Severity:** blocking, high, medium, or low;
- **Containment:** stop publication, roll back, mark release pending verification, disable a path, or otherwise limit harm;
- **Reproduction:** smallest deterministic test or user-visible path that demonstrates the failure.

Do not continue ordinary planned work through a blocking failure. First contain and classify it.

### 2. Investigate and fix the immediate problem

1. Reproduce the issue when possible.
2. Identify the smallest credible root cause with evidence.
3. Apply the smallest safe hotfix that restores required behavior without deleting unrelated canonical content.
4. Validate the repaired output at the level where it failed:
   - source/graph failure → source validation;
   - compile failure → compile the exact final candidate artifact, not a stale fixture;
   - runtime/display failure → after publication integrity passes, request one bounded user-observed preview in the visible UI; do not substitute static checks for that observation;
   - mathematical/content failure → independent subject review where warranted.
5. Verify the fix did not cause regressions in directly adjacent paths.
6. When publication or deployment is involved, verify artifact integrity before any runtime/display claim:
   - record candidate revision identifier, byte count, and SHA-256;
   - record live revision identifier, byte count, and SHA-256;
   - compare candidate and live bytes, or record an approved field-by-field equivalence check;
   - validate required artifact structure and canonical-content counts against the live artifact.

A source-level validator passing against a live artifact does not prove that the artifact is complete or that publication preserved the candidate.

Record technical root cause, hotfix, and verification separately from process prevention.

### 3. Investigate and fix the process

After containment and hotfix, default to **Five Whys**. Start from the observed failure, not from a preferred solution.

1. Why did the user observe the failure?
2. Why did the defective output pass immediate checks?
3. Why did the existing process omit or inadequately perform the needed check?
4. Why did governing instructions, release checklists, tooling, or ownership not make it mandatory?
5. Why was that process gap not previously visible or tested?

Stop earlier only if a verified, directly actionable root cause is established. Mark uncertain causal links as hypotheses and seek evidence.

If one incident contains distinct failure modes—for example, an application defect followed by publication corruption—record a separate root-cause analysis and Five Whys for each failure mode. A process patch for the original defect does not close a later deployment-integrity failure.

Then create a process patch that includes one or more of:

- an explicit release/acceptance gate;
- deterministic regression automation;
- a required human display or domain review;
- a checklist revision;
- a maintainer-skill or charter rule;
- a test fixture;
- a clear ownership/approval boundary.

The process patch must state the failure class prevented, trigger point, exact check, required evidence, and residual risks.

## Main governing documents for this project

1. `WIKI_CHARTER.md` — durable project policy and architecture.
2. `.agents/skills/wiki-maintainer-assistant/SKILL.md` — maintainer workflow.
3. `.agents/skills/wiki-maintainer-assistant/references/` — reusable checklists and standards.
4. `.agents/issues/` — deferred work and recurring-risk tracking.
5. `.agents/handoffs/` — incident status, hotfix, Five Whys, process patch, validation, and next action.

Do not scatter a permanent process rule only in chat or a one-off incident note.

## Release-specific rule

Distinguish:

- **candidate verification** — source, structure, compile, deterministic checks;
- **published-display verification** — actual published user-facing behavior.

Candidate/live byte equality proves equivalence, not correctness. A runtime/display defect discovered after publish means the release gate failed even when compilation and byte equality passed.

Use precise status:

- `candidate validated, publication pending` before a publication attempt;
- `published, integrity verification pending` after a write but before complete live-artifact and candidate/live-equivalence checks;
- `preview available; awaiting user observation` only after integrity verification and all live deterministic checks pass;
- `published, pending display verification` only after at least one bounded user-observed preview passes but broader required display checks remain;
- `verified and ready` only after candidate, live-integrity, and all required display gates pass;
- `failed — <gate/failure>` when a required gate fails, including incomplete, truncated, or non-equivalent publication.

## Completion criteria

Do not report a failure as resolved until:

- triage is recorded;
- immediate defect is fixed and verified at the level of failure;
- Five Whys or evidence-based equivalent is recorded;
- the process patch is written into governing documents;
- deterministic automation is added when feasible;
- residual manual checks are explicit when automation cannot prove behavior;
- regression/release gates pass;
- the handoff gives a next maintainer exact status and remaining risks.

## Compact incident template

```markdown
# Incident — <short title>

## Triage
- Observed:
- Expected:
- Impact/severity:
- Containment:
- Reproduction:

## Immediate investigation and hotfix
- Root cause:
- Hotfix:
- Verification:

## Failure modes
- Failure mode 1:
- Failure mode 2 (if applicable):

## Process investigation — Five Whys
1. Why?
2. Why?
3. Why?
4. Why?
5. Why?

## Publication integrity (when applicable)
- Candidate revision / SHA-256 / bytes:
- Live revision / SHA-256 / bytes:
- Candidate/live comparison:
- Live completeness/count validation:

## Process patch
- Failure class:
- New/changed gate:
- Automation:
- Required human check:
- Governing documents changed:
- Residual risk:

## Status and next action
```
