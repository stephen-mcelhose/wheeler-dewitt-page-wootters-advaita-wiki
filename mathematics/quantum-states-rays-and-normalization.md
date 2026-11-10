---
{
  "schema_version": "2.0",
  "id": "quantum-states-rays-and-normalization",
  "type": "concept",
  "title": "Quantum States, Rays, and Normalization",
  "summary": "How mathematical vectors represent pure physical quantum states.",
  "review_status": "ai_reviewed",
  "parents": [
    "hilbert-spaces"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "dirac-notation"
    },
    {
      "type": "related-to",
      "target": "def-normalization"
    },
    {
      "type": "related-to",
      "target": "def-ray"
    },
    {
      "type": "illustrates",
      "target": "example-quantum-states-rays-and-normalization"
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
      "definition_id": "ray",
      "term": "ray",
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

# Quantum States, Rays, and Normalization

A state vector is a mathematical representative used to describe a quantum system. A pure physical state is more precisely a [ray](../definitions/def-ray.md): nonzero vectors that differ by an overall nonzero complex scalar represent the same ray after the physical-state convention is imposed.

In practice one usually chooses a [normalized](../definitions/def-normalization.md) representative satisfying \(\langle\psi|\psi\rangle=1\). Multiplying a normalized representative by a global phase, \(|\psi\rangle\mapsto e^{i\theta}|\psi\rangle\), does not change the pure physical state.
