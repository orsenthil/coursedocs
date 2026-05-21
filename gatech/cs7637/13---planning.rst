.. title: 13 - Planning 
.. slug: 13 - Planning 
.. date: 2016-01-23 06:43:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

=============
13 - Planning
=============

Planning Overview
-----------------

**Planning** is a method for action selection that uses the syntax of logic to specify goals, states, and operators for moving between states. Key concerns:

- When multiple goals exist, plans can conflict
- **Partial-order planning** detects and avoids conflicts between goals
- **Hierarchical task networks (HTNs)** enable planning at multiple levels of abstraction

States and Goals
----------------

States and goals are expressed in propositional logic:

- **Initial state**: ``On(Robot, Floor) ∧ Dry(Ladder) ∧ Dry(Ceiling)``
- **Goal state**: ``Painted(Ceiling) ∧ Painted(Ladder)``

The goal is fully specified by the initial state plus the desired goal state.

Operators
---------

Operators transform one state into another, specified by **preconditions** and **postconditions**:

- Preconditions: assertions that must be true before the operator can apply (by convention, only positive literals)
- Postconditions: assertions that become true after the operator applies (may include negative literals)

Example — Climb-Ladder:

- Precondition: ``On(Robot, Floor) ∧ Dry(Ladder)``
- Postcondition: ``On(Robot, Ladder)``

An operator is applicable if and only if its preconditions are satisfied in the current state. This notation originates from **STRIPS** (Stanford Research Institute Problem Solver), an early robot planner for the robot Shaky.

Planning and State Spaces
~~~~~~~~~~~~~~~~~~~~~~~~~

A plan is a sequence of states punctuated by operators. Each operator's preconditions match the preceding state, and its postconditions produce the succeeding state. Assertions from prior states propagate forward unless explicitly negated by an operator's postconditions.

Goals provide **control knowledge** — they help select which operator to apply. In means-ends analysis, you compare current and goal states, enumerate differences, and select operators to reduce the largest difference. Planning provides more systematic methods for operator selection.

Linear Planning and Goal Clobbering
------------------------------------

A **linear (simple) planner** treats goals independently and does not reason about conflicts. This leads to **goal clobbering**: achieving one goal creates conditions that prevent achieving another.

Example — painting a ceiling and a ladder:

1. If the robot paints the ladder first → ladder becomes wet → cannot climb it to paint ceiling
2. The plan for Painted(Ladder) clobbers the precondition Dry(Ladder) needed for Climb-Ladder in the Painted(Ceiling) plan

Partial-Order Planning
----------------------

**Partial-order planning** (nonlinear planning) addresses goal clobbering through three steps:

1. **Generate** independent plans for each goal
2. **Detect conflicts** — check if any state in Plan A clobbers a precondition of an operator in Plan B (and vice versa)
3. **Resolve conflicts** — promote or demote goals to establish a valid ordering

Conflict detection: compare each operator's preconditions against states in other plans. If a precondition (e.g., Dry(Ladder)) is contradicted by a state in another plan (e.g., ¬Dry(Ladder) after painting), a conflict exists.

Conflict resolution: reorder goals so the conflicting state occurs after the clobbered operator has already executed. If **open preconditions** arise after reordering (e.g., robot is on ladder but needs to be on floor), insert additional operators (e.g., Descend-Ladder) to bridge the gap.

Blocks world example:

- Initial: D on B, B on A, A on C, C on Table
- Goal: A on B, B on C, C on D, D on Table
- Operators: Move(x, y) with preconditions Clear(x) ∧ Clear(y); MoveToTable(x) with precondition Clear(x)
- Independent plans for each sub-goal conflict; partial-order planning detects and resolves the ordering

Key insights:

- Knowledge includes **control knowledge** (often tacit) for selecting operators
- Goals provide control knowledge
- Partial-order planning emerges from interaction of three micro-abilities: plan generation, conflict detection, conflict resolution (related to Minsky's "society of mind")

Hierarchical Task Network Planning
-----------------------------------

**Hierarchical planning** addresses complex problems by reasoning at multiple levels of abstraction. A **Hierarchical Task Network (HTN)** defines macro-operators that abstract sequences of primitive operations.

Example — sorting blocks:

- Primitive operations: Move(D, Table), Move(B, Table), Move(A, Table), Move(C, D), Move(B, C), Move(A, B)
- Macro-operators: ``Unstack`` (move all blocks to table), ``Stack-Ascending`` (stack in order)
- Each macro-operator has preconditions, postconditions, and an expansion into primitive moves

At any one level of abstraction, the problem appears small and simple. Knowledge at multiple abstraction levels is the key — this embodies the fundamental notion of knowledge-based AI.

Cognitive Connection
--------------------

Planning is central to cognition because action selection is central to cognition. Everyday decisions (where to eat, how to cook, what to do with a bonus) are all action-selection problems requiring planning.

Cognitive agents manage multiple goals with potential interactions — sometimes positive (achieving one enables another), sometimes negative (conflicts). Detecting and avoiding conflicts is a central cognitive process for achieving multiple goals simultaneously.
