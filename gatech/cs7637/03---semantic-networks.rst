.. title: Semantic Networks
.. slug: Semantic Networks
.. date: 2016-01-23 06:34:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Semantic Networks
=================

Knowledge Representations
-------------------------

A **knowledge representation** has two components:

- **Language** — A vocabulary and syntax (e.g., the language of algebraic equations: ``y = bx``)
- **Content** — The actual knowledge expressed in that language (e.g., Newton's second law: ``F = ma``)

AI has developed many knowledge representations, each with its own affordances and constraints. Semantic networks are one such representation.

Semantic Networks
-----------------

A **semantic network** represents knowledge as a graph of **nodes** (objects) connected by **labeled, directed links** (relationships).

Constructing a semantic network for a 2x1 matrix problem (A:B :: C:D):

1. **Identify objects** — Label objects in each image (e.g., x = circle, y = diamond, z = black dot)
2. **Represent intra-image relationships** — Add labeled links between objects within each image (e.g., "y inside x", "z above y")
3. **Represent inter-image transformations** — Add labeled links between corresponding objects across images (e.g., "x unchanged", "y expanded", "z deleted"). If an object has no counterpart, use a dummy node.

The transformation from A to B is captured by these inter-image links. To test whether a candidate answer is correct, build the same representation for C-to-candidate and check whether it matches the A-to-B transformation.

Consistent vocabulary matters: once you choose terms like "inside" and "above," use them throughout.

Structure of Semantic Networks
------------------------------

Three components define the representation:

- **Lexicon** — Nodes representing objects
- **Structure** — Directed links between nodes, composing them into complex representations
- **Semantics** — Labels on links that enable inference and reasoning

Characteristics of Good Representations
----------------------------------------

A good knowledge representation:

- **Makes relationships explicit** — All objects, relationships, and constraints are visible
- **Exposes natural constraints** — The problem's constraints are surfaced by the structure
- **Works at the right level of abstraction** — Captures everything needed, omits irrelevant detail
- **Is transparent and concise** — Easy to understand, no unnecessary complexity
- **Is complete** — Captures all information needed to solve the problem
- **Is fast** — Avoids unnecessary detail that would slow computation
- **Is computable** — Enables drawing the inferences needed to solve the problem

Guards and Prisoners Problem
----------------------------

A classic constraint-satisfaction problem (also known as Cannibals and Missionaries, dating to ~880 AD):

- 3 guards and 3 prisoners must cross a river
- One boat carries at most 2 people; cannot travel empty
- Prisoners can never outnumber guards on either bank

**Semantic network representation:** Each **node** represents a state (number of guards, prisoners, and boat position on each bank). **Links** represent moves (who crosses in the boat). **Labels** on links describe the move.

Using this representation for problem solving:

1. From the initial state (all on left), enumerate possible moves (5 possible: move 1 guard, 1 guard + 1 prisoner, 2 guards, 2 prisoners, or 1 prisoner)
2. **Prune illegal moves** — Eliminate states where prisoners outnumber guards on either bank
3. **Prune unproductive moves** — Eliminate moves that return to previously visited states
4. Continue expanding legal, productive moves until reaching the goal state (all on right)

The solution requires **11 moves**. The representation makes systematic problem solving tractable by making all constraints, objects, and relationships explicit. Once in a state, how you arrived there is irrelevant — only the current state matters.

Represent and Reason for Analogy Problems
-----------------------------------------

The **represent-and-reason** paradigm underlies all of KBAI:

1. Build semantic network representations for A:B and C:candidate
2. Compare the transformation structure: if the C:candidate transformation matches A:B, accept the candidate
3. If transformations differ (e.g., A:B has "y expanded" but C:candidate has "s unchanged"), reject and try another candidate
4. Select the candidate whose transformation best matches

When multiple candidates partially match, a similarity metric is needed to rank them.

Choosing Matches by Weights
---------------------------

When multiple interpretations of a transformation are valid, a **similarity metric** with **weighted transformations** can disambiguate:

Example weight scale (higher = easier/more similar):

- Unchanged: 5
- Reflected: 4
- Rotated: 3
- Scaled: 2
- Deleted: 1

For a problem with two valid interpretations:

- Interpretation 1: p deleted (1) + q unchanged (5) = **total 6**
- Interpretation 2: p scaled (2) + q deleted (1) = **total 3**

The agent prefers interpretation 1 (higher total weight), favoring transformations that preserve more structure. This explains why, for ambiguous problems (e.g., reflection vs. rotation), agents and humans tend to prefer the simpler transformation.

Connections
-----------

Three important connections from semantic networks:

- **Memory** — A and B can be stored in memory; C paired with each candidate serves as a probe. The candidate most similar to what's stored (by some similarity metric) is chosen. This connects to **case-based reasoning**.
- **Correspondence problem** — Given two situations, which object in one corresponds to which object in the other? This recurs in **analogical reasoning**.
- **Relationships over features** — KBAI emphasizes relationships between objects, not just object properties. The focus is on "inside," "above," "expanded," "deleted" — not on "is a circle" or "is large."

The Cognitive Connection
------------------------

Two connections to human cognition:

1. **Representation enables reasoning** — Just as AI agents use knowledge representations to solve problems, the human mind represents problems and uses those representations to reason. Representation is key.
2. **Spreading activation networks** — Semantic networks relate to a popular theory of human memory. Example: hearing "John wanted to become rich. He got a gun." activates nodes for "rich" and "gun," and activation spreads through the network until paths merge — connecting through nodes like "rob a bank" — producing story comprehension through inference.
