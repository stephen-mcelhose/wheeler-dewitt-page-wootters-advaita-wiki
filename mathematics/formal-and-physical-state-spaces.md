---
{
  "schema_version": "2.0",
  "id": "formal-and-physical-state-spaces",
  "type": "concept",
  "title": "Formal and Physical State Spaces",
  "summary": "A distinction among the kinematical representation, formal constraint solutions, and the space carrying physical amplitudes.",
  "review_status": "ai_reviewed",
  "parents": [
    "dirac-quantization"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "dirac-quantization-gravity"
    },
    {
      "type": "illustrates",
      "target": "example-dirac-quantization-c3-formal-and-physical-spaces"
    },
    {
      "type": "related-to",
      "target": "def-kinematical-state"
    },
    {
      "type": "related-to",
      "target": "def-formal-constraint-solution"
    },
    {
      "type": "related-to",
      "target": "def-physical-state"
    },
    {
      "type": "related-to",
      "target": "physical-inner-product"
    }
  ],
  "sources": [
    {
      "title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems",
      "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems",
      "persistent_id": "ISBN:9780691037691"
    },
    {
      "title": "D. Giulini and D. Marolf, On the Generality of Refined Algebraic Quantization",
      "url": "https://arxiv.org/abs/gr-qc/9812024",
      "persistent_id": "arXiv:gr-qc/9812024"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "kinematical-state",
      "term": "kinematical space",
      "occurrence": "first"
    },
    {
      "definition_id": "formal-constraint-solution",
      "term": "formal solution space",
      "occurrence": "first"
    },
    {
      "definition_id": "physical-inner-product",
      "term": "physical inner product",
      "occurrence": "first"
    },
    {
      "definition_id": "physical-state",
      "term": "physical state space",
      "occurrence": "first"
    }
  ]
}
---
# Formal and Physical State Spaces

Dirac quantization uses several spaces or representations that are easily conflated. Their distinction is structural, not merely a difference of names.

| Layer | What is specified | What has not automatically been supplied |
|---|---|---|
| **{{def:kinematical-state|Kinematical space}}** \(\mathcal H_{\mathrm{kin}}\) | A representation of candidate variables and candidate constraints. | Solutions of the constraints, gauge reduction, or physical amplitudes. |
| **{{def:formal-constraint-solution|Formal solution space}}** | Objects satisfying the quantum constraint condition in a stated domain or distributional extension. | A positive physical pairing or a completed observable interpretation. |
| **{{def:physical-state|Physical state space}}** \(\mathcal H_{\mathrm{phys}}\) | The admissible physical states together with a **{{def:physical-inner-product|physical inner product}}**, or an equivalent amplitude construction. | A universal formula for constructing it from arbitrary constraints. |

## Formal does not mean physical

Let \(\Phi\) be a selected test space in \(\mathcal H_{\mathrm{kin}}\), when such a choice is appropriate. Formal solutions may be elements of a dual space \(\Phi^*\), schematically

\[
\hat C_I\Psi=0,\qquad \Psi\in\Phi^*,
\]

rather than ordinary elements of \(\mathcal H_{\mathrm{kin}}\). This notation is deliberately schematic: the action on \(\Phi^*\), the test space, and the domain conditions must be stated in a particular model. The point is that a solution may have no finite kinematical norm, so simply restricting \(\langle\cdot|\cdot\rangle_{\mathrm{kin}}\) can be undefined or physically inappropriate.

A completed physical construction instead supplies a positive sesquilinear pairing, conventionally written

\[
\langle\Psi_1|\Psi_2\rangle_{\mathrm{phys}},
\]

on the chosen physical representatives (with null states quotiented and completion taken if the construction requires it). Read the subscript “phys” as identifying this pairing, not as asserting that it is inherited from the kinematical one.

## Why an ordinary kernel is not universal

If \(\hat C\) is a finite matrix, then \(\ker\hat C\subset\mathcal H_{\mathrm{kin}}\) is an ordinary finite-dimensional subspace. This is a pedagogical convenience. For unbounded operators, the expression \(\ker\hat C\) is domain-sensitive; if zero lies in continuous spectrum, ordinary Hilbert-space kernel vectors may be absent even though generalized solutions are relevant. With several constraints, compatibility and quantum closure must be settled before a joint solution condition is well posed.

Furthermore, even when an ordinary kernel exists, its inherited inner product is a choice requiring justification, not a theorem of the kernel equation. Gauge equivalence, orbit volume, boundary conditions, superselection sectors, and observable adjointness can matter to the physical pairing.

## Paired finite model and its boundary

The proposed paired \(\mathbb C^3\) example deliberately has the friendly coincidence

\[
\mathcal H_{\mathrm{form}}=\ker\hat C=\operatorname{span}\{|0\rangle\}\subset\mathcal H_{\mathrm{kin}}.
\]

It then separately declares \(\langle\alpha0|\beta0\rangle_{\mathrm{phys}}=7\alpha^*\beta\). The factor \(7\) makes the pedagogical point visible: the physical pairing is part of the model declaration, even when it is equivalent to a rescaling of the inherited finite pairing. Neither this kernel inclusion nor this simple pairing is a universal feature of constrained quantization.

## What does not follow

No displayed formal solution space establishes a physical inner product, a rigging map, an anomaly-free constraint representation, or a physical observable algebra. Conversely, a physical construction can require distributional solutions, quotients, or completions that are invisible in a finite null-space computation.
