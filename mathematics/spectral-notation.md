---
{
  "schema_version": "2.0",
  "id": "spectral-notation",
  "type": "concept",
  "title": "Spectra and Generalized Bases",
  "summary": "The distinction between discrete bases in a Hilbert space and generalized continuous-spectrum notation.",
  "review_status": "ai_reviewed",
  "parents": [
    "dirac-notation"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "clock-states"
    },
    {
      "type": "related-to",
      "target": "def-eigenvalue"
    },
    {
      "type": "related-to",
      "target": "def-eigenvector"
    },
    {
      "type": "related-to",
      "target": "def-generalized-eigenvector"
    },
    {
      "type": "related-to",
      "target": "def-orthonormal-basis"
    },
    {
      "type": "related-to",
      "target": "def-rigged-hilbert-space"
    }
  ],
  "sources": [
    {
      "title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis",
      "url": "https://doi.org/10.1016/C2013-0-10329-X",
      "persistent_id": "doi:10.1016/C2013-0-10329-X"
    },
    {
      "title": "P. A. M. Dirac, The Principles of Quantum Mechanics",
      "url": "https://global.oup.com/academic/product/the-principles-of-quantum-mechanics-9780198520115",
      "persistent_id": "ISBN:9780198520115"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "eigenvalue",
      "term": "eigenvalue",
      "occurrence": "first"
    },
    {
      "definition_id": "eigenvector",
      "term": "eigenvector",
      "occurrence": "first"
    },
    {
      "definition_id": "generalized-eigenvector",
      "term": "generalized eigenvector",
      "occurrence": "first"
    },
    {
      "definition_id": "rigged-hilbert-space",
      "term": "rigged Hilbert space",
      "occurrence": "first"
    },
    {
      "definition_id": "discrete-basis",
      "term": "discrete basis",
      "occurrence": "first"
    },
    {
      "definition_id": "orthonormal-basis",
      "term": "orthonormal",
      "occurrence": "first"
    },
    {
      "definition_id": "povm",
      "term": "POVM",
      "occurrence": "first"
    }
  ]
}
---
# Spectra and Generalized Bases

For an operator \(\hat A\), an [eigenvector](../definitions/def-eigenvector.md) \(|a\rangle\) and its [eigenvalue](../definitions/def-eigenvalue.md) \(a\) satisfy

\[
\hat A|a\rangle=a|a\rangle.
\]

In a finite-dimensional model, ordinary eigenvectors can be normalized and used in a [discrete basis](../definitions/def-discrete-basis.md). If that basis is [orthonormal](../definitions/def-orthonormal-basis.md), then \(\langle n|m\rangle=\delta_{nm}\).

For continuous spectra, formal expressions such as \(\langle x|x'\rangle=\delta(x-x')\) and \(\int dx\,|x\rangle\langle x|=I\) are generalized spectral notation. A [generalized eigenvector](../definitions/def-generalized-eigenvector.md) is a distributional object used in such a formal eigenvalue equation, not an ordinary Hilbert-space vector. Position-like vectors \(|x\rangle\) are not ordinary normalized Hilbert-space vectors.

A useful formal setting is a [rigged Hilbert space](../definitions/def-rigged-hilbert-space.md) \(\Phi\subset\mathcal H\subset\Phi'\), where generalized eigenvectors can be handled as distributions. Ideal clock kets \(|t\rangle\) used later in Page–Wootters derivations have this idealized status unless a concrete clock [POVM](../definitions/def-povm.md) construction is specified.
