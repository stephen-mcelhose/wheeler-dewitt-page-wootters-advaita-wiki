---
{
  "schema_version": "2.0",
  "id": "bases-and-coordinates",
  "type": "concept",
  "title": "Bases and Coordinates",
  "summary": "How a chosen independent spanning set gives unique coordinates to vectors in a finite-dimensional space.",
  "review_status": "ai_reviewed",
  "parents": [
    "quantum-states-rays-and-normalization"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "dirac-notation"
    },
    {
      "type": "related-to",
      "target": "def-span"
    },
    {
      "type": "related-to",
      "target": "def-linear-independence"
    },
    {
      "type": "related-to",
      "target": "def-basis"
    },
    {
      "type": "related-to",
      "target": "def-coordinates"
    },
    {
      "type": "related-to",
      "target": "def-orthonormal-basis"
    },
    {
      "type": "illustrates",
      "target": "example-bases-coordinates-and-orthonormality"
    }
  ],
  "sources": [
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "span",
      "term": "span",
      "occurrence": "first"
    },
    {
      "definition_id": "linear-independence",
      "term": "linearly independent",
      "occurrence": "first"
    },
    {
      "definition_id": "basis",
      "term": "basis",
      "occurrence": "first"
    },
    {
      "definition_id": "coordinates",
      "term": "coordinates",
      "occurrence": "first"
    },
    {
      "definition_id": "orthonormal-basis",
      "term": "orthonormal basis",
      "occurrence": "first"
    }
  ]
}
---

# Bases and Coordinates

A chosen collection of vectors can provide a coordinate system for a vector space. The collection's [span](../definitions/def-span.md) is every vector that can be built from its linear combinations:

\[
\operatorname{span}\{v_1,\ldots,v_k\}
=\left\{\sum_{j=1}^{k}c_jv_j:c_j\in\mathbb C\right\}.
\]

The collection is [linearly independent](../definitions/def-linear-independence.md) when the equation

\[
\sum_{j=1}^{k}c_jv_j=0
\]

forces every coefficient \(c_j\) to be zero. Intuitively, no vector in the collection is redundant.

A [basis](../definitions/def-basis.md) for a target vector space is a collection that is both spanning and linearly independent. Every vector in the target space then has one unique expansion in that basis.

## Ordered basis and coordinates

A coordinate system for a vector space has three linked parts:

1. a target vector space \(V\);
2. an ordered basis \(B=(b_0,\ldots,b_{d-1})\) of that space;
3. a coordinate map that sends each vector \(v\in V\) to its coefficient column relative to \(B\).

If

\[
v=\sum_{j=0}^{d-1}c_jb_j,
\]

then the [coordinates](../definitions/def-coordinates.md) of \(v\) relative to \(B\) are

\[
[v]_B=\begin{pmatrix}c_0\\\vdots\\c_{d-1}\end{pmatrix}.
\]

The coordinate column is not the abstract vector by itself. It represents the vector only after the ordered basis is specified. Reordering the same basis vectors generally changes the coordinate column of the same abstract vector. Basis labels such as \(0\), \(1\), or \(n\) are assigned when the ordered basis is chosen; they are not extracted from vector entries.

## Example: the standard basis of \(\mathbb C^2\)

The space \(\mathbb C^2\) has dimension two. Define the ordered standard basis contract

\[
B_{\mathrm{std}}=(e_0,e_1),
\qquad
e_0=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
e_1=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Within this declared contract, label \(0\) identifies \(e_0\) and label \(1\) identifies \(e_1\). The labels are stable only while the target space, basis vectors, and their order remain this specified \(B_{\mathrm{std}}\). Every vector

\[
v=\begin{pmatrix}a\\b\end{pmatrix}
\]

has the unique expansion

\[
v=ae_0+be_1.
\]

Thus \((e_0,e_1)\) spans \(\mathbb C^2\). It is also linearly independent, so it is a basis.

For two vectors \(u=(u_0,u_1)^T\) and \(v=(v_0,v_1)^T\) in \(\mathbb C^2\), make the coordinate matrix

\[
A=\begin{pmatrix}u_0&v_0\\u_1&v_1\end{pmatrix}.
\]

Then

\[
\det A=u_0v_1-u_1v_0.
\]

For a pair of vectors in \(\mathbb C^2\), \(\det A\ne0\) means the pair is linearly independent; because there are two independent vectors in a two-dimensional target space, the pair also spans \(\mathbb C^2\) and is a basis. This equivalence is specific to this finite two-dimensional case.

## Orthonormal basis

An orthonormal set has unit-norm vectors and zero overlap between distinct vectors. It is an [orthonormal basis](../definitions/def-orthonormal-basis.md) only when it also spans the target space.

\[
\langle b_i|b_j\rangle=\delta_{ij}
\]

expresses orthonormality. It does not alone prove spanning in an arbitrary target space. In \(\mathbb C^2\), however, two orthonormal vectors form an orthonormal basis because they are independent and there are already two of them.

Later, Dirac notation writes the standard basis vectors as \(|0\rangle\) and \(|1\rangle\). The labels are basis identifiers; they are not norms, vector components, or numbers extracted from the kets.

This page treats finite-dimensional bases first. Infinite-dimensional Hilbert-space bases require norm convergence, and continuous labels require further qualification in Spectra and Generalized Bases.
