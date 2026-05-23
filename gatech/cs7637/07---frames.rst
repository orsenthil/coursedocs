Frames
======

Overview
--------

**Frames** are a structured knowledge representation central to common sense reasoning. They appear throughout topics like understanding, scripts, and story comprehension. Frames are useful for enabling inferences that go beyond what is explicitly stated in input.

Frames and Common Sense Reasoning
---------------------------------

Consider the sentence "Ashok ate a frog." From this alone, we can infer: the frog is dead, the frog is in Ashok's stomach, and Ashok is probably happy. None of these facts are stated explicitly — they come from our stereotypical knowledge about the action of eating. Frames capture this kind of knowledge.

Frame Structure: Slots and Fillers
----------------------------------

A **frame** is a knowledge structure associated with a stereotypical situation, action, or object. It consists of **slots** (attributes) and **fillers** (values for those attributes).

Example frame for the verb "ate":

- **Subject** — the agent doing the eating (from sentence parsing)
- **Object** — what is being eaten (from sentence parsing)
- **Location** — where the eating occurs
- **Time** — when it occurs
- **Utensil** — tool used (e.g., fork, spoon)
- **Object-alive** — typically false (default)
- **Object-location** — inside the subject's body (default)
- **Subject-mood** — typically happy (default)

Key properties:

- **Default fillers** enable inference without explicit input — this is the basis of common sense reasoning
- **Sentence-derived fillers** come from parsing input (e.g., subject="Ashok", object="frog")
- **Slots remain constant** for a given frame type; fillers change per instance
- Frames deal with **stereotypical** situations — defaults can be overridden by specific input

Frames are analogous to *molecules* of knowledge representation (structured, multi-part), whereas production rules are like *atoms* (single units). Frames are also closely analogous to **objects in object-oriented programming** — both emerged in the 1960s–70s and influenced each other. Slots correspond to variables/properties; fillers correspond to values.

Complex Frame Systems
---------------------

Frames support **discourse-level understanding**, not just sentence-level. A discourse containing multiple sentences can generate multiple frames that hook together:

- A sentence about Angela's food preferences → a frame for Angela
- A sentence about Olive Garden restaurant → a frame for Olive Garden
- "Angela had lasagna with her dad at Olive Garden" → an "ate" frame that links to both

By connecting frames, the system achieves understanding of larger units of language and can pull information across sentences to fill slots.

Properties of Frames
--------------------

Three main properties:

1. **Represent stereotypes** — frames encode typical/expected structure of a concept or event
2. **Provide default values** — slots have defaults that enable inference when information is missing
3. **Support inheritance** — frames can inherit slots and fillers from parent frames

Frames and Semantic Networks
----------------------------

Frames and semantic networks are **representationally equivalent**. Any semantic network can be rewritten as a set of frames and vice versa.

Example: An image with objects X (large diamond, filled), Y (small circle, filled, inside X), and Z (small circle, empty) can be represented as:

- Semantic network: nodes for X, Y, Z with labeled edges (inside, above, etc.)
- Frames: one frame per object with slots for name, shape, size, fill; relationships captured by slots pointing to other frames (e.g., Y's "inside" slot → X)

Relationships between frames can be expressed either as directed links between frame nodes or as slot values referencing other frame names (e.g., ``inside: X``).

Frames and Production Systems
-----------------------------

Frames appeared implicitly in production systems — the working memory structure (feature-value pairs like ``inning: 7th``, ``outs: 2``) is essentially a frame. Frames can be thought of as capturing conceptual knowledge stored in **semantic memory**.

When a verb like "ate" appears in input, its frame is retrieved from semantic memory into working memory. The frame immediately generates **expectations** — it tells the system what to look for (subject, object, location, etc.). This makes processing **partially top-down**: rather than purely bottom-up from input, the mind provides structured knowledge that guides interpretation.

Cognitive Connection
--------------------

Three key connections between frames and human cognition:

1. **Structured knowledge** — Frames are molecular (vs. atomic) knowledge representations, capturing large amounts of organized information as packets
2. **Top-down processing** — Frames enable a theory of cognition that is not purely bottom-up; retrieved knowledge structures generate expectations that guide perception and interpretation
3. **Stereotypes** — Humans use stereotypes of situations and events because they are cognitively efficient — default values enable rapid expectation generation without reasoning from scratch each time. This efficiency comes at the cost of occasionally incorrect inferences.
