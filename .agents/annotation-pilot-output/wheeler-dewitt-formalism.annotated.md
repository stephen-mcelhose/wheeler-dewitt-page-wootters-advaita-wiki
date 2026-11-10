---
{
  "schema_version": "2.0",
  "id": "wheeler-dewitt-formalism",
  "type": "concept",
  "title": "Wheeler–DeWitt Formalism",
  "summary": "The formal local quantum constraints of canonical gravity, together with their unresolved definition problems.",
  "review_status": "draft",
  "parents": [
    "adm-constraints",
    "superspace",
    "dirac-quantization-gravity"
  ],
  "relationships": [
    {
      "type": "addresses",
      "target": "problem-of-time"
    },
    {
      "type": "related-to",
      "target": "def-anomaly"
    },
    {
      "type": "related-to",
      "target": "def-functional-derivative"
    }
  ],
  "sources": [
    {
      "title": "T. Thiemann, Lectures on Loop Quantum Gravity",
      "url": "https://arxiv.org/abs/gr-qc/0110034",
      "persistent_id": "arXiv:gr-qc/0110034"
    },
    {
      "title": "B. S. DeWitt, Quantum Theory of Gravity. I. The Canonical Theory",
      "url": "https://doi.org/10.1103/PhysRev.160.1113",
      "persistent_id": "doi:10.1103/PhysRev.160.1113"
    },
    {
      "title": "E. Anderson, Problem of Time in Quantum Gravity",
      "url": "https://arxiv.org/abs/1206.2403",
      "persistent_id": "arXiv:1206.2403"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "functional-derivative",
      "term": "functional derivatives",
      "occurrence": "first"
    }
  ]
}
---
# Wheeler–DeWitt Formalism

The formal vacuum Wheeler–DeWitt conditions are \(\hat{\mathcal H}^{\rm vac}_\perp(x)\Psi[h]=0\) and \(\hat{\mathcal H}_a(x)\Psi[h]=0\) for all \(x\in\Sigma\), using the vacuum, compact-boundaryless convention declared in [Canonical Gravity](canonical-gravity.md). The shorthand \(\hat H\Psi=0\) is used only for declared reduced models or as a schematic abbreviation.

In a formal metric representation, \(\hat h_{ab}(x)\Psi[h]=h_{ab}(x)\Psi[h]\) and \(\hat\pi^{ab}(x)\Psi[h]=-i\hbar\delta\Psi[h]/\delta h_{ab}(x)\). With the lower-index DeWitt supermetric \(G_{abcd}\), a schematic scalar condition has the strictly vacuum pattern
\[
\hat{\mathcal H}^{\rm vac}_\perp(x)\Psi[h]\sim\left[-16\pi G\hbar^2G_{abcd}(h;x)\frac{\delta^2}{\delta h_{ab}(x)\delta h_{cd}(x)}-\frac{\sqrt h}{16\pi G}{}^{(3)}R(x)\right]\Psi[h]=0.
\]
Products of {{def:functional-derivative|functional derivatives}} at coincident points require regularization; no factor ordering, regulator, domain, quantum closure, physical inner product, or observable algebra is defined by this formal pattern. Matter, cosmological-constant, noncompact, and finite-boundary additions require separately declared actions, normalizations, and source audits. The formalism is an approach to quantum gravity, not an experimentally established completed theory.
