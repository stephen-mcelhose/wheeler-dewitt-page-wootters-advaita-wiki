---
{
  "schema_version": "2.0",
  "id": "composite-systems",
  "type": "concept",
  "title": "Composite Quantum Systems",
  "summary": "Finite-dimensional tensor-product systems, product and entangled states, density operators, and unconditioned reduced states.",
  "review_status": "draft",
  "parents": ["dirac-notation", "operators-and-domains"],
  "relationships": [
    {"type": "prerequisite-for", "target": "conditional-states"},
    {"type": "prerequisite-for", "target": "page-wootters-mechanism"},
    {"type": "illustrates", "target": "example-composite-bell-state-partial-trace"},
    {"type": "related-to", "target": "def-tensor-product"},
    {"type": "related-to", "target": "def-density-operator"},
    {"type": "related-to", "target": "def-partial-trace"},
    {"type": "related-to", "target": "def-reduced-state"},
    {"type": "related-to", "target": "def-entanglement"}
  ],
  "sources": [
    {"title": "M. Nielsen and I. Chuang, Quantum Computation and Quantum Information", "url": "https://doi.org/10.1017/CBO9780511976667", "persistent_id": "doi:10.1017/CBO9780511976667"}
  ],
  "inline_definitions": [
    {"definition_id": "tensor-product", "term": "tensor product", "occurrence": "first"},
    {"definition_id": "density-operator", "term": "density operator", "occurrence": "first"},
    {"definition_id": "partial-trace", "term": "partial trace", "occurrence": "first"},
    {"definition_id": "reduced-state", "term": "reduced state", "occurrence": "first"},
    {"definition_id": "entanglement", "term": "entangled", "occurrence": "first"}
  ]
}
---
# Composite Quantum Systems

## Finite-dimensional scope and tensor-product order

This concept first works with finite-dimensional Hilbert spaces \(\mathcal H_C\) and \(\mathcal H_S\), representing a clock-labelled factor \(C\) and a system-labelled factor \(S\). Their composite space is the {{def:tensor-product|tensor product}}
\[
\mathcal H_{CS}=\mathcal H_C\otimes\mathcal H_S.
\]
The factor order is part of the representation: \(|c\rangle_C\otimes|s\rangle_S\), abbreviated \(|c\rangle_C|s\rangle_S\), has clock coordinates first and system coordinates second. If each factor has ordered basis \((|0\rangle,|1\rangle)\), this page uses the composite product-basis order
\[
(|0\rangle_C|0\rangle_S,\ |0\rangle_C|1\rangle_S,\ |1\rangle_C|0\rangle_S,\ |1\rangle_C|1\rangle_S).
\]
Thus \(|1\rangle_C|0\rangle_S\) has coordinate column \((0,0,1,0)^T\) in this chosen order. Reversing factors is a different ordering convention and requires an explicit swap map; it must never be silently assumed.

The inner product on simple tensors is fixed by
\[
\langle c_1\otimes s_1\mid c_2\otimes s_2\rangle
=\langle c_1|c_2\rangle_C\langle s_1|s_2\rangle_S,
\]
and extended linearly. This finite-dimensional presentation avoids the completion and domain details needed for general infinite-dimensional tensor products.

## Product states, entanglement, and density operators

A pure joint state is a normalized vector \(|\Psi\rangle\in\mathcal H_C\otimes\mathcal H_S\), or equivalently its ray. It is a **product state** when there are normalized \(|c\rangle\in\mathcal H_C\) and \(|s\rangle\in\mathcal H_S\) with \(|\Psi\rangle=|c\rangle\otimes|s\rangle\). It is {{def:entanglement|entangled}} when it is not a product state. This is a statement about a specified bipartition \(C:S\); it is not an absolute property independent of how the joint system is factored.

A {{def:density-operator|density operator}} \(\rho_{CS}\) is a positive semidefinite operator of trace one. A pure joint vector gives \(\rho_{CS}=|\Psi\rangle\langle\Psi|\); density operators also represent mixtures. The distinction between a product state and entanglement applies directly to pure states. Mixed-state separability requires a separate convex-combination definition and is not established merely by checking whether a mixed density operator is one tensor product.

## Reduced state: discard a factor, do not select an outcome

The {{def:partial-trace|partial trace}} over \(C\) gives the {{def:reduced-state|reduced state}}
\[
\rho_S=\operatorname{Tr}_C(\rho_{CS}).
\]
It is the unique operator on \(S\) satisfying
\[
\operatorname{Tr}_S(A_S\rho_S)
=\operatorname{Tr}_{CS}[(I_C\otimes A_S)\rho_{CS}]
\]
for every system operator \(A_S\). Hence \(\rho_S\) supplies the statistics of system-only observables when the clock factor is ignored, not read out. For a product density operator \(\rho_C\otimes\rho_S\), tracing out \(C\) returns \(\rho_S\). An entangled pure joint state can instead have a mixed reduced state.

A reduced state is **unconditioned**: no outcome has been selected and no measurement update is implied. A conditional state requires a declared condition and, where a post-measurement update is intended, a declared instrument. That distinction is the subject of [Measurements and Conditional States](conditional-states.md).

## Scope boundary

The tensor-factor labels in this finite model are assumed, not derived. In constrained or gravitational theories, a clock/system factorization can be nonunique, approximate, or unavailable after constraints are imposed. Nothing here establishes a preferred physical clock, a continuous ideal clock, or a factorization of full gravity.
