---
{
  "schema_version": "2.0",
  "id": "def-projector",
  "type": "definition",
  "title": "Projector",
  "summary": "An operator that keeps the component of a vector in a specified subspace; an orthogonal projector obeys P² = P and P† = P.",
  "review_status": "ai_reviewed",
  "parents": [],
  "relationships": [
    {
      "type": "related-to",
      "target": "projection-operators"
    }
  ],
  "sources": []
}
---
# Projector

A projector is an operator \(P\) satisfying \(P^2=P\). An orthogonal projector also satisfies \(P^\dagger=P\) and projects onto its target subspace along the orthogonal complement. For a normalized ket \(|a\rangle\), \(P_a=|a\rangle\langle a|\) is the rank-one orthogonal projector onto \(\operatorname{span}\{|a\rangle\}\).

Learn more: [Projection Operators](../mathematics/projection-operators.md).
