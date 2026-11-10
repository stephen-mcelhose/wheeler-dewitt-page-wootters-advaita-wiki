---
{
  "schema_version": "2.0",
  "id": "example-quantum-states-rays-and-normalization",
  "type": "example",
  "title": "Quantum States, Rays, and Normalization: One Direction, Many Vectors",
  "summary": "A self-contained example showing scalar multiples, normalization, global phase, same-ray testing, and why the zero vector has no ray.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text"],
  "topics": ["quantum-states-rays-and-normalization", "inner-product-spaces", "norms-distance-and-convergence"],
  "teaches": ["scale a complex vector", "calculate a norm", "normalize a nonzero vector", "recognize same-ray vectors", "distinguish a ray from a normalized representative", "recognize global phase"],
  "prerequisites": ["inner-product-spaces", "norms-distance-and-convergence", "hilbert-spaces"],
  "action": "Scale one nonzero vector, normalize the original and scaled vectors, compare them using a same-ray test, and identify the remaining global phase.",
  "non_conclusion": "This finite-dimensional example explains ray equivalence for pure state vectors. It does not describe mixed states, a measurement update, or a total ordering of quantum states.",
  "relationships": [
    {"type": "illustrates", "target": "quantum-states-rays-and-normalization"}
  ],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}
  ]
}
---

# Quantum States, Rays, and Normalization: One Direction, Many Vectors

## Prerequisites and local setup

This example uses a complex vector in \(\mathbb C^2\). The standard physics inner product is

\[
\langle\phi|\psi\rangle=\sum_j\phi_j^*\psi_j,
\]

where the star means complex conjugation. The norm of a vector is

\[
\|\psi\|=\sqrt{\langle\psi|\psi\rangle}.
\]

We start with the nonzero ket

\[
|\psi\rangle=\begin{pmatrix}1+i\\5\end{pmatrix}.
\]

Its self-inner-product and norm are

\[
\langle\psi|\psi\rangle=(1-i)(1+i)+5\cdot5=27,
\qquad
\|\psi\|=\sqrt{27}.
\]

## 1. Scale the vector

Let

\[
c=2-i.
\]

Scale \(|\psi\rangle\) by this nonzero complex number:

\[
|\chi\rangle=c|\psi\rangle
=(2-i)\begin{pmatrix}1+i\\5\end{pmatrix}
=\begin{pmatrix}3+i\\10-5i\end{pmatrix}.
\]

This is called **scalar multiplication** or **scaling**. It produces a different vector, because it generally changes the vector's norm.

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

func inner(phi, psi []complex128) complex128 {
    var total complex128
    for i := range phi {
        total += cmplx.Conj(phi[i]) * psi[i]
    }
    return total
}

func norm(ket []complex128) float64 {
    return math.Sqrt(real(inner(ket, ket)))
}

func scale(scalar complex128, ket []complex128) []complex128 {
    scaled := make([]complex128, len(ket))
    for i, entry := range ket {
        scaled[i] = scalar * entry
    }
    return scaled
}

func main() {
    psi := []complex128{1 + 1i, 5}
    c := complex(2, -1)
    chi := scale(c, psi)

    fmt.Println(chi) // [(3+1i) (10-5i)]
    fmt.Println(norm(psi))
    fmt.Println(norm(chi))
}
```

The scale factor has magnitude

\[
|c|=|2-i|=\sqrt{2^2+(-1)^2}=\sqrt5.
\]

Therefore the norm scales by that magnitude:

\[
\|\chi\|=\|c\psi\|=|c|\,\|\psi\|=\sqrt5\sqrt{27}=\sqrt{135}.
\]

## 2. Normalize each vector

A **normalized representative** has norm one. For any nonzero vector, divide by its norm:

\[
|\widehat\psi\rangle=\frac{|\psi\rangle}{\|\psi\|},
\qquad
|\widehat\chi\rangle=\frac{|\chi\rangle}{\|\chi\|}.
\]

For the scaled vector \(|\chi\rangle=c|\psi\rangle\), this gives

\[
|\widehat\chi\rangle
=\frac{c}{|c|}|\widehat\psi\rangle.
\]

The factor \(c/|c|\) has magnitude one. It is a global phase:

\[
\frac{c}{|c|}=\frac{2-i}{\sqrt5}=e^{i\theta}
\]

for some angle \(\theta\). Thus normalization removes the scale magnitude but can leave a global phase.

```go
func normalize(ket []complex128) ([]complex128, error) {
    length := norm(ket)
    if length == 0 {
        return nil, fmt.Errorf("the zero vector cannot be normalized")
    }

    normalized := make([]complex128, len(ket))
    for i, entry := range ket {
        normalized[i] = entry / complex(length, 0)
    }
    return normalized, nil
}
```

The zero vector must be rejected because its norm is zero, so division by its norm is undefined. It also has no direction and therefore does not determine a ray.

## 3. Same ray, not necessarily the same vector

The ray of \(|\psi\rangle\) is the set of all its nonzero scalar multiples:

\[
[\psi]=\{c|\psi\rangle:c\in\mathbb C,\ c\ne0\}.
\]

The vectors \(|\psi\rangle\) and \(|\chi\rangle\) are not equal as vectors, but they lie on the same ray because

\[
|\chi\rangle=(2-i)|\psi\rangle.
\]

For nonzero vectors, an equivalent same-ray test is

\[
\frac{|\langle\chi|\psi\rangle|}{\|\chi\|\,\|\psi\|}=1.
\]

The numerator is the magnitude of their overlap. Dividing by both norms removes the dependence on scale. A result of one means the vectors are parallel in Hilbert-space geometry, up to a complex phase and magnitude.

```go
func sameRay(phi, psi []complex128, tolerance float64) bool {
    phiNorm := norm(phi)
    psiNorm := norm(psi)
    if phiNorm == 0 || psiNorm == 0 {
        return false // the zero vector does not determine a ray
    }

    normalizedOverlap := cmplx.Abs(inner(phi, psi)) / (phiNorm * psiNorm)
    return math.Abs(normalizedOverlap-1) < tolerance
}

func main() {
    psi := []complex128{1 + 1i, 5}
    chi := scale(complex(2, -1), psi)

    fmt.Println(sameRay(psi, chi, 1e-12)) // true
}
```

## 4. Global phase does not change the ray

If \(|\widehat\psi\rangle\) is normalized, then

\[
|\widehat\psi\rangle
\mapsto e^{i\theta}|\widehat\psi\rangle
\]

changes its vector representative but not its ray. Both representatives are normalized because

\[
\left\|e^{i\theta}|\widehat\psi\rangle\right\|
=|e^{i\theta}|\,\|\widehat\psi\|
=1.
\]

This is why a pure quantum state is represented by a ray rather than by one uniquely selected vector.

## 5. A lazy stream of representatives

A ray contains infinitely many nonzero scalar multiples, so code cannot enumerate the entire ray. It can, however, lazily generate a chosen sequence of representatives.

For a normalized representative \(|\widehat\psi\rangle\), every normalized representative of the same ray has the form

\[
e^{i\theta}|\widehat\psi\rangle.
\]

The following generator samples phases in equal steps. It generates a selected countable stream through the ray; it does not enumerate the full ray, because the full set of nonzero complex scalar multiples is uncountable.

```go
// Given: representative is a normalized nonzero ket and phaseStep is a chosen real angle.
// Every generated ket MUST have norm 1 and belong to the same ray as representative.
// The stream samples selected phase representatives; it does not enumerate the full ray.
type RayPhaseGenerator struct {
    representative []complex128
    phaseStep      float64
    index          int
}

func (g *RayPhaseGenerator) Next() []complex128 {
    theta := float64(g.index) * g.phaseStep
    phase := cmplx.Exp(complex(0, theta))
    g.index++

    next := make([]complex128, len(g.representative))
    for i, entry := range g.representative {
        next[i] = phase * entry
    }
    return next
}
```

For example, a phase step of \(\pi/4\) produces

\[
|\widehat\psi\rangle,
\quad e^{i\pi/4}|\widehat\psi\rangle,
\quad e^{i\pi/2}|\widehat\psi\rangle,
\quad\ldots
\]

Each ket is a normalized representative of the same ray.

## 6. Appendix — Directional generalization: supplied scalar streams

The phase generator above is deliberately specialized: it chooses equal phase steps and emits normalized representatives. A more general design separates **how scalars are selected** from **which ket is scaled**.

Mathematically, for a chosen sequence of nonzero scalars \(c_0,c_1,c_2,\ldots\), the construction is

\[
c_k\longmapsto c_k|\psi\rangle.
\]

The following higher-order shape first accepts a lazy scalar stream and then accepts the ket. It is a directional generalization, not a replacement for the concrete phase generator above.

```go
// ScaleGenerator accepts a ket and lazily returns vectors obtained by scaling it.
// The scalar-selection pattern is configured before the ket is supplied.
type ScaleGenerator func(ket []complex128) iter.Seq[[]complex128]

// Given: scalars supplies a chosen lazy sequence of nonzero complex scalars.
// Given: ket is a nonzero coordinate ket in a chosen finite basis.
// Model scope: the returned stream samples selected representatives; it does not
// enumerate the full uncountable ray of ket.
// Each emitted ket MUST belong to the ray of ket.
func scaleRepresentatives(
    scalars iter.Seq[complex128],
) ScaleGenerator {
    return func(ket []complex128) iter.Seq[[]complex128] {
        return func(yield func([]complex128) bool) {
            for scalar := range scalars {
                if scalar == 0 {
                    continue
                }

                representative := make([]complex128, len(ket))
                for i, entry := range ket {
                    representative[i] = scalar * entry
                }

                if !yield(representative) {
                    return
                }
            }
        }
    }
}
```

The two-stage call keeps the scalar-selection pattern separate from the ket. In a `range` loop, apply the configured generator directly to the ket:

```go
streamScaledKets := scaleRepresentatives(nonzeroScalars)

for representative := range streamScaledKets(psi) {
    // Do something with each lazily emitted scaled ket.
}
```

The loop requests representatives lazily, one at a time. With an infinite scalar stream, the loop needs a stopping condition when the intended work is finite. The scalar stream can describe selected phase factors, changing magnitudes, alternating signs, or another chosen pattern. A scalar equal to zero is skipped because \(0|\psi\rangle\) is the zero vector and is not a representative of the ray.

## 7. Rays do not have a natural comparator

The same-ray predicate answers a yes/no question: do two nonzero vectors represent the same ray?

There is no canonical order such as

\[
[\phi]<[\psi].
\]

A program can impose an arbitrary order for sorting data, but that order depends on a chosen representation and has no intrinsic physical or mathematical meaning for rays.

## What this example does and does not show

This example shows how a nonzero vector, its scalar multiples, and its normalized representatives belong to one ray. It does not claim that every quantum state is pure, explain mixed states, or specify a general measurement update.
