---
{
  "schema_version": "2.0",
  "id": "conditional-page-wootters-state",
  "type": "concept",
  "title": "Conditional Page–Wootters State",
  "summary": "The normalized system state relative to an idealized clock reading.",
  "review_status": "ai_reviewed",
  "parents": [
    "clock-states",
    "conditional-states",
    "composite-systems",
    "operators-and-domains"
  ],
  "relationships": [
    {
      "type": "derives-from",
      "target": "conditional-states"
    },
    {
      "type": "prerequisite-for",
      "target": "page-wootters-mechanism"
    },
    {
      "type": "uses",
      "target": "composite-systems"
    },
    {
      "type": "uses",
      "target": "operators-and-domains"
    },
    {
      "type": "related-to",
      "target": "def-clock-system-factorization"
    }
  ],
  "sources": [
    {
      "title": "D. N. Page and W. K. Wootters, Evolution without evolution: Dynamics described by stationary observables",
      "url": "https://doi.org/10.1103/PhysRevD.27.2885",
      "persistent_id": "doi:10.1103/PhysRevD.27.2885"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "clock-system-factorization",
      "term": "clock/system factorization",
      "occurrence": "first"
    }
  ]
}
---

# Conditional Page–Wootters State

For an idealized pure global state in the {{def:clock-system-factorization|clock/system factorization}} of the composite system, with the compatible-domain cautions of [Operators, Domains, and Self-Adjointness](../mathematics/operators-and-domains.md), define the unnormalized conditional vector \(|\widetilde\psi_S(t)\rangle=({}_C\langle t|\otimes I_S)|\Psi\rangle\). If its norm is nonzero and finite, define \(|\psi_S(t)\rangle=|\widetilde\psi_S(t)\rangle/\sqrt{\langle\widetilde\psi_S(t)|\widetilde\psi_S(t)\rangle}\).

With \(\hat C=\hat H_C\otimes I_S+I_C\otimes\hat H_S\), \(\hat C|\Psi\rangle=0\), and the clock convention from the preceding node, projecting with \({}_C\langle t|\otimes I_S\) gives \(-i\hbar\partial_t|\widetilde\psi_S(t)\rangle+\hat H_S|\widetilde\psi_S(t)\rangle=0\). Hence \(i\hbar\partial_t|\widetilde\psi_S(t)\rangle=\hat H_S|\widetilde\psi_S(t)\rangle\). This formal derivation assumes compatible domains, enough regularity to differentiate, and an ideal clock representation.
