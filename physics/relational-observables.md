---
{
  "schema_version": "2.0",
  "id": "relational-observables",
  "type": "concept",
  "title": "Relational and Complete Observables",
  "summary": "Physical predictions formulated as correlations among dynamical degrees of freedom.",
  "review_status": "draft",
  "parents": [
    "problem-of-time",
    "constrained-systems",
    "dirac-quantization"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "page-wootters-mechanism"
    },
    {
      "type": "related-to",
      "target": "def-complete-observable"
    },
    {
      "type": "related-to",
      "target": "def-deparametrization"
    },
    {
      "type": "related-to",
      "target": "def-partial-observable"
    }
  ],
  "sources": [
    {
      "title": "E. Anderson, Problem of Time in Quantum Gravity",
      "url": "https://arxiv.org/abs/1206.2403",
      "persistent_id": "arXiv:1206.2403"
    },
    {
      "title": "K. Kuchař, Time and Interpretations of Quantum Gravity",
      "url": "https://doi.org/10.1142/9789812385123_0009",
      "persistent_id": "doi:10.1142/9789812385123_0009"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "partial-observable",
      "term": "partial observable",
      "occurrence": "first"
    },
    {
      "definition_id": "complete-observable",
      "term": "complete or Dirac observable",
      "occurrence": "first"
    },
    {
      "definition_id": "deparametrization",
      "term": "deparametrized model",
      "occurrence": "first"
    }
  ]
}
---
# Relational and Complete Observables

A [first-class constrained-system](../mathematics/constrained-systems.md) description distinguishes quantities defined on kinematical phase space from gauge-invariant predictions. A [partial observable](../definitions/def-partial-observable.md) is a quantity that can be specified operationally but need not commute with all constraints. A [complete or Dirac observable](../definitions/def-complete-observable.md) is constructed to be gauge invariant, at least weakly, under the constraints; the relevant physical-state issues are introduced in [Dirac Quantization](dirac-quantization-gravity.md).

In a successfully [deparametrized model](../definitions/def-deparametrization.md), one may express relational evolution of a quantity \(F\) with a reduced Hamiltonian \(H_{\mathrm{red}}\) as \(O_F(\tau)=e^{i\hat H_{\mathrm{red}}\tau/\hbar}\hat F e^{-i\hat H_{\mathrm{red}}\tau/\hbar}\). This formula presupposes a good reduction, gauge choice, and reduced Hamiltonian; it should not be treated as a general full-GR result.
