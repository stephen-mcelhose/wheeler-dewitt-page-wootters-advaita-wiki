---
{
  "schema_version": "2.0",
  "id": "parametrized-particle",
  "type": "concept",
  "title": "Parametrized Particle",
  "summary": "A constrained toy model that separates gauge parameterization from relational evolution.",
  "review_status": "draft",
  "parents": [
    "constrained-systems"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "canonical-gravity"
    },
    {
      "type": "illustrates",
      "target": "dirac-quantization"
    },
    {
      "type": "related-to",
      "target": "def-phase-space"
    }
  ],
  "sources": [
    {
      "title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems",
      "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems",
      "persistent_id": "ISBN:9780691037691"
    },
    {
      "title": "E. Anderson, Problem of Time in Quantum Gravity",
      "url": "https://arxiv.org/abs/1206.2403",
      "persistent_id": "arXiv:1206.2403"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "constraint",
      "term": "constraint",
      "occurrence": "first"
    }
  ]
}
---
# Parametrized Particle

Treat Newtonian time \(t\) as a configuration variable with [conjugate momentum](../definitions/def-phase-space.md) \(p_t\). Reparametrization invariance produces the constraint \(C=p_t+H(q,p)\approx0\). Dirac quantization gives \((-i\hbar\partial_t+\hat H)\Psi(t,q)=0\), which is the Schrödinger equation after a sign convention is fixed.

This toy model shows why a constraint does not automatically mean “nothing happens.” It also displays assumptions that can fail in gravity: a globally usable clock, a simple deparametrization, and a tractable physical inner product.
