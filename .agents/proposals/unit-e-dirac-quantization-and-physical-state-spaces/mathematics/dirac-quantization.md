---
{
  "schema_version": "2.0",
  "id": "dirac-quantization",
  "type": "concept",
  "title": "Dirac Quantization and Physical States",
  "summary": "A constrained-quantization program that separates a kinematical representation, formal quantum-constraint solutions, and a completed physical construction.",
  "review_status": "draft",
  "parents": ["constrained-systems", "operators-and-domains", "spectral-notation"],
  "relationships": [
    {"type": "prerequisite-for", "target": "formal-and-physical-state-spaces"},
    {"type": "prerequisite-for", "target": "dirac-quantization-gravity"},
    {"type": "illustrates", "target": "example-dirac-quantization-c3-formal-and-physical-spaces"},
    {"type": "related-to", "target": "def-kinematical-state"},
    {"type": "related-to", "target": "def-formal-constraint-solution"},
    {"type": "related-to", "target": "def-physical-state"},
    {"type": "related-to", "target": "def-physical-inner-product"},
    {"type": "related-to", "target": "def-factor-ordering"},
    {"type": "related-to", "target": "def-anomaly"}
  ],
  "sources": [
    {"title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems", "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems", "persistent_id": "ISBN:9780691037691"},
    {"title": "D. Giulini and D. Marolf, On the Generality of Refined Algebraic Quantization", "url": "https://arxiv.org/abs/gr-qc/9812024", "persistent_id": "arXiv:gr-qc/9812024"}
  ],
  "inline_definitions": [
    {"definition_id": "kinematical-state", "term": "kinematical state", "occurrence": "first"},
    {"definition_id": "formal-constraint-solution", "term": "formal constraint solution", "occurrence": "first"},
    {"definition_id": "physical-state", "term": "physical state", "occurrence": "first"},
    {"definition_id": "physical-inner-product", "term": "physical inner product", "occurrence": "first"},
    {"definition_id": "factor-ordering", "term": "factor ordering", "occurrence": "first"},
    {"definition_id": "anomaly", "term": "constraint anomaly", "occurrence": "first"}
  ]
}
---
# Dirac Quantization and Physical States

Dirac quantization is a program for quantizing a system whose classical description has constraints. One first chooses a **{{def:kinematical-state|kinematical state}}** representation, typically a Hilbert space \(\mathcal H_{\mathrm{kin}}\), and represents a suitable set of classical first-class constraints by operators \(\hat C_I\). At this stage, \(\mathcal H_{\mathrm{kin}}\) is an auxiliary arena; its vectors are not thereby physical states.

## The formal constraint condition

After domains have been specified, the formal Dirac condition is

\[
\hat C_I\,|\Psi\rangle=0\qquad\text{for every imposed constraint }I.
\]

Read this as “C hat sub I acting on ket capital psi equals zero.” It is meaningful only for vectors in the relevant operator domains. A **{{def:formal-constraint-solution|formal constraint solution}}** is an object that solves these equations in the stated representation or extension of it. The notation alone does not say whether that object is an ordinary vector, a distribution acting on a test space, or a normalizable physical state.

For a single bounded finite-dimensional operator, the displayed condition is equivalent to membership in its ordinary kernel. That useful special case must not be promoted to the general construction: realistic constraint operators may be unbounded, several constraints may require a common invariant domain, and zero can belong to continuous rather than point spectrum. Then solutions may be generalized or distributional rather than members of \(\mathcal H_{\mathrm{kin}}\).

## From formal solutions to physical states

A **{{def:physical-state|physical state}}** belongs to a completed physical construction: admissible solutions are selected or represented appropriately, gauge redundancy is addressed where relevant, and a **{{def:physical-inner-product|physical inner product}}** determines physical amplitudes and probabilities. The physical inner product is additional structure. It need not equal the restriction of the kinematical inner product, and it can be defined on a representation of solutions that is not a subspace of \(\mathcal H_{\mathrm{kin}}\).

A model-dependent rigging map is one refined-algebraic-quantization device for sending chosen test vectors to generalized solutions and inducing a physical pairing. This page does not assume that a rigging map exists, is unique, or is appropriate for every constraint system. Group averaging is likewise a construction with hypotheses, not an automatic consequence of writing \(\hat C_I|\Psi\rangle=0\).

## Consistency conditions are part of the program

The operator symbols \(\hat C_I\) require more than a classical formula with hats added:

- **Domains:** products and commutators must be defined on suitable common domains.
- **{{def:factor-ordering|Factor ordering}}:** noncommuting quantum factors can produce inequivalent candidate constraint operators.
- **Constraint relations:** a **{{def:anomaly|constraint anomaly}}** can obstruct the required quantum realization of the classical constraint algebra.
- **Physical interpretation:** boundary conditions, sectors, observables, and the physical inner product can affect which solutions and amplitudes are admissible.

These are not optional technical decorations; without enough of this structure, the displayed equation is a formal starting point rather than a completed quantum theory.

## Bounded finite model

The paired \(\mathbb C^3\) example, [Finite \(\mathbb C^3\) Constraint: Formal Kernel and Separately Declared Physical Pairing](../examples/example-dirac-quantization-c3-formal-and-physical-spaces.md), computes an ordinary kernel and then declares a positive pairing on it. Its purpose is to make the distinctions inspectable, not to supply a general algorithm for physical Hilbert spaces.

## What does not follow

It does not follow from \(\hat C_I|\Psi\rangle=0\) alone that \(|\Psi\rangle\) is normalizable in \(\mathcal H_{\mathrm{kin}}\), that all constraints have a common solution, that their commutators close, or that a physical inner product has been found. In particular, the physical state space does **not** generally equal an ordinary kernel in the kinematical Hilbert space.
