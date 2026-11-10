# Review — Unit D: Hamiltonian phase space and classical constrained systems

## Recommendation: add a compact prerequisite primer

**Yes.** A compact **Classical Canonical Mechanics Primer** is required before the existing Hamiltonian concept. The current concept starts with canonical coordinates, conjugate momenta, partial derivatives, a summation, a Hamiltonian, and a time derivative, without teaching their mechanical relation. Its empty `parents` list makes those assumptions invisible. The current constrained-systems page also incorrectly lists `operators-and-domains`—a quantum-operator topic—as a prerequisite; it should instead depend on the proposed primer and Hamiltonian phase-space concept.

The primer is deliberately bounded: finite-dimensional, smooth, external-time mechanical models with regular Legendre transform. It introduces no constraint analysis and does not claim coverage of field theory, singular Lagrangians, boundary terms, or relativity.

## Core repair adopted throughout

Two distinct flows must never be conflated:

| Context | Generator and parameter | What it represents |
|---|---|---|
| Ordinary Hamiltonian mechanics | `H` and an externally supplied time `t` | Evolution of a physical state in an external-time model. |
| First-class constrained system | constraint combination and a gauge parameter `s` | Motion between gauge-related phase-space descriptions; `s` is not time. |

A parametrized free particle demonstrates the distinction. In the proposed convention, the constraint flow changes the clock coordinate as `dt/ds=1`, so `t` may label points locally along an orbit, but the flow parameter `s` remains a gauge parameter. Selecting `t=t_0` is a gauge condition, not a declaration that gauge flow is external-time evolution.

## Mathematical scope and caveats

- All general formulas use a finite-dimensional smooth phase space in canonical coordinates. Global coordinate and global gauge-fixing problems are excluded.
- First-class statements are qualified by regularity assumptions. A first-class constraint is not automatically a complete, globally valid gauge generator in arbitrary systems.
- The total Hamiltonian displayed is the primary-constraint Dirac–Bergmann form. Secondary constraints and multiplier-consistency conditions require the full algorithm and are named as outside scope.
- The second-class contrast uses the bracket matrix and does not derive the Dirac bracket.
- The parametrized model is a pedagogical deparametrizable toy model. It establishes neither a global clock nor a result about canonical gravity.

## Direct prerequisite audit

| Need | Disposition |
|---|---|
| Partial derivatives, finite sums, ordinary ODE notation | Explicitly locally introduced in primer/examples; notation register expansion requested. |
| Lagrangian, regular Legendre transform, conjugate momentum, Hamiltonian | New primer + Hamiltonian definition. |
| Phase space / Poisson bracket | Repair existing definitions and full Hamiltonian concept. |
| Hamiltonian vector field / flow | New reusable definition and local derivation. |
| Constraint surface, canonical/total Hamiltonian | New definitions and constrained concept. |
| Weak equality, first-/second-class conditions | Repair existing definitions; conditions stated with constraint-set and regularity qualification. |
| Gauge orbit / gauge fixing | New definitions; global failures clearly excluded. |
| Lagrange multiplier | Repair existing definition to distinguish multiplier arbitrariness from a time parameter. |

## Source plan

Proposed sources are standard references suitable for verification during integration:

1. V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, DOI: `10.1007/978-1-4757-2063-1` — canonical mechanics and Hamiltonian flow.
2. P. A. M. Dirac, *Lectures on Quantum Mechanics*, Belfer Graduate School, ISBN: `9780486417134` — constrained Hamiltonian terminology.
3. M. Henneaux and C. Teitelboim, *Quantization of Gauge Systems*, Princeton University Press, ISBN: `9780691037691` — Dirac–Bergmann analysis, first/second class constraints, gauge fixing.
4. K. V. Kuchař, “Time and interpretations of quantum gravity,” in *Proceedings of the 4th Canadian Conference on General Relativity and Relativistic Astrophysics* (1992) — later context only; do not use the toy model as evidence for gravity.

The proposal retains `draft` status. Independent review should check sign conventions, the exact scope of gauge-generator wording, and links to the existing parametrized-particle page before integration.

## Link recommendations

- New primer `prerequisite-for` Hamiltonian Phase Space and Poisson Brackets.
- Hamiltonian Phase Space and Poisson Brackets `prerequisite-for` Classical Constrained Systems and `illustrates` its oscillator example.
- Classical Constrained Systems `prerequisite-for` Parametrized Particle and Dirac Quantization; `illustrates` its free-particle constraint-flow example.
- The free-particle example should have a labeled `related-to` link to existing `physics/parametrized-particle.md`, not silently replace its quantum sign-convention example.
- Definition nodes should have `related-to` edges to their owning concept. The main agent must reconcile whether a future standalone gauge-orbit/reduced-phase-space concept is needed; this package proposes definitions only.

## Integration blockers

1. The shared notation reference must be expanded before canonical use of the new symbols.
2. The learning path must accept the primer before Hamiltonian mechanics is presented as an unparented topic.
3. The current `constrained-systems` parent `operators-and-domains` needs removal after graph review; it is not a conceptual prerequisite for classical constrained mechanics.
4. The current `parametrized-particle.md` incorrectly links “conjugate momentum” to `def-phase-space`; a separate definition or corrected local text is needed. This package does not own the canonical repair.
5. No canonical source validation or independent review has been performed in this proposal-only work.
