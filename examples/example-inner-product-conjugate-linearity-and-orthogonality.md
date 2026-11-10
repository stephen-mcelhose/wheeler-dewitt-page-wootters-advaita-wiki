---
{
  "schema_version": "2.0",
  "id": "example-inner-product-conjugate-linearity-and-orthogonality",
  "type": "example",
  "title": "Inner Products: Scaling, Conjugation, and Orthogonality",
  "summary": "Finite-dimensional examples of the physics inner-product convention, including conjugate-linearity, linearity, and zero overlap.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text"],
  "topics": ["inner-product-spaces", "dirac-notation", "orthogonality"],
  "teaches": ["calculate a complex inner product", "distinguish conjugate-linearity from linearity", "recognize orthogonal vectors"],
  "prerequisites": ["inner-product-spaces"],
  "action": "Calculate each bracket by conjugating the first vector, then compare the result with the stated scaling rule or orthogonality condition.",
  "non_conclusion": "These finite-dimensional examples illustrate the adopted inner-product convention only; they do not establish a measurement rule or a state-update rule.",
  "relationships": [
    {"type": "illustrates", "target": "inner-product-spaces"},
    {"type": "illustrates", "target": "dirac-notation"}
  ],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}
  ]
}
---

# Inner Products: Scaling, Conjugation, and Orthogonality

We use the physics convention: the inner product is **conjugate-linear in its first argument** and **linear in its second**. For column vectors in \(\mathbb C^2\), form a bra by taking the ket's conjugate transpose.

## Example 1 — \(\phi\) compared with \(\psi\)

Let

\[
|\phi\rangle=\begin{pmatrix}1+i\\5\end{pmatrix},
\qquad
|\psi\rangle=\begin{pmatrix}2\\i\end{pmatrix}.
\]

The bra associated with \(\phi\) is

\[
\langle\phi|=\begin{pmatrix}1-i&5\end{pmatrix}.
\]

Therefore,

\[
\langle\phi|\psi\rangle
=(1-i)\cdot2+5\cdot i
=2+3i.
\]

Use all three of these verbal forms for the same expression:

- **“Bra phi ket psi.”**
- **“The inner product of phi and psi.”**
- **“The overlap of phi with psi.”**

The first is the standard Dirac-notation reading. The second emphasizes the mathematical operation. The third is especially useful in quantum mechanics, where the complex number measures how the two vectors align. This overlap is generally complex; an inner product between two different vectors need not be real.

```go
package main

import (
    "fmt"
    "math/cmplx"
)

func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

func main() {
    phi := []complex128{1 + 1i, 5}
    psi := []complex128{2, 1i}
    fmt.Println(inner(phi, psi)) // (2+3i)
}
```

## Hermitian adjoint helper

For a ket represented in Go as a slice, the Hermitian adjoint produces the entries of the associated bra by complex-conjugating them. The row-versus-column orientation is supplied by the mathematical context: a Go slice itself has no row/column orientation.

\[
|\phi\rangle=\begin{pmatrix}1+i\\5\end{pmatrix}
\quad\Longrightarrow\quad
\langle\phi|=\begin{pmatrix}1-i&5\end{pmatrix}.
\]

```go
func hermitianAdjoint(ket []complex128) []complex128 {
    bra := make([]complex128, len(ket))
    for i, entry := range ket {
        bra[i] = cmplx.Conj(entry)
    }
    return bra
}
```

For example:

```go
phi := []complex128{1 + 1i, 5}
fmt.Println(hermitianAdjoint(phi)) // [(1-1i) (5+0i)]
```

When an actual matrix representation is needed, the Hermitian adjoint also transposes the matrix. For a ket column, this turns the column into a bra row while applying the same complex conjugation.

### Code note

The Go blocks in this example are **pedagogical excerpts**. They assume equal-length vectors and omit production checks such as length validation and floating-point tolerances.

## Example 2 — Why the first argument is conjugate-linear

Let \(a=1+i\). First scale \(\phi\) in the **first** argument:

\[
\langle a\phi|\psi\rangle
=a^*\langle\phi|\psi\rangle.
\]

Because \(a^*=1-i\) and \(\langle\phi|\psi\rangle=2+3i\),

\[
\langle (1+i)\phi|\psi\rangle
=(1-i)(2+3i)=5+i.
\]

The coefficient is conjugated when it comes out of the first argument.

```go
package main

import (
    "fmt"
    "math/cmplx"
)

func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

func main() {
    a := complex(1, 1)
    phi := []complex128{1 + 1i, 5}
    psi := []complex128{2, 1i}
    scaledPhi := []complex128{a * phi[0], a * phi[1]}

    fmt.Println(inner(scaledPhi, psi))          // (5+1i)
    fmt.Println(cmplx.Conj(a) * inner(phi, psi)) // (5+1i)
}
```

## Example 3 — Why the second argument is linear

Now scale \(\psi\) in the **second** argument by the same \(a=1+i\):

\[
\langle\phi|a\psi\rangle
=a\langle\phi|\psi\rangle.
\]

Thus,

\[
\langle\phi|(1+i)\psi\rangle
=(1+i)(2+3i)=-1+5i.
\]

The coefficient comes out unchanged from the second argument.

```go
package main

import (
    "fmt"
    "math/cmplx"
)

func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

func main() {
    a := complex(1, 1)
    phi := []complex128{1 + 1i, 5}
    psi := []complex128{2, 1i}
    scaledPsi := []complex128{a * psi[0], a * psi[1]}

    fmt.Println(inner(phi, scaledPsi)) // (-1+5i)
    fmt.Println(a * inner(phi, psi))   // (-1+5i)
}
```

## Example 4 — \(|0\rangle\) and \(|1\rangle\) have zero overlap

Let

\[
|0\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|1\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Then

\[
\langle0|1\rangle
=\begin{pmatrix}1&0\end{pmatrix}
\begin{pmatrix}0\\1\end{pmatrix}
=0.
\]

The vectors are **orthogonal**: \(|1\rangle\) has no component in the \(|0\rangle\) direction. If these are normalized state vectors and a projective measurement asks whether a system in \(|1\rangle\) is in the \(|0\rangle\) direction, the yes probability is

\[
|\langle0|1\rangle|^2=0.
\]

```go
package main

import (
    "fmt"
    "math/cmplx"
)

func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

func main() {
    ket0 := []complex128{1, 0}
    ket1 := []complex128{0, 1}
    overlap := inner(ket0, ket1)

    fmt.Println(overlap)                             // (0+0i)
    fmt.Println(cmplx.Abs(overlap) * cmplx.Abs(overlap)) // 0
}
```

## What these examples do and do not show

They show how the chosen complex inner-product convention controls scaling and orthogonality in a finite-dimensional vector space. They do not by themselves explain measurement dynamics.
