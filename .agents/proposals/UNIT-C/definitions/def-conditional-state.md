---
{
  "schema_version": "2.0",
  "id": "def-conditional-state",
  "type": "definition",
  "title": "Conditional State",
  "summary": "A normalized state assigned relative to a stated condition or selected outcome with positive probability and a declared conditioning prescription.",
  "review_status": "draft",
  "parents": [],
  "relationships": [{"type": "related-to", "target": "conditional-states"}, {"type": "contrasts-with", "target": "composite-systems"}],
  "sources": [{"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}]
}
---
# Conditional State

A conditional state is normalized relative to a declared event or condition whose probability is positive. For a clock effect \(E_t\), effect conditioning gives \(\rho^{\mathrm{eff}}_{S|t}=\operatorname{Tr}_C[(E_t\otimes I_S)\rho_{CS}]/p(t)\); an instrument-defined post-measurement state requires the instrument as additional data.

Learn more: [Measurements and Conditional States](../mathematics/conditional-states.md).
