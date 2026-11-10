---
{
  "schema_version": "2.0",
  "id": "born-rule-and-quantum-probability",
  "type": "concept",
  "title": "Born Rule and Quantum Probability",
  "summary": "The measurement rule that turns amplitudes and projectors into probabilities.",
  "review_status": "ai_reviewed",
  "parents": [
    "dirac-notation",
    "projection-operators"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "conditional-states"
    },
    {
      "type": "related-to",
      "target": "def-inner-product"
    },
    {
      "type": "related-to",
      "target": "def-projector"
    },
    {
      "type": "related-to",
      "target": "def-normalization"
    },
    {
      "type": "related-to",
      "target": "def-overlap"
    },
    {
      "type": "illustrates",
      "target": "example-born-rule-amplitudes-probabilities-and-luders-update"
    }
  ],
  "sources": [
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "inner-product",
      "term": "inner product",
      "occurrence": "first"
    },
    {
      "definition_id": "projector",
      "term": "projector",
      "occurrence": "first"
    },
    {
      "definition_id": "normalization",
      "term": "normalized",
      "occurrence": "first"
    }
  ]
}
---

# Born Rule and Quantum Probability

The [inner product](../definitions/def-inner-product.md) supplies amplitudes and norms, but probabilities enter through a measurement rule. For a normalized state \(|\psi\rangle\) and an orthogonal [projector](../definitions/def-projector.md) \(P\), the Born rule assigns
\[
p(P)=\langle\psi|P|\psi\rangle.
\]
For a basis state \(|a\rangle\), the probability of the corresponding sharp outcome is \(|\langle a|\psi\rangle|^2\). State update is a separate rule and is treated later with measurements and conditional states.
