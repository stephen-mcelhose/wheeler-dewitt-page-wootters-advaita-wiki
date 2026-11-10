---
{
  "schema_version": "2.0",
  "id": "def-povm",
  "type": "definition",
  "title": "POVM",
  "summary": "A set of effects that sums to the identity, specifying generalized outcome probabilities but not selective updates.",
  "review_status": "draft",
  "parents": [],
  "relationships": [{"type": "related-to", "target": "conditional-states"}],
  "sources": [{"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}]
}
---
# POVM

A discrete POVM \(\{E_x\}_x\) consists of effects with \(\sum_xE_x=I\), so \(p(x)=\operatorname{Tr}(E_x\rho)\). It specifies probabilities only; an instrument is required to specify selective outcome updates.

Learn more: [Measurements and Conditional States](../mathematics/conditional-states.md).
