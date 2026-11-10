---
{
  "schema_version": "2.0",
  "id": "hilbert-spaces",
  "type": "concept",
  "title": "Hilbert Spaces",
  "summary": "Complete inner-product spaces: the mathematical setting for quantum state vectors.",
  "review_status": "ai_reviewed",
  "parents": [
    "inner-product-spaces",
    "norms-distance-and-convergence"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "quantum-states-rays-and-normalization"
    },
    {
      "type": "related-to",
      "target": "def-inner-product"
    },
    {
      "type": "related-to",
      "target": "def-cauchy-sequence"
    },
    {
      "type": "related-to",
      "target": "def-completeness"
    },
    {
      "type": "related-to",
      "target": "def-ray"
    },
    {
      "type": "related-to",
      "target": "def-normalization"
    },
    {
      "type": "related-to",
      "target": "def-orthogonality"
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
      "definition_id": "completeness",
      "term": "Completeness",
      "occurrence": "first"
    },
    {
      "definition_id": "norm",
      "term": "norm",
      "occurrence": "first"
    },
    {
      "definition_id": "cauchy-sequence",
      "term": "Cauchy sequence",
      "occurrence": "first"
    },
    {
      "definition_id": "ray",
      "term": "ray",
      "occurrence": "first"
    },
    {
      "definition_id": "normalization",
      "term": "normalized",
      "occurrence": "first"
    },
    {
      "definition_id": "orthogonality",
      "term": "orthogonality",
      "occurrence": "first"
    },
    {
      "definition_id": "born-rule",
      "term": "Born rule",
      "occurrence": "first"
    }
  ]
}
---
# Hilbert Spaces

A **complex Hilbert space** is a complex [inner-product space](../definitions/def-inner-product.md) that is complete with respect to the norm-induced metric \(d(\phi,\psi)=\|\phi-\psi\|\). The inner product \(\langle\phi|\psi\rangle\) defines the [norm](../definitions/def-norm.md)

\[
\|\psi\|=\sqrt{\langle\psi|\psi\rangle},
\]

and therefore the distance above. [Completeness](../definitions/def-completeness.md) means that every [Cauchy sequence](../definitions/def-cauchy-sequence.md)—an approximation sequence whose later members become arbitrarily close to one another—converges to a vector still in the same space.

In quantum mechanics, vectors in a Hilbert space are used as **state vectors**. A pure physical state is more precisely a [ray](../definitions/def-ray.md): nonzero vectors that differ only by an overall nonzero complex factor represent the same ray. We usually choose a [normalized](../definitions/def-normalization.md) representative,

\[
\langle\psi|\psi\rangle=1.
\]

Multiplying a normalized representative by an overall phase, \(|\psi\rangle\mapsto e^{i\theta}|\psi\rangle\), does not change the pure state. The inner product defines [orthogonality](../definitions/def-orthogonality.md): \(|\phi\rangle\) and \(|\psi\rangle\) are orthogonal when \(\langle\phi|\psi\rangle=0\).

Probabilities enter only once a measurement rule, such as the [Born rule](../definitions/def-born-rule.md), is specified. This page adopts the physics convention that the inner product is conjugate-linear in its first argument and linear in its second.

> **Why completeness matters**
> Quantum models often use limits of approximation sequences, for example when expanding states in bases or taking idealized limits. Completeness ensures that a norm-convergent approximation still represents an allowed state vector rather than an object outside the state space.
