# UNIT C Proposal Manifest — Composite Systems plus Measurements and Conditional States

**Package status:** proposal only; no canonical, index, Explorer, learning-path, notation-reference, or process file was edited. All proposed nodes are `draft` pending mathematical/quantum-information review and later user review. The implementation plan and required corrections are recorded in [`REVIEW.md`](REVIEW.md); it supersedes any conflicting guidance below.

## Intended canonical targets

| Proposal file | Intended canonical target | Action |
|---|---|---|
| `mathematics/composite-systems.md` | `mathematics/composite-systems.md` | Material concept repair and example link |
| `mathematics/conditional-states.md` | `mathematics/conditional-states.md` | Material concept repair and example link |
| `examples/example-composite-bell-state-partial-trace.md` | `examples/example-composite-bell-state-partial-trace.md` | New dedicated composite-systems example |
| `examples/example-clock-effect-conditional-state.md` | `examples/example-clock-effect-conditional-state.md` | New dedicated conditional-states example |
| `definitions/def-reduced-state.md` | `definitions/def-reduced-state.md` | New definition |
| `definitions/def-conditional-state.md` | `definitions/def-conditional-state.md` | New definition |
| `definitions/def-entanglement.md` | `definitions/def-entanglement.md` | New definition, explicitly scoped to pure bipartite states |
| `definitions/def-tensor-product.md` | `definitions/def-tensor-product.md` | Repair malformed math and clarify simple vs general tensors |
| `definitions/def-density-operator.md` | `definitions/def-density-operator.md` | Repair malformed math and add positive-semidefinite language |
| `definitions/def-partial-trace.md` | `definitions/def-partial-trace.md` | Repair malformed math and make the unconditioned boundary explicit |
| `definitions/def-effect.md` | `definitions/def-effect.md` | Repair: statistics only, not update |
| `definitions/def-povm.md` | `definitions/def-povm.md` | Repair: probabilities only, not update |
| `definitions/def-quantum-instrument.md` | `definitions/def-quantum-instrument.md` | Repair CP/TNI/TP-aggregate vocabulary |

## Direct prerequisites and graph recommendations

- `composite-systems` parents remain `dirac-notation` and `operators-and-domains`; its relationship `prerequisite-for → conditional-states` remains appropriate.
- `conditional-states` parents remain `composite-systems` and `born-rule-and-quantum-probability`.
- Add `illustrates → example-composite-bell-state-partial-trace` from `composite-systems`, and `illustrates → example-clock-effect-conditional-state` from `conditional-states`.
- The two new examples each carry a reciprocal `illustrates` relationship to their target concept.
- New definition links are recall support only: reduced state and entanglement from Composite Systems; conditional state, effect, POVM, and quantum instrument from Measurements and Conditional States.
- No learning-path change is proposed. Before integration is complete, perform the notation-coverage audit in `REVIEW.md`; add/revise global entries for every retained conditional-operator, effect/POVM, instrument/trace-dual, and identity-map notation family, as well as local first-use readings.

## Dependencies and review gates

1. Acceptance of the Born-rule unit is a genuine prerequisite. Unit B is not a mathematical blocker for Unit C’s stated finite-dimensional models, though it remains earlier in the learning path and is needed before later unbounded/ideal-clock material. Any change to the active delegation plan’s conservative Unit-B scheduling gate remains a central-orchestration decision.
2. **Blocking correction:** under a clock-local instrument with associated effect \(E_t=\mathcal I_t^*(I_C)\), its postselected **system marginal** equals the effect-conditioned system state after tracing out the clock. The proposal must not claim the two system constructions generally differ. The effect does not, however, determine the postselected joint state, residual clock state, or sequential clock statistics. See `REVIEW.md`.
3. Obtain independent quantum-information/mathematical review of: partial-trace calculation; pure-state entanglement scope; positivity and normalization of effect conditioning; effect/POVM/instrument distinction; the clock-local marginal equality; CP/TNI maps and TP aggregate; and the special status of the Lüders instrument.
4. Main-agent integration must reconcile exact metadata schema, definition annotation transform behavior, shared definition IDs, links to the existing finite-clock and downstream Page--Wootters files, sources, notation coverage, and Go code/tests.
5. Run annotation-transform tests, index build, graph validation, Go tests, and render inspection only after reconciliation. This worker did not run them because the package intentionally does not alter canonical source.

## Explicit non-targets

No claim is made about continuous ideal clocks, a unique factorization in constrained gravity, Page--Wootters dynamics, a physical collapse mechanism, Bell nonlocality, signalling, or mixed-state entanglement classification.
