---
{
  "schema_version": "2.0",
  "id": "example-bases-coordinates-and-orthonormality",
  "type": "example",
  "title": "Bases and Coordinates: From a Set of Kets to an Orthonormal Basis of C²",
  "summary": "A self-contained C² example of spanning, linear independence, coordinates, basis labels, and orthonormal bases.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text"],
  "topics": ["bases-and-coordinates", "inner-product-spaces", "dirac-notation"],
  "teaches": ["calculate a span", "test linear independence in C²", "distinguish an orthonormal set from a basis", "assign basis labels", "compute coordinates relative to an ordered basis"],
  "prerequisites": ["inner-product-spaces", "norms-distance-and-convergence", "hilbert-spaces", "quantum-states-rays-and-normalization"],
  "action": "Start with an incomplete orthonormal set, add a second ket, verify independence and spanning in C², and recover coordinates in the resulting ordered orthonormal basis.",
  "non_conclusion": "This C² determinant test is specific to two vectors in a two-dimensional finite target space. It does not provide a universal spanning test for arbitrary finite or infinite-dimensional Hilbert spaces.",
  "relationships": [
    {"type": "illustrates", "target": "bases-and-coordinates"}
  ],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}
  ]
}
---

# Bases and Coordinates: From a Set of Kets to an Orthonormal Basis of \(\mathbb C^2\)

## Prerequisites and local setup

This example works only in the finite two-dimensional complex vector space \(\mathbb C^2\). A ket is represented by its coordinate column in one chosen coordinate system. The standard physics inner product is

\[
\langle\phi|\psi\rangle=\phi_0^*\psi_0+\phi_1^*\psi_1.
\]

**Model scope:** This example uses the two-dimensional complex target space \(\mathbb C^2\). The \(\mathbb C^2\) restriction is used later for its two-vector determinant and spanning theorem; the inner product and norm themselves work in any chosen finite-dimensional coordinate basis.

Define the ordered standard-basis contract

\[
B_{\mathrm{std}}=(e_0,e_1),
\qquad
e_0=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
e_1=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Within this contract, label \(0\) stably identifies \(e_0\), and label \(1\) stably identifies \(e_1\). The labels are not extracted from the coordinate entries. They retain this meaning only while the target space, these basis vectors, and their stated order remain fixed.

## 1. An orthonormal set that is not yet a basis

The one-element set \(\{e_0\}\) is orthonormal because

\[
\langle e_0|e_0\rangle=1.
\]

But it is not a basis for \(\mathbb C^2\). Its span contains only vectors of the form

\[
ae_0=\begin{pmatrix}a\\0\end{pmatrix}.
\]

It cannot produce

\[
e_1=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Thus an orthonormal set need not span the target space.

## 2. Add a second ket

Now use the ordered collection

\[
B=(e_0,e_1).
\]

It is orthonormal because

\[
\langle e_0|e_0\rangle=1,
\qquad
\langle e_1|e_1\rangle=1,
\qquad
\langle e_0|e_1\rangle=0.
\]

To test linear independence and spanning in \(\mathbb C^2\), form a matrix with the kets as columns:

\[
A=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Its determinant is

\[
\det A=1\ne0.
\]

Therefore \(e_0,e_1\) are linearly independent. Because \(\mathbb C^2\) has dimension two, two linearly independent vectors span it. Thus \(B\) is an orthonormal basis for \(\mathbb C^2\).

## 3. Coordinates and labels

The order in the declared contract \(B_{\mathrm{std}}=(e_0,e_1)\) assigns labels:

\[
e_0\equiv|0\rangle,
\qquad
e_1\equiv|1\rangle.
\]

The labels \(0\) and \(1\) identify positions in this chosen ordered basis. They are not extracted from the entries of the kets. The stable label contract is

\[
(B_{\mathrm{std}},0)\mapsto e_0,
\qquad
(B_{\mathrm{std}},1)\mapsto e_1.
\]

A label by itself is therefore insufficient outside its declared basis contract: another ordered basis can assign the same label to a different vector.

For

\[
|\psi\rangle=\begin{pmatrix}3-i\\2+i\end{pmatrix},
\]

the coordinate expansion relative to \(B\) is

\[
|\psi\rangle=(3-i)e_0+(2+i)e_1.
\]

Its coordinate column relative to \(B\) is

\[
[\psi]_B=\begin{pmatrix}3-i\\2+i\end{pmatrix}.
\]

In this standard basis, the coordinate column happens to look exactly like the ket's usual column representation. In another ordered basis, the same abstract ket generally has different coordinates.

## 4. Pedagogical Go checks for \(\mathbb C^2\)

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

// Given: |φ⟩ and |ψ⟩ have coordinates in the same chosen finite basis.
// Under the physics convention, ⟨φ|ψ⟩ is conjugate-linear in φ and linear in ψ.
// This inner-product calculation does not require the target space to be C².
func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

// Given: |ψ⟩ has coordinates in a chosen finite basis.
// The norm is the nonnegative square root of ⟨ψ|ψ⟩.
// This norm calculation does not require the target space to be C².
func norm(ket []complex128) float64 {
    return math.Sqrt(real(inner(ket, ket)))
}

// Given: u and v are coordinate kets in one chosen finite basis.
// Model scope: u and v each have exactly two coordinates, so they are vectors in C².
// In C², two vectors are linearly independent exactly when their column
// determinant has nonzero magnitude. Floating-point checks use a tolerance.
func isLinearlyIndependent2D(u, v []complex128, tolerance float64) bool {
    if len(u) != 2 || len(v) != 2 {
        return false
    }
    determinant := u[0]*v[1] - u[1]*v[0]
    return cmplx.Abs(determinant) > tolerance
}

// Given: u and v are coordinate kets in one chosen finite basis.
// Model scope: the declared target space is C² and u, v each have two coordinates.
// Naming note: spansComplexNumbers2D is deliberately explicit; the shorter spansC2
// would be conventional mathematical shorthand, while spansComplexNumbers2 would
// read as though it referred to two complex numbers rather than a 2D complex space.
// Two linearly independent vectors in this C² model MUST span C².
func spansComplexNumbers2D(u, v []complex128, tolerance float64) bool {
    return isLinearlyIndependent2D(u, v, tolerance)
}

// Given: u and v are coordinate kets in one chosen finite basis.
// Model scope: the declared target space is C² and u, v each have two coordinates.
// A basis MUST be both linearly independent and spanning.
func isBasisForComplexNumbers2D(u, v []complex128, tolerance float64) bool {
    return isLinearlyIndependent2D(u, v, tolerance) && spansComplexNumbers2D(u, v, tolerance)
}

// Given: u and v are coordinate kets in one chosen finite basis.
// Model scope: the declared target space is C² and u, v each have two coordinates.
// An orthonormal basis MUST be an orthonormal set that also spans its target space.
// In this C² model, spansComplexNumbers2D establishes the required spanning condition.
func isOrthonormalBasisForComplexNumbers2D(u, v []complex128, tolerance float64) bool {
    normalized := math.Abs(norm(u)-1) < tolerance && math.Abs(norm(v)-1) < tolerance
    orthogonal := cmplx.Abs(inner(u, v)) < tolerance && cmplx.Abs(inner(v, u)) < tolerance
    return normalized && orthogonal && spansComplexNumbers2D(u, v, tolerance)
}

func main() {
    ket0 := []complex128{1, 0}
    ket1 := []complex128{0, 1}
    tolerance := 1e-12

    fmt.Println(isLinearlyIndependent2D(ket0, ket1, tolerance)) // true
    fmt.Println(spansComplexNumbers2D(ket0, ket1, tolerance))                 // true
    fmt.Println(isBasisForComplexNumbers2D(ket0, ket1, tolerance))            // true
    fmt.Println(isOrthonormalBasisForComplexNumbers2D(ket0, ket1, tolerance)) // true
}
```

## What this example does and does not show

This example establishes how basis labels, coordinates, span, linear independence, and orthonormality work in \(\mathbb C^2\). It does not provide a general computational spanning test in higher dimensions or for infinite-dimensional Hilbert spaces.
