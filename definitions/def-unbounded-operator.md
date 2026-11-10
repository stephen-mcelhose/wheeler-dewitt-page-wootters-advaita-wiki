---
{
  "schema_version": "2.0",
  "id": "def-unbounded-operator",
  "type": "definition",
  "title": "Unbounded Operator",
  "summary": "A linear operator for which no uniform norm bound holds on its stated domain.",
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
# Unbounded Operator

A linear operator \(A:D(A)\to\mathcal H\) is **unbounded** when there is no finite \(C\) such that \(\|A\psi\|\le C\|\psi\|\) for every \(\psi\in D(A)\). This is a statement quantified over its declared (usually infinite-dimensional) domain; a finite collection of numerical samples cannot establish it. In particular, every operator on a finite-dimensional normed space is bounded.

An everywhere-defined **closed** linear operator between Banach spaces is bounded by the closed graph theorem. This standard boundary must be applied with its hypotheses; it does not turn a finite truncation into an unbounded operator.

Learn more: [Operators, Domains, and Self-Adjointness](../mathematics/operators-and-domains.md).
