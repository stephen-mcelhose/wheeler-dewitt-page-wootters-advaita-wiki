# Notation Coverage Contract

Use this reference whenever adding or materially revising canonical prose, equations, examples, definitions, code comments, or reader rendering.

## Goal

Every notation element used in the wiki must be readable by the intended learner at the point it appears. A learner must not be expected to infer how to pronounce or parse a symbol merely because it is conventional to an expert.

This is a coverage requirement, not an instruction to repeat a full notation lecture on every page.

## Two layers of coverage

### 1. Global notation primer and register

The canonical **Mathematical Notation and Formula Reading** prerequisite must cover every recurring notation family used across the rigorous curriculum. It must provide:

- rendered form;
- spoken reading;
- structural reading or parsing rule;
- minimal meaning;
- first concept where the notation gains its full technical meaning;
- scope notes where a notation is overloaded.

The global register supports recall and consistent pronunciation. It must be kept current as the curriculum grows.

### 2. Local first-use coverage

Every concept and worked example must locally introduce or restate notation that is essential to understanding its current argument, derivation, model, or code. A link or popover may support recall, but cannot hide an essential assumption or reading step.

A reader who followed declared prerequisites should be able to parse each displayed formula. If that is not true, the maintainer must add one of:

- a missing primer/register entry;
- a prerequisite concept or definition;
- a local notation sentence or reading cue;
- a worked reading example;
- an explicit scope/convention statement.

## Coverage inventory

At minimum, maintain coverage for these notation families as they appear in the curriculum:

1. **Formula structure:** equality, plus/minus, parentheses, brackets, commas, colon, semicolon, implication, equivalence, mapping, quantifiers, set membership, set-builder notation.
2. **Numbers and scalars:** natural, integer, real, rational, and complex-number symbols; imaginary unit; absolute value; complex conjugation; real/imaginary parts.
3. **Coordinates and vectors:** subscripts, superscripts, column/row notation, transpose, matrices, indices, summation, products, norms, distances, limits, convergence.
4. **Dirac and Hilbert notation:** ket, bra, bracket, outer product, identity, basis labels, Kronecker delta, projectors, rays, tensor product, partial trace/density notation when introduced.
5. **Operators and spectra:** operator hats, adjoint, commutator, eigenvalue/eigenvector notation, domains, self-adjointness, generalized eigenstates, delta distributions where introduced.
6. **Classical mechanics and constraints:** phase-space coordinates, Poisson brackets, weak equality, constraint surfaces, Hamiltonian vector fields, gauge notation.
7. **Canonical gravity:** spatial/spacetime indices, metric notation, lapse/shift, functional derivatives, constraint densities, DeWitt notation, local versus smeared constraints.
8. **Page–Wootters and relational time:** clock/system labels, tensor-factor identities, conditional states, POVM/instrument notation, clock readout labels, finite-clock periodicity notation.
9. **Exploratory philosophy:** any notation used there must first retain its standard mathematical meaning and visibly distinguish established usage from exploratory modeling.

## Maintainer audit

Before marking an example or concept ready, the maintainer must inspect every new or materially changed formula and notation-bearing code comment.

For each symbol or structural construct, ask:

1. Can the intended learner read it aloud?
2. Can the intended learner parse its structure?
3. Is its minimal meaning already covered by a declared prerequisite or stated locally?
4. Is its full technical meaning deferred to a later concept? If so, is that boundary explicit?
5. Is the symbol overloaded? If so, is the active meaning and scope clear?
6. Does code use an identifier derived from notation whose model scope is explicit?

If any answer is no, do not silently proceed. Add the needed coverage and update the learning/prerequisite path if required.

## Exposure policy

The notation reference is a general-access guide, not a learning-path prerequisite. Its default exposure is a persistent, low-friction global route in the Explorer. It may also be selectively suggested from notation-dense concepts or examples when that provides clear just-in-time support.

Do not make selective suggestion a blocking dependency for publication. If contextual links become costly, inconsistent, visually noisy, or difficult to maintain, retain the stable global route and defer additional local exposure rather than delaying a reader-visible change.

## Presentation rules

- Give the rendered notation before authoring markup. Learners read \(\phi_0\), not merely `\\phi_0`.
- State the spoken form near first use when it is not obvious.
- Explain subscripts, superscripts, accents, bars, hats, brackets, and delimiters as structure, not decorative typography.
- Use a notation table/register for recall, but explain essential notation in running prose before relying on it.
- Do not treat a code identifier as a substitute for a mathematical definition.
- Do not add a glossary term merely to avoid teaching the notation locally.

## Validation and review

Automated checks may detect unbalanced delimiters, obsolete formula markers, and known notation inventory omissions. They cannot fully decide whether a learner can parse a formula.

For material notation additions in mathematics, quantum mechanics, constrained systems, canonical gravity, or Page–Wootters, request an independent mathematics or physics pedagogy review.
