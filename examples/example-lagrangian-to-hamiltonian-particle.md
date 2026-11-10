---
{
  "schema_version": "2.0",
  "id": "example-lagrangian-to-hamiltonian-particle",
  "type": "example",
  "title": "Classical Canonical Mechanics: From Lagrangian to Hamiltonian",
  "summary": "A self-contained one-dimensional particle example deriving conjugate momentum and the Hamiltonian from a regular Lagrangian.",
  "review_status": "draft",
  "status": ["synthetic"],
  "patterns": ["calculation", "derivation", "code"],
  "modality": ["text", "code"],
  "topics": ["classical-canonical-mechanics-primer", "hamiltonian-phase-space-and-poisson-brackets"],
  "teaches": ["calculate conjugate momentum", "invert a regular velocity-momentum relation", "construct a Hamiltonian by Legendre transformation", "distinguish a Lagrangian from a Hamiltonian"],
  "prerequisites": ["classical-canonical-mechanics-primer"],
  "action": "Start with a regular particle Lagrangian, calculate its conjugate momentum, solve for velocity, and construct the Hamiltonian in canonical variables.",
  "non_conclusion": "This one-dimensional regular mechanical model does not establish a Hamiltonian construction for singular Lagrangians, constrained systems, fields, or general relativity.",
  "relationships": [
    {"type": "illustrates", "target": "classical-canonical-mechanics-primer"}
  ],
  "sources": [
    {"title": "V. I. Arnold, Mathematical Methods of Classical Mechanics", "url": "https://doi.org/10.1007/978-1-4757-2063-1", "persistent_id": "doi:10.1007/978-1-4757-2063-1"}
  ]
}
---

# Classical Canonical Mechanics: From Lagrangian to Hamiltonian

## Prerequisites and local setup

**Model scope:** Use one configuration coordinate \(q\), an externally supplied time \(t\), and a particle with mass \(m>0\) in a potential \(V(q)\). The velocity is

\[
\dot q=\frac{dq}{dt}.
\]

The model is regular because its velocity--momentum relation can be inverted. Singular Lagrangians and constraints are deferred to Classical Constrained Systems.

## 1. Start with the Lagrangian

Take the standard particle Lagrangian

\[
L(q,\dot q)=\frac12m\dot q^2-V(q).
\]

Read: “L of q and q dot equals one half m q dot squared minus V of q.”

The first term is kinetic and the second is the potential contribution in this standard mechanical model.

## 2. Calculate the conjugate momentum

The momentum conjugate to \(q\) is

\[
p=\frac{\partial L}{\partial\dot q}.
\]

For this Lagrangian,

\[
p=\frac{\partial}{\partial\dot q}\left(\frac12m\dot q^2-V(q)\right)=m\dot q.
\]

Because \(m>0\), solve this relation for the velocity:

\[
\dot q=\frac{p}{m}.
\]

This invertibility is the regularity property used by the canonical construction.

## 3. Construct the Hamiltonian

The Hamiltonian is the Legendre transformation

\[
H(q,p)=p\dot q-L(q,\dot q),
\]

with \(\dot q\) replaced by its expression in \((q,p)\). Substitute \(\dot q=p/m\):

\[
\begin{aligned}
H(q,p)
&=p\left(\frac{p}{m}\right)
-\left[\frac12m\left(\frac{p}{m}\right)^2-V(q)\right]\\
&=\frac{p^2}{2m}+V(q).
\end{aligned}
\]

The canonical variables are now \((q,p)\), which the next concept organizes into phase space.

## 4. Harmonic-oscillator follow-up

For the particular potential

\[
V(q)=\frac12m\omega^2q^2,
\]

the Hamiltonian becomes

\[
H(q,p)=\frac{p^2}{2m}+\frac12m\omega^2q^2.
\]

This is the Hamiltonian used in the next harmonic-oscillator phase-space example.

## 5. Pedagogical Go construction

```go
package main

import (
    "errors"
    "fmt"
)

// Given: mass is positive and velocity is the externally timed derivative dq/dt.
// Model scope: this is the kinetic term of the stated one-dimensional regular particle model.
func kineticLagrangian1D(mass, velocity float64) (float64, error) {
    if mass <= 0 {
        return 0, errors.New("regular particle model requires mass > 0")
    }
    return 0.5 * mass * velocity * velocity, nil
}

// Given: mass is positive and velocity is dq/dt in the stated regular model.
// Mathematical fact: p = ∂L/∂qDot = m qDot for this particle Lagrangian.
func conjugateMomentum1D(mass, velocity float64) (float64, error) {
    if mass <= 0 {
        return 0, errors.New("conjugate momentum requires mass > 0")
    }
    return mass * velocity, nil
}

// Given: mass is positive and momentum was defined by p = m qDot.
// Mathematical fact: the regular velocity--momentum relation inverts as qDot = p/m.
func velocityFromMomentum1D(momentum, mass float64) (float64, error) {
    if mass <= 0 {
        return 0, errors.New("velocity reconstruction requires mass > 0")
    }
    return momentum / mass, nil
}

// Given: mass is positive and potential gives V(q) for the declared model.
// Model scope: this computes H(q,p) = p²/(2m) + V(q) after the regular Legendre transform.
func hamiltonianFromLagrangian1D(
    position, momentum, mass float64,
    potential func(float64) float64,
) (float64, error) {
    if mass <= 0 {
        return 0, errors.New("Hamiltonian construction requires mass > 0")
    }
    return momentum*momentum/(2*mass) + potential(position), nil
}

func main() {
    mass := 2.0
    velocity := 3.0
    position := 1.0
    omega := 4.0

    kinetic, _ := kineticLagrangian1D(mass, velocity)
    momentum, _ := conjugateMomentum1D(mass, velocity)
    reconstructedVelocity, _ := velocityFromMomentum1D(momentum, mass)
    harmonicPotential := func(q float64) float64 {
        return 0.5 * mass * omega * omega * q * q
    }
    hamiltonian, _ := hamiltonianFromLagrangian1D(position, momentum, mass, harmonicPotential)

    fmt.Println(kinetic)               // 9
    fmt.Println(momentum)              // 6
    fmt.Println(reconstructedVelocity) // 3
    fmt.Println(hamiltonian)           // 17
}
```

The code implements the same chain used in the calculation:

```text
Lagrangian
    → conjugate momentum
    → invert velocity--momentum relation
    → Hamiltonian
```

## What this example does and does not show

This example shows the regular one-dimensional particle construction. It does not establish a Legendre transformation for singular Lagrangians, derive constraints, model fields, prove global canonical coordinates, or identify every Hamiltonian with conserved energy.
