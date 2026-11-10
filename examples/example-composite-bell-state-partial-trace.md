---
{
  "schema_version": "2.0",
  "id": "example-composite-bell-state-partial-trace",
  "type": "example",
  "title": "Composite System: Bell State, Partial Trace, and Product-State Contrast",
  "summary": "A self-contained two-qubit calculation of a Bell-state density operator and its reduced state, contrasted with a product state.",
  "review_status": "ai_reviewed",
  "status": [
    "synthetic"
  ],
  "patterns": [
    "calculation",
    "comparison"
  ],
  "modality": [
    "text",
    "code"
  ],
  "topics": [
    "composite-systems"
  ],
  "teaches": [
    "declare an ordered product basis",
    "form a pure-state density operator",
    "take a partial trace",
    "distinguish a product state from pure-bipartite entanglement"
  ],
  "prerequisites": [
    "inner-product-spaces",
    "quantum-states-rays-and-normalization",
    "bases-and-coordinates",
    "dirac-notation",
    "composite-systems"
  ],
  "action": "Expand the Bell state in the declared C:S product-basis order, form its density operator, take the partial trace over C, and contrast it with a product state.",
  "non_conclusion": "This finite two-qubit calculation does not classify arbitrary mixed-state entanglement, provide a Bell-inequality test, imply signalling, or construct a physical clock or gravitational subsystem split.",
  "relationships": [
    {
      "type": "illustrates",
      "target": "composite-systems"
    }
  ],
  "sources": [
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ]
}
---
# Composite System: Bell State, Partial Trace, and Product-State Contrast

## Prerequisites and local setup

Let \(C\) and \(S\) each be \(\mathbb C^2\), with orthonormal bases \((|0\rangle,|1\rangle)\). **Convention:** all columns and matrices use the product-basis order
\[
(|0\rangle_C|0\rangle_S,|0\rangle_C|1\rangle_S,|1\rangle_C|0\rangle_S,|1\rangle_C|1\rangle_S).
\]
The first label is \(C\), so \(|1\rangle_C|0\rangle_S=(0,0,1,0)^T\). This is a representation choice.

## Bell state, density operator, and partial trace

**Model scope:** choose the normalized two-qubit Bell state
\[
|\Phi^+\rangle=\frac{|0\rangle_C|0\rangle_S+|1\rangle_C|1\rangle_S}{\sqrt2}
=\frac1{\sqrt2}(1,0,0,1)^T.
\]
Its density operator is
\[
\rho_{CS}=|\Phi^+\rangle\langle\Phi^+|=
\frac12\begin{pmatrix}1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1\end{pmatrix}.
\]
For the declared clock basis,
\[
\operatorname{Tr}_C(\rho_{CS})=
\sum_{c=0}^1({}_C\langle c|\otimes I_S)\rho_{CS}(|c\rangle_C\otimes I_S).
\]
The diagonal terms yield \(\tfrac12|0\rangle\langle0|\) and \(\tfrac12|1\rangle\langle1|\); the cross terms vanish because \(\langle0|1\rangle_C=0\). Thus the reduced state is
\[
\rho_S=\tfrac12(|0\rangle\langle0|+|1\rangle\langle1|)=\tfrac12I_S.
\]
It is mixed even though the joint state is pure, because it ignores correlations with \(C\).

## Product-state contrast

\(|0\rangle_C|0\rangle_S\) is product and has reduced state \(|0\rangle_S\langle0|\). In contrast, the Bell coefficient matrix is
\[
A_{\Phi^+}=\frac1{\sqrt2}\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]
A pure two-factor state is product exactly when its coefficient matrix has rank one. Here \(\det A_{\Phi^+}=1/2\ne0\), so it has rank two and is entangled. This is a pure finite-bipartite criterion, not a test for mixed states.

The reduced state \(I_S/2\) has no selected outcome. A conditional state requires an outcome condition; see [Measurements and Conditional States](../mathematics/conditional-states.md).

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
type CoefficientMatrix2D [2][2]complex128

// Given: clock and system are coordinate kets in their declared C² bases.
// Convention: the output uses the C:S factor order, so ket[c][s] is the
// coefficient of |c⟩C|s⟩S.
func tensorKet2D(clock, system [2]complex128) JointKet2D {
    var joint JointKet2D
    for c := 0; c < 2; c++ {
        for s := 0; s < 2; s++ {
            joint[c][s] = clock[c] * system[s]
        }
    }
    return joint
}

// Given: ket is a normalized pure joint ket in the declared C:S product basis.
// Mathematical fact: ρCS = |Ψ⟩⟨Ψ| has components
// ρ[c][s][d][t] = Ψ[c][s] × conjugate(Ψ[d][t]).
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

// Given: rho[c][i][d][j] is ⟨c,i|ρ_CS|d,j⟩ in the declared C:S basis order.
// Model scope: C and S are finite two-dimensional factors.
// The partial trace is (Tr_C rho)[i][j] = Σ_c rho[c][i][c][j].
func partialTraceOverClock2D(rho JointDensity2D) SystemDensity2D {
    var reduced SystemDensity2D
    for c := 0; c < 2; c++ { for i := 0; i < 2; i++ { for j := 0; j < 2; j++ {
        reduced[i][j] += rho[c][i][c][j]
    } } }
    return reduced
}

// Given: a is the coefficient matrix of a pure C²⊗C² vector in chosen local bases.
// Model scope: determinant rank testing applies only to this pure two-factor model.
// A nonzero determinant rules out product form; this is not a mixed-state entanglement test.
func isRankOneCoefficientMatrix2D(a CoefficientMatrix2D, tolerance float64) bool {
    return cmplx.Abs(a[0][0]*a[1][1]-a[0][1]*a[1][0]) <= tolerance
}

// Given: rho is a finite 2×2 matrix in the declared orthonormal system basis.
// A Hermitian matrix MUST equal its Hermitian adjoint. For 2×2 coordinates,
// this checks real diagonal entries and conjugate-symmetric off-diagonal entries.
func isHermitianMatrix2D(rho SystemDensity2D, tolerance float64) bool {
    return math.Abs(imag(rho[0][0])) <= tolerance &&
        math.Abs(imag(rho[1][1])) <= tolerance &&
        cmplx.Abs(rho[0][1]-cmplx.Conj(rho[1][0])) <= tolerance
}

// Given: rho is a finite 2×2 matrix.
// A density operator MUST have trace one. This checks the declared finite
// coordinate trace up to floating-point tolerance.
func hasUnitTrace2D(rho SystemDensity2D, tolerance float64) bool {
    trace := rho[0][0] + rho[1][1]
    return math.Abs(imag(trace)) <= tolerance &&
        math.Abs(real(trace)-1) <= tolerance
}

// Given: rho is a finite Hermitian 2×2 matrix in the declared basis.
// In this finite model, positive semidefiniteness is equivalent to nonnegative
// diagonal entries and nonnegative determinant, within tolerance.
func isPositiveSemidefinite2D(rho SystemDensity2D, tolerance float64) bool {
    determinant := rho[0][0]*rho[1][1] - rho[0][1]*rho[1][0]
    return real(rho[0][0]) >= -tolerance &&
        real(rho[1][1]) >= -tolerance &&
        math.Abs(imag(determinant)) <= tolerance &&
        real(determinant) >= -tolerance
}

// Given: rho is supplied as a finite 2×2 matrix in the declared system basis.
// A finite density operator MUST be Hermitian, positive semidefinite, and trace one.
// This is a scoped C² predicate, not a proof of the general density-operator theorem.
func isDensityOperator2D(rho SystemDensity2D, tolerance float64) bool {
    return isHermitianMatrix2D(rho, tolerance) &&
        hasUnitTrace2D(rho, tolerance) &&
        isPositiveSemidefinite2D(rho, tolerance)
}

func main() {
    // Bell state |Φ⁺⟩ = (|00⟩ + |11⟩) / √2 in the declared C:S basis.
    bellKet := JointKet2D{
        {1 / math.Sqrt2, 0},
        {0, 1 / math.Sqrt2},
    }

    bellDensity := jointPureStateDensity2D(bellKet)
    reduced := partialTraceOverClock2D(bellDensity)
    coefficient := CoefficientMatrix2D{{1 / math.Sqrt2, 0}, {0, 1 / math.Sqrt2}}

    fmt.Println(reduced, isDensityOperator2D(reduced, 1e-12), isRankOneCoefficientMatrix2D(coefficient, 1e-12))
    // [[(0.5+0i) (0+0i)] [(0+0i) (0.5+0i)]] true false
}
```

## What this example does not show

It does not classify mixed-state entanglement, model a physical measurement implementation, or select a preferred clock--system split in quantum gravity.
