Logic and Planning
==================

Propositional Logic
-------------------

Truth Tables
~~~~~~~~~~~~

Standard truth table for logical connectives:

=  =  =======  ======  ===========  ==========  =============
P  Q  P AND Q  P OR Q  P IMPLIES Q  P IFF Q     NOT P
=  =  =======  ======  ===========  ==========  =============
T  T  T        T       T            T            F
T  F  F        T       F            F            F
F  T  F        T       T            F            T
F  F  F        F       T            T            T
=  =  =======  ======  ===========  ==========  =============

Key equivalences:

- :math:`P \Rightarrow Q \equiv \neg P \lor Q`
- :math:`P \Leftrightarrow Q \equiv (P \Rightarrow Q) \land (Q \Rightarrow P)`
- De Morgan's: :math:`\neg(P \land Q) \equiv \neg P \lor \neg Q`

Terminology
~~~~~~~~~~~

- **Valid sentence (tautology)**: True under every interpretation (e.g., :math:`P \lor \neg P`).
- **Satisfiable**: True under at least one interpretation.
- **Unsatisfiable**: True under no interpretation (e.g., :math:`P \land \neg P`).
- **Model**: An assignment of truth values that makes a sentence true.

Limitations of Propositional Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Cannot express relations between objects or quantify over them.
- Number of propositions explodes for domains with many objects.
- No way to say "for all X" or "there exists an X" — motivates first-order logic.

First-Order Logic
-----------------

FOL extends propositional logic with **constants**, **predicates**, **functions**, and **quantifiers**.

Syntax
~~~~~~

- **Constants**: objects in the domain (e.g., ``John``, ``2``).
- **Predicates**: properties or relations (e.g., ``Mortal(X)``, ``GreaterThan(X, Y)``).
- **Functions**: mappings from objects to objects (e.g., ``MotherOf(X)``).
- **Quantifiers**:

  - Universal: :math:`\forall x\; P(x)` — "for all x, P(x) holds."
  - Existential: :math:`\exists x\; P(x)` — "there exists an x such that P(x) holds."

- **Negation of quantifiers**: :math:`\neg \forall x\; P(x) \equiv \exists x\; \neg P(x)`

Models in FOL
~~~~~~~~~~~~~

A model specifies a domain of objects, an interpretation for each constant, predicate, and function symbol. A sentence is true in a model if every possible variable assignment satisfies it.

Vacuum World Example
~~~~~~~~~~~~~~~~~~~~

Representing a simple vacuum world in FOL:

- ``At(Vacuum, Location)`` — vacuum is at a location.
- ``Dirty(Location)`` — location is dirty.
- Actions: ``Suck``, ``Left``, ``Right``.

Higher-Order Logic
~~~~~~~~~~~~~~~~~~

Allows quantification over predicates and functions (not just objects). More expressive than FOL but undecidable in general. FOL with equality is semi-decidable.

Unification and Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Unification**: finding a substitution that makes two FOL expressions identical. Used in resolution-based theorem proving.
- **Resolution**: refutation-complete inference rule. To prove :math:`KB \models \alpha`, show :math:`KB \land \neg\alpha` is unsatisfiable by deriving the empty clause.

Planning
--------

Problem Solving vs. Planning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Problem solving** (search): states are atomic, actions are sequences, no internal structure.
- **Planning**: states have internal structure (sets of logical sentences), actions have preconditions and effects, can reason about sub-goals independently.

Planning vs. Execution
~~~~~~~~~~~~~~~~~~~~~~

Real-world complicates planning due to:

- **Stochastic environments**: actions may have uncertain outcomes.
- **Partial observability**: agent may not know full state.
- **Multi-agent**: other agents affect the environment.
- **Unknown environments**: model may be incomplete.

Approaches by environment type:

- **Sensorless (conformant) planning**: find a plan that works regardless of initial state or observations.
- **Partially observable**: maintain a belief state, interleave planning with observation.
- **Stochastic**: use contingency plans with branching (AND-OR search).

Belief State and Predict-Update Cycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Predict**: apply action to each state in belief state to get new belief state.
- **Update**: incorporate observation to narrow belief state.
- Handles partial observability and nondeterminism.

Classical Planning
------------------

State-space representation using propositional fluents (Boolean variables that change over time).

STRIPS Representation
~~~~~~~~~~~~~~~~~~~~~

An action schema has:

- **Preconditions**: conjunctive conditions that must hold before execution.
- **Add list (effects+)**: fluents that become true after execution.
- **Delete list (effects-)**: fluents that become false after execution.

Example — ``Fly(p, from, to)``:

- Precond: ``At(p, from) ∧ Plane(p) ∧ Airport(from) ∧ Airport(to)``
- Effect: ``¬At(p, from) ∧ At(p, to)``

Search Strategies
~~~~~~~~~~~~~~~~~

**Progression (forward search)**:
  Start from initial state, apply actions whose preconditions are met, search toward goal. Complete but may explore irrelevant actions.

**Regression (backward search)**:
  Start from goal, find actions whose effects satisfy (part of) the goal, regress to their preconditions. Focuses search on relevant actions only.

**Plan-space search (partial-order planning)**:
  Search through space of partial plans rather than states. Add actions and ordering constraints to resolve open preconditions and threats. Allows least-commitment — don't order actions unless necessary.

Heuristics for Planning
~~~~~~~~~~~~~~~~~~~~~~~

- **Ignore delete lists**: solve relaxed problem (never undo progress). Gives admissible heuristic.
- **Sub-goal independence**: sum cost of achieving each goal independently. Inadmissible if sub-goals interact.

Situation Calculus
------------------

Represents planning in FOL by encoding situations (histories of actions) as terms.

- **Situation**: a sequence of actions from the initial situation :math:`S_0`.
- ``Result(a, s)`` — situation resulting from doing action ``a`` in situation ``s``.
- **Successor-state axiom**: specifies when a fluent holds after an action, handling the frame problem.

Example: :math:`Poss(Move(x, y), s) \Leftrightarrow At(Agent, x, s) \land Adjacent(x, y)`

The **frame problem**: representing everything that does *not* change after an action. Successor-state axioms solve this by specifying exactly when each fluent changes.
