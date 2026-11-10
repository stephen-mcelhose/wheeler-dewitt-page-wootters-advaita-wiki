---
{
  "schema_version": "2.0",
  "id": "def-adjoint",
  "type": "definition",
  "title": "Adjoint",
  "summary": "The operator determined by the inner-product relation on its explicitly defined domain.",
  "review_status": "ai_reviewed",
  "parents": [],
  "relationships": [
    {
      "type": "related-to",
      "target": "operators-and-domains"
    }
  ],
  "sources": [
    {
      "title": "M. Reed and B. Simon, Methods of Modern Mathematical Physics I: Functional Analysis",
      "url": "https://doi.org/10.1016/C2013-0-10329-X",
      "persistent_id": "doi:10.1016/C2013-0-10329-X"
    }
  ]
}
---
# Adjoint

For a densely defined operator \(A:D(A)\to\mathcal H\), the domain \(D(A^*)\) consists of vectors \(\phi\in\mathcal H\) for which there is an \(\eta\in\mathcal H\) satisfying \(\langle\phi|A\psi\rangle=\langle\eta|\psi\rangle\) for every \(\psi\in D(A)\). The adjoint is defined by \(A^*\phi=\eta\). In a finite orthonormal coordinate basis, the adjoint is represented by the conjugate-transpose matrix.

Learn more: [Operators, Domains, and Self-Adjointness](../mathematics/operators-and-domains.md).
