Regression
==========

**What is regression?**
- In ML: **function approximation** — map continuous inputs to continuous outputs (supervised).
- Name origin: Galton's **"regression to the mean"** — tall parents' children tend shorter than parents but taller than population mean; slope of parent–child height line **< 1**.
- Historical term stuck; ML **regression** = fit a functional form to data points (not psychological "regressing").

Regression and Function Approximation
-------------------------------------

- Parent height vs average child height: approximately **linear** relationship; slope **2/3** in real populations → children regress toward mean.
- Modern use: find mathematical relationship from measurements (coefficients :math:`C_0, C_1, \ldots`).

Linear Regression
-----------------

- Example: **housing price** vs square footage (synthetic 9 points, 1k–10k sq ft).
- **Best-fit line** minimizes **sum of squared errors** between points and line.
- Interpolation at 5k sq ft may disagree with line vs eyeballing neighbors.

Finding the Best Fit
--------------------

- **Error**: sum of squared distances from points to fitted curve.
- Many **loss functions** exist (absolute, squashed, …); **squared error** is smooth → **calculus** finds minimum.

**Best constant** (:math:`k=0`)
- Hypothesis: :math:`f(x) = C` for all :math:`x`.
- Error: :math:`E(C) = \sum_i (C - y_i)^2`.
- Derivative, set to zero → **:math:`C = \frac{1}{n}\sum_i y_i`** (mean of :math:`y`).
- Squared loss brings the **mean** back; same idea generalizes to lines and higher-order polynomials.

Order of the Polynomial
-----------------------

Polynomial family:

.. math::

   f(x) = C_0 + C_1 x + C_2 x^2 + \cdots + C_k x^k

- :math:`k=0`: constant (mean); :math:`k=1`: line; :math:`k=2`: parabola — often better fit on housing data.
- Higher :math:`k` (up to :math:`n-1` with :math:`n` points) → training error ↓; **order 8** can hit every point (zero training error) but **wild oscillations** between points (e.g. near 9000 sq ft).
- More degrees of freedom always ≥ nested lower-order fit (can zero higher coefficients).

**Quiz: pick degree for housing**
- Degree **3 (cubic)**: good fit without over-committing; degree **8** overfits noise.
- Degree 0/1/2 leave substantial error; cubic stays between points sensibly.

Polynomial Regression (matrix form)
-----------------------------------

For :math:`n` examples :math:`(x_i, y_i)`, find :math:`C_0,\ldots,C_3` for cubic regression:

.. math::

   \mathbf{X} \mathbf{w} \approx \mathbf{y}

- Rows of :math:`\mathbf{X}`: powers :math:`[1, x_i, x_i^2, x_i^3]`; :math:`\mathbf{w}` = coefficients.
- **Least squares** solution:

.. math::

   \mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}

- Equivalent to **projection** minimizing squared error; arrange data into :math:`\mathbf{X}`, compute :math:`\mathbf{w}`.

Errors
------

Observed :math:`y` = true function + **noise**. Common sources (all realistic):

| Source | Description |
|--------|-------------|
| **Sensor error** | Physical measurement noise |
| **Malicious / bad faith** | Adversarial or misrepresented data |
| **Transcription error** | Human typos, digit swaps |
| **Unmeasured factors** | Housing: location, quality, interest rates — not just size |

Goal: fit **signal**, not **noise**.

Cross Validation
----------------

- **Goal**: **generalize** to unseen data; test set is a stand-in for the future.
- **IID assumption**: training, validation, and future data drawn from same distribution (fundamental for many algorithms).
- **Cheating**: training on the test set → great test error, poor generalization.
- **Hold-out / cross-validation set**: reserve part of training data as fake test set.
- **K-fold CV**: split training into **folds**; train on :math:`k-1` folds, evaluate on held-out fold; rotate and **average** errors; pick model class (e.g. polynomial degree) with lowest average CV error.

**Underfitting vs overfitting**
- Too simple → **underfit** (high error, misses structure).
- Too complex → **overfit** (fits training noise; high error on unseen data).
- Sweet spot: complex enough for structure, not so complex that error is modeled.

Housing Example Revisited
-------------------------

- **Training error** (red): decreases monotonically as polynomial degree ↑ (nested models).
- **Cross-validation error** (blue): starts higher (predicting held-out points); tracks training at low degree; **rises** at high degree (inverted-U / overfitting).
- Best degree by CV: **3** (close to 4; order 4 nearly zeros quartic term but generalizes slightly worse).

Other Input Spaces
------------------

**Vector inputs**
- Multiple continuous features (e.g. size + distance to zoo) → **planes / hyperplanes** in feature space.
- Polynomial regression generalizes to multivariate features.

**Discrete / categorical inputs**
- Boolean (job yes/no): encode as **0/1**.
- Count (houses owned): scalar.
- **Nominal** (hair color, job type): **one-hot** vectors preferred over arbitrary numeric codes (avoids false order, e.g. blonde "between" brown and black).
- **RGB encoding** of colors still implies ordering if multiplied by a scalar coefficient — same pitfall as 1,2,3,… labels.

**Squared-error minimization (sketch)**
- For constant :math:`C`: :math:`E(C)=\sum_i(C-y_i)^2`.
- :math:`\frac{dE}{dC} = \sum_i 2(C-y_i)`; set to 0 → :math:`nC = \sum_i y_i`.
- For line :math:`y = mx + b`: same calculus over two parameters (or matrix least squares).
- Alternatives to calculus: **hill climbing** on slope/intercept; **random search** — squared loss preferred for closed form.

**Polynomial orders on housing data**
- Order 0: horizontal line at mean price.
- Order 1: best line (green) — captures upward trend; under-predicts at 5k sq ft vs neighbors.
- Order 2: parabola — better tuck against points.
- Orders 4–6: tighter fit, follows curvature.
- Order 8 (max with 9 points): **zero training error**, hits every point; unstable between 9k–10k sq ft.
- Error vs degree plot: monotonic decrease in training SSE to 0 at degree 8.

**K-fold procedure (detail)**
1. Partition training set into :math:`k` folds.
2. For each fold :math:`i`: train on all folds except :math:`i`, evaluate SSE on fold :math:`i`.
3. Average fold errors → **cross-validation error** for that model class.
4. Select degree (or other hyperparameter) with lowest mean CV error.
5. Retrain on full training set with chosen hyperparameter before final test evaluation.

**Goldilocks / bias–variance**
- Underfit: high train + high CV error (model too weak).
- Overfit: low train, high CV error (model memorizes noise).
- Just right: train error still decreasing but CV error near minimum (degree 3 in housing plot).

**Conclusion**
- Regression: continuous outputs; squared loss + linear algebra for fitting; polynomial order and **cross-validation** control bias–variance; features can be scalar, vector, or encoded discrete.
