Instance Based Learning
=======================

Revision reference for **lazy learning**, **k-NN**, complexity, biases, and the **curse of dimensionality**. (ML textbook Ch. 8)

Eager vs Lazy Learning
----------------------

**Eager learners** (e.g., linear regression): learn a compact function f from training data (x,y pairs), then discard data; query = f(x).

**Lazy / instance-based learners**: store all training data; defer computation to query time.

+----------------------------+------------------------------------------+
| **Lazy advantages**        | **Lazy disadvantages**                   |
+============================+==========================================+
| Exact recall of seen points| No generalization for unseen x           |
+----------------------------+------------------------------------------+
| No training phase          | Sensitive to noise (memorization)        |
+----------------------------+------------------------------------------+
| Simple                     | Duplicate x with different y → ambiguous |
+----------------------------+------------------------------------------+

**Lookup baseline**: F(x) = database lookup(x) — exact match only; no generalization.

1-Nearest Neighbor
------------------

For unseen query q: label = label of **nearest** training point (by distance metric).

- Works when **locality** holds (e.g., house prices by map location).
- Fails when neighbors disagree (boundary / ambiguous regions).

**Georgia Tech housing example**: classify house price (red/blue/green) by map location.

- Black query near green cluster → 1-NN → green ✓
- Black query in red cluster → 1-NN → red ✓
- Black query between red, blue, green → **1-NN ambiguous** → use **k > 1**

k-Nearest Neighbor (k-NN)
-------------------------

**Algorithm** (pseudocode):

1. Given training set D, distance metric, integer k, query q.
2. Find set NN = k training points closest to q (break ties: include all at k-th distance).
3. **Classification**: return **mode** (plurality vote) of labels in NN.
4. **Regression**: return **mean** of y values in NN.

**Pseudocode**:

.. code-block:: text

   KNN(D, dist, k, q):
     NN = {k points in D with smallest dist(·, q)}  # tie-break: all at k-th distance
     if classification: return mode({y : (x,y) in NN})
     if regression:    return mean({y : (x,y) in NN})

**Tie-breaking** (classification): pick alphabetically, random, or global label frequency.

**Free parameters** (domain knowledge):

- **k**: number of neighbors (k=1 brittle; larger k smoother).
- **Distance / similarity metric**: how "near" is defined.

**Variants**:

- **Weighted vote / average**: weight by 1/distance (closer neighbors matter more).
- k = n with weighted average still varies by query location (not constant function).

Distance Metrics
----------------

- **Euclidean** (L2): √(Σ(x_i − q_i)²) — order preserved without sqrt for ranking.
- **Manhattan** (L1): Σ|x_i − q_i|
- **Weighted distances**: scale dimensions differently (addresses unequal feature importance).
- **Discrete / mixed features**: mismatch counts, domain-specific similarity (images, etc.).

Distance = **domain knowledge**; wrong metric → poor performance regardless of k.

Complexity (1-D, sorted data, n points)
---------------------------------------

+-------------------+-------------+-------------+-------------+-------------+
|                   | 1-NN learn  | 1-NN query  | k-NN query  | Lin. reg.   |
+===================+=============+=============+=============+=============+
| **Time**          | O(1)        | O(log n)    | O(log n + k)| O(n) learn  |
+-------------------+-------------+-------------+-------------+-------------+
|                   |             |             |             | O(1) query  |
+-------------------+-------------+-------------+-------------+-------------+
| **Space (model)** | O(n)        | O(1) query  | O(1) query  | O(1)        |
+-------------------+-------------+-------------+-------------+-------------+

- Unsorted 1-D: nearest neighbor scan O(n).
- **Trade-off**: lazy = cheap learn, cost at query; eager = pay once, cheap queries.
- If querying >> n times, eager can win overall.

**Lazy vs eager**: nearest-neighbor = **lazy** (procrastinate until query); linear regression = **eager** (learn upfront).

**k-NN in higher dimensions**: brute-force query O(n) per query; spatial data structures (k-d trees) help low d but degrade in high d.

Domain Knowledge Example
------------------------

True function: y = x₁² + x₂. Query (4, 2) → true y = **18**.

+------------------+------------------+
| Method           | Prediction       |
+==================+==================+
| 1-NN Euclidean   | 8                |
+------------------+------------------+
| 3-NN Euclidean   | 42               |
+------------------+------------------+
| 1-NN Manhattan   | 29               |
+------------------+------------------+
| 3-NN Manhattan   | 35.5             |
+------------------+------------------+
| Custom (sq x₁)   | ~12 (closer)     |
+------------------+------------------+

**Lesson**: k, metric, and weighting encode assumptions; none matched the true function here — yet k-NN often works well when biases align with the domain.

k-NN Preference Biases
----------------------

1. **Locality**: nearby points are similar (via chosen metric).
2. **Smoothness**: averaging/voting assumes labels change smoothly over space.
3. **Equal feature relevance**: standard L1/L2 treat all dimensions equally — bad when features have different scales or importance (e.g., x₁² vs x₁ in target function).

Optimal distance metric exists per fixed problem but may be hard to find; oracle metric (same label → distance 0) requires solving the problem.

Curse of Dimensionality
-----------------------

**Bellman's curse of dimensionality**: as dimensionality d grows, data needed to generalize grows **exponentially** (~10^d points to maintain fixed neighborhood coverage).

- 1-D line: 10 points cover 1/10 each.
- 2-D square: need ~100 points (10×10 grid) for same local density.
- d dimensions: ~10^d points.

**Implications for k-NN**:

- "Nearest" neighbors become **far** in high dimensions → weak locality.
- Irrelevant features dilute signal (all features weighted equally by default).
- Adding features without more data **hurts** generalization.

**Mitigations**: feature selection, weighted metrics, dimensionality reduction (covered later in course).

Locally Weighted Regression
---------------------------

Replace simple mean with **local model** fit on neighbors:

- Weight neighbors by similarity (e.g., 1/distance).
- Fit linear regression (or any learner) on weighted neighborhood → **locally weighted linear regression (LWLR)**.
- k = n with weighting: prediction varies by query; can approximate curves from linear local pieces.
- Can substitute decision trees, neural nets, etc. for the local model.

**Effect**: simple global hypothesis class + local fitting → effectively **richer** hypothesis space.

Summary
-------

+----------------------+---------------------------------------------------+
| Topic                | Takeaway                                          |
+======================+===================================================+
| **Lazy learning**    | Store data; compute at query                      |
+----------------------+---------------------------------------------------+
| **k-NN**             | k neighbors + metric + vote/mean                  |
+----------------------+---------------------------------------------------+
| **Parameters**       | k and distance = domain knowledge                 |
+----------------------+---------------------------------------------------+
| **Complexity**       | O(n) space; O(log n + k) query (sorted 1-D)       |
+----------------------+---------------------------------------------------+
| **Biases**           | Locality, smoothness, equal feature weight        |
+----------------------+---------------------------------------------------+
| **High dimensions**  | Exponential data need; k-NN especially vulnerable   |
+----------------------+---------------------------------------------------+
| **LWLR**             | Local models extend expressive power                |
+----------------------+---------------------------------------------------+
