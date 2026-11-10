---
{
  "schema_version": "2.0",
  "id": "clock-povms",
  "type": "concept",
  "title": "Clock POVMs and Operational Conditioning",
  "summary": "A finite-resolution formulation of clock readings and conditional quantum states.",
  "review_status": "draft",
  "parents": [
    "page-wootters-mechanism",
    "conditional-states",
    "clock-states"
  ],
  "relationships": [
    {
      "type": "limitation",
      "target": "page-wootters-mechanism"
    },
    {
      "type": "uses",
      "target": "conditional-states"
    },
    {
      "type": "related-to",
      "target": "def-povm"
    },
    {
      "type": "related-to",
      "target": "def-quantum-instrument"
    },
    {
      "type": "related-to",
      "target": "covariant-time-povm"
    },
    {
      "type": "related-to",
      "target": "clock-reading-and-external-time"
    }
  ],
  "sources": [
    {
      "title": "M. Favalli and A. Smerzi, Time observables in a quantum universe",
      "url": "https://arxiv.org/abs/2003.09042",
      "persistent_id": "arXiv:2003.09042"
    },
    {
      "title": "M. Ozawa, Quantum measuring processes of continuous observables",
      "url": "https://doi.org/10.1063/1.526000",
      "persistent_id": "doi:10.1063/1.526000"
    },
    {
      "title": "M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ],
  "inline_definitions": [
    {"definition_id":"povm","term":"POVM","occurrence":"first"},
    {"definition_id":"quantum-instrument","term":"instrument","occurrence":"first"},
    {"definition_id":"clock-reading-and-external-time","term":"clock outcome","occurrence":"first"},
    {"definition_id":"covariant-time-povm","term":"covariant time POVM","occurrence":"first"}
  ]
}
---

# Clock POVMs and Operational Conditioning

Using the {{def:povm|POVM}} and {{def:quantum-instrument|instrument}} distinction introduced in [Measurements and Conditional States](../mathematics/conditional-states.md), let a {{def:clock-reading-and-external-time|clock outcome}} \(x\) be represented by an effect \(E_x\). It determines the probability
\[
p(x)=\operatorname{Tr}[(E_x\otimes I_S)\rho_{CS}].
\]
When \(p(x)>0\), effect conditioning gives the system state
\[
\rho^{\rm effect}_{S|x}=
\frac{\operatorname{Tr}_C[(E_x\otimes I_S)\rho_{CS}]}{p(x)}.
\]
This is a conditioning rule for statistics. An effect alone does not specify a unique selective measurement update.

For a selective update, specify a clock instrument \(\{\mathcal I_x\}_x\). Each outcome map is completely positive and trace-nonincreasing, its associated effect is \(E_x=\mathcal I_x^*(I_C)\), and the aggregate \(\sum_x\mathcal I_x\) is trace preserving (with the corresponding integral condition for continuous outcomes). The selected conditional state is then
\[
\rho^{\rm inst}_{S|x}=
\frac{\operatorname{Tr}_C[(\mathcal I_x\otimes\mathrm{id}_S)(\rho_{CS})]}
{\operatorname{Tr}[(\mathcal I_x\otimes\mathrm{id}_S)(\rho_{CS})]}.
\]
After tracing out the clock, this clock-local instrument construction equals the displayed effect-conditioned system state for its associated \(E_x\). The effect still does not determine the selected joint output, residual clock state, disturbance account, or sequential statistics involving later clock measurements.

Finite resolution replaces exact idealized readings with intervals or smeared effects. A {{def:covariant-time-povm|covariant time POVM}} is one additional operational structure a clock model may specify; it prevents interpreting \(|t\rangle\) as a perfectly sharp physical state, but it does not by itself establish a full-gravity clock construction.
