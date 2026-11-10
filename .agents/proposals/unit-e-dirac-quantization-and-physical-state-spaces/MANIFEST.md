# Unit E Proposal Manifest — Dirac Quantization and Physical State Spaces

**Status:** Proposal only. This package is conditional on acceptance of Unit D (Hamiltonian phase space and classical constrained systems). No canonical, generated, Explorer, learning-path, release/process, or shared notation file is modified.

## Proposed target files

| Proposed package file | Intended canonical target | Purpose |
|---|---|---|
| `mathematics/dirac-quantization.md` | `mathematics/dirac-quantization.md` | Replaces the short concept stub with scoped Dirac-quantization content, including domains, generalized solutions, ordering, anomaly, and physical-pairing boundaries. |
| `mathematics/formal-and-physical-state-spaces.md` | `mathematics/formal-and-physical-state-spaces.md` | Separates kinematical, formal-solution, and physical layers, and explains why an ordinary kernel is not universal. |
| `definitions/def-formal-constraint-solution.md` | `definitions/def-formal-constraint-solution.md` | Adds the reusable local term required by both proposed concepts. |
| `examples/example-dirac-quantization-c3-formal-and-physical-spaces.md` | `examples/example-dirac-quantization-c3-formal-and-physical-spaces.md` | A paired, self-contained finite C³ toy example illustrating both Unit E concepts. |

## Direct dependencies

- `mathematics/constrained-systems.md` — **Unit D acceptance blocker**: classical first-class constraints and their role must be accepted before this package is integrated.
- `mathematics/operators-and-domains.md` — operator-domain caveats.
- `mathematics/spectral-notation.md` — generalized/distributional-solution boundary.
- Existing definitions: `def-kinematical-state`, `def-physical-state`, `def-physical-inner-product`, `def-factor-ordering`, `def-anomaly`, `def-operator-domain`, and `def-generalized-eigenvector`.
- Downstream target: `physics/dirac-quantization-gravity.md`.

## Intended graph-link recommendations

1. Add `spectral-notation` as a parent of `dirac-quantization` because distributional/generalized solutions are a visible prerequisite distinction.
2. Add `dirac-quantization` → `formal-and-physical-state-spaces` as `prerequisite-for`.
3. Add the paired example as `illustrates` from **both** Unit E concepts; its own metadata has two `illustrates` edges.
4. Add `def-formal-constraint-solution` as a `related-to` node for both Unit E concepts.
5. Retain `formal-and-physical-state-spaces` → `dirac-quantization-gravity` as `prerequisite-for`.

## Shared-file changes requested for central reconciliation

None performed. If the main agent accepts this proposal, reconcile the following shared changes centrally:

1. Register notation locally and globally as needed: \(\mathcal H_{\mathrm{kin}}\), \(\mathcal H_{\mathrm{phys}}\), \(\Phi\), \(\Phi^*\), \(\langle\cdot|\cdot\rangle_{\mathrm{kin}}\), and \(\langle\cdot|\cdot\rangle_{\mathrm{phys}}\). The proposed pages introduce each locally; `notation-reference.md` requires a central decision and is intentionally untouched.
2. Reconcile the existing `def-anomaly` link target (currently gravity-only) with the general constrained-quantization use proposed here.
3. Reconcile current canonical inline-definition metadata/style with the explicit `{{def:...|...}}` proposal markup, transform tests, and graph validator behavior.
4. Decide whether a separate reusable `rigging map` definition is wanted. This proposal intentionally explains it locally and does not make it a required term, because its construction is not used by the finite example.
5. Add the example to generated indexes only after canonical integration; do not alter learning-path ordering.

## Source and review requirements

- Sources supplied: Henneaux–Teitelboim (ISBN:9780691037691) and Giulini–Marolf (arXiv:gr-qc/9812024).
- Require independent mathematics/theoretical-physics review of constraint domains, generalized solutions, anomaly language, rigging-map caveats, and the proposed physical-pairing statement before promotion beyond `draft`.
- Run definition-annotation transform tests, index build, and graph validation only after the main agent integrates canonical files.
