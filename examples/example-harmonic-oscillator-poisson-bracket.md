---
{
  "schema_version": "2.0",
  "id": "example-harmonic-oscillator-poisson-bracket",
  "type": "example",
  "title": "Harmonic Oscillator: Poisson Brackets and External-Time Flow",
  "summary": "A self-contained one-degree-of-freedom calculation of a Poisson bracket and ordinary Hamiltonian evolution.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "code"],
  "modality": ["text", "code"],
  "topics": ["hamiltonian-phase-space-and-poisson-brackets"],
  "teaches": ["compute a canonical Poisson bracket", "derive Hamilton's equations", "distinguish external-time flow from later gauge flow"],
  "prerequisites": ["classical-canonical-mechanics-primer", "hamiltonian-phase-space-and-poisson-brackets"],
  "action": "Compute {q,H} and {p,H} for the oscillator, then use a small-step numerical check to see the phase-space point move in external time.",
  "non_conclusion": "This one-dimensional external-time model does not contain constraints or gauge redundancy and does not model a constrained gravitational system.",
  "relationships": [{"type": "illustrates", "target": "hamiltonian-phase-space-and-poisson-brackets"}],
  "sources": [{"title": "V. I. Arnold, Mathematical Methods of Classical Mechanics", "url": "https://doi.org/10.1007/978-1-4757-2063-1", "persistent_id": "doi:10.1007/978-1-4757-2063-1"}]
}
---
# Harmonic Oscillator: Poisson Brackets and External-Time Flow

## Prerequisites and local setup

Use one canonical coordinate \(q\), its conjugate momentum \(p\), and an **external** time \(t\). For functions \(F(q,p)\), \(G(q,p)\), define

\[
\{F,G\}=\frac{\partial F}{\partial q}\frac{\partial G}{\partial p}-\frac{\partial F}{\partial p}\frac{\partial G}{\partial q}.
\]

Let \(m>0\), \(\omega>0\), and

\[
H(q,p)=\frac{p^2}{2m}+\frac12m\omega^2q^2.
\]

This is the one-dimensional harmonic-oscillator Hamiltonian. The model uses no constraints.

## Calculation

Since \(\partial q/\partial q=1\), \(\partial q/\partial p=0\), and \(\partial H/\partial p=p/m\),

\[
\{q,H\}=\frac{p}{m}.
\]

Since \(\partial p/\partial q=0\), \(\partial p/\partial p=1\), and \(\partial H/\partial q=m\omega^2q\),

\[
\{p,H\}=-m\omega^2q.
\]

Hamilton's equations therefore give

\[
\frac{dq}{dt}=\frac{p}{m},\qquad \frac{dp}{dt}=-m\omega^2q.
\]

Differentiating the first and using the second yields \(d^2q/dt^2=-\omega^2q\). The energy is conserved because \(H\) has no explicit \(t\)-dependence and \(\{H,H\}=0\).

## Pedagogical Go check

The code uses an Euler step only to expose the two bracket-derived rates. It is not a high-quality long-time symplectic integrator.

```go
package main

import (
    "errors"
    "fmt"
)

type PhasePoint1D struct {
    Q float64
    P float64
}

// Model scope: this predicate checks only the positive parameters required by this finite oscillator model.
func HasPositiveOscillatorParameters1D(mass, omega float64) bool {
    return mass > 0 && omega > 0
}

// Given: mass and omega are positive real constants, and state stores one canonical pair (q,p).
// Model scope: this is the one-dimensional harmonic oscillator with external time t.
// Convention: qDot and pDot represent dq/dt and dp/dt, not derivatives with respect to a gauge parameter.
func HarmonicOscillatorRates1D(state PhasePoint1D, mass, omega float64) (qDot, pDot float64, err error) {
    if !HasPositiveOscillatorParameters1D(mass, omega) {
        return 0, 0, errors.New("oscillator model requires mass > 0 and omega > 0")
    }
    return state.P / mass, -mass * omega * omega * state.Q, nil
}

// Given: dt is a chosen external-time increment and positive oscillator parameters.
// Illustration: forward Euler makes the bracket-derived rates visible in one update.
// Limitation: repeated Euler steps do not exactly conserve the oscillator energy.
func EulerStepExternalTime1D(state PhasePoint1D, mass, omega, dt float64) (PhasePoint1D, error) {
    qDot, pDot, err := HarmonicOscillatorRates1D(state, mass, omega)
    if err != nil { return PhasePoint1D{}, err }
    return PhasePoint1D{Q: state.Q + dt*qDot, P: state.P + dt*pDot}, nil
}

func main() {
    state := PhasePoint1D{Q: 1, P: 0}
    next, err := EulerStepExternalTime1D(state, 1, 2, 0.01)
    if err != nil { panic(err) }
    fmt.Printf("q(t+dt)=%.4f, p(t+dt)=%.4f\n", next.Q, next.P)
}
```

With \(q=1\), \(p=0\), \(m=1\), and \(\omega=2\), the initial rates are \(dq/dt=0\) and \(dp/dt=-4\). For \(dt=0.01\), the code produces \((q,p)=(1,-0.04)\) after one Euler step.

## What this does not show

The parameter \(t\) here is an external time supplied by the model. This calculation does not license calling every Hamiltonian flow “time evolution.” In the next unit, constraint-generated curves use a gauge parameter \(s\), which is not time.
