---
{
  "schema_version": "2.0",
  "id": "norms-distance-and-convergence",
  "type": "concept",
  "title": "Norms, Distance, and Convergence",
  "summary": "The notions needed to make completeness meaningful.",
  "review_status": "ai_reviewed",
  "parents": [
    "inner-product-spaces"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "hilbert-spaces"
    },
    {
      "type": "related-to",
      "target": "def-cauchy-sequence"
    },
    {
      "type": "related-to",
      "target": "def-completeness"
    },
    {
      "type": "related-to",
      "target": "def-inner-product"
    },
    {
      "type": "related-to",
      "target": "def-norm"
    },
    {
      "type": "illustrates",
      "target": "example-norms-distance-cauchy-completeness"
    }
  ],
  "sources": [
    {
      "title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis",
      "url": "https://doi.org/10.1016/C2013-0-10329-X",
      "persistent_id": "doi:10.1016/C2013-0-10329-X"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "inner-product",
      "term": "inner product",
      "occurrence": "first"
    },
    {
      "definition_id": "norm",
      "term": "norm",
      "occurrence": "first"
    },
    {
      "definition_id": "completeness",
      "term": "Completeness",
      "occurrence": "first"
    }
  ]
}
---

# Norms, Distance, and Convergence

An [inner product](../definitions/def-inner-product.md) induces a [norm](../definitions/def-norm.md), \(\|\psi\|=\sqrt{\langle\psi|\psi\rangle}\). A norm induces a distance, \(d(\phi,\psi)=\|\phi-\psi\|\), which lets us say when vectors are close.

A sequence is [Cauchy](../definitions/def-cauchy-sequence.md) if, far enough along the sequence, its members become arbitrarily close to one another. A sequence converges if its members approach a specific limiting vector. [Completeness](../definitions/def-completeness.md) means that every Cauchy sequence converges to a vector still inside the same space.
