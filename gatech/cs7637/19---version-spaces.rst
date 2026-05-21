.. title: 19 - Version Spaces 
.. slug: 19 - Version Spaces 
.. date: 2016-01-23 06:49:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

===================
19 - Version Spaces
===================

Overview
--------

**Version spaces** is a technique for incremental concept learning that converges on the correct concept characterization without requiring background knowledge or a teacher who orders examples. It maintains two boundary models — a most-specific and a most-general — and refines them as examples arrive until they converge.

Comparison with Incremental Concept Learning
---------------------------------------------

In incremental concept learning (e.g., learning "arch"):

- A teacher provides examples in a controlled order
- Each example differs from the current concept in exactly one feature, focusing the learner's attention
- Background knowledge guides generalization (e.g., knowing brick and wedge are both blocks)
- Positive examples → generalization; negative examples → specialization

Version spaces relaxes these requirements:

- Examples arrive in **arbitrary order**
- **No background knowledge** is needed to decide how far to generalize
- Examples may differ in **multiple features** simultaneously

The Generalization Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~

Without guidance, learners risk:

- **Under-generalization**: concept is correct but too narrow to transfer (e.g., "a dog is a four-legged furry black animal named Buddy")
- **Over-generalization**: concept is too broad and includes incorrect instances (e.g., "all four-legged furry animals are dogs" — includes cats)

Version spaces solves this by maintaining boundaries that provably converge given sufficient examples.

The Algorithm
-------------

The agent maintains two models:

- **Specific model (S)**: the most restrictive concept consistent with all positive examples seen so far
- **General model (G)**: the most permissive concept consistent with all negative examples seen so far

Processing rules:

1. **Positive example** → generalize S to include it; prune any G models that cannot be a generalization of the updated S
2. **Negative example** → specialize G to exclude it; prune any S models that cannot be a specialization of the updated G
3. **Prune** any model subsumed by another model on the same side

**Convergence** occurs when S and G become identical. The converged model is the learned concept.

Food Allergies Example
~~~~~~~~~~~~~~~~~~~~~~

Given visits to restaurants with features (restaurant, meal, day, cost) and an allergic/not-allergic label:

**Example 1** (positive): Sam's, breakfast, Friday, cheap

- S = {Sam's, breakfast, Friday, cheap}
- G = {any, any, any, any}

**Example 2** (negative): Kim's, lunch, Friday, expensive

- S unchanged (positive examples only affect S)
- Specialize G → {Sam's, any, any, any}, {any, breakfast, any, any}, {any, any, any, cheap} (prune {any, any, Friday, any} since it matches the negative example)

**Example 3** (positive): Sam's, lunch, Saturday, cheap

- Generalize S → {Sam's, any, any, cheap}
- Prune G: {any, breakfast, any, any} is inconsistent with this positive (lunch) example → removed
- G = {Sam's, any, any, any}, {any, any, any, cheap}

**Example 4** (negative): Bob's, breakfast, Saturday, cheap

- {any, any, any, cheap} must be specialized → {Sam's, any, any, cheap}
- {Sam's, any, any, any} already excludes Bob's → no change needed
- Prune: {Sam's, any, any, cheap} is subsumed by {Sam's, any, any, any} → prune the broader model
- G = {Sam's, any, any, cheap}

**Example 5** (negative): Sam's, dinner, Saturday, expensive

- Specialize {Sam's, any, any, any} → only valid specialization consistent with S is {Sam's, any, any, cheap}
- S = G = {Sam's, any, any, cheap} → **converged**

Result: allergic reactions occur at Sam's when the meal is cheap.

Key Properties
~~~~~~~~~~~~~~

- Convergence is **guaranteed** given sufficient examples, regardless of ordering
- No background knowledge or intelligent teacher required
- The number of examples needed depends on the concept complexity and feature space

Identification Trees
--------------------

An alternative to version spaces for the same type of data. Also called **decision trees**.

Unlike discrimination trees (learned incrementally, potentially suboptimal), identification trees are constructed with all examples available upfront, yielding more optimal classification.

Construction Process
~~~~~~~~~~~~~~~~~~~~

1. Select the feature that best separates positive from negative examples
2. Split examples by that feature's values
3. If a split contains only positive or only negative examples, it becomes a leaf
4. Otherwise, recurse on the remaining examples with remaining features

Choosing the Best Feature
~~~~~~~~~~~~~~~~~~~~~~~~~

The optimal feature creates splits where each branch contains only one class (all positive or all negative). Example with beach sunburn data (features: hair color, height, age, lotion):

- **Hair color** first: brown → no sunburn, red → sunburn, blonde → mixed
- **Lotion** second (for blondes): lotion → no sunburn, no lotion → sunburn
- Result: two features classify all nine examples

A suboptimal ordering (e.g., height first) produces a bushier, less efficient tree.

Trade-off with Version Spaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Decision trees**: more optimal classification but require all examples upfront
- **Version spaces**: learn incrementally but may need more processing
- **Discrimination trees** (from case-based reasoning): incremental but potentially suboptimal

Cognitive Connection
--------------------

Cognitive agents face the same generalization dilemma. Version spaces model **cognitive flexibility** — maintaining multiple viable concept characterizations simultaneously, converging over time. An alternative cognitive strategy is to commit to one generalization, test it in the world, and correct mistakes when they occur (mistake-based learning).
