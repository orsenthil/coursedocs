Maximum Flow
============

*From Computability, Complexity & Algorithms — Charles Brubaker and Lance Fortnow*

* Source: https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6505/maximumflow.html

----

Flow Networks
-------------

A **flow network** is a directed graph :math:`G = (V, E)` with:

* A **source** vertex :math:`s` and a **sink** vertex :math:`t`.
* A **capacity function** :math:`c : E \to \mathbb{R}_{\geq 0}`.

.. figure:: images/maximumflow/FlowNetworkDef.png
   :alt: FlowNetworkDef

   Example flow network with source, sink, and capacity labels on edges.

A **flow** :math:`f : E \to \mathbb{R}_{\geq 0}` must satisfy:

1. **Capacity constraint:** :math:`0 \leq f(u,v) \leq c(u,v)` for all edges.
2. **Flow conservation:** for every internal vertex :math:`u \notin \{s, t\}`:

   .. math::

      \sum_{v} f(v, u) = \sum_{v} f(u, v)

3. **Anti-symmetry / single direction:** at most one direction carries flow between any pair.

.. figure:: images/maximumflow/FlowDef.png
   :alt: FlowDef

   Flow conservation illustrated at an internal vertex.

The **value** of flow :math:`f` is the total flow leaving :math:`s`:

.. math::

   |f| = \sum_{v} f(s, v)

.. figure:: images/maximumflow/FillInFlowQuiz.png
   :alt: FillInFlowQuiz

   *Quiz:* Calculate the missing flow values on a given network.

Network Modelling Tricks
~~~~~~~~~~~~~~~~~~~~~~~~

**Rational capacities:** Scale all capacities to integers; the algorithm still terminates.

.. figure:: images/maximumflow/RationalTrick.png
   :alt: RationalTrick

   Handling rational capacities by scaling to integers.

**Anti-parallel edges:** Replace :math:`(u,v)` and :math:`(v,u)` with an auxiliary vertex.

.. figure:: images/maximumflow/AntiparallelEdgeTrick.png
   :alt: AntiparallelEdgeTrick

   Converting anti-parallel edges using an intermediate vertex.

**Multiple sources/sinks:** Add a super-source :math:`s'` with infinite-capacity edges to
each source, and a super-sink :math:`t'` from each sink.

.. figure:: images/maximumflow/MultiSourceSinkTrick.png
   :alt: MultiSourceSinkTrick

   Super-source/super-sink construction for multi-commodity networks.

----

Ford-Fulkerson Method
---------------------

**Idea:** Repeatedly find a path from :math:`s` to :math:`t` in the **residual graph**
and push more flow along it.

Augmenting Flow
~~~~~~~~~~~~~~~

.. figure:: images/maximumflow/InitialFlow.png
   :alt: InitialFlow

   Starting flow configuration.

.. figure:: images/maximumflow/AugmentingFlow.png
   :alt: AugmentingFlow

   Augmenting flow (orange) added to increase the total flow value.

.. figure:: images/maximumflow/AugmentedFlow.png
   :alt: AugmentedFlow

   Result after combining initial and augmenting flows.

Residual Graph
~~~~~~~~~~~~~~

For each edge :math:`(u,v)` with capacity :math:`c(u,v)` and flow :math:`f(u,v)`,
define the **residual capacity**:

.. math::

   c_f(u,v) = c(u,v) - f(u,v) \qquad \text{(forward — remaining capacity)}

.. math::

   c_f(v,u) = f(u,v) \qquad \text{(backward — flow that can be cancelled)}

The **residual graph** :math:`G_f` contains all edges with positive residual capacity.

.. figure:: images/maximumflow/ResidualDef.png
   :alt: ResidualDef

   Residual capacity defined for forward and backward edges.

.. figure:: images/maximumflow/ResidualErrorsQuiz.png
   :alt: ResidualErrorsQuiz

   *Quiz:* Identify errors in a given residual network diagram.

.. figure:: images/maximumflow/AugmentationEg.png
   :alt: AugmentationEg

   Example: augmenting flows and combining them in the residual network.

Ford-Fulkerson Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/maximumflow/FordFulkerson.png
   :alt: FordFulkerson

   Ford-Fulkerson pseudocode.

.. code-block:: text

   f ← 0 (zero flow)
   while ∃ augmenting path p in G_f (s → t):
       push flow along p (bottleneck capacity)
       update G_f
   return f

.. figure:: images/maximumflow/FordFulkersonAnalysis.png
   :alt: FordFulkersonAnalysis

   Analysis: each augmentation increases :math:`|f|` by at least 1 (integer capacities),
   so at most :math:`|f^*|` iterations, each :math:`O(E)` → total :math:`O(E \cdot |f^*|)`.

**Limitation:** With poor path selection, this can be exponential in the capacity values.

----

Max-Flow Min-Cut Theorem
------------------------

An :math:`s`-:math:`t` **cut** partitions :math:`V` into sets :math:`A \ni s` and
:math:`B \ni t`. Its **capacity** is:

.. math::

   c(A, B) = \sum_{\substack{u \in A \\ v \in B}} c(u, v)

.. figure:: images/maximumflow/CutEg1.png
   :alt: CutEg1

   Example :math:`s`-:math:`t` cut — green vertices in :math:`A`, orange in :math:`B`.

.. figure:: images/maximumflow/CutEg2.png
   :alt: CutEg2

   Alternative :math:`s`-:math:`t` cut showing a different partition.

.. figure:: images/maximumflow/CutCapacityQuiz.png
   :alt: CutCapacityQuiz

   *Quiz:* Calculate the capacity of a given cut.

**Key inequality:** For any flow :math:`f` and any :math:`s`-:math:`t` cut :math:`(A,B)`:

.. math::

   |f| \leq c(A, B)

.. figure:: images/maximumflow/WillTheyMeet.png
   :alt: WillTheyMeet

   Flow value is bounded above by every cut capacity — will the bounds meet?

.. figure:: images/maximumflow/StrategyComplete.png
   :alt: StrategyComplete

   Strategy: show equivalence of max flow, no augmenting path, and min cut.

**Theorem (Max-Flow Min-Cut):** The following are equivalent:

1. :math:`f` is a maximum flow.
2. The residual graph :math:`G_f` has no :math:`s`-:math:`t` augmenting path.
3. There exists an :math:`s`-:math:`t` cut :math:`(A^*, B^*)` with :math:`c(A^*, B^*) = |f|`.

Proof Sketch
~~~~~~~~~~~~

Define :math:`A^*` as all vertices reachable from :math:`s` in :math:`G_f` when no
augmenting path exists:

.. figure:: images/maximumflow/ReachableCutQuiz.png
   :alt: ReachableCutQuiz

   *Quiz:* Determine flow properties across the reachable set.

.. figure:: images/maximumflow/ReachableCutEg.png
   :alt: ReachableCutEg

   Reachable set in :math:`G_f` defines a cut saturating all forward edges and
   cancelling all backward edges, giving :math:`|f| = c(A^*, B^*)`.

.. figure:: images/maximumflow/MaxFlowMinCutComplete.png
   :alt: MaxFlowMinCutComplete

   Complete proof diagram for the Max-Flow Min-Cut theorem.

**Conclusion:** Ford-Fulkerson terminates with a maximum flow.

----

Improved Algorithms
-------------------

Bad Augmentation Paths
~~~~~~~~~~~~~~~~~~~~~~

Naive path selection (e.g., DFS) can alternate between two paths and take
:math:`O(C)` iterations for maximum flow :math:`C`.

.. figure:: images/maximumflow/BadAugmentations.png
   :alt: BadAugmentations

   Adversarial example where poor path selection causes :math:`O(C)` augmentations.

Scaling Algorithm
~~~~~~~~~~~~~~~~~

Prioritise augmenting paths with **large bottleneck capacity** using a threshold
:math:`\Delta`:

.. figure:: images/maximumflow/ScalingAlgorithm.png
   :alt: ScalingAlgorithm

   Scaling algorithm pseudocode — only use paths with bottleneck :math:`\geq \Delta`.

.. figure:: images/maximumflow/ScalingAlgTheorem.png
   :alt: ScalingAlgTheorem

   **Theorem:** Scaling algorithm runs in :math:`O(E^2 \log C)` time.

Each scaling phase (halving :math:`\Delta`) has at most :math:`O(E)` augmentations,
and there are :math:`O(\log C)` phases.

Edmonds-Karp Algorithm
~~~~~~~~~~~~~~~~~~~~~~

Use **BFS** (shortest path in terms of number of edges) to select augmenting paths:

.. figure:: images/maximumflow/EdmondsKarpAlg.png
   :alt: EdmondsKarpAlg

   Edmonds-Karp pseudocode — Ford-Fulkerson with BFS path selection.

**Theorem:** Edmonds-Karp runs in :math:`O(VE^2)` time.

Key argument: the shortest augmenting path length is non-decreasing, and each edge
can be saturated at most :math:`O(V)` times before the shortest path through it grows.

Dinic's Algorithm
~~~~~~~~~~~~~~~~~

Build a **level graph** (BFS layers from :math:`s`), then find a **blocking flow**
(saturating all :math:`s`-:math:`t` paths in the level graph) before rebuilding:

.. figure:: images/maximumflow/LevelGraphEg.png
   :alt: LevelGraphEg

   Level graph constructed by BFS layers from the source.

.. figure:: images/maximumflow/OnlyBackEdges.png
   :alt: OnlyBackEdges

   After augmentation, only backward edges are added to the level graph — no new
   forward shortcuts are created.

.. figure:: images/maximumflow/OneEdgeSaturated.png
   :alt: OneEdgeSaturated

   Each augmentation saturates at least one edge, bounding work per phase.

.. figure:: images/maximumflow/DinicAlg.png
   :alt: DinicAlg

   Dinic's algorithm pseudocode with level-graph phases.

.. figure:: images/maximumflow/DinicAnalysis.png
   :alt: DinicAnalysis

   **Theorem:** Dinic's algorithm runs in :math:`O(V^2 E)` time.

Each phase takes :math:`O(VE)` (DFS blocking flow with dead-end elimination) and
there are at most :math:`O(V)` phases (shortest path length grows each phase).

----

Complexity Summary
------------------

.. list-table::
   :header-rows: 1
   :widths: 35 30 35

   * - Algorithm
     - Time Complexity
     - Notes
   * - Ford-Fulkerson
     - :math:`O(E \cdot |f^*|)`
     - Pseudo-polynomial; depends on max flow value
   * - Scaling
     - :math:`O(E^2 \log C)`
     - :math:`C` = max capacity
   * - Edmonds-Karp
     - :math:`O(VE^2)`
     - Strongly polynomial
   * - Dinic's
     - :math:`O(V^2 E)`
     - Strongly polynomial; faster in practice

----

Key Formulas
------------

**Residual capacity:**

.. math::

   c_f(u,v) = c(u,v) - f(u,v), \qquad c_f(v,u) = f(u,v)

**Flow conservation:**

.. math::

   \sum_{v} f(v, u) = \sum_{v} f(u, v) \quad \forall\, u \notin \{s, t\}

**Weak duality (flow** :math:`\leq` **cut):**

.. math::

   |f| \leq c(A, B) \quad \text{for any flow } f \text{ and cut } (A, B)

**Max-flow min-cut:**

.. math::

   \max_{f} |f| = \min_{(A,B)} c(A, B)

----

Further Reading
---------------

* Bipartite matching as max flow (unit capacities)
* Project selection / closure problems
* Gomory-Hu trees for all-pairs max flow
* Push-relabel algorithms: :math:`O(V^2 \sqrt{E})`
