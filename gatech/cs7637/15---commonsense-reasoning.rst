.. title: Commonsense Reasoning
.. slug: Commonsense Reasoning
.. date: 2016-01-23 06:45:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Commonsense Reasoning
=====================

Commonsense Reasoning Overview
-------------------------------

**Commonsense reasoning** enables agents to make natural, obvious inferences about the world — the kind humans do effortlessly. Example: if asked to "find the weather outside," a robot should not jump out a window. The robot needs commonsense knowledge that jumping from a height causes injury.

Key ideas:

- A small set of **primitive actions** (only 14) organizes vast amounts of knowledge
- Primitive actions compose into **hierarchies of sub-actions**
- Actions cause **state changes**, enabling prediction of consequences

The Problem of Multiple Meanings
---------------------------------

Two complementary challenges in understanding verbs:

1. **One word, many meanings** (polysemy): "eat" can mean consume food, erode ("river ate the riverbank"), obsess ("eating him"), absorb losses ("eat the losses")
2. **Many words, one meaning** (synonymy): "ate," "devoured," "consumed," "ingested," "partook," "dined on" all convey the same basic event

Additionally, sentences with different structure can share meaning: "Bob shot Bill" ≡ "Bob killed Bill with a gun."

Primitive Actions
-----------------

Rather than maintaining separate frames for every verb, we map verbs to a small set of **primitive actions** that capture deep meaning:

- **Move-object** (propel) — physically moving something
- **Ingest** — taking something into the body
- **Expel** — removing something from the body
- **Move-body-part** — moving a part of one's own body
- **Grasp** — grabbing/holding an object
- **Speak** — communicating verbally
- **Attend** — focusing sensory attention
- **Think** — cognitive processing
- **Feel** — experiencing emotion
- **Do** — generic action (used when specific primitive is unclear)

(Plus a few more, totaling ~14)

All synonymous verbs for eating (ate, devoured, consumed, ingested, partook) map to the single primitive action **Ingest**. The frame for Ingest specifies: agent, object, initial state (object outside body), final state (object inside body, object dead, agent happy via defaults).

Mapping examples:

- "John pushed the cart" → **Propel** (agent in contact with object)
- "John took the book from Mary" → **Move-object** (transfer of possession)
- "John ate ice cream with a spoon" → **Ingest**
- "John decided to go to the store" → **Think** (decision) + **Move-object** (movement)

Thematic Roles and Primitive Actions
-------------------------------------

Processing a sentence like "John pushed the cart":

1. Bottom-up: encounter verb "pushed" → probe memory → retrieve frame for **Propel**
2. Top-down: frame specifies expected slots (agent, object) with rules for extraction
3. Rule for agent: "if a concept before the verb is animate → fill agent slot" → John
4. Rule for object: "if a concept after the verb is inanimate → fill object slot" → cart

The frame acts as a hook — once activated, it generates expectations and guides slot-filling. Processing combines bottom-up (data-driven) initiation with top-down (knowledge-driven) completion.

If the wrong frame is selected, difficulty in filling slots signals the need to abandon and try another. In longer stories, context from surrounding sentences resolves ambiguity.

Implied Actions
---------------

Some verbs don't map directly to primitives. "John fertilized the field" implies "John put fertilizer on the field" — the implied action **Move-object** (put) is the true primitive.

"Bill shot Bob" implies "Bill propelled a bullet into Bob" — the primitive is **Propel**, with agent=Bill, object=bullet, destination=Bob.

When a verb doesn't map cleanly, the agent must infer implied actions that do map to primitives. This itself is commonsense reasoning.

Actions and Sub-actions
-----------------------

Primitive actions can decompose into sub-action sequences. For "Ashok puts the wedge on the block," the Move-object action decomposes into:

1. Grasp the wedge
2. Move-body-part (arm) to position above block
3. Release (un-grasp) the wedge

This hierarchical decomposition parallels hierarchical planning — complex actions break into simpler constituents.

State Changes
-------------

Actions produce **state changes**. Frame representations capture both the action and resulting states:

- "Susan comforted Jing" → Action: Do(Susan, something) → State change: Jing's mood becomes happy
- "Ashok enjoyed eating a frog" → Two frames: Ingest(agent=Ashok, object=frog) + Feel(agent=Ashok, object=enjoyment), connected by a "result" link

For sentences with multiple verbs (e.g., "Maria told Ben to throw the ball"):

- Frame 1: Speak(agent=Maria, result=Frame 2)
- Frame 2: Propel(agent=Ben, object=ball)

The "result" slot connects action frames, enabling multi-verb sentence understanding.

Cognitive Connection
--------------------

Commonsense reasoning is central to cognition but not fully understood. We use goals, context, and world models to decide what actions are reasonable. This extends beyond physical actions to the social world — **theory of mind** allows us to ascribe goals, beliefs, and desires to others, enabling commonsense social inferences.

Context is critical: it disambiguates polysemous words (one word, many meanings) and identifies synonymous expressions (many words, one meaning). Commonsense reasoning provides the formal structure to interpret the world, enabling agents to predict effects of actions and reason about causes of observed states.
