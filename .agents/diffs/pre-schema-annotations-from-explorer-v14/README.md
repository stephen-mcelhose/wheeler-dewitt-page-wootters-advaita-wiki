# Pre-schema annotations snapshot from Explorer v14

## Purpose
Internal, pre-change snapshot for the approved schema-annotation work. This is a preservation checkpoint only; no visual verification is claimed or recorded.

## Approved baselines
1. **v14** is the user-approved baseline for the overall reader layout and math display.
2. The approved older **Hilbert Spaces / Dirac Notation** styling is the baseline for inline definition treatments.
3. Definition terms must remain visually distinct from ordinary links.

## Regression set
Run regression checks against the following five pages:
1. Hilbert Spaces
2. Dirac Notation
3. Wheeler–DeWitt Formalism
4. Page–Wootters Mechanism
5. Exploratory Model: JON, Brackets, and Projection

## Snapshot record
- Source artifact path: `/app/artifacts/instances/ReactComponent/quantum-time-wiki-explorer/current.json`
- Preserved artifact JSON: `current.json`
- SHA-256 checksum: `c5f027383e319f896aba47e0d6146165d68bd1ca422b5374ca6f5057985934da`
- Artifact modified or published by this snapshot task: No.

## Rollback instructions
1. Stop any pending artifact changes.
2. Confirm the saved `current.json` checksum matches the value in this manifest.
3. Replace the source artifact JSON at the exact source artifact path above with this snapshot's `current.json` using the approved artifact replacement workflow.
4. Confirm the restored source JSON checksum matches the checksum recorded above.
5. Resume review using v14 as the reader-layout and math-display baseline, and the approved older Hilbert Spaces / Dirac Notation styling for inline definitions.
