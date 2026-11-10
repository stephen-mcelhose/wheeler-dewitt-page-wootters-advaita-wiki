# Unit D proposal manifest

This is a **review-only proposal package**. Nothing in this directory is canonical or indexed.

## Proposed canonical targets

| Proposal file | Intended canonical target | Action | Direct dependencies |
|---|---|---|---|
| `mathematics/classical-canonical-mechanics-primer.md` | `mathematics/classical-canonical-mechanics-primer.md` | New prerequisite concept | elementary multivariable differentiation; current mathematical-notation reference (must be expanded) |
| `mathematics/hamiltonian-phase-space-and-poisson-brackets.md` | `mathematics/hamiltonian-phase-space-and-poisson-brackets.md` | Replace/expand | `classical-canonical-mechanics-primer` |
| `mathematics/constrained-systems.md` | `mathematics/constrained-systems.md` | Replace/expand | `hamiltonian-phase-space-and-poisson-brackets`; primer; a restricted regular Dirac–Bergmann setting |
| `examples/example-harmonic-oscillator-poisson-bracket.md` | `examples/example-harmonic-oscillator-poisson-bracket.md` | New dedicated example | primer; Hamiltonian Phase Space and Poisson Brackets |
| `examples/example-parametrized-free-particle-constraint-flow.md` | `examples/example-parametrized-free-particle-constraint-flow.md` | New dedicated example | primer; Classical Constrained Systems |
| `definitions/def-phase-space.md` | `definitions/def-phase-space.md` | Repair | Hamiltonian Phase Space and Poisson Brackets |
| `definitions/def-poisson-bracket.md` | `definitions/def-poisson-bracket.md` | Repair | Hamiltonian Phase Space and Poisson Brackets |
| `definitions/def-hamiltonian.md` | `definitions/def-hamiltonian.md` | New | Classical Canonical Mechanics Primer |
| `definitions/def-hamiltonian-flow.md` | `definitions/def-hamiltonian-flow.md` | New | Hamiltonian Phase Space and Poisson Brackets |
| `definitions/def-constraint-surface.md` | `definitions/def-constraint-surface.md` | New | Classical Constrained Systems |
| `definitions/def-canonical-hamiltonian.md` | `definitions/def-canonical-hamiltonian.md` | New | Classical Constrained Systems |
| `definitions/def-total-hamiltonian.md` | `definitions/def-total-hamiltonian.md` | New | Classical Constrained Systems |
| `definitions/def-gauge-orbit.md` | `definitions/def-gauge-orbit.md` | New | Classical Constrained Systems |
| `definitions/def-gauge-fixing.md` | `definitions/def-gauge-fixing.md` | New | Classical Constrained Systems |
| `definitions/def-constraint.md` | `definitions/def-constraint.md` | Repair | Classical Constrained Systems |
| `definitions/def-weak-equality.md` | `definitions/def-weak-equality.md` | Repair | Classical Constrained Systems |
| `definitions/def-first-class-constraint.md` | `definitions/def-first-class-constraint.md` | Repair | Classical Constrained Systems |
| `definitions/def-second-class-constraint.md` | `definitions/def-second-class-constraint.md` | Repair | Classical Constrained Systems |
| `definitions/def-lagrange-multiplier.md` | `definitions/def-lagrange-multiplier.md` | Repair | Classical Constrained Systems |

## Integration requests outside this package

1. Insert the proposed primer immediately before the current Hamiltonian concept in `overview-learning-path.md`; do not make quantum operators/domains a parent of Classical Constrained Systems.
2. Add the proposed concept/example links and definition relationships after shared-ID reconciliation.
3. Expand `notation-reference.md` for \,\(q^i,p_i\), \,\(\partial_i\), \,\(X_H\), \,\(\dot F\), \,\(\phi_a\), \,\(\Gamma\), \,\(\approx\), \,\(H_{\rm can}\), \,\(H_T\), \,\(\lambda^a\), and a gauge parameter \,\(s\). The register must say explicitly that `s` is **not time**.
4. Run source, graph, annotation-transform, index, and independent classical-mechanics/theoretical-physics review gates during integration.
