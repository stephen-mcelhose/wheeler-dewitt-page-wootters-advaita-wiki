---
{
  "schema_version": "2.0",
  "id": "def-effect",
  "type": "definition",
  "title": "Measurement Effect",
  "summary": "A positive operator no larger than the identity that determines one outcome probability, but not its state update.",
  "review_status": "draft",
  "parents": [],
  "relationships": [{"type": "related-to", "target": "conditional-states"}],
  "sources": [{"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}]
}
---
# Measurement Effect

An effect \(E\) satisfies \(0\leq E\leq I\) and gives probability \(\operatorname{Tr}(E\rho)\) in state \(\rho\). An effect fixes statistics for that outcome, not a unique selective post-measurement state.

Learn more: [Measurements and Conditional States](../mathematics/conditional-states.md).
