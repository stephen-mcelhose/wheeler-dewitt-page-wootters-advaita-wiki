---
{
  "schema_version": "2.0",
  "id": "example-norms-distance-cauchy-completeness",
  "type": "example",
  "title": "Norms, Distance, Cauchy Sequences, and Completeness",
  "summary": "A step-by-step finite-dimensional example: subtract vectors, measure the norm, examine a Cauchy sequence, and identify why its limit remains in a complete space.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text"],
  "topics": ["norms-distance-and-convergence", "hilbert-spaces", "inner-product-spaces"],
  "teaches": ["subtract vectors", "calculate an induced norm", "calculate norm-induced distance", "recognize a Cauchy sequence", "distinguish convergence from completeness"],
  "prerequisites": ["inner-product-spaces", "norms-distance-and-convergence"],
  "action": "Work through subtraction, norm, distance, the distance between late sequence terms, and the limit of the sequence in the same vector space.",
  "non_conclusion": "This finite-dimensional example illustrates the standard norm on C². It does not establish the properties of every normed space or replace the general definition of completeness.",
  "relationships": [
    {"type": "illustrates", "target": "norms-distance-and-convergence"},
    {"type": "illustrates", "target": "hilbert-spaces"}
  ],
  "sources": [
    {"title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis", "url": "https://doi.org/10.1016/C2013-0-10329-X", "persistent_id": "doi:10.1016/C2013-0-10329-X"}
  ]
}
---

# Norms, Distance, Cauchy Sequences, and Completeness

This example uses the standard inner-product norm on \(\mathbb C^2\):

\[
\left\|\begin{pmatrix}z_1\\z_2\end{pmatrix}\right\|
=\sqrt{|z_1|^2+|z_2|^2}.
\]

## Example 1 — Vector subtraction

Let

\[
|\phi\rangle=\begin{pmatrix}3\\1\end{pmatrix},
\qquad
|\psi\rangle=\begin{pmatrix}1\\2\end{pmatrix}.
\]

To ask how far apart the vectors are, first form their difference:

\[
|\phi\rangle-|\psi\rangle
=\begin{pmatrix}3\\1\end{pmatrix}
-\begin{pmatrix}1\\2\end{pmatrix}
=\begin{pmatrix}2\\-1\end{pmatrix}.
\]

The difference vector is the displacement from \(|\psi\rangle\) to \(|\phi\rangle\).

```go
package main

import "fmt"

func subtract(phi, psi []complex128) []complex128 {
    difference := make([]complex128, len(phi))
    for i := range phi {
        difference[i] = phi[i] - psi[i]
    }
    return difference
}

func main() {
    phi := []complex128{3, 1}
    psi := []complex128{1, 2}
    fmt.Println(subtract(phi, psi)) // [(2+0i) (-1+0i)]
}
```

### Subtraction with imaginary components

Vector subtraction works component by component for complex entries too. Let

\[
|\alpha\rangle=\begin{pmatrix}1+i\\2-3i\end{pmatrix},
\qquad
|\beta\rangle=\begin{pmatrix}2-i\\4+i\end{pmatrix}.
\]

Then

\[
|\alpha\rangle-|\beta\rangle
=\begin{pmatrix}(1+i)-(2-i)\cr(2-3i)-(4+i)\end{pmatrix}
=\begin{pmatrix}-1+2i\\-2-4i\end{pmatrix}.
\]

Subtracting a complex number means subtracting both its real and imaginary parts. For example,

\[
(1+i)-(2-i)=(1-2)+(1-(-1))i=-1+2i.
\]

```go
package main

import "fmt"

func subtract(alpha, beta []complex128) []complex128 {
    difference := make([]complex128, len(alpha))
    for i := range alpha {
        difference[i] = alpha[i] - beta[i]
    }
    return difference
}

func main() {
    alpha := []complex128{1 + 1i, 2 - 3i}
    beta := []complex128{2 - 1i, 4 + 1i}
    fmt.Println(subtract(alpha, beta)) // [(-1+2i) (-2-4i)]
}
```

## Example 2 — Norm and induced distance

The norm of the difference vector is

\[
\left\||\phi\rangle-|\psi\rangle\right\|
=\left\|\begin{pmatrix}2\\-1\end{pmatrix}\right\|
=\sqrt{2^2+(-1)^2}
=\sqrt5.
\]

Therefore the norm induces the distance

\[
d(\phi,\psi)=\|\phi-\psi\|=\sqrt5.
\]

The norm of a vector is its distance from the zero vector:

\[
\|\phi\|=d(\phi,0).
\]

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

func norm(vector []complex128) float64 {
    var squared float64
    for _, entry := range vector {
        magnitude := cmplx.Abs(entry)
        squared += magnitude * magnitude
    }
    return math.Sqrt(squared)
}

func main() {
    difference := []complex128{2, -1}
    fmt.Println(norm(difference)) // about 2.2360679, which is sqrt(5)
}
```

The norm is the square root of the squared component magnitudes, so this result is \(\sqrt5\).

## Example 3 — A Cauchy sequence

Define a sequence of vectors:

\[
|\psi_n\rangle=\begin{pmatrix}1+1/n\\2-1/n\end{pmatrix},
\qquad n=1,2,3,\ldots
\]

Its proposed limit is

\[
|\psi\rangle=\begin{pmatrix}1\\2\end{pmatrix}.
\]

The distance from the \(n\)-th vector to this limit is

\[
\|\psi_n-\psi\|
=\left\|\begin{pmatrix}1/n\\-1/n\end{pmatrix}\right\|
=\frac{\sqrt2}{n}.
\]

As \(n\) increases, this distance approaches zero. Thus \(|\psi_n\rangle\) converges to \(|\psi\rangle\).

It is also Cauchy. For large \(m\) and \(n\),

\[
\|\psi_n-\psi_m\|
=\sqrt2\left|\frac1n-\frac1m\right|,
\]

which can be made arbitrarily small by choosing both indices sufficiently large.

```go
package main

import (
    "fmt"
    "math"
)

func distanceToLimit(n float64) float64 {
    return math.Sqrt(2) / n
}

func main() {
    fmt.Println(distanceToLimit(10))  // about 0.1414
    fmt.Println(distanceToLimit(100)) // about 0.01414
}
```

A Cauchy sequence is described without naming its limit first: its later terms become arbitrarily close to each other. In this example, we can see both facts: the vectors become close to one another and converge to \(|\psi\rangle\).

## Example 4 — Completeness

The limit

\[
|\psi\rangle=\begin{pmatrix}1\\2\end{pmatrix}
\]

is itself an element of \(\mathbb C^2\). This particular calculation therefore stays inside the same vector space after taking the limit.

More generally, finite-dimensional normed vector spaces, including \(\mathbb C^2\) with its standard norm, are known to be complete. This sequence illustrates that theorem; it does not prove completeness from one sequence alone. Completeness guarantees that **every** Cauchy sequence has a limit that is still in the space.

For contrast, the rational numbers \(\mathbb Q\) are not complete with the ordinary distance. Rational approximations to \(\sqrt2\) can form a Cauchy sequence, but their limit \(\sqrt2\) is not rational. The real numbers \(\mathbb R\) contain that limit; \(\mathbb Q\) does not.

In quantum mechanics, a Hilbert space is complete under its norm-induced distance. This ensures that valid approximation sequences do not converge to an object outside the state space.

## What these examples do and do not show

They show the relationship:

\[
\text{inner product}\ \longrightarrow\ \text{norm}\ \longrightarrow\ \text{distance}\ \longrightarrow\ \text{convergence and completeness}.
\]

They do not prove completeness of every Hilbert space from this one finite-dimensional example.
