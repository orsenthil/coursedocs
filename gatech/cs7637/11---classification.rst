.. title: 11 - Classification 
.. slug: 11 - Classification 
.. date: 2016-01-23 06:41:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

===================
11 - Classification
===================

Classification Overview
-----------------------

**Classification** is the mapping of percepts into equivalence classes so that agents can select actions efficiently. Given a cognitive system dealing with percepts in the world, classification reduces the complexity of mapping percepts to actions.

The core challenge: if there are *n* binary percepts, there are 2^n possible combinations. With even 10 percepts, there are 1024 combinations; with 300 percepts, the combinations exceed the number of atoms in the universe. Intelligent agents must map these percept combinations to actions in near real-time despite having only finite computational resources.

Equivalence Classes
-------------------

Classification solves the percept-to-action mapping problem by breaking one impossibly large lookup table into many small tables. Without classification, an agent would need a table with 2^n rows (percept combinations) and 2^m columns (action combinations). Classification groups percepts into **equivalence classes**, making the problem tractable.

This is the power of knowledge: taking a complex problem and decomposing it into smaller, simpler problems.

Concept Hierarchies
-------------------

Concepts organize into hierarchies. For example: Vertebrate > Bird > {Eagle, Bluebird, Penguin}. Each level in the hierarchy keys on different features:

- At higher levels (Bird vs. Reptile vs. Mammal), features like "has feathers" or "lays eggs" matter
- At lower levels (Eagle vs. Bluebird), features like size become discriminating

This hierarchical organization provides control over processing: **establish** a node, then **refine** it downward. The organization itself is a source of power — it dictates what processing should occur at each level.

Types of Concepts
-----------------

Concepts lie on a spectrum from formal to informal:

1. **Axiomatic concepts** — defined by necessary and sufficient conditions (e.g., geometric shapes). A circle is all points equidistant from a center point. Easy to communicate and program.

2. **Prototype concepts** — defined by typical properties that can be overridden (e.g., "chair"). A prototypical chair has four legs, a back, metal material, no arms, no cushion. Represented naturally using frames with default slot values. Specific instances (e.g., stool) inherit from the prototype but override certain properties (e.g., no back). Related to frame inheritance and defaults.

3. **Exemplar concepts** — defined only by examples, with no typical or necessary conditions (e.g., beauty, freedom). Culture-specific or individual-specific. Very hard to define, communicate, or program.

Beyond exemplars, **qualia** (raw sensations like bitterness) are even less formal — nearly impossible to communicate to others.

Matching concepts to methods: case-based reasoning suits exemplar concepts (hard to abstract into conditions), while formal logical methods suit axiomatic concepts with clear necessary/sufficient conditions.

Bottom-Up Classification
-------------------------

Two complementary classification strategies:

- **Top-down (establish-and-refine)**: Start at the top of a hierarchy and refine downward. Best when you already know something belongs to a broad category and need to determine the specific subclass.

- **Bottom-up (identify-and-abstract)**: Start with known leaf-node values and abstract upward to make a prediction at the root. Example: predicting Dow Jones Industrial Average from GDP, inflation, employment — which themselves are derived from overtime hours, consumer sentiment index, new orders index, etc.

Bottom-up processing applies when you know feature values at the lowest level and need to classify or predict at a higher level.

Cognitive Connection
--------------------

Classification is ubiquitous in cognition: recognizing a car as a Porsche, diagnosing a software bug, a doctor naming a disease category. Its centrality stems from enabling action selection — once a doctor classifies a disease, therapy follows; once you classify a bug, repair follows. If intelligence is largely about selecting the right action, classification is central to cognition.
