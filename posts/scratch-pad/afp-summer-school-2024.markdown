---
title: AFP Summer School 2024
author: Philipp Theyssen
---

# Attending the Advanced Functional Programming Summer School 2024

I am traveling to Utrecht right now to attend the Advanced Functional Programming in Haskell 
(https://uu-afp.github.io/index.html).

I am very excited to improve my functional programming knowledge.

During my master heard about it.

Interested to see which concepts will be useful for my day to day work.

## Topics to review

Great resources:
- https://github.com/sdiehl/wiwinwlh
- https://learnyouahaskell.com/
- https://jutge.org/doc/haskell-cheat-sheet.pdf
- https://learnxinyminutes.com/docs/haskell/

### Haskell Notes
- System F underlying formalism for haskell https://en.wikipedia.org/wiki/System_F

- Type classes for polymorphism
- fold is the reduce function!
https://stackoverflow.com/questions/13280159/haskell-foldl-and-foldr
- Comments {- -}, --, {- | for function definition haddock
https://haskell-haddock.readthedocs.io/latest/
- String "", characters ''
- multi-line strings with \, \n

- Haskell number types, type classes

- pattern matching
- maybe

- argument capture (@)
- guards |
- record syntax pattern matching

- fundamental value-oriented (applicative) programming
paradigm
- main model of computation evaluation of expressions
- haskell functions are values but cannot be printed

- polymorphism: type schema (a) can be replaced by concrete type,
constraints via type classes: Num: Int, Double..
- equality Eq almost all but not functions (
- checking if two functions are equal (reduces to halting problem!)

- can write boolean guard on pattern
myElem x (y:ys) | x == y = True

- non-trivial haskell programs contain problem-specific
type definitions

- type synonyms (domain for string) (DDD with FP =>F# book)

- Types enumeration data Color = Red | Green

- Bool is predefined enumeration

- recursive data types (constructor)
- record syntax
- data type polymorphic
- mutual recursion!

- interesting API design considerations
  - what to expose, which elements, what is needed,
    what is the goal => domain!
    
- type constraints foo :: (Num a, Show a) => a -> String

- implementing Instance (declaration)
 - Num: +, -, *, fromInteger
 
- Equational reasoning equivalence of expressions!
  => mean the same thing (meaning of the program),
     can replace them
     
Haskell I/O
- top level result printer is not pure
 ==> have pure program compute a lazy list (stream)
     of I/O requests (actions) for the top-level printer 
     to perform
     
====> producing the list it self is effect free,
obeying it is not
- list is inspected incrementally

==> need more complicated datatype than list to
also receive input from real world

Simplified 

- REPL:
  - if top-level expression has ordinary type (non IO) then just evaluate and print (should have show instance!)
  
- exception passing style problem whith Maybe monad

- global constants just in module global constant,
  problem when global mutable state (parallel vs. in sequence)
  => make explicit passing state around!!
  ==> all other programming languages basically pass this "monad" global
  state implicitly with them and especially when you access it!
  - state passing is fixed by monad
  
==> goal effectful function without Monad: a -> b corresponds
to total, pure function of type a -> M b

M t is the type of computations returning a result of type t

Computation that just returns a given value:

unit :: a -> M a
 - errors (maybe): unit a = Just a
 - state : unit a = \s -> (a,s)
 
Bind: computation that applies effectful function to result (if any)
of effectful computation: bind :: M a -> (a -> M b) -> M b

For error:
bind (Just a) f = f a
bind (Nothing) f = Nothing


Errors: M t = Maybe t
State: M t = Int -> (t, Int)

For state:
bind m f = (\s -> 
               let (a s1) = s m in
                 f a)
                 
                 
For state:


Computations with creating a new computation + bind how to bind computations
together, but have to obey laws!

- return is unit!


Monad laws:
- say composition of effectful functions  behaves as expected! (associative!)

Monads are functors and applicatives

- functor typeclass, things that can be mapped over!
-- applicative functors 
https://en.wikibooks.org/wiki/Haskell/Applicative_functors

fmap infix <$>

- kind when talking about types => * -> *
https://wiki.haskell.org/Kind

- generally monads etc. only for structuring crucial effects,
  with outside world etc. does not effect writing pure (lambda) functions
  that we can reason about nicely
  
- Invariants

- logic, mathematics, computations (traversing, data structures, APIs,
runtime behaviour)

- computer huge array of memory cells, CPU, fetching data, applying, mathematical
functions to it

- software architecture, layering, connecting different modules

#### Haskell 2010 Language Report

## Topics covered
- Monads and I/O
- Applicative functors
- GADTs
- Lambda calculus
- Information flow
- Accelerate https://hackage.haskell.org/package/accelerate => nice GPU programming! => math! https://ivogabe.com/
- Type families


## Development Setup
I am in a bit of a weird situation having NixOs as my daily driver,
but having not yet fully grasps all its details.

Moreover setting up a haskell development environemt seems to be
a bit tricky at times.

Different options:
- use nix only for ghc + cabal + zlib then let cabal install all dependencies
- use nix for also installing haskell dependencies / packages => caching + sharing

- https://discourse.nixos.org/t/super-simple-haskell-development-with-nix/14287/3
- https://docs.haskellstack.org/en/stable/nix_integration/


Emacs with Eglot with and Language server 
is working pretty nicely.

Would like complete hoogle / haskell source code
offline mirror of websites!


# Goals for AFP 2024
- Learn useful FP, formal concepts for building software
- network, meet new people, discuss ideas
- share thoughts
- learn a lot => focus
- ask questions! => clarify from first principles things I do not understand
- what basic programming structures are needed
- improve end-2-end knowledge of computer systems
  - parallelism
  - correctness
  - File I/O
  - networking, distributed systems
  - basic strace (do system calls auditing)
     - what requests, queries are issued
  - algorithms and data structures
- domain modeling with FP / data types
- modules / API design!
- underlying formalism, lambda, type checking / compiler
- dive into underlying model (breitner thesis)
- make things explicit, learn fundamental underlying
nature of computation, functions, modules, correctness,
systems, operating systems, expressed in
clean useful way!
- junior mindest => how to build systems!

==> nothing shameful / bad about using easiest possible formal methods to model
domain for example state machines in UI / dashboard, make it explicit

==> end goal domain modeling writing software that is:
- solving business problem
- correct
- clean design => changing requirements / refactoring
- fast!
- technical tools for producing value / saving costs
  => team enablement, productive tools

## FP Software Design 
Larger design patterns, concepts, algebraic refactoring.


Strut


## Find nice applications of FP / Haskell
- DSL for concurrent computation
- DSL for correctness, compilers
- Web applications (servant, strong types!) => lacking tooling?
- Elm / Purescript for frontend design?


# Lecture 1
Fun of programming


Haskell Review:
- pattern matching 
- functions as first class (lambda!)
- not possible type as an argument to a function, data type declaration (variable)

- polymorphic 

- theorem for free, behaviour reading from map type

- Haskell distinguishing feature
  - type classes (interface) => not many others have this?
  
- type classes => reuse a lot of code (elem) => 

- typeclasses, extra function / dictionary which has all the functions from the
typeclass => when compiled and then that function is being called

- 5 is overloaded, Num a (5 are polymorphic)
==> when writing code 5 is a function, can not be easily inlined etc. have to keep in mind!

- ad-hoc polymorphism


Packages and modules:
- Haskell module system => splitting code into files/modules
- Strength and weaknesses:
  - units of compilation (.hi file) haskell interface
  - namespace management
  
- compared to Ocaml (which has interface, signatures) in the module, this haskell is not
   => different modules implement that same 
   
- class system, Haskell backpack => interface declaration like ocaml


module M(D(), f, g) where -- exporting D(), f, g

Module names uppercase letter

- extension, hierarchical modules:
  - module X.Y.Z to be named X/Y/Z.hs or X/Y/Z.lhs (literate haskell)
  
==> Haskell standard library got refittet into hierarchical module System
  List => Data.List
  
- same module can be imported multiple times (different functions)
  - qualified names
  
- name clashes are reported lazily, rename with as


import M1 -- both foo
import M2 -- foo


==> name clash only at runtime!


import Prelude -- always (implicitly

qualified Prelude -- for overwriting / hiding

Modules allowed to mutually recursive, but discouraged

==> top module imports everything you want and exports the bits you want to expose in your library

- implementation you want as a type class (a bit fishy, broken)
  => only one instance for every type class ==> wrapper (sorting)

API and want to have different implemention

- be explicit / qualified for imports

- compilation units, GHC


Best pratices:

- use qualified names vs. pre- and suffix (no mapTree, instead map) in Tree module!

- use qualified (Data.Map import qualified Data.Map as M)

https://wiki.haskell.org/Import

- packages (cabal package), modules form unit to
be distributed

- cabal => just installs packages
- stack manages ghc version, base libraries etc.

- no nesting where

- hlint, use blank lines for readablility
   => 

- make small functions! => split up (one screen)!
 ==> split up large functions

- introduce type synonyms 

Introduce newtype wrapper / data type

newtype Hours = Hours Int

- basics small functions + custom types
 ==> redefine typeclasses for each one separately
- wrapping / unwrapping
 
- hide implementation detail that it is an Int

- API, modules, implementations
- testing quickcheck, property based testing

- newtype is nop (same runtime representation)

- with real data type
- data in memory

boxed type (thunk), pointer?!, 


Comments:
- every top level function
- comment tricky code (invariant) etc.
- use haddock

Use (data) Types!
- application for banks / domain!!
==> work with different currencies
- ==> huge data models => what is being manipulated

- good at modeling algebraic data types!

- make types meaningful => 

- do not throw error but instead maybe etc.
- make functions total!

- avoid partial functions => adjust data model!

- detect partial functions:
  -Wall
  
  
- use let 

let x = foo bar baz in x + x +x 

foo bar baz + foo bar baz + foo bar baz

difference semantically (denotationally they are the same,
but operational not)

- let bound function only executed once (more performant)

- compiler: common subexpression elimination
  - can sometimes not happen
  
- lazy language

- dive into GHC https://www.haskell.org/ghc/

- design recipes https://htdp.org/
  - start with examples
  - test driven behaviour a bit (though not full domains)
  
- Better: play around with type definitions!, leave
bits undefined (type hole), when defining functor
instance of complicated data structure

- choose types / domain modeling, define data types
  - define functions already API / domain design
   ==> conal elliot same insight => rewatch talk
   
- interfacing with databases

- forcing pure functions + making side effects explicit
  - pure data structures, non destructive updates

- Data Modeling database / domain model, currencies
etc. => what are we talking about even with
domain experts, contracts, not so much ML, python
libraries for raw compute on GPUs but generally
just correct data model, process modeling with formal
methods!


## Monad lecture
- motivate with examples:
- error 

- Monad, 

- refactor example bind operator calls


Simulating exceptions => throwError, catchError

### State Monad

- explicit but still convenient

- parallel programming => simon marlow book!

- get and put function

- wrap state with new type (runState)


- find interesting domain / library

- list comprehension "<-" similar to bind (>>=)
--> list comprehension order matters!

- monad as common interface! (type class), nothing else

Class Monad ranges not over ordinary types
but parameterized types: * -> *
can have 

Functor less specialized, can be derived from monad
- first comes domain, model, data model, then
computation basic (networking, 

Monad laws:
- programming perspective, type will behave
weirdly
- library functions polymorphic over monads assume laws to be true

use functor, kleisli operator (fish) f >=> g
g . f works within a monad, f x >>= g


```haskell
(>>=) :: m a -> (a -> m b) -> m b
return :: a -> m a

join :: m (m a) -> m a
return :: a -> m a
```

">>" sequence in Monad get effects of monadic
operation but do not care about result

do-notation:
- just syntactic sugar (>>=)


IO monad!
IO is primitive built into haskell (>>=) and
return for IO are primitive functions

- no runIO :: IO a -> a
- value of IO denote side-effecting programs
that can be executed by the run-time system

- show laws hold for IO / state, equality in haskell,
use equational reasoning


ghci> :i IO
type IO :: * -> *
newtype IO a
  = GHC.Types.IO (GHC.Prim.State# GHC.Prim.RealWorld
                  -> (# GHC.Prim.State# GHC.Prim.RealWorld, a #
))
        -- Defined in ‘GHC.Types’
instance MonadFail IO -- Defined in ‘Control.Monad.Fail’
instance Monoid a => Monoid (IO a) -- Defined in ‘GHC.Base’
instance Semigroup a => Semigroup (IO a) -- Defined in ‘GHC.Base’
instance Applicative IO -- Defined in ‘GHC.Base’
instance Functor IO -- Defined in ‘GHC.Base’
instance Monad IO -- Defined in ‘GHC.Base’

- state has unique value, threaded throughout the program,
does not change order of IO operations

- side effect and variables
- 

- IO monad does not allow to judge what kind of IO
is being done, in prinipcal everything can happen

mapM
mapM_ => underscore return unit

sequence :: (Monad m) => [m a] -> m [a]

foldM


## Instruct haskell language server to use installed cabal packages!
https://haskell-language-server.readthedocs.io/en/latest/configuration.html

create hie.yaml file with

```yaml
cradle:
  cabal:
```


Use quickcheck, basic property based testing for 
typescript / JS => improve correctness of system

- higher level, meta reasoning where appropriate,
what constructs, types, closures, environments,
compilers, intermediate languages


- basic of TDD, property based testing to verify
specifications first!


- review applicative + monad laws => data structures,
recursion across datastructures!

- writing code in haskell libaries, algorithms,

real world applications, CRUD, database, web application,
- platform
- testing
- performance
- robustness
- logging

TeleType Monad specializes IO into 
getline interaction stdout, stdin

--> Biased as Application developer => want to build
CRUD app in it?

Monad as FP programming patterns, functor, applicative


- use rosetree for 

- to have total functions define custom tree,
=> subset of valid rose tree


## Applicative functors
- same class as monads * -> * (kinds)
- applicative functors
- foldable
- traversable
- arrows

- example sequencing => using do- monad is 
a bit weird

- ap function

Evaluating expressions

data Expr v = Var v | Val Int
 | Add (Expr v) (Expr v)

type Env v = Map v Int

eval : Expr v -> Env -> Int
eval (Var v) env = lookup v env
eval (Val i) env = i
eval (Add l r) env = (eval l env) + (eval r env)

applicative alternative:
const : a -> (env -> a)
const x = \env -> a

s : (env -> a -> b)

transpose matrix / zipping example

work through https://en.wikibooks.org/wiki/Haskell/Applicative_functors

monad subsequent actions can depend on previous side 
effect, in applicative usually not the case

- great to have applicative, use interfaces,
typical functions you can use to map over etc.

- monad transformers for composing monads,
  composition of specific monads, and interface
  to extend this 
  
- for every new monad you want to add, have to
write for each existing ones how it composes with them


composing applicative functors

applicative functor laws, people expect to hold
(would be better to have stronger type system which
ensures it holds)

- identity
- composition
- homomorphism
- interchange

Traversing



Folding: foldable

class => containers example IO is not foldable, traversable
but lists and maybe are

class Foldable f where
  foldr :: (a -> b -> b) -> b -> f a -> b
  foldMap :: Monoid m => (a -> m) -> t a -> m

- for lists foldr makes sense, but for other
data structures not good fit, foldMap


Monoid (half group?)
- mempty + mappend
- mempty unit (mempty + x = x)
- associative


Mathemtical structure, Algebra showing up in manipulating data (domain model in real world,
category theory) combinations of things, rules

foldMap (need monoid)
foldMap :: Monoid m => (a -> m) -> t a -> m

foldMap :: Monoid m => (a -> m) -> Tree a -> m
foldMap f Empty = mepty
foldMap f (


Point of typeclases (abstractions), foldr is useful for lists

Generalize any with traversable type (foldMap), need monoid

wrap boolean in new type for monoid

so wrap boolean in new type so other people 

- any for binary tree implementation with foldable subclass

prelude functions work over any traversable
 ==> prelude functions work if define instance of elem, length, any
 
 
instance Foldable Maybe :
foldr 
foldMap

Pairs

foldr f p1 


Focus on applicable, useful knowledge, impact on the world
structuring things


Arrows:
abstraction over functions and function composition,
alternative categories

pattern in multiple places, abstract over it
- type classes capture a common pattern
- boilerplate code 
 --> example prelude functions which work over
     every container only need to link custom
     data structure into interface
     
- understanding patterns can help guide design


- is doing exercises, problem sets really the right
thing, should I not follow something I think
is impactful and work on that constantly?


Datatypes:

new datatype Tree kind * -> *
two constructor functions
Leaf :: Tree a
Node :: Tree a -> a -> Tree a -> Tree a

GADT syntax

{-# LANGUAGE GADTS #-}
data Tree a where
    Leaf :: Tree a
    Node :: Tree a -> a -> Tree a -> Tree a
    
    
3 constraints

Phantom types erased at compilation?

- smart constructors, APIs

- typesafe APIs, important for BE, FE, databases

GADTS
-> can have different return types

- pattern matching works key for GADTs
 ==> right hand sides usually all the same type
 but with GADT no longer constraint to that
 
 type refinement in GADT, more type information?

Without GADT type inference of haskell alg always
finds most general type, with GADT this breaks
==> need to write type and top level

GADT, allow 

eval :: Expr a -> a
eval (Pair x y) = Pair (eval x) (eval y)
eval (Fst p) = fst (eval p)
eval (Snd p) = snd (eval p)


GADT 


Lists with known length

- peano naturla number (unary representation)

- head and tail

vectors!

data Zero -- no constructor
data Succ n -- no constructor


New GADT describing addition as a relation


- singletons 

Equality type:
- Equal is an equivalence relation


Type families get some restricted notion of functions
on types

In dependently types languages have all value level
programming, curry-howard correspondence,
type in agada corresponds to theorem, program
corresponds to proof

Haskell type system (inconsistent etc.?),
if depedently 

Agda functions have to be total, terminated
- agda is kind of haskell with depedently types
- dependent types with haskell will not be a proof
systems, but could be very useful for invariants

- servant is using type level programming
 - on type level web apis always respect
 
- chordify -> has haskell backend + servant!

- backend servant service, make use / impact of advanced
functional features

Agda Intro:



- applied FP / FRP => UI, event based updates +
data, sql, kafka etc., flink data platforms, computation,
algorithms, correctness

- work on problems, exercises => stay sharp

# Lambda calculus

Compared to haskell very small,

e := var 
   | e e          -- function application
   | \ var -> e   -- lambda exprexion (anonymous function)

Writing fibonacci in lambda calculus!

fib :: Int -> Int
fib n = if n < 2 then 1 else
        fib (n-1) + fib (n-2)
        
        
        
Booleans:

Reduction / evaluates


Natural numbers:


n1 < n2

if nil 

zero  = \z s -> 
succ  = \z

scott encoding (dana scott)

fix point in lambda for implementing recursion



Focus on basic information flow, APIs, microservice, consistency etc.
Information flow

Haskell, GHC core lambda calculus with built in case + performance optimization

IO is implemented with C runtime system (magic)
- no mutations

Focus on useful technologies, useful systems, solving applied business problems,
using formal methods etc., infer (meta) statist analysis


# Lecture Information flow

- use haskell to identify IO code vs. pure functions, pure code imports is fine

- DbIO custom IO monad only to the database

- IFC libaries wrap IO actions to prevent leaks

- Simple "standard" GHC extensions
- multi-parameter type classes
- safe haskell (unsafe low level IO functions)

MAC: static ifc haskell libarary => ~ 200LOC

Labeled mutable references:

- figure out order of throw
  - order of exceptions


- no read-up no write down

newRef :: l1 <= l2 => a -> MAC l1 (Ref l2 a)

writeRef :: l2 <= l1  => Ref l1 a -> a -> MAC l2 ()

readRef ::   => Ref l1 a -> MAC l2 a


https://ifc-challenge.appspot.com/

# Accelerate
- DSL embedded in haskell, functional parallel array programming

- map
- reduction
- prefix sum
- permutate


Accelerate provides combinators

import Data.Array.Accelerate

dotp :: Acc (Vector Float) -> Acc (Vector Float -> Acc(Scalar Float)

only fold function needs associativity

 Deep embedding: combinators representation of a computation
 
 Acc a is the represetntation of AST of an array computation
 
 Language design contains parallelisable constructs/combinators
 
 two types to represent computations:
 - Acc array comp
 - Exp calar comp
 
 
map :: (Exp t1 -> Exp t2) -> Acc (Array sh t1) -> Acc (Array sh t2)

Shallow Embedding: direct compute
Deep Embedding: only construct representation of computation before sending to CPU

- only use haskell to construct computation (let user specify computation)

- runtime/compiler of accelerate in haskell
  ==> generate llvm code directly not C code
  
Tradeoff writing cuda => someone for knowing GPU code vs. someone knowing haskell


filter :: map predicate

map
fold
scanl
permute

map => apply predicate (make it 0 or 1)
scanl => fill index (0, +1)
permute => put elements into correct index 

Implementing scan in parallel fashion:


Get humbled by experts => keep learning, improving

Fusion optimization:
- dsl advocates splitting the program into many small steps,
but that would be inefficient to execute like this
- naive: one (parallel) loop per combinator
- Fusion: combine multiple combinators into one loop

programming GPUs, writing fast programs is hard!


