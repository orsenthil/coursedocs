.. title: 05 - Means-End Analysis 
.. slug: 05 - Means-End Analysis 
.. date: 2016-01-23 06:36:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

=======================
05 - Means-End Analysis
=======================

State Spaces
------------

Problem solving can be framed as navigation through a **state space**:

- **Initial state** — The starting configuration
- **Goal state** — The desired configuration
- **Operators** — Actions that transform one state into another
- **Path** — A sequence of operators leading from initial to goal state

Example — the **blocks world problem**: Three blocks (A, B, C) on a table. Initial state: A on table, B on table, C on A. Goal state: C on table, B on C, A on B. Constraints: move only one block at a time; can only move a block with nothing on top of it.

Available operators move a block to a location (e.g., "move C to table," "move B onto C"). The solution is a path: move C to table → move B onto C → move A onto B.

Means-End Analysis
------------------

**Means-end analysis** selects operators by measuring which one most reduces the **difference** (distance) between the current state and the goal state:

1. Compare the current state to the goal state
2. Identify the differences between them
3. For each applicable operator, compute the resulting state's difference from the goal
4. Select the operator that minimizes this difference

The "means" are the operators applied; the "end" is the goal state. The method iteratively reduces differences until the goal is reached (difference = 0).

Blocks world example (3 blocks):

- Initial state has 3 differences from the goal
- "Move C to table" reduces differences to 2
- "Move B onto C" reduces differences to 1
- "Move A onto B" reduces differences to 0

When multiple operators reduce distance equally, means-end analysis alone cannot decide between them — additional methods (e.g., planning) are needed.

Limitations of Means-End Analysis
---------------------------------

With a more complex blocks world (4 blocks: A, B, C, D), means-end analysis can:

- **Get stuck** — Reach states where no operator reduces the distance to the goal
- **Enter loops** — Revisit previously explored states
- **Miss optimal paths** — The greedy choice at each step doesn't guarantee a globally optimal solution

Means-end analysis is a **universal (weak) method**: applicable to a very large class of problems, but provides no guarantees of success, computational efficiency, or solution optimality. Its power lies in broad applicability rather than deep domain-specific reasoning.

Problem Reduction
-----------------

**Problem reduction** decomposes a hard problem into smaller, simpler subproblems:

1. **Decompose** the goal into subgoals
2. **Solve** each subgoal independently (potentially using means-end analysis)
3. **Compose** the sub-solutions into a solution for the whole problem

Example: In the 4-block problem where means-end analysis stalled, decompose the goal (A on B, B on C, C on D, D on table) into subgoals. Attack one subgoal at a time — e.g., first achieve "C on D," then "B on C," then "A on B."

When solving a subgoal, focus only on the blocks relevant to that subgoal and ignore the rest. This reduces the effective state space.

Problem reduction is itself a universal method — broadly applicable but without guarantees of success. One of knowledge's fundamental roles is telling you *how* to decompose a hard problem into simpler ones.

Combining Methods for Raven's Problems
---------------------------------------

Complex problems often require combining multiple methods:

- **Problem reduction** breaks a Raven's matrix into sub-problems (e.g., individual transformations between frames)
- **Means-end analysis** drives toward a target transformation by reducing the difference between the current and desired representations
- **Generate and test** produces candidate answers and tests them against the available choices

All three methods can use the same **semantic network** knowledge representation. The coupling between these universal methods and the representation is **weak** — the methods don't demand specific knowledge structures, and the representation doesn't dictate a specific method. This is why they are called **weak methods**.

Later in the course, **strong methods** will be introduced where knowledge and problem-solving strategy are tightly coupled — knowledge affords specific inferences, and inferences demand specific knowledge. Strong methods are more efficient but require domain knowledge that isn't always available.

The Cognitive Connection
------------------------

**Weak methods** (generate and test, means-end analysis, problem reduction) make little use of domain knowledge. **Strong methods** are knowledge-intensive and produce good solutions efficiently, but require expertise.

Humans use weak methods when working in unfamiliar domains where they lack expertise. In domains where they are experts, humans tend to use knowledge-intensive methods that leverage their deep understanding of the world. This distinction between novice and expert problem-solving — weak general methods vs. strong specialized ones — is a key theme in cognitive science and KBAI.
