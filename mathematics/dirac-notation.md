---
{
  "schema_version": "2.0",
  "id": "dirac-notation",
  "type": "concept",
  "title": "Dirac Notation",
  "summary": "A compact notation for vectors, dual vectors, inner products, and operators in Hilbert space.",
  "review_status": "ai_reviewed",
  "parents": [
    "bases-and-coordinates"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "born-rule-and-quantum-probability"
    },
    {
      "type": "prerequisite-for",
      "target": "spectral-notation"
    },
    {
      "type": "prerequisite-for",
      "target": "composite-systems"
    },
    {
      "type": "related-to",
      "target": "def-ket"
    },
    {
      "type": "related-to",
      "target": "def-bra"
    },
    {
      "type": "related-to",
      "target": "def-dual-vector"
    },
    {
      "type": "related-to",
      "target": "def-overlap"
    },
    {
      "type": "related-to",
      "target": "def-orthonormal-basis"
    },
    {
      "type": "related-to",
      "target": "def-discrete-basis"
    },
    {
      "type": "related-to",
      "target": "def-kronecker-delta"
    },
    {
      "type": "related-to",
      "target": "def-identity-operator"
    },
    {
      "type": "related-to",
      "target": "def-resolution-of-identity"
    },
    {
      "type": "related-to",
      "target": "def-basis-expansion"
    },
    {
      "type": "illustrates",
      "target": "example-dirac-notation-basis-and-adjoint"
    }
  ],
  "sources": [
    {
      "title": "P. A. M. Dirac, The Principles of Quantum Mechanics",
      "url": "https://global.oup.com/academic/product/the-principles-of-quantum-mechanics-9780198520115",
      "persistent_id": "ISBN:9780198520115"
    },
    {
      "title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information",
      "url": "https://doi.org/10.1017/CBO9780511976667",
      "persistent_id": "doi:10.1017/CBO9780511976667"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "ket",
      "term": "ket",
      "occurrence": "first"
    },
    {
      "definition_id": "bra",
      "term": "bra",
      "occurrence": "first"
    },
    {
      "definition_id": "dual-vector",
      "term": "dual vector",
      "occurrence": "first"
    },
    {
      "definition_id": "overlap",
      "term": "overlap",
      "occurrence": "first"
    },
    {
      "definition_id": "norm",
      "term": "norm",
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
      "definition_id": "kronecker-delta",
      "term": "Kronecker delta",
      "occurrence": "first"
    },
    {
      "definition_id": "identity-operator",
      "term": "identity operator",
      "occurrence": "first"
    },
    {
      "definition_id": "resolution-of-identity",
      "term": "resolution of the identity",
      "occurrence": "first"
    },
    {
      "definition_id": "basis-expansion",
      "term": "basis expansion",
      "occurrence": "first"
    }
  ]
}
---
# Dirac Notation

A [ket](../definitions/def-ket.md) \(|\psi\rangle\) denotes a vector in a Hilbert space \(\mathcal H\). Its [bra](../definitions/def-bra.md) \(\langle\psi|\) is the [dual vector](../definitions/def-dual-vector.md) induced by the inner product: under this wiki's convention, it is a continuous linear functional of the vector placed to its right. The [overlap](../definitions/def-overlap.md) \(\langle\phi|\psi\rangle\) is a complex number, and \(\langle\psi|\psi\rangle\) is the squared [norm](../definitions/def-norm.md).

For a [discrete basis](../definitions/def-discrete-basis.md) \(\{|n\rangle\}\) that is [orthonormal](../definitions/def-orthonormal-basis.md), \(\langle n|m\rangle=\delta_{nm}\), where \(\delta_{nm}\) is the [Kronecker delta](../definitions/def-kronecker-delta.md). Its [resolution of the identity](../definitions/def-resolution-of-identity.md) is \(\sum_n|n\rangle\langle n|=I\), where \(I\) is the [identity operator](../definitions/def-identity-operator.md), with appropriate convergence. Applying that identity gives the [basis expansion](../definitions/def-basis-expansion.md) \(|\psi\rangle=\sum_n|n\rangle\langle n|\psi\rangle\). These identities must not be transferred without qualification to continuous labels; see [Spectra and Generalized Bases](spectral-notation.md).
