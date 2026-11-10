---
{
  "schema_version": "2.0",
  "id": "example-composite-bell-state-partial-trace",
  "type": "example",
  "title": "Composite System: Bell State, Partial Trace, and Product-State Contrast",
  "summary": "A self-contained two-qubit calculation of a Bell-state density operator and its maximally mixed reduced state, contrasted with a product state.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison"],
  "modality": ["text", "code"],
  "topics": ["composite-systems"],
  "teaches": ["declare an ordered product basis", "form a pure-state density operator", "take a partial trace", "distinguish a product state from an entangled state", "distinguish a reduced state from a conditional state"],
  "prerequisites": ["inner-product-spaces", "quantum-states-rays-and-normalization", "bases-and-coordinates", "dirac-notation", "composite-systems"],
  "action": "Use the stated C:S product-basis order to expand a Bell state, form its density operator, take the partial trace over C, and compare the result with a product state and with outcome-conditioned states.",
  "non_conclusion": "This finite two-qubit calculation does not characterize arbitrary mixed-state entanglement, provide a Bell-inequality test, imply signalling, or construct a physical clock or a gravitational subsystem split.",
  "relationships": [{"type": "illustrates", "target": "composite-systems"}],
  "sources": [{"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}]
}
---
# Composite System: Bell State, Partial Trace, and Product-State Contrast

## Prerequisites and local setup

Assume the finite-dimensional tensor-product model from [Composite Quantum Systems](../mathematics/composite-systems.md). Let \(C\) and \(S\) each be a copy of \(\mathbb C^2\), with orthonormal bases \((|0\rangle_C,|1\rangle_C)\) and \((|0\rangle_S,|1\rangle_S)\).

**Convention — product-basis order:** all four-component columns below use
\[
(|0\rangle_C|0\rangle_S,\ |0\rangle_C|1\rangle_S,\ |1\rangle_C|0\rangle_S,\ |1\rangle_C|1\rangle_S).
\]
The first label is always \(C\), the second always \(S\). In particular, \(|1\rangle_C|0\rangle_S=(0,0,1,0)^T\). This order is a representation choice, not a property of the abstract tensor product.

## 1. Bell state and density operator

Choose the normalized Bell state
\[
|\Phi^+\rangle=\frac{|0\rangle_C|0\rangle_S+|1\rangle_C|1\rangle_S}{\sqrt2}
=\frac1{\sqrt2}\begin{pmatrix}1\\0\\0\\1\end{pmatrix}.
\]
Its density operator is
\[
\rho_{CS}=|\Phi^+\rangle\langle\Phi^+|
=\frac12\left(
|00\rangle\langle00|+|00\rangle\langle11|
+|11\rangle\langle00|+|11\rangle\langle11|
\right),
\]
where \(|cs\rangle\) abbreviates \(|c\rangle_C|s\rangle_S\). As a matrix in the declared order,
\[
\rho_{CS}=\frac12\begin{pmatrix}
1&0&0&1\\
0&0&0&0\\
0&0&0&0\\
1&0&0&1
\end{pmatrix}.
\]

## 2. Partial trace over the clock factor

For the chosen clock basis, calculate the partial trace with
\[
\operatorname{Tr}_C(\rho_{CS})
=\sum_{c=0}^1({}_C\langle c|\otimes I_S)\rho_{CS}(|c\rangle_C\otimes I_S).
\]
Only the \(|00\rangle\langle00|\) term survives for \(c=0\), yielding \(\tfrac12|0\rangle_S\langle0|\); only \(|11\rangle\langle11|\) survives for \(c=1\), yielding \(\tfrac12|1\rangle_S\langle1|\). The cross terms vanish because \(\langle0|1\rangle_C=0\). Therefore
\[
\rho_S=\operatorname{Tr}_C(\rho_{CS})
=\frac12\bigl(|0\rangle\langle0|+|1\rangle\langle1|\bigr)
=\frac12 I_S.
\]
The joint state is pure, while this reduced state is mixed. This is compatible with a pure global state because the subsystem description ignores correlations with \(C\).

## 3. Product-state contrast

The state \(|0\rangle_C|0\rangle_S\) is product by construction, and
\[
\operatorname{Tr}_C\bigl(|00\rangle\langle00|\bigr)=|0\rangle_S\langle0|.
\]
The Bell state cannot be written as \(|c\rangle_C|s\rangle_S\). One quick check is its coefficient matrix in the declared local bases:
\[
A_{\Phi^+}=\frac1{\sqrt2}\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]
A pure two-factor state is product exactly when this coefficient matrix has rank one. Here its determinant is \(1/2\ne0\), so its rank is two and \(|\Phi^+\rangle\) is entangled. This rank criterion is only for this pure finite bipartite setting.

## 4. Reduced is not conditional

If an ideal clock-basis outcome \(0\) is selected, the unnormalized system operator is
\[
\widetilde\rho_{S|0}=\operatorname{Tr}_C[(|0\rangle\langle0|_C\otimes I_S)\rho_{CS}]
=\frac12|0\rangle\langle0|_S.
\]
Its trace, \(p(0)=1/2\), is the outcome probability. Dividing by this positive probability gives the conditional state \(|0\rangle\langle0|_S\). The reduced state \(I_S/2\) instead has no selected outcome and is the average
\[
\rho_S=\tfrac12|0\rangle\langle0|+\tfrac12|1\rangle\langle1|.
\]
This calculation uses effect conditioning; a statement about a post-measurement joint state additionally needs an instrument.

## 5. Pedagogical Go check

```go
package main

import "fmt"

// Given: rho[a][i][b][j] represents ⟨a,i|ρ_CS|b,j⟩ in the product-basis order
// (|0⟩_C|0⟩_S, |0⟩_C|1⟩_S, |1⟩_C|0⟩_S, |1⟩_C|1⟩_S).
// Model scope: both C and S are two-dimensional complex Hilbert spaces.
// Representation: rho is stored as tensor indices so partialTraceOverClock2D sums a=b.
type JointDensity2D [2][2][2][2]complex128

type SystemDensity2D [2][2]complex128

// Given: rho is a joint operator on C⊗S in the declared factor order.
// The partial trace over C is (Tr_C rho)[i][j] = Σ_c rho[c][i][c][j].
func partialTraceOverClock2D(rho JointDensity2D) SystemDensity2D {
    var reduced SystemDensity2D
    for c := 0; c < 2; c++ {
        for i := 0; i < 2; i++ {
            for j := 0; j < 2; j++ {
                reduced[i][j] += rho[c][i][c][j]
            }
        }
    }
    return reduced
}

func main() {
    var bellDensity JointDensity2D
    bellDensity[0][0][0][0] = 0.5 // |00⟩⟨00|
    bellDensity[0][0][1][1] = 0.5 // |00⟩⟨11|
    bellDensity[1][1][0][0] = 0.5 // |11⟩⟨00|
    bellDensity[1][1][1][1] = 0.5 // |11⟩⟨11|

    fmt.Println(partialTraceOverClock2D(bellDensity))
    // [[(0.5+0i) (0+0i)] [(0+0i) (0.5+0i)]]
}
```

## What this example does and does not show

This example shows that a finite pure entangled state can have a mixed reduced state and that tracing out a factor differs from selecting an outcome with positive probability. It does not establish that every mixed state is entangled or separable, a Bell experiment, faster-than-light signalling, a physical measurement implementation, or a preferred clock--system split in quantum gravity.
