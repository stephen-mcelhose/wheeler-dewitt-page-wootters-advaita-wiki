---
{
  "schema_version": "2.0",
  "id": "example-integrated-hilbert-space-basics",
  "type": "example",
  "title": "Hilbert-Space Basics: Norm, Orthogonality, Projector, and Born Rule",
  "summary": "One finite-dimensional complex-vector example connecting Hermitian adjoints, normalization, rays, orthogonality, projectors, and Born-rule probabilities.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "derivation"],
  "modality": ["text"],
  "topics": ["hilbert-spaces", "inner-product-spaces", "quantum-states-rays-and-normalization", "projection-operators", "born-rule-and-quantum-probability"],
  "teaches": ["form a Hermitian adjoint", "calculate a norm", "normalize a vector", "test orthogonality", "construct a rank-one projector", "calculate a Born-rule probability", "distinguish a vector from its ray"],
  "prerequisites": ["inner-product-spaces", "norms-distance-and-convergence", "hilbert-spaces", "quantum-states-rays-and-normalization", "dirac-notation", "projection-operators", "born-rule-and-quantum-probability"],
  "action": "Follow one pair of vectors through adjoint, norm, normalization, orthogonality, projection, and probability calculations.",
  "non_conclusion": "This finite-dimensional calculation illustrates the standard physics convention and a projective yes/no measurement model. It does not describe a general measurement update or every type of quantum measurement.",
  "relationships": [
    {"type": "illustrates", "target": "hilbert-spaces"},
    {"type": "illustrates", "target": "projection-operators"},
    {"type": "illustrates", "target": "born-rule-and-quantum-probability"}
  ],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}
  ]
}
---

# Hilbert-Space Basics: Norm, Orthogonality, Projector, and Born Rule

This example uses the physics convention: the inner product is conjugate-linear in its first argument and linear in its second.

Let

\[
|\psi\rangle=
\begin{pmatrix}1+i\\1-i\end{pmatrix},
\qquad
|\phi\rangle=
\begin{pmatrix}1+i\\-(1-i)\end{pmatrix}.
\]

## 1. Hermitian adjoint: ket to bra

The Hermitian adjoint is written \(\dagger\). For a ket column, it complex-conjugates the entries and changes the column into a row:

\[
\langle\psi|
=\left(|\psi\rangle\right)^\dagger
=\begin{pmatrix}1-i&1+i\end{pmatrix}.
\]

**Code note:** The Go fragments below are pedagogical excerpts. They assume compatible vector lengths; `normalize` also assumes a nonzero norm. Production numerical code should validate inputs and use tolerances for floating-point comparisons.

```go
func hermitianAdjoint(ket []complex128) []complex128 {
    bra := make([]complex128, len(ket))
    for i, entry := range ket {
        bra[i] = cmplx.Conj(entry)
    }
    return bra
}
```

For a vector stored as a Go slice, this function returns the conjugated entries. The surrounding mathematics supplies the row orientation of the bra. A full matrix Hermitian adjoint also transposes rows and columns.

## 2. Self-inner-product and norm

The self-inner-product is

\[
\langle\psi|\psi\rangle
=(1-i)(1+i)+(1+i)(1-i)
=2+2=4.
\]

Therefore the norm is

\[
\|\psi\|=\sqrt{\langle\psi|\psi\rangle}=2.
\]

The **normalization factor** is \(1/\|\psi\|=1/2\). Define

\[
|\widehat\psi\rangle
=\frac{|\psi\rangle}{\|\psi\|}
=\frac12\begin{pmatrix}1+i\\1-i\end{pmatrix}.
\]

Then

\[
\langle\widehat\psi|\widehat\psi\rangle=1.
\]

The vector \(|\phi\rangle\) has the same norm:

\[
\langle\phi|\phi\rangle=4,
\qquad
\|\phi\|=2,
\qquad
|\widehat\phi\rangle
=\frac{|\phi\rangle}{\|\phi\|}
=\frac12\begin{pmatrix}1+i\\-(1-i)\end{pmatrix}.
\]

```go
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

func normalize(ket []complex128) ([]complex128, error) {
    length := norm(ket)
    if length == 0 {
        return nil, errors.New("the zero vector cannot be normalized")
    }

    scale := complex(1/length, 0)
    normalized := make([]complex128, len(ket))
    for i, entry := range ket {
        normalized[i] = scale * entry
    }
    return normalized, nil
}
```

Normalization is the operation that takes an already scaled nonzero vector back to a **unit-length representative** of its ray:

\[
|\psi\rangle\longmapsto
\frac{|\psi\rangle}{\|\psi\|}.
\]

For a scaled vector \(|\chi\rangle=c|\psi\rangle\), with \(c\ne0\), normalization gives

\[
\frac{|\chi\rangle}{\|\chi\|}
=\frac{c}{|c|}\frac{|\psi\rangle}{\|\psi\|}.
\]

The factor \(c/|c|\) has magnitude one, so normalization removes the scale \(|c|\) but leaves a possible global phase. There is no unique normalized vector for a ray unless an additional phase convention is chosen.

## 3. Same-ray predicate and orthogonality predicate

The two vectors have zero overlap:

\[
\langle\phi|\psi\rangle
=(1-i)(1+i)- (1+i)(1-i)
=2-2=0.
\]

Thus \(|\phi\rangle\) and \(|\psi\rangle\) are orthogonal. Their normalized versions are orthogonal as well:

\[
\langle\widehat\phi|\widehat\psi\rangle=0.
\]

### Same-ray predicate

Two nonzero vectors lie on the same ray exactly when one is a nonzero scalar multiple of the other:

\[
|\chi\rangle\sim|\psi\rangle
\iff
\exists\,c\in\mathbb C\setminus\{0\}
\text{ such that }
|\chi\rangle=c|\psi\rangle.
\]

For nonzero vectors, an equivalent Hilbert-space test is that their normalized overlap has magnitude one:

\[
\frac{|\langle\chi|\psi\rangle|}{\|\chi\|\,\|\psi\|}=1.
\]

In floating-point code, test whether that quantity is sufficiently close to one. The zero vector has no ray, so it must be rejected.

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
```

This is a **same-ray test**, not an ordering. Rays do not have a natural physical or mathematical order, so there is no canonical comparator such as “ray A is less than ray B.” A program may impose an arbitrary order for sorting or storage, but that order has no ray-invariant meaning.

### Orthogonality predicate

For exact symbolic calculations, the predicate is

\[
\operatorname{orthogonal}(\phi,\psi)
\iff
\langle\phi|\psi\rangle=0.
\]

For floating-point calculations, use a tolerance \(\varepsilon>0\):

\[
\operatorname{orthogonal}_{\varepsilon}(\phi,\psi)
\iff
|\langle\phi|\psi\rangle|<\varepsilon.
\]

```go
func isOrthogonal(phi, psi []complex128, tolerance float64) bool {
    return cmplx.Abs(inner(phi, psi)) < tolerance
}
```

## 4. Rank-one projector

The rank-one projector onto the normalized \(|\widehat\psi\rangle\) direction is

\[
P_\psi=|\widehat\psi\rangle\langle\widehat\psi|.
\]

For this vector,

\[
P_\psi=
\begin{pmatrix}
\frac12&\frac{i}{2}\\
-\frac{i}{2}&\frac12
\end{pmatrix}.
\]

It is an orthogonal projector because

\[
P_\psi^2=P_\psi,
\qquad
P_\psi^\dagger=P_\psi.
\]

It keeps the component in the \(|\widehat\psi\rangle\) direction and removes the orthogonal component.

```go
type Matrix2 [2][2]complex128

func projector(ket []complex128) Matrix2 {
    psiHat := normalize(ket)
    return Matrix2{
        {psiHat[0] * cmplx.Conj(psiHat[0]), psiHat[0] * cmplx.Conj(psiHat[1])},
        {psiHat[1] * cmplx.Conj(psiHat[0]), psiHat[1] * cmplx.Conj(psiHat[1])},
    }
}
```

## 5. Born-rule probability

If the system is in \(|\widehat\psi\rangle\), a yes/no measurement represented by \(P_\psi\) returns yes with probability

\[
p(P_\psi)
=\langle\widehat\psi|P_\psi|\widehat\psi\rangle
=1.
\]

For the orthogonal state \(|\widehat\phi\rangle\), the same yes outcome has probability

\[
p(P_\psi)
=\langle\widehat\phi|P_\psi|\widehat\phi\rangle
=0.
\]

The projector distinguishes these two orthogonal directions perfectly in this idealized projective-measurement model.

## 6. Ray and global phase

A pure quantum state is represented by a **ray**, not by one uniquely chosen nonzero vector. For example,

\[
|\widehat\psi\rangle
\sim e^{i\theta}|\widehat\psi\rangle.
\]

The global phase changes the vector representative but not the ray. It also leaves the projector unchanged:

\[
|e^{i\theta}\widehat\psi\rangle
\langle e^{i\theta}\widehat\psi|
=|\widehat\psi\rangle\langle\widehat\psi|
=P_\psi.
\]

Multiplying by a nonzero scalar such as \(7e^{i\theta}\) also stays on the same ray, but the resulting vector is no longer normalized. Normalization selects a convenient unit-length representative of that ray.

## What this example does and does not show

This example connects the standard inner product, norm, normalization, orthogonality, a rank-one projector, and a Born-rule probability in \(\mathbb C^2\). It does not establish how a general measurement physically updates a state after an outcome.
