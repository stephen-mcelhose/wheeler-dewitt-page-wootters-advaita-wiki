# Review — UNIT B: Operators, Domains, and Self-Adjointness

## Scope reviewed

This proposal package supplies concrete draft canonical content for one concept, one example, and eight definitions. It follows the required sequence: finite C² linearity witness; bounded diagonal C² matrix with analytic bound and sample ratio; the \(\ell^2\) multiplier with analytic \(e_k\) proof and truncation ratio; finite-support truncations with tail norm and density proof. It retains finite full-domain C² self-adjointness and a short, non-computational restricted-derivative contrast.

## Mandatory computation-scope audit

| Item | Proposed helper / argument | Honest scope |
|---|---|---|
| C² linearity | `isLinearWitnessMatrix2D` | One supplied \((\alpha,\beta,x,y)\) witness only; the text separately identifies matrix algebra as the universal proof. |
| Bounded diagonal C² map | `boundedDiagonalAnalyticBound2D`, `boundedDiagonalSampleRatio2D` | The first returns the analytic finite-dimensional bound; the second is one nonzero-vector ratio. |
| Complex transpose symmetry | `isSymmetricFiniteMatrix2D` | Explicit finite matrix equality \(A=A^T\), deliberately distinct from adjointness. |
| Finite self-adjointness | `isSelfAdjointFiniteMatrix2D` | Valid for an explicit matrix with fixed full C² domain and orthonormal basis; prohibited for unbounded/restricted-domain use. |
| \(\ell^2\) multiplier | Analytic \(e_k\) proof plus `finiteMultiplierTruncationRatio` | Each fixed truncation is bounded; no function called `isUnbounded` exists. |
| Dense finite-support domain | Analytic tail proof plus `finiteTailNormAfter` | Computes only supplied finite tail data; no function called `isDense` exists. |

The comments explicitly separate sample/fixed-data checks from general finite-model statements and from infinite-dimensional mathematical truth. This is the key acceptance condition for the revised package.

## Mathematical scope decisions

- For a full-domain matrix on finite-dimensional \(\mathbb C^2\), \(H=H^\dagger\) is equivalent to self-adjointness. The code and prose state the required orthonormal-coordinate and full-domain assumptions.
- The multiplier is defined on \(D(T)=\{x\in\ell^2:(nx_n)\in\ell^2\}\); the \(e_k\) proof establishes its unboundedness analytically. No finite result is offered as a decision procedure.
- Finite-support sequences are dense in \(\ell^2\) by truncation and vanishing squared tail. The code only illustrates tails of supplied finite arrays.
- For \(P_0=-i\,d/dx\) on \(C_c^\infty(0,1)\), integration by parts is used only for symmetry. The package does not compute \(D(P_0^*)\), assert self-adjointness, classify extensions, or select boundary conditions.

## Source and citation verification flags

The sole proposed source remains **Reed & Simon, _Methods of Modern Mathematical Physics I: Functional Analysis_, doi:10.1016/C2013-0-10329-X**. This package did not independently access it. Its presence is a proposed citation, not approval. Before integration, an approved-source reviewer must verify and, where supported, add chapter/page/theorem locators for:

1. Adjoint definition for densely defined operators; symmetry as \(A\subset A^*\); and self-adjoint equality including domains.
2. The \(\ell^2\) multiplication-operator domain and the \(e_k\) unboundedness argument.
3. Density of \(c_{00}\) in \(\ell^2\) by coordinate truncation.
4. The closed-graph boundary: an everywhere-defined closed linear Banach-space operator is bounded.
5. The restricted-domain derivative integration-by-parts contrast and any statement about adjoint domains/boundary conditions.
6. Any future restoration of spectral-theorem or Stone-theorem claims (removed from the revised core rather than left unsupported).

Until verified, all six items are **explicit source-verification flags**. No source claim is marked approved.

## Local notation and implementation audit

- Local prose defines \(\ell^2\), \(c_{00}\), \(D(T)\), truncation, \(L^2([0,1])\), and \(C_c^\infty(0,1)\) before use.
- Central notation-reference reconciliation is deliberately deferred and must not be edited in proposal work.
- The Go listing is self-contained (`package main`) and intended as proposed example content. Integration should run `gofmt` and compile/test it in the project’s chosen code-extraction workflow.
- The dense/unbounded definition files were revised to state directly that finite tests cannot decide their infinite quantified properties.

## Required integration checks (deferred)

1. Obtain independent mathematics/source review resolving every flag above.
2. Reconcile definition-node IDs, inline annotations, frontmatter schema, controlled relationships, and reciprocal-example graph convention.
3. Reconcile notation reference without changing it in this proposal package.
4. Run code formatting/compilation, formula rendering, annotation-transform tests, link checks, and `make index validate` after authorized merge.
5. Do not publish or update Explorer/index artifacts as part of this unit.

## Review status

`draft` — implementation-ready as a proposal package, pending source verification, independent mathematics review, and authorized canonical integration.
