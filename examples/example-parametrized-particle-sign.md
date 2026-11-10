---
{
  "schema_version": "2.0",
  "id": "example-parametrized-particle-sign",
  "type": "example",
  "title": "Parametrized Particle: Recovering Schrödinger Evolution",
  "summary": "A synthetic sign-convention walkthrough for a deparametrizable constrained model.",
  "review_status": "ai_reviewed",
  "status": ["synthetic"],
  "patterns": ["derivation"],
  "modality": ["text"],
  "topics": ["parametrized-particle", "constrained-systems", "dirac-quantization"],
  "teaches": ["derive the Schrödinger equation from a parametrized-particle constraint", "separate a gauge parameter from an internal clock variable"],
  "prerequisites": ["constrained-systems", "dirac-quantization"],
  "action": "Apply the operator substitution p_t to the stated constraint and rearrange the result into the Schrödinger equation.",
  "non_conclusion": "This toy model does not establish a global internal time, a physical inner product, or a deparametrization for full general relativity.",
  "relationships": [
    {"type": "illustrates", "target": "parametrized-particle"}
  ],
  "sources": [
    {"title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems", "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems", "persistent_id": "ISBN:9780691037691"}
  ]
}
---

# Parametrized Particle: Recovering Schrödinger Evolution

Consider the synthetic constrained model

\[
C=p_t+H(q,p)\approx0.
\]

Quantize with \(\hat p_t=-i\hbar\partial_t\). The constraint condition becomes

\[
(-i\hbar\partial_t+\hat H)\Psi(t,q)=0.
\]

Moving the second term to the other side gives

\[
i\hbar\partial_t\Psi(t,q)=\hat H\Psi(t,q).
\]

The calculation shows how ordinary Schrödinger evolution can appear after choosing \(t\) as an internal clock variable in this simple model. Its force is deliberately limited by the stated non-conclusion.
