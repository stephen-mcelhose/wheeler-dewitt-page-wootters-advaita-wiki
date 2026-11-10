---
{
  "schema_version": "2.0",
  "id": "example-born-rule-amplitudes-probabilities-and-luders-update",
  "type": "example",
  "title": "Born Rule: Amplitudes, Probabilities, and an Ideal Lüders Update",
  "summary": "A self-contained C² example distinguishing a complex amplitude, a sharp yes/no probability, a projected component, and an optional ideal Lüders state update.",
  "review_status": "ai_reviewed",
  "status": [
    "synthetic"
  ],
  "patterns": [
    "calculation",
    "comparison"
  ],
  "modality": [
    "text"
  ],
  "topics": [
    "born-rule-and-quantum-probability",
    "projection-operators",
    "dirac-notation",
    "quantum-states-rays-and-normalization"
  ],
  "teaches": [
    "distinguish amplitude from probability",
    "calculate a sharp yes/no Born probability",
    "construct complementary outcomes",
    "check probability normalization",
    "distinguish projection from state update",
    "apply an ideal Lueders update"
  ],
  "prerequisites": [
    "inner-product-spaces",
    "norms-distance-and-convergence",
    "quantum-states-rays-and-normalization",
    "bases-and-coordinates",
    "dirac-notation",
    "projection-operators"
  ],
  "action": "Verify a complex two-level state is normalized, calculate one amplitude and its probability, compare projector and amplitude forms, construct the complementary outcome, and optionally normalize the selected component after an ideal yes outcome.",
  "non_conclusion": "This is a finite-dimensional ideal sharp projective measurement model. It does not describe a general POVM, a general measurement instrument, mixed-state measurement, continuous outcomes, or a universal physical collapse mechanism.",
  "relationships": [
    {
      "type": "illustrates",
      "target": "born-rule-and-quantum-probability"
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

# Born Rule: Amplitudes, Probabilities, and an Ideal Lüders Update

## Prerequisites and local setup

**Model scope:** Work in the two-dimensional complex Hilbert space \(\mathbb C^2\), with declared orthonormal basis

\[
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
\]

The measurement is an ideal sharp two-outcome projective measurement \(\{P_0,I-P_0\}\). This example does not yet model general measurements.

**Convention:** The physics inner product is conjugate-linear in its first argument and linear in its second:

\[
\langle\phi|\psi\rangle=\phi_0^*\psi_0+\phi_1^*\psi_1.
\]

Use the state

\[
|\psi\rangle=
\frac12\begin{pmatrix}1+i\\1-i\end{pmatrix}
=
\frac{1+i}{2}|0\rangle+\frac{1-i}{2}|1\rangle.
\]

## 1. Verify normalization

\[
\langle\psi|\psi\rangle
=
\left|\frac{1+i}{2}\right|^2+
\left|\frac{1-i}{2}\right|^2
=
\frac12+\frac12=1.
\]

Thus \(|\psi\rangle\) is normalized. The simple Born-rule formula used below requires this condition.

## 2. Define the yes outcome

The yes outcome “the state lies in the \(|0\rangle\) direction” is represented by the rank-one orthogonal projector

\[
P_0=|0\rangle\langle0|
=
\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

It satisfies

\[
P_0^2=P_0,
\qquad
P_0^\dagger=P_0.
\]

## 3. Amplitude is not probability

The amplitude for the \(|0\rangle\) outcome is

\[
A_0=\langle0|\psi\rangle
=\frac{1+i}{2}.
\]

Read: “Bra zero ket psi equals one plus i over two.”

\(A_0\) is a complex amplitude. It is not a probability. The yes probability is its squared modulus:

\[
p_{\mathrm{yes}}
=|A_0|^2
=
\left|\frac{1+i}{2}\right|^2
=
\frac{1^2+1^2}{2^2}
=
\frac12.
\]

## 4. The projector form gives the same probability

First project the state:

\[
P_0|\psi\rangle
=|0\rangle\langle0|\psi\rangle
=\frac{1+i}{2}|0\rangle
=
\begin{pmatrix}\frac{1+i}{2}\\0\end{pmatrix}.
\]

This is a vector component, not a probability. Its squared norm is

\[
\|P_0|\psi\rangle\|^2
=
\frac12.
\]

The Born-rule projector expression agrees:

\[
p_{\mathrm{yes}}
=\langle\psi|P_0|\psi\rangle
=\frac12.
\]

## 5. The complementary no outcome

The no projector is

\[
P_1=I-P_0=|1\rangle\langle1|
=
\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]

Its probability is

\[
p_{\mathrm{no}}
=\langle\psi|P_1|\psi\rangle
=\frac12.
\]

The two probabilities are real, lie in the interval from zero to one, and add to one:

\[
0\leq p_{\mathrm{yes}},p_{\mathrm{no}}\leq1,
\qquad
p_{\mathrm{yes}}+p_{\mathrm{no}}
=\langle\psi|(P_0+P_1)|\psi\rangle
=\langle\psi|I|\psi\rangle
=1.
\]

## 6. Appendix — ideal Lüders update after the yes outcome

The Born rule gives a probability. A state update is an additional rule answering what state to use after an outcome is actually obtained.

**Model scope:** In an ideal sharp projective measurement, if the yes outcome occurs and \(p_{\mathrm{yes}}>0\), the Lüders update is

\[
|\psi\rangle
\longmapsto
\frac{P_0|\psi\rangle}{\sqrt{\langle\psi|P_0|\psi\rangle}}.
\]

For this example,

\[
\frac{P_0|\psi\rangle}{\sqrt{p_{\mathrm{yes}}}}
=
\frac{\frac{1+i}{2}|0\rangle}{\sqrt{1/2}}
=
\frac{1+i}{\sqrt2}|0\rangle.
\]

This updated ket differs from \(|0\rangle\) only by a global phase, so it represents the same ray as \(|0\rangle\). If \(p_{\mathrm{yes}}=0\), the outcome cannot occur in this model and this normalization is undefined.

## 7. Pedagogical Go checks in \(\mathbb C^2\)

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

type Matrix2 [2][2]complex128

// Given: |φ⟩ and |ψ⟩ have coordinates in one chosen finite orthonormal basis.
// Convention: the first argument is conjugated in the physics inner product.
func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

// Given: |ψ⟩ has finite coordinates in the declared basis.
// The squared norm is ⟨ψ|ψ⟩; for a valid numerical representation its imaginary part
// SHOULD be negligible up to floating-point round-off.
func normSquared(psi []complex128) complex128 {
    return inner(psi, psi)
}

func isNormalized(psi []complex128, tolerance float64) bool {
    squaredNorm := normSquared(psi)
    return math.Abs(imag(squaredNorm)) < tolerance &&
        math.Abs(real(squaredNorm)-1) < tolerance
}

func multiplyMatrix2D(A, B Matrix2) Matrix2 {
    var product Matrix2
    for row := range A {
        for column := range B {
            for k := range A {
                product[row][column] += A[row][k] * B[k][column]
            }
        }
    }
    return product
}

func hermitianAdjoint2D(A Matrix2) Matrix2 {
    return Matrix2{
        {cmplx.Conj(A[0][0]), cmplx.Conj(A[1][0])},
        {cmplx.Conj(A[0][1]), cmplx.Conj(A[1][1])},
    }
}

func matricesClose2D(A, B Matrix2, tolerance float64) bool {
    for row := range A {
        for column := range A {
            if cmplx.Abs(A[row][column]-B[row][column]) >= tolerance {
                return false
            }
        }
    }
    return true
}

// Given: P is a finite 2×2 matrix in the declared orthonormal C² basis.
// An orthogonal projector MUST satisfy both P² = P and P† = P.
func isOrthogonalProjector2D(P Matrix2, tolerance float64) bool {
    return matricesClose2D(multiplyMatrix2D(P, P), P, tolerance) &&
        matricesClose2D(hermitianAdjoint2D(P), P, tolerance)
}

// Given: |ψ⟩ is normalized and P is an orthogonal projector.
// Model scope: this returns the Born probability for an ideal sharp yes/no outcome.
// The result MUST be real and lie in [0, 1] up to floating-point tolerance.
func bornProbability2D(psi []complex128, P Matrix2, tolerance float64) (float64, error) {
    if !isNormalized(psi, tolerance) || !isOrthogonalProjector2D(P, tolerance) {
        return 0, fmt.Errorf("Born-rule preconditions are not satisfied")
    }

    projected := []complex128{
        P[0][0]*psi[0] + P[0][1]*psi[1],
        P[1][0]*psi[0] + P[1][1]*psi[1],
    }
    value := inner(psi, projected)
    if math.Abs(imag(value)) >= tolerance || real(value) < -tolerance || real(value) > 1+tolerance {
        return 0, fmt.Errorf("result is not a valid probability within tolerance")
    }
    return math.Max(0, math.Min(1, real(value))), nil
}

func main() {
    psi := []complex128{(1 + 1i) / 2, (1 - 1i) / 2}
    P0 := Matrix2{{1, 0}, {0, 0}}
    tolerance := 1e-12

    probability, err := bornProbability2D(psi, P0, tolerance)
    fmt.Println(probability, err) // 0.5 <nil>
}
```

## What this example does and does not show

This example shows how an ideal sharp two-outcome projective measurement converts a complex amplitude into a probability and distinguishes that probability from a projected vector and an optional ideal Lüders update. It does not describe general POVMs, arbitrary measurement instruments, mixed states, continuous outcomes, or a universal physical collapse mechanism.
