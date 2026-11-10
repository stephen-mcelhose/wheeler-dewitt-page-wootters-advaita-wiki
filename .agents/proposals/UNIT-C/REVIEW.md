# Unit C Planning Review — User-Review-Ready Implementation Plan

**Scope:** planning/review only. This report evaluates the proposal package against the current canonical concepts, definitions, examples, learning path, charter, active delegation plan, maintainer skill, notation-coverage contract, and example-comment reference. It does **not** authorize copying proposal files into canonical locations, rebuilding indexes, changing Explorer behavior, or publishing.

**Decision:** retain Unit C as one quantum-information implementation unit, but revise the conditional-measurement formulation before any integration. The two dedicated examples are sound teaching shapes after the corrections and completion gates below. All proposed canonical nodes remain `draft` until independent quantum-information review and human review.

## 1. Current canonical gap and proposed outcome

The canonical concepts are skeletal:

- `mathematics/composite-systems.md` states the tensor-product and reduced-state ideas but has no self-contained worked example, no product-basis convention, no usable product-versus-entangled distinction, and no explicit graph link to an example.
- `mathematics/conditional-states.md` correctly says probability differs from update, but its single formula uses an unqualified `\rho_{S|t}` while also saying an appropriate measurement model is needed. That wording collapses two distinct questions.
- The existing `examples/example-finite-clock-conditional-state.md` is a useful downstream Page--Wootters/finite-clock illustration, but it is not a replacement for the required dedicated conditional-states example: it lacks local measurement-model setup, metadata-rich scope, effect/instrument distinction, and programmer-facing finite checks.
- Existing reusable definitions for tensor product, density operator, partial trace, and effect contain broken TeX source (for example `\rho`/`\rangle` has lost its leading backslash). The proposal’s definition repairs are necessary rather than cosmetic.

The implementation should produce exactly these two dedicated, self-contained examples:

1. **Composite Quantum Systems:** a two-qubit Bell-state calculation with declared `C:S` product-basis order, density matrix, partial trace, product-state contrast, and explicit unconditioned reduced-state conclusion.
2. **Measurements and Conditional States:** the same finite correlated state used independently, with a sharp clock effect, outcome probability, unnormalized and normalized effect-conditioned system operator, reduced-state comparison, and an explicitly declared Lüders instrument as a special update model.

Intentional repetition of the Bell correlation is required for self-containment and is consistent with the charter; it must not make the conditional example depend on the composite example for essential calculations.

## 2. Required mathematical correction before integration (blocking)

The proposal currently says that effect conditioning and instrument-selective conditioning of the **system after a clock-local instrument and partial trace over the clock** “need not agree for a general instrument.” That statement is false under the formula it gives.

For a clock-local outcome map `\mathcal I_t` and its effect `E_t=\mathcal I_t^*(I_C)`, the unnormalized system operator obeys

\[
\operatorname{Tr}_C[(\mathcal I_t\otimes\mathrm{id}_S)(\rho_{CS})]
=
\operatorname{Tr}_C[(E_t\otimes I_S)\rho_{CS}].
\]

Thus, after discarding the clock, the normalized system state is fixed by the effect and is the same for every clock-local instrument realizing that effect (when `p(t)>0`). This follows by testing against arbitrary system observables and using the trace-dual definition. The proposed formula is a valid positive operator in this finite setting; equivalently, it can be displayed in manifestly positive form as

\[
\operatorname{Tr}_C[(\sqrt{E_t}\otimes I_S)\rho_{CS}(\sqrt{E_t}\otimes I_S)],
\]

with the equality stated rather than presumed.

**Required repair:**

- Keep the four-way distinction below, but change the claimed distinction between `\rho^{\mathrm{eff}}_{S|t}` and `\rho^{\mathrm{inst}}_{S|t}`.
- State that the effect does **not** determine the selected **joint clock--system post-measurement state**, the residual clock state, a physical disturbance narrative, or a later sequential statistic involving the clock. An instrument supplies that information.
- State that the two displayed **reduced system** constructions agree for a clock-local instrument associated with `E_t`; their agreement does not license inferring the joint update, nor does it cover instruments that act jointly on clock and system.
- Retain the Lüders section as a special sharp-projective joint-update model. In the Bell example it gives the same conditional system state, but the extra assumption is needed to state the selected joint output.
- Do not introduce `\rho^{\mathrm{inst}}_{S|t}` as a competing system-state construction unless the page explicitly says it equals `\rho^{\mathrm{eff}}_{S|t}` under the declared clock-local assumptions. Prefer one `\rho^{\mathrm{cond}}_{S|t;E}` notation for the system state and reserve instrument notation for the joint selective output.

Independent review must explicitly verify this correction and terminology before any canonical edit.

## 3. Required distinctions in canonical prose and examples

The implementation must visibly keep these objects separate at first essential use:

| Object | Finite-dimensional expression | Meaning and boundary |
|---|---|---|
| Outcome probability | `p(t)=Tr_{CS}[(E_t\otimes I_S)\rho_{CS}]` | Scalar in `[0,1]`; an effect/POVM supplies statistics, not a state update. |
| Unnormalized effect-conditioned system operator | `\widetilde\rho_{S|t}=Tr_C[(E_t\otimes I_S)\rho_{CS}]` | Positive operator of trace `p(t)`; equivalently use the sandwiched-`\sqrt{E_t}` form. It is not normalized and is not a probability. |
| Normalized conditional system state | `\rho_{S|t}=\widetilde\rho_{S|t}/p(t)` only when `p(t)>0` | State conditioned on the stated effect/outcome. Undefined by this formula when `p(t)=0`. It is not, without further data, a joint post-measurement state. |
| Reduced state | `\rho_S=Tr_C(\rho_{CS})` | Unconditioned system state when the clock is ignored; for a discrete POVM, `\rho_S=\sum_t p(t)\rho_{S|t}`. |
| Selective update | `\rho'_{CS|t}=(\mathcal I_t\otimes id_S)(\rho_{CS})/p(t)` | Joint post-outcome state determined only after declaring a clock-local instrument. Its system marginal equals the effect-conditioned state for the associated effect, but its joint/clock information is not determined by that effect. |

The conditional concept must say whether “conditional state” means the finite operational effect-conditioned **system** state in this unit. Later Page--Wootters pages may use idealized conditional vectors only after stating their additional pure-state, clock representation, domain, and normalization assumptions. The concepts must not present outcome labels as an external time parameter or a continuous time ket.

## 4. Concrete implementation sequence

### A. Composite Quantum Systems

1. Replace the canonical concept with the reconciled proposal, preserving stable ID and `draft` review status. Limit the main development to finite-dimensional `\mathcal H_C\otimes\mathcal H_S`; state explicitly that factor order and a chosen product-basis order are representational conventions.
2. Define product pure states and entanglement only relative to a specified bipartition. State that the rank-one coefficient-matrix criterion is a finite-dimensional **pure bipartite** test, not a mixed-state separability criterion.
3. Give the partial-trace characterization through system-only observable statistics, then state in body text—not only a definition popup—that a reduced state discards/ignores `C` and selects no outcome.
4. Add `definitions/def-reduced-state.md` and `definitions/def-entanglement.md`; repair/reconcile `def-tensor-product.md`, `def-density-operator.md`, and `def-partial-trace.md`. Definition bodies remain one or two sentences, with essential caveats retained in the concept.
5. Integrate `example-composite-bell-state-partial-trace.md`, with its `C,S` labels, no personal labels, explicit basis order, Bell density matrix, partial-trace calculation, product contrast, and non-conclusion. Its existing final “reduced is not conditional” calculation may remain as a short signpost, but must direct the complete measurement distinction to the conditional-states example.
6. Add reciprocal `illustrates` links between concept and example. Use stable definition IDs and first-use annotation metadata; do not keep legacy Markdown links alongside `{{def:...|...}}` at the same first use.

### B. Measurements and Conditional States

1. Replace the canonical concept with the corrected finite-dimensional account: effect and discrete POVM statistics; positive-probability normalization gate; unconditioned reduced state; and the instrument/joint-update boundary.
2. Reconcile/repair `def-effect.md`, `def-povm.md`, and `def-quantum-instrument.md`; add `def-conditional-state.md`. Definitions must make the statistics-versus-update distinction in a sentence, while the concept supplies equations and qualifications.
3. Integrate `example-clock-effect-conditional-state.md` only after applying the correction in Section 2. It must independently introduce its two-qubit state, basis/factor convention, effect, probability calculation, unnormalized operator, `p(0)>0` normalization, reduced-state comparison, and declared Lüders joint update.
4. In that example, show `p(0)=1/2`, `\widetilde\rho_{S|0}=|0\rangle\langle0|/2`, `\rho_{S|0}=|0\rangle\langle0|`, and `\rho_S=I_S/2`. State that the Lüders assumption determines `\rho'_{CS|0}=|00\rangle\langle00|`, while the system marginal agrees with the effect-conditioned state for the stated local instrument.
5. Add reciprocal `illustrates` links and retain `prerequisite-for → page-wootters-mechanism`. Reconcile downstream terminology in `clock-povms.md`, `conditional-page-wootters-state.md`, and the existing finite-clock example in the same integration change; at minimum, they must not retain a false contrast between local-instrument and effect-conditioned **system** marginals.
6. Retain `example-finite-clock-conditional-state.md` as a downstream finite-clock illustration (`finite-clock-model` remains its primary topic), but revise its relationship/wording only if needed to point readers to the dedicated conditional-measurement example for measurement semantics. Do not replace it with the new dedicated example.

## 5. Finite Go helpers and predicates

Code is warranted because these two examples use finite arrays to expose factor indices, partial trace, conditioning normalization, and the limited rank criterion. Code and its tests must be authored/reviewed as one behavioral unit.

Required helper/predicate set (names may vary only if their scope remains equally explicit):

- `partialTraceOverClock2D(JointDensity2D) SystemDensity2D`: implement `(Tr_C rho)[i][j]=Σ_c rho[c][i][c][j]` using the declared `C,S` index order.
- `isRankOneCoefficientMatrix2D(matrix, tolerance) bool` or a clearly named equivalent: use determinant/matrix rank only for the declared finite pure two-factor coefficient model; its comment must say it is not a mixed-state entanglement test.
- `hasStrictlyPositiveFiniteProbability(p, tolerance) bool`: distinguish a numerically positive finite normalization denominator from zero/negative/non-finite supplied data. The pedagogical prose must still state the exact mathematical condition `p(t)>0`.
- `normalizeConditionalSystem2D(unnormalized, p) (SystemDensity2D, error)`: reject nonpositive/non-finite denominators and, if it accepts a tolerance, explain that the tolerance is for floating-point checking rather than a modification of the exact condition.
- At least one honest finite-data predicate, preferably `isDensityOperator2D(rho, tolerance) bool`, checking approximate Hermiticity, trace one, and 2-by-2 positive semidefiniteness. It must say it validates supplied finite coordinates, not a general density-operator theorem or a measurement implementation.

Do **not** write a Boolean predicate that claims to determine “is entangled” for arbitrary density operators, instruments, continuous outcomes, or gravitational factorization. Do not write code that “proves” the instrument/effect equality; calculate the finite example and explain the general finite-dimensional relation in prose with source/review support.

Every new code block must follow the comment standard: `Given:` for typed/basis/precondition facts, `Model scope:` for `C²⊗C²`, `Convention:`/`Representation:` for index order/storage, `Illustration:` for the Bell values, and direct mathematical limitations. The current proposal needs added `Model scope:` comments in both Go blocks and must flag its new measurement-comment pattern for review because no existing golden example covers instruments.

## 6. Definitions, notation, graph, and source checklist

### Definitions and annotation

- Proposed reusable IDs: `reduced-state`, `conditional-state`, `entanglement`; retain the six existing IDs (`tensor-product`, `density-operator`, `partial-trace`, `effect`, `povm`, `quantum-instrument`). Verify every target exists before annotation transform.
- Repair malformed TeX in canonical definition bodies and inspect rendered definition popovers; raw TeX is a release-blocking defect only at later reader-release time, not a reason to publish now.
- Use `{{def:<stable-id>|<exact surface form>}}` only in eligible prose. The proposed composite metadata currently names `entangled` for the `entanglement` definition; rewrite first-use prose to introduce the noun **entanglement** so the surface form and definition ID are semantically exact.

### Notation coverage

Local prose must read/parse: `\mathcal H_C\otimes\mathcal H_S`, product-ket order, `\rho_{CS}`, `I_C/I_S`, `\operatorname{Tr}_C` versus `\operatorname{Tr}_{CS}`, `E_t`, `0\le E_t\le I`, `\widetilde\rho_{S|t}`, `p(t)>0`, `\mathcal I_t`, `\mathcal I_t^*`, and `\mathrm{id}_S`.

The current global notation reference already covers `\otimes`, `\rho_{CS}`, `Tr_C`, and a basic `\rho_{S|t}`. Before implementation completion, add/revise global entries for the tilde/unnormalized conditional operator, effect/POVM inequality and summation, instrument and trace-dual notation, and `\mathrm{id}_S`, **if those expressions remain in canonical prose**. Include rendered form, spoken reading, parsing, minimal meaning, first full concept, and scope. Do not make the guide a learning-path prerequisite.

### Relationships and sources

- Preserve learning-path positions 11 and 12; do not change path order in this unit.
- Add the two concept/example `illustrates` pairs; preserve `composite-systems → conditional-states` as `prerequisite-for` and both concepts’ downstream Page--Wootters links.
- Use only controlled relationship types. Definition links are recall support, not prerequisites.
- Verify Nielsen & Chuang against the exact finite density/partial-trace/POVM claims and Ozawa against the instrument/update claims; retain accessible DOI URLs and persistent IDs. Independent review must flag any terminology that needs a more focused measurement-theory source.

## 7. Dependencies and gates

### Genuine prerequisites

- **Required before implementation/user review:** the Born-rule unit must be accepted enough that probabilities, projectors, trace, and finite operator notation are available to the learner.
- **Required within Unit C:** Composite Quantum Systems precedes Measurements and Conditional States.
- **Not a genuine mathematical blocker for finite Unit C:** Unit B’s unbounded-operator/domain material. All operations in the proposed `2×2` models are finite-dimensional and everywhere defined. Unit B remains earlier in the approved learning-path order and is a genuine later prerequisite for idealized/generalized Page--Wootters clock discussions, but Unit C implementation need not wait for Unit B merely to state its finite model.

This differs from the active delegation plan’s conservative “Unit B has settled” integration gate. The implementation owner should amend that gate only through the central orchestration process; until then, treat it as a scheduling policy rather than silently claiming a mathematical dependency.

### Required review and acceptance gates

1. **Pre-integration reconciliation:** apply the correction in Section 2, resolve exact metadata/annotation schema, inspect all existing/downstream references named above, and prepare code tests with the code.
2. **Independent quantum-information/theoretical-measurement review:** verify Bell partial trace; pure bipartite rank scope; positivity/normalization and zero-probability boundary; effect versus POVM versus instrument language; the clock-local marginal equality; Lüders scope; sources; and downstream Page--Wootters terminology.
3. **Author remediation:** record each review finding by severity, exact file/claim, correction, and verification. Keep all changed nodes `draft` unless an independent AI review is actually recorded; human approval alone is required for `approved`.
4. **Structural/reader candidate gate after canonical integration:** annotation-transform tests; `make index validate`; graph/link validation; Go tests; rendered math/definition-popover inspection; and explicit notation-coverage audit. Do not rebuild indexes or publish as part of this planning phase.
5. **User-review gate:** present the two concepts and their two dedicated examples together, plus the independent-review findings and the explicit reduced-state/probability/conditional-state/selective-update table. Only then seek acceptance.

## 8. Non-goals and remaining risks

Unit C does not establish mixed-state entanglement classification, Bell nonlocality/signalling, a physical collapse theory, a continuous ideal clock, Page--Wootters dynamics, a unique clock/system split, or a factorization of constrained gravity. It must not imply any of these.

**Current blockers:**

1. The false “general instrument system state need not agree” claim must be repaired as specified before integration.
2. Independent quantum-information/measurement review has not occurred.
3. The active plan’s Unit-B scheduling gate needs a central-orchestration decision if the recommended genuine-dependency interpretation is adopted.

No canonical source, generated index, Explorer configuration, or publication state was changed during this review.
