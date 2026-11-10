---
{
  "schema_version": "2.0",
  "id": "def-povm",
  "type": "definition",
  "title": "POVM",
  "summary": "Positive-Operator-Valued Measure: a family of effects summing to the identity that represents generalized measurement outcome probabilities.",
  "review_status": "ai_reviewed",
  "parents": [],
  "relationships": [
    {
      "type": "related-to",
      "target": "conditional-states"
    }
  ],
  "sources": [
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ]
}
---
# POVM

**POVM** stands for **Positive-Operator-Valued Measure**. A discrete POVM is a family \(\{E_x\}_x\) of measurement effects satisfying

\[
0\leq E_x\leq I,
\qquad
\sum_xE_x=I.
\]

For a density operator \(\rho\), the probability of outcome \(x\) is

\[
p(x)=\operatorname{Tr}(E_x\rho).
\]

A POVM fixes outcome probabilities, but it does not by itself fix post-measurement states; a quantum instrument supplies the outcome-specific update maps.

Learn more: [Measurements and Conditional States](../mathematics/conditional-states.md).
