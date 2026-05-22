.. title: Logic
.. slug: Logic
.. date: 2016-01-23 06:42:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Logic
=====

Why Formal Logic
----------------

A logic-based AI agent has two parts:

1. **Knowledge base** — sentences in the language of logic representing the agent's knowledge of the world
2. **Inference engine** — applies rules of inference to the knowledge base

Two key guarantees of a logical inference system:

- **Soundness** — rules of inference derive only valid conclusions
- **Completeness** — rules of inference derive all valid conclusions

Logic provides provably correct solutions, which is why it has been central to AI since the field's inception. However, this course focuses primarily on conceptual, experiential, and heuristic knowledge, using logic mainly as a foundation for methods like planning.

Predicates
----------

A **predicate** is a function that maps object arguments to true or false. Examples:

- ``Feathers(Bluebird)`` → true (bluebird has feathers)
- ``Feathers(Animal)`` → true or false depending on the animal

Implicative sentences capture relationships between predicates:

- ``Feathers(Animal) → Bird(Animal)`` — if the animal has feathers, then it is a bird

Conjunctions, Disjunctions, and Negation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Conjunction** (AND): ``Lays-eggs(x) ∧ Flies(x) → Bird(x)``
- **Disjunction** (OR): ``Lays-eggs(x) ∨ Flies(x) → Bird(x)``
- **Negation** (NOT): ``Flies(x) ∧ ¬Bird(x) → Bat(x)``

Implication Elimination
~~~~~~~~~~~~~~~~~~~~~~~

``A → B`` can be rewritten as ``¬A ∨ B``. Example: ``Feathers → Bird`` becomes ``¬Feathers ∨ Bird``. This rewrite is essential for converting sentences to conjunctive normal form.

Truth Tables and Properties
---------------------------

Truth tables determine the truth value of complex sentences from their component predicates. Key properties:

- **Commutative**: ``A ∧ B ≡ B ∧ A``
- **Distributive**: ``A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C)``
- **Associative**: ``(A ∧ B) ∧ C ≡ A ∧ (B ∧ C)``
- **De Morgan's Law**: ``¬(A ∧ B) ≡ ¬A ∨ ¬B`` and ``¬(A ∨ B) ≡ ¬A ∧ ¬B``

These properties enable rewriting sentences into forms amenable to inference rules.

Truth of Implications
~~~~~~~~~~~~~~~~~~~~~

An implication ``A → B`` is false only when A is true and B is false. If A is false, the implication is true regardless of B (we cannot make a determination about B from a false antecedent).

Rules of Inference
------------------

- **Modus Ponens**: If ``P → Q`` and ``P``, then ``Q``
- **Modus Tollens**: If ``P → Q`` and ``¬Q``, then ``¬P``

Example: Given "feathers → bird" and "Harry has feathers," conclude "Harry is a bird" (Modus Ponens). Given "feathers → bird" and "Buzz is not a bird," conclude "Buzz does not have feathers" (Modus Tollens).

While truth tables and simple inference rules work in principle, they are computationally infeasible for large knowledge bases — truth tables grow exponentially, and the search space of inference chains becomes enormous.

Quantifiers
-----------

**Propositional logic** (zeroth-order) has no variables. **Predicate calculus** (first-order logic) introduces:

- **Universal quantifier** (∀): ``∀x: Lays-eggs(x) ∧ Flies(x) → Bird(x)`` — for all x
- **Existential quantifier** (∃): ``∃y: Lays-eggs(y) ∧ Flies(y) → Bird(y)`` — there exists at least one y

Universal quantification compresses what would otherwise be many propositional sentences into one.

Resolution Theorem Proving
--------------------------

**Resolution theorem proving** is a computationally efficient method for proving sentences in logic, using proof by refutation.

Algorithm:

1. Convert all sentences in the knowledge base to **conjunctive normal form** (CNF) — literals, disjunctions of literals, or conjunctions of disjunctions
2. Negate what you want to prove and add it as a new sentence
3. Repeatedly resolve: find complementary literals (P and ¬P) across sentences, eliminate them
4. If you reach the **null clause** (empty/contradiction), the original negation is false, so the theorem is proved

Simple example (robot proving a box is not liftable):

- S1: ``¬Can-move → ¬Liftable`` becomes ``Can-move ∨ ¬Liftable`` (implication elimination)
- S2: ``¬Can-move`` (from perception)
- S3: ``Liftable`` (negation of goal ``¬Liftable``)
- Resolve S3 with S1 on Liftable/¬Liftable → leaves ``Can-move``
- Resolve with S2 on Can-move/¬Can-move → null (contradiction)
- Therefore ``¬Liftable`` is proved

Complex example (adding battery check):

- S1: ``¬Can-move ∧ Battery-full → ¬Liftable`` becomes ``Can-move ∨ ¬Battery-full ∨ ¬Liftable`` (implication elimination + De Morgan's)
- S2: ``¬Can-move``, S3: ``Battery-full``, S4: ``Liftable`` (negation of goal)
- Resolve S4 with S1 on Liftable → leaves ``Can-move ∨ ¬Battery-full``
- Resolve with S3 on Battery-full → leaves ``Can-move``
- Resolve with S2 → null (contradiction). Proved.

Horn Clauses and Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A **horn clause** is a disjunction containing at most one positive literal. When all sentences are horn clauses, resolution theorem proving gains computational efficiency through clear focus of attention — always begin with the literal to prove, find its negation, resolve, and proceed with the remainder.

Cognitive Connection
--------------------

Logic is important in AI for providing precise reasoning and formal notation. However, human reasoning is often **inductive** (generalizing from samples) or **abductive** (reasoning from effects to causes, e.g., doctor diagnosing from symptoms) rather than purely deductive (reasoning from causes to effects). Behavior may appear logical without logic being the underlying mechanism — analogical reasoning can produce logically consistent results without using formal logic.
