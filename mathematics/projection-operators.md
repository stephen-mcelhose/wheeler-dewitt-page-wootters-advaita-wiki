---
{
  "schema_version": "2.0",
  "id": "projection-operators",
  "type": "concept",
  "title": "Projection Operators",
  "summary": "Operators that retain a specified subspace component; rank-one projectors model sharp yes/no alternatives.",
  "review_status": "ai_reviewed",
  "parents": [
    "dirac-notation"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "born-rule-and-quantum-probability"
    },
    {
      "type": "prerequisite-for",
      "target": "conditional-states"
    },
    {
      "type": "related-to",
      "target": "def-projector"
    },
    {
      "type": "illustrates",
      "target": "example-projection-operators-rank-and-orthogonality"
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
      "definition_id": "projector",
      "term": "projector",
      "occurrence": "first"
    }
  ]
}
---
# Projection Operators

A projector \(P\) is an operator satisfying \(P^2=P\). An **orthogonal projector** also satisfies \(P^\dagger=P\). It retains the component of a vector lying in its target subspace and removes the orthogonal component.

For a normalized ket \(|a\rangle\), the rank-one operator

\[
P_a=|a\rangle\langle a|
\]

is an orthogonal projector onto the one-dimensional direction spanned by \(|a\rangle\). Applied to an arbitrary ket \(|\psi\rangle\), it gives

\[
P_a|\psi\rangle=|a\rangle\langle a|\psi\rangle.
\]

The result is generally an unnormalized component. In the ideal sharp-measurement setting, the Born rule assigns the yes probability \(\langle\psi|P_a|\psi\rangle=|\langle a|\psi\rangle|^2\) for normalized \(|\psi\rangle\). A probability rule and a state-update rule are distinct; a later measurement model must specify the update assumptions.
