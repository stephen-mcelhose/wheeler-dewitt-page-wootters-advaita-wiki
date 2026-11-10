---
{
  "schema_version": "2.0",
  "id": "example-dirac-notation-basis-and-adjoint",
  "type": "example",
  "title": "Dirac Notation: Bras, Kets, Bases, and the Kronecker Delta",
  "summary": "A self-contained two-dimensional example of Hermitian adjoints, orthonormal basis vectors, Kronecker delta, basis expansion, and the identity operator.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text"],
  "topics": ["dirac-notation", "inner-product-spaces", "quantum-states-rays-and-normalization"],
  "teaches": ["read bras and kets", "take a Hermitian adjoint", "evaluate Kronecker delta", "test an orthonormal basis", "expand a vector in a basis", "apply the identity resolution"],
  "prerequisites": ["inner-product-spaces", "norms-distance-and-convergence", "hilbert-spaces", "quantum-states-rays-and-normalization"],
  "action": "Construct bras from kets, calculate all basis overlaps, connect them to the Kronecker delta, test orthonormality, and reconstruct a vector from its basis components.",
  "non_conclusion": "This finite two-dimensional example illustrates a discrete orthonormal basis only. It does not justify treating continuous labels as ordinary normalized basis vectors.",
  "relationships": [
    {"type": "illustrates", "target": "dirac-notation"}
  ],
  "sources": [
    {"title": "P. A. M. Dirac, The Principles of Quantum Mechanics", "url": "https://global.oup.com/academic/product/the-principles-of-quantum-mechanics-9780198520115", "persistent_id": "ISBN:9780198520115"},
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}
  ]
}
---

# Dirac Notation: Bras, Kets, Bases, and the Kronecker Delta

## Prerequisites and local setup

A **ket** is a vector, usually represented after choosing a basis as a column. A **bra** is the associated dual vector, represented in coordinates by the ket's Hermitian adjoint: complex-conjugate every entry and transpose the column into a row.

For vectors in \(\mathbb C^2\), use the physics inner product

\[
\langle\phi|\psi\rangle
=\phi_0^*\psi_0+\phi_1^*\psi_1.
\]

For a complex number \(a+bi\), complex conjugation flips the imaginary sign:

\[
(a+bi)^*=a-bi.
\]

## 1. Ket to bra: Hermitian adjoint

Let

\[
|\psi\rangle=\begin{pmatrix}1+i\\5-2i\end{pmatrix}.
\]

Its Hermitian adjoint is

\[
\langle\psi|
=\left(|\psi\rangle\right)^\dagger
=\begin{pmatrix}1-i&5+2i\end{pmatrix}.
\]

The Hermitian adjoint does two things:

1. complex-conjugates entries, so \(i\) changes sign;
2. transposes the ket column into a bra row.

The standard term is **Hermitian adjoint** or **conjugate transpose**. “Dual conjugate” is not standard terminology. The bra is the coordinate representation of the associated dual vector.

```go
package main

import (
    "fmt"
    "math/cmplx"
)

// Given: |ψ⟩ is represented by its coordinates in a chosen finite basis.
// Mathematically, the Hermitian adjoint |ψ⟩† has conjugated coordinates and
// reverses column-to-row orientation. This slice representation shows only
// the coordinate conjugation; it does not encode row/column orientation.
func hermitianAdjoint(ket []complex128) []complex128 {
    bra := make([]complex128, len(ket))
    for i, entry := range ket {
        bra[i] = cmplx.Conj(entry)
    }
    return bra
}

func main() {
    psi := []complex128{1 + 1i, 5 - 2i}
    fmt.Println(hermitianAdjoint(psi)) // [(1-1i) (5+2i)]
}
```

## 2. A two-vector discrete basis

Define the standard basis kets

\[
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Their bras are

\[
\langle0|=\begin{pmatrix}1&0\end{pmatrix},
\qquad
\langle1|=\begin{pmatrix}0&1\end{pmatrix}.
\]

Calculate all four overlaps:

\[
\langle0|0\rangle=1,
\qquad
\langle1|1\rangle=1,
\]

\[
\langle0|1\rangle=0,
\qquad
\langle1|0\rangle=0.
\]

Thus \(|0\rangle\) and \(|1\rangle\) are **orthonormal**: each has norm one, and they have zero overlap with one another.

## 3. Kronecker delta

The **Kronecker delta** is the compact label-matching rule

\[
\delta_{nm}=
\begin{cases}
1,&n=m,\\
0,&n\ne m.
\end{cases}
\]

For an orthonormal discrete basis, all the overlap calculations above become one statement:

\[
\langle n|m\rangle=\delta_{nm}.
\]

Read this as:

> “Bra n ket m equals delta n m.”

It means: compare the two basis labels. Equal labels give one; different labels give zero.

```go
// Given: n and m label elements of one chosen discrete orthonormal basis.
// The Kronecker delta is 1 when the labels are equal and 0 when they differ.
// In an orthonormal basis, ⟨n|m⟩ MUST equal δ_nm.
func kroneckerDelta(n, m int) float64 {
    if n == m {
        return 1
    }
    return 0
}

// Given: n and m label elements of one chosen discrete basis.
// Basis labels are assigned with the basis; they are not extracted from vector entries.
func isSameBasisLabel(n, m int) bool {
    return kroneckerDelta(n, m) == 1
}
```

For example, `isSameBasisLabel(0, 0)` is `true`, while `isSameBasisLabel(0, 1)` is `false`. This compares the labels assigned when the basis is defined; it is different from computing an inner product of the actual vectors.

## 4. Inner product and basis predicates

The inner-product helper conjugates the entries of its first argument. The predicates below are pedagogical floating-point checks; they assume equal-length vectors.

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

// Given: |φ⟩ and |ψ⟩ have coordinates in the same chosen finite basis.
// Under the physics convention, ⟨φ|ψ⟩ is conjugate-linear in φ and linear in ψ.
func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

// norm returns the length induced by inner.
// The real part of inner(ket, ket) SHOULD be nonnegative up to round-off.
func norm(ket []complex128) float64 {
    return math.Sqrt(real(inner(ket, ket)))
}

// Given: |ψ⟩ has coordinates in a space with the inner product used above.
// A normalized ket has norm 1. Floating-point approximations require a tolerance.
func isNormalized(ket []complex128, tolerance float64) bool {
    return math.Abs(norm(ket)-1) < tolerance
}

// Given: |φ⟩ and |ψ⟩ have coordinates in the same chosen finite basis.
// Orthogonal kets have zero inner product. Floating-point approximations use a tolerance.
func isOrthogonal(phi, psi []complex128, tolerance float64) bool {
    return cmplx.Abs(inner(phi, psi)) < tolerance
}

// Given: the collection contains coordinate kets in one chosen finite space.
// An orthonormal set has unit-norm kets and zero overlap between distinct kets.
// Bases and Coordinates establishes that such a set is a basis only if it also
// spans the target space; this helper checks orthonormality, not spanning.
func isOrthonormal(basis [][]complex128, tolerance float64) bool {
    for i := range basis {
        if !isNormalized(basis[i], tolerance) {
            return false
        }
        for j := range basis {
            if i != j && !isOrthogonal(basis[i], basis[j], tolerance) {
                return false
            }
        }
    }
    return true
}

// For slice representations, this checks conjugated coordinates only.
// A full matrix Hermitian-adjoint test must also check transpose orientation.
func isHermitianAdjointOf(bra, ket []complex128, tolerance float64) bool {
    if len(bra) != len(ket) {
        return false
    }
    for i := range ket {
        if cmplx.Abs(bra[i]-cmplx.Conj(ket[i])) >= tolerance {
            return false
        }
    }
    return true
}

func main() {
    ket0 := []complex128{1, 0}
    ket1 := []complex128{0, 1}
    basis := [][]complex128{ket0, ket1}
    tolerance := 1e-12

    fmt.Println(inner(ket0, ket0))               // (1+0i)
    fmt.Println(inner(ket0, ket1))               // (0+0i)
    fmt.Println(kroneckerDelta(0, 1))            // 0
    fmt.Println(isOrthonormal(basis, tolerance)) // true
    fmt.Println(isHermitianAdjointOf([]complex128{1, 0}, ket0, tolerance)) // true
}
```

## 5. Basis expansion and resolution of identity

Let

\[
|\eta\rangle=
\begin{pmatrix}a\\b\end{pmatrix}.
\]

The two basis overlaps are its components:

\[
\langle0|\eta\rangle=a,
\qquad
\langle1|\eta\rangle=b.
\]

Therefore the basis expansion is

\[
|\eta\rangle=|0\rangle\langle0|\eta\rangle+|1\rangle\langle1|\eta\rangle.
\]

The same statement can be written using the identity operator:

\[
I=|0\rangle\langle0|+|1\rangle\langle1|,
\qquad
I|\eta\rangle=|\eta\rangle.
\]

This is the two-dimensional version of the resolution of the identity:

\[
\sum_n|n\rangle\langle n|=I.
\]

## What this example does and does not show

This example shows discrete, finite-dimensional Dirac notation. It does not justify applying the same finite sums or ordinary normalized basis vectors to continuous labels such as position or ideal clock time.
