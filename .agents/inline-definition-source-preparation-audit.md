# Conservative all-page inline-definition source-preparation audit

**Date:** 2025-02-14  
**Scope:** Canonical Markdown source and source-only transform tests. The React explorer artifact was not modified or published.

## Result

- **Concept sources examined:** 34
- **Qualifying concept pages with `inline_definitions`:** 32
- **Declared schema targets / terms:** 79
- **Transform result:** 79 annotation tokens; 0 unmatched schemas; 0 protected-syntax placements.
- **Review statuses:** Preserved verbatim. All materially edited `draft` pages remain `draft`; no status was promoted or otherwise changed.

### Applied schemas

| Section | Pages | Terms |
| --- | ---: | ---: |
| `mathematics/` | 14 | 48 |
| `physics/` | 10 | 15 |
| `page-wootters/` | 6 | 8 |
| `philosophy/` | 2 | 8 |
| **Total** | **32** | **79** |

The exact `(definition_id, surface form)` pairs are stored in each page frontmatter and are programmatically checked by `scripts/test_annotation_transform.py`.

## Deferred and skipped pages

- **Resolved:** `physics/spacetime-foliations-and-general-relativity-primer.md`. Its first `foliation` occurrence uses the explicit override `**{{def:foliation|foliation}}**`, which preserves bold emphasis while replacing the legacy definition link with definition semantics. The annotation transform regression suite asserts that this bold-wrapped explicit token is preserved structurally.
- **No schema:** `philosophy/advaita-orientation.md` and `philosophy/maya.md`. The Advaita terms **Brahman**, **māyā**, and **avidyā** have no governed definition nodes and remain unannotated.
- **Excluded semantic mismatches (not mapped):**
  - `inner-product space` → `inner-product`
  - `anomaly freedom` → `anomaly`
  - `kinematical Hilbert space` / `physical state space` → state definitions
  - `conjugate momentum` → `phase-space`
  - `generalized vectors` → `generalized-eigenvector`

## Source repair

- `page-wootters/conditional-page-wootters-state.md`: repaired the malformed nested Markdown construction around the clock/system setup. The visible prose now contains the exact phrase `clock/system factorization`, with explicit `{{def:clock-system-factorization|clock/system factorization}}` markup. The repair leaves the composite-system relationship in prose, is semantically exact, and does not alter the page's `draft` status.

## Test and validation record

Passed:

```bash
cd /app/workspace/wheeler-dewitt-page-wootters-advaita-wiki
python3 scripts/test_annotation_transform.py
# Ran 4 tests; OK

python3 .agents/skills/doc-manager/scripts/build_index.py .
# Indexed 103 nodes.
python3 .agents/skills/doc-manager/scripts/validate.py .
# Validation passed: 103 graph nodes.
```

The all-page test parses every concept source and verifies that each schema ID names a real definition (normalizing definition-node `def-` file IDs); no page repeats a definition ID; the transform has no unmatched schemas; exactly one annotation token exists per declared target after explicit overrides; and no tokens occur in headings, warnings/blockquote lines, display math, inline math, code, or Markdown links. It also retains the five-page pilot regression set.

`make index validate` was attempted but `make` is not installed in this environment; the equivalent required doc-manager commands above succeeded.

## Files changed

- 32 concept Markdown sources under `mathematics/`, `physics/`, `page-wootters/`, and `philosophy/`
- `scripts/annotation_transform.py` (scope wording only)
- `scripts/test_annotation_transform.py` (all-page schema gate, retained pilot regressions, and bold-wrapped explicit-annotation regression)
- `.agents/inline-definition-source-preparation-audit.md` (this report)

No files under `viewer/` and no React explorer artifact were changed or published.
