---
{
  "schema_version": "2.0",
  "id": "finite-clock-model",
  "type": "concept",
  "title": "Finite Clock Models",
  "summary": "Discrete clock models that make relational conditioning calculable before ideal time states are used.",
  "review_status": "ai_reviewed",
  "parents": [
    "conditional-states",
    "relational-observables",
    "constrained-clock-system-models"
  ],
  "relationships": [
    {
      "type": "contrasts-with",
      "target": "clock-states"
    },
    {
      "type": "related-to",
      "target": "clock-quality"
    },
    {
      "type": "related-to",
      "target": "def-effect"
    }
  ],
  "sources": [
    {
      "title": "D. N. Page and W. K. Wootters, Evolution without evolution: Dynamics described by stationary observables",
      "url": "https://doi.org/10.1103/PhysRevD.27.2885",
      "persistent_id": "doi:10.1103/PhysRevD.27.2885"
    },
    {
      "title": "M. Favalli and A. Smerzi, Time observables in a quantum universe",
      "url": "https://arxiv.org/abs/2003.09042",
      "persistent_id": "arXiv:2003.09042"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "effect",
      "term": "measurement effects",
      "occurrence": "first"
    },
    {
      "definition_id": "clock-quality",
      "term": "finite readout resolution",
      "occurrence": "first"
    }
  ]
}
---

# Finite Clock Models

For the cleared finite additive model, readouts are ordinary vectors or explicitly defined measurement effects; use clock-first tensor order and
\[
\hat C=\hat H_C\otimes I_S+I_C\otimes\hat H_S,
\qquad \hat C|\Psi\rangle=0.
\]
Let the selected clock sector have \(d\) equally spaced energies \(E_n=E_{\rm ref}+n\Delta E\), with \(n\in\{0,\ldots,d-1\}\), \(\Delta E=2\pi\hbar/T\), and readout labels \(\tau_k=\tau_0+kT/d\). Only system energy vectors satisfying \(\hat H_S|\epsilon_n\rangle=-E_n|\epsilon_n\rangle\) can be paired in a history state
\[
|\Psi\rangle=\sum_{n\in A}c_n|E_n\rangle_C\otimes|\epsilon_n\rangle_S.
\]
Thus nontrivial states require compatible clock and system spectral support; the matched sector \(A\) may be a proper subset of the system spectrum.

Two equivalent-looking readout conventions must not be mixed. The physical-energy kets are
\[
|\tau_k\rangle_{\rm phys}=\frac1{\sqrt d}\sum_{n=0}^{d-1}
 e^{-iE_n(\tau_k-\tau_0)/\hbar}|E_n\rangle,
\]
while the reference-energy-free Fourier kets are
\[
|\tau_k\rangle_{\rm rel}=\frac1{\sqrt d}\sum_{n=0}^{d-1}e^{-2\pi ink/d}|E_n\rangle,
\qquad
|\tau_k\rangle_{\rm phys}=e^{-iE_{\rm ref}(\tau_k-\tau_0)/\hbar}|\tau_k\rangle_{\rm rel}.
\]
Both are orthonormal readout bases in this finite model. The reference-free labels wrap exactly, \(|\tau_{k+d}\rangle_{\rm rel}=|\tau_k\rangle_{\rm rel}\), but physical clock evolution retains its reference phase:
\[
e^{-i\hat H_C(T/d)/\hbar}|\tau_k\rangle_{\rm rel}
=e^{-iE_{\rm ref}T/(d\hbar)}|\tau_{k+1}\rangle_{\rm rel}.
\]
For physical-energy kets, recurrence after \(T\) is exact only if \(e^{-iE_{\rm ref}T/\hbar}=1\); otherwise it is recurrence of rays. A finite readout is discrete and periodic, not an exact canonical time observable.

Conditioning with the physical-energy convention gives
\[
|\widetilde\psi_{\rm phys}(\tau_k)\rangle
=\frac1{\sqrt d}\sum_{n\in A}c_ne^{+iE_n(\tau_k-\tau_0)/\hbar}|\epsilon_n\rangle,
\qquad
|\widetilde\psi_{\rm phys}(\tau_{k+1})\rangle
=e^{-i\hat H_S T/(d\hbar)}|\widetilde\psi_{\rm phys}(\tau_k)\rangle.
\]
For reference-free conditioning, \(|\widetilde\psi_{\rm rel}(\tau_k)\rangle=e^{-iE_{\rm ref}(\tau_k-\tau_0)/\hbar}|\widetilde\psi_{\rm phys}(\tau_k)\rangle\), so its step operator is \(e^{-i(\hat H_S+E_{\rm ref}I_S)T/(d\hbar)}\). Crucially, the reference-free conditional vector is exactly periodic:
\[
|\widetilde\psi_{\rm rel}(\tau_k+T)\rangle=|\widetilde\psi_{\rm rel}(\tau_k)\rangle.
\]
The \(E_{\rm ref}\) cyclicity condition and ray-only qualification instead concern physical-energy ket/vector representatives. Normalize a conditional vector only when its norm is finite and positive.

Finite-dimensional clocks have {{def:clock-quality|finite readout resolution}} and, in this equally spaced model, cyclic recurrence. These model features let students calculate conditional states directly while making clear that “time” is supplied by selected clock–system correlations, not by a universal ideal observable.
