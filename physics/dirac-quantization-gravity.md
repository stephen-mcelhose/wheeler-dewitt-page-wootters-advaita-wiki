---
{
  "schema_version": "2.0",
  "id": "dirac-quantization-gravity",
  "type": "concept",
  "title": "Dirac Quantization in Canonical Gravity",
  "summary": "Formal imposition of local gravitational constraints on a kinematical representation.",
  "review_status": "draft",
  "parents": [
    "constraint-algebra",
    "dirac-quantization"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "wheeler-dewitt-formalism"
    },
    {
      "type": "related-to",
      "target": "def-factor-ordering"
    },
    {
      "type": "related-to",
      "target": "def-physical-state"
    }
  ],
  "sources": [
    {
      "title": "B. S. DeWitt, Quantum Theory of Gravity. I. The Canonical Theory",
      "url": "https://doi.org/10.1103/PhysRev.160.1113",
      "persistent_id": "doi:10.1103/PhysRev.160.1113"
    },
    {
      "title": "E. Anderson, Problem of Time in Quantum Gravity",
      "url": "https://arxiv.org/abs/1206.2403",
      "persistent_id": "arXiv:1206.2403"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "factor-ordering",
      "term": "factor ordering",
      "occurrence": "first"
    },
    {
      "definition_id": "physical-state",
      "term": "physical states",
      "occurrence": "first"
    }
  ]
}
---
# Dirac Quantization in Canonical Gravity

A canonical quantization begins with a kinematical representation and seeks quantum representatives of the local constraints. In the bounded ADM/WDW treatment, this is only a formal vacuum program: a physical construction must address their domains, [factor ordering](../definitions/def-factor-ordering.md), regulator dependence, closure, and physical inner product.

The quantum theory is not defined merely by writing down a formal constraint equation. In particular, [physical states](../definitions/def-physical-state.md) may be distributional and need not inherit a usable inner product from \(\mathcal H_{\mathrm{kin}}\). No defined full Wheeler–DeWitt operator, quantum constraint closure, solution space, physical inner product, or observable algebra follows from the displayed formal constraints.
