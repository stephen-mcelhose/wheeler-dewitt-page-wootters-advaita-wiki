---
{
  "schema_version": "2.0",
  "id": "constrained-systems",
  "type": "concept",
  "title": "Classical Constrained Systems",
  "summary": "A scoped Dirac–Bergmann introduction to constraint surfaces, constraint classes, gauge flow, and gauge fixing.",
  "review_status": "draft",
  "parents": ["classical-canonical-mechanics-primer", "hamiltonian-phase-space-and-poisson-brackets"],
  "relationships": [
    {"type": "prerequisite-for", "target": "dirac-quantization"},
    {"type": "prerequisite-for", "target": "parametrized-particle"},
    {"type": "illustrates", "target": "example-parametrized-free-particle-constraint-flow"},
    {"type": "related-to", "target": "def-constraint"},
    {"type": "related-to", "target": "def-constraint-surface"},
    {"type": "related-to", "target": "def-canonical-hamiltonian"},
    {"type": "related-to", "target": "def-total-hamiltonian"},
    {"type": "related-to", "target": "def-weak-equality"},
    {"type": "related-to", "target": "def-first-class-constraint"},
    {"type": "related-to", "target": "def-second-class-constraint"},
    {"type": "related-to", "target": "def-gauge-orbit"},
    {"type": "related-to", "target": "def-gauge-fixing"}
  ],
  "sources": [
    {"title": "P. A. M. Dirac, Lectures on Quantum Mechanics", "url": "https://store.doverpublications.com/products/9780486417134", "persistent_id": "ISBN:9780486417134"},
    {"title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems", "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems", "persistent_id": "ISBN:9780691037691"}
  ],
  "inline_definitions": [
    {"definition_id": "constraint", "term": "constraint", "occurrence": "first"},
    {"definition_id": "constraint-surface", "term": "constraint surface", "occurrence": "first"},
    {"definition_id": "weak-equality", "term": "weak equality", "occurrence": "first"},
    {"definition_id": "first-class-constraint", "term": "first-class", "occurrence": "first"},
    {"definition_id": "second-class-constraint", "term": "second-class", "occurrence": "first"},
    {"definition_id": "gauge-orbit", "term": "gauge orbit", "occurrence": "first"},
    {"definition_id": "gauge-fixing", "term": "gauge fixing", "occurrence": "first"}
  ]
}
---
# Classical Constrained Systems

## Scope

Consider a finite-dimensional smooth canonical phase space and a regular local portion of a Dirac–Bergmann analysis. A singular Lagrangian can produce a {{def:constraint|constraint}} \(\phi_a(q,p)\approx0\). The simultaneous conditions define the {{def:constraint-surface|constraint surface}}

\[
\Gamma=\{(q,p):\phi_a(q,p)=0\text{ for all }a\}.
\]

The notation \(F\approx G\) means {{def:weak-equality|weak equality}}: \(F-G\) vanishes when restricted to \(\Gamma\). It is not permission to replace \(F\) by \(G\) before computing a Poisson bracket. For example, even if \(\phi\approx0\), the bracket \(\{F,\phi\}\) can be nonzero on \(\Gamma\).

## Canonical and total Hamiltonians

The Legendre construction gives a {{def:canonical-hamiltonian|canonical Hamiltonian}} \(H_{\rm can}\). When primary constraints \(\phi_a\) occur, the Dirac total Hamiltonian is

\[
H_T=H_{\rm can}+\lambda^a\phi_a.
\]

The \(\lambda^a\) are Lagrange multipliers. They are auxiliary functions selected subject to consistency conditions; they are not automatically physical observables or a time coordinate. Requiring constraints to remain satisfied may determine some multipliers and may produce secondary constraints. This page does not execute the full iterative algorithm.

## First class, second class, and gauge

A constraint set is {{def:first-class-constraint|first-class}} when its brackets with all constraints vanish weakly (equivalently, close into constraints locally):

\[
\{\phi_a,\phi_b\}\approx0.
\]

Under the usual regularity and complete-generator assumptions, the associated first-class generator produces gauge transformations. Its integral curves on \(\Gamma\) are {{def:gauge-orbit|gauge orbits}}: multiple phase-space descriptions of one physical situation.

For a {{def:second-class-constraint|second-class}} set \(\chi_a\), the matrix \(C_{ab}=\{\chi_a,\chi_b\}\) is invertible on \(\Gamma\). These constraints do not supply gauge redundancy in the same way; one may solve them locally or introduce the Dirac bracket. The Dirac-bracket construction is outside this unit.

## Gauge flow is not external-time evolution

If a first-class generator \(G\) is smeared with a gauge parameter \(s\), then locally

\[
\frac{dF}{ds}=\{F,G\}.
\]

Here \(s\) labels a gauge transformation. **It is not time.** This equation differs in interpretation from \(dF/dt=\{F,H\}+\partial F/\partial t\) in the regular external-time model. A constraint can contain a variable later selected as an internal clock, but that selection requires extra conditions and does not convert the gauge parameter into external time.

A {{def:gauge-fixing|gauge fixing}} imposes supplementary conditions intended to intersect each nearby gauge orbit once. It can produce a reduced description, but global intersections, Gribov-type ambiguities, and boundary issues can fail. Gauge fixing is therefore a local construction here, not a universal recipe.

The next example uses a parametrized free particle to calculate constraint flow explicitly and contrasts it with a bounded second-class pair. It does not establish a global clock or resolve the time problem in gravity.
