Case-Based Reasoning
====================

Overview
--------

**Case-based reasoning (CBR)** extends learning by recording cases to handle situations where the new problem is *similar but not identical* to a previously encountered problem. Rather than directly reusing a past solution, CBR tweaks it to fit the new problem.

The core insight: in learning by recording cases, new problem = old problem. In CBR, new problem ≈ old problem, requiring adaptation.

The CBR Process
---------------

CBR consists of four phases:

1. **Retrieval** — Find the most similar case in memory (e.g., using k-nearest neighbor)
2. **Adaptation** — Modify the retrieved solution to fit the new problem
3. **Evaluation** — Test whether the adapted solution actually meets the new problem's requirements
4. **Storage** — If successful, encapsulate the new problem-solution pair as a case and store it in case memory

This process **unifies memory, reasoning, and learning**: memory stores and retrieves cases; reasoning adapts and evaluates; learning occurs when new cases are stored.

Assumptions
~~~~~~~~~~~

CBR rests on the assumption that **similar problems have similar solutions**. While counterexamples exist (similar problems can occasionally have very different solutions), this holds true most of the time.

Case Adaptation
---------------

Three primary methods for adapting a retrieved case:

Model-Based Adaptation
~~~~~~~~~~~~~~~~~~~~~~

Use a **causal model of the world** to understand why the old solution worked and how to modify it for the new context. The model explains the relationships between problem features and solution components, guiding principled modifications.

Recursive Case-Based Adaptation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decompose the adaptation problem itself into sub-problems and use CBR recursively to solve each sub-problem. If adapting a navigation route, for example, break it into segments and find stored cases for each segment.

Rule-Based Adaptation
~~~~~~~~~~~~~~~~~~~~~

Apply **heuristic rules** that specify common adaptations. Example: "If you want to make an artifact lighter, try a different material." Designers frequently use such rules of thumb to evolve existing designs.

Case Evaluation
---------------

After adaptation, the candidate solution must be evaluated:

- For navigation: simulate the route to check it reaches the destination
- For programming: run the adapted program against test cases
- For design: prototype, simulate, or have other designers critique it

If evaluation fails, two recovery paths exist:

- **Repair:** Return to the adaptation step and try a different modification
- **Retrieve:** Go back to retrieval and find a different case entirely

Case Storage
------------

Successful new cases are stored back into case memory, enabling the system to handle an ever-growing range of problems. Two storage mechanisms:

Indexing
~~~~~~~~

Cases are stored in a table indexed by features (e.g., origin coordinates, destination coordinates). Retrieval scans the table to find the closest match. Simple but **linear-time retrieval** — becomes inefficient as the case library grows.

Discrimination Trees
~~~~~~~~~~~~~~~~~~~~

A **discrimination tree** organizes cases as leaf nodes of a tree. Internal nodes contain questions about case features (based on the indexing structure).

- Navigating the tree with a new case's features leads to the appropriate storage location
- If two cases share a branch, a new discriminating question is added to distinguish them
- Retrieval uses the same tree traversal: navigate with the new problem's features to find the most similar stored case
- Provides **logarithmic-time retrieval** vs. linear for tabular indexing
- The tree structure is learned incrementally — each new case potentially adds a new discriminating node

Example: A tree might ask "Is origin north of 5N?" at the root, then "Is origin east of 5E?" at the next level, progressively narrowing to individual cases.

Advanced CBR
------------

**Failed cases are valuable:** Storing failures in case memory helps anticipate and avoid similar failures in the future. Recovery from failure can go back to adaptation (repair) or all the way to retrieval (try a different case).

**The utility problem:** Not every successful case should be stored. If the case library grows too large, retrieval becomes inefficient. Only cases that cover a novel region of the problem space — something interesting or noteworthy — should be stored.

Open questions in CBR:

- Should we abstract over individual cases to form general concepts?
- When should cases be forgotten?
- At what point does the case library become intractably large?

Cognitive Connection
--------------------

CBR connects to human cognition through **analogical reasoning**, which operates on a spectrum of similarity:

- **Identical problems** → direct retrieval and reuse (learning by recording cases)
- **Similar problems** → retrieve, adapt, and apply (case-based reasoning)
- **Semantically distant problems** → cross-domain analogy (covered in later lessons)

The middle of this spectrum — similar but not identical — is the most common in human cognition.

CBR unifies all three components of the cognitive architecture:

- **Learning** — acquiring and storing experiences
- **Memory** — retrieving relevant experiences when needed
- **Reasoning** — adapting past experiences to meet new problem requirements
