---
{
  "schema_version": "2.0",
  "id": "example-projection-operators-rank-and-orthogonality",
  "type": "example",
  "title": "Projection Operators: Rank, Orthogonality, and Components",
  "summary": "A self-contained finite-dimensional example of rank-one, rank-two, and rank-three orthogonal projectors, including an isOrthogonalProjector predicate and explicit applications of Pa|psi⟩ = |a⟩⟨a|psi⟩.",
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
    "projection-operators",
    "dirac-notation",
    "bases-and-coordinates",
    "inner-product-spaces"
  ],
  "teaches": [
    "distinguish vector norm from operator rank",
    "construct a rank-one projector",
    "compare rank-one rank-two and rank-three projectors",
    "test an orthogonal projector",
    "apply a projector to a ket",
    "distinguish projection from normalized state update"
  ],
  "prerequisites": [
    "inner-product-spaces",
    "norms-distance-and-convergence",
    "bases-and-coordinates",
    "dirac-notation"
  ],
  "action": "Construct projectors onto one, two, and three basis directions; apply the rank-one projector to a general ket; and check idempotence and self-adjointness with a finite-dimensional predicate.",
  "non_conclusion": "This finite-dimensional example illustrates orthogonal projectors in declared orthonormal bases. It does not establish a general measurement update rule, handle unbounded projection-related operators, or replace domain conditions in infinite-dimensional Hilbert spaces.",
  "relationships": [
    {
      "type": "illustrates",
      "target": "projection-operators"
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

# Projection Operators: Rank, Orthogonality, and Components

## Prerequisites and local setup

A **projector** is an operator \(P\) satisfying

\[
P^2=P.
\]

Applying it twice gives the same result as applying it once. An **orthogonal projector** also satisfies

\[
P^\dagger=P.
\]

The dagger is the Hermitian adjoint. In the finite orthonormal coordinate bases used here, it is the conjugate transpose of the matrix.

**Model scope:** The first two examples use the declared orthonormal basis \((|0\rangle,|1\rangle)\) of \(\mathbb C^2\). The rank-three comparison uses the declared orthonormal basis \((|0\rangle,|1\rangle,|2\rangle)\) of \(\mathbb C^3\). These finite matrix models do not replace general Hilbert-space domain questions.

**Convention:** This wiki uses the physics inner-product convention: the first argument is conjugate-linear and the second is linear.

## 1. Rank is not vector length

The **rank** of an operator is the dimension of its image: the number of independent output directions it can produce. It is not the norm or length of a vector.

For a projector, rank is the dimension of the subspace kept by the projection:

- a rank-one projector keeps one independent direction;
- a rank-two projector keeps a two-dimensional subspace;
- a rank-three projector can keep all three independent directions of \(\mathbb C^3\).

## 2. A rank-one orthogonal projector

Use the normalized basis ket

\[
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
\langle0|=\begin{pmatrix}1&0\end{pmatrix}.
\]

The outer product is

\[
P_0=|0\rangle\langle0|
=\begin{pmatrix}1\\0\end{pmatrix}
\begin{pmatrix}1&0\end{pmatrix}
=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Every output of \(P_0\) is a scalar multiple of \(|0\rangle\), so its image has one independent direction. Therefore \(P_0\) has rank one.

It is a projector because

\[
P_0^2=
\begin{pmatrix}1&0\\0&0\end{pmatrix}
\begin{pmatrix}1&0\\0&0\end{pmatrix}
=\begin{pmatrix}1&0\\0&0\end{pmatrix}
=P_0.
\]

It is orthogonal because

\[
P_0^\dagger=P_0.
\]

## 3. Apply \(P_a|\psi\rangle=|a\rangle\langle a|\psi\rangle\)

Let

\[
|\psi\rangle=
\begin{pmatrix}3+i\\2-i\end{pmatrix}.
\]

Project it onto the \(|0\rangle\) direction. First calculate the overlap:

\[
\langle0|\psi\rangle
=\begin{pmatrix}1&0\end{pmatrix}
\begin{pmatrix}3+i\\2-i\end{pmatrix}
=3+i.
\]

Then multiply that scalar by the target ket:

\[
P_0|\psi\rangle
=|0\rangle\langle0|\psi\rangle
=\begin{pmatrix}1\\0\end{pmatrix}(3+i)
=\begin{pmatrix}3+i\\0\end{pmatrix}.
\]

Read this as:

> “P sub zero acting on ket psi equals ket zero times bra zero ket psi.”

The projector keeps the \(|0\rangle\) component and removes the component along \(|1\rangle\):

\[
|\psi\rangle=(3+i)|0\rangle+(2-i)|1\rangle,
\qquad
P_0|\psi\rangle=(3+i)|0\rangle.
\]

The projected vector is generally **not normalized**. Projection is not itself a complete state-update rule. A sharp measurement update would additionally require a declared measurement model and, for a nonzero selected outcome, normalization of the projected component.

## 4. A rank-two orthogonal projector

In \(\mathbb C^2\), the identity operator keeps both basis directions:

\[
I_2=|0\rangle\langle0|+|1\rangle\langle1|
=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Its image is all of \(\mathbb C^2\), which has two independent directions. Thus \(I_2\) has rank two.

\[
I_2|\psi\rangle=|\psi\rangle.
\]

This is still an orthogonal projector:

\[
I_2^2=I_2,
\qquad
I_2^\dagger=I_2.
\]

Rank two does not mean “twice the length.” It means that the projector keeps a two-dimensional subspace.

## 5. A rank-three orthogonal projector

In \(\mathbb C^3\), use the declared orthonormal basis \((|0\rangle,|1\rangle,|2\rangle)\). The identity operator is

\[
I_3=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
\]

It keeps all three independent directions in \(\mathbb C^3\), so it has rank three:

\[
I_3^2=I_3,
\qquad
I_3^\dagger=I_3.
\]

For comparison, the projector

\[
P_{01}=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&0
\end{pmatrix}
\]

has rank two: it keeps the plane spanned by \(|0\rangle\) and \(|1\rangle\), while removing the \(|2\rangle\) component.

## 6. Pedagogical Go checks in \(\mathbb C^2\)

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

// Given: |a⟩ is normalized and has two coordinates in the chosen C² basis.
// Model scope: this constructs a rank-one matrix in C² only.
func rankOneProjector2D(a []complex128) Matrix2 {
    return Matrix2{
        {a[0] * cmplx.Conj(a[0]), a[0] * cmplx.Conj(a[1])},
        {a[1] * cmplx.Conj(a[0]), a[1] * cmplx.Conj(a[1])},
    }
}

// Given: P is a 2×2 matrix and |ψ⟩ has two coordinates.
// Model scope: this multiplies a finite C² matrix by a C² coordinate ket.
func applyMatrix2D(P Matrix2, psi []complex128) []complex128 {
    return []complex128{
        P[0][0]*psi[0] + P[0][1]*psi[1],
        P[1][0]*psi[0] + P[1][1]*psi[1],
    }
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

// Given: this example represents the identity operator in the declared C² basis.
// The identity operator MUST return every C² coordinate ket unchanged.
func identityMatrix2D() Matrix2 {
    return Matrix2{{1, 0}, {0, 1}}
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
// This predicate checks those two matrix identities within floating-point tolerance.
func isOrthogonalProjector2D(P Matrix2, tolerance float64) bool {
    return matricesClose2D(multiplyMatrix2D(P, P), P, tolerance) &&
        matricesClose2D(hermitianAdjoint2D(P), P, tolerance)
}

func main() {
    ket0 := []complex128{1, 0}
    psi := []complex128{3 + 1i, 2 - 1i}
    P0 := rankOneProjector2D(ket0)
    I2 := identityMatrix2D()
    tolerance := 1e-12

    fmt.Println(inner(ket0, psi))                       // (3+1i)
    fmt.Println(applyMatrix2D(P0, psi))                 // [(3+1i) (0+0i)]
    fmt.Println(isOrthogonalProjector2D(P0, tolerance)) // true
    fmt.Println(applyMatrix2D(I2, psi))                 // [(3+1i) (2-1i)]
    fmt.Println(isOrthogonalProjector2D(I2, tolerance)) // true
}
```

The function `isOrthogonalProjector2D` is intentionally narrow. It establishes neither a general arbitrary-dimensional rank calculation nor the domain conditions needed for infinite-dimensional operator theory.

## What this example does and does not show

This example shows rank-one, rank-two, and rank-three orthogonal projectors in finite-dimensional declared orthonormal bases. It distinguishes operator rank from vector norm and shows that \(P_a|\psi\rangle=|a\rangle\langle a|\psi\rangle\) extracts a component. It does not establish a general physical measurement-update rule, arbitrary-dimensional numerical linear algebra, or domain issues for infinite-dimensional Hilbert-space operators.
