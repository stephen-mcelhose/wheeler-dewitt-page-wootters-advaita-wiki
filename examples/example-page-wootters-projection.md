---
{
  "schema_version": "2.0",
  "id": "example-page-wootters-projection",
  "type": "example",
  "title": "Ideal Clock: Page–Wootters Projection and Sign Check",
  "summary": "A formal ideal-clock derivation that makes the sign convention explicit.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["derivation"],
  "modality": ["text"],
  "topics": ["clock-states", "conditional-page-wootters-state", "page-wootters-mechanism"],
  "teaches": ["project a global constraint onto a clock bra", "verify a sign convention", "identify formal ideal-clock assumptions"],
  "prerequisites": ["clock-states", "conditional-page-wootters-state", "operators-and-domains"],
  "action": "Apply the clock bra to the constraint term by term, substitute the stated clock convention, and verify the final sign.",
  "non_conclusion": "This formal calculation does not show that an ideal global clock exists, that the tensor-product split survives all gravitational constraints, or that Page–Wootters solves the full problem of time.",
  "relationships": [
    {"type": "illustrates", "target": "conditional-page-wootters-state"},
    {"type": "illustrates", "target": "page-wootters-mechanism"}
  ],
  "sources": [
    {"title": "D. N. Page and W. K. Wootters, Evolution without evolution: Dynamics described by stationary observables", "url": "https://doi.org/10.1103/PhysRevD.27.2885", "persistent_id": "doi:10.1103/PhysRevD.27.2885"}
  ]
}
---

# Ideal Clock: Page–Wootters Projection and Sign Check

Assume the formal constraint

\[
(\hat H_C\otimes I_S+I_C\otimes\hat H_S)|\Psi\rangle=0
\]

and define \(|\widetilde\psi_S(t)\rangle=({}_C\langle t|\otimes I_S)|\Psi\rangle\). Use the convention

\[
{}_C\langle t|\hat H_C=-i\hbar\partial_t{}_C\langle t|.
\]

Applying \({}_C\langle t|\otimes I_S\) to the constraint yields

\[
-i\hbar\partial_t|\widetilde\psi_S(t)\rangle+\hat H_S|\widetilde\psi_S(t)\rangle=0.
\]

Therefore

\[
i\hbar\partial_t|\widetilde\psi_S(t)\rangle=\hat H_S|\widetilde\psi_S(t)\rangle.
\]

The derivation is formal because ideal clock kets are generalized states and the relevant domains and differentiability assumptions must be supplied in a concrete construction.
