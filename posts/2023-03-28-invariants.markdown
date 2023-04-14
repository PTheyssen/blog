---
title: Invariants
author: Philipp Theyssen
---

Distilling the concept of invariants for microservice applications,
such that one can translate them into flink -> quantify their violation.

## Introduction

Invariants about programs, systems, mathematical (formal) 
statements about a program, system that are always true.


Landmark paper is Hoare (An Axiomatic Basis for
Computer Programming), which proposes to use
logical foundations for  computer programming and using 
axioms and deduction rules (formal proofs) for proofing
properties of computer programs (Hoare Logic).

Properties / invariants of computer programs (semantics 
of programming language), model microservices
as statemachine (distributed system).

Mathematical/formal exact description of execution space,
behaviour of the program.

Deterministic vs. Non-deterministic System important
distinction, mostly large complex system become
non-deterministic in some regards?

Software, programming will have functionality / purpose,
need to be sure it is fulfilled (depends on definition,
specification).

Basically can check if program adheres to specification,
properties (business logic, correctness properties,
domain properties etc.).

Larger / open problem to come up with specification in
the first place, facing constraints / limitation
of resources (time, compute, memory) -> need
to fit software into entire world / model, business,
organization, social organisations, constructs,
agents (game theory), predictions.

-> some pointers (full systems building, formal methods
applied).

### Lambda calculus, type theory foundations
Haskell / liquid haskell, coq, agda -> 
express programs in these and then proof properties
about them.

### TLA+ (state machines)
Model a system with simplified model (state machine,
transitions functions), model check properties.

## Definition


## Checking


## Data integrity Invariants (microservices)
