---
{
  "schema_version": "2.0",
  "id": "conditional-states",
  "type": "concept",
  "title": "Measurements and Conditional States",
  "summary": "Finite-dimensional outcome probabilities, effect-conditioned system states, instrument-selective joint updates, and the ideal Lüders boundary.",
  "review_status": "ai_reviewed",
  "parents": [
    "composite-systems",
    "born-rule-and-quantum-probability"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "page-wootters-mechanism"
    },
    {
      "type": "illustrates",
      "target": "example-clock-effect-conditional-state"
    },
    {
      "type": "related-to",
      "target": "def-effect"
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
      "target": "def-conditional-state"
    },
    {
      "type": "contrasts-with",
      "target": "composite-systems"
    }
  ],
  "sources": [
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    },
    {
      "title": "M. Ozawa, Quantum measuring processes of continuous observables",
      "url": "https://doi.org/10.1063/1.526000",
      "persistent_id": "doi:10.1063/1.526000"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "effect",
      "term": "effect",
      "occurrence": "first"
    },
    {
      "definition_id": "povm",
      "term": "POVM",
      "occurrence": "first"
    },
    {
      "definition_id": "conditional-state",
      "term": "conditional state",
      "occurrence": "first"
    },
    {
      "definition_id": "quantum-instrument",
      "term": "quantum instrument",
      "occurrence": "first"
    }
  ]
}
---
# Measurements and Conditional States

## Probability is not an update

Work in finite dimensions. An outcome \(x\) is represented statistically by an {{def:effect|effect}} \(E_x\), with \(0\leq E_x\leq I\). In state \(\rho\), its probability is \(p(x)=\operatorname{Tr}(E_x\rho)\). A discrete {{def:povm|POVM}} \(\{E_x\}_x\) satisfies \(\sum_xE_x=I\), so it fixes outcome probabilities, but not a unique post-outcome update.

For a joint clock--system state \(\rho_{CS}\), a clock effect \(E_t\) has probability
\[
p(t)=\operatorname{Tr}_{CS}[(E_t\otimes I_S)\rho_{CS}].
\]
Read \(\operatorname{Tr}_{CS}\) as “trace over clock and system.” Normalization below is permitted only when \(p(t)>0\). At \(p(t)=0\), division does not define a conditional state.

## Effect-conditioned system state

The unnormalized conditional system operator is most transparently written in manifestly positive form:
\[
\widetilde\rho_{S|t}
=\operatorname{Tr}_C[(\sqrt{E_t}\otimes I_S)\rho_{CS}(\sqrt{E_t}\otimes I_S)].
\]
In this finite setting it equals \(\operatorname{Tr}_C[(E_t\otimes I_S)\rho_{CS}]\), by the factor-local partial-trace identity for operators acting only on \(C\). It is positive and has trace \(p(t)\). When \(p(t)>0\), the {{def:conditional-state|conditional state}} in this unit means the normalized system state
\[
\rho_{S|t}=\frac{\widetilde\rho_{S|t}}{p(t)}.
\]
It is not a claim about a selected joint post-measurement state or a disturbance mechanism.

By contrast, the unconditioned reduced state is \(\rho_S=\operatorname{Tr}_C(\rho_{CS})\): it ignores the clock outcome. For a finite discrete POVM, \(\rho_S=\sum_t p(t)\rho_{S|t}\). The reduced and conditional states therefore generally answer different questions.

## Instrument-selective joint update and the local marginal equality

A {{def:quantum-instrument|quantum instrument}} \(\{\mathcal I_t\}_t\) declares an outcome map and thus supplies selective-update information. In finite dimensions its maps are completely positive (the standard condition that positivity is retained even when an untouched ancillary system is included), trace-nonincreasing, and have trace-preserving aggregate. Its associated clock effect is
\[
E_t=\mathcal I_t^*(I_C),
\qquad
\operatorname{Tr}[A\mathcal I_t(\sigma)]
=\operatorname{Tr}[\mathcal I_t^*(A)\sigma],
\]
where \(\mathcal I_t^*\) is the trace-dual and \(\mathrm{id}_S\) is the identity map on \(S\).

For this clock-local instrument, the normalized selected **joint** output is
\[
\rho'_{CS|t}=\frac{(\mathcal I_t\otimes\mathrm{id}_S)(\rho_{CS})}{p(t)}
\quad (p(t)>0).
\]
Crucially, its system marginal agrees with the effect-conditioned system state:
\[
\operatorname{Tr}_C\rho'_{CS|t}=\rho_{S|t}.
\]
This finite clock-local equality follows from the trace-dual relation; an instrument with the same effect cannot give a different postselected system marginal after the clock is discarded. The effect nevertheless does **not** determine the selected joint state, residual clock state, disturbance account, or sequential statistics involving a later clock measurement. Nor does this statement cover an instrument acting jointly on \(C\) and \(S\).

## Ideal Lüders boundary

For an ideal sharp projective measurement with projectors \(\{P_t\}\), the Lüders instrument is \(\mathcal I_t(\sigma)=P_t\sigma P_t\). If \(\operatorname{Tr}(P_t\rho)>0\), its update is \(\rho\mapsto P_t\rho P_t/\operatorname{Tr}(P_t\rho)\). This is a scoped ideal-projective model, not a universal consequence of Born probabilities or an arbitrary effect.

A finite clock label \(t\) here is an outcome label, not an external time parameter or generalized continuous time ket. Later idealized Page--Wootters vectors require additional pure-state, clock-representation, domain, and normalization assumptions.
