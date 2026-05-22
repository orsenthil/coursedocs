Ensemble Learning: Boosting and Bagging
=======================================


Ensemble Learning Overview
--------------------------

Core Idea
~~~~~~~~~

- Combine many **simple rules** (each weak alone) into one **strong composite classifier**.
- Each rule provides partial evidence; none alone is sufficient.
- Analogous to decision tree nodes (simple rules combined by structure) or neural network features (combined by weights).

**Spam email example** — simple indicative rules:

+----------------------------+--------+---------------------------+
| Rule                       | Sign   | Notes                     |
+============================+========+===========================+
| Body contains "manly"      | +spam  | Evidence, not definitive  |
| From spouse                | −spam  | Usually not spam          |
| Very short / URL only      | +spam  | Common spam pattern       |
| Just an image              | +spam  | Pharmaceutical ads        |
| Misspelled words           | +spam  | Blacklist approach        |
| "Make money fast"          | +spam  | Classic spam phrase       |
+----------------------------+--------+---------------------------+

- Each rule is partially right but individually unreliable.
- Need a principled way to **combine** them → ensemble learning.


Ensemble Learning Algorithm (General Form)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   for each round:
       learn a rule on a subset of data
   combine all rules into final hypothesis

**Two design questions**:

1. How to select **subsets** of data?
2. How to **combine** the learned rules?


Bagging (Bootstrap Aggregation)
-------------------------------

Subset Selection
~~~~~~~~~~~~~~~~

- **Uniformly random** subsets of training data.
- Sample **with replacement** (bootstrap) — same point can appear multiple times.
- Apply a learner to each subset → get hypothesis :math:`h_t`.

Combination
~~~~~~~~~~~

- **Regression**: average (mean) of all hypotheses.
- **Classification**: majority vote (or averaged scores + threshold).
- Equal weight to each hypothesis (no reason one random subset is better).

**Quiz: Ensemble Learning Outputs**

- Setup: :math:`N` data points; learner = 0th-order polynomial (constant); :math:`N` disjoint subsets of 1 point each; combine by mean.
- Each learner outputs its single point's :math:`y` value.
- Mean of all = **mean of dataset** = best 0th-order polynomial = constant.
- Same as unweighted k-NN with :math:`k = n`.

Housing Data Example
~~~~~~~~~~~~~~~~~~~~

- 9 data points; hold out 1 (green) for testing.
- 5 random subsets of 5 points (with replacement); learn **3rd-order polynomial** on each; average.
- **Result** (many trials):
  - Blue line (single 4th-order polynomial on all data): better on **training** points.
  - Red line (bagged average of 3rd-order): almost always better on **held-out green point**.
- Bagged ensemble of simpler hypotheses outperforms single complex hypothesis on test data.

**Why bagging works**:

- Random subsets prevent overfitting to individual noisy/outlier points.
- Averaging reduces variance — same argument as cross-validation.
- Mixing data focuses on important structure, not spurious fits.

**Name**: **Bagging** = **Bootstrap Aggregation**.


Boosting
--------

Motivation vs Bagging
~~~~~~~~~~~~~~~~~~~~~

+----------------------------+---------------------------+---------------------------+
|                            | Bagging                   | Boosting                  |
+============================+===========================+===========================+
| Subset selection           | Random uniform            | Focus on **hard** examples|
| Combination                | Unweighted mean/vote      | **Weighted** mean/vote    |
| Learns from mistakes       | No (independent rounds)   | Yes (re-weight each round)|
+----------------------------+---------------------------+---------------------------+

- **Hard examples**: points current ensemble misclassifies.
- Intuition: spend effort on what you haven't mastered (like learning a skill).
- Spam analogy: don't keep finding rules for already-classified mail; focus on misclassified messages.
- Weighting prevents **thrashing** — mastered examples down-weighted so they aren't forgotten entirely.


Distribution-Weighted Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Standard error** (implicit uniform distribution):

.. math::

   \text{error rate} = \frac{\text{\# mismatches}}{\text{\# examples}}

**Distribution-weighted error**:

.. math::

   \text{error}_D(h) = P_{x \sim D}[h(x) \neq c(x)]

- :math:`D` = distribution over examples (importance / frequency).
- :math:`h` = hypothesis; :math:`c` = true concept.
- Probability of disagreement, weighted by how often each example appears.

**Quiz example** — 4 examples, 2 correct / 2 wrong:

+----------+-------------+------------------+
| Example  | Correct?    | :math:`P(x)`     |
+==========+=============+==================+
| :math:`x_1` | ✓        | ½                |
| :math:`x_2` | ✗        | ¹⁄₂₀             |
| :math:`x_3` | ✓        | ⁴⁄₁₀             |
| :math:`x_4` | ✗        | ¹⁄₂₀             |
+----------+-------------+------------------+

- Uniform count: 50% error.
- Distribution-weighted: :math:`\frac{1}{20} + \frac{1}{20} = \frac{1}{10}` → **10% error** (90% correct).
- Rare mistakes matter less; frequent mistakes matter more.
- Boosting uses distributions to define **"hardest"** = highest-weight misclassified examples.


Weak Learner
~~~~~~~~~~~~

**Definition**: a learner that, for **any** distribution :math:`D` over the data, produces a hypothesis with error strictly better than chance:

.. math::

   \forall D: \;\; \text{error}_D(h) \leq \frac{1}{2} - \epsilon

- :math:`\epsilon > 0` = small constant (bounded away from ½).
- Always extracts **some information** regardless of example weighting.
- Chance (coin flip) = ½ error = zero information.

**Quiz: Weak Learning** — 3 hypotheses, 4 examples:

+------+------+------+------+
|      | H1   | H2   | H3   |
+======+======+======+======+
| :math:`x_1` | ✗ | ✓ | ✓ |
| :math:`x_2` | ✓ | ✗ | ✗ |
| :math:`x_3` | ✓ | ✓ | ✗ |
| :math:`x_4` | ✓ | ✗ | ✓ |
+------+------+------+------+

- **Good distribution** (¼ each): H1 gets ¾ correct → weak learner exists.
- **Evil distribution** (½ on :math:`x_1`, ½ on :math:`x_2`, 0 elsewhere): all hypotheses get exactly 50% → **no weak learner** for this hypothesis space.
- Fix: add more/better hypotheses (e.g., make H3 correct on :math:`x_2`).
- Finding a weak learner is **easy for 2 seconds, hard for 4** — actually a strong requirement.
- Need diverse hypotheses that do well on different example subsets.


Boosting Algorithm (Pseudocode)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Input**: training set :math:`\{(x_i, y_i)\}`, labels :math:`y_i \in \{-1, +1\}`

::

   Initialize D_1(i) = 1/n for all i          // uniform distribution

   for t = 1 to T:
       Find weak classifier h_t with small error ε_t on distribution D_t
           (error_D_t(h_t) ≤ 1/2 - ε)

       Compute α_t = (1/2) ln((1 - ε_t) / ε_t)   // weight for h_t

       Update distribution:
           D_{t+1}(i) = (D_t(i) / Z_t) · exp(-α_t · y_i · h_t(x_i))
           // Z_t = normalization constant (sums to 1)

   Output: H(x) = sign(Σ_t α_t · h_t(x))

**Key parameters**:

+-------------+----------------------------------------------------------+
| Symbol      | Meaning                                                  |
+=============+==========================================================+
| :math:`D_t` | Distribution over examples at round :math:`t`            |
| :math:`h_t` | Weak hypothesis at round :math:`t` (outputs ±1)          |
| :math:`\epsilon_t` | Weighted error of :math:`h_t` on :math:`D_t`      |
| :math:`\alpha_t` | Weight of :math:`h_t` in final vote (always > 0)    |
| :math:`Z_t` | Normalization constant for valid distribution            |
+-------------+----------------------------------------------------------+


Distribution Update
~~~~~~~~~~~~~~~~~~~

.. math::

   D_{t+1}(i) = \frac{D_t(i)}{Z_t} \exp\left(-\alpha_t y_i h_t(x_i)\right)

- :math:`y_i h_t(x_i) = +1` when hypothesis **agrees** with label.
- :math:`y_i h_t(x_i) = -1` when hypothesis **disagrees**.

**When they agree** (:math:`y_i h_t = +1`):

- Exponent is negative → :math:`e^{-\alpha_t y_i h_t} < 1` → weight **decreases** (relative to misclassified).

**When they disagree** (:math:`y_i h_t = -1`):

- Exponent is positive → :math:`e^{-\alpha_t y_i h_t} > 1` → weight **increases**.

**Quiz: When D agrees** — answer: **depends** on normalization :math:`Z_t` and other examples' updates. Practically: correct examples decrease weight when at least one other is wrong; wrong examples increase.

- Effect: misclassified (hard) examples get more weight next round.
- Weak learner guarantee ensures progress on re-weighted hard examples.


Final Hypothesis
~~~~~~~~~~~~~~~~

.. math::

   H(x) = \text{sign}\left(\sum_{t=1}^{T} \alpha_t h_t(x)\right)

- Weighted vote: better weak learners (lower :math:`\epsilon_t`) get higher :math:`\alpha_t`.
- :math:`\alpha_t = \frac{1}{2}\ln\frac{1-\epsilon_t}{\epsilon_t}` — measure of hypothesis quality.
- Sign function thresholds: positive → +1, negative → −1, zero → undecided.
- Information discarded by sign (confidence) becomes important in SVM lecture connection.


Worked Example: Three Boxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Setup**: 2D points (+ red, − green) in a square region.

**Hypothesis space**: **axis-aligned semi-planes** — horizontal or vertical line; one side = +, other = −.

**Round 1** (uniform weights):

- Learner returns vertical line separating left 2 pluses from rest.
- Correct: 2 left pluses + all minuses. Wrong: 3 right pluses ("Three Plusketeers").
- :math:`\epsilon_1 = 0.3`; :math:`\alpha_1 = 0.42`.
- Distribution update: wrong pluses ↑ weight; correct points ↓ weight.

**Round 2**:

- Vertical line to right of 3 Plusketeers (everything left = +).
- Correct: 3 Plusketeers + 2 left pluses. Wrong: 3 middle minuses (low weight).
- :math:`\epsilon_2 = 0.21`; :math:`\alpha_2 = 0.65$.
- Distribution: middle minuses ↑; Plusketeers ↓ (but still above original); never-wrong points → near zero.

**Round 3** — **Quiz: Which Hypothesis?**

- A: horizontal line above middle minuses (best — separates heavily weighted points).
- B: horizontal line lower (worse on weighted points).
- C: vertical line (used in round 2, doesn't fit current weights).
- Answer: **A**. :math:`\epsilon_3 = 0.14`; :math:`\alpha_3 = 0.92`.

**Final combined hypothesis**:

- Weighted sum :math:`\alpha_1 h_1 + \alpha_2 h_2 + \alpha_3 h_3` passed through sign.
- Produces **non-axis-aligned curved boundary** separating all points perfectly.
- Simple axis-aligned weak learners → complex decision boundary via weighted combination + sign nonlinearity.
- Analogous to: decision tree shapes, neural net weighted sums, weighted linear regression / k-NN.


Why Boosting Works (Intuition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Re-weight misclassified examples → they become increasingly important.
2. Weak learner **must** beat chance on any distribution → forced to address hard examples.
3. **Exponential weighting**: examples wrong multiple times become dominant; can't cycle forever.
4. Examples consistently correct → weight → 0 (irrelevant to future rounds).
5. Must accumulate information across rounds; can't just oscillate on same errors.
6. Result: final hypothesis gets few weighted errors → converges to good combined classifier.
7. Formal proof in assigned reading (AdaBoost convergence bound).

**Information gain perspective**: each round must pick up new information; exponential weights prevent thrashing.


Summary
-------

+-------------------+--------------------------------------------------------+
| Method            | Key idea                                               |
+===================+========================================================+
| **Ensemble**      | Combine simple rules from subsets → complex classifier |
| **Bagging**       | Random subsets + unweighted average → reduce variance  |
| **Boosting**      | Re-weight hard examples + weighted vote → reduce bias  |
| **Weak learner**  | Error < ½ − ε for any distribution :math:`D`           |
| **Distribution**  | :math:`D_t(i)` = importance of example :math:`i`       |
| **Update rule**   | Increase weight on misclassified, decrease on correct  |
| **Final output**  | :math:`H(x) = \text{sign}(\sum \alpha_t h_t(x))`       |
| **Overfitting**   | Boosting resists overfit (margin effect); fails if     |
|                   | weak learner itself overfits                           |
+-------------------+--------------------------------------------------------+
