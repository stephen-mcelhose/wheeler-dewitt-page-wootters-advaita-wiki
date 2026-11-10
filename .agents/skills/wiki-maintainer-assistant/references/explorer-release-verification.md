# Explorer Release Verification

Use this reference for every publication or republish of the Quantum Time Wiki Explorer.

## Purpose

A successful build, TypeScript compile, graph validation, candidate-data check, or candidate/live byte-equality check does **not** prove that the user-facing explorer renders correctly. Byte equality only proves that the published artifact matches the candidate; it can preserve the same runtime defect.

A release is not verified until both the **candidate gates** and the **published-display gates** pass.

## A. Candidate gates — before publication

1. Run canonical annotation tests, index build, and graph validation.
2. Run source-count reconciliation before generating a content/data preview:
   ```sh
   python3 .agents/reconcile_source_counts.py \
     --source-index viewer/wiki-data.json \
     --expected .agents/expected-source-counts.json
   ```
   - If actual counts are **more**, stop and ask: “Did I intentionally add a concept, definition, example, or guide? Should I update expected counts?” If no, fail hard and investigate. If yes, update the approved expected-count snapshot only after the additions are identified and confirmed.
   - If actual counts are **less**, stop and ask the corresponding removal question. If no, fail hard and investigate. If yes, update the snapshot only after the removals are identified and confirmed.
   - If counts are **equal**, still ask/record: “Did this work intentionally add or remove a concept, definition, example, or guide?” If yes, investigate why the aggregate count did not change, then record the reconciliation decision before continuing.
3. Confirm the candidate contains all canonical concepts, definitions, examples, nonempty bodies, relationships, and generated annotations.
3. Run `python3 .agents/validate_explorer_data_payload.py <candidate> --label candidate` before compile. It must reject every configured invalid placeholder sentinel (including literal `PLACEHOLDER`) and require parseable, nonempty `concepts`, `definitions`, `examples`, and `learningOrder` exports plus `totalNodes`; concept and example canonical bodies must be nonempty. TypeScript compilation alone is insufficient.
4. Run the required exact-artifact TSX gate: `python3 .agents/exact_artifact_tsx_gate.py <candidate>`. It must re-run the sentinel/payload gate and materialize and compile the exact candidate artifact's `code` as `/App.tsx` and `files['/data.ts']['code']` as `/data.ts` after all candidate generation. A stale compiler fixture or related source file is insufficient.
5. Run relevant deterministic regression checks for previously observed defects.
6. For every changed reader-visible path, identify the minimal user-visible scenario that must render after publication.

The sentinel/payload and exact-artifact TSX gates are blocking release gates. Record their commands, artifact hash, canonical counts, and App/data byte counts in the release handoff before publication.

## A.2 User-observed preview gate — default for reader-visible changes

For a reader-visible explorer change, the default workflow is **candidate gates → publish → integrity gates → user preview → release claim**, not autonomous repeated release attempts.

1. Build and publish the candidate only after A passes.
2. Immediately complete A.1 publication-integrity checks. If they fail, contain the failure and do not ask the user to preview a known-corrupt artifact.
3. After A.1 passes, label the result **`preview available; awaiting user observation`**. Do not call it a release, verified, ready, or display-checked.
4. Tell the user exactly where to look and the single smallest behavior to inspect. For example: “Open Bases and Coordinates, select Worked examples, open the example, then use Back to Bases and Coordinates.”
5. Wait for the user’s observation. The user’s visible Explorer panel is valid primary evidence for the rendered UI.
6. If the user reports an error or unexpected behavior, treat it as a failed gate. Preserve workflow state, triage the failure, repair the candidate, and return to A. Do not ask the user to perform a broader test while a blocking error is present.
7. Only after the user confirms the stated preview behavior, record the user-observed display result in the handoff and advance the status to the next explicitly scoped preview or to verified readiness if all required display checks are complete.

The assistant must not request a long multi-step checklist by default. Ask for one bounded visible behavior per preview iteration, unless the user explicitly asks for a broader review.

## A.1 Published-artifact integrity gates — immediately after publication

Before display inspection:

1. Retrieve the live ReactComponent artifact and record its version/revision, SHA-256, App-source byte count, and `/data.ts` byte count.
2. Compare the live artifact SHA-256 with the approved candidate SHA-256. If byte identity is not expected, record and validate an approved field-level equivalence instead.
3. Run `python3 .agents/validate_explorer_data_payload.py <live-artifact> --label live` before any display status. It must reject the configured placeholder sentinels and require the same parseable, nonempty canonical payload exports as the candidate gate.
4. Verify live artifact completeness: required `/data.ts` exports, expected canonical counts, and nonempty concept/definition/example payloads. `validate_published_artifact.py` must enforce the sentinel/payload gate for both candidate and live before comparing counts.
5. Run the exact-artifact TSX parser/compiler gate against the live artifact after materializing its actual `code` and `/data.ts`: `python3 .agents/exact_artifact_tsx_gate.py <live-artifact> --label live`. A candidate-only compiler result, a stale fixture, or a byte comparison is not a substitute.
6. Run relevant deterministic regression validators against the live artifact only after the completeness gate passes.
7. If any integrity check fails, status is `failed — publication integrity failure`; do not proceed to published-display verification or call the artifact published-ready.

## B. Published-display gates — after publication

Only after A and A.1 pass, inspect the newly published explorer itself, not only its JSON/artifact bytes.

For this explorer, the minimum release smoke path is:

1. Open the explorer successfully; no global error screen, blank screen, or runtime exception may appear.
2. Open one concept from each available populated domain/category.
3. Verify that an absent optional domain/category renders empty or is omitted without a crash.
4. Open a concept with inline definitions and verify one definition popover, including the Norm fixture:
   \[
   \|\psi\|=\sqrt{\langle\psi|\psi\rangle}.
   \]
   The math must render, not appear as raw TeX.
5. Verify the visible learning-path/next-navigation behavior for every changed learning-flow relation.
6. Verify at least one worked example renders with prose, equations, and code visible.

Record the tested paths and result in the release handoff.

## C. Acceptance language

- Call a release **published, pending display verification** only after publication integrity verification is complete but before B is complete.
- Do not use `published, pending display verification` for a truncated, non-equivalent, malformed, or otherwise integrity-unverified artifact.
- Call it **verified and ready** only after A and B pass.
- If a display inspection capability is unavailable, say that B could not be performed. Do not describe the release as fully verified.
- If B reveals an error, treat the release as failed regardless of compilation, data checks, or candidate/live byte equality.

## D. Regression-test policy

After an observed production/display failure:

1. Identify whether an established release step was skipped or insufficient.
2. Record the missed/insufficient step in the incident handoff.
3. Add the smallest deterministic regression test that directly guards the failure pattern when feasible.
4. Add or refine the published-display smoke path if the failure would only be visible at runtime.
5. Do not call an implementation hotfix a process patch. The process patch is the changed gate, checklist, automation, or acceptance rule that prevents recurrence.

## Current regression checks

`.agents/release_smoke_check.py` is a narrow regression check for unsafe optional domain-bucket access. It is useful but insufficient as a complete release verification. It supplements, and does not replace, the published-display gates above.

`.agents/validate_kronecker_delta_math_fixture.py <artifact>` is a blocking candidate and live regression gate for the exact Kronecker-delta and notation-reference not-equal fixtures. It requires the emitted payload to retain canonical `n\\ne m` and `n\\neq m` source forms plus balanced Kronecker `cases` markup, then validates the actual artifact `MathBlock` general relation-token normalization and KaTeX HTML for both aliases. Both rendered forms must be free of KaTeX errors and private-use glyphs and expose a clear not-equal condition. Run it after the payload gate and exact-artifact compile before publication, and again against the live artifact during A.1.
