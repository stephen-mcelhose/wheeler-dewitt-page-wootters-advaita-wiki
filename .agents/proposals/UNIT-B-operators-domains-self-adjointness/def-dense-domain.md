---
{
  "schema_version": "2.0",
  "id": "def-dense-domain",
  "type": "definition",
  "title": "Dense Domain",
  "summary": "A domain whose vectors approximate every vector of the Hilbert space in norm.",
  "review_status": "draft",
  "parents": [],
  "relationships": [{"type": "related-to", "target": "operators-and-domains"}],
  "sources": [{"title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis", "url": "https://doi.org/10.1016/C2013-0-10329-X", "persistent_id": "doi:10.1016/C2013-0-10329-X"}]
}
---
# Dense Domain

A domain \(D(A)\subset\mathcal H\) is **dense** in \(\mathcal H\) when, for every \(\psi\in\mathcal H\) and every \(\varepsilon>0\), there is a \(\phi\in D(A)\) with \(\|\psi-\phi\|<\varepsilon\). Density is an infinite, norm-topological assertion, not a property that finitely many vectors can decide. Finite-support truncations can calculate the error for one supplied sequence and illustrate the approximation proof, but do not decide density in general.

For a densely defined operator, the Hilbert-space adjoint is defined through its inner-product relation on a specified adjoint domain.

Learn more: [Operators, Domains, and Self-Adjointness](../mathematics/operators-and-domains.md).
