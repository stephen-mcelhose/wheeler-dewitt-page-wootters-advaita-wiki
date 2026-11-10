---
{
  "schema_version": "2.0",
  "id": "example-clock-effect-conditional-state",
  "type": "example",
  "title": "Clock Effect: Probability, Conditional Operator, and Lüders Boundary",
  "summary": "A finite two-branch clock--system calculation separating a clock effect's probability and effect-conditioned state from an instrument-defined selective update.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["derivation", "comparison"],
  "modality": ["text", "code"],
  "topics": ["conditional-states"],
  "teaches": ["calculate an effect probability", "form an unnormalized conditional operator", "normalize only at positive probability", "distinguish conditional and reduced states", "state the Lüders-instrument boundary"],
  "prerequisites": ["born-rule-and-quantum-probability", "composite-systems", "conditional-states"],
  "action": "For a two-branch clock--system state, calculate a clock-effect probability, its unnormalized and normalized conditional system operators, compare them with the reduced state, and identify the additional instrument assumption needed for a Lüders update.",
  "non_conclusion": "This discrete ideal projective model neither gives a general POVM update nor a continuous ideal clock, an interacting measurement model, a Page--Wootters dynamical derivation, or a full-gravity clock construction.",
  "relationships": [{"type": "illustrates", "target": "conditional-states"}],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"},
    {"title": "M. Ozawa, Quantum measuring processes of continuous observables", "url": "https://doi.org/10.1063/1.526000", "persistent_id": "doi:10.1063/1.526000"}
  ]
}
---
# Clock Effect: Probability, Conditional Operator, and Lüders Boundary

## Prerequisites and local setup

Assume the finite composite-system model of [Composite Quantum Systems](../mathematics/composite-systems.md) and the effect/instrument distinction of [Measurements and Conditional States](../mathematics/conditional-states.md). Let the clock \(C\) and system \(S\) each have the ordered basis \((|0\rangle,|1\rangle)\); product states use the order \(C\) then \(S\).

**Model scope:** take the normalized correlated state
\[
|\Psi\rangle=\frac{|0\rangle_C|0\rangle_S+|1\rangle_C|1\rangle_S}{\sqrt2},
\qquad \rho_{CS}=|\Psi\rangle\langle\Psi|.
\]
Treat the clock label \(t=0\) as a discrete outcome label, not an external time parameter. Use the sharp clock effect
\[
E_0=|0\rangle_C\langle0|.
\]
It is an effect because \(0\leq E_0\leq I_C\). Together with \(E_1=|1\rangle\langle1|\), it forms the ideal two-outcome clock-basis POVM.

## 1. The effect supplies an outcome probability

The probability of the clock effect \(E_0\) is
\[
\begin{aligned}
p(0)
&=\operatorname{Tr}_{CS}[(E_0\otimes I_S)\rho_{CS}]\\
&=\langle\Psi|(E_0\otimes I_S)|\Psi\rangle\\
&=\frac12.
\end{aligned}
\]
This number answers “how often would this outcome occur in the stated state and measurement statistics?” It does not yet state what the post-outcome joint state is.

## 2. Unnormalized then normalized effect-conditioned operator

The unnormalized conditional system operator is
\[
\begin{aligned}
\widetilde\rho^{\mathrm{eff}}_{S|0}
&=\operatorname{Tr}_C[(E_0\otimes I_S)\rho_{CS}]\\
&=\frac12|0\rangle_S\langle0|.
\end{aligned}
\]
Its trace is \(1/2=p(0)\). Since this conditioning probability is strictly positive, divide by it:
\[
\rho^{\mathrm{eff}}_{S|0}
=\frac{\widetilde\rho^{\mathrm{eff}}_{S|0}}{p(0)}
=|0\rangle_S\langle0|.
\]
If \(p(0)=0\), the unnormalized operator can still be calculated but the normalized expression is undefined. A zero-probability outcome must not be assigned a normalized conditional state by this formula.

## 3. It is not the reduced state

Without selecting a clock effect, trace out the whole clock factor:
\[
\rho_S=\operatorname{Tr}_C(\rho_{CS})
=\frac12|0\rangle\langle0|+\frac12|1\rangle\langle1|
=\frac12 I_S.
\]
The reduced state is unconditioned. In this example it is the probability-weighted average of effect-conditioned states:
\[
\rho_S=p(0)\rho^{\mathrm{eff}}_{S|0}+p(1)\rho^{\mathrm{eff}}_{S|1}.
\]
Thus \(|0\rangle\langle0|\) answers a question conditional on a selected clock outcome, whereas \(I_S/2\) answers the system-only question when the clock outcome is ignored.

## 4. Ideal Lüders instrument: an extra assumption

The effect \(E_0\) alone does not select a unique physical state-update map. For this particular ideal sharp-projective model, add the **Lüders-instrument assumption**
\[
\mathcal I_0(\sigma)=E_0\sigma E_0,
\qquad
\mathcal I_1(\sigma)=E_1\sigma E_1.
\]
These completely positive maps are trace-nonincreasing and their sum is trace preserving. The selected joint post-outcome state is then
\[
\rho'_{CS|0}
=\frac{(\mathcal I_0\otimes\mathrm{id}_S)(\rho_{CS})}{p(0)}
=|0\rangle_C|0\rangle_S\langle0|_C\langle0|_S.
\]
Tracing out \(C\) yields \(|0\rangle_S\langle0|\), agreeing here with the effect-conditioned system state. This agreement is a feature of this sharp Lüders model, not a license to infer an instrument from an arbitrary effect or POVM.

## 5. Pedagogical Go check

```go
package main

import "fmt"

type SystemDensity2D [2][2]complex128

// Given: unnormalized is positive semidefinite and has trace equal to the selected
// outcome probability p. Model scope: this helper only normalizes a 2×2 system operator.
// A normalized conditional state exists only when p is strictly positive.
func normalizeConditionalSystem2D(unnormalized SystemDensity2D, p float64) (SystemDensity2D, error) {
    if p <= 0 {
        return SystemDensity2D{}, fmt.Errorf("conditional state undefined: conditioning probability is not positive")
    }
    var normalized SystemDensity2D
    for i := 0; i < 2; i++ {
        for j := 0; j < 2; j++ {
            normalized[i][j] = unnormalized[i][j] / complex(p, 0)
        }
    }
    return normalized, nil
}

func main() {
    // Illustration: E_0 conditioning of the stated Bell correlation gives ½|0⟩⟨0|.
    unnormalizedAtZero := SystemDensity2D{{0.5, 0}, {0, 0}}
    conditionalAtZero, err := normalizeConditionalSystem2D(unnormalizedAtZero, 0.5)
    fmt.Println(conditionalAtZero, err)
    // [[(1+0i) (0+0i)] [(0+0i) (0+0i)]] <nil>
}
```

## What this example does and does not show

This example distinguishes an effect's probability, an unnormalized conditional operator, a normalized state at positive conditioning probability, and an instrument-dependent selective update. It does not show that all effects imply the Lüders update, model general detectors or continuous outcomes, derive time evolution, or identify the clock outcome with a physical time observable in full constrained gravity.
