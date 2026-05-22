Constraint Satisfaction
=======================

CSP Fundamentals
----------------

Definition
~~~~~~~~~~

A **Constraint Satisfaction Problem** is defined by:

- **Variables**: :math:`X = \{X_1, X_2, \ldots, X_n\}`
- **Domains**: :math:`D_i` for each variable (set of possible values)
- **Constraints**: relations restricting combinations of values

A **solution** is an assignment of values to all variables that satisfies every constraint.

Types of constraints:

- **Unary**: restricts a single variable (e.g., :math:`X_1 \neq \text{red}`).
- **Binary**: relates two variables (e.g., :math:`X_1 \neq X_2`).
- **Higher-order (global)**: involves three or more variables (represented via constraint hypergraph).
- **Preference (soft) constraints**: define optimization problems, solvable via linear programming.

Map Coloring Example
~~~~~~~~~~~~~~~~~~~~

- **Variables**: regions (e.g., WA, NT, SA, Q, NSW, V, T for Australia).
- **Domains**: {Red, Green, Blue}.
- **Constraints**: adjacent regions must have different colors.
- **Constraint graph**: nodes = variables, edges = binary constraints.

Backtracking Search
-------------------

Basic Algorithm
~~~~~~~~~~~~~~~

Depth-first search with one variable assigned per level:

1. Select an unassigned variable.
2. Try each value in its domain.
3. If consistent with constraints, recurse.
4. If no value works, **backtrack** to the previous variable.

Complexity: :math:`O(d^n)` in the worst case for :math:`n` variables with domain size :math:`d`.

Variable Ordering — MRV
~~~~~~~~~~~~~~~~~~~~~~~~

**Minimum Remaining Values (MRV)**: choose the variable with the fewest legal values remaining. Fails early on constrained variables ("fail-first" strategy).

**Degree heuristic** (tiebreaker): among MRV-tied variables, choose the one involved in the most constraints on unassigned variables.

Value Ordering — LCV
~~~~~~~~~~~~~~~~~~~~

**Least Constraining Value (LCV)**: choose the value that rules out the fewest choices for neighboring variables. Maximizes future flexibility ("fail-last" for values).

Forward Checking
~~~~~~~~~~~~~~~~

After assigning a variable, immediately remove inconsistent values from the domains of neighboring unassigned variables.

- Acts as an early warning system: if any neighbor's domain becomes empty, backtrack immediately.
- Detects failure earlier than plain backtracking.

Constraint Propagation and Arc Consistency
------------------------------------------

Arc Consistency (AC-3)
~~~~~~~~~~~~~~~~~~~~~~

An arc :math:`(X_i, X_j)` is **arc-consistent** if for every value in :math:`D_i`, there exists a consistent value in :math:`D_j`.

**AC-3 algorithm**:

1. Initialize queue with all arcs.
2. For each arc :math:`(X_i, X_j)`, remove values from :math:`D_i` that have no support in :math:`D_j`.
3. If :math:`D_i` changed, re-enqueue all arcs :math:`(X_k, X_i)` where :math:`k \neq j`.
4. If any domain becomes empty, the CSP has no solution.

Complexity: :math:`O(ed^3)` where :math:`e` = number of arcs, :math:`d` = max domain size.

Forward checking is a restricted form of arc consistency (only checks arcs from assigned to unassigned variables).

Structured CSPs
---------------

- If the constraint graph is a **tree** (no loops), the CSP can be solved in :math:`O(nd^2)` time.
- **Algorithm**: choose a root, apply directed arc consistency from leaves to root (topological order), then assign values from root to leaves.
- For non-tree graphs: **tree decomposition** or **cutset conditioning** to exploit near-tree structure.

Reference: `Topological Search (U. Washington) <https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf>`_

Iterative (Local Search) Methods
---------------------------------

**Min-Conflicts algorithm**:

1. Start with a complete random assignment.
2. Select a variable that violates a constraint.
3. Reassign it to the value that minimizes the number of conflicts.
4. Repeat until solution found or max iterations reached.

Effective for large CSPs (e.g., million-queens). Typically solves n-Queens in roughly :math:`O(n)` steps.
