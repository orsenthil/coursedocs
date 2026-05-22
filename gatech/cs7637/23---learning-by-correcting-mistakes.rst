.. title: Learning by Correcting Mistakes
.. slug: Learning by Correcting Mistakes
.. date: 2016-01-23 06:53:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Learning by Correcting Mistakes
===============================


Introduction
------------

**Learning by correcting mistakes** occurs when an agent reaches an incorrect or suboptimal decision, identifies *why* the mistake happened, and corrects its own knowledge to prevent recurrence. This is the first lesson in meta-reasoning — the agent diagnoses itself rather than an external system.

The process follows three phases:

1. Detect that a failure occurred (via feedback from the world)
2. Isolate the knowledge element responsible (using explanation)
3. Repair the knowledge so the same error cannot recur


Credit Assignment
-----------------

**Credit assignment** (or blame assignment) is the problem of identifying which fault or gap in an agent's knowledge was responsible for a failure. Failures can stem from errors in:

- Knowledge (incorrect facts or concept definitions)
- Reasoning (flawed inference process)
- Architecture (structural limitations)

This lesson focuses on errors in classification knowledge. Credit assignment is considered by some (e.g., Marvin Minsky) to be the *central* problem in learning, because agents operate in dynamic worlds — even a perfect agent will eventually fail as the world changes and must be able to self-correct.


False and True Suspicious Features
-----------------------------------

Given a positive example (correctly classified) and a negative example (incorrectly classified as positive), we can visualize feature sets as overlapping circles:

- **Shared features**: present in both positive and negative examples (e.g., concave, has a handle) — not diagnostic
- **False suspicious features**: features present *only* in the negative example — one or more of these caused the agent to incorrectly accept the negative example
- **True suspicious features**: features present *only* in a positive example that was incorrectly rejected — one or more of these prevented correct classification

To narrow down which suspicious feature is responsible:

- Present additional positive/negative examples that cover subsets of the suspicious features
- Alternatively, try features one at a time and get feedback

This is analogous to the focus problem in incremental concept learning, where examples are ordered so each differs from the current concept in exactly one feature.


Explanation-Free Repair
-----------------------

A simple repair strategy modifies the concept definition directly. For example, if the old rule is:

    IF object has a handle AND object is concave → cup

And the agent incorrectly classified a pail (movable handle) as a cup, the repaired rule becomes:

    IF object has a handle AND handle is fixed AND object is concave → cup

This is similar to incremental concept learning — the concept definition evolves with new examples. However, this approach has a limitation: the feature set can grow large quickly, and there is no understanding of *why* "handle is fixed" matters. Without explanation, the learning is shallow.


Explanation-Based Repair
------------------------

Deeper learning requires building an explanation for why the identified feature matters. The agent must determine *where* in its causal explanation the corrective feature belongs.

For the cup/pail example:

- The agent identifies "handle is fixed" as the distinguishing feature
- It must place this assertion in the correct position within the explanation chain
- Placing it beneath "object is liftable" is wrong — pails and briefcases have movable handles yet are still liftable
- The correct placement is: handle is fixed → object is manipulable → object enables drinking

With background knowledge, the agent can build a richer explanation:

    object has handle + handle is fixed → object is orientable → object is manipulable → object enables drinking

The key insight: classification alone is insufficient. Explanation leads to deeper, more robust learning by capturing *why* features matter for a concept.


Connection to Incremental Concept Learning
------------------------------------------

In incremental concept learning, the focus was on *how* to learn (technique). In learning by correcting mistakes, the focus shifts to *how knowledge is used* — failures during use drive what needs to be learned.

This reflects a core KBAI principle: reasoning, learning, and memory are tightly coupled through action and feedback. The agent:

1. Uses knowledge to select actions
2. Receives feedback from the world
3. Uses feedback to drive learning (converting the learning task into a problem-solving task)

Learning by correcting mistakes treats learning as problem-solving: isolate the fault, explain it, then repair it. This connects directly to metacognition — the agent reasons about its own reasoning.


Cognitive Connection
--------------------

Learning by correcting mistakes closely resembles everyday human learning. Humans are active learners who generate expectations; when expectations are violated, we construct explanations for what went wrong in our knowledge or reasoning and attempt to repair it. This process — thinking about one's own thinking — is a step toward meta-reasoning.
