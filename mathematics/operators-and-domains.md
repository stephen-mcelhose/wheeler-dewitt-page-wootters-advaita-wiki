---
{
  "schema_version": "2.0",
  "id": "operators-and-domains",
  "type": "concept",
  "title": "Operators, Domains, and Self-Adjointness",
  "summary": "Operator/domain pairs, finite C² checks, and the limits of finite evidence for unboundedness, density, and self-adjointness.",
  "review_status": "ai_reviewed",
  "parents": [
    "hilbert-spaces",
    "dirac-notation"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "composite-systems"
    },
    {
      "type": "prerequisite-for",
      "target": "dirac-quantization"
    },
    {
      "type": "prerequisite-for",
      "target": "page-wootters-mechanism"
    },
    {
      "type": "related-to",
      "target": "def-linear-operator"
    },
    {
      "type": "related-to",
      "target": "def-bounded-operator"
    },
    {
      "type": "related-to",
      "target": "def-unbounded-operator"
    },
    {
      "type": "related-to",
      "target": "def-operator-domain"
    },
    {
      "type": "related-to",
      "target": "def-dense-domain"
    },
    {
      "type": "related-to",
      "target": "def-adjoint"
    },
    {
      "type": "related-to",
      "target": "def-symmetric-operator"
    },
    {
      "type": "related-to",
      "target": "def-self-adjoint-operator"
    },
    {
      "type": "related-to",
      "target": "def-commutator"
    },
    {
      "type": "illustrates",
      "target": "example-operators-domains-self-adjointness"
    }
  ],
  "sources": [
    {
      "title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis",
      "url": "https://doi.org/10.1016/C2013-0-10329-X",
      "persistent_id": "doi:10.1016/C2013-0-10329-X"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "linear-operator",
      "term": "linear operator",
      "occurrence": "first"
    },
    {
      "definition_id": "operator-domain",
      "term": "domain",
      "occurrence": "first"
    },
    {
      "definition_id": "bounded-operator",
      "term": "bounded",
      "occurrence": "first"
    },
    {
      "definition_id": "unbounded-operator",
      "term": "unbounded",
      "occurrence": "first"
    },
    {
      "definition_id": "dense-domain",
      "term": "dense",
      "occurrence": "first"
    },
    {
      "definition_id": "adjoint",
      "term": "adjoint",
      "occurrence": "first"
    },
    {
      "definition_id": "symmetric-operator",
      "term": "symmetric",
      "occurrence": "first"
    },
    {
      "definition_id": "self-adjoint-operator",
      "term": "self-adjoint",
      "occurrence": "first"
    },
    {
      "definition_id": "commutator",
      "term": "commutator",
      "occurrence": "first"
    }
  ]
}
---
# Operators, Domains, and Self-Adjointness

A {{def:linear-operator|linear operator}} includes its {{def:operator-domain|domain}}: \(A:D(A)\to\mathcal H\). The rule \(A\psi\) is meaningful only for \(\psi\in D(A)\), and the formal rule alone does not specify the operator.

## What a finite model can check

A {{def:bounded-operator|bounded}} operator has a finite \(C\) with \(\|A\psi\|\le C\|\psi\|\) throughout its stated scope. Every matrix on a finite-dimensional Hilbert space is bounded. In a declared orthonormal \(\mathbb C^2\) coordinate model, linearity of a selected witness, an analytic norm bound for a diagonal matrix, matrix symmetry, and Hermitian/self-adjointness of an everywhere-defined matrix are all meaningful finite claims.

The worked example deliberately performs these checks first. Its predicates are explicitly scoped to their representation and data. A witness predicate checks only its supplied inputs; it is not a proof over all complex vectors unless an analytic argument is stated alongside it.

## What finite computation cannot decide

An {{def:unbounded-operator|unbounded}} operator admits no uniform bound on its declared domain. For \(T\) on \(\ell^2\), \((Tx)_n=n x_n\), the unit vector \(e_k\) has \(\|Te_k\|/\|e_k\|=k\). Since \(k\) is arbitrary, this is an analytic proof of unboundedness. Computing ratios on finite truncations only displays the finite-window behavior; every fixed truncation is bounded.

Likewise, a {{def:dense-domain|dense}} domain approximates every Hilbert-space vector in norm. Finite-support sequences are dense in \(\ell^2\): for \(x\in\ell^2\), its first-\(N\)-coordinate truncation has squared error \(\sum_{n>N}|x_n|^2\), which tends to zero by the definition of \(\ell^2\). Code can compute a finite supplied tail or a finite-input truncation; it cannot certify this universal limiting statement. Therefore the example intentionally provides no predicates named `isUnbounded` or `isDense`.

## Adjoint, symmetry, and self-adjointness

Assume \(A\) is densely defined. Its {{def:adjoint|adjoint}} has domain

\[
D(A^*)=\{\phi\in\mathcal H:\exists\eta\in\mathcal H,\ \langle\phi|A\psi\rangle=\langle\eta|\psi\rangle\ \text{for every }\psi\in D(A)\},
\]

with \(A^*\phi=\eta\). The first argument is conjugate-linear under this wiki convention. A {{def:symmetric-operator|symmetric}} operator obeys \(\langle\phi|A\psi\rangle=\langle A\phi|\psi\rangle\) for \(\phi,\psi\in D(A)\), equivalently \(A\subset A^*\). A {{def:self-adjoint-operator|self-adjoint}} operator satisfies \(A=A^*\), including \(D(A)=D(A^*)\).

For an everywhere-defined finite matrix in an orthonormal basis, \(H=H^\dagger\) is equivalent to self-adjointness in that finite model. It is not a test for an unbounded operator. A restricted derivative can be symmetric by integration by parts while its adjoint has a larger domain; boundary conditions and adjoint-domain analysis are separate work.

This distinction matters later for formal quantum constraints, including Wheeler–DeWitt-type expressions \(\widehat{\mathcal C}\Psi=0\): a displayed differential expression becomes an operator equation only after its Hilbert space, action, and domain are declared. Symmetry or self-adjointness questions, and the construction of a physical inner product, are additional model-dependent steps; no finite matrix check settles them.

## Worked sequence and later use

[Finite C² Witnesses, \(\ell^2\) Truncations, and a Restricted-Domain Contrast](../examples/example-operators-domains-self-adjointness.md) follows this order: finite linearity; bounded diagonal matrix; analytic \(\ell^2\) unboundedness plus truncation ratios; finite-support density plus tail norms; and finite self-adjointness followed by a non-computational derivative contrast. For sums, products, or a {{def:commutator|commutator}} of unbounded operators, every displayed action still needs a compatible stated domain.

**Source-review boundary:** the adjoint/domain claims and the \(\ell^2\) examples use the approved functional-analysis source listed above. This page does not prove the underlying functional-analysis theorems; later spectral or Stone-theorem uses require their own scoped source verification.
