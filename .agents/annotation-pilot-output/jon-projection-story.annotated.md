---
{
  "schema_version": "2.0",
  "id": "jon-projection-story",
  "type": "concept",
  "title": "Exploratory Model: JON, Brackets, and Projection",
  "summary": "A personal, exploratory mathematical model using JON as a named state vector; it is not a physics claim about individuality or māyā.",
  "review_status": "draft",
  "parents": [
    "physics-method-boundary"
  ],
  "relationships": [
    {
      "type": "uses",
      "target": "dirac-notation"
    },
    {
      "type": "uses",
      "target": "inner-product-spaces"
    },
    {
      "type": "uses",
      "target": "born-rule-and-quantum-probability"
    },
    {
      "type": "analogical-comparison",
      "target": "maya"
    },
    {
      "type": "related-to",
      "target": "def-dual-vector"
    },
    {
      "type": "related-to",
      "target": "def-inner-product"
    },
    {
      "type": "related-to",
      "target": "def-ket"
    },
    {
      "type": "related-to",
      "target": "def-projector"
    }
  ],
  "sources": [
    {
      "title": "P. A. M. Dirac, The Principles of Quantum Mechanics",
      "url": "https://global.oup.com/academic/product/the-principles-of-quantum-mechanics-9780198520115",
      "persistent_id": "ISBN:9780198520115"
    }
  ],
  "inline_definitions": [
    {
      "definition_id": "ket",
      "term": "ket",
      "occurrence": "first"
    },
    {
      "definition_id": "dual-vector",
      "term": "dual vector",
      "occurrence": "first"
    },
    {
      "definition_id": "inner-product",
      "term": "inner product",
      "occurrence": "first"
    },
    {
      "definition_id": "projector",
      "term": "projector",
      "occurrence": "first"
    }
  ]
}
---
# Exploratory Model: JON, Brackets, and Projection

> [!WARNING] Under Construction
> **Not reviewed.** This is exploratory opinion and personal philosophical reflection, not a scientific or metaphysical conclusion.
> **Exploratory opinion for personal use.** This page uses mathematics as a reflective modeling language. It is not a scientific theory of consciousness, individuality, māyā, non-duality, or the universe.

## 1. Established mathematical statement

In Dirac notation, \(|\mathrm{JON}\rangle\) is a {{def:ket|ket}}: a vector in a Hilbert space. Its associated bra \(\langle\mathrm{JON}|\) is a {{def:dual-vector|dual vector}} supplied by the {{def:inner-product|inner product}}. In a chosen finite-dimensional orthonormal basis, writing the bra from the ket uses the **conjugate transpose** (also called the Hermitian adjoint): transpose the column into a row and complex-conjugate its entries. “Dual conjugate” is not the standard term; use **dual vector** for the mathematical object and **conjugate transpose/Hermitian adjoint** for this operation in coordinates.

If the vector is normalized, then

\[
\langle\mathrm{JON}|\mathrm{JON}\rangle=1.
\]

This equality holds only for a normalized representative. For example, the unnormalized vector

\[
|\mathrm{JON}\rangle=\begin{pmatrix}1+i\\5\end{pmatrix}
\]

has \(\langle\mathrm{JON}|\mathrm{JON}\rangle=27\). Its normalized representative is \(|\mathrm{JON}\rangle/\sqrt{27}\), and that representative has self-inner-product \(1\). Rescaling by \(1/\sqrt{27}\) changes the vector's length but represents the same pure-state ray.

This [inner product](../definitions/def-inner-product.md) is the norm squared of the vector. It is **not**, by itself, a physical collapse event or a statement that a system “becomes itself.” If a specific yes/no measurement is represented by the {{def:projector|projector}} onto \(|\mathrm{JON}\rangle\), then a system already in that state has probability one for the corresponding yes outcome.

In the opposite order,

\[
\hat P_{\mathrm{JON}}=|\mathrm{JON}\rangle\langle\mathrm{JON}|
\]

is a rank-one projector when \(|\mathrm{JON}\rangle\) is normalized. Applied to an arbitrary state \(|\psi\rangle\),

\[
\hat P_{\mathrm{JON}}|\psi\rangle=|\mathrm{JON}\rangle\langle\mathrm{JON}|\psi\rangle.
\]

It retains the component aligned with the JON direction and removes components orthogonal to that direction. The result is generally an unnormalized component; a measurement update and normalization are separate matters.

## 2. Proposed analogy/model

For personal reflection, treat \(\hat P_{\mathrm{JON}}\) as a **spotlight model of selection**: a rich state description is represented relative to one chosen direction, here named JON. The bra is the comparison operation—“how much of this description aligns with JON?”—and the ket supplies the selected direction.

This use of the labels **Alice**, **Bob**, or **JON** is intentional: they make the choice of direction vivid without claiming that a vector is a person.

## 3. Interpretive reflection

The model can prompt a question about perspective: if a description is conditioned on a selected direction, what becomes foregrounded and what remains outside that selected component? In a non-duality or [Advaita-adjacent](advaita-orientation.md) reflection, this may be used to examine the felt sense of a bounded individual perspective without assuming that this perspective exhausts every possible description. The term [māyā](maya.md) belongs to a distinct Advaita philosophical context; its presence here is an optional analogy prompt, not a result derived from the mathematics.

## 4. What does not follow

- A projector is a linear-algebra operation, not a model of a person or consciousness.
- Projection does not establish that individuality is false, illusory, or māyā.
- The expression \(\langle\mathrm{JON}|\mathrm{JON}\rangle=1\) does not describe collapse into a self.
- Quantum mechanics does not, from these equations, prove non-duality or any Advaita doctrine.
