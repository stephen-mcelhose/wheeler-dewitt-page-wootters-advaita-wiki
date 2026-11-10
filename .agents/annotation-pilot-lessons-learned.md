# Schema Annotation Pilot — Lessons Learned

**Status:** Active scratch record for the next narrowly scoped implementation attempt.

## What failed

An earlier five-page pilot was published with an empty `/data.ts` array. The React component compiled, but its canonical concept and definition data were not preserved. It therefore violated the project's highest-priority rule: the canonical Markdown-derived page body is the sole source of reader content.

## Non-negotiable safeguards

1. **Never construct or publish an artifact with partial data.** Every candidate must retain the full, nonempty `/data.ts` file and its canonical page bodies.
2. **Copy the existing artifact as the candidate.** Modify only the minimum required source fields; do not rebuild the ReactComponent object from a reduced template.
3. **Verify data retention before publish.** Require all of the following against the candidate:
   - `/data.ts` exists and is nonempty;
   - the concept and definition arrays are nonempty;
   - the five regression-page IDs and their full bodies exist;
   - candidate data length does not materially shrink from the baseline unless explicitly approved.
4. **One small task at a time.** First write the pilot schema and audit data only. Next, modify the renderer only after the schema is present and verified. Do not combine a broad content migration with a renderer change.
5. **Use a source-level dry run before publishing.** The pilot logic must return the unchanged canonical body if no page schema applies or if a term is unmatched.
6. **Do not claim visual verification without inspecting a render.** Compile success and JSON validity are not visual verification.

## Baselines that must remain separate

- **Explorer v14:** approved baseline for overall reader layout and mathematical rendering.
- **Approved Hilbert Spaces / Dirac Notation treatment:** baseline for inline definition appearance and behavior.
- **Ordinary links:** remain conventional navigation links. Definitions are local explanatory annotations and must not resemble ordinary links.

## Scope for the retry

Only five pages may receive schema-driven annotation metadata and annotation behavior:

1. Hilbert Spaces
2. Dirac Notation
3. Wheeler–DeWitt Formalism
4. Page–Wootters Mechanism
5. Exploratory Model: JON, Brackets, and Projection

Do not roll the feature out globally until the pilot has passed visual comparison and received explicit approval.

## Required annotation behavior

- Primary format: page-level `inline_definitions` schema that defines a term and annotates only its first eligible prose occurrence.
- Escape hatch: explicit `{{def:definition-id|Visible term}}` syntax, used only when automatic placement is ambiguous.
- The full canonical body remains rendered verbatim except for the inserted inline definition control.
- Annotation must never occur inside headings, equations, code, citations, warning/caveat blocks, or existing Markdown links.
- An unmatched term leaves source prose unchanged and generates a maintenance/audit warning.

## Candidate pre-publish checklist

- [ ] Candidate was copied from the baseline artifact rather than reconstructed.
- [ ] `/data.ts` is present, nonempty, and near baseline length.
- [ ] All five pilot concepts and their full bodies are present.
- [ ] Existing ordinary links retain link styling and direct navigation.
- [ ] Definition terms use the approved inline definition style, not link styling.
- [ ] v14 inline and display mathematics remain handled separately from prose annotation.
- [ ] Philosophy pages preserve Draft / Under Construction / Not reviewed warnings.
- [ ] TypeScript compilation passes.
- [ ] No browser/pixel verification is claimed unless a render was actually inspected.

## Second failed attempt — additional lesson

The retry again produced a candidate with a populated definitions array but an empty `concepts` array. It was immediately rolled back before leaving that state in the explorer. This demonstrates that agent-generated reconstruction of the large `/data.ts` file is unsafe, even when a task explicitly requests copy-preservation.

### New hard constraint

**Do not delegate or hand-author the full artifact JSON or `/data.ts` for this pilot.** The next implementation must make a small, deterministic source transformation directly from the checked baseline file, then parse the generated JSON and assert that it preserves all 34 concepts, all 58 definitions, and the full canonical bodies before it can be published.

The transformation must be driven by a script stored in the workspace so its exact input, output, validation, and diff are inspectable. If a safe parser-based edit cannot be prepared locally, stop before publishing and retain the baseline.

## Rollback source

`/app/workspace/wheeler-dewitt-page-wootters-advaita-wiki/.agents/diffs/pre-schema-annotations-from-explorer-v14/current.json`

Checksum: `c5f027383e319f896aba47e0d6146165d68bd1ca422b5374ca6f5057985934da`
