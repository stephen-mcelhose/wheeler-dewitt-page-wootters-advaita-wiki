---
{
  "schema_version": "2.0",
  "id": "conditional-states",
  "type": "concept",
  "title": "Measurements and Conditional States",
  "summary": "Finite-dimensional outcome probabilities, effect conditioning, instrument-selective conditional states, and the ideal Lüders boundary.",
  "review_status": "draft",
  "parents": ["composite-systems", "born-rule-and-quantum-probability"],
  "relationships": [
    {"type": "prerequisite-for", "target": "page-wootters-mechanism"},
    {"type": "illustrates", "target": "example-clock-effect-conditional-state"},
    {"type": "related-to", "target": "def-effect"},
    {"type": "related-to", "target": "def-povm"},
    {"type": "related-to", "target": "def-quantum-instrument"},
    {"type": "related-to", "target": "def-conditional-state"},
    {"type": "contrasts-with", "target": "composite-systems"}
  ],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"},
    {"title": "M. Ozawa, Quantum measuring processes of continuous observables", "url": "https://doi.org/10.1063/1.526000", "persistent_id": "doi:10.1063/1.526000"}
  ],
  "inline_definitions": [
    {"definition_id": "effect", "term": "effect", "occurrence": "first"},
    {"definition_id": "povm", "term": "POVM", "occurrence": "first"},
    {"definition_id": "conditional-state", "term": "conditional state", "occurrence": "first"},
    {"definition_id": "quantum-instrument", "term": "quantum instrument", "occurrence": "first"}
  ]
}
---
# Measurements and Conditional States

## Probability is not an update

Work first in finite dimensions. A measurement outcome \(x\) is represented statistically by an {{def:effect|effect}} \(E_x\), an operator satisfying \(0\leq E_x\leq I\). For a state \(\rho\), its probability is
\[
p(x)=\operatorname{Tr}(E_x\rho).
\]
A discrete {{def:povm|POVM}} is a set \(\{E_x\}_x\) of effects with \(\sum_xE_x=I\). Therefore it determines outcome probabilities. It does **not** by itself determine a unique state after an outcome is selected: different physical measurement implementations can share the same POVM while producing different post-outcome states.

For a joint clock--system state \(\rho_{CS}\), a clock effect \(E_t\) has probability
\[
p(t)=\operatorname{Tr}_{CS}[(E_t\otimes I_S)\rho_{CS}].
\]
Read \(\operatorname{Tr}_{CS}\) as “trace over clock and system.” The denominator in every normalized conditioning formula below must satisfy \(p(t)>0\). If \(p(t)=0\), the normalized conditional state is undefined; assigning one by division would be invalid.

## Effect conditioning: a conditional system operator

Given only the joint state and a clock effect, define the unnormalized conditional system operator
\[
\widetilde\rho^{\mathrm{eff}}_{S|t}
=\operatorname{Tr}_C[(E_t\otimes I_S)\rho_{CS}].
\]
It is positive and has trace \(p(t)\). When \(p(t)>0\), the corresponding {{def:conditional-state|conditional state}} is
\[
\rho^{\mathrm{eff}}_{S|t}
=\frac{\widetilde\rho^{\mathrm{eff}}_{S|t}}{p(t)}.
\]
This is a conditional state associated with the displayed effect and joint state. It is not, by itself, a claim about the physical disturbance or post-measurement state of the clock: an effect encodes outcome statistics, not a selective update.

By contrast, the unconditioned reduced state is
\[
\rho_S=\operatorname{Tr}_C(\rho_{CS}).
\]
It averages over the clock factor without selecting \(t\). The two agree only in special cases. For a POVM \(\{E_t\}\), \(\rho_S=\sum_t p(t)\rho^{\mathrm{eff}}_{S|t}\) in the finite discrete model.

## Instrument-selective conditioning

A {{def:quantum-instrument|quantum instrument}} \(\{\mathcal I_t\}_t\) supplies the missing update information. Each \(\mathcal I_t\) is completely positive and trace-nonincreasing, its associated effect is
\[
E_t=\mathcal I_t^*(I_C),
\]
and the aggregate \(\sum_t\mathcal I_t\) is trace preserving. Here \(\mathcal I_t^*\) is the trace-dual map, defined by \(\operatorname{Tr}[A\mathcal I_t(\sigma)]=\operatorname{Tr}[\mathcal I_t^*(A)\sigma]\).

The selected joint output is \((\mathcal I_t\otimes\mathrm{id}_S)(\rho_{CS})\). Its trace is the same outcome probability \(p(t)\), and when \(p(t)>0\) the system state after that specified selective update is
\[
\rho^{\mathrm{inst}}_{S|t}=
\frac{\operatorname{Tr}_C[(\mathcal I_t\otimes\mathrm{id}_S)(\rho_{CS})]}{p(t)}.
\]
Thus the superscripts “eff” and “inst” name two distinct constructions. They need not agree for a general instrument. A page must name which construction it uses rather than writing \(\rho_{S|t}\) ambiguously.

## Ideal Lüders boundary

For an ideal sharp projective measurement with orthogonal projectors \(\{P_t\}\), the Lüders instrument is \(\mathcal I_t(\sigma)=P_t\sigma P_t\). If the selected outcome has \(\operatorname{Tr}(P_t\rho)>0\), its normalized post-measurement state is
\[
\rho\longmapsto\frac{P_t\rho P_t}{\operatorname{Tr}(P_t\rho)}.
\]
This is a special ideal-projective model, not a universal update rule and not a consequence of the Born probability alone. General POVMs, nonideal detectors, indirect measurements, and continuous outcomes require an explicitly supplied instrument; continuous outcomes additionally require a measure-theoretic formulation.

## Clock scope

A clock label \(t\) in this finite-dimensional discussion is an outcome label, not yet an external time parameter or a generalized continuous time ket. This construction supports later operational Page--Wootters discussions only after their clock model, tensor factorization, constraint assumptions, and conditioning convention have been stated. It does not establish a full-gravity clock construction or solve the problem of time.
