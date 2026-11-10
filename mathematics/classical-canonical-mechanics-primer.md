---
{
  "schema_version": "2.0",
  "id": "classical-canonical-mechanics-primer",
  "type": "concept",
  "title": "Classical Canonical Mechanics Primer",
  "summary": "A bounded finite-dimensional introduction to Lagrangians, conjugate momenta, Hamiltonians, and externally timed Hamiltonian evolution.",
  "review_status": "ai_reviewed",
  "parents": [],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "hamiltonian-phase-space-and-poisson-brackets"
    },
    {
      "type": "related-to",
      "target": "def-lagrangian"
    },
    {
      "type": "related-to",
      "target": "def-hamiltonian"
    },
    {
      "type": "illustrates",
      "target": "example-lagrangian-to-hamiltonian-particle"
    }
  ],
  "sources": [
    {
      "title": "V. I. Arnold, Mathematical Methods of Classical Mechanics",
      "url": "https://doi.org/10.1007/978-1-4757-2063-1",
      "persistent_id": "doi:10.1007/978-1-4757-2063-1"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "lagrangian",
      "term": "Lagrangian",
      "occurrence": "first"
    },
    {
      "definition_id": "hamiltonian",
      "term": "Hamiltonian",
      "occurrence": "first"
    }
  ]
}
---
# Classical Canonical Mechanics Primer

## Scope

This compact primer uses a finite number of smooth configuration coordinates \(q^i\) and an **external** time parameter \(t\). It assumes a regular Lagrangian: the relations below can be inverted to express velocities \(\dot q^i=dq^i/dt\) in terms of \((q,p,t)\). Singular Lagrangians, constraints, field theory, and relativity are deferred to **Classical Constrained Systems**.

## From a Lagrangian to canonical variables

A {{def:lagrangian|Lagrangian}} \(L(q,\dot q,t)\) is a function of coordinates, their externally timed velocities, and possibly \(t\). Its conjugate momenta are

\[
p_i=\frac{\partial L}{\partial \dot q^i}.
\]

Here \(i\) labels degrees of freedom and repeated labels are summed. If the velocity–momentum relation is regular, define the {{def:hamiltonian|Hamiltonian}}

\[
H(q,p,t)=p_i\dot q^i-L(q,\dot q,t),
\]

with each \(\dot q^i\) replaced by its expression in \((q,p,t)\). The resulting canonical variables are \((q^i,p_i)\). They will be organized as phase space in the next concept.

For a particle of mass \(m>0\) in a potential \(V(q)\),

\[
L=\frac12m\dot q^2-V(q),\qquad p=m\dot q,\qquad H=\frac{p^2}{2m}+V(q).
\]

The equality of this \(H\) with familiar energy is a property of this standard mechanical form; a Hamiltonian is not universally “the energy,” especially in constrained systems.

## External-time evolution

For the regular external-time model, Hamilton’s equations are

\[
\frac{dq^i}{dt}=\frac{\partial H}{\partial p_i},\qquad
\frac{dp_i}{dt}=-\frac{\partial H}{\partial q^i}.
\]

These equations describe change with respect to the already supplied external time \(t\). This use of \(t\) is intentionally distinct from the gauge parameter \(s\) introduced later for constraint flows. A constrained Hamiltonian equation may contain arbitrary multipliers and need not describe external-time evolution.

## What this does not establish

This primer does not show that every Lagrangian admits a Hamiltonian description of this form, that every Hamiltonian is conserved, or that canonical variables are globally available. It supplies only the local regular mechanics required to read the next concept.
