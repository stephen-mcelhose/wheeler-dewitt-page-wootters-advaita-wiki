---
{
  "schema_version": "2.0",
  "id": "example-clock-effect-conditional-state",
  "type": "example",
  "title": "Clock Effect: Probability, Conditional Operator, and Lüders Boundary",
  "summary": "A finite two-qubit calculation separating clock-effect probability, conditional system state, reduced state, and an instrument-defined joint update.",
  "review_status": "ai_reviewed",
  "status": [
    "synthetic"
  ],
  "patterns": [
    "derivation",
    "comparison"
  ],
  "modality": [
    "text",
    "code"
  ],
  "topics": [
    "conditional-states"
  ],
  "teaches": [
    "calculate an effect probability",
    "form an unnormalized conditional operator",
    "normalize only at positive probability",
    "distinguish conditional and reduced states",
    "scope an ideal Lüders update"
  ],
  "prerequisites": [
    "born-rule-and-quantum-probability",
    "composite-systems",
    "conditional-states"
  ],
  "action": "Calculate p(0), the unnormalized and normalized conditional system operators, the reduced state, and the extra instrument assumption behind a Lüders joint update.",
  "non_conclusion": "This discrete ideal projective model does not provide a general POVM update, a continuous ideal clock, an interacting measurement model, a Page--Wootters dynamical derivation, or a full-gravity clock construction.",
  "relationships": [
    {
      "type": "illustrates",
      "target": "conditional-states"
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
  ]
}
---
# Clock Effect: Probability, Conditional Operator, and Lüders Boundary

## Prerequisites and local setup

Let \(C\) and \(S\) each have declared orthonormal bases \((|0\rangle,|1\rangle)\). Their tensor factors are ordered \(C:S\); if a four-component coordinate representation is needed, use \((|00\rangle,|01\rangle,|10\rangle,|11\rangle)_{C:S}\). Take
\[
|\Psi\rangle=\frac{|0\rangle_C|0\rangle_S+|1\rangle_C|1\rangle_S}{\sqrt2},\qquad
\rho_{CS}=|\Psi\rangle\langle\Psi|.
\]
**Model scope:** \(t=0\) is a discrete clock outcome label, not an external time parameter. The sharp clock effect is \(E_0=|0\rangle_C\langle0|\), with \(E_1=|1\rangle_C\langle1|\).

## Probability, unnormalized operator, and conditional state

The effect supplies a scalar probability:
\[
p(0)=\operatorname{Tr}_{CS}[(E_0\otimes I_S)\rho_{CS}]=\frac12.
\]
It does not yet specify a joint post-outcome state. The unnormalized conditional **system operator** is
\[
\widetilde\rho_{S|0}=\operatorname{Tr}_C[(E_0\otimes I_S)\rho_{CS}]
=\frac12|0\rangle_S\langle0|.
\]
Its trace is \(p(0)\). Since \(p(0)>0\), the normalized conditional system state is
\[
\rho_{S|0}=\widetilde\rho_{S|0}/p(0)=|0\rangle_S\langle0|.
\]
If \(p(0)=0\), the unnormalized operator remains meaningful but this normalized state is undefined: division is an error, not a state assignment.

Without outcome selection, the reduced state is
\[
\rho_S=\operatorname{Tr}_C(\rho_{CS})=\tfrac12I_S,
\]
which differs from \(\rho_{S|0}\). Indeed \(\rho_S=p(0)\rho_{S|0}+p(1)\rho_{S|1}\).

## 3. A finite POVM effect is not necessarily a projector

A general measurement outcome may be represented by an effect that is not a projector. For example, in the clock basis \((|0\rangle,|1\rangle)\), let

\[
F_0=
\begin{pmatrix}
0.9&0\\
0&0.2
\end{pmatrix},
\qquad
F_1=I_C-F_0=
\begin{pmatrix}
0.1&0\\
0&0.8
\end{pmatrix}.
\]

The pair \(\{F_0,F_1\}\) is a finite two-outcome POVM because each effect satisfies \(0\leq F_x\leq I_C\) and

\[
F_0+F_1=I_C.
\]

But \(F_0\) is not a projector:

\[
F_0^2=
\begin{pmatrix}
0.81&0\\
0&0.04
\end{pmatrix}
\ne F_0.
\]

This is a fuzzy clock readout: outcome \(0\) can occur with probability \(0.9\) for \(|0\rangle_C\) and with probability \(0.2\) for \(|1\rangle_C\). A POVM specifies these outcome probabilities; it still does not by itself specify a selected joint post-outcome state.

## Appendix — scoped ideal Lüders update

Add the special sharp Lüders instrument \(\mathcal I_0(\sigma)=E_0\sigma E_0\). It gives the selected joint state
\[
\rho'_{CS|0}=\frac{(\mathcal I_0\otimes\mathrm{id}_S)(\rho_{CS})}{p(0)}=|00\rangle\langle00|.
\]
Its system marginal is \(|0\rangle\langle0|=\rho_{S|0}\). More generally, every clock-local instrument with associated effect \(E_t\) has this same postselected system marginal after tracing out the clock. The effect still does not determine the selected joint state, residual clock state, disturbance account, or later sequential clock statistics.

## Pedagogical Go checks

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

type JointKet2D [2][2]complex128
type JointDensity2D [2][2][2][2]complex128
type SystemDensity2D [2][2]complex128

// Given: ket[c][s] is the coefficient of |c⟩C|s⟩S in the declared C:S basis.
// Mathematical fact: a normalized pure joint ket defines ρCS = |Ψ⟩⟨Ψ|.
func jointPureStateDensity2D(ket JointKet2D) JointDensity2D {
    var rho JointDensity2D
    for c := 0; c < 2; c++ {
        for s := 0; s < 2; s++ {
            for d := 0; d < 2; d++ {
                for t := 0; t < 2; t++ {
                    rho[c][s][d][t] = ket[c][s] * cmplx.Conj(ket[d][t])
                }
            }
        }
    }
    return rho
}

// Given: outcome is 0 or 1 and rho is represented in the declared C:S basis.
// Model scope: this applies the sharp clock projector |outcome⟩⟨outcome|.
// The returned operator is the unnormalized conditional system operator.
func sharpClockConditionalSystem2D(
    rho JointDensity2D,
    outcome int,
) (SystemDensity2D, error) {
    if outcome < 0 || outcome > 1 {
        return SystemDensity2D{}, fmt.Errorf("clock outcome must be 0 or 1")
    }

    var conditional SystemDensity2D
    for systemRow := 0; systemRow < 2; systemRow {
        for systemColumn := 0; systemColumn < 2; systemColumn++ {
            conditional[systemRow][systemColumn] =
                rho[outcome][systemRow][outcome][systemColumn]
        }
    }
    return conditional, nil
}

// Given: p is a supplied finite floating-point approximation to an exact probability.
// Model scope: this guard checks a numerical denominator; mathematically normalization requires p > 0.
func hasStrictlyPositiveFiniteProbability(p, tolerance float64) bool {
    return !math.IsNaN(p) && !math.IsInf(p, 0) && p > tolerance
}

// Given: unnormalized has trace p in the declared finite two-level model.
// A conditional state is undefined at zero probability; tolerance handles round-off, not the exact rule.
func normalizeConditionalSystem2D(unnormalized SystemDensity2D, p, tolerance float64) (SystemDensity2D, error) {
    if !hasStrictlyPositiveFiniteProbability(p, tolerance) {
        return SystemDensity2D{}, fmt.Errorf("conditional state undefined: probability is not strictly positive")
    }
    var normalized SystemDensity2D
    for i := 0; i < 2; i++ { for j := 0; j < 2; j++ {
        normalized[i][j] = unnormalized[i][j] / complex(p, 0)
    } }
    return normalized, nil
}

// Given: M is a finite 2×2 matrix in the declared orthonormal clock basis.
// A Hermitian 2×2 matrix is positive semidefinite when its diagonal entries and
// determinant are nonnegative, within numerical tolerance.
func isPositiveSemidefinite2D(M SystemDensity2D, tolerance float64) bool {
    determinant := M[0][0]*M[1][1] - M[0][1]*M[1][0]
    return cmplx.Abs(M[0][1]-cmplx.Conj(M[1][0])) < tolerance &&
        math.Abs(imag(M[0][0])) < tolerance &&
        math.Abs(imag(M[1][1])) < tolerance &&
        real(M[0][0]) >= -tolerance && real(M[1][1]) >= -tolerance &&
        math.Abs(imag(determinant)) < tolerance && real(determinant) >= -tolerance
}

// Given: E is a finite 2×2 operator in the declared orthonormal clock basis.
// An effect MUST satisfy 0 ≤ E ≤ I. In this finite model, check that E and I-E
// are positive semidefinite through their Hermitian 2×2 principal-minor conditions.
func isEffect2D(E SystemDensity2D, tolerance float64) bool {
    complement := SystemDensity2D{{1 - E[0][0], -E[0][1]}, {-E[1][0], 1 - E[1][1]}}
    return isPositiveSemidefinite2D(E, tolerance) &&
        isPositiveSemidefinite2D(complement, tolerance)
}

// Given: effects contains finite 2×2 effects in one declared clock basis.
// A discrete POVM MUST consist of effects that sum to the identity operator.
func isPOVM2D(effects []SystemDensity2D, tolerance float64) bool {
    var total SystemDensity2D
    for _, effect := range effects {
        if !isEffect2D(effect, tolerance) {
            return false
        }
        for i := 0; i < 2; i++ {
            for j := 0; j < 2; j++ {
                total[i][j] += effect[i][j]
            }
        }
    }
    return math.Abs(real(total[0][0])-1) < tolerance &&
        math.Abs(real(total[1][1])-1) < tolerance &&
        cmplx.Abs(total[0][1]) < tolerance &&
        cmplx.Abs(total[1][0]) < tolerance
}

func main() {
    // Bell state |Ψ⟩ = (|00⟩ + |11⟩) / √2 in the declared C:S basis.
    bellKet := JointKet2D{
        {1 / math.Sqrt2, 0},
        {0, 1 / math.Sqrt2},
    }

    joint := jointPureStateDensity2D(bellKet)
    unnormalized, err := sharpClockConditionalSystem2D(joint, 0)
    probability := real(unnormalized[0][0] + unnormalized[1][1])
    conditional, normalizeErr := normalizeConditionalSystem2D(unnormalized, probability, 1e-12)
    _, zeroErr := normalizeConditionalSystem2D(unnormalized, 0, 1e-12)

    F0 := SystemDensity2D{{.9, 0}, {0, .2}}
    F1 := SystemDensity2D{{.1, 0}, {0, .8}}

    fmt.Println(unnormalized, probability, err)
    fmt.Println(conditional, normalizeErr, zeroErr != nil)
    fmt.Println(isEffect2D(F0, 1e-12))
    fmt.Println(isPOVM2D([]SystemDensity2D{F0, F1}, 1e-12))
    // [[(0.5+0i) (0+0i)] [(0+0i) (0+0i)]] 0.5 <nil>
    // [[(1+0i) (0+0i)] [(0+0i) (0+0i)]] <nil> true
    // true
    // true
}
```

## What this example does not show

It does not make Lüders updating universal, describe all detectors or continuous outcomes, derive time evolution, or identify a finite outcome label with a physical time observable in full constrained gravity.
