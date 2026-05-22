Probability
===========

Fundamentals
------------

Probability theory provides the formal framework for reasoning under uncertainty.

**Key notation:**

* :math:`P(X)` — prior probability of event :math:`X`
* :math:`P(X|Y)` — conditional probability of :math:`X` given :math:`Y`
* :math:`P(\neg X) = 1 - P(X)` — complement rule

**Negation of conditionals:**

.. math::

   P(\neg X | Y) = 1 - P(X | Y)

The negation applies only to the query variable. You **cannot** negate the conditioning variable and assume probabilities sum to 1: :math:`P(X|Y) + P(X|\neg Y) \neq 1` in general.

Independence
~~~~~~~~~~~~

Two events :math:`X, Y` are independent iff:

.. math::

   P(X, Y) = P(X) \cdot P(Y)

Equivalently, :math:`P(X|Y) = P(X)`.

Total Probability
~~~~~~~~~~~~~~~~~

For any random variable :math:`Y` and a partition :math:`\{X_i\}`:

.. math::

   P(Y) = \sum_i P(Y | X_i) \cdot P(X_i)

This is the primary tool for computing marginal probabilities when direct computation is intractable.

Bayes Rule
----------

The central identity for diagnostic reasoning:

.. math::

   P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}

**Components:**

* :math:`P(A)` — **prior** (belief before evidence)
* :math:`P(B|A)` — **likelihood** (probability of evidence given cause)
* :math:`P(B)` — **marginal likelihood** (normalizer)
* :math:`P(A|B)` — **posterior** (updated belief after evidence)

Bayes rule converts **diagnostic reasoning** (evidence → cause) into **causal reasoning** (cause → evidence), corrected by the prior and normalized by the evidence.

The normalizer is typically expanded via total probability:

.. math::

   P(B) = \sum_a P(B | A = a) \cdot P(A = a)

Conditional Probability Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given:

::

   P(X) = 0.03
   P(¬Y | X) = 0.01
   P(Y | ¬X) = 0.1

   P(X | Y) = ?

   P(Y | X) = 1 - P(¬Y | X) = 1 - 0.01 = 0.99

   P(Y) = P(Y|X)·P(X) + P(Y|¬X)·P(¬X)
        = 0.99 × 0.03 + 0.1 × 0.97
        = 0.1267

   P(X | Y) = (0.99 × 0.03) / 0.1267
            = 0.2344

Cancer Test Example
~~~~~~~~~~~~~~~~~~~

Setup: :math:`P(C) = 0.01`, :math:`P(+|C) = 0.9`, :math:`P(+|\neg C) = 0.2`.

::

   P(C | +) = P(+ | C) · P(C) / P(+)
            = (0.9 × 0.01) / (0.009 + 0.198)
            = 0.009 / 0.207
            = 0.0435

Despite a 90% sensitive test, the posterior :math:`P(C|+) \approx 0.043` because the prior :math:`P(C) = 0.01` is very small — the base rate dominates.

Bayes Networks Overview
-----------------------

A Bayes network is a compact representation of a joint probability distribution over many variables. It encodes conditional independence relationships as a directed acyclic graph (DAG).

* Nodes represent random variables
* Edges represent direct probabilistic dependencies
* Each node stores a conditional probability table (CPT) given its parents

Given observed evidence variables, we can compute posterior distributions over unobserved query variables using the network structure.

Reference
=========

* http://sites.nicholas.duke.edu/statsreview/probability/jmc/
