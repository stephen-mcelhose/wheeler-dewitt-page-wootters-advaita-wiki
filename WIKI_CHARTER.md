<!-- review_status: ai_reviewed -->
# Wiki Charter

## Purpose and audience
- **Purpose:** Provide a rigorous, navigable physics-first deep dive into the Wheeler–DeWitt equation and the Page–Wootters relational-time mechanism. Only after readers complete an independent physics foundation does the wiki introduce a carefully bounded philosophical comparison layer involving selected Advaita Vedānta concepts, especially māyā.
- **Primary audience:** Physics students with undergraduate quantum mechanics and introductory general-relativity familiarity. Mathematical notation and explicit assumptions are central; the philosophical layer is optional and comes last.

## Scope and non-goals
- **In scope:** A physics curriculum of roughly 25–35 canonical concepts: a dedicated Dirac-notation primer; constrained Hamiltonian systems; ADM/canonical gravity; Hamiltonian and momentum constraints; Dirac quantization; superspace; the Wheeler–DeWitt equation; the problem of time; relational observables; Page–Wootters states; clocks; conditional states; ideal-clock assumptions; finite-clock corrections; and limitations. A final optional philosophical section introduces exploratory mathematical-modeling reflections on non-duality, including Advaita and māyā where appropriate, only after the physics sequence. Its worked vector stories intentionally use the labels Alice, Bob, or JON.
- **Non-goals:** A new theory unifying physics and Advaita; claims that either field proves the other; treating a philosophical model as an explanation of a quantum-gravity formalism; exhaustive coverage of quantum gravity, all Vedānta schools, or every interpretation of quantum mechanics; spiritual or medical advice.

## Source and research policy
Use the user-approved standard authoritative sources: primary research papers and peer-reviewed/institutional physics sources; primary translations and scholarly academic references for Advaita. Treat scientific and philosophical sources as distinct evidence domains. Do not imply empirical validation for comparative claims; label them as interpretive analogies, contrasts, or questions.

## Canonical document types
`concept`, `definition`, `guide`, and `redirect` are canonical graph types. `example` documents live only in `/examples` and do not define concepts. A **concept** is a teachable unit with explanation, prerequisites, equations or examples where useful, sources, and relationships. A **definition** is a short reusable explanation of a local term, symbol, or distinction; it can link to a concept for deeper study but does not need to appear in the main learning path. Definitions must not carry essential safety assumptions or caveats: those remain visible in the canonical concept body.

## Concept and relationship policy
Use stable kebab-case canonical IDs and a prerequisite-first physics hierarchy. Typed links use the controlled vocabulary `prerequisite-for`, `formalizes`, `addresses`, `derives-from`, `limitation`, `contrasts-with`, `analogical-comparison`, `historical-context`, `uses`, `illustrates`, and `related-to`. The physics graph must stand alone: no physics concept depends on Advaita nodes. Comparative links are restricted to the optional final layer and must state their limits.

## Review-status policy
Every graph node carries `review_status`: `draft` for authored but not independently reviewed content, `ai_reviewed` for content checked by an AI review pass, and `approved` only after explicit human approval. Generated indexes and reader documents display a corresponding status marker. Validation enforces the controlled values but does not convert an AI review into human approval.

## Definition and content-quality policy
Define concepts once in canonical documents. Separate source-based accounts from editorial synthesis. Present equations with assumptions and explain what follows only within the stated model. Use a three-layer exposure pattern: (1) the main learning path contains only concepts needed in sequence; (2) unfamiliar local vocabulary is linked to short definitions, shown as hoverable on pointer devices and tappable/clickable on touch devices, with a persistent “Learn more” route where a deeper concept exists; and (3) the glossary supports recall rather than first explanation. Hover/tap definitions are limited to one or two sentences plus minimal notation. They must never hide essential assumptions, sign conventions, limitations, or safety boundaries.

### Boundary between rigorous mathematics/physics and opinionated philosophical exploration

**Rigorous mathematics and physics** live in `mathematics/`, `physics/`, `page-wootters/`, `definitions/`, and `examples/`. They are explanatory and evidential material: every mathematical statement must be correct under stated assumptions; every physical claim must be scoped, sourced, and open to mathematical/physics review. Personal, philosophical, spiritual, or metaphysical interpretation is excluded from the evidential body of these nodes.

**Opinionated philosophical exploration** lives only in `philosophy/`. It is an exploratory mathematical-modeling and personal-reflection space, not a physics result, empirical theory, or metaphysical proof. A philosophical page may quote or link to established mathematics, but it must not alter, extend, or reinterpret the mathematical claim as evidence. Each such page must visibly separate: (a) **Established mathematical or physical statement**; (b) **Proposed analogy/model**; (c) **Interpretive reflection**; and (d) **What does not follow**. It may use Alice, Bob, or JON as intentional state-vector labels. A bra, ket, inner product, or projector may be used as a bounded modeling metaphor only after its standard mathematical meaning is stated first; no metaphor may be presented as evidence about consciousness, individuality, māyā, non-duality, turiya, or the physical universe.

**Linking rule:** rigorous nodes may not parent, prerequisite, cite, or depend on philosophy nodes. Philosophy may link outward to rigorous nodes only with `uses`, `related-to`, or explicitly bounded `analogical-comparison` relationships.

**Persistent review label:** every page in `philosophy/` must visibly state that it is **not reviewed** while its `review_status` is `draft`, using `> [!WARNING] Under Construction` plus wording that it is exploratory opinion/personal reflection and is not a scientific or metaphysical conclusion. Do not remove or soften this visible label until an appropriate philosophy/methods review has occurred and a human explicitly approves the page. A mathematical or physics review alone may validate only a quoted rigorous statement; it does not count as review of the philosophical interpretation.

The mathematics sequence precedes the physics sequence: inner-product spaces; norms, distance, and convergence; Hilbert spaces; quantum states, rays, and normalization; bases and coordinates; Dirac notation; projection operators; Born-rule probability; discrete versus generalized bases; unbounded operators and domains; tensor products; density operators; POVMs and conditional states; constrained Hamiltonian systems; then canonical gravity. Do not write the Wheeler–DeWitt equation as an unqualified ordinary eigenvalue equation: introduce local Hamiltonian and diffeomorphism constraints, kinematical versus physical state spaces, and regularization/ordering/domain/inner-product caveats first. Qualify live disputes, including whether Page–Wootters fully resolves any facet of the problem of time and the scope of māyā across Advaita exegesis.

## Source and provenance policy
Verify material claims against cited sources. Record an accessible reader URL and a persistent identifier where available. References are divided into physics, Advaita primary texts/translations, and scholarship; unapproved candidates are excluded.

## Examples policy
Examples live under `/examples`, are bounded teaching artifacts, identify model assumptions and non-conclusions, cite sources, and never redefine canonical concepts. Comparative examples cannot claim identity or causal correspondence between a physical formalism and a philosophical doctrine.

Examples outside `philosophy/` must use standard mathematical or physical labels—such as \(|\phi\rangle\), \(|\psi\rangle\), \(|0\rangle\), \(|1\rangle\), \(q,p\), \(h_{ab}\), clock \(C\), and system \(S\). Do not use personal names or person-like labels in rigorous mathematics, physics, or general teaching examples. Alice, Bob, and JON are permitted only in explicitly exploratory philosophy pages, where their pedagogical status and non-evidential limits remain visible.

### One concept, one self-contained example policy

Each canonical concept should eventually have at least one bounded worked example designed specifically for that concept. Examples are permitted to repeat code, notation, and elementary calculations from earlier examples when that repetition makes the current concept independently understandable. Do not remove needed explanatory setup merely to avoid duplication.

Before using any prerequisite idea, symbol, operation, or code helper in an example, define or briefly restate it locally at the level needed for that example. Link to the deeper prerequisite concept where useful, but do not force the learner to reconstruct essential steps from a previous example. Every example must clearly distinguish: (1) prerequisites being assumed; (2) local definitions/setup; (3) the concept-specific calculation or construction; and (4) scope/non-conclusions.

### Go-equivalent requirement for rigorous worked examples

Every worked example outside `philosophy/` MUST include a programmer-facing Go equivalent of its central finite or bounded calculation, construction, predicate, or invariant. The Go section must let a programmer inspect the same conceptual operation used in the mathematical example—not merely print a precomputed answer.

When a full direct computation would be mathematically dishonest or impossible in finite code—such as unboundedness, density, infinite series, generalized eigenvectors, continuum operator domains, functional derivatives, or a formal Wheeler–DeWitt expression—the example MUST include the closest honest computational counterpart: a finite truncation, finite witness, prefix monitor, certified bound, or explicit non-computational contrast. It MUST state what that code establishes and what it cannot establish. Do not omit code solely because the general mathematics is infinite-dimensional.

Each Go section must:

1. use concept-bearing names and scoped types where useful;
2. provide predicates for mathematical properties that are honestly checkable in the declared finite model;
3. name a predicate’s scope in its identifier when a general property cannot be decided, for example `IsOrthogonalProjector2D`, `IsSelfAdjointFiniteMatrix2D`, or `IsLinearWitnessMatrix2D`;
4. avoid dishonest universal predicates such as `IsUnbounded` or `IsDense` from finite data;
5. use errors for checkable violations of declared contracts, not claims about uncheckable infinite properties;
6. state finite/infinite, domain, basis/order, tolerance, and representation limits in local mathematical comments.

Philosophy examples may use code only when it first preserves the standard mathematical meaning and their exploratory status remains visible.

### Mathematical code-comment standard

Code comments in worked examples describe the **mathematical model**, not incidental implementation behavior. Use this pattern where code expresses a mathematical operation or predicate:

Classify every example assumption before writing a code comment. Do not present every assumption as a universal requirement.

1. **Mathematical precondition** — Start with `Given:` and state facts required to interpret the calculation: the objects' mathematical type, a pre-established basis, a domain, or a condition such as nonzero norm.
2. **Model scope** — State a deliberate restriction used to make a general idea calculable, such as a target space of \(\mathbb C^2\), a finite clock, or a compact boundaryless spatial slice. This is not automatically a general requirement of the concept.
3. **Convention or representation** — State a selected inner-product convention, sign convention, ordered basis, or coordinate/data representation. Distinguish the abstract object from its chosen representation when relevant.
4. **Illustrative choice** — State choices made for clarity that are not mathematically unique, such as the standard basis or a chosen phase step.
5. **Mathematical fact or limitation** — State the relevant definition, theorem, or limitation in ordinary language.
6. Use RFC 2119 keywords (`MUST`, `MUST NOT`, `SHOULD`, `MAY`) only for a precise, specable mathematical requirement or scope boundary—not as generic programming-style advice. The keyword MUST be read within the preceding preconditions and model scope.
7. State any representation limitation only when necessary; for example, a Go slice does not encode row/column orientation even when it stores coordinates of a bra or ket.
8. If the code assumes a concept that has not yet been established—such as spanning, linear independence, a target-space dimension, or an operator domain—the comment MUST name that precondition. The learning path must then supply the missing prerequisite concept before relying on the code as a teaching example.

Example:

```go
// Given: n and m label elements of one chosen discrete orthonormal basis.
// Model scope: this calculation concerns that selected basis only.
// The Kronecker delta is 1 when the labels are equal and 0 when they differ.
// In an orthonormal basis, ⟨n|m⟩ MUST equal δ_nm.
```

Example of an illustrative restriction:

```go
// Model scope: this example works in the two-dimensional complex space C².
// Illustration: e₀ and e₁ are chosen because their coordinates are transparent.
// In this C² model, two linearly independent vectors MUST span C².
```

## Canonical paths and navigation policy

The wiki distinguishes **paths through content** from sidebar/domain grouping. Existing sidebar grouping is classification only and must not be redesigned merely to repair paths.

### Learning path

`overview-learning-path.md` is the canonical, prerequisite-first **learning path**. Its ordered numbered concept links define the recommended learner sequence and are the sole authority for an unlabeled reader **Previous** or **Next** control. A learning path is a curated total order: it must respect declared prerequisites, but it may order otherwise independent concepts for clarity, reinforcement, examples, and gradual complexity.

### Prerequisite path

Concept `parents` metadata and `prerequisite-for` relationships define the **prerequisite path**: a partial dependency order answering “what must be understood before this?” A prerequisite edge is a strong claim that the target relies on the source’s definitions, operations, or distinctions. Because this graph can branch and merge, it must not alone power an unlabeled Previous/Next control.

### Other paths

Typed relationships define labeled **exploration paths**—for example `uses`, `illustrates`, `derives-from`, `limitation`, `contrasts-with`, and `related-to`. Definition popovers and `Learn more` links define a **recall path**. These must be visibly labeled by their purpose and are not default lesson navigation.

Lexical/index order, generated artifact-array order, filesystem order, package order, and search-result order are technical/retrieval orders. They MUST NOT be presented as curriculum or unlabeled learning navigation.

### Path registry and future path types

The current only user-facing sequential path is `learning`. Future paths may be added only when they have:

1. a stable machine-readable identifier;
2. a canonical source document or deterministic generator;
3. a declared purpose and audience;
4. explicit ordering semantics (total, partial, or labeled traversal);
5. validation requirements; and
6. user-facing controls labeled with the path’s purpose.

Do not introduce a future path merely because a graph relation exists. Record it in `.agents/references-canonical-flows.md` and add an issue with acceptance criteria before implementation.

## Explorer and package workflow
Run `make index validate` after edits; test the explorer; before delivery run `make clean index validate package`; keep tooling standard-library-only. The explorer must surface definition links as hoverable and tappable term affordances, expose the definition text accessibly without hover, and retain a navigable destination for every term that has a deeper concept.

### Definition interaction visual standard — MUST preserve
The approved visual reference is the version-6 treatment visible on the **Hilbert Spaces** and **Dirac Notation** reader pages. This is a mandatory baseline for every inline definition across the explorer and **must not be changed without explicit human sign-off**. The required treatment is:

- definition terms are visibly embedded in the reader prose, not replaced by a separate index, chip, panel, or generic body text;
- pale warm-cream rounded inline highlight;
- dark-brown bold term text with an orange dotted underline;
- no inline info icon, alternate definition marker, or Definitions-mode visual override;
- the same comfortable inline spacing as the approved reference;
- a large white rounded popover with soft shadow, a small outlined cream `Definition` pill, dark-navy title, slate explanatory text, and solid indigo `Learn more` button with arrow;
- hover, keyboard focus, and click/tap all open the same interaction; `Learn more` remains visible and navigable, or explicitly disabled with a clear unavailable-destination message.
- **Definition-popover mathematics MUST render as mathematics.** Popover text uses the same trusted inline-math pipeline as reader prose; raw TeX delimiters or commands (for example `\\(`, `\\sqrt`, or `\\langle`) visible in a popover are a release-blocking rendering defect. The Norm definition, including \(\|\psi\|=\sqrt{\langle\psi|\psi\rangle}\), is the mandatory regression fixture.

Definition indexes, counts, and search may supplement this treatment but may never replace it. Any request to revise this appearance requires explicit human sign-off before implementation, a rendered before/after comparison against the approved Hilbert/Dirac reference, and a recorded charter change.

### Definition annotation syntax and naming — MUST preserve

Inline definition markup is a semantic annotation, not generic display syntax:

```text
{{def:<definition-id>|<surface-form>}}
```

- `<definition-id>` **must exactly equal** the stable canonical ID of an existing definition node, without the `def-` filename prefix. For example, the definition file `definitions/def-completeness.md` uses `completeness`, yielding `{{def:completeness|completeness}}`.
- `<surface-form>` is the exact reader-visible word or phrase being explained. It may use capitalization, plurality, or an inflected form when that is both grammatically natural and semantically exact.
- The surface form must name the **same concept** as the definition ID. Do not use an adjective or nearby word merely because it is a textual match when it changes the concept being introduced. For example, annotate `completeness` for the definition `completeness`; do not annotate `complete` as if it were the noun concept.
- The visual label is reader-facing and should be understandable as the concept named by the popover title. If this is not possible without awkward prose, rewrite the sentence, introduce the noun phrase explicitly, or use a more specific definition; do not force an incorrect surface form.
- The annotation token replaces a legacy definition link only. It is not an ordinary Markdown link and must not be applied to external links, concept links, citations, headings, equations, code, warning/caveat blocks, or reference labels.
- For a page-level schema, `term` is the intended surface form and `definition_id` is the canonical definition ID. The transform annotates the first eligible occurrence only. Explicit `{{def:...|...}}` markup is an override for an intentionally chosen ambiguous occurrence and takes precedence over automatic placement.
- Definition IDs are kebab-case, stable, and singular by default. Rename/split a definition through the redirect/version policy; do not silently retarget existing annotation IDs.
- Every annotation change requires transform tests to assert: target definition exists; exactly one intended first-use annotation is inserted; visible prose is retained; and no annotation is inserted into protected syntax.

## Change, redirect, and version policy
Record material charter decisions here. For renamed or split concepts, add redirects and update links/indexes. Record a dated change note for material releases.

## Definition of done
The mathematics foundation is complete and reviewed before canonical gravity begins. The physics curriculum is then complete, self-contained, sourced, and validated before the optional Advaita layer begins. The optional layer is distinguishable and linked only through bounded comparisons; examples, indexes, links, provenance, redirects, and explorer work; `make clean index validate package` succeeds.
