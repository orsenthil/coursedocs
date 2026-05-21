.. title: 20 - Constraint Propagation 
.. slug: 20 - Constraint Propagation 
.. date: 2016-01-23 06:50:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

===========================
20 - Constraint Propagation
===========================

Overview
--------

**Constraint propagation** is a method of inference in which an agent assigns values to variables to satisfy conditions called **constraints**. It is a general-purpose technique used across knowledge-based AI — in planning, natural language processing, visual reasoning, and more.

The core idea: local constraints, when propagated through a network of variables, yield global inferences about the problem.

3D Object Recognition
---------------------

A motivating example: humans effortlessly perceive 3D objects from 2D line drawings (e.g., recognizing a cube). Constraint propagation explains how.

Marr's Theory of Vision
~~~~~~~~~~~~~~~~~~~~~~~~

David Marr decomposed visual object recognition into three stages:

1. **Edge detection**: pixels grouped into lines based on light intensity gradients
2. **Surface identification**: lines grouped into surfaces with orientations (defined by surface normals)
3. **Object recognition**: surfaces grouped into complete 3D objects

This exemplifies **task decomposition** — a recurring theme in knowledge-based AI. The specific subtask where constraint propagation applies is grouping lines into surfaces.

Line Labeling
-------------

**Line labeling** assigns semantic labels to edges in a 2D drawing to infer 3D surface structure. The method relies on a vocabulary of junction types and their associated constraints.

Junction Types (Trihedral Objects)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For trihedral objects (where exactly three surfaces meet at each vertex):

- **Y junction**: three edges meeting at a point
- **W junction** (arrow): three edges, one pointing inward
- **L junction**: two edges meeting at a corner
- **T junction**: one edge abutting another

Edge Labels
~~~~~~~~~~~

Each edge is classified as:

- **Fold**: a line where two surfaces meet (a true 3D edge)
- **Blade**: a line where no surface connection can be inferred (a boundary or occluding edge)

Constraint Rules (Simplified)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Y junction**: all three edges are folds (fold, fold, fold)
- **L junction**: both edges are blades (blade, blade)
- **W junction**: blade, fold, blade

Propagation Process
~~~~~~~~~~~~~~~~~~~

1. Identify the junction type at each vertex
2. Apply the constraint rule for that junction type to label its edges
3. Propagate: if one junction labels an edge as "fold," that label constrains adjacent junctions sharing that edge

Starting from any junction, labels propagate through the drawing. Once all edges are labeled, surfaces can be identified: folds delineate surface boundaries.

More Complex Scenes
~~~~~~~~~~~~~~~~~~~

The simplified ontology above handles single convex objects. For complex scenes (overlapping objects, concave shapes), a richer constraint ontology is needed:

- Y junctions may also be (blade, blade, blade)
- L junctions may also be (fold, fold) or (blade, fold) / (fold, blade)
- W junctions have additional configurations

Additional conventions help resolve ambiguity — e.g., edges adjacent to the background are labeled as blades. Once boundary edges are fixed, constraints propagate inward to determine interior labels.

This process is an instance of **abduction** — inferring the best explanation for observed data.

Natural Language Processing
---------------------------

Constraint propagation also applies to parsing sentences. Given a grammar:

- Sentence → Noun Phrase + Verb Phrase
- Noun Phrase → [Adjective]* + (Noun | Pronoun)
- Verb Phrase → Verb + [Adverb]*

To check "Colorless green ideas sleep furiously":

1. **Top-down**: hypothesize a split into noun phrase + verb phrase
2. **Bottom-up**: assign lexical categories from a lexicon (colorless=adj, green=adj, ideas=noun, sleep=verb, furiously=adverb)
3. **Verify**: the assignments satisfy the grammar constraints → the sentence is grammatically correct (though semantically meaningless)

The same constraint propagation framework applies to both visual and linguistic processing — define constraints from domain knowledge, then propagate to resolve ambiguities.

Cognitive Connection
--------------------

- Constraint propagation is a general-purpose cognitive mechanism, like means-ends analysis
- Constraints can be **symbolic** (grammar rules, junction types) or **numeric** (spreadsheet formulas propagating changes across cells)
- The method appears across many cognitive tasks: planning, understanding, visual perception, auditory processing, even reading braille
- Configuration (next topic) is a specific application of constraint propagation in the context of design
