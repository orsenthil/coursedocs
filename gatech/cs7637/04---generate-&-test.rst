.. title: 04 - Generate & Test 
.. slug: 04 - Generate & Test 
.. date: 2016-01-23 06:35:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

====================
04 - Generate & Test
====================

Overview
--------

**Generate and test** is a general-purpose problem-solving method:

1. **Generate** potential solutions to a problem
2. **Test** each solution for correctness or fitness
3. Accept, reject, or revise based on test results

If you had complete and correct world knowledge, infinite computational resources, and a guaranteed-correct reasoning method, you could generate the optimal solution directly without testing. In practice, none of these hold, so you generate plausible solutions and test them.

Applying Generate and Test
--------------------------

Using the Guards and Prisoners problem as an example:

A **generator** takes the current state and produces all possible successor states. A **tester** evaluates each successor and removes illegal or unproductive ones.

With a **dumb generator** (generates all possible states) and **dumb tester** (only checks the constraint that prisoners cannot outnumber guards):

- From the initial state (3 guards, 3 prisoners, boat on left), the generator produces 5 successor states
- The tester eliminates states violating the prisoner-guard constraint
- Remaining legal states are expanded further

Problem: iterating with dumb generator + dumb tester causes **combinatorial explosion** — the state space grows rapidly because previously visited states are regenerated.

Smart Testers and Smart Generators
----------------------------------

The balance of intelligence can shift between generator and tester:

**Smart tester** — Detects when a generated state is identical to a previously visited state and prunes it. This eliminates cycles and collapses the search tree to the same compact graph we derived from semantic network analysis alone.

**Smart generator** — Avoids generating previously visited or illegal states in the first place, preventing wasted computation.

Key insight: the knowledge representation alone does not solve problems. A **problem-solving method** (like generate and test) must be coupled with the representation. Semantic networks provide the knowledge structure; generate and test provides the reasoning strategy. More than one problem-solving method (or variation) can be applied to the same knowledge representation.

For small problems, the balance between generator and tester intelligence matters little. For problems with millions of states, it becomes critical.

**Genetic algorithms** are an instance of generate and test: recombination and mutation generate candidate solutions, and a fitness function tests them. They are effective for many large problems but inherently inefficient because neither generator nor tester encodes deep domain knowledge.

Generate and Test for Raven's Problems
--------------------------------------

Raven's matrix problems present a more complex generate-and-test challenge than Guards and Prisoners because transformations are **continuous** rather than discrete — a shape can be displaced by varying amounts, resized by varying percentages, etc. The space of possibilities is enormous, making smart generators and testers essential.

Two strategies for applying generate and test:

1. **Generate-then-match** — Infer the A→B transformation, apply it to C to generate a candidate D, then test the candidate against the six answer choices to find the closest match
2. **Test-each-candidate** — Place each answer choice (1–6) into D, compute the C→D transformation for each, and test which C→D transformation best matches the A→B transformation

Semantic networks help enormously here because they abstract away continuous variation. Instead of tracking exact pixel displacements and sizes, the representation captures discrete relationships: "y expanded," "z deleted," "x unchanged." This level of abstraction makes generate and test tractable — the problem-solving method doesn't need to worry about details below the representation's abstraction level.

If the best match doesn't meet a confidence threshold, the agent can backtrack and consider alternative transformations (e.g., reconsider whether the outer or inner shape was the one that changed).

The Cognitive Connection
------------------------

Humans use generate and test constantly — we generate candidate solutions and test them because we lack complete knowledge, infinite resources, and guaranteed-correct reasoning. This method connects not only to human cognition but also to **biological evolution**: genetic algorithms (crossover, mutation, fitness testing) are a direct computational analog of evolutionary generate-and-test.
