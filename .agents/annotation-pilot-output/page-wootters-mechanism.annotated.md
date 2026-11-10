---
{
  "schema_version": "2.0",
  "id": "page-wootters-mechanism",
  "type": "concept",
  "title": "Page–Wootters Mechanism",
  "summary": "A relational-time construction in which conditional subsystem dynamics arise from correlations in a constrained global state.",
  "review_status": "ai_reviewed",
  "parents": [
    "conditional-page-wootters-state",
    "problem-of-time"
  ],
  "relationships": [
    {
      "type": "uses",
      "target": "clock-states"
    },
    {
      "type": "uses",
      "target": "conditional-page-wootters-state"
    },
    {
      "type": "limitation",
      "target": "page-wootters-limitations"
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
    },
    {
      "title": "M. Favalli and A. Smerzi, Time observables in a quantum universe",
      "url": "https://arxiv.org/abs/2003.09042",
      "persistent_id": "arXiv:2003.09042"
    },
    {
      "title": "E. Anderson, Problem of Time in Quantum Gravity",
      "url": "https://arxiv.org/abs/1206.2403",
      "persistent_id": "arXiv:1206.2403"
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

# Page–Wootters Mechanism

Page and Wootters (1983) introduced a relational/conditional-time proposal in constrained quantum mechanics. The presentation here is a modern, bounded constrained-model formulation; it is not a completed quantization of gravity.

At the model level, choose a {{def:clock-system-factorization|clock/system factorization}} \(\mathcal H_{CS}=\mathcal H_C\widehat\otimes\mathcal H_S\) and a constraint \(\hat C=\hat H_C\otimes I_S+I_C\otimes\hat H_S\). The Page–Wootters setup selects global states satisfying \(\hat C|\Psi\rangle=0\). Nontrivial states require compatible clock and system spectral support: under this additive-plus convention, a clock energy \(E\) must be paired with a system sector at \(-E\). In continuous-spectrum models, such constraint solutions can be generalized rather than normalizable kinematical vectors, so a physical inner product and conditioning construction must be specified rather than presumed.

The mechanism does not say that every bipartite Hamiltonian yields relational time. It requires a clock choice, a suitable constraint, matched spectral correlations, and a conditioning prescription. Finite, operational, and ideal-clock descriptions make different additional assumptions. It is a relational-time framework for certain constrained quantum models, not a complete resolution of the full canonical-gravity problem of time.
