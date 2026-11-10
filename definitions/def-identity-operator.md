---
{
  "schema_version": "2.0",
  "id": "def-identity-operator",
  "type": "definition",
  "title": "Identity operator",
  "summary": "The operator that returns every vector unchanged; in finite coordinates, it is the matrix with ones on the diagonal and zeros elsewhere.",
  "review_status": "ai_reviewed",
  "parents": [],
  "relationships": [
    {
      "type": "related-to",
      "target": "dirac-notation"
    },
    {
      "type": "related-to",
      "target": "projection-operators"
    },
    {
      "type": "related-to",
      "target": "spectral-notation"
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
# Identity operator

The identity operator on a vector space \(V\), written \(I_V\) or simply \(I\) when the space is clear, is the operator that returns every vector unchanged:

\[
I_V|\psi\rangle=|\psi\rangle
\qquad\text{for every }|\psi\rangle\in V.
\]

A programmer-friendly name is `identity`, `identityOperator`, or `identityMatrix` when a particular finite coordinate representation is intended.

For the declared standard basis of \(\mathbb C^2\), its matrix is

\[
I_2=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

It returns

\[
I_2\begin{pmatrix}a\\b\end{pmatrix}
=
\begin{pmatrix}a\\b\end{pmatrix}.
\]

More generally, in a declared \(d\)-dimensional coordinate basis, \(I_d\) has ones on the diagonal and zeros elsewhere. The identity operator does not depend on the basis; only its matrix representation does.

Learn more: [Dirac Notation](../mathematics/dirac-notation.md).
