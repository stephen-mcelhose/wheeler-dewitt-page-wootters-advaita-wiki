---
{
  "schema_version": "2.0",
  "id": "canonical-gravity",
  "type": "concept",
  "title": "Canonical Gravity and the ADM Split",
  "summary": "The Hamiltonian formulation of general relativity obtained from a 3+1 decomposition.",
  "review_status": "draft",
  "parents": [
    "spacetime-foliations-and-general-relativity-primer"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "adm-constraints"
    },
    {
      "type": "addresses",
      "target": "problem-of-time"
    },
    {
      "type": "related-to",
      "target": "def-lagrange-multiplier"
    },
    {
      "type": "related-to",
      "target": "def-phase-space"
    }
  ],
  "sources": [
    {
      "title": "R. Arnowitt, S. Deser, and C. Misner, The Dynamics of General Relativity",
      "url": "https://arxiv.org/abs/gr-qc/0405109",
      "persistent_id": "arXiv:gr-qc/0405109"
    },
    {
      "title": "T. Thiemann, Lectures on Loop Quantum Gravity",
      "url": "https://arxiv.org/abs/gr-qc/0110034",
      "persistent_id": "arXiv:gr-qc/0110034"
    },
    {
      "title": "E. Anderson, Problem of Time in Quantum Gravity",
      "url": "https://arxiv.org/abs/1206.2403",
      "persistent_id": "arXiv:1206.2403"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "lagrange-multiplier",
      "term": "Lagrange multipliers",
      "occurrence": "first"
    }
  ]
}
---
# Canonical Gravity and the ADM Split

Building on the [spacetime-foliation primer](spacetime-foliations-and-general-relativity-primer.md), the ADM formulation decomposes spacetime into spatial hypersurfaces \(\Sigma_t\) under the usual global-hyperbolicity assumptions. The induced metric \(h_{ab}\) and [conjugate momentum](../definitions/def-phase-space.md) \(\pi^{ab}\) are canonical variables. Lapse \(N\) and shift \(N^a\) are [Lagrange multipliers](../definitions/def-lagrange-multiplier.md); the \(3+1\) split is a representation of general covariance, not a preferred physical time.

The displayed ADM family uses one bounded vacuum convention: signature \((-+++)\), future-directed unit normal \(n^\mu\), \(t^\mu=Nn^\mu+N^\mu\) with \(N>0\), \(c=1\), and explicit \(G\) and \(\hbar\). Take \(\Sigma\) smooth, compact, orientable, and without boundary, with smooth metric data, lapse, and shift. With \(K_{ab}=(\dot h_{ab}-D_aN_b-D_bN_a)/(2N)\), \(\pi^{ab}=\sqrt h(K^{ab}-h^{ab}K)/(16\pi G)\) is a symmetric contravariant density of weight \(+1\). The spatial curvature convention is \([D_a,D_b]v^c={} ^{(3)}R^c{}_{dab}v^d\).

In this compact-boundaryless regime, the ADM action is
\[
S_{\mathrm{ADM}}=\int dt\int_\Sigma d^3x\,[\pi^{ab}\dot h_{ab}-N\mathcal H_\perp-N^a\mathcal H_a].
\]
The bulk canonical Hamiltonian is a combination of local constraints. Finite-boundary and asymptotic cases, including their action terms, boundary conditions, differentiable generators, and charges, are excluded from these displays rather than covered by an unspecified boundary term.
