# Explorer v12 Snapshot

## Purpose

Preserved immediately before repairing the full-reader annotation rollout. The user reports two regressions:

1. Mathematics display is broken.
2. The visual style no longer matches the approved version-6 Hilbert/Dirac reference.

## Snapshot

- Saved file: `quantum-time-wiki-explorer-current.json`
- SHA-256: `1e0ed51358c19c1cd5f97d5d28e11f2f3a90a43d908af73be8ff4995812a7142`

## Repair requirements

- Preserve the full canonical content and annotation approach.
- Add a deterministic math-block parser for inline `\(...\)` and display `\[...\]` mathematics.
- Render math as dedicated visual blocks, preserving equation spacing, line breaks, matrices, fractions, and operators. Do not display raw backslashes, delimiters, or escape sequences as prose.
- Restore the approved version-6 visual style exactly for concept layout and definition terms/popovers; do not permit full-reader conversion to introduce a different typography, spacing, or definition style.
- Do not publish an unverified visual restyle.
