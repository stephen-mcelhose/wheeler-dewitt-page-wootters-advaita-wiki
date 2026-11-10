# Explorer v11 Snapshot

## Purpose

This directory preserves the exact explorer artifact state before the annotation-based reader implementation is attempted. It is a rollback/reference snapshot, not an approved UI baseline.

## Snapshot

- Source artifact: `Quantum Time Wiki Explorer`
- Saved file: `quantum-time-wiki-explorer-current.json`
- SHA-256: `41df87a11db5b3dc0771f0f18eb2cb96dd919c5e9a09b2c6338fe02d6b55e3fe`
- Reason for snapshot: the current explorer has drifted from the approved version-6 reader content and styling. Preserve it before replacing its abbreviated artifact-specific reader prose.

## Proposed reader annotation syntax

Use an explicit inline definition annotation in canonical reader content:

```text
{{def:definition-id|Visible term}}
```

Examples:

```text
A {{def:ket|ket}} is a vector in a Hilbert space.
The {{def:resolution-of-identity|resolution of the identity}} gives a basis expansion.
```

## Rendering contract

1. The reader renders `Visible term` in the approved version-6 inline definition treatment.
2. `definition-id` resolves against the canonical definition dataset.
3. Hover, keyboard focus, click, and tap open the same definition popover.
4. The popover provides a visible `Learn more` route to the linked deeper concept.
5. If the definition or target is missing, the visible prose remains intact and the UI shows a clear, non-breaking fallback.
6. Canonical concept prose must remain complete; annotations enhance terms and must never be used as a reason to replace prose with an abbreviated artifact summary.

## Non-goals

- This annotation is not yet a charter-wide mandatory content format.
- The approved visual definition style remains governed by the existing charter standard.
- No mathematical or philosophical content is changed by adopting this annotation.
