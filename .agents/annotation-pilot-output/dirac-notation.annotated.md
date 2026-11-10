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

A {{def:ket|ket}} \(|\psi\rangle\) denotes a vector in a Hilbert space \(\mathcal H\). Its {{def:bra|bra}} \(\langle\psi|\) is the {{def:dual-vector|dual vector}} induced by the inner product: under this wiki's convention, it is a continuous linear functional of the vector placed to its right. The {{def:overlap|overlap}} \(\langle\phi|\psi\rangle\) is a complex number, and \(\langle\psi|\psi\rangle\) is the squared {{def:norm|norm}}.

For a {{def:discrete-basis|discrete basis}} \(\{|n\rangle\}\) that is {{def:orthonormal-basis|orthonormal}}, \(\langle n|m\rangle=\delta_{nm}\), where \(\delta_{nm}\) is the {{def:kronecker-delta|Kronecker delta}}. Its {{def:resolution-of-identity|resolution of the identity}} is \(\sum_n|n\rangle\langle n|=I\), where \(I\) is the [identity operator](../definitions/def-identity-operator.md), with appropriate convergence. Applying that identity gives the {{def:basis-expansion|basis expansion}} \(|\psi\rangle=\sum_n|n\rangle\langle n|\psi\rangle\). These identities must not be transferred without qualification to continuous labels; see [Spectra and Generalized Bases](spectral-notation.md).
