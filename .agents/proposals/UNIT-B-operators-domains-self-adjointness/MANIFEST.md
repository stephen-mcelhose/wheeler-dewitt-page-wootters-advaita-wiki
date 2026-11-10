# UNIT B Manifest — Operators, Domains, and Self-Adjointness

## Proposal-only status

This implementation-ready package is not integrated. It does not alter canonical source, indexes, Explorer artifacts, learning paths, release/process records, publication state, or `notation-reference.md`.

## Proposed canonical targets

| Proposal file | Intended canonical path | Action | Implementation content |
|---|---|---|---|
| `operators-and-domains.md` | `mathematics/operators-and-domains.md` | Replace/expand | Domain-first concept; finite/infinite computational boundary; adjoint, symmetry, and self-adjointness. |
| `example-operators-domains-self-adjointness.md` | `examples/example-operators-domains-self-adjointness.md` | Create | Required four-part sequence, scoped Go helpers, finite self-adjointness, and derivative contrast. |
| `def-linear-operator.md` | `definitions/def-linear-operator.md` | Create | Concrete reusable definition. |
| `def-bounded-operator.md` | `definitions/def-bounded-operator.md` | Create | Concrete reusable definition. |
| `def-unbounded-operator.md` | `definitions/def-unbounded-operator.md` | Create | Definition explicitly separating universal truth from finite truncation evidence. |
| `def-dense-domain.md` | `definitions/def-dense-domain.md` | Create | Definition explicitly separating density from finite tail calculations. |
| `def-operator-domain.md` | `definitions/def-operator-domain.md` | Repair | Concrete reusable definition. |
| `def-adjoint.md` | `definitions/def-adjoint.md` | Repair | Concrete reusable definition. |
| `def-symmetric-operator.md` | `definitions/def-symmetric-operator.md` | Repair | Concrete reusable definition. |
| `def-self-adjoint-operator.md` | `definitions/def-self-adjoint-operator.md` | Repair | Concrete reusable definition. |

## Required implementation sequence in the proposed example

1. **Finite C² linearity witness:** `isLinearWitnessMatrix2D` checks one explicit witness and says it is not a universal proof.
2. **Finite C² bounded diagonal matrix:** an analytic \(\|D\|\le3\) proof is paired with `boundedDiagonalAnalyticBound2D` and `boundedDiagonalSampleRatio2D`.
3. **\(\ell^2\) index multiplier:** \((Tx)_n=nx_n\), with an analytic \(e_k\) proof of unboundedness and `finiteMultiplierTruncationRatio` for bounded finite prefixes.
4. **Finite support/density:** truncation and tail-norm proof, with `finiteTailNormAfter` for supplied finite data and its computational limits.

The same example retains `isSymmetricFiniteMatrix2D` and `isSelfAdjointFiniteMatrix2D`, carefully scoped to matrices on full \(\mathbb C^2\), followed by a short non-computational restricted-derivative contrast. No helper is named `isUnbounded` or `isDense`.

## Intended graph and definition links

- `operators-and-domains` has parents `hilbert-spaces` and `spectral-notation`; it is prerequisite for `composite-systems`, `dirac-quantization`, and `page-wootters-mechanism`.
- It has an `illustrates` relationship to the example; the example includes the reciprocal relationship pending project graph-convention validation.
- Inline definitions are marked at intended first reader-visible uses. During integration, reconcile metadata IDs such as `linear-operator` with canonical `def-...` node/file conventions before transform tests.

## Deferred shared-file work — do not apply here

1. Reconcile `notation-reference.md` for \(A:D(A)\to\mathcal H\), \(D(A)\), \(A^*\), \(A\subset A^*\), \(A=A^*\), and whether \(\ell^2\), \(c_{00}\), \(L^2([0,1])\), and \(C_c^\infty(0,1)\) need global rows.
2. Add/repair definitions and regenerate central glossary/index data only after source and schema review.
3. Resolve all source-review flags in `REVIEW.md` with approved locators.

## Integration validation (deferred)

Run frontmatter, relationship, link, annotation-transform, rendering, and `make index validate` checks only after canonical integration is authorized. Do not publish as part of this unit.
