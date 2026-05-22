.. title: Incremental Concept Learning
.. slug: Incremental Concept Learning
.. date: 2016-01-23 06:40:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Incremental Concept Learning
============================

Overview
--------

**Incremental concept learning** abstracts general concepts from individual examples, one example at a time. Unlike case-based reasoning (which stores raw cases), this method builds and refines a concept definition as labeled examples arrive.

Key characteristics:

- **Incremental** — examples arrive one at a time, not in bulk
- **Supervised** — each example is labeled positive or negative by a teacher
- **Order matters** — the first example is typically positive; subsequent positive and negative examples drive generalization and specialization
- **Small sample** — concepts are extracted from very few examples, unlike statistical ML which requires thousands or millions
- **Background knowledge dependent** — what the agent learns depends heavily on what it already knows

The Learning Algorithm
----------------------

Given labeled examples arriving one at a time:

- If the example is **positive** and not covered by the current concept definition → **generalize**
- If the example is **negative** and covered by the current concept definition → **specialize**
- If the example is already correctly handled → no change needed

Variabilization
~~~~~~~~~~~~~~~

From the first (positive) example, the only possible learning is **variabilization** — replacing specific constants with variables. For example, given four specific bricks (Brick-A, Brick-B, Brick-C, Brick-D) in an arch configuration, replace each with the general category "brick." This allows any brick to fill each role as long as the structural relationships hold.

Generalization Heuristics
-------------------------

When a positive example is not covered by the current concept definition, apply one of these heuristics to broaden the definition:

Drop-Link
~~~~~~~~~

If the current concept and the new positive example differ only in that the concept has an extra relationship link, **drop that link**. The new definition covers both the old concept and the new example.

*Use when:* The structures overlap almost exactly, except for one extra link in the current definition.

Enlarge-Set
~~~~~~~~~~~

If a slot has a specific filler (e.g., "brick") and the new positive example has a different filler (e.g., "wedge"), replace the filler with a set: "brick OR wedge."

*Use when:* The structures are identical except one element has a different type.

Climb-Tree
~~~~~~~~~~

If background knowledge provides a class hierarchy (e.g., brick and cylinder are both subclasses of "block"), replace the specific set with the **parent class**. Instead of "brick OR cylinder," use "block."

*Use when:* An enlarge-set can be further abstracted using known taxonomic relationships.

Close-Interval
~~~~~~~~~~~~~~

For continuous-valued features, expand the range of acceptable values to include the new example. If the concept only covered small dogs and a large dog is a positive example, widen the size range.

*Use when:* The differing feature is continuous rather than categorical.

Specialization Heuristics
-------------------------

When a negative example is covered by the current concept definition, apply one of these heuristics to narrow the definition:

Require-Link
~~~~~~~~~~~~

If the current concept and the negative example share most structure but the concept has a relationship link that the negative example lacks, mark that link as **required** (must be present).

*Example:* The concept of an arch requires that vertical blocks *support* the top block. A negative example with three blocks but no support relationship triggers require-link on the support links.

Forbid-Link
~~~~~~~~~~~

If the negative example has a relationship link that the current concept does not, **forbid that link**. Mark it with a "must not" condition.

*Example:* The arch concept says vertical blocks must not touch each other. A negative example where they touch triggers forbid-link on the "touches" relationship.

Worked Example: Learning "Arch"
-------------------------------

1. **Example 1** (positive): Four bricks — two vertical supports, two horizontal on top. *Variabilize:* replace Brick-A/B/C/D with generic "brick." Record structural relationships: left-of, supports.

2. **Example 2** (positive): Three bricks — vertical supports, one on top (missing the extra top brick). *Generalize* using **drop-link:** remove the extra "supports" link for the second top brick, since this example lacks it.

3. **Example 3** (negative): Three bricks, but the top brick is not supported by the verticals. *Specialize* using **require-link:** mark the support links as required.

4. **Example 4** (negative): Three bricks, but the two vertical bricks are touching. *Specialize* using **forbid-link:** add "must not touch" between the vertical elements.

5. **Example 5** (positive): Two bricks as supports with a wedge on top instead of a brick. *Generalize* using **enlarge-set:** top element becomes "brick OR wedge." With background knowledge that both are subclasses of "block," **climb-tree** can further generalize to "block."

The final concept definition depends on both the input examples *and* the agent's background knowledge. Different background knowledge leads to different learned concepts.

Contrast with Statistical ML
----------------------------

Incremental concept learning differs fundamentally from standard machine learning:

- **Sample size** — ICL works with very few examples; statistical ML requires large datasets
- **Incrementality** — ICL processes one example at a time; batch ML processes all examples at once
- **Knowledge role** — ICL relies heavily on background knowledge and heuristics to guide learning; statistical ML relies on detecting patterns of regularity in large data
- **Overgeneralization/overspecialization** — With few examples, the risk of learning the wrong concept boundary is high; heuristics and background knowledge mitigate this

Cognitive Connection
--------------------

Incremental concept learning closely mirrors human learning:

- Humans learn from **one example at a time** in daily life — we rarely encounter millions of examples at once
- Background knowledge critically shapes what we learn — two people with different prior knowledge learn different concepts from the same examples
- The incremental, knowledge-guided nature of this method is closer to how human cognition actually works than batch statistical approaches
