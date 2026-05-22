Bayesian Inference
==================

Revision reference for **Bayesian networks**, **conditional independence**, **inference**, and **Naive Bayes**.

Intro
-----

**Bayesian networks** (belief nets, Bayes nets, graphical models): compact representation for reasoning about probabilistic quantities over complex spaces. Complements **Bayesian learning** from the prior lecture.

Joint Distribution
------------------

**Joint distribution**: probability over all combinations of variables.

Example — storm / lightning / thunder (Atlanta summer, 2 PM):

+------------------+-----------+-----------+
|                  | Lightning | No light. |
+==================+===========+===========+
| **Storm**        | 0.25      | 0.40      |
+------------------+-----------+-----------+
| **No storm**     | 0.05      | 0.30      |
+------------------+-----------+-----------+

- Four mutually exclusive outcomes; probabilities sum to 1.
- **Marginalization**: sum over unwanted variables.
  - P(storm) = 0.25 + 0.40 = 0.65; P(¬storm) = 0.35.
- **Conditional probability**: P(lightning | storm) = 0.25 / 0.65 ≈ 0.385.
- P(¬lightning | storm) = 0.40 / 0.65 ≈ 0.615.
- P(no storm) = 0.05 + 0.30 = 0.35.

**Quiz answers (2-variable table)**:

- P(¬storm) = 0.05 + 0.30 = **0.35**
- P(lightning | storm) = 0.25 / (0.25 + 0.40) = **5/13 ≈ 0.385**

Adding Variables
----------------

Each new **binary** variable doubles the number of entries (2^n for n binary vars). Categorical variables multiply further (e.g., food type ×5). Full joint tables become intractable → **factor** the distribution via independence structure.

Conditional Independence
------------------------

**Independence**: P(X,Y) = P(X)·P(Y) ⟺ P(X|Y) = P(X) for all x, y.

**Conditional independence**: X is conditionally independent of Y given Z iff:

.. math::

    P(X=x \mid Y=y, Z=z) = P(X=x \mid Z=z)

for all x, y, z. Knowing Z makes Y irrelevant for predicting X → **factors** the joint.

Storm example: **Thunder ⊥ Storm | Lightning** — P(thunder | lightning, storm) = P(thunder | lightning). Storm value does not matter once lightning is known.

**8-row joint** (storm S, lightning L, thunder T — binary each):

Verify conditional independence: P(T=t | L=l, S=s) equals P(T=t | L=l) for all settings. Example:

- P(T=1 | L=0, S=1) = 0.04/0.40 = **0.1**
- P(T=1 | L=0, S=0) = 0.03/0.30 = **0.1**  (same → storm irrelevant given lightning)

**Quiz**: any (T, L) assignment works; storm column cancels from numerator and denominator.

Belief Networks (Bayes Nets)
----------------------------

**Structure**: directed graph; nodes = random variables; edges encode **conditional dependencies** (not necessarily causal).

Storm → Lightning → Thunder network needs only **5 parameters** vs 8 in full joint:

- P(S), P(L|S), P(L|¬S)
- P(T|L), P(T|¬L)  (thunder independent of storm given lightning)

**Key properties**:

- Arrows encode **statistical** dependence / conditional independence, not physical causation.
- **Parents**: variables a node depends on. Parameters at a node grow as **2^(# parents)** (CPT size).
- Graph is a **DAG** (directed acyclic graph) — cycles would break conditional-independence semantics.

**Bayes net vs neural net** (important):

- Neural net: multiple inputs to a node → **weighted sum** of influences.
- Bayes net: node value depends on **all joint combinations** of parent values → CPT size **2^(# parents)**.
- Removing edge S→T is valid only when **T ⊥ S | L**; otherwise need extra edge and larger CPT.

**Arrows ≠ causation**: edges encode conditional independence structure for probability factorization, not necessarily physical causation (though generative stories can help intuition).

**Filling CPTs** (storm example):

- P(S=1) = 0.65
- P(L=1|S=1) = 0.25/0.65 ≈ 0.385; P(L=1|S=0) = 0.05/0.35 ≈ 0.143
- P(T=1|L=1) = 0.2/0.25 = 0.8; P(T=1|L=0) = 0.04/0.4 = 0.1

Sampling From a Bayes Net
-------------------------

To sample one full assignment:

1. Sample root nodes (no incoming edges) from priors.
2. Sample each child conditioned on already-sampled parents.
3. Repeat in **topological order** (parents before children).

**Topological sort** requires an acyclic graph.

Recovering the Joint Distribution
---------------------------------

Any joint assignment (a,b,c,...) equals the **product** of local CPT entries:

.. math::

    P(A=a, B=b, C=c, \ldots) = P(A=a) \cdot P(B=b) \cdot P(C=c \mid A=a, B=b) \cdots

Compact when each node has few parents; exponential only in parent count, not total variables.

**Parameter count example** (5 Boolean nodes A–E, naive joint = 2⁵−1 = 31):

- P(A): 1 param; P(B): 1; P(C|A,B): 4; P(D|B): 2; P(E|C,D): 4 → **14 params** vs 31.
- If all variables independent: only **5** params (one per marginal).
- Compactness depends on **parent count**, not total variable count.

**Quiz (5-node net A→C, B→C, B→D, C→E, D→E)**: sample in **topological order** (e.g., A, B, C, D, E). Requires **DAG** — no cycles.

Sampling and Approximate Inference
----------------------------------

**Uses of sampling**:

- **Simulation**: generate worlds consistent with the model.
- **Approximate inference**: estimate P(query | evidence) by counting samples where query holds (e.g., P(storm | thunder) via many sampled worlds).
- **Visualization / intuition**: concrete examples from high-dimensional nets.

**Exact inference** on general Bayes nets is **NP-hard** (reduction from SAT). Sampling trades accuracy for tractability.

Inference Rules
---------------

Three core tools:

1. **Marginalization**: P(X) = Σ_y P(X, Y=y)
2. **Chain rule**: P(X,Y) = P(X)·P(Y|X) = P(Y)·P(X|Y)
   - Network Y → X corresponds to P(Y)·P(X|Y)
3. **Bayes' rule**: P(H|D) = P(D|H)·P(H) / P(D)

Inference by Hand: Boxes and Balls
----------------------------------

Setup: pick Box 1 (4 balls: 3G, 1Y) or Box 2 (5 balls: 2G, 3B) with P=0.5 each. Draw without replacement. Given first draw = **green**, find P(second = blue).

Bayes net: Box → Ball1 → Ball2 (Ball2 depends on both Box and Ball1).

.. math::

    P(B_2=\text{blue} \mid B_1=\text{green}) = \sum_{\text{box}} P(B_2=\text{blue} \mid B_1=\text{green}, \text{box}) \cdot P(\text{box} \mid B_1=\text{green})

From CPTs: P(blue | green, box1) = 0; P(blue | green, box2) = 3/4.

Update box beliefs via **Bayes' rule**:

- P(box1 | green) = (3/4 · 1/2) / P(green) = 15/23
- P(box2 | green) = 8/23

Result: P(second blue | first green) = 0 · 15/23 + 3/4 · 8/23 = **6/23**.

**CPT fragment** (Ball2 | Ball1=green):

+------+----------+----------+----------+
| Box  | P(G|G,box)| P(Y|G,box)| P(B|G,box)|
+======+==========+==========+==========+
| 1    | 2/3      | 1/3      | 0        |
+------+----------+----------+----------+
| 2    | 1/4      | 0        | 3/4      |
+------+----------+----------+----------+

**Marginalization + chain rule** pattern used throughout:

.. math::

    P(X) = \sum_y P(X, Y=y) = \sum_y P(X \mid Y=y)\, P(Y=y)

Naive Bayes
-----------

**Structure**: class node (e.g., Spam) → feature nodes (words). Features **conditionally independent given class**.

Spam example CPTs (illustrative):

- P(spam) = 0.4
- P(viagra|spam)=0.3, P(viagra|¬spam)=0.001
- P(prince|spam)=0.2, P(prince|¬spam)=0.1
- P(udacity|spam)≈0, P(udacity|¬spam)=0.1

**Classification** — compute P(class | features) via Bayes' rule; features factor:

.. math::

    P(v \mid a_1,\ldots,a_n) \propto P(v) \prod_i P(a_i \mid v)

**MAP class**:

.. math::

    \hat{v} = \arg\max_v P(v) \prod_i P(a_i \mid v)

Normalize over classes or compare unnormalized scores (ordering preserved).

**Worked spam query**: P(spam | viagra=1, prince=0, udacity=0):

.. math::

    P(\text{spam} \mid \mathbf{a}) \propto P(\text{spam}) \cdot P(\text{viagra}|\text{spam}) \cdot P(\neg\text{prince}|\text{spam}) \cdot P(\neg\text{udacity}|\text{spam})

.. math::

    = 0.4 \times 0.3 \times 0.8 \times 1.0

Compare to ¬spam product; normalize or take argmax only.

**General form** (class v, attributes aᵢ):

.. math::

    P(v \mid a_1,\ldots,a_n) = \frac{P(v) \prod_i P(a_i \mid v)}{\sum_{v'} P(v') \prod_i P(a_i \mid v')}

Why Naive Bayes Works
---------------------

- General inference on Bayes nets is hard; **Naive Bayes structure** makes inference **linear** in # attributes (2 params per feature + class prior).
- **Parameter estimation**: count frequencies in labeled data.
- **"Naive" assumption** (features independent given class) is often false, yet classification works because:
  - Only **argmax** matters, not calibrated probabilities.
  - Redundant/correlated features may **double-count** but preserve ranking.
- **Zero-count problem**: unseen (feature, class) pairs zero the product → **Laplace smoothing** (add small pseudo-counts); analogous to avoiding overfitting.

Summary
-------

+---------------------------+--------------------------------------------------+
| Concept                   | Key point                                        |
+===========================+==================================================+
| **Joint distribution**    | Grows exponentially; marginalize / condition     |
+---------------------------+--------------------------------------------------+
| **Conditional indep.**    | Factor joint; fewer parameters                     |
+---------------------------+--------------------------------------------------+
| **Bayes net**             | DAG + CPTs; product recovers joint               |
+---------------------------+--------------------------------------------------+
| **Sampling**              | Topological order; approximate inference         |
+---------------------------+--------------------------------------------------+
| **Exact inference**       | NP-hard in general                               |
+---------------------------+--------------------------------------------------+
| **Naive Bayes**           | Class → features; linear params; strong baseline |
+---------------------------+--------------------------------------------------+
