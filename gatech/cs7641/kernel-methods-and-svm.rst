Kernel Methods and SVM
======================

Support Vector Machines
-----------------------

Motivation: Maximum Margin
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Setup**: 2D points labeled + (positive) and − (negative), linearly separable.

- Infinitely many separating lines exist (e.g., 3 green × 3 red anchor points → 9 possible lines).
- **Best line**: middle line with equal space on both sides — largest **margin** / demilitarized zone.
- Lines close to one class risk misclassifying nearby unseen points → **overfitting** (believing training data too much).
- **Least commitment principle**: be consistent with data while committing as little as possible.
- This is the foundation of **Support Vector Machines (SVMs)**.

Hyperplane Notation
~~~~~~~~~~~~~~~~~~~

- In multiple dimensions, separating surface is a **hyperplane**:

  .. math::

     y = w^T x + b

  +------------------+---------------------------------------------------+
  | Symbol           | Meaning                                           |
  +==================+===================================================+
  | :math:`y`        | Classification label (+1 / −1)                    |
  | :math:`w`        | Parameter vector (normal to hyperplane)           |
  | :math:`b`        | Bias — shifts hyperplane in/out of origin         |
  | :math:`x`        | Input feature vector                              |
  +------------------+---------------------------------------------------+

- **Decision boundary** (classifier output = 0, neither positive nor negative):

  .. math::

     w^T x + b = 0

- Labels: :math:`y_i \in \{-1, +1\}` (same convention as boosting).

- **Margin boundaries** — parallel hyperplanes touching each class without misclassification:

  .. math::

     w^T x + b = +1 \quad \text{(positive class boundary)}

  .. math::

     w^T x + b = -1 \quad \text{(negative class boundary)}

Margin Derivation
~~~~~~~~~~~~~~~~~

**Construction**:

1. Top gray line: as close as possible to + points without crossing → outputs +1 at first + point.
2. Bottom gray line: as close as possible to − points → outputs −1.
3. Middle orange line: decision boundary, equidistant from both gray lines.

**Distance between parallel hyperplanes**:

- Pick :math:`x_1` on +1 boundary, :math:`x_2` on −1 boundary.
- Subtract equations:

  .. math::

     w^T (x_1 - x_2) = 2

- Divide both sides by :math:`|w|` (unit normal):

  .. math::

     \frac{w^T}{|w|} (x_1 - x_2) = \frac{2}{|w|}

- Left side = length of projection of :math:`x_1 - x_2` onto :math:`w`.
- :math:`w` is **perpendicular** to hyperplane; :math:`x_1 - x_2` is also perpendicular → projection equals full distance.
- **Margin** :math:`m`:

  .. math::

     m = \frac{2}{|w|}

**Optimization goal**: maximize :math:`m` ⟺ minimize :math:`|w|`, subject to correct classification.

- Setting :math:`w = 0` would maximize margin but fail to classify — need constraints.

Primal Optimization Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Correct classification as constraint**:

- Want: classifier output ≥ +1 for positive examples, ≤ −1 for negative examples.
- Multiply both sides by label :math:`y_i` (clever trick — flips inequality for negatives):

  .. math::

     y_i (w^T x_i + b) \geq 1 \quad \forall i \in \text{training set}

**Primal formulation**:

- Original: maximize :math:`\frac{2}{|W|}` subject to constraints above.
- Equivalent (easier to solve): **minimize** :math:`\frac{1}{2}|W|^2` subject to same constraints.
  - Reciprocal reverses max/min (for positive values).
  - Squaring is monotone → same optimum, magnified differences.

**Quadratic Programming (QP)**:

- Form: minimize quadratic function subject to linear constraints.
- SVM primal always has a solution; always has a **unique** solution.
- Solved via standard QP solvers.

Dual Form (Lagrange Multipliers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transform primal → dual (via Lagrange multipliers / KKT):

.. math::

   \max_\alpha \;\; \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j

**Constraints**:

.. math::

   \alpha_i \geq 0 \quad \forall i

.. math::

   \sum_i \alpha_i y_i = 0

**Recover primal weights from dual**:

.. math::

   w = \sum_i \alpha_i y_i x_i

**Recover bias** :math:`b`: plug any support vector (on margin boundary) into :math:`w^T x + b = \pm 1`.

Support Vectors
~~~~~~~~~~~~~~~

**Key property**: in the dual solution, **most** :math:`\alpha_i = 0`.

- **Non-zero** :math:`\alpha_i` → point is a **support vector**.
- :math:`w = \sum_i \alpha_i y_i x_i` — only non-zero-α points contribute.
- Points **far from decision boundary** → :math:`\alpha = 0` (no influence on boundary).
- Points **on/near boundary** → non-zero :math:`\alpha` (define the margin contours).

**Quiz: Optimal Separator** — which points have zero α?

- Answer: points far from the green decision line (e.g., lower-left −, upper-right +).
- Points close to boundary are support vectors.

**Analogy to KNN**:

- Like instance-based learning where only local points matter.
- SVM pre-computes which points matter (via QP) — can discard the rest.
- Not just nearest neighbors; QP selects the informative ones.

Non-Linearly Separable Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Case 1: Outlier / noise**

- Single − point among + cluster → no zero-error linear separator; margin becomes negative.
- **Soft margin**: find separator minimizing misclassifications while maximizing margin (homework).
- Trade-off knob between margin size and number of errors.

**Case 2: Non-linear structure ("Linearly Married")**

- + points form inner cluster; − points form outer ring.
- No line separates classes in 2D.
- **Solution**: transform data to higher dimensions where separation becomes linear.

Feature Mapping and the Kernel Trick
------------------------------------

Feature Map φ — Worked Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: ring of − points around + cluster; not linearly separable in 2D.

**Transform** :math:`\phi`: 2D → 3D without adding external information:

.. math::

   \phi(q) = \left(q_1^2,\; q_2^2,\; \sqrt{2}\, q_1 q_2\right) \quad \text{where } q = (q_1, q_2)

- Pluses near origin → lower 3rd coordinate.
- Minuses on ring → higher 3rd coordinate.
- Hyperplane in 3D separates the classes.

**Quiz: What is the Output?** — compute :math:`\phi(x)^T \phi(y)`:

.. math::

   \phi(x)^T \phi(y) = x_1^2 y_1^2 + x_2^2 y_2^2 + 2 x_1 x_2 y_1 y_2 = (x_1 y_1 + x_2 y_2)^2 = (x^T y)^2

- Factorization: :math:`(x^T y)^2` — **squared dot product** in original space.
- Geometric shift:
  - Original :math:`x^T y`: projection-based (directional) similarity.
  - Transformed: circular/radial similarity (inside vs outside circle).

**The Kernel Trick**:

- Dual QP uses data only via dot products :math:`x_i^T x_j`.
- Instead of computing :math:`\phi(x_i)^T \phi(x_j)` explicitly, define:

  .. math::

     K(x_i, x_j) = \phi(x_i)^T \phi(x_j)

- For this example: :math:`K(x, y) = (x^T y)^2`.
- **Never compute** :math:`\phi` — just square the dot product in code.
- Same optimization, implicit high-dimensional mapping.

Kernels
-------

Definition
~~~~~~~~~~

- **Kernel** :math:`K(x_i, x_j)` replaces :math:`x_i^T x_j` throughout the dual SVM.
- Represents **similarity** between data points.
- Mechanism for injecting **domain knowledge** into SVM learning.
- Every valid kernel corresponds to some (possibly infinite-dimensional) feature map :math:`\phi`.
- :math:`K(x, y)` = dot product in that implicit feature space.

Common Kernels
~~~~~~~~~~~~~~

**Linear kernel** (standard dot product):

.. math::

   K(x, y) = x^T y

**Polynomial kernel** (general form):

.. math::

   K(x, y) = (x^T y + c)^p

+-------------+---------------------------+
| Parameters  | Special case              |
+=============+===========================+
| :math:`p=1, c=0` | Linear kernel        |
| :math:`p=2, c=0` | Squared dot product  |
+-------------+---------------------------+

- Related to **polynomial regression** — represents polynomial decision boundaries.

**Radial Basis Function (RBF / Gaussian) kernel**:

.. math::

   K(x, y) = \exp\left(-\frac{\|x - y\|^2}{2\sigma^2}\right)

- :math:`x \approx y` → :math:`K \approx e^0 = 1` (high similarity).
- :math:`x, y` far apart → :math:`K \approx 0`.
- Symmetric Gaussian bump; :math:`\sigma` controls width (like bandwidth).

**Sigmoid kernel**:

.. math::

   K(x, y) = \tanh(\alpha\, x^T y + c)

- S-shaped transition between similarity levels.

Kernel Properties
~~~~~~~~~~~~~~~~~

- Kernels work on **non-numeric** data if similarity is definable:
  - Strings: **edit distance** (few transformations → similar).
  - Graphs, images: custom similarity functions.
- Not every function is a valid kernel.
- **Mercer Condition**: technical requirement (positive semi-definite) for kernel to behave as a proper similarity/distance function. Required for all SVM math to hold.
- Intuition: kernel must relate points consistently, not be arbitrary.
- In practice: almost any reasonable similarity function has an equivalent (possibly infinite-dimensional) feature map.

SVM Summary
-----------

+---------------------------+--------------------------------------------------+
| Concept                   | Detail                                           |
+===========================+==================================================+
| Goal                      | Decision boundary that **maximizes margin**      |
+---------------------------+--------------------------------------------------+
| Margin                    | :math:`m = 2/|w|`                                |
+---------------------------+--------------------------------------------------+
| Primal                    | Minimize :math:`\frac{1}{2}|W|^2` s.t.          |
|                           | :math:`y_i(w^T x_i + b) \geq 1`                  |
+---------------------------+--------------------------------------------------+
| Dual                      | Maximize :math:`\sum_i \alpha_i                  |
|                           | - \frac{1}{2}\sum_{i,j}\alpha_i\alpha_j y_i y_j  |
|                           | x_i^T x_j`                                       |
+---------------------------+--------------------------------------------------+
| Dual constraints          | :math:`\alpha_i \geq 0`;                         |
|                           | :math:`\sum_i \alpha_i y_i = 0`                  |
+---------------------------+--------------------------------------------------+
| Weights                   | :math:`w = \sum_i \alpha_i y_i x_i`              |
+---------------------------+--------------------------------------------------+
| Support vectors           | Training points with :math:`\alpha_i > 0`        |
+---------------------------+--------------------------------------------------+
| Kernel trick              | Replace :math:`x_i^T x_j` with :math:`K(x_i,x_j)`|
+---------------------------+--------------------------------------------------+
| Non-linear separation     | Implicit high-dim mapping via kernel             |
+---------------------------+--------------------------------------------------+

Boosting and Margins
--------------------

Why Boosting Resists Overfitting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Observation**: boosting training error → 0, but test error does **not** degrade — often keeps improving.

**Boosted classifier**:

.. math::

   h(x) = \text{sign}\left(\sum_t \alpha_t h_t(x)\right)

- :math:`\alpha_t` here = weight on weak hypothesis :math:`h_t` (different from SVM dual :math:`\alpha_i`).
- :math:`\alpha_t = \frac{1}{2}\ln\frac{1-\epsilon_t}{\epsilon_t}` > 0 always (weak learner beats chance).

**Normalized output** (for analysis; same classification):

.. math::

   \frac{\sum_t \alpha_t h_t(x)}{\sum_t \alpha_t} \in [-1, +1]

**Error vs confidence**:

+----------------------------+------------------------------------------+
| Output region              | Interpretation                           |
+============================+==========================================+
| Correct, near +1 or −1     | Confident and correct                    |
| Correct, near 0            | Correct but unconfident                  |
| Incorrect, far from 0      | Confident and wrong                      |
+----------------------------+------------------------------------------+

- KNN analogy: low variance among neighbors = high confidence.

**After zero training error, continued boosting**:

1. Training **error stays at zero**.
2. Hard examples (near boundary) get re-weighted; new weak learners focus on them.
3. Boundary points drift **farther from decision boundary** → confidence increases.
4. Effect: **margin grows** between + and − clusters.
5. Large margins → less overfitting (same principle as SVM).

- More weak learners → smoother, less overfit classifier (counter-intuitive: more complexity, less overfit).

When Boosting Overfits
~~~~~~~~~~~~~~~~~~~~~~

**Quiz: Boosting Tends to Overfit** — which conditions cause overfitting?

+---+-------------------------------+--------+
| # | Condition                     | Overfit?|
+===+===============================+========+
| 1 | Weak learner picks weakest    | No     |
|   | output above chance           |        |
+---+-------------------------------+--------+
| 2 | Weak learner is deep neural   | **Yes**|
|   | network (many layers/nodes)   |        |
+---+-------------------------------+--------+
| 3 | Very large training set       | No     |
+---+-------------------------------+--------+
| 4 | True concept is non-linear    | No     |
+---+-------------------------------+--------+
| 5 | Train too long (10¹¹ iter)    | No     |
+---+-------------------------------+--------+

**Why neural network weak learner fails**:

- Powerful NN perfectly fits training data → overfits.
- Returns same overfit hypothesis every round (all examples equal weight after zero error).
- Weighted sum of identical functions = that function → boosting cannot help.

**Other overfitting case**: **pink noise** (= uniform noise) in data.

**Weak vs strong learner terminology**:

- **Weak learner** (formal): for **any** distribution :math:`D`, error :math:`\leq \frac{1}{2} - \epsilon`.
- "Strong learner" is informal — not a precise technical term.
- Any strong learner is also technically a weak learner (does better than chance).
- Not weak ⟹ not a learner at all (error ≥ ½, provides no information).
