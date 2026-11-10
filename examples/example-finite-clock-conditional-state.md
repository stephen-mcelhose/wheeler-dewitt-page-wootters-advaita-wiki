---
{
  "schema_version": "2.0",
  "id": "example-finite-clock-conditional-state",
  "type": "example",
  "title": "Finite Clock: Conditional State from a Two-Branch Correlation",
  "summary": "A synthetic finite-dimensional example of conditioning a system state on a clock reading.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["derivation"],
  "modality": ["text"],
  "topics": ["finite-clock-model", "conditional-states", "composite-systems"],
  "teaches": ["take a partial inner product", "normalize a conditional state", "distinguish a conditional state from an unconditioned reduced state"],
  "prerequisites": ["composite-systems", "conditional-states", "finite-clock-model"],
  "action": "Project the clock factor onto each clock basis state, compute the norm of the resulting system vector, and normalize it.",
  "non_conclusion": "This two-branch correlation does not provide a continuous ideal clock, derive full Page–Wootters dynamics, or model full canonical gravity.",
  "relationships": [
    {"type": "illustrates", "target": "finite-clock-model"},
    {"type": "illustrates", "target": "conditional-states"}
  ],
  "sources": [
    {"title": "D. N. Page and W. K. Wootters, Evolution without evolution: Dynamics described by stationary observables", "url": "https://doi.org/10.1103/PhysRevD.27.2885", "persistent_id": "doi:10.1103/PhysRevD.27.2885"}
  ]
}
---

# Finite Clock: Conditional State from a Two-Branch Correlation

> This remains a downstream finite-clock illustration. For the measurement semantics separating effects, probabilities, conditional operators, and selective updates, see [Clock Effect: Probability, Conditional Operator, and Lüders Boundary](example-clock-effect-conditional-state.md).

Let the clock and system each have orthonormal two-state bases. Define the synthetic normalized global state

\[
|\Psi\rangle=\frac{1}{\sqrt2}\bigl(|0\rangle_C\otimes|0\rangle_S+|1\rangle_C\otimes|1\rangle_S\bigr).
\]

Conditioning on the clock result \(0\) gives

\[
({}_C\langle0|\otimes I_S)|\Psi\rangle=\frac{1}{\sqrt2}|0\rangle_S.
\]

Its squared norm is \(1/2\), so the normalized conditional system state is \(|0\rangle_S\). Conditioning on the clock result \(1\) analogously gives \(|1\rangle_S\).

By contrast, tracing out the clock gives the unconditioned reduced state

\[
\rho_S=\frac12|0\rangle\langle0|+\frac12|1\rangle\langle1|.
\]

This directly exhibits why a reduced state and a conditional state answer different questions.
