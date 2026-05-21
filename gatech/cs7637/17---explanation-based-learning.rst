.. title: 17 - Explanation-Based Learning 
.. slug: 17 - Explanation-Based Learning 
.. date: 2016-01-23 06:47:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

===============================
17 - Explanation-Based Learning
===============================

Overview
--------

**Explanation-based learning (EBL)** does not learn new concepts. Instead, it learns new *connections* among existing concepts by building causal explanations. EBL transfers knowledge from familiar situations to novel ones, making it a form of **speed-up learning** — the agent becomes more capable without acquiring fundamentally new knowledge.

EBL is closely tied to creativity: when usual tools or methods are unavailable, an agent improvises by finding novel uses for known objects through explanation.

Concept Space and Prior Knowledge
---------------------------------

EBL operates over a **concept space** — a network of concepts and their interrelationships. Each concept is represented with:

- **Structural features** — observable properties (e.g., "has a flat bottom," "is concave," "has a handle")
- **Functional features** — behavioral properties (e.g., "is stable," "is liftable," "carries liquid")
- **Causal connections** — links explaining *why* a functional feature holds (e.g., "the brick is stable *because* its bottom is flat")

Example prior knowledge:

- **Brick**: stable because bottom is flat; heavy
- **Briefcase**: liftable because it has a handle and is light; useful because it contains papers
- **Bowl**: carries liquid because it is concave
- **Glass**: enables drinking because it carries liquid and is liftable; pretty

Not all structural features participate in causal explanations — only those linked by causal connections matter for EBL.

Abstraction
-----------

From a known concept, the agent abstracts a **transferable causal pattern** by:

1. Retaining only features involved in causal relationships (dropping causally irrelevant features)
2. Replacing the specific concept with a generic placeholder (e.g., "bowl" → "object")

Example: "The bowl carries liquid because it is concave" abstracts to "An object carries liquid because it is concave."

Transfer and Explanation Construction
-------------------------------------

Given a novel object and a target concept to prove (e.g., "Is this object a cup?"), the agent:

1. Identifies the conditions the target concept requires (e.g., a cup must be stable and enable drinking)
2. Searches prior knowledge for abstractions whose causal patterns match observable features of the new object
3. Chains these abstractions into a **causal proof** connecting the object's features to the target concept's requirements

For example, to prove an object is a cup:

- Stability: the object has a flat bottom → stable (transferred from brick)
- Enables drinking: the object is concave → carries liquid; has a handle and is light → liftable; carries liquid + liftable → enables drinking (transferred from bowl, briefcase, glass)

The proof the agent builds depends on what background knowledge is available — different knowledge yields different valid proofs.

Proving an Object Is a Mug
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A **mug** requires three properties: stable, enables drinking, and protects against heat. The first two can be proved as with a cup. For heat protection, the agent needs a concept like a **pot** (limits heat transfer because it has thick sides and is made of clay) or an **oven mitt** / **wooden spoon** — whichever is available in memory.

This illustrates that the minimal knowledge needed is goal-driven: the agent asks "what do I need to prove X?" and searches for exactly that knowledge.

Everyday Improvisation
----------------------

EBL explains everyday creative problem-solving:

- Using a coffee mug as a paperweight (heavy + flat bottom → stable → acts as weight)
- Using a chair to prop open a door
- Using an eraser as a doorstop

In each case, the agent builds a causal explanation for why a familiar object can serve an unfamiliar function.

Cognitive Connection
--------------------

- EBL is central to cognitive science's goal of human-level intelligence; it models how humans generate and use explanations
- Humans can only explain consciously accessible processes — we cannot easily explain implicit skills (e.g., motor coordination)
- Generating explanations can *deepen* understanding by exposing causal structure, but the explanation process may differ from the original reasoning process
- For AI systems to earn trust, they must explain both their answers and the reasoning behind them — explanation is fundamental to trust
