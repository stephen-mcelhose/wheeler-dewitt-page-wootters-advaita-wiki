---
{
  "schema_version": "2.0",
  "id": "clock-states",
  "type": "concept",
  "title": "Clock States and Sign Convention",
  "summary": "The idealized clock representation required to derive conditional Schrödinger evolution.",
  "review_status": "ai_reviewed",
  "parents": [
    "constrained-clock-system-models",
    "spectral-notation",
    "formal-and-physical-state-spaces"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "conditional-page-wootters-state"
    },
    {
      "type": "related-to",
      "target": "def-generalized-eigenvector"
    },
    {
      "type": "related-to",
      "target": "ideal-clock-state-family"
    },
    {
      "type": "related-to",
      "target": "covariant-time-povm"
    },
    {
      "type": "related-to",
      "target": "def-povm"
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
      "definition_id": "ideal-clock-state-family",
      "term": "idealized clock representation",
      "occurrence": "first"
    },
    {
      "definition_id": "covariant-time-povm",
      "term": "covariant POVMs",
      "occurrence": "first"
    },
    {
      "definition_id": "povm",
      "term": "POVMs",
      "occurrence": "first"
    }
  ]
}
---

# Clock States and Sign Convention

In an {{def:ideal-clock-state-family|idealized clock representation}} with a continuous clock label \(t\), choose the convention \({}_C\langle t|\hat H_C=-i\hbar\partial_t{}_C\langle t|\). The sign is a convention and must be kept consistent with the constraint.

The symbols \(|t\rangle\) are generally [generalized vectors](../definitions/def-generalized-eigenvector.md), not ordinary normalized states. For Hamiltonians with a lower-bounded spectrum, a universally self-adjoint time operator canonically conjugate to the Hamiltonian is not generally available; realistic clocks are instead approximate or described through {{def:covariant-time-povm|covariant POVMs}} and related operational {{def:povm|POVMs}}.
