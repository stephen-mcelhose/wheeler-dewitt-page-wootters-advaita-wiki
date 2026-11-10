---
{
  "schema_version": "2.0",
  "id": "inner-product-spaces",
  "type": "concept",
  "title": "Inner-Product Spaces",
  "summary": "Vector spaces with a complex-valued comparison rule that defines length and orthogonality.",
  "review_status": "ai_reviewed",
  "parents": [],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "norms-distance-and-convergence"
    },
    {
      "type": "prerequisite-for",
      "target": "hilbert-spaces"
    },
    {
      "type": "related-to",
      "target": "def-orthogonality"
    },
    {
      "type": "related-to",
      "target": "def-vector-space"
    },
    {
      "type": "illustrates",
      "target": "example-inner-product-conjugate-linearity-and-orthogonality"
    }
  ],
  "sources": [
    {
      "title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis",
      "url": "https://doi.org/10.1016/C2013-0-10329-X",
      "persistent_id": "doi:10.1016/C2013-0-10329-X"
    },
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "vector-space",
      "term": "vector space",
      "occurrence": "first"
    },
    {
      "definition_id": "orthogonality",
      "term": "orthogonality",
      "occurrence": "first"
    }
  ]
}
---

# Inner-Product Spaces

An inner-product space is a [vector space](../definitions/def-vector-space.md) equipped with a rule \(\langle\phi|\psi\rangle\) that compares two vectors and returns a complex number. In the physics convention used here, the inner product is conjugate-linear in the first argument and linear in the second.

For vectors \(|\phi\rangle,|\chi\rangle,|\psi\rangle\) and complex scalars \(a,b\), the rule has four linked properties:

\[
\langle\phi|\psi\rangle=\langle\psi|\phi\rangle^*,
\]

\[
\langle a\phi+b\chi|\psi\rangle
=a^*\langle\phi|\psi\rangle+b^*\langle\chi|\psi\rangle,
\]

\[
\langle\phi|a\psi+b\chi\rangle
=a\langle\phi|\psi\rangle+b\langle\phi|\chi\rangle,
\]

and

\[
\langle\psi|\psi\rangle\ge0,
\qquad
\langle\psi|\psi\rangle=0\ \text{only when}\ |\psi\rangle=0.
\]

The first property is **conjugate symmetry**. The next two show the selected physics convention: scalars leave the second argument unchanged but are complex-conjugated when they leave the first argument. The last property is **positive definiteness**; it lets the inner product define a genuine norm. It also defines [orthogonality](../definitions/def-orthogonality.md): two vectors are orthogonal when \(\langle\phi|\psi\rangle=0\). This page supplies the local vocabulary needed before Hilbert spaces and Dirac notation.
