VC Dimensions
=============

**Motivation: infinite hypothesis spaces**
- Prior sample bound (finite :math:`|\mathcal{H}|`):

.. math::

   m \ge \frac{1}{\epsilon}\left(\log|\mathcal{H}| + \log\frac{1}{\delta}\right)

- Need :math:`m` large when :math:`\epsilon` small (low error) or :math:`\delta` small (low failure probability).
- **Problem**: many hypothesis classes are **infinite** (e.g. real-valued parameters).


Which Hypothesis Spaces are Infinite
------------------------------------

| Hypothesis class | Infinite? |
|------------------|-----------|
| **Linear separators** (:math:`y = mx + b`, weights real) | Yes |
| **Neural networks** (real weights) | Yes |
| **Decision trees, discrete inputs** (finite features, no reuse) | No |
| **Decision trees, continuous inputs** (thresholds : 0.1, 0.11, …) | Yes |
| **k-NN** | Debatable: infinite layouts of neighbors; if data "baked in," effectively one classifier; often called **non-parametric** (= infinite parameters) |

Nearly everything discussed is infinite syntactically → need a different complexity measure.


Maybe It Is Not So Bad
----------------------

**Example**: :math:`\mathcal{X} = \{1,\ldots,10\}`, :math:`h_\theta(x) = \mathbf{1}[x \ge \theta]`, :math:`\theta \in \mathbb{R}` → **syntactically infinite** hypotheses.
- Only **11** semantically distinct behaviors (thresholds 1…10 and "all false").
- **Syntactic** :math:`\mathcal{H}`: all describable hypotheses; **semantic**: distinct input–output functions.
- Track only **meaningfully different** hypotheses, not every syntactic variant (same idea for decision trees re-splitting useless attributes).


Power of Hypothesis Space
-------------------------

**Question**: largest set of inputs the hypothesis class can label in **all** possible ways?

**Threshold classifier** on a line:
- One point: can label **+** and **−** → shatter size ≥ 1.
- Two points :math:`x_1 < x_2`: cannot get **(+ , −)** — everything left of :math:`\theta` is always negative.
- **VC dimension = 1** (weak / low expressiveness despite infinite syntactic class).


What Does VC Stand For?
-----------------------

- **Vapnik–Chervonenkis** (Vapnik & Chervonenkis).
- **Shattering**: hypothesis class **shatters** set :math:`S` if for every labeling of points in :math:`S`, some :math:`h \in \mathcal{H}` realizes it.
- **VC dimension** :math:`\mathrm{VC}(\mathcal{H})`: size of the **largest** set that can be shattered (or :math:`\infty\)).
- Finite VC dimension → finite sample complexity even if :math:`|\mathcal{H}| = \infty\).


Quiz: Intervals on the Real Line
--------------------------------

- Hypothesis: **interval** :math:`(a,b)` — positive inside, negative outside; :math:`a,b \in \mathbb{R}` → infinitely many hypotheses.
- VC = **2**:
  - **Lower bound**: two distinct points on line — all 4 labelings achievable.
  - **Upper bound**: three collinear points — pattern **+ − +** impossible (interval containing 1 and 3 must include middle).
- Proving VC ≥ :math:`d`: **∃** one set of :math:`d` points that shatters.
- Proving VC < :math:`d+1`: **∀** arrangements of :math:`d+1` points, **∃** some labeling no hypothesis achieves.


Quiz: Linear Separators in :math:`\mathbb{R}^2`
-----------------------------------------------

- Hypothesis: :math:`\mathbf{w} \cdot \mathbf{x} \ge \theta` → half-plane (line separator).
- VC = **3**:
  - 1 point: 2 labelings (flip :math:`\mathbf{w}\)).
  - 2 points: 4 labelings (line between them).
  - 3 non-collinear points (triangle): all 8 labelings (use slanted line for **+ − +** pattern).
  - 4 points: **XOR** labeling on square corners (+ on opposite corners) **not** linearly separable — fails for any layout (collinear / collapsed cases also fail).
- **:math:`d`-dimensional** linear separators: VC = **:math:`d+1`** (matches number of parameters: :math:`d` weights + :math:`\theta`).


Quiz: Convex Polygons in :math:`\mathbb{R}^2`
---------------------------------------------

- Hypothesis: points **inside** a convex polygon (on boundary counts as inside).
- Place :math:`n` points on a **circle**; for any labeling, connect **+** vertices → convex polygon; **−** points on circle stay outside ("rubber band" / omit vertex).
- Works for any :math:`n` → **VC dimension = :math:`\infty`** (unbounded parameters as sides grow).
- Circles alone have VC = 3; convex polygons are **more** expressive in this sense.
- Polygons with vertices on unit circle are **convex** by construction.


Sample Complexity
-----------------

Sufficient sample size (with probability :math:`1-\delta\), error ≤ :math:`\epsilon\)):

.. math::

   m \ge \frac{1}{\epsilon}\left(8 \cdot \mathrm{VC}(\mathcal{H}) \cdot \log_2\frac{13}{\epsilon} + 4 \log_2\frac{2}{\delta}\right)

- Same structure as finite case: **:math:`1/\epsilon\)** upfront; failure term **:math:`\log(1/\delta\)`**; hypothesis complexity via **VC dimension** (linear), not :math:`\log|\mathcal{H}|\).
- VC dimension plays role analogous to **:math:`\log|\mathcal{H}|\)** in finite bounds (VC not logged; size of finite class is).


VC Dimension of Finite Hypothesis Classes
---------------------------------------

- If :math:`\mathrm{VC}(\mathcal{H}) = D`, need ≥ :math:`2^D` distinct hypotheses (one per shattered labeling).
- So :math:`2^D \le |\mathcal{H}|` → **:math:`D \le \log_2|\mathcal{H}|`**.
- Connects finite and infinite analyses; constant **13** comes from proof details.

**PAC learnability**
- **:math:`\mathcal{H}`** is PAC-learnable **iff** **VC dimension is finite**.
- Finite VC → learnable (bound above); infinite VC → not PAC-learnable.
- VC dimension captures learnability in one quantity.


Intervals: Proof Checklist
--------------------------

**VC ≥ 1**: one point — bracket interval around it (+) or brackets only to one side (−).

**VC ≥ 2**: two points — four labelings:

| Labeling | Interval placement |
|----------|-------------------|
| ++ | Brackets around both |
| +− | Left bracket fixed; right bracket just right of second point |
| −+ | Mirror of +− |
| −− | Brackets outside both (left of first, right of second) |

**VC < 3**: for any three distinct collinear points, labeling **+ − +** fails — any interval containing first and third includes the middle.

**Logic of bounds**
- Lower bound (:math:`\mathrm{VC} \ge d`): **∃** one point set of size :math:`d` that shatters (**existential**).
- Upper bound (:math:`\mathrm{VC} < d+1`): **∀** point arrangements of size :math:`d+1`, **∃** a labeling no :math:`h \in \mathcal{H}` achieves (**for all** / **not exists**).


Linear Separators: Additional Arguments
---------------------------------------

**VC ≥ 3 in :math:`\mathbb{R}^2`**
- Collinear three points fail (+ − +) like 1D threshold — fix by placing third point off the line (triangle).
- Slanted line separates (+,−,+) pattern; flip weights for opposite labelings.
- Remaining 6 of 8 labelings: vertical line left of all (+,+) or (−,−); other cases reduce to 1D interval logic on an axis.

**VC < 4**
- **XOR** labeling on four corners of a square (or diamond): :math:`(0,0),(1,0),(0,1),(1,1)` with labels +,−,−,+.
- Any line putting both **+** corners on same side forces a **−** corner on that side too.
- **Convex hull** argument: interior point cannot differ from all exterior points if exterior share one label.
- Moving corners cannot fix XOR without collinear/coincident degeneracies (which also fail).

**Parameter-count heuristic ("the ring")**
- 1D threshold (:math:`\theta`): VC = 1.
- Interval (:math:`a, b`): VC = 2.
- 2D linear separator (:math:`\mathbf{w} \in \mathbb{R}^2`, :math:`\theta`): VC = 3 = #parameters.
- :math:`d`-dim hyperplane: VC = :math:`d+1` (:math:`d` weights + bias :math:`\theta`).


Convex Polygons: VC = ∞
-----------------------

- Points on a **unit circle**; labeling arbitrary **+**/**−** pattern.
- Connect **+** points as polygon vertices; omit **−** points from vertex set ("pop out" with rubber-band intuition).
- 1 point: degenerate polygon; 2 points: line segment (convex); all labelings realizable.
- :math:`n` can grow without bound → **unbounded VC dimension**.
- Vertices on circle ⇒ polygon **convex** (subtended by circle).
- Contrast: **circle** hypothesis class alone has VC = 3; convex polygons strictly more expressive.


Connecting to Original Sample Bound
-----------------------------------

| Finite :math:`|\mathcal{H}|` | Infinite / continuous :math:`\mathcal{H}` |
|-------------------------------|---------------------------------------------|
| :math:`\log|\mathcal{H}|` in bound | :math:`\mathrm{VC}(\mathcal{H})` (not logged) |
| Count hypotheses | Measure shattering power |
| PAC if finite | PAC iff finite VC |

- For finite :math:`\mathcal{H}`: :math:`\mathrm{VC}(\mathcal{H}) \le \log_2|\mathcal{H}|` because shattering :math:`D` points needs :math:`2^D` distinct hypotheses.
- Explains why finite bound logs hypothesis count while VC bound does not.


Summary
-------

- **Shattering** / **VC dimension**: expressiveness of hypothesis class.
- **Syntactic vs semantic** hypothesis spaces.
- VC often tracks **number of real parameters** (:math:`d+1` for :math:`d`-dim linear separators).
- **Compute VC**: prove lower bound with one shattered set; prove upper bound with one impossible labeling for all point arrangements.
- **Sample complexity**: VC replaces :math:`\log|\mathcal{H}|` for infinite classes.
- **PAC learnability** ↔ finite VC dimension.
