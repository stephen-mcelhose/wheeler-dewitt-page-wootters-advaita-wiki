# Canonical Flows and Orders

**Status:** Governing reference for navigation, sequencing, and release validation.

## Purpose

The wiki has more than one legitimate way to traverse its content. Each flow has a distinct purpose. A user-facing control must name the flow it follows and must not silently substitute a technical sort order for a curricular or graph meaning.

## Path registry

| Path ID | User-facing status | Purpose | Canonical source | Ordering semantics |
|---|---|---|---|---|
| `learning` | Active | Recommended prerequisite-first study route | `overview-learning-path.md` | Curated total order |
| `prerequisite` | Available as labeled dependency traversal only | Identify required conceptual dependencies | `parents` metadata and `prerequisite-for` relationships | Partial order / directed graph |
| `exploration` | Available as labeled relationship traversal only | Discover connected concepts/examples by relationship meaning | typed `relationships` metadata | Labeled graph traversal |
| `recall` | Available as local support only | Explain local vocabulary and link to deeper treatment | definitions and inline annotations | Local contextual links |

Only `learning` is currently a user-facing sequential reader path. Future path IDs require the charter’s path-registry conditions and an approved issue before implementation.

## 1. Learning flow — canonical total order for guided study

**Canonical source:** `overview-learning-path.md`.

This is the authoritative ordered curriculum for a learner using prerequisite-first study. Its ordered numbered lists define the only canonical meaning of user-facing **Previous** and **Next** learning navigation.

The current rigorous learning flow is:

1. Mathematical Foundations, in the displayed numbered order.
2. Canonical Gravity and the Problems of Time, in the displayed numbered order.
3. Page–Wootters Relational Time, in the displayed numbered order.
4. Optional Philosophy, in the displayed numbered order and only after the rigorous path.

A learning-flow navigation control MUST derive its sequence from this file or from a generated artifact that is deterministically verified against this file.

## Learning-order generation and release gate

`.agents/generate_learning_order.py` is the deterministic generator for the active `learning` path. It parses numbered local concept links, resolves stable canonical IDs, rejects duplicate, unresolved, missing, malformed, or empty sequences, and verifies declared prerequisites precede each listed concept. It emits `.agents/generated/learning-order.json`.

Every explorer candidate with unlabeled Previous/Next controls must pass `.agents/validate_learning_navigation.py <candidate>`. The validator requires artifact `learningOrder` to exactly equal the parsed source order and rejects artifact-array positional navigation. A concept outside `learningOrder` has no unlabeled Previous/Next control. After publication, the release handoff must record the actual visible results for every changed learning-flow relation; candidate/live equality alone is insufficient.

## 2. Prerequisite graph flow — canonical partial order

**Canonical sources:** concept `parents` metadata and `prerequisite-for` relationships.

This graph answers: “What must be understood before this concept?” It is a directed acyclic dependency structure where valid traversals can branch or merge. It is not a single total order and therefore MUST NOT alone drive an unlabeled Previous/Next button.

The learning flow is one curated linearization of this prerequisite graph, with visible pedagogical checkpoints and bounded scope.

## 3. Taxonomy/domain grouping — existing classification, out of scope for path repair

**Canonical sources:** source directory/domain classification:

- `mathematics/`
- `physics/`
- `page-wootters/`
- `philosophy/`

This answers: “Which subject domain contains this node?” The explorer already groups nodes by these domains. **Do not redesign, regenerate, or otherwise treat sidebar grouping as part of the current navigation repair.** It is recorded here only to distinguish grouping from paths.

The philosophy domain is optional, draft, and non-evidential. It is not part of the rigorous prerequisite path.

## 4. Relationship/exploration paths — canonical typed links, not sequence

**Canonical source:** typed `relationships` metadata.

This flow supports exploration by meanings such as `uses`, `illustrates`, `derives-from`, `limitation`, `contrasts-with`, and `related-to`. It answers: “What is connected to this node, and how?” It may cross between nearby concepts, examples, and definitions but does not supply a default next lesson.

## 5. Definition/recall flow — canonical local support, not sequence

**Canonical sources:** definition nodes and inline definition annotations.

Definitions provide short local explanations and a `Learn more` destination. They support recall while reading a concept. They are not a required sequence and must not replace essential prerequisite explanations in canonical concept bodies.

## Non-canonical technical orders

The following orders are implementation details and MUST NOT be presented as learning or conceptual navigation:

1. **Lexicographic/index order** — `build_index.py` sorts nodes by title to create indexes and `viewer/wiki-data.json`. This is for stable generated listing/index output only.
2. **Artifact-array order** — the generated `concepts` array may reflect lexical or build order. It must not drive user-facing Previous/Next learning controls.
3. **Filesystem/package order** — file enumeration and archive ordering are technical reproducibility details, not content sequence.
4. **Search-result order** — relevance/filter order is a retrieval aid, not curriculum order.

## Explorer-control contract

- A control labelled **Previous** or **Next** without another qualifier means **Learning flow** and follows `overview-learning-path.md`.
- A control navigating graph links must name the relationship, for example **Prerequisite**, **Illustrates**, or **Related concept**.
- Existing sidebar taxonomy/domain groups are out of scope for this repair. They must not be changed merely to repair reader paths.
- Search may order by matching/relevance but must not alter learning navigation.

## Current known defect

The current explorer reader uses artifact-array positional navigation. This is non-canonical technical order and violates the Explorer-control contract. See `.agents/handoffs/2026-11-07-navigation-order-incident.md`.
