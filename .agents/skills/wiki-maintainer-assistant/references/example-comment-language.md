# Mathematical Example Comment Language

Use this reference when adding or materially revising code in worked examples.

## Purpose

Comments explain the **mathematical model and its assumptions**. They must not merely narrate implementation behavior.

Examples are self-contained teaching artifacts. Repetition of notation, definitions, code, and elementary calculations is intentional when it lets a learner understand the current concept without reconstructing essential steps from a prior example.

## Assumption categories

Classify each assumption before writing a comment. Use only the categories needed by the example.

### 1. Mathematical precondition

Use `Given:` for facts required to interpret the calculation.

Examples:

```go
// Given: |φ⟩ and |ψ⟩ have coordinates in the same chosen finite basis.
```

```go
// Given: representative is a normalized nonzero ket.
```

Use this for object types, pre-established bases, domains, and nonzero or finite-norm conditions.

### 2. Model scope

Use `Model scope:` for deliberate restrictions that make a general idea calculable. A model scope is not automatically a requirement of the general concept.

Examples:

```go
// Model scope: this example works in the two-dimensional complex space C².
```

```go
// Model scope: this example uses a finite periodic clock.
```

```go
// Model scope: the ADM calculation assumes smooth compact boundaryless Σ.
```

### 3. Convention or representation

Use `Convention:` or `Representation:` for selected notation, sign, ordering, or data representation.

Examples:

```go
// Convention: ⟨φ|ψ⟩ is conjugate-linear in φ and linear in ψ.
```

```go
// Representation: a Go slice stores coordinates in one chosen ordered basis.
// It does not itself encode row/column orientation.
```

### 4. Illustrative choice

Use `Illustration:` for a choice made for clarity that is not mathematically unique.

```go
// Illustration: e₀ and e₁ are chosen because their coordinates are transparent.
```

```go
// Illustration: phaseStep selects one countable sample stream through a ray.
```

### 5. Mathematical fact or limitation

State the applicable definition, theorem, or boundary directly.

```go
// An orthonormal set has unit-norm vectors and zero overlap between distinct vectors.
```

```go
// A Go slice can represent finite coordinates but not an infinite-dimensional ket.
```

## RFC 2119 keywords

Use `MUST`, `MUST NOT`, `SHOULD`, and `MAY` only for precise, specable mathematical requirements or scope boundaries. The keyword is interpreted inside the preceding `Given:` and `Model scope:` statements.

Correct:

```go
// Given: n and m label elements of one chosen discrete orthonormal basis.
// Model scope: this calculation concerns that selected basis only.
// In an orthonormal basis, ⟨n|m⟩ MUST equal δ_nm.
```

Correct:

```go
// Model scope: this example works in C².
// In this C² model, two linearly independent vectors MUST span C².
```

Avoid generic implementation directives such as:

```go
// The caller MUST pass valid vectors.
```

Instead explain the mathematics that makes the operation meaningful:

```go
// Given: |φ⟩ and |ψ⟩ have coordinates in the same chosen finite basis.
```

## Missing prerequisites

If code assumes an idea not yet established—such as span, linear independence, target-space dimension, operator domain, or a measurement instrument—the comment must name the precondition. The learning path must then provide the missing prerequisite concept before the code is relied on pedagogically.

Example:

```go
// Given: u and v are coordinate kets in the target space C².
// A basis requires both linear independence and spanning.
// This example uses the C² theorem that two independent vectors span C².
```

## Golden examples

When an author is unsure which assumption category applies, or whether RFC 2119 wording is appropriate, they MUST begin from a reviewed golden example rather than inventing a new comment style.

Current golden references:

1. **Finite-dimensional basis scope and prerequisite logic** — `examples/example-bases-coordinates-and-orthonormality.md`
   - distinguishes general inner-product/norm operations from the \(\mathbb C^2\)-specific determinant and spanning model;
   - uses `Given:`, `Model scope:`, and a scoped `MUST` requirement;
   - names the boundary between an orthonormal set and an orthonormal basis.

2. **Ray representation and illustrative phase sampling** — `examples/example-quantum-states-rays-and-normalization.md`
   - distinguishes nonzero-vector preconditions from a chosen lazy phase-sampling stream;
   - states that a selected generator samples representatives and does not enumerate an uncountable ray.

3. **Discrete labels and Kronecker delta** — `examples/example-dirac-notation-basis-and-adjoint.md`
   - distinguishes assigned basis labels from vector entries;
   - scopes \(\delta_{nm}\) to a chosen discrete orthonormal basis.

If none of these covers the situation, write the proposed comment and flag it for review in the example handoff before treating it as a reusable pattern. Once reviewed, add it to this reference as a new golden example.

## Go-equivalent checklist

Every rigorous worked example includes Go that models its central finite or bounded calculation, construction, predicate, or invariant.

- The code must implement or check the central operation; it must not only print a precomputed value.
- When the central concept is infinite-dimensional or formal, include the closest honest finite representation: finite truncation, witness, prefix monitor, certified tail-bound contract, or non-computational contrast.
- State whether a result is an algebraic proof, an analytic infinite argument, a finite-model property, a supplied-data witness, or a prefix observation.
- Use scoped predicate names for honest finite checks, such as `IsOrthogonalProjector2D`, `IsSelfAdjointFiniteMatrix2D`, and `IsLinearWitnessMatrix2D`.
- Do not expose unscoped finite predicates that imply a general theorem, such as `IsUnbounded` or `IsDense`.
- Use errors for structural or declared-contract violations that the runtime can establish; do not raise an error claiming to decide an infinite property from a finite prefix without a stated certificate/budget contract.
- For streams, explicitly distinguish coordinate-stream shape from membership in \(\ell^2\) or an unbounded operator domain. Prefix monitors may report what holds through the observed prefix only.

## Self-contained-example checklist

Before completing an example, confirm that it visibly contains:

1. assumed prerequisites;
2. local setup and notation;
3. local definitions or restatements for every operation/helper used;
4. the concept-specific calculation;
5. mathematical scope and non-conclusions;
6. standard mathematical labels outside philosophy;
7. pedagogical code labeling or numerical safeguards;
8. comments that distinguish precondition, model scope, convention/representation, and illustrative choice where relevant.
