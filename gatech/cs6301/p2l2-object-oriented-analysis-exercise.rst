Object Oriented Analysis Exercise
=================================

Object-Oriented Analysis (OOA)
------------------------------

Before solving a problem (design), you must understand it (analysis). **Object-Oriented Analysis (OOA)** is a requirements analysis technique developed by Abbott and Booch in the 1980s. It models real-world objects from their natural-language descriptions to produce an object analysis model, expressed primarily using UML class model diagrams.

Why Objects over Functions
--------------------------

Prior to OOA, the dominant approach was **functional decomposition** (structured analysis/design), which focused on the functions a system must provide. Objects are a better starting point because they are **more stable than functions** over a system's lifetime.

Example: In a banking application, functions like interest computation, fee structures, and tax rules change frequently. But the need to represent accounts, account holders, and transactions persists. Designing around stable objects leads to more sustainable designs.

In structured analysis, data is secondary to functions. In OOA, **data objects are defined first** (attributes and types), then functions are defined and associated with specific objects.

The OOA Technique
-----------------

OOA takes a textual description (e.g., a requirements document) and extracts:

- **Nouns** → candidate classes
- **Adjectives** → attributes
- **Action verbs** → operations
- **Stative verbs** → relationships

Steps
~~~~~

1. Obtain or prepare a textual description of the problem
2. Underline all **nouns**; organize into groups as candidate classes (apply stemming to merge duplicates like "pile/piles", "leaf/leaves")
3. Underline all **adjectives**; assign as attributes of candidate classes (also consider prepositional phrases like "parts of the tree" → tree has attribute "parts")
4. Underline all **verbs**; distinguish action verbs from stative/linking verbs
5. Assign **action verbs** as operations of appropriate classes
6. Assign **stative verbs** as relationships between classes

Example: Counting Tree Leaves
------------------------------

Given a description of a program that counts leaves in a tree data structure by maintaining a pile of uncounted subtrees:

Candidate Classes
~~~~~~~~~~~~~~~~~

Nouns extracted and grouped (after stemming and deduplication): **Tree**, **Pile**, **Counter**, **Leaf**, **Node**, **Part**.

Attributes (from Adjectives)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Prepositional phrases yield attributes not directly from adjectives (e.g., "parts of the tree" → Tree has ``parts``)
- "single leaf" → a count value of 1; "two subtrees" → a count of 2
- Tree: ``leftSubtree``, ``rightSubtree``, ``leaves``, ``parts``
- Pile: ``empty`` (Boolean)
- Counter: ``value``

Operations (from Action Verbs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Pile: ``put(tree)``, ``get()``, ``take()``
- Counter: ``increment()``, ``display()``
- Tree: ``split()``, ``throwAway()``

Issues: "has been counted" is stative (describes state, not action) — revisited under relationships. "Examine", "consists of", and "is set to" describe conditions rather than actions and map to equality checks.

.. mermaid::

   classDiagram
       class Tree {
           +Tree leftSubtree
           +Tree rightSubtree
           +Integer leaves
           +Integer parts
           +split()
           +throwAway()
       }
       class Leaf
       class Pile {
           +Boolean empty
           +put(tree)
           +get()
           +take()
       }
       class Counter {
           +Integer value
           +increment()
           +display()
       }
       Tree <|-- Leaf : is-a
       Tree o-- Tree : subtrees
       Pile o-- Tree : contains
       Counter -- Leaf : counts

Relationships
-------------

UML class model diagrams use three relationship types:

Generalization
~~~~~~~~~~~~~~

Indicated by a line ending in an open triangle. The child class is a *kind of* the parent class (subset relationship). Keywords: "kind of", "type of", or implicit from class names.

In the tree example, **Leaf** is a specialization of **Tree** — an implicit generalization not stated directly in the text.

Aggregation
~~~~~~~~~~~

Indicated by a line ending in an open diamond. Keywords: "consists of", "part of", "contains", "has", "incorporates", "belongs to".

In the tree example: a Tree consists of subtrees (aggregation); a Pile contains Trees (aggregation).

Association
~~~~~~~~~~~

A general relationship indicated by an unadorned labeled line. **Stative verbs** (denoting states of being) often indicate associations.

In the tree example, there is an implied association between Counter and Leaf — the counter *counts* the leaves.

Caveats
-------

- Analysis conclusions are always **tentative** — learning more about the problem leads to revisions
- Requirements documents are inherently incomplete, inconsistent, or imprecise; the analyst's job is to elicit the correct description
- Questions during OOA often reveal issues the customer hadn't considered
- Analysis is **inherently incremental**, leading to joint understanding between analyst and customer
- Distinguish analysis (understanding the problem) from design (crafting the solution) to avoid prematurely biasing the approach
- Always validate results with stakeholders, especially the customer
