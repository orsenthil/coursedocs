Bayes Nets
==========

Bayes nets combine probability with efficient graph structures to model how uncertain variables influence each other.

**Notation:** Capital letters denote variables; lowercase denotes the variable being true; a leading :math:`\neg` denotes false.

Structure and Parameters
------------------------

A Bayes network is a directed acyclic graph (DAG) where:

* Each node is a random variable with a conditional probability table (CPT)
* Edges encode direct causal/probabilistic dependencies
* The full joint distribution factorizes as:

.. math::

   P(X_1, \ldots, X_n) = \prod_i P(X_i \mid \text{Parents}(X_i))

For a single binary variable with one binary parent, we need three parameters: :math:`P(\text{evidence})`, :math:`P(\text{child} | \text{parent})`, and :math:`P(\text{child} | \neg\text{parent})`.

Computing Bayes Rule
~~~~~~~~~~~~~~~~~~~~

Compute the unnormalized posterior, then normalize:

.. math::

   P'(A|B) = P(B|A) \cdot P(A)

.. math::

   P(A|B) = \frac{P'(A|B)}{P'(A|B) + P'(\neg A|B)}

This avoids computing :math:`P(B)` directly — the normalizer is recovered from the unnormalized terms themselves.

Two-Test Cancer Example
~~~~~~~~~~~~~~~~~~~~~~~

Given :math:`P(C) = 0.01`, :math:`P(+|C) = 0.9`, :math:`P(+|\neg C) = 0.2`, and two conditionally independent positive tests:

::

   P(C | ++) = ?

   P'(C|++)  = P(+|C) · P(+|C) · P(C)    = 0.9 × 0.9 × 0.01
   P'(¬C|++) = P(+|¬C) · P(+|¬C) · P(¬C) = 0.2 × 0.2 × 0.99

   P(C|++) = P'(C|++) / [P'(C|++) + P'(¬C|++)]

   n1 = 0.9 × 0.9 × 0.01
   d1 = 0.2 × 0.2 × 0.99
   P(C|++) = n1 / (n1 + d1) = 0.1698

Two positive tests raise the posterior from ~4.3% (one test) to ~17%.

Conditional Independence
------------------------

Conditional independence is the central structural property of Bayes networks.

:math:`X \perp Y \mid Z` means :math:`X` and :math:`Y` are conditionally independent given :math:`Z`:

.. math::

   P(X, Y \mid Z) = P(X \mid Z) \cdot P(Y \mid Z)

**Key pattern — common cause** (:math:`B \leftarrow A \rightarrow C`):

* **Without** observing :math:`A`: :math:`B` and :math:`C` are independent
* **Given** :math:`A`: :math:`B` and :math:`C` become dependent (both conditioned on the common cause)

To verify conditional independence computationally, apply total probability to marginalize hidden variables and check whether the joint factors into marginals.

Absolute vs. Conditional Independence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Absolute independence (:math:`X \perp Y`) and conditional independence (:math:`X \perp Y \mid Z`) are distinct properties. Neither implies the other.

Confounding Cause
~~~~~~~~~~~~~~~~~

When two effects share a common hidden cause (fork: :math:`B \leftarrow A \rightarrow C`), the effects appear correlated. Conditioning on the cause :math:`A` renders them independent.

Explaining Away
~~~~~~~~~~~~~~~

When two independent causes produce a common effect (collider: :math:`A \rightarrow C \leftarrow B`):

* **Before** observing :math:`C`: :math:`A \perp B` (causes are marginally independent)
* **After** observing :math:`C`: :math:`A \not\perp B \mid C` (knowing the effect makes the causes dependent — observing one "explains away" the other)

This extends transitively: observing any descendant of the collider also activates the dependency between the causes.

D-Separation
------------

D-separation determines conditional independence in a Bayes network from graph structure alone.

**Triplet types** (for path :math:`X - Z - Y`):

.. list-table::
   :header-rows: 1
   :widths: 30 20 20

   * - Structure
     - :math:`Z` unknown
     - :math:`Z` known
   * - Causal chain: :math:`X \to Z \to Y`
     - Active (dependent)
     - Inactive (independent)
   * - Common cause: :math:`X \leftarrow Z \to Y`
     - Active (dependent)
     - Inactive (independent)
   * - Common effect: :math:`X \to Z \leftarrow Y`
     - Inactive (independent)
     - Active (dependent)

**Rules:**

* **Active triplets** → variables are **dependent**
* **Inactive triplets** → variables are **independent**
* Two nodes are d-separated (conditionally independent) given evidence :math:`E` iff **every** undirected path between them contains at least one inactive triplet

Probabilistic Inference
-----------------------

Given a Bayes network, inference answers queries of the form :math:`P(Q \mid E = e)` where:

* **Query variables** :math:`Q` — what we want to compute
* **Evidence variables** :math:`E` — what we observe
* **Hidden variables** :math:`H` — neither query nor evidence; must be marginalized out

The output is a probability distribution over the query variables.

Inference is direction-sensitive: networks flowing from causes to effects are easier to reason about.

Enumeration
~~~~~~~~~~~

Enumerate all possible assignments to hidden variables:

.. math::

   P(Q \mid e) = \alpha \sum_{h} \prod_i P(x_i \mid \text{Parents}(x_i))

where :math:`\alpha` is the normalizing constant and the product is over all variables evaluated at their assigned values.

Define :math:`f(e, a)` as the product of all relevant CPT entries for a particular assignment. The final answer sums :math:`f` over all :math:`2^n` joint assignments of :math:`n` binary hidden variables.

**Optimization — pulling out terms:** Factor terms that don't depend on the innermost summation variable outside the sum. This reduces the cost per row (though the number of rows stays the same).

Variable Elimination
~~~~~~~~~~~~~~~~~~~~

Exact inference is NP-hard in general. Variable elimination improves on enumeration by:

1. Choosing a variable to eliminate (marginalize out)
2. Computing a **factor** by summing over that variable in relevant CPTs
3. Replacing the original terms with the smaller factor
4. Repeating until only query variables remain

Each elimination step shrinks the effective network. With a good elimination ordering, variable elimination is significantly more efficient than full enumeration — though finding the optimal ordering is itself NP-hard.

Approximate Inference — Sampling
--------------------------------

When exact inference is intractable, sampling methods provide approximate answers.

Direct Sampling
~~~~~~~~~~~~~~~

Sample each variable in topological order from its CPT given its parents' sampled values. Count outcomes to estimate any probability.

* In the limit of infinite samples, estimates converge to true probabilities (**consistency**)
* Works for full joint distributions or individual marginals
* Does not require knowing the conditional probabilities analytically — just the ability to sample from the process

Rejection Sampling
~~~~~~~~~~~~~~~~~~

To estimate :math:`P(Q \mid E = e)`: generate samples from the full joint, **reject** any sample where evidence variables don't match :math:`e`, and count query outcomes in accepted samples.

**Problem:** When evidence is unlikely, most samples are rejected — exponentially inefficient.

Likelihood Weighting
~~~~~~~~~~~~~~~~~~~~

Fix evidence variables to their observed values; sample only non-evidence variables. Weight each sample by:

.. math::

   w = \prod_{e_i \in E} P(e_i \mid \text{Parents}(e_i))

Use weighted counts to estimate the posterior. This is a **consistent** estimator and avoids rejecting any samples.

**Limitation:** Only accounts for evidence upstream of query variables in the sampling order; downstream evidence is handled through weights, not the sampling distribution itself.

Gibbs Sampling
~~~~~~~~~~~~~~

A Markov Chain Monte Carlo (MCMC) method that accounts for **all** evidence:

1. Initialize all non-evidence variables randomly
2. Repeat: pick one non-evidence variable, resample it conditioned on its **Markov blanket** (parents, children, and children's other parents)
3. After a burn-in period, collect samples

**Properties:**

* Considers both upstream and downstream evidence via the Markov blanket
* Successive samples are correlated (not independent)
* Consistent — converges to the true distribution in the limit
