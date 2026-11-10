# Case Study — Failure Escalation: Learning Navigation and Publication Integrity

## Scenario

The Quantum Time Wiki Explorer is intended to guide a learner through a prerequisite-first curriculum. The user observed that the unlabeled **Next** control from **Dirac Notation** opened **Dirac Quantization and Physical States** instead of **Projection Operators**.

The expected learning transition was:

\[
\text{Bases and Coordinates}
\longrightarrow
\text{Dirac Notation}
\longrightarrow
\text{Projection Operators}
\longrightarrow
\text{Born Rule and Quantum Probability}.
\]

Initial diagnosis showed that the reader navigated by adjacent positions in the generated `concepts` artifact array. That array was a technical order, not the canonical curriculum order in `overview-learning-path.md`.

A source-derived learning-navigation candidate was built, but publication then produced a second failure: the live artifact payload was truncated. The validated candidate and live artifact had different SHA-256 values, and the live `/data.ts` payload was drastically smaller. The release therefore could not be treated as verified or ready.

## Action

### 1. Triage and containment

- Recorded observed versus expected navigation behavior, user impact, severity, reproduction, and containment.
- Paused the Foundations workflow at the Bases and Coordinates → Dirac Notation gate.
- Explicitly blocked progression until navigation semantics and publication integrity were verified.

### 2. Immediate technical investigation

- Identified the reader implementation using `concepts[at-1]` and `concepts[at+1]`.
- Distinguished the existing content classifications from paths through content.
- Identified canonical path types:
  - `learning` — curated total order for recommended study;
  - `prerequisite` — dependency partial order;
  - `exploration` — labeled typed-relationship traversal;
  - `recall` — local definition support.
- Preserved sidebar/domain grouping as explicitly out of scope.

### 3. Hotfix design and candidate validation

- Added a deterministic parser for `overview-learning-path.md`.
- Generated a machine-readable `learningOrder` with 38 canonical concept IDs.
- Updated the candidate reader to use `learningOrder`, not artifact-array position, for unlabeled Previous/Next controls.
- Added candidate validation requiring source-order equality and rejecting positional `concepts[at±1]` navigation.
- Candidate checks passed: annotation tests, graph/index validation, TypeScript compilation, optional-domain regression check, learning-order parser, learning-navigation validator, and completeness/preservation checks.

### 4. Process investigation and patch

The navigation defect Five Whys established that technical array order silently substituted for the canonical learning path because no source-derived path data or navigation validator existed, and no display check inspected the changed transition.

The process patch added:

- canonical path governance in `WIKI_CHARTER.md`;
- a path registry in `.agents/references-canonical-flows.md`;
- an active navigation issue with source, validation, and display acceptance criteria;
- release policy distinguishing candidate validation from published-display validation.

The publication-truncation failure then exposed a separate process gap: candidate validation and a successful write did not prove that the live artifact retained the full candidate payload.

The process patch was extended with:

- `validate_published_artifact.py` for candidate/live SHA-256 equality, live payload structure, counts, and required navigation tokens;
- a mandatory publication-integrity gate before display verification;
- explicit release statuses separating candidate validation, integrity verification, display verification, and verified readiness;
- a requirement for separate Five Whys when one incident contains distinct failure modes.

## Outcome

### What worked

- The original navigation defect was correctly contained and diagnosed.
- The candidate fix was source-derived and deterministically validated.
- The escalation process prevented an incomplete/truncated publication from being described as a verified release.
- The project now distinguishes a technical hotfix from a durable process patch.

### What did not yet work

- The first publication of the learning-navigation candidate did not preserve the complete data payload.
- Candidate/live SHA-256 mismatch proved that live artifact integrity had not been established.
- Published-display verification was correctly not performed before integrity restoration.

### Status at case-study creation

```text
failed — publication integrity failure;
candidate validated;
live artifact non-equivalent to candidate;
published-display verification not performed.
```

## Next Steps

1. Restore the complete live artifact from the validated deterministic candidate through a source-preserving publication method.
2. Run `validate_published_artifact.py <candidate> <live>` and require success before any UI inspection.
3. Run learning-navigation and optional-domain regression checks against the complete live artifact.
4. Perform and record published-display verification:
   - explorer opens without runtime error;
   - Bases and Coordinates → Dirac Notation → Projection Operators → Born Rule;
   - one definition popover renders the Norm math fixture as mathematics;
   - one worked example renders prose, equations, and code.
5. Complete the publication-truncation Five Whys with evidence about the failed publication mechanism.
6. Update the incident handoff with final integrity evidence, display results, residual risk, and release status.
7. Resume the Foundations workflow only after the navigation release is verified and ready.
