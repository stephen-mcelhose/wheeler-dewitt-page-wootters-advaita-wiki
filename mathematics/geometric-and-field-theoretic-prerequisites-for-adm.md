---
{
  "schema_version": "2.0",
  "id": "geometric-and-field-theoretic-prerequisites-for-adm",
  "type": "concept",
  "title": "Geometric and Field-Theoretic Prerequisites for ADM",
  "summary": "The spatial geometric and field-variable language needed before the ADM canonical formulation.",
  "review_status": "draft",
  "parents": [
    "spacetime-foliations-and-general-relativity-primer",
    "hamiltonian-phase-space-and-poisson-brackets"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "canonical-gravity"
    }
  ],
  "sources": [
    {
      "title": "E. Gourgoulhon, 3+1 Formalism in General Relativity",
      "url": "https://arxiv.org/abs/gr-qc/0703035",
      "persistent_id": "arXiv:gr-qc/0703035"
    },
    {
      "title": "R. Arnowitt, S. Deser, and C. Misner, The Dynamics of General Relativity",
      "url": "https://arxiv.org/abs/gr-qc/0405109",
      "persistent_id": "arXiv:gr-qc/0405109"
    }
  ]
}
---
# Geometric and Field-Theoretic Prerequisites for ADM

On each spatial hypersurface, the ADM configuration variable is a spatial metric: a smoothly varying, positive-definite tensor field that assigns spatial lengths and angles. It is a field rather than a finite list of coordinates, so the configuration space contains one metric value at every spatial point. This field character is why later canonical expressions involve spatial integrals, functional derivatives, and locality conditions.

The inverse metric is the tensor field that reverses the metric’s index-lowering action. Together, the metric and its inverse distinguish covectors from vectors and permit contractions of spatial indices. The metric also determines the volume density customarily written as \(\sqrt h\), where \(h\) denotes the determinant of the metric components in a coordinate chart. This density supplies the coordinate-independent spatial volume element used in geometric integrals.

A spatial metric determines its compatible torsion-free spatial derivative, usually denoted \(D_a\). Compatibility means that this derivative preserves the metric, so it consistently differentiates spatial tensors while respecting lengths and contractions. Its curvature is summarized by the spatial scalar curvature, customarily written \({}^{(3)}R\). Scalar curvature is local geometric information, not an additional independent field chosen alongside the metric.

Boundary conditions are part of this setup. Varying geometric actions and moving spatial derivatives by integration by parts can produce boundary terms. On compact boundaryless slices those terms may vanish under the stated regularity assumptions; at finite or asymptotic boundaries they can require boundary data, counterterms, or physical generator terms. Thus a formal bulk expression cannot by itself settle which variations or Hamiltonian generators are well defined.

This page supplies geometric vocabulary only. It does not choose ADM sign, curvature, momentum, or boundary conventions; those must be declared where an ADM formula is used.
