---
{
  "schema_version": "2.0",
  "id": "def-quantum-instrument",
  "type": "definition",
  "title": "Quantum Instrument",
  "summary": "A family of completely positive outcome maps that fixes both outcome probabilities and selective post-measurement states.",
  "review_status": "draft",
  "parents": [],
  "relationships": [{"type": "related-to", "target": "conditional-states"}],
  "sources": [{"title": "M. Ozawa, Quantum measuring processes of continuous observables", "url": "https://doi.org/10.1063/1.526000", "persistent_id": "doi:10.1063/1.526000"}]
}
---
# Quantum Instrument

A discrete instrument \(\{\mathcal I_x\}_x\) has completely positive, trace-nonincreasing maps with trace-preserving aggregate \(\sum_x\mathcal I_x\). Its effect is \(E_x=\mathcal I_x^*(I)\), and, when \(\operatorname{Tr}\mathcal I_x(\rho)>0\), its normalized output gives the selective post-measurement state.

Learn more: [Measurements and Conditional States](../mathematics/conditional-states.md).
