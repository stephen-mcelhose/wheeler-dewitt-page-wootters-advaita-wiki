---
{
  "schema_version": "2.0",
  "id": "example-spectra-eigenvalues-and-generalized-bases",
  "type": "example",
  "title": "Spectra: Eigenvalues, Eigenvectors, and Why Continuous Labels Need Care",
  "summary": "A self-contained finite C² eigenvalue example that contrasts ordinary normalized eigenvectors with formal continuous-spectrum notation.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text"],
  "topics": ["spectral-notation", "operators-and-domains", "dirac-notation", "bases-and-coordinates"],
  "teaches": ["identify eigenvalues and eigenvectors", "verify an eigenvalue equation", "distinguish a finite discrete spectrum from continuous notation", "recognize why generalized eigenvectors need qualification"],
  "prerequisites": ["inner-product-spaces", "norms-distance-and-convergence", "hilbert-spaces", "bases-and-coordinates", "dirac-notation", "projection-operators"],
  "action": "Apply a diagonal operator to two basis kets, identify its eigenvalues and eigenvectors, and compare the ordinary finite-dimensional result with the formal continuous-spectrum notation used later.",
  "non_conclusion": "This finite-dimensional matrix example does not prove the spectral theorem for unbounded operators or justify treating continuous-spectrum kets as ordinary normalized Hilbert-space vectors.",
  "relationships": [
    {"type": "illustrates", "target": "spectral-notation"}
  ],
  "sources": [
    {"title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis", "url": "https://doi.org/10.1016/C2013-0-10329-X", "persistent_id": "doi:10.1016/C2013-0-10329-X"},
    {"title": "P. A. M. Dirac, The Principles of Quantum Mechanics", "url": "https://global.oup.com/academic/product/the-principles-of-quantum-mechanics-9780198520115", "persistent_id": "ISBN:9780198520115"}
  ]
}
---

# Spectra: Eigenvalues, Eigenvectors, and Why Continuous Labels Need Care

## Prerequisites and local setup

**Model scope:** Work in the finite two-dimensional complex Hilbert space \(\mathbb C^2\), with declared orthonormal basis

\[
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
\]

An **eigenvector** \(|a\rangle\ne0\) of an operator \(\hat A\) has an associated **eigenvalue** \(a\) when

\[
\hat A|a\rangle=a|a\rangle.
\]

The operator changes the vector only by scalar multiplication, so it preserves that vector’s direction.

## 1. A finite operator with two eigenvalues

Consider the operator

\[
\hat A=
\begin{pmatrix}
2&0\\
0&5
\end{pmatrix}.
\]

Apply it to \(|0\rangle\):

\[
\hat A|0\rangle
=
\begin{pmatrix}
2&0\\
0&5
\end{pmatrix}
\begin{pmatrix}1\\0\end{pmatrix}
=
\begin{pmatrix}2\\0\end{pmatrix}
=2|0\rangle.
\]

Thus \(|0\rangle\) is an eigenvector with eigenvalue \(2\).

Apply it to \(|1\rangle\):

\[
\hat A|1\rangle
=
\begin{pmatrix}
2&0\\
0&5
\end{pmatrix}
\begin{pmatrix}0\\1\end{pmatrix}
=
\begin{pmatrix}0\\5\end{pmatrix}
=5|1\rangle.
\]

Thus \(|1\rangle\) is an eigenvector with eigenvalue \(5\).

The spectrum in this finite model is the discrete set

\[
\{2,5\}.
\]

## 2. A vector that is not an eigenvector

Let

\[
|+\rangle=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}.
\]

It is normalized, but applying \(\hat A\) gives

\[
\hat A|+\rangle
=
\frac1{\sqrt2}\begin{pmatrix}2\\5\end{pmatrix}.
\]

This is not a single scalar times \(|+\rangle\), because its two components would require the same scalar to be both \(2\) and \(5\). Therefore \(|+\rangle\) is not an eigenvector of \(\hat A\).

Normalization and being an eigenvector are different properties.

## 3. Discrete orthonormal eigenbasis

The two eigenvectors form a discrete orthonormal basis:

\[
\langle0|0\rangle=1,
\qquad
\langle1|1\rangle=1,
\qquad
\langle0|1\rangle=0.
\]

In this finite example, the identity resolution is

\[
I=|0\rangle\langle0|+|1\rangle\langle1|.
\]

Every ket can be expanded in this basis. For example,

\[
|+\rangle
=\frac1{\sqrt2}|0\rangle+\frac1{\sqrt2}|1\rangle.
\]

## 4. Why continuous labels need care

A position-like notation may formally use labels such as \(|x\rangle\) and equations such as

\[
\langle x|x'\rangle=\delta(x-x').
\]

This is not the same type of statement as \(\langle0|1\rangle=0\) for two ordinary normalized kets in \(\mathbb C^2\). The position-like \(|x\rangle\) is generally a generalized eigenvector: a distributional object, not an ordinary normalized Hilbert-space vector.

Likewise, the formal continuous identity resolution

\[
\int dx\,|x\rangle\langle x|=I
\]

requires a generalized spectral setting and must not be read as an ordinary finite sum of normalized vectors.

## 5. Pedagogical Go check in \(\mathbb C^2\)

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

type Matrix2 [2][2]complex128

// Given: A is a finite 2×2 operator and ket has coordinates in the same C² basis.
// Model scope: this is finite-dimensional matrix multiplication only.
func applyMatrix2D(A Matrix2, ket []complex128) []complex128 {
    return []complex128{
        A[0][0]*ket[0] + A[0][1]*ket[1],
        A[1][0]*ket[0] + A[1][1]*ket[1],
    }
}

// Given: ket is nonzero and A acts on the same finite C² coordinate space.
// An eigenvector MUST satisfy A|v⟩ = λ|v⟩ for one scalar λ.
// Model scope: this helper chooses the first nonzero coordinate to infer λ.
func eigenvalueIfEigenvector2D(A Matrix2, ket []complex128, tolerance float64) (complex128, bool) {
    if len(ket) != 2 || cmplx.Abs(ket[0]) < tolerance && cmplx.Abs(ket[1]) < tolerance {
        return 0, false
    }

    result := applyMatrix2D(A, ket)
    index := 0
    if cmplx.Abs(ket[index]) < tolerance {
        index = 1
    }
    value := result[index] / ket[index]

    for i := range ket {
        if cmplx.Abs(result[i]-value*ket[i]) >= tolerance {
            return 0, false
        }
    }
    return value, true
}

func main() {
    A := Matrix2{{2, 0}, {0, 5}}
    ket0 := []complex128{1, 0}
    ket1 := []complex128{0, 1}
    ketPlus := []complex128{1 / math.Sqrt2, 1 / math.Sqrt2}
    tolerance := 1e-12

    fmt.Println(eigenvalueIfEigenvector2D(A, ket0, tolerance))    // (2+0i) true
    fmt.Println(eigenvalueIfEigenvector2D(A, ket1, tolerance))    // (5+0i) true
    fmt.Println(eigenvalueIfEigenvector2D(A, ketPlus, tolerance)) // 0 false
}
```

## What this example does and does not show

This example shows ordinary finite-dimensional eigenvalues and eigenvectors for one diagonal \(2\times2\) operator. It does not prove the spectral theorem, calculate spectra of arbitrary matrices, handle degeneracy, establish self-adjointness, or justify continuous-spectrum notation as ordinary normalized-vector notation.
