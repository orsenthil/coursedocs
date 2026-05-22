Decision Trees
==============

Most popular technique in data mining and machine learning. Core tension throughout ML: complicated model that fits data well vs. **Occam's Razor** — simplest adequate theory.

**Occam's Razor**: prefer the simplest theory that explains the data.

Supervised Learning — Classification vs Regression
----------------------------------------------------

**Classification**: map input :math:`x` → discrete label (true/false, male/female, car vs cougar).

**Regression**: map input → continuous real value (points on a line, hair length in inches, age 23.7).

Preview: regression covered in more detail in a later lecture; this unit focuses on classification via decision trees.

Classification vs Regression
----------------------------

Two types of **supervised learning**:

| | **Classification** | **Regression** |
|---|---------------------|----------------|
| Output | Discrete label (small finite set) | Continuous real value |
| Examples | Male/female; lend/don't lend; HS/college/grad | Predict age 23.7; credit score; hair length |
| Input | Can be discrete, continuous, or complex | Same |

**The task type is determined by the output**, not the input.

**Quiz examples**:

1. **Lend money** (yes/no) → **classification** (binary)
2. **Education level** (HS / college / grad) → **classification** (trinary; still discrete)
3. **Age** (possibly fractional, e.g. 22.3) → **regression** (continuous output)

Note: ages *could* be treated as 250 discrete year-classes → classification, but predicting 23.7 as a real number is the natural regression formulation.

**Supervised Learning Quiz — reasoning**:

| Problem | Output type | Task |
|---------|------------|------|
| Lend money? | Binary yes/no | Classification |
| Education level (HS/college/grad) | 3 discrete classes | Classification |
| Age (22.3 years) | Continuous real | Regression |

For age: even though people don't usually say "22.3 years old," fractional ages make regression natural. Discretizing to integer years (1…250) would make it classification with a large but finite label set.

Key Terminology
---------------

* **Instances** — input vectors (attributes/features): pixels, income, restaurant features, etc.
* **Concept** — function mapping instances → outputs; intuitively, membership in a set (e.g. "maleness", "creditworthiness")
* Formally: concept = mapping from input space to output space; intuitively = idea describing a set of things
* Example: "tallness" maps objects → {tall, not tall}; "car" maps objects → {car, non-car}
* **Target concept** — the true function we want to learn (the actual answer)
* **Hypothesis class** — set of functions we are willing to consider
* Could be all possible functions, but with finite data exhaustive search is impossible
* Already restricted: excludes regression functions like :math:`y = x^2`
* For decision trees: all tree-structured functions over our attributes
* **Training set** — labeled input/output pairs used to learn (inductive learning from examples)
* **Candidate** — a hypothesized concept (a specific decision tree)
* **Testing set** — held-out labeled data to evaluate generalization

**Critical**: training set and testing set must **not** overlap — testing on training data is "cheating" (memorization ≠ generalization).

Classification Learning — Worked Example
------------------------------------------

**Creditworthiness** example:

* **Instances**: pictures of people, or financial attributes (income, etc.)
* **Target concept**: creditworthy (true/false) — the function we want to learn
* **Hypothesis class**: initially "all possible functions" is too large; decision trees restrict this

**Inductive learning**: instead of a dictionary definition of "creditworthy," provide many labeled examples (input + correct output). Learner must **generalize** beyond seen examples.

**Candidate concept example**: "curly hair → creditworthy" — fails when testing set has curly-haired person who is not creditworthy.

**Testing**: apply candidate to held-out examples; count misclassifications = **error**. True target concept in this example: whether person **smiles** (illustrating that candidates can be wrong even on training-like data).

**Generalization** is the whole point of machine learning — final exams test new instances, not memorized facts.

**Hypothesis class** note: could be all possible functions, but finite data makes exhaustive search impossible. Decision trees restrict to tree-structured functions; already a subset of all functions (excludes e.g. :math:`y = x^2` regression).

Contingency Tables
------------------

* **1-D contingency table** = histogram
* **K-D contingency table** — pick K attributes :math:`(a_1, \ldots, a_k)`, count each value combination
* Database terminology: k-dimensional **data cube**; **OLAP** (Online Analytical Processing) views slices and aggregates of database tables

**Why contingency tables?** Multi-dimensional view of data — understand relationships across several attributes simultaneously.

**Combinatorics**:

* With **n** attributes, number of **m-D** contingency tables: :math:`\binom{n}{m}` (**n choose m**)
* With 100 attributes, 3-D tables:

.. math::

   100 C_{3} = (100 * 99 * 98) / (3 * 2 * 1) =  161700

Data Mining & Information Theory
--------------------------------

**Data mining** — process of finding patterns in data; decide which patterns are interesting vs. illusory and how to exploit them. **Information gain** is the engine driving decision tree learning.

**Information theory** — originally for compression; now used in data mining. **Information gain** is a sub-topic.

Key quantities (from contingency-table analysis):

* :math:`H(\text{wealth})` — entropy of wealth attribute alone
* :math:`H(\text{wealth} \mid \text{relation})` — conditional entropy of wealth given relation
* :math:`IG(\text{wealth} \mid \text{relation})` — information gain from knowing relation when predicting wealth

High information gain on an attribute → that attribute is **predictive** of the target.

Learning Decision Trees
-----------------------

A decision tree is a **tree-structured plan** of attribute tests to predict output:

1. Find attribute with highest **information gain**
2. Test it at the current node
3. **Recurse** on each branch's subset

Base cases for recursion:

* All records have same output label
* No attribute can further subdivide records
* No information gain from any remaining attribute (**XOR** example — no single split helps)

**Decision stump** — a tree with only the root node (single attribute test). Useful baseline; full trees built by recursive splitting.

**XOR base-case problem**: if we stop when IG = 0, XOR never splits (every attribute gives zero gain) — illustrates why XOR is hard and why parity needs exponential trees.

Dating Example — Problem Setup
------------------------------

**Classification** task: enter restaurant (yes/no)?

**Attributes** (features about the situation):

| Attribute | Type | Example values |
|-----------|------|----------------|
| Type | multi-valued | Italian, French, Thai, American, Greek, … |
| Atmosphere | multi-valued | fancy, casual, hole-in-wall |
| Occupied | binary | yes / no |
| Hot date | binary | yes / no |
| Cost | discrete or numeric | cheap / moderate / expensive (or average entrée price) |
| Hungry | binary | yes / no |
| Raining | binary | yes / no |

Some features relate to the restaurant; others are external (weather, hunger, date context). Irrelevant features (e.g. "cars parked across the country") should be excluded — tree building via IG naturally deprioritizes them.

Decision Tree Representation
----------------------------

**Representation vs algorithm**: first understand what a decision tree *is* (data structure); then learn the algorithm (ID3) to *build* one.

Structure:

* **Decision nodes** (circles) — test an attribute; **edges** = possible attribute values
* **Leaf nodes** (squares) — output label (yes/no, true/false)
* Traverse **top-down from root only** — never bottom-up

Example path: "Hungry?" → yes → "Raining?" → no → **Enter (true)**

At leaves, T/F means the **output answer**, not an attribute value.

**Concrete example tree** uses only **Occupied**, **Type** (pizza/Thai/other), **Happiness** (patrons look happy):

* Occupied = true → check type; pizza → no-go; Thai → go; other → check happiness
* Occupied = false → no-go (always)
* Hot date, hungry, raining irrelevant for this particular tree

The instance table serves as a **testing set**; the tree is a **candidate concept**.

Representation Quiz — Tracing Instances
---------------------------------------

Six restaurant scenarios; trace each **from root** (Occupied node):

| Instance | Occupied | Type | Happiness | Path | Output |
|----------|----------|------|-----------|------|--------|
| 1 | true | pizza | true | occupied→type(pizza) | **No go** |
| 2 | false | — | — | occupied(false) branch | **No go** |
| 3 | true | Thai | — | occupied→type(Thai) | **Go** |
| 4 | false | — | — | occupied(false) | **No go** |
| 5 | true | Thai | — | occupied→type(Thai) | **Go** |
| 6 | true | other | true | occupied→type(other)→happiness(true) | **Go** |

**Common mistake**: starting from a leaf (e.g. happiness node) instead of root — decision trees always evaluate top-down.

Only 3 of 6+ features matter for this tree; hot date, hungry, raining are irrelevant here.

Best Attribute
--------------

Given training instances labeled red (×) or green (○), rank three possible splits:

| Rank | Split behavior | Assessment |
|------|---------------|------------|
| **1 (best)** | All × on one side, all ○ on other | Perfect — done classifying |
| **2** | Splits into smaller groups but ~50/50 mix on both sides | Some splitting, no label separation; arguably useless (may overfit) |
| **3 (worst)** | All data to one side | Does nothing — "kicked the can down the road" |

Good split = **reduces uncertainty** about labels.

Decision Tree Expressiveness
----------------------------

**AND / OR / XOR recap** (2 attributes):

| Function | Min nodes | Separable by one test? |
|----------|-----------|----------------------|
| AND | 2 | Yes (one split) |
| OR | 2 | Yes |
| XOR | 3 | No — needs multiple levels |

**Boolean functions** over :math:`n` attributes:

**OR (any function)** — if any attribute true, output true:

::

   A1? ──true──→ YES
     └──false──→ A2? ──true──→ YES
                        └──false──→ A3? ──true──→ YES
                                       └──false──→ ... ──→ NO

* Tree structure: test attributes sequentially until one is true
* Size: **:math:`O(n)`** nodes — **linear**
* Each attribute tested at most once along any path

**XOR / Parity (odd function)** — output true if odd number of attributes are true:

* Must explore essentially all combinations
* Size: **:math:`O(2^n)`** nodes — **exponential**, **hard / evil**
* No clever attribute ordering avoids exhaustive branching
* For :math:`n=3`: 7 internal nodes (suspiciously :math:`2^3 - 1`)
* For :math:`n=4`: entire new level added → doubles again

**XOR truth table** (3 attributes):

| A1 | A2 | A3 | XOR |
|----|----|----|-----|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

Each subtree at an internal node is itself a smaller parity problem.

**Representation matters**: adding derived attribute B = sum of all Aᵢ (treating true=1, false=0) reduces parity to a simple test on B — but requires choosing a good representation upfront ("cheating" in the strict sense, but good practice). AI adage: hardest problem is finding a good representation.

How Many Decision Trees?
~~~~~~~~~~~~~~~~~~~~~~~~

Boolean inputs, Boolean output → analyze via **truth table**:

* :math:`n` Boolean attributes → :math:`2^n` rows (all combinations of true/false)
* Each row's output can be true or false independently
* Attribute ordering for internal nodes: combinatorial (roughly factorial in :math:`n`)
* Leaf labels: exponential choices

Total: enormously large — far beyond exhaustive search. ID3's greedy IG heuristic navigates this space efficiently.

Truth table row count examples:

| Attributes :math:`n` | Rows :math:`2^n` |
|---------------------|-----------------|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| :math:`n` | :math:`2^n` |

ID3 Algorithm
-------------

Greedy top-down tree builder:

::

   function ID3(examples, attributes):
       if all examples same label → return leaf with that label
       if no attributes left → return leaf with majority label
       A ← attribute with maximum information gain
       create node N for attribute A
       for each value v of A:
           create branch for v
           examples_v ← subset of examples where A = v
           if examples_v empty → add leaf with majority label
           else → add subtree ID3(examples_v, attributes - {A})
       return tree rooted at N

**ID3 in plain language**:

1. Loop until solved
2. Pick best attribute (max information gain)
3. Create node; branch on each attribute value
4. Sort training examples into branches
5. If perfectly classified → stop that branch
6. Otherwise recurse on each branch's subset

**Information Gain**

.. math::

   IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|}\, H(S_v)

* :math:`S` — current training examples at this node
* :math:`H(S)` — **entropy** of class labels in :math:`S`
* :math:`H(S_v)` — entropy of subset where attribute :math:`A = v`
* Choose attribute A that **maximizes** IG

Entropy
~~~~~~~

Measure of **randomness / uncertainty** in labels:

.. math::

   H(S) = -\sum_{v} P(v)\,\log P(v)

Intuition:

* **Fair coin** (P=½ each): 1 bit of entropy — maximum uncertainty
* **Two-headed coin**: 0 bits — outcome known in advance
* All labels same → entropy = 0 (no uncertainty)
* Even mix of × and ○ → maximum entropy for that set

Connecting to the three split examples:

1. All data one side → entropy unchanged → IG = 0
2. Split in half but same mix both sides → total entropy unchanged → IG = 0
3. Perfect separation → child entropies = 0 → IG = H(S) (maximum)

Entropy Example — Coin Flips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Coin type | P(heads) | Entropy |
|-----------|----------|---------|
| Fair (two-sided) | ½ | 1 bit (max uncertainty) |
| Two-headed | 1 | 0 bits (no uncertainty) |
| Training set: 50% ×, 50% ○ | — | Maximum for that label set |
| Training set: 100% × | — | 0 (no uncertainty) |

ID3 Inductive Bias
------------------

Two kinds of **bias**:

**Restriction bias** — hypothesis class = decision trees over discrete attributes (not all functions, not regression formulas like :math:`y = 2x`).

**Preference bias** — among decision trees, ID3 prefers:

1. **Good splits near the top** (high information gain first)
2. **Correct** trees over incorrect ones
3. **Shorter** trees over longer ones (consequence of good top splits — reaches leaves faster)

Given two trees representing the same function, ID3 prefers the one with better top-level splits.

An attribute that puts all data on one side (zero IG) would create a longer, unnecessary tree — ID3 avoids this automatically.

Continuous Attributes
---------------------

Problem: branching on every exact value → infinite branches for truly continuous variables; cannot handle unseen values at test time.

**Naive approaches (and why they fail)**:

| Approach | Problem |
|----------|---------|
| Branch per exact value (1.0, 1.1, 1.11, …) | Infinite branches |
| Branch only on training-set values | Unseen test values don't match any branch |
| Use test set to pick splits | Cheating — test set must remain unseen |

**Solution**: binary splits on **ranges**:

* e.g. ``age >= 20 AND age < 30`` (inclusive of 20, exclusive of 30)
* Represented as a single binary decision node

Finding split points:

* Examine **training set** values only
* If all values in 20s, no point splitting on 30s range
* **Binary search** on training values: ``value < median`` vs ``value >= median``
* Evaluate each candidate split with information gain
* Many candidates for continuous variables, but finite from training data

**Worked example — age splits**:

* Training ages: {22, 25, 28, 35, 41}
* Candidate splits: < 25, < 28, < 35, etc.
* Each creates two branches evaluated by IG

**Repeating attributes on a path**:

| Attribute type | Repeat on same path? | Reason |
|---------------|---------------------|--------|
| **Discrete** | No | Same question → zero information gain |
| **Continuous** | Yes (different ranges) | "Age in 20s?" vs "Age ≥ 40?" are different questions |

**Quiz: repeat attribute on same path?**

* **Discrete** (e.g. ``A = true?`` then later ``A = true?`` again): **No** — zero information gain; IG automatically deprioritizes
* **Continuous** (e.g. ``age in 20s?`` then ``age >= 44?``): **Yes** — different questions about same underlying variable

Other Considerations
--------------------

**When to stop?**

* All training examples correctly classified — but problematic with **noisy data** (conflicting labels on same instance → never stops)
* Run out of attributes
* Need better criteria for continuous attributes (infinite possible splits)

**Overfitting**

Memorizing every training quirk → excellent training accuracy, poor generalization. Violates **Occam's Razor**.

**When noise exists** (mislabeled examples, duplicate instances with conflicting labels):

* "Stop when all correct" → never terminates
* Must use alternative stopping criteria

**Mitigations**:

1. **Hold-out validation set / cross-validation**
   * Build tree on training data (excluding validation)
   * Evaluate on validation set
   * Pick tree with lowest validation error
   * Avoids needing a separate stopping rule during growth

2. **Early stopping with validation**
   * Before each expansion, check validation error so far
   * Stop if error is low enough or starts increasing
   * Use **breadth-first** expansion so all branches grow evenly (depth-first can over-expand one branch before testing others)

3. **Pruning** (post-hoc, efficient)
   * Build full tree as if overfitting weren't a concern
   * From leaves upward: collapse subtrees into single nodes
   * Keep collapse if validation error increase is small
   * Discard collapse if validation error jumps too much
   * Produces smaller tree; simple addition to standard ID3
   * Many pruning variants exist

**Stopping criteria summary**:

| Criterion | Handles noise? | Notes |
|-----------|---------------|-------|
| All training examples correct | No | Infinite loop with conflicting labels |
| No attributes left | Partially | Forced stop |
| No information gain | Partially | XOR never splits |
| Validation error threshold | Yes | Preferred with continuous attrs |
| Pruning post-hoc | Yes | Build full tree first |

Regression Trees
----------------

So far: discrete outputs with information gain. For **regression** (continuous outputs):

* **Split criterion**: e.g. **variance reduction** instead of entropy (measures spread of continuous values)
* **Leaf prediction**: average of training values in leaf, or linear fit
* **Classification leaves**: majority vote when labels mixed
* Pruning and validation apply similarly

**Leaf output when labels mixed** (classification): majority **vote**. With pruning, even impure leaves need an output — vote generalizes best for maximizing correct classifications.

Regression vs Classification Trees
----------------------------------

| Aspect | Classification tree | Regression tree |
|--------|--------------------|-----------------|
| Output | Discrete label | Continuous value |
| Split criterion | Information gain (entropy) | Variance reduction |
| Leaf value | Majority vote | Average (or linear fit) |
| Pruning metric | Classification error | Squared error / variance |
| Mixed leaves | Vote ≈ average for binary | Average of continuous values |

Basic Decision Tree — Quick Reference
-------------------------------------

**Build** (ID3):

#. Start with all examples at root
#. Choose attribute with max information gain
#. Split; recurse on each branch
#. Stop at pure leaf, no attributes, or validation/pruning criterion

**Use**:

#. Start at root
#. Follow edge matching instance's attribute value
#. Repeat until leaf → output label

**Key formulas**:

.. math::

   H(S) = -\sum_v P(v) \log P(v)

.. math::

   IG(S, A) = H(S) - \sum_v \frac{|S_v|}{|S|} H(S_v)

.. math::

   \binom{n}{m} \text{ contingency tables from } n \text{ attributes, dimension } m

Summary
-------

* **Decision trees** — interpretable top-down attribute tests; root-to-leaf path = series of decisions
* **ID3** — greedy recursive builder; best attribute = max **information gain** (entropy reduction)
* **Expressiveness** — any Boolean function representable; OR is linear, parity/XOR is exponential
* **Bias** — restricted to trees; prefers correct, short trees with informative top splits
* **Continuous inputs** — range-based binary splits from training data; can repeat attribute with different ranges
* **Overfitting** — pruning / validation; don't trust perfect training classification with noisy data
* **Regression variant** — variance-based splits; average/vote at leaves

References
----------

* Andrew Ng's tutorial — self-contained material on decision trees
* `Weka Tutorial <http://art.uniroma2.it/basili/MLWM09/002_DecTree_Weka.pdf>`_
* `Information Gain <http://www.autonlab.org/tutorials/infogain.html>`_

Further topics (assignments): advanced pruning, multi-class trees, missing values, cost-sensitive splits.
