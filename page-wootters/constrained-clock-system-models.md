---
{
  "schema_version": "2.0",
  "id": "constrained-clock-system-models",
  "type": "concept",
  "title": "Constrained Clock–System Models",
  "summary": "The selected bipartite constrained models in which Page–Wootters correlations can support relational clock readings.",
  "review_status": "ai_reviewed",
  "parents": [
    "conditional-states",
    "relational-observables"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "finite-clock-model"
    },
    {
      "type": "prerequisite-for",
      "target": "page-wootters-mechanism"
    },
    {
      "type": "related-to",
      "target": "constrained-history-state"
    }
  ],
  "sources": [
    {
      "title": "D. N. Page and W. K. Wootters, Evolution without evolution: Dynamics described by stationary observables",
      "url": "https://doi.org/10.1103/PhysRevD.27.2885",
      "persistent_id": "doi:10.1103/PhysRevD.27.2885"
    },
    {
      "title": "M. P. Woods, R. Silva, and J. Oppenheim, Autonomous Quantum Machines and Finite-Sized Clocks",
      "url": "https://arxiv.org/abs/1607.04591",
      "persistent_id": "arXiv:1607.04591"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "clock-system-factorization",
      "term": "clock-system factorization",
      "occurrence": "first"
    },
    {
      "definition_id": "constrained-history-state",
      "term": "constrained history state",
      "occurrence": "first"
    }
  ]
}
---
# Constrained Clock–System Models

A Page–Wootters model begins by selecting a {{def:clock-system-factorization|clock-system factorization}}: a tensor-factor description with one factor designated as a clock and another as a system. This is a model choice, not a consequence of every composite quantum system. The choice can be useful when a clock readout and system quantities can be correlated, but it may be nonunique or unavailable in a constrained theory.

The standard pedagogical setting uses a noninteracting additive constraint: the clock contribution and system contribution are added, with each acting on its selected factor. A global state satisfying that constraint can define a {{def:constrained-history-state|constrained history state}} with correlated clock and system energy sectors. Conceptually, an allowed clock-energy contribution is paired with a compensating system-energy contribution, so the total constrained value is fixed. This energy correlation is stronger than arbitrary entanglement and is part of the model’s dynamical input.

Finite or discrete clock choices make the construction more concrete. A clock may have finitely many distinguishable readouts and a discrete spectrum, which limits resolution and usually makes recurrence or periodicity unavoidable. Recurrence is a feature of the selected finite model; it is not evidence that physical time is universally periodic, nor does it turn a finite readout into an ideal time observable.

These are constrained bipartite quantum models, not local full-general-relativity constraints. Full canonical gravity has constraints at spatial points, diffeomorphism structure, and unresolved questions about quantum constraint closure, physical states, and global clock choices. A successful clock/system construction therefore illustrates relational conditioning in its declared model; it does not supply a general reduction of full gravity or resolve all problems of time.
