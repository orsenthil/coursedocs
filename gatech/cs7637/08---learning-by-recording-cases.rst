.. title: Learning by Recording Cases
.. slug: Learning by Recording Cases
.. date: 2016-01-23 06:38:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Learning by Recording Cases
===========================

Overview
--------

**Learning by recording cases** is a method where an agent stores past experiences (cases) in memory and uses them to solve new problems by finding the most similar stored case. This is the first topic in analogical reasoning, considered a core process of cognition.

A **case** is an encapsulation of a past experience — the problem encountered and the solution applied. When a new problem arrives, the agent retrieves the most similar case and applies its solution directly.

This method works across a wide range of situations, from tying shoelaces to medical diagnosis: a doctor faced with new symptoms retrieves the most similar past patient case and applies the same diagnosis.

Nearest Neighbor Method
-----------------------

The key challenge is operationalizing "most similar." The **nearest neighbor method** addresses this by:

1. Representing cases and the new problem as points in a feature space
2. Computing the distance between the new problem and each stored case
3. Selecting the case with the smallest distance

**Euclidean distance** in two dimensions between a case (x_c, y_c) and a new problem (x_n, y_n):

.. math::

   d = \sqrt{(x_c - x_n)^2 + (y_c - y_n)^2}

Example: In a world of colored blocks characterized by width and height, each block maps to a point on a 2D grid. A new block is plotted on the same grid, distances to all known blocks are computed, and the nearest block's color is assigned to the new one.

K-Nearest Neighbor in Higher Dimensions
---------------------------------------

Real-world problems require **multi-dimensional** feature spaces. The Euclidean distance generalizes to k dimensions:

.. math::

   d = \sqrt{\sum_{i=1}^{k}(f_i^{case} - f_i^{problem})^2}

Example: A navigation problem (go from origin to destination) requires four dimensions — x and y coordinates for both origin and destination. Comparing on origin alone might select case B; comparing on destination alone might select case E; but computing distance in the full 4D space correctly identifies case D as the overall best match.

This is the **KNN (k-nearest neighbor) method** — simple but powerful.

Limitations
-----------

- **High-dimensional spaces** — As dimensionality grows, determining which stored case is truly closest becomes increasingly difficult
- **Solution transfer** — Even when a new problem is close to an existing case, the old solution may not directly apply to the new problem
- **Qualitative features** — Many real-world cases involve qualitative labels rather than numeric features, making distance computation harder

These limitations motivate **case-based reasoning**, which adds adaptation and evaluation phases to handle cases where the retrieved solution needs modification.

Cognitive Connection
--------------------

Learning by recording cases has a strong connection to cognition:

- Cognitive agents are situated in a world with **patterns of regularity** — the same problems recur daily
- For routine tasks (e.g., tying shoelaces), memory supplies the answer directly without deliberative reasoning
- This shifts the balance in the reasoning-memory-learning triad: **memory and learning become primary**, reducing the need for active reasoning
- We don't think as much as we think we do — much of intelligent behavior is memory-driven retrieval rather than novel problem-solving


Resources
---------

* https://techtalktone.wordpress.com/2014/11/09/using-learning-by-recording-cases-to-solve-rpm/
