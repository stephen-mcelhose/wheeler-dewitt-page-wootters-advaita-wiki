---
{
  "schema_version": "2.0",
  "id": "spacetime-foliations-and-general-relativity-primer",
  "type": "concept",
  "title": "Spacetime Foliations and General Relativity Primer",
  "summary": "The geometric bridge from constrained mechanics to the 3+1 canonical formulation of general relativity.",
  "review_status": "draft",
  "parents": [
    "parametrized-particle"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "canonical-gravity"
    },
    {
      "type": "related-to",
      "target": "def-foliation"
    },
    {
      "type": "related-to",
      "target": "def-lapse"
    },
    {
      "type": "related-to",
      "target": "def-shift"
    },
    {
      "type": "related-to",
      "target": "def-induced-metric"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "foliation",
      "term": "foliation",
      "occurrence": "first"
    }
  ],
  "sources": [
    {
      "title": "R. Arnowitt, S. Deser, and C. Misner, The Dynamics of General Relativity",
      "url": "https://arxiv.org/abs/gr-qc/0405109",
      "persistent_id": "arXiv:gr-qc/0405109"
    }
  ]
}
---
# Spacetime Foliations and General Relativity Primer

General relativity describes spacetime geometry rather than fields evolving on a fixed background spacetime. To formulate it canonically, one assumes an appropriate globally hyperbolic setting and represents spacetime as a family of spatial hypersurfaces \(\Sigma_t\), called a **{{def:foliation|foliation}}**.

Each hypersurface carries an [induced spatial metric](../definitions/def-induced-metric.md) \(h_{ab}\). The [lapse](../definitions/def-lapse.md) \(N\) describes the normal separation between successive hypersurfaces, and the [shift](../definitions/def-shift.md) \(N^a\) describes how spatial coordinates are displaced from one hypersurface to the next. These quantities encode a chosen decomposition; they do not select a preferred physical time.

This is the geometric bridge from the parametrized-particle toy model to the ADM formalism. Boundary and asymptotic conditions matter: they can change the interpretation of Hamiltonian generators and must be stated in a full application.
