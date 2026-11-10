---
{
  "schema_version": "2.0",
  "id": "example-parametrized-free-particle-constraint-flow",
  "type": "example",
  "title": "Parametrized Free Particle: Constraint Flow Is Gauge Flow",
  "summary": "A self-contained constrained toy model that calculates first-class constraint flow, local gauge fixing, and a second-class contrast without calling the gauge parameter time.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "comparison", "code"],
  "modality": ["text", "code"],
  "topics": ["constrained-systems", "parametrized-particle"],
  "teaches": ["calculate a first-class constraint bracket", "distinguish a gauge parameter from external time", "interpret a local clock gauge", "recognize an invertible second-class bracket matrix"],
  "prerequisites": ["classical-canonical-mechanics-primer", "hamiltonian-phase-space-and-poisson-brackets", "constrained-systems"],
  "action": "Compute the constraint flow of q, p, and t; verify that the constraint is first class; then compare its zero bracket matrix with a two-constraint second-class matrix.",
  "non_conclusion": "This deparametrizable free-particle toy model does not establish a global internal clock, a physical reduced phase space for gravity, or that gauge parameterization is physical time.",
  "relationships": [{"type": "illustrates", "target": "constrained-systems"}, {"type": "related-to", "target": "parametrized-particle"}],
  "sources": [
    {"title": "M. Henneaux and C. Teitelboim, Quantization of Gauge Systems", "url": "https://press.princeton.edu/books/paperback/9780691037691/quantization-of-gauge-systems", "persistent_id": "ISBN:9780691037691"},
    {"title": "P. A. M. Dirac, Lectures on Quantum Mechanics", "url": "https://store.doverpublications.com/products/9780486417134", "persistent_id": "ISBN:9780486417134"}
  ]
}
---
# Parametrized Free Particle: Constraint Flow Is Gauge Flow

## Prerequisites and local setup

Use extended canonical coordinates \((t,p_t;q,p)\), with nonzero brackets

\[
\{t,p_t\}=1,\qquad \{q,p\}=1.
\]

For a free particle of mass \(m>0\), define

\[
H(q,p)=\frac{p^2}{2m},\qquad C=p_t+\frac{p^2}{2m}\approx0.
\]

The symbol \(\approx0\) states that allowed points lie on the constraint surface \(C=0\). We take \(H_{\rm can}=0\) and total Hamiltonian \(H_T=N(s)C\), where \(N\) is a multiplier. The curve label \(s\) is a **gauge parameter, not time**.

## 1. The constraint is first class

There is only one constraint, so antisymmetry gives

\[
\{C,C\}=0\approx0.
\]

Thus this single constraint is first class in this regular toy setting. Its Hamiltonian vector field moves points along a gauge orbit:

\[
\frac{dF}{ds}=\{F,C\}
\]

when the illustrative multiplier is chosen as \(N=1\).

Apply this to the canonical coordinates:

\[
\frac{dt}{ds}=\{t,C\}=1,
\qquad
\frac{dq}{ds}=\{q,C\}=\frac{p}{m},
\qquad
\frac{dp}{ds}=\{p,C\}=0.
\]

Therefore \(p(s)=p_0\), \(t(s)=t_0+s\), and \(q(s)=q_0+(p_0/m)s\). These are gauge-related phase-space descriptions. They are not a claim that \(s\) is a physical time variable.

## 2. A local clock gauge and relational relation

Choose the gauge condition

\[
\chi=t-\tau=0,
\]

where \(\tau\) is a selected numerical clock reading. Since

\[
\{\chi,C\}=1,
\]

this condition intersects each local orbit once in this toy model. Eliminating \(s=\tau-t_0\) gives

\[
q(\tau)=q_0+\frac{p_0}{m}(\tau-t_0).
\]

This is a relational statement: the value of \(q\) when the configuration variable \(t\) reads \(\tau\). It does not identify the gauge parameter \(s\) with time, nor does it show that every constrained system admits such a global gauge.

## 3. Bounded second-class contrast

Now consider a different phase space with canonical pair \((Q,P)\) and constraints

\[
\chi_1=Q\approx0,\qquad \chi_2=P\approx0.
\]

Their bracket matrix is

\[
C_{ab}=\{\chi_a,\chi_b\}=
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad \det C=1.
\]

It is invertible, so this pair is second class. The pair directly removes the \((Q,P)\) degrees of freedom; it does not generate a family of gauge-equivalent descriptions as the first-class \(C\) above does.

## Pedagogical Go check

```go
package main

import "fmt"

type ExtendedPhasePoint struct {
    T  float64
    PT float64
    Q  float64
    P  float64
}

// Given: mass is positive and state obeys the extended canonical-coordinate model (t,p_t;q,p).
// Model scope: C = p_t + p²/(2m) is the parametrized free-particle constraint with multiplier N=1.
// Convention: s labels gauge flow; it is not external time.
func freeParticleConstraintRates(state ExtendedPhasePoint, mass float64) (tPrime, qPrime, pPrime float64) {
    return 1, state.P / mass, 0
}

// Given: ds is a chosen gauge-parameter increment, not a time increment.
// Illustration: forward Euler displays the exact constant rates of this free-particle constraint flow.
// This update moves to a gauge-related description and MUST NOT be interpreted as generic physical-time evolution.
func eulerStepGaugeParameter(state ExtendedPhasePoint, mass, ds float64) ExtendedPhasePoint {
    tPrime, qPrime, pPrime := freeParticleConstraintRates(state, mass)
    return ExtendedPhasePoint{
        T: state.T + ds*tPrime, PT: state.PT,
        Q: state.Q + ds*qPrime, P: state.P + ds*pPrime,
    }
}

// Given: chi1=Q and chi2=P use one canonical pair (Q,P).
// The second-class bracket matrix has determinant 1, so it is invertible in this bounded contrast.
func secondClassBracketDeterminant() float64 { return 1 }

func main() {
    state := ExtendedPhasePoint{T: 0, PT: -2, Q: 3, P: 2}
    next := eulerStepGaugeParameter(state, 1, 0.5)
    fmt.Printf("gauge-related point: t=%.1f, q=%.1f, p=%.1f; det C=%.0f\n",
        next.T, next.Q, next.P, secondClassBracketDeterminant())
}
```

The initial point satisfies \(C=-2+2^2/(2\cdot1)=0\). With \(ds=0.5\), it moves to \((t,q,p)=(0.5,4,2)\), still on \(C=0\). The output labels this as gauge-related rather than later in time.

## What this does not show

This example is deliberately solvable because \(t\) is monotonic along its local gauge orbits and \(\{t-\tau,C\}\ne0\). In general, clock choices can fail globally, gauge conditions can intersect an orbit more than once or not at all, and field-theoretic gravity has local constraints and boundary subtleties absent here.
