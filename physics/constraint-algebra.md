---
{
  "schema_version": "2.0",
  "id": "constraint-algebra",
  "type": "concept",
  "title": "Hypersurface-Deformation Algebra",
  "summary": "The first-class constraint relations of canonical general relativity.",
  "review_status": "draft",
  "parents": [
    "adm-constraints"
  ],
  "relationships": [
    {
      "type": "prerequisite-for",
      "target": "dirac-quantization-gravity"
    },
    {
      "type": "related-to",
      "target": "def-anomaly"
    },
    {
      "type": "related-to",
      "target": "def-smearing"
    },
    {
      "type": "related-to",
      "target": "def-structure-function"
    }
  ],
  "sources": [
    {
      "title": "T. Thiemann, Lectures on Loop Quantum Gravity",
      "url": "https://arxiv.org/abs/gr-qc/0110034",
      "persistent_id": "arXiv:gr-qc/0110034"
    },
    {
      "title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems",
      "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems",
      "persistent_id": "ISBN:9780691037691"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "smearing",
      "term": "smeared constraints",
      "occurrence": "first"
    },
    {
      "definition_id": "structure-function",
      "term": "structure functions",
      "occurrence": "first"
    },
    {
      "definition_id": "anomaly",
      "term": "constraint anomaly",
      "occurrence": "first"
    }
  ]
}
---
# Hypersurface-Deformation Algebra

In the vacuum, smooth compact-boundaryless regime fixed in [Canonical Gravity](canonical-gravity.md), define [smeared constraints](../definitions/def-smearing.md) \(H[N]=\int_\Sigma d^3x\,N\mathcal H_\perp\) and \(D[\vec N]=\int_\Sigma d^3x\,N^a\mathcal H_a\). Their classical Poisson brackets take the form
\[
\{D[\vec N],D[\vec M]\}=D[[\vec N,\vec M]],
\]
\[
\{D[\vec N],H[M]\}=H[\mathcal L_{\vec N}M],
\]
\[
\{H[N],H[M]\}=D[h^{ab}(N\partial_bM-M\partial_bN)].
\]
The final bracket contains the inverse spatial metric \(h^{ab}\), so these are [structure functions](../definitions/def-structure-function.md) rather than constant structure constants. These are classical differentiable-generator relations in the declared regime, not a quantum commutator algebra. At the quantum level, representing the constraints consistently requires attention to ordering, regulation, domains, and closure. A [constraint anomaly](../definitions/def-anomaly.md) can invalidate the proposed quantum constraint system.
