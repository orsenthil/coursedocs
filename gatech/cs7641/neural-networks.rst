Neural Networks
===============

Overview
--------

Biological neurons (billions in the brain) fire spike trains down axons across synapses. Artificial neural networks use a **cartoon abstraction**: tunable units that compute via weighted sums and activation functions, trained by learning rules.

**Perceptron Unit**
-------------------

Simplified neuron model:

* **Inputs** :math:`x_1, x_2, x_3, \ldots` — firing rates / input strengths
* **Weights** :math:`w_1, w_2, w_3, \ldots` — gain / sensitivity per input
* **Activation**: :math:`a = \sum_i w_i x_i`
* **Output**: compare activation to **firing threshold** :math:`\theta`

.. math::

   y = \begin{cases} 1 & \text{if } a \geq \theta \\ 0 & \text{otherwise} \end{cases}

The whole unit = **linear sum + threshold** → a **Perceptron**.

**Worked Example**

Inputs :math:`(1, 0, -1.5)`, weights :math:`(\tfrac{1}{2}, \tfrac{3}{5}, 1)`, threshold :math:`\theta = 0`:

.. math::

   a = \tfrac{1}{2}(1) + \tfrac{3}{5}(0) + 1(-1.5) = \tfrac{1}{2} - \tfrac{3}{2} = -1

Activation is negative → :math:`y = \mathbf{0}` (not above threshold).

Perceptron = Half-Plane
-----------------------

With 2 inputs :math:`(x_1, x_2)`, the perceptron divides the plane:

* Example: :math:`w_1 = w_2 = \tfrac{1}{2}`, :math:`\theta = \tfrac{3}{4}`
* If :math:`x_1 = 0`: need :math:`x_2 \geq 1.5` to fire → dividing line at :math:`x_2 = 1.5`
* If :math:`x_2 = 0`: need :math:`x_1 \geq 1.5`
* Solving the linear inequality → a **line** dividing 0-region from 1-region

**Key properties**:

* A perceptron computes a **half-plane** (hyperplane in higher dimensions)
* Perceptrons are **linear classifiers**
* Always a linear dividing boundary where activation equals threshold
* In 3+ dimensions: dividing surface is a **hyperplane**; output regions are half-spaces

Visualizing the half-plane (:math:`w_1 = w_2 = \tfrac{1}{2}`, :math:`\theta = \tfrac{3}{4}`):

* Boundary line: :math:`w_1 x_1 + w_2 x_2 = \theta` → :math:`x_1 + x_2 = 1.5`
* Points with :math:`x_1 + x_2 \geq 1.5` → output 1
* Points below the line → output 0
* Generalizes: any perceptron defines a linear decision boundary

Boolean Functions via Perceptrons
---------------------------------

Restrict inputs/outputs to :math:`\{0,1\}` → **Boolean functions** (zero = false, one = true).

**AND**

With :math:`w_1 = w_2 = \tfrac{1}{2}`, :math:`\theta = \tfrac{3}{4}` and binary inputs only:

| :math:`x_1` | :math:`x_2` | Above line? | Output |
|------------|------------|-------------|--------|
| 0 | 0 | no | 0 |
| 0 | 1 | no | 0 |
| 1 | 0 | no | 0 |
| 1 | 1 | yes | 1 |

→ Computes **conjunction** (AND).

**OR**

Want :math:`y = 1` if either input is 1. Many valid weight/threshold pairs:

* :math:`w_1 = w_2 = 1`, :math:`\theta = 1` — one input alone reaches threshold
* Keep original weights, lower :math:`\theta` to :math:`\tfrac{1}{2}` (or any value in :math:`(0, 1]`)

**NOT** (single variable)

| :math:`x_1` | Desired output |
|------------|----------------|
| 0 | 1 |
| 1 | 0 |

Solution: :math:`w_1 = -1`, :math:`\theta = 0` — negative weight flips the sign; threshold at 0 exploits :math:`\geq`.

**Key result**: AND, OR, NOT all expressible as single perceptrons → any **Boolean function** composable from these.

XOR Requires a Network
----------------------

**Single perceptron cannot compute XOR** — not linearly separable (the "evil" parity function).

**Two-unit network**:

* Inputs: :math:`x_1, x_2`
* Unit 1: AND gate (known weights/threshold from above)
* Unit 2: inputs :math:`x_1, x_2`, AND output → computes XOR

Truth table insight:

| :math:`x_1` | :math:`x_2` | AND | OR | XOR |
|------------|------------|-----|----|----|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

XOR = OR except at :math:`(1,1)`. Unit 2 should compute **OR − 2·AND**:

* OR weights: :math:`w_{x_1} = w_{x_2} = 1`, :math:`\theta = 1`
* Subtract AND with :math:`w_{\text{AND}} = -2` (not −1 — when both on, sum = 2 − 2 = 0 < threshold)

Step-by-step for unit 2 (OR minus 2·AND):

1. Set OR weights: :math:`w_{x_1} = w_{x_2} = 1`, :math:`\theta = 1` → fires if either input on
2. Add :math:`w_{\text{AND}} = -1`: fixes :math:`(1,1)` case? No — sum = 2 − 1 = 1 ≥ threshold still
3. Set :math:`w_{\text{AND}} = -2`: sum at :math:`(1,1)` = 2 − 2 = 0 < threshold → output 0 ✓
4. When AND off, unit acts as pure OR → correct for other three rows

Infinite solutions exist for XOR networks.

Perceptron Training
-------------------

Hand-set weights are impractical. Need learning from **training set**: examples :math:`(x, y)` where :math:`x` is a vector, :math:`y \in \{0,1\}`.

Two learning rules covered:

1. **Perceptron Rule** — uses thresholded outputs
2. **Gradient Descent / Delta Rule** — uses unthresholded activations

Both modify weights iteratively over the training set.

The Bias Trick
~~~~~~~~~~~~~~

Instead of learning :math:`\theta` separately, fold it into weights:

* Add **bias unit** with input always **1**
* Weight on bias = :math:`-\theta`
* Compare activation to **0** instead of :math:`\theta`

This unifies threshold and weight learning.

Perceptron Rule
~~~~~~~~~~~~~~~

For each training example :math:`(x, y)`:

.. math::

   \hat{y} = \begin{cases} 1 & \text{if } w \cdot x \geq 0 \\ 0 & \text{otherwise} \end{cases}

.. math::

   \Delta w_i = \eta \,(y - \hat{y})\, x_i

:math:`\eta` = **learning rate** (small step to avoid overshooting).

| :math:`y` | :math:`\hat{y}` | :math:`y - \hat{y}` | Weight change |
|----------|----------------|---------------------|---------------|
| 0 | 0 | 0 | none (correct) |
| 1 | 1 | 0 | none (correct) |
| 0 | 1 | −1 | decrease (sum too large) |
| 1 | 0 | +1 | increase (sum too small) |

When wrong: large :math:`x_i` values cause larger weight adjustments in the corrective direction.

**Training loop** (while error exists):

::

   for each (x, y) in training set:
       compute y_hat = threshold(w · x)
       for each weight i:
           w_i ← w_i + η (y - y_hat) x_i
   stop when all examples classified correctly

Linear Separability
~~~~~~~~~~~~~~~~~~~

* If a half-plane separates positive (green) from negative (red) examples → data is **linearly separable**
* **Perceptron Rule guarantee**: converges in **finite iterations** for linearly separable data
* After convergence: :math:`y - \hat{y} = 0` always → weights stop changing
* If **not** separable: algorithm never stops (unless you add a stop-on-zero-error condition)
* Cannot generally detect non-separability — would require solving halting problem in worst case
* Practical check: run algorithm; if it stops → separable; if not after long run → inconclusive

Gradient Descent (Delta Rule)
-----------------------------

Need a learning algorithm **robust to non-linear separability**.

Instead of thresholding during training, minimize error on **continuous activation** :math:`a = w \cdot x`.

Error Metric
~~~~~~~~~~~~

.. math::

   E(w) = \tfrac{1}{2} \sum_{d \in D} \bigl(y_d - a_d\bigr)^2

The :math:`\tfrac{1}{2}` is a constant for minimization but cancels the exponent in the derivative.

Partial Derivative
~~~~~~~~~~~~~~~~~~

Chain rule on :math:`E` w.r.t. :math:`w_i`:

.. math::

   \frac{\partial E}{\partial w_i} = \sum_{d \in D} (a_d - y_d)\, x_{d,i}

Only the term matching :math:`w_i` survives (other weights' derivatives = 0).

Weight Update
~~~~~~~~~~~~~

Move opposite to gradient:

.. math::

   \Delta w_i = \eta \,(y - a)\, x_i

**Derivation sketch**:

.. math::

   E = \tfrac{1}{2} \sum_d (y_d - a_d)^2, \quad a_d = \sum_j w_j x_{d,j}

.. math::

   \frac{\partial E}{\partial w_i} = \sum_d (a_d - y_d)\, x_{d,i}
   \quad \Rightarrow \quad
   \Delta w_i = -\eta \frac{\partial E}{\partial w_i} = \eta (y - a)\, x_i

Note: derivative of :math:`w_i` w.r.t. terms where :math:`j \neq i` is zero — only matching input :math:`x_i` contributes.

Comparison of Learning Rules
----------------------------

+---------------------------+----------------------------------+----------------------------------+
|                           | **Perceptron Rule**              | **Gradient Descent (Delta Rule)** |
+===========================+==================================+==================================+
| Output used               | thresholded :math:`\hat{y}`      | continuous :math:`a`             |
| Convergence             | finite, if linearly separable    | limit only; local optimum        |
| Non-separable data        | fails / never stops              | more robust                      |
| Similarity              | same form except thresholding    | same form except thresholding    |
+---------------------------+----------------------------------+----------------------------------+

Why Not Gradient Descent on :math:`\hat{y}`?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We want :math:`\hat{y}` (thresholded output) to match target, not raw activation :math:`a`. But gradient descent on :math:`\hat{y}` fails because:

| Possible reason | Valid? |
|----------------|--------|
| Computationally intractable | No |
| **Not differentiable** (step at 0) | **Yes** |
| Weights grow too fast / unstable | No |
| Multiple ill-defined answers | No |

:math:`\hat{y}` is a **step function**:

* Derivative = 0 everywhere except **undefined** at the jump (activation = 0)
* Zero derivative gives no direction to fix weights
* The "pointy spot" at zero is what makes it non-differentiable

**Solution**: replace step with a **smooth, differentiable** activation (softened threshold).

Sigmoid Activation
------------------

**Sigmoid** (:math:`\sigma`, "s-shaped"):

.. math::

   \sigma(a) = \frac{1}{1 + e^{-a}}

Properties:

* :math:`a \to -\infty`: :math:`e^{-a} \to \infty` → :math:`\sigma(a) \to 0`
* :math:`a \to +\infty`: :math:`e^{-a} \to 0` → :math:`\sigma(a) \to 1`
* Gradual S-curve between ≈−5 and ≈+5 (vs. abrupt threshold)
* **Differentiable** → gradient descent applicable

At :math:`a = 0`:

.. math::

   1 / (1 + e^0 ) = 1 / (1 + 1) = 1 / 2

**Derivative** (elegant closed form):

.. math::

   \sigma'(a) = \sigma(a)\,\bigl(1 - \sigma(a)\bigr)

* At :math:`a = 0`: :math:`\sigma'(0) = \tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}`
* Derivative flattens at extreme activations (near 0 or 1)
* Other smooth threshold functions exist with same general shape

Sigmoid behavior summary:

| Activation :math:`a` | :math:`\sigma(a)` | :math:`\sigma'(a)` |
|---------------------|-------------------|-------------------|
| :math:`-\infty` | → 0 | → 0 |
| −5 | ≈ 0 | ≈ 0 |
| 0 | 0.5 | 0.25 |
| +5 | ≈ 1 | ≈ 0 |
| :math:`+\infty` | → 1 | → 0 |

Neural Network Architecture
---------------------------

Construct **networks** of sigmoid units:

* **Input layer** — components of :math:`x`
* **Hidden layer(s)** — intermediate units (not directly observed)
* **Output layer** — :math:`y`

Each unit: weighted sum of previous layer → sigmoid → output to next layer.

**Back-propagation**:

* Full input→output mapping is **differentiable** in all weights
* Efficient **chain rule** organization: forward pass (inputs → outputs), then error flows **backward**
* Computes all weight gradients; updates weights to reduce error
* Also called **error back-propagation**

Any **differentiable** activation enables this (not just sigmoid).

* Sigmoid units are **analogous to** perceptrons but not identical — no hard threshold, no finite convergence guarantee
* Replacing sigmoid with any other differentiable function still permits back-propagation

Back-Propagation Details
~~~~~~~~~~~~~~~~~~~~~~~~

At its heart, back-propagation is a computationally beneficial organization of the **chain rule**:

1. **Forward pass**: compute activations layer by layer, inputs → outputs
2. **Compute error** at output (difference from target)
3. **Backward pass**: propagate error signals back through network
4. Each weight's gradient tells how much to adjust to reduce error
5. Update all weights simultaneously via gradient descent

The "back" in back-propagation refers to error flowing from outputs toward inputs.

Local Optima
~~~~~~~~~~~~

Unlike single-unit parabolic error surface, multi-layer networks create complex error landscapes:

* Smooth but many valleys — can get stuck in **local optima**
* No finite-time convergence guarantee
* Weights at a local minimum: any single-weight change increases error, but joint changes might find better solution

Optimizing Weights & Overfitting
--------------------------------

Gradient descent can get stuck in **local minima**. Advanced optimization:

* **Momentum** — continue past shallow minima (physical analogy: roll through small hills)
* Higher-order derivatives (Hessian-based methods)
* **Randomized optimization** (covered later in course)
* **Complexity penalties** — penalize overly complex structure

Overfitting in Neural Nets
~~~~~~~~~~~~~~~~~~~~~~~~~~

Same issue as regression (polynomial order) and decision trees (tree size / depth):

| Source of complexity | Effect |
|---------------------|--------|
| More **nodes** | Richer mapping, more local minima, can fit noise |
| More **layers** | Same |
| Large **weight magnitudes** | Same architecture but more complex effective function |

Decision tree analogy for overfitting:

* Let tree grow too deep → explains every quirk in data → overfits
* Remedies: **pruning**, depth limits, complexity penalty
* Neural nets: same idea via architecture limits, weight penalties, early stopping

Neural net failures (similar to overfitting):

* Stuck in local minima
* Weights growing too large
* Training too long without stopping criterion

**Cross-validation** selects: number of hidden layers, nodes per layer, when to **stop training**.

Training vs. Validation Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Training error drops monotonically with iterations
* Held-out / CV error may initially drop, then **rise** as weights grow
* Stop at minimum CV error — further training overfits even without changing architecture
* Weight magnitudes often grow at the turnaround point

Restriction Bias
----------------

**Restriction bias** = representational power of the hypothesis class (what functions can be represented).

| Stage | Restriction | Can represent |
|-------|-------------|---------------|
| Single perceptron | Linear only | Half-planes |
| Perceptron network | Compositional | XOR, all Boolean functions |
| Sigmoid network, many units | Weak restriction | Very general mappings |

**Universal approximation**:

* **Continuous functions** (no discontinuities): **1 hidden layer** with enough units — each unit models a patch, output layer stitches patches
* **Arbitrary functions** (including discontinuous): **2 hidden layers** with enough units — patches can have jumps between them

Neural nets in general: **not very restrictive** → high overfitting risk.

Any **fixed architecture** (bounded layers/units) does impose restriction — cannot capture every arbitrary function.

Preference Bias
---------------

**Preference bias** = what the **learning algorithm** prefers among representable hypotheses.

Weight Initialization
~~~~~~~~~~~~~~~~~~~~~

* Must initialize weights (cannot start undefined)
* Typical: **small random values**
* Random: no reason to prefer one region; variability across runs; helps avoid identical local minima
* Small: start with low complexity; large weights → overfitting risk

Preferences
~~~~~~~~~~~

1. **Correct** over incorrect
2. **Simpler** over complex (when error equal)
3. Start simple → allow complexity only as training progresses and error demands it
4. Stop before weights grow too large (cross-validation)

Occam's Razor
~~~~~~~~~~~~~

"Entities should not be multiplied unnecessarily."

* Don't increase complexity unless it improves fit
* If two hypotheses have similar error → choose the simpler one
* Formalized in supervised learning → better **generalization**

Neural Nets vs Other Supervised Learners
----------------------------------------

| Property | Decision Trees | Regression | Neural Networks |
|----------|---------------|------------|-----------------|
| Build process | Construct tree, then may overfit | Solve closed form, may overfit | **Iterative** training; error drops over iterations |
| Overfitting signal | Tree too big | Polynomial too high | Weights too large; train too long |
| Stop criterion | Pruning / CV | CV on polynomial degree | CV on architecture + **stop training** at CV minimum |
| Unique aspect | — | — | Complexity in weight **magnitude**, not just structure |

Perceptron vs Sigmoid — Comparison
----------------------------------

| Property | Perceptron (hard threshold) | Sigmoid unit |
|----------|----------------------------|--------------|
| Output | 0 or 1 (discrete) | :math:`(0, 1)` continuous |
| Differentiable | No | Yes |
| Linear separability | Required for Perceptron Rule | Not required for gradient descent |
| Convergence | Finite (if separable) | Asymptotic to local minimum |
| Composition | Boolean circuits | Universal approximator (enough units) |

Summary
-------

* **Perceptron**: linear sum + threshold; half-plane; Perceptron Rule converges if linearly separable
* **Boolean logic**: AND, OR, NOT via single units; XOR needs network
* **Gradient descent**: continuous activation; robust to non-separability; local optima only
* **Sigmoid**: smooth differentiable threshold; :math:`\sigma'(a) = \sigma(a)(1-\sigma(a))`
* **Back-propagation**: chain rule through network; error flows backward
* **Overfitting**: control architecture, weight magnitude, training duration (CV)
* **Bias**: weak restriction + preference for simple correct solutions
