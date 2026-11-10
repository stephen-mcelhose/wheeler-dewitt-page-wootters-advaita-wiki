---
{
  "schema_version": "2.0",
  "id": "example-operators-domains-self-adjointness",
  "type": "example",
  "title": "Finite C² Witnesses, ℓ² Truncations, and a Restricted-Domain Contrast",
  "summary": "Scoped finite C² checks, analytic ℓ² arguments illustrated by truncations, and a non-computational symmetric-versus-self-adjoint contrast.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "contrast"],
  "modality": ["text", "code"],
  "topics": ["operators-and-domains", "dirac-notation", "hilbert-spaces"],
  "teaches": ["separate finite checks from universal claims", "prove an ℓ² multiplier unbounded analytically", "use finite-support truncations to explain density", "distinguish finite Hermitian self-adjointness from restricted-domain symmetry"],
  "prerequisites": ["inner-product-spaces", "hilbert-spaces", "bases-and-coordinates", "dirac-notation"],
  "action": "Run explicitly scoped finite helpers, then read the analytic arguments that finite samples illustrate but cannot establish.",
  "non_conclusion": "No finite output proves ℓ² unboundedness or density, and no finite Hermitian predicate settles self-adjointness for an unbounded differential operator.",
  "relationships": [{"type": "illustrates", "target": "operators-and-domains"}],
  "sources": [{"title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis", "url": "https://doi.org/10.1016/C2013-0-10329-X", "persistent_id": "doi:10.1016/C2013-0-10329-X"}]
}
---
# Finite C² Witnesses, \(\ell^2\) Truncations, and a Restricted-Domain Contrast

We use the physics inner product \(\langle\phi|\psi\rangle=\phi^\dagger\psi\), conjugate-linear in the first argument. The four parts below intentionally distinguish executable facts about declared finite data from mathematical claims quantified over infinite spaces.

## 1. Finite \(\mathbb C^2\) linearity witness

Let \(A:\mathbb C^2\to\mathbb C^2\) be the matrix map for
\[
A=\begin{pmatrix}2&1-i\\1+i&3\end{pmatrix}.
\]
Matrix multiplication analytically proves that this map is linear for all vectors and scalars in \(\mathbb C^2\). The code predicate below is more limited: it checks the linearity equation for **one declared finite witness** \((\alpha,\beta,x,y)\). Its `true` result is useful as a regression check, not as a universal proof.

## 2. Bounded finite diagonal matrix

On \(\mathbb C^2\), let \(D=\operatorname{diag}(2,-3i)\). For \(x=(x_1,x_2)\),
\[
\|Dx\|^2=4|x_1|^2+9|x_2|^2\le9\|x\|^2,
\]
so \(\|D\|\le3\) (indeed equality holds at \((0,1)\)). This analytic inequality proves a bound for every \(x\in\mathbb C^2\). `boundedDiagonalSampleRatio2D` merely returns \(\|Dx\|/\|x\|\) for one nonzero supplied vector and must not be confused with an operator-norm algorithm.

## 3. The \(\ell^2\) index multiplier: proof first, truncation second

Let \(\ell^2=\{x=(x_n)_{n\ge1}:\sum_{n\ge1}|x_n|^2<\infty\}\) and give the multiplier its natural domain
\[
D(T)=\{x\in\ell^2:(n x_n)_{n\ge1}\in\ell^2\},\qquad (Tx)_n=n x_n.
\]
For the standard unit vector \(e_k\), we have \(e_k\in D(T)\), \(\|e_k\|=1\), and \(\|Te_k\|=k\). If a finite uniform bound \(C\) existed, then \(k\le C\) for every positive integer \(k\), which is impossible. This is the analytic proof that \(T\) is unbounded.

A slice can model only the first \(N\) coordinates. Its multiplier has the finite bound \(N\), and a unit-coordinate sample reports its index ratio. The helper is deliberately named `finiteMultiplierTruncationRatio`, not `isUnbounded`: no fixed finite computation can evaluate the infinite quantifier in unboundedness.

## 4. Finite support and density: proof first, tail code second

Let \(c_{00}\) be the finite-support sequences. For every \(x\in\ell^2\), define \(x^{(N)}=(x_1,\ldots,x_N,0,0,\ldots)\in c_{00}\). Then
\[
\|x-x^{(N)}\|^2=\sum_{n>N}|x_n|^2\longrightarrow0.
\]
Thus \(c_{00}\) is dense in \(\ell^2\). The code calculates a tail norm for a supplied finite prefix or a finite array standing in for supplied data. It cannot inspect an infinite tail, prove convergence for every \(x\in\ell^2\), or decide density. Accordingly, there is intentionally no predicate named `isDense`.

## Scoped Go helpers

```go
package main

import (
    "fmt"
    "math"
    "math/cmplx"
)

type Matrix2 [2][2]complex128
type Ket2 [2]complex128

// Model scope: coordinates are in one declared orthonormal C² basis.
func applyMatrix2(A Matrix2, x Ket2) Ket2 {
    return Ket2{
        A[0][0]*x[0] + A[0][1]*x[1],
        A[1][0]*x[0] + A[1][1]*x[1],
    }
}

func norm2(x Ket2) float64 {
    return math.Sqrt(cmplx.Abs(x[0])*cmplx.Abs(x[0]) + cmplx.Abs(x[1])*cmplx.Abs(x[1]))
}

func closeKet2(left, right Ket2, tolerance float64) bool {
    return cmplx.Abs(left[0]-right[0]) <= tolerance && cmplx.Abs(left[1]-right[1]) <= tolerance
}

// Sample/fixed-data check only: checks A(αx+βy)=αAx+βAy for this supplied witness.
// It does not prove linearity for all C² vectors and scalars; matrix multiplication does.
func isLinearWitnessMatrix2D(A Matrix2, alpha, beta complex128, x, y Ket2, tolerance float64) bool {
    combined := Ket2{alpha*x[0] + beta*y[0], alpha*x[1] + beta*y[1]}
    ax, ay := applyMatrix2(A, x), applyMatrix2(A, y)
    expected := Ket2{alpha*ax[0] + beta*ay[0], alpha*ax[1] + beta*ay[1]}
    return closeKet2(applyMatrix2(A, combined), expected, tolerance)
}

// General finite-model statement: for D=diag(d0,d1), ||Dx|| ≤ max(|d0|,|d1|)||x|| for every C² x.
// This returns that analytic finite-model bound; it is not evidence about an infinite-dimensional operator.
func boundedDiagonalAnalyticBound2D(d0, d1 complex128) float64 {
    return math.Max(cmplx.Abs(d0), cmplx.Abs(d1))
}

// Sample/fixed-data check only: returns ||Dx||/||x|| for one nonzero C² vector.
// The bool is false for x=0 because the ratio is undefined.
func boundedDiagonalSampleRatio2D(d0, d1 complex128, x Ket2) (ratio float64, defined bool) {
    denominator := norm2(x)
    if denominator == 0 { return 0, false }
    return norm2(Ket2{d0 * x[0], d1 * x[1]}) / denominator, true
}

func conjugateTranspose2(A Matrix2) Matrix2 {
    return Matrix2{{cmplx.Conj(A[0][0]), cmplx.Conj(A[1][0])}, {cmplx.Conj(A[0][1]), cmplx.Conj(A[1][1])}}
}

func subtractMatrix2(A, B Matrix2) Matrix2 {
    var difference Matrix2
    for row := range A {
        for column := range A {
            difference[row][column] = A[row][column] - B[row][column]
        }
    }
    return difference
}

// Given: A and B are finite 2×2 operators in the same declared C² basis.
// The commutator is [A,B] = AB - BA. Both products are defined in this finite model.
func commutatorMatrix2D(A, B Matrix2) Matrix2 {
    return subtractMatrix2(multiplyMatrix2(A, B), multiplyMatrix2(B, A))
}

// Given: A and B are finite 2×2 operators in the same declared C² basis.
// Model scope: this checks whether the finite commutator [A,B] is zero within tolerance.
// For unbounded operators, [A,B] additionally requires a compatible common domain.
func commutesMatrix2D(A, B Matrix2, tolerance float64) bool {
    return matricesClose2(commutatorMatrix2D(A, B), Matrix2{}, tolerance)
}

// General finite-model check: tests A=Aᵀ for this explicit 2×2 coordinate matrix.
// This is complex transpose symmetry, not the Hilbert-space symmetric-operator
// condition for complex matrices.
func hasTransposeSymmetryMatrix2D(A Matrix2, tolerance float64) bool {
    return cmplx.Abs(A[0][1]-A[1][0]) <= tolerance
}

// General finite-model check: tests A=A† in the declared orthonormal C² basis.
// Since the domain is all C², true means this finite matrix operator is self-adjoint.
// It MUST NOT be used to decide self-adjointness of an unbounded or restricted-domain operator.
func isSelfAdjointFiniteMatrix2D(A Matrix2, tolerance float64) bool {
    return cmplx.Abs(A[0][0]-cmplx.Conj(A[0][0])) <= tolerance &&
        cmplx.Abs(A[1][1]-cmplx.Conj(A[1][1])) <= tolerance &&
        cmplx.Abs(A[0][1]-cmplx.Conj(A[1][0])) <= tolerance
}

// Finite truncation only: x[j] represents coordinate n=j+1 of an ℓ² prefix.
// Every fixed slice defines a bounded finite-dimensional multiplier. This is not isUnbounded.
func finiteMultiplierTruncationRatio(x []complex128) (ratio float64, defined bool) {
    var inputSquared, outputSquared float64
    for j, value := range x {
        inputSquared += cmplx.Abs(value) * cmplx.Abs(value)
        scaled := complex(float64(j+1), 0) * value
        outputSquared += cmplx.Abs(scaled) * cmplx.Abs(scaled)
    }
    if inputSquared == 0 { return 0, false }
    return math.Sqrt(outputSquared / inputSquared), true
}

// Finite supplied-data helper: squared norm of entries after the first keep entries.
// It cannot see the infinite tail of an ℓ² sequence and is not isDense.
func finiteTailNormAfter(x []complex128, keep int) float64 {
    if keep < 0 { keep = 0 }
    if keep > len(x) { keep = len(x) }
    var squared float64
    for _, value := range x[keep:] { squared += cmplx.Abs(value) * cmplx.Abs(value) }
    return math.Sqrt(squared)
}

func main() {
    A := Matrix2{{2, 1 - 1i}, {1 + 1i, 3}}
    x, y := Ket2{1, 1i}, Ket2{2 - 1i, -1}
    fmt.Println(isLinearWitnessMatrix2D(A, 2-1i, -1i, x, y, 1e-12)) // true

    fmt.Println(boundedDiagonalAnalyticBound2D(2, -3i)) // 3
    ratio, ok := boundedDiagonalSampleRatio2D(2, -3i, Ket2{1, 1})
    fmt.Println(ratio, ok) // about 2.5495, true

    S := Matrix2{{2, 1 + 1i}, {1 + 1i, 3}}
    fmt.Println(hasTransposeSymmetryMatrix2D(S, 1e-12)) // true
    fmt.Println(isSelfAdjointFiniteMatrix2D(A, 1e-12))  // true

    diagonal := Matrix2{{1, 0}, {0, -1}}
    swap := Matrix2{{0, 1}, {1, 0}}
    fmt.Println(commutatorMatrix2D(diagonal, swap))    // [[(0+0i) (2+0i)] [(-2+0i) (0+0i)]]
    fmt.Println(commutesMatrix2D(diagonal, swap, 1e-12)) // false

    ratio, ok = finiteMultiplierTruncationRatio([]complex128{0, 0, 0, 1})
    fmt.Println(ratio, ok) // 4, true: the e₄ witness in this finite prefix
    fmt.Println(finiteTailNormAfter([]complex128{1, 2, 3, 4}, 2)) // 5
}
```

## 5. Finite commutator example

For finite matrices \(A\) and \(B\), the commutator is

\[
[A,B]=AB-BA.
\]

Take

\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
B=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Then

\[
AB=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
BA=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]

so

\[
[A,B]=\begin{pmatrix}0&2\\-2&0\end{pmatrix}\ne0.
\]

Thus \(A\) and \(B\) do not commute: applying them in different orders gives different results. In this finite matrix model, both products are defined for every input. For unbounded operators, the commutator is meaningful only on vectors for which both \(AB\) and \(BA\) are defined.

## 6. Finite self-adjointness and restricted derivative contrast

The matrix \(A\) above obeys \(A=A^\dagger\). As its domain is all of \(\mathbb C^2\), its adjoint has the same full finite-dimensional domain, so it is self-adjoint **in this finite model**.

Now change spaces: on \(L^2([0,1])\), define
\[
(P_0f)(x)=-if'(x),\qquad D(P_0)=C_c^\infty(0,1).
\]
For \(f,g\in D(P_0)\), integration by parts has no boundary term and gives \(\langle f|P_0g\rangle=\langle P_0f|g\rangle\). Thus \(P_0\) is symmetric on this stated domain. This is deliberately non-computational: it does not calculate \(D(P_0^*)\), establish self-adjointness, classify extensions, or choose boundary conditions.

## Limits and source-review boundary

The executable routines validate only the scopes stated in their comments. They provide no numerical decision procedure for infinite-dimensional unboundedness, density, adjoint domains, or self-adjoint extensions.
