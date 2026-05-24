Search
======

* http://norvig.com/

Problem Solving
---------------

Search problems arise when an agent must find a sequence of actions to reach a goal.
Complexity stems from two sources:

* **Many choices** — large branching factor at each state
* **Partial observability** — the agent may not see the full state

Example: finding a route from Arad to Bucharest on the Romania road map.

Problem Definition
~~~~~~~~~~~~~~~~~~

A search problem is formally defined by five components:

* **Initial State** — starting configuration
* **Actions(s)** → {a1, a2, a3, ...} — actions available in state *s*
* **Result(s, a)** → s' — transition model
* **GoalTest(s)** → T | F — is this a goal state?
* **Path Cost** — cumulative cost of the path (sum of step costs)

Tree Search
-----------

A **tree search** generates successors from the frontier without tracking visited states.
It can revisit the same state via different paths, potentially looping.

**Algorithm sketch:**

::

    function TREE-SEARCH(problem):
        frontier = {initial state}
        loop:
            if frontier is empty: return failure
            choose a leaf node and remove from frontier
            if node is a goal: return solution
            expand node, add resulting nodes to frontier

Graph Search
~~~~~~~~~~~~

Graph search adds an **explored set** (closed list). A state is expanded at most once,
preventing the redundant expansion that tree search suffers from.

::

    function GRAPH-SEARCH(problem):
        frontier = {initial state}
        explored = {}
        loop:
            if frontier is empty: return failure
            choose a leaf node and remove from frontier
            if node is a goal: return solution
            add node to explored
            expand node, add successors to frontier if not in explored or frontier

Uninformed Search Strategies
----------------------------

Breadth-First Search (BFS)
~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Frontier:** FIFO queue
* **Complete:** Yes (if branching factor *b* is finite)
* **Optimal:** Yes when all step costs are equal
* **Time:** O(b^d)
* **Space:** O(b^d) — every node at the goal depth may be in memory

Depth-First Search (DFS)
~~~~~~~~~~~~~~~~~~~~~~~~~

* **Frontier:** LIFO stack (or recursion)
* **Complete:** No (can loop in infinite state spaces; yes with graph search in finite spaces)
* **Optimal:** No
* **Time:** O(b^m), where *m* is maximum depth
* **Space:** O(b·m) — linear in the depth of the deepest path

Uniform Cost Search (UCS)
~~~~~~~~~~~~~~~~~~~~~~~~~

* Expands the node with the **lowest path cost** g(n).
* **Frontier:** priority queue ordered by g(n).
* Equivalent to BFS when all step costs are equal.
* **Complete:** Yes (if every step cost ≥ ε > 0)
* **Optimal:** Yes

Search Strategy Comparison
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+----------+----------+---------+---------+
| Criterion         | BFS      | DFS      | UCS     | IDS     |
+===================+==========+==========+=========+=========+
| Complete?         | Yes      | No       | Yes     | Yes     |
+-------------------+----------+----------+---------+---------+
| Optimal?          | Yes*     | No       | Yes     | Yes*    |
+-------------------+----------+----------+---------+---------+
| Time              | O(b^d)   | O(b^m)   | O(b^C)  | O(b^d)  |
+-------------------+----------+----------+---------+---------+
| Space             | O(b^d)   | O(b·m)   | O(b^C)  | O(b·d)  |
+-------------------+----------+----------+---------+---------+

\*When all step costs are equal. C = ⌈C*/ε⌉ for UCS, where C* is optimal cost.

Informed (Heuristic) Search
---------------------------

Greedy Best-First Search
~~~~~~~~~~~~~~~~~~~~~~~~

* Expands the node that appears **closest to the goal** using heuristic h(n).
* **Not optimal** — ignores path cost already incurred.
* **Not complete** — can loop.

A* Search
~~~~~~~~~

Combines uniform cost and greedy best-first:

  **f(n) = g(n) + h(n)**

* g(n) = cost from start to *n*
* h(n) = estimated cost from *n* to goal
* A* is **optimal** when h is admissible (tree search) or consistent (graph search).
* A* is **optimally efficient** — no other optimal algorithm expands fewer nodes.

Admissible Heuristic
~~~~~~~~~~~~~~~~~~~~

A heuristic h is **admissible** if it never overestimates the true cost:

  h(s) ≤ true cost to goal from *s*

Properties:

* h must be **optimistic**
* h(goal) = 0
* Admissibility guarantees A* optimality in tree search

Consistent (Monotone) Heuristic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

h is **consistent** if for every node *n* and successor *n'* via action *a*:

  h(n) ≤ c(n, a, n') + h(n')

Consistency implies admissibility. Guarantees A* optimality in graph search.

State Spaces
------------

Example: vacuum world with two locations (A, B).

* Robot position: A or B → 2 states
* Location A dirty or clean → 2 states
* Location B dirty or clean → 2 states
* **Total:** 2 × 2 × 2 = **8 state spaces**

With partial observability or stochastic actions, the agent must reason over
**belief states** (sets of possible states).

Sliding Blocks Puzzle
---------------------

Heuristics for the 15-puzzle:

* **h₁ = misplaced tiles** — counts tiles not in goal position (admissible)
* **h₂ = Manhattan distance** — sum of each tile's horizontal + vertical distance from goal (admissible, dominates h₁)
* Relaxed problems: removing constraints generates admissible heuristics automatically.

Tri-Directional Search
----------------------

Challenge: find optimal meeting point of three simultaneous A* searches.
Uses tri-directional A* on a road network graph.

Rubik's Cube Search
-------------------

* `Finding Optimal Solutions to Rubik's Cube Using Pattern Databases`_ — Korf uses pattern databases as admissible heuristics.
* `God's Number is 26 in the Quarter-Turn Metric`_ — every position solvable in ≤ 26 quarter turns.

.. _Finding Optimal Solutions to Rubik's Cube Using Pattern Databases: https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf
.. _God's Number is 26 in the Quarter-Turn Metric: http://www.cube20.org/qtm/

Problems with Search
--------------------

* Search algorithms can face **exponential blowup** in large or infinite state spaces.
* Practical implementations require careful data structure choices for the frontier
  (e.g., priority queues with decrease-key for A*) and efficient explored-set lookups
  (e.g., hash sets).

References
----------

* Korf, 1997, `Finding Optimal Solutions to Rubik's Cube Using Pattern Databases`_
* Goldberg, 2011. `Reach for A* An Efficient Point-to-Point Shortest Path Algorithm`_
* Goldberg & Harrelson, March 2003. `Computing the Shortest Path A* Search Meets Graph Theory.`_
* Gutman, 2004. `Reach-based Routing A New Approach to Shortest Path Algorithms Optimized for Road Networks.`_

.. _Reach for A* An Efficient Point-to-Point Shortest Path Algorithm: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/02-search-01-Astart-ALT-Reach.pdf
.. _Computing the Shortest Path A* Search Meets Graph Theory.: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/02-search-Goldberg03tr.pdf
.. _Reach-based Routing A New Approach to Shortest Path Algorithms Optimized for Road Networks.: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/02-search-Gutman04siam.pdf
