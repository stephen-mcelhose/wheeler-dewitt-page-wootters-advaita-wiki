---
{
  "schema_version": "2.0",
  "id": "adm-constraints",
  "type": "concept",
  "title": "Hamiltonian and Momentum Constraints",
  "summary": "The local constraints encoding normal and tangential hypersurface deformations.",
  "review_status": "draft",
  "parents": [
    "canonical-gravity"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "constraint-algebra"
    },
    {
      "type": "prerequisite-for",
      "target": "wheeler-dewitt-formalism"
    },
    {
      "type": "related-to",
      "target": "def-constraint"
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
      "title": "B. S. DeWitt, Quantum Theory of Gravity. I. The Canonical Theory",
      "url": "https://doi.org/10.1103/PhysRev.160.1113",
      "persistent_id": "doi:10.1103/PhysRev.160.1113"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "constraint",
      "term": "constraints",
      "occurrence": "first"
    }
  ]
}
---
# Hamiltonian and Momentum Constraints

In the declared vacuum, compact-boundaryless convention of [Canonical Gravity](canonical-gravity.md), the ADM Hamiltonian is
\[
H_{\mathrm{ADM}}[N,N^a]=\int_\Sigma d^3x\,(N\mathcal H_\perp+N^a\mathcal H_a).
\]
The local constraints are \(\mathcal H_\perp(x)\approx0\) and \(\mathcal H_a(x)\approx0\) for every \(x\in\Sigma\). Their vacuum expressions are
\[
\mathcal H_\perp=\frac{16\pi G}{\sqrt h}\left(\pi^{ab}\pi_{ab}-\frac12\pi^2\right)-\frac{\sqrt h}{16\pi G}\,{}^{(3)}R,
\qquad
\mathcal H_a=-2h_{ab}D_c\pi^{bc}.
\]
Here \(\mathcal H_\perp\) and \(\mathcal H_a\) have density weight \(+1\), while \(N\) and \(N^a\) have weight zero. Matter, cosmological-constant, noncompact, and finite-boundary extensions require separately declared conventions and are not represented in these displays. The momentum constraints generate spatial diffeomorphisms; the scalar constraint participates in normal deformations within the hypersurface-deformation framework. A single global equation is not an adequate replacement for these local conditions in full canonical gravity.
