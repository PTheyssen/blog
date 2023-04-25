---
title: Invariants
author: Philipp Theyssen
---

Distilling the concept of invariants for microservice applications,
such that one can translate them into flink
-> quantify their  violation.

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
The main goal is enabling online monitoring of invariants
that concern data integrity in microservice applications using
stream processing.

One of the main tasks of the master thesis besides programming
type of work is coming up with a decent language for expressing
invariants and with that specifically invariants for capturing
data integrity in microservice applications.

We deal with systems that have the following properties and underlying
assumptions:

- distributed
- contain replicated / duplicated data in heteregenous datastores
- event driven communication between microservices (broker: Kafka) or
  row-level change events from using CDC on databases


Our runtime engine / computation to check the invariants will
be based on apache flink (a stream processing framework). We will
utilize the standard datastream API (allows for abitrary java code + state)
and the flink CEP library (cep patterns compiled into NFA+buffer).

In terms of related work one has to consider earlier work in CEP and
pattern languages. Further this also connects to runtime monitoring,
which has a more formal background and often directly monitors
invariants expressed as logical formulas (modal temporal first order logic).
This approach has the shortcoming of being potentially only accesible to
experts for formulating the invariants but in the end the software engineers
themselves have the domain knowledge and are the most capable of formulating
the invariants / maintaining and updating them.

On the other side of the spectrum you can write direct flink queries / operators
which comes down to using the flink API and writing java code, this
is very powerful and will be the choice of experienced flink users but
for engineers without stream processing experience this is a high
barrier of entry, therefore we aim at a simple language that allows
to quickly formulate relevant invariants using constructs which
get translating into a flink query.

Further, there are several pattern languages from research in CEP,
for example Cayuga, these focus on embedding SQL into event streams,
again this powerful and basically can be accomblished by
using the Flink SQL API but the invariants will often
result in multiple complicated queries and there is no clear
focus on expressing invariants.

### General Invariants Constructs
-> select latest event concerning some property for example:

LATEST product-price-changed KEY product-id as pc


-> before / ordering, followed by (causal ordering)

customer-accept FOLLOWED BY policy-creation

-> value based / comparison

-> for each event need select case (specification) then
can formulate invariant (ordering, causality + time invariant)

EVENT product-bought pb

EVENT product-price-changed pc
WHERE pc.ts < pb.ts
AND LATEST pc.id


INVARIANT pc.price = pb.price WHERE pc.id = pb.id

------------------------------------------------------------
EVENT product-bought pb, product-price-changed pc

INVARIANT pc.ts < pb.ts AND pc.price = pb.price AND pc.id = pb.id

------------------------------------------------------------

pb1 pb2 pc1 pb3 pc2 pc3 pb4

simpleCond: pb or pc, simpleCond: pb or pc: iterative:cond

EVENT SEQ (pc, pb) (next, followedBy,followedByAny)
INVARIANT: 


policy-created, policy-updated, policy-deleted
EVENT SEQ (policy-created, policy-updated, policy-deleted)
STATE 


foreign key
user-deleted, post-deleted, post-created

foreign key
user-deleted-from-db1, user-deleted-from-db2


product-price-changed pc {id, price}
product-bought pb {id, amount, price}
EVENT SEQ  pc1, !pc2, *, pb
WHERE pc.id = pb.id AND pc1.id = pc2.id
INVARIANT  pc.price = pb.price


Event Ordering Syntax (similar to regex)
EVENT SEQ  pc1, (pc2 | pb)
translating: pc1.followedByAny(SimpCond(pc2 or pb))

EVENT SEQ  pc1, [!pc2]*, pb
-> translating: pc1.notFollowedBy(pc2).followedByAny(pb)
pc1.followedBy(SimpCond(!pc2)) .

pc1, !pc2 -> pc1.notNext(pc2)

pc1, pc2*, pb


buy, buy, buy, buy-statistics
EVENT SEQ (buy+, buy-statistics)
WHERE buy.userid = buy-statistics.userid
INVARIANT SUM(buy.amount) = buy-statistics.total-amount


EVENT SEQ (customer-decision, policy-created) WITHIN 500ms

Writing an invariant:
0.1 (maybe filter beforehand only for relevant events)
1. Specify event seq (with ordering, with regex or, not followed, wildcard)
   -> how to handle followedBy, followedByAny 
   -> example: need followedByAny for checkout, otherwise would only check the invariant for first checkout
               and not subsequent ones
   -> only allow single or + as start of sequence
2. State (optionally)
3. WHERE clause before invariant / filter
3. Condition / Invariant -> has to be true




A a {id}
B b {id}
C c {id}
EVENT SEQ (a, b, c)


EVENTS e f g (f or g)



EVENT SEQ (product-bought pb, product-price-changed pc)
WHERE 


Invariants involving CDC of catalog items:
- if user is deleted in sql database -> orders and basket should be deleted

==> formulating these invariants with deep knowledge of each datastore
of each microservice defeats the whole purpose of microservice (developer
needs to know details about each microservice, and if microservice
evolves schema then invariants have to be changed


------ social network invariants
- only posts should exist if user exists (no user deleted event)
- timely reaction (limit on eventual consistency -> quantify eventual consistency in simulation)
  ==> these metrics could also be extracted from logging / tracing framework
  
--> invariants that just concern events themselves (timing) are not that novel / probably
easier to check in logging / tracing / monitoring
==> invariants get interesting once you look at data values / content of events
--> causal ordering detection (sequence of events) (specify DAG for event orders)


