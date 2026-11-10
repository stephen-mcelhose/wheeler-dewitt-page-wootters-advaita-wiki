# Review Report — Unit E Proposal: Dirac Quantization and Physical State Spaces

## Scope and package status

This is a **proposal-only** implementation package. It is conditional on acceptance of Unit D. It does not modify canonical pages, definitions, indexes, Explorer artifacts, learning paths, global process files, or `notation-reference.md`.

## Files proposed

- `mathematics/dirac-quantization.md`
- `mathematics/formal-and-physical-state-spaces.md`
- `definitions/def-formal-constraint-solution.md`
- `examples/example-dirac-quantization-c3-formal-and-physical-spaces.md`
- `MANIFEST.md`

## Mathematical and pedagogical audit

### Covered prerequisites and local setup

- Unit D’s constrained-system distinction is explicitly treated as an integration gate.
- Operator domains are named before writing the formal constraint equation as meaningful.
- Generalized/distributional solutions are connected to spectral prerequisites and are not presented as ordinary kets.
- The paired example restates its finite C³ basis, inner-product convention, constraint matrix, matrix action, null-space calculation, and declared pairing locally.

### Core distinctions preserved

1. **Kinematical space:** an auxiliary representation, not already a physical state space.
2. **Formal solutions:** objects satisfying a stated quantum constraint condition; may be distributional or domain-dependent.
3. **Physical construction:** requires a physical inner product or equivalent amplitude construction; it is not provided by merely writing the formal equation.
4. **Finite toy scope:** in the example, the ordinary kernel is an intentional finite-matrix coincidence and the physical pairing is explicitly stipulated rather than derived.

### Required caveats explicitly visible

- operator domains and common-domain compatibility;
- physical inner products are additional/model-dependent;
- factor-ordering ambiguity;
- constraint anomalies/closure;
- generalized/distributional solutions;
- zero in continuous spectrum;
- no general inference that physical state space equals a kinematical kernel;
- rigging maps and group averaging are conditional strategies, not automatic outputs.

## Source audit

The proposed material cites:

- M. Henneaux and C. Teitelboim, *Quantization of Gauge Systems* (ISBN:9780691037691).
- D. Giulini and D. Marolf, “On the Generality of Refined Algebraic Quantization” (arXiv:gr-qc/9812024).

The central integrator should verify exact support and any preferred reader URLs during canonical source validation. The narrow claim about a rigging map is intentionally conditional and non-universal.

## Example/code audit

- Uses standard mathematical labels only; no person-like labels.
- Includes `Given:`, `Model scope:`, and `Convention:` code comments following the required mathematical-comment language.
- Uses explicit finite-model Go helper names: `applyConstraint3D`, `zeroConstraintResidual3D`, and `physicalInnerProductOnToyKernel3D`.
- Uses a numerical tolerance only for the finite residual check and labels that result as a representation-specific ordinary matrix-kernel test.
- Does not offer the code as an algorithm for generalized solutions, rigging maps, anomaly checks, gauge reduction, or infinite-dimensional physical state spaces.

## Findings and blockers

### Critical blockers

- **Unit D must be accepted first.** The proposal relies on its settled explanation of classical constraints/first-class systems. No Unit E integration is recommended before that gate.

### High-priority central reconciliation

- The shared notation reference needs central registration/review of \(\mathcal H_{\mathrm{kin}}\), \(\mathcal H_{\mathrm{phys}}\), \(\Phi\), \(\Phi^*\), and kinematical/physical inner-product subscripts if this package is integrated.
- Reconcile `def-anomaly` so its general constrained-quantization wording/linking is appropriate; its current canonical target is gravity-specific.
- Run the repository’s metadata/annotation transform and graph validations after integration; none were run because this package intentionally does not alter canonical sources.

### Requested independent review

An independent mathematics or theoretical-physics reviewer should check:

1. the formal/physical-space distinction, especially the role of dual/test spaces;
2. conditions under which group averaging or a rigging map can be invoked;
3. factor-ordering and anomaly language;
4. the phrase “same underlying solution vectors” in the finite toy model, to ensure it is read only as a deliberately declared representation, not as a general physical-space construction.

## Readiness

**Ready for user review as a bounded proposal package, conditional on Unit D acceptance.** It is not ready for canonical integration or an `approved` status without the stated unit gate, shared-file reconciliation, source validation, independent review, and post-integration validation.
