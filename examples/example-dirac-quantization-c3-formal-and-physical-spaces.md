---
{
  "schema_version": "2.0",
  "id": "example-dirac-quantization-c3-formal-and-physical-spaces",
  "type": "example",
  "title": "Finite C³ Constraint: Formal Kernel and Separately Declared Physical Pairing",
  "summary": "A paired finite-dimensional toy model separating a kinematical C³ space, an ordinary constraint kernel, and an explicitly declared physical pairing.",
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
    "dirac-quantization",
    "formal-and-physical-state-spaces",
    "operators-and-domains",
    "constrained-systems"
  ],
  "teaches": [
    "identify a finite kinematical space",
    "solve a finite quantum constraint as a null-space equation",
    "separate an ordinary kernel from a declared physical pairing",
    "state why finite coincidences are not universal"
  ],
  "prerequisites": [
    "inner-product-spaces",
    "hilbert-spaces",
    "bases-and-coordinates",
    "dirac-notation",
    "spectral-notation",
    "operators-and-domains",
    "constrained-systems"
  ],
  "action": "Apply one diagonal constraint to a general ket in C³, compute its ordinary kernel, evaluate both the kinematical and separately declared physical pairings on formal solutions, and identify which equalities are only toy-model features.",
  "non_conclusion": "This finite model neither constructs a physical Hilbert space for a general constrained system nor shows that physical states are generally ordinary kernel vectors, that the physical pairing is inherited, or that anomalies and domain questions disappear.",
  "relationships": [
    {
      "type": "illustrates",
      "target": "dirac-quantization"
    },
    {
      "type": "illustrates",
      "target": "formal-and-physical-state-spaces"
    }
  ],
  "sources": [
    {
      "title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems",
      "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems",
      "persistent_id": "ISBN:9780691037691"
    },
    {
      "title": "D. Giulini and D. Marolf, On the Generality of Refined Algebraic Quantization",
      "url": "https://arxiv.org/abs/gr-qc/9812024",
      "persistent_id": "arXiv:gr-qc/9812024"
    }
  ]
}
---
# Finite C³ Constraint: Formal Kernel and Separately Declared Physical Pairing

## Prerequisites, scope, and local setup

Assume a finite-dimensional Hilbert space, an orthonormal basis, matrix action on coordinate columns, and the distinction between a kinematical space and a physical construction. This example uses no generalized states and no gauge-orbit calculation.

**Model scope:** Let the kinematical Hilbert space be \(\mathcal H_{\mathrm{kin}}=\mathbb C^3\), with the ordered orthonormal basis \((|0\rangle,|1\rangle,|2\rangle)\). Every kinematical ket has the form

\[
|\psi\rangle=a|0\rangle+b|1\rangle+c|2\rangle
\quad\longleftrightarrow\quad
\begin{pmatrix}a\\b\\c\end{pmatrix},
\qquad a,b,c\in\mathbb C.
\]

**Convention:** The kinematical inner product is conjugate-linear in the first argument and linear in the second:

\[
\langle\phi|\psi\rangle_{\mathrm{kin}}
=\phi_0^*\psi_0+\phi_1^*\psi_1+\phi_2^*\psi_2.
\]

Choose the finite constraint operator

\[
\hat C=
\begin{pmatrix}
0&0&0\\
0&1&0\\
0&0&2
\end{pmatrix}.
\]

It is a bounded self-adjoint matrix on all of \(\mathbb C^3\). This removes domain difficulty by design; it does not resolve domain issues in general Dirac quantization.

## 1. Kinematical vectors are not yet constraint solutions

The three basis kets are kinematical vectors. Applying the constraint gives

\[
\hat C|0\rangle=0,\qquad
\hat C|1\rangle=|1\rangle,\qquad
\hat C|2\rangle=2|2\rangle.
\]

Thus membership in \(\mathcal H_{\mathrm{kin}}\) does not itself make a vector a solution. For the general ket,

\[
\hat C|\psi\rangle
=
\begin{pmatrix}0\\b\\2c\end{pmatrix}.
\]

The finite formal constraint equation \(\hat C|\psi\rangle=0\) requires \(b=0\) and \(c=0\), while \(a\) is unrestricted. Therefore the formal solution space in this model is the ordinary matrix kernel

\[
\mathcal H_{\mathrm{form}}
=\ker\hat C
=\left\{a|0\rangle:a\in\mathbb C\right\}
=\operatorname{span}\{|0\rangle\}.
\]

Here “formal” marks the role of the constraint equation; it does not silently add a physical probability interpretation.

## 2. Separately declare the physical pairing

To make the next logical step explicit, define a physical state representation by the same underlying solution vectors but **declare** its pairing to be

\[
\langle\alpha0|\beta0\rangle_{\mathrm{phys}}
:=7\alpha^*\beta,
\qquad \alpha,\beta\in\mathbb C.
\]

This is a positive inner product: for \(\alpha\ne0\),

\[
\langle\alpha0|\alpha0\rangle_{\mathrm{phys}}
=7|\alpha|^2>0.
\]

Compare it with the inherited kinematical value on the same coordinate representatives:

\[
\langle\alpha0|\beta0\rangle_{\mathrm{kin}}=\alpha^*\beta.
\]

For example,

\[
\langle0|0\rangle_{\mathrm{kin}}=1,
\qquad
\langle0|0\rangle_{\mathrm{phys}}=7.
\]

The two pairings differ numerically because the physical one was a separate declaration. In this one-dimensional toy model, the difference is an innocuous positive rescaling after normalization; it is chosen solely to keep the logical distinction visible. It is **not** a derivation of a physical inner product from \(\hat C\).

If physical normalization is wanted, use

\[
|0\rangle_{\mathrm{phys,norm}}=\frac1{\sqrt7}|0\rangle,
\qquad
\langle0_{\mathrm{phys,norm}}|0_{\mathrm{phys,norm}}\rangle_{\mathrm{phys}}=1.
\]

## 3. Why the coincidences are limited

This example has four deliberately favorable coincidences:

1. \(\hat C\) is a finite bounded matrix defined everywhere;
2. zero is a discrete eigenvalue;
3. the formal solution space is an ordinary subspace of \(\mathcal H_{\mathrm{kin}}\);
4. the physical pairing is easily declared on that one-dimensional space.

None is universal. In an infinite-dimensional constrained system, constraints can be unbounded and domain-sensitive; zero can be in continuous spectrum; solutions can be distributional rather than normalizable kets; multiple constraint operators can fail to have a consistent common quantum implementation; and the physical pairing can require gauge reduction, boundary conditions, a rigging map, group averaging, or another model-specific construction. Factor ordering and anomalies are absent here only because the single diagonal finite matrix was chosen to avoid them.

## 4. Pedagogical Go check for this finite model

```go
package main

import (
    "fmt"
    "math/cmplx"
)

type Ket3 [3]complex128
type Matrix3 [3][3]complex128

// Given: ket stores coordinates in the declared ordered orthonormal C³ basis.
// Model scope: this helper represents only finite 3×3 matrix action.
func applyConstraint3D(constraint Matrix3, ket Ket3) Ket3 {
    var result Ket3
    for row := range constraint {
        for column := range ket {
            result[row] += constraint[row][column] * ket[column]
        }
    }
    return result
}

// Given: tolerance is positive and constraint acts on the same finite C³ basis.
// Model scope: zeroConstraintResidual3D tests an ordinary matrix-kernel condition.
// A true result means C|ψ⟩ is numerically zero in this finite representation only.
func zeroConstraintResidual3D(constraint Matrix3, ket Ket3, tolerance float64) bool {
    residual := applyConstraint3D(constraint, ket)
    for _, component := range residual {
        if cmplx.Abs(component) >= tolerance {
            return false
        }
    }
    return true
}

// Given: alpha|0⟩ and beta|0⟩ lie in the one-dimensional formal kernel of this model.
// Convention: the first coefficient is conjugated.
// Model scope: physicalInnerProductOnToyKernel3D is a separately declared pairing,
// not a general physical-inner-product construction.
func physicalInnerProductOnToyKernel3D(alpha, beta complex128) complex128 {
    return 7 * cmplx.Conj(alpha) * beta
}

func main() {
    constraint := Matrix3{{0, 0, 0}, {0, 1, 0}, {0, 0, 2}}
    ket0 := Ket3{1, 0, 0}
    ket1 := Ket3{0, 1, 0}
    tolerance := 1e-12

    fmt.Println(zeroConstraintResidual3D(constraint, ket0, tolerance)) // true
    fmt.Println(zeroConstraintResidual3D(constraint, ket1, tolerance)) // false
    fmt.Println(physicalInnerProductOnToyKernel3D(1, 1))                // (7+0i)
}
```

The names `applyConstraint3D`, `zeroConstraintResidual3D`, and `physicalInnerProductOnToyKernel3D` intentionally state their finite-model scope. They do not claim to solve constraints or construct physical amplitudes in a general theory.

## What this example does and does not show

The calculation distinguishes the finite kinematical space, its ordinary null space, and a separately stipulated physical pairing. It does not establish that a physical state space generally equals a kernel, that all physical pairings are rescalings, that a finite matrix models gauge reduction, or that the full consistency requirements of Dirac quantization have been met.
