Bayesian Learning
=================

Revision reference for **MAP/ML learning**, **Bayes' rule**, noise models, **MDL**, and **Bayesian classification**.

Introduction
------------

**Bayesian learning goal**: find the **most probable hypothesis** given data and domain knowledge.

.. math::

    \hat{h} = \arg\max_{h \in H} \Pr(h \mid D)

- **h**: hypothesis; **D**: training data; **Pr**: probability.

Bayes' Rule
-----------

.. math::

    \Pr(h \mid D) = \frac{\Pr(D \mid h) \cdot \Pr(h)}{\Pr(D)}

**Term meanings**:

+------------------+------------------+------------------------------------------+
| Term             | Name             | Role                                     |
+==================+==================+==========================================+
| **Pr(h|D)**      | Posterior        | What we want — belief in h after data    |
+------------------+------------------+------------------------------------------+
| **Pr(D|h)**      | Likelihood       | P(labels | h); often "run h on data"     |
+------------------+------------------+------------------------------------------+
| **Pr(h)**        | Prior            | Domain knowledge over hypotheses         |
+------------------+------------------+------------------------------------------+
| **Pr(D)**        | Evidence         | Normalizer; often ignored for argmax     |
+------------------+------------------+------------------------------------------+

**Likelihood intuition**: D = {(x_i, d_i)}. Pr(D|h) = probability of seeing labels d_i given inputs x_i if h were true.

Example: h(x) = true iff x ≥ 10. Data: x=7, label=true → Pr(D|h) = 0.

**Posterior increases when**: prior Pr(h) ↑ or likelihood Pr(D|h) ↑. Pr(D) ↓ also raises posterior but is not h-specific.

**Chain rule derivation**: P(A,B) = P(A|B)P(B) = P(B|A)P(A) → Bayes' rule.

**Prior as domain knowledge**: Pr(h) encodes beliefs before data — analogous to:

- **k-NN**: Euclidean distance assumes nearby points share labels.
- **Decision trees**: feature / information-gain preferences.
- **Neural nets**: architecture choices.

**When Pr(h|D) increases**: higher Pr(h), higher Pr(D|h), or lower Pr(D).

Bayes' Rule Quiz: Rare Disease
------------------------------

**Spleentitis** test: sensitivity 98%, specificity 97%, prevalence 0.8%. Patient tests **positive**. P(disease | +)?

.. math::

    P(S \mid +) \propto P(+ \mid S) \cdot P(S) = 0.98 \times 0.008 = 0.00784

.. math::

    P(\neg S \mid +) \propto P(+ \mid \neg S) \cdot P(\neg S) = 0.03 \times 0.992 = 0.02976

→ **P(S|+) ≈ 21%** — more likely **no disease** despite accurate test.

**Lesson**: **priors matter**. Test useful only when prior is high enough (screen high-risk populations, not random walk-ins).

MAP and Maximum Likelihood
--------------------------

**MAP algorithm**:

1. For each h ∈ H: score ∝ Pr(D|h) · Pr(h)
2. Return h with maximum score.

Drop Pr(D) for argmax (constant w.r.t. h).

**Maximum A Posteriori (MAP)**: uses both likelihood and **prior** Pr(h).

**Maximum Likelihood (ML)**: uniform prior over H → maximize Pr(D|h) only.

.. math::

    \hat{h}_{ML} = \arg\max_h \Pr(D \mid h)

- MAP = domain knowledge in prior; ML = all hypotheses equally likely a priori.
- Conceptual gold standard but **intractable** when |H| is large or infinite (e.g., linear separators).

Bayesian Learning: Noise-Free Version Space
-------------------------------------------

**Assumptions**: noise-free labels d_i = c(x_i); true concept c ∈ H; **uniform prior** over H.

- Pr(h) = 1/|H|
- Pr(D|h) = 1 if h consistent with all labels, else 0
- Pr(D) = |VS| / |H| where VS = version space (consistent hypotheses)

.. math::

    \Pr(h \mid D) = \begin{cases} 1/|VS| & h \in VS \\ 0 & \text{otherwise} \end{cases}

→ All consistent hypotheses **equally probable** → pick any h ∈ VS (matches earlier learning-theory advice).

**Derivation sketch**:

.. math::

    \Pr(D) = \sum_{h_i \in H} \Pr(D \mid h_i)\,\Pr(h_i) = \sum_{h_i \in VS} 1 \cdot \frac{1}{|H|} = \frac{|VS|}{|H|}

Substitute into Bayes' rule → uniform over VS.

Noisy Data Quiz
---------------

True process: label = k · x with P(k) = 1/2^k (geometric). Hypothesis h(x) = x (identity).

Data: (1,5), (3,6), (11,11), (12,36), (20,100).

.. math::

    \Pr(D \mid h) = \prod_i \frac{1}{2^{d_i / x_i}} \quad \text{if } d_i \bmod x_i = 0 \text{, else } 0

Example: (1,5) → k=5 → 1/32; product over all i = **1/65536**.

**IID** labels → product of per-example likelihoods.

Gaussian Noise → Sum of Squared Errors
--------------------------------------

**Setup**: d_i = f(x_i) + ε_i, ε_i ~ N(0, σ²) i.i.d.; f unknown; h approximates f.

**ML hypothesis** maximizes ∏_i Pr(d_i | h, x_i). Gaussian likelihood:

.. math::

    \Pr(d_i \mid h, x_i) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(h(x_i) - d_i)^2}{2\sigma^2}\right)

Take log, drop constants, flip max to min:

.. math::

    \hat{h}_{ML} = \arg\min_h \sum_i (h(x_i) - d_i)^2

→ **Minimizing sum of squared errors (SSE)** = ML under **zero-mean Gaussian noise** on outputs.

**Derivation steps**:

1. ML: argmax_h ∏ᵢ Pr(dᵢ | h, xᵢ)
2. Log → sum of log-Gaussians
3. Drop constants (1/√2πσ²) and σ² inside argmax
4. log exp(·) → sum of squared residuals with negative sign
5. argmax → **argmin** Σ(h(xᵢ) − dᵢ)²

**Assumptions baked in**:

- Deterministic f plus i.i.d. Gaussian ε (same σ).
- Noise on outputs only (not on inputs) — if x also noisy, SSE may be wrong model.
- Different noise models → different loss functions.

Best Hypothesis Quiz
--------------------

Uniform prior over {constant, linear, mod-9}. SSE picks **mod-9** for given data (lowest error), beating best linear regression — SSE does not prefer simpler models without explicit penalty.

**Quiz data** (x → d): (1,1), (2,2), (3,3), (9,9), (10,1), (11,2) — mod-9 fits local structure; best linear reg SSE ≈ 15.8; constant ≈ 19; mod-9 SSE = **12**.

Minimum Description Length (MDL)
--------------------------------

Apply log base 2 to MAP (monotonic → same argmax), negate to minimize:

.. math::

    \hat{h}_{MAP} = \arg\min_h \left[ -\log_2 \Pr(D \mid h) - \log_2 \Pr(h) \right]

**Information-theoretic interpretation** (optimal code length = −log₂ P):

- **−log₂ Pr(h)** = **description length of hypothesis** (bits to encode h).
- **−log₂ Pr(D|h)** ≈ **description length of data given h** (errors / mismatches must be transmitted).

→ MAP = minimize **error + model complexity** → **Occam's razor** / **MDL**.

- Shorter decision trees = smaller −log Pr(h) → prefer pruned/smaller trees.
- Large neural-net weights need more bits → complexity penalty links to overfitting.

**Minimum description length**: trade off fit vs simplicity; units of error vs size may need tuning.

Bayesian Classification vs MAP Hypothesis
-----------------------------------------

**Critical distinction**: goal is often best **label**, not best **hypothesis**.

Example: three hypotheses with P(h|D) = 0.4, 0.3, 0.3; labels on x: +, −, −.

- **MAP hypothesis** → h₁ → label **+**
- **Bayesian optimal label**: weighted vote over all h

.. math::

    P(\text{label} \mid D) = \sum_h \Pr(h \mid D) \cdot \Pr(\text{label} \mid h)

P(−) = 0.3 + 0.3 = **0.6** > P(+) = 0.4 → predict **−**.

**Bayesian classification**:

.. math::

    \hat{v} = \arg\max_v \sum_{h \in H} \Pr(h \mid D) \cdot \Pr(v \mid h)

Analogous to **boosting**, **weighted k-NN**: combine hypotheses by posterior weight, don't commit to single MAP h.

Summary
-------

+---------------------------+--------------------------------------------------+
| Concept                   | Key point                                        |
+===========================+==================================================+
| **Bayesian learning**     | argmax Pr(h|D)                                   |
+---------------------------+--------------------------------------------------+
| **Bayes' rule**           | Posterior ∝ likelihood × prior                 |
+---------------------------+--------------------------------------------------+
| **MAP vs ML**             | Prior vs uniform over H                          |
+---------------------------+--------------------------------------------------+
| **Noise-free**            | Uniform over version space                       |
+---------------------------+--------------------------------------------------+
| **Gaussian noise**        | ML = minimize SSE                                |
+---------------------------+--------------------------------------------------+
| **MDL / Occam**           | Minimize error + description length              |
+---------------------------+--------------------------------------------------+
| **Classification**        | Weighted vote over h, not MAP h alone            |
+---------------------------+--------------------------------------------------+
