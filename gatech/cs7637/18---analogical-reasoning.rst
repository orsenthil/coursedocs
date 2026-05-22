.. title: Analogical Reasoning
.. slug: Analogical Reasoning
.. date: 2016-01-23 06:48:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Analogical Reasoning
====================

Overview
--------

**Analogical reasoning** addresses new problems by transferring knowledge of relationships from known problems, potentially across domains. It generalizes the transfer mechanism introduced in explanation-based learning and extends case-based reasoning to cross-domain settings.

The process has five phases: **retrieval, mapping, transfer, evaluation, and storage**.

Similarity
----------

Similarity between two situations can be measured along multiple dimensions:

- **Relationships** between objects (e.g., "climbing up")
- **Objects** themselves (e.g., woman, ladder)
- **Features** of objects (e.g., size, shape)
- **Values** of features (e.g., tall, short)

Two situations may share objects but differ in relationships (a woman *climbing* a ladder vs. *painting* a ladder), or share relationships but differ in objects (a woman climbing a ladder vs. an ant climbing a wall). Relationship similarity is generally more important for analogy than object similarity.

Spectrum of Similarity
~~~~~~~~~~~~~~~~~~~~~~

At one extreme, the target problem and source case are identical (all dimensions match). At the other, nothing is shared. Between these:

- **Recording cases**: relationships, objects, features, and values all similar (same domain, same objects)
- **Case-based reasoning**: relationships and objects similar, but features/values may differ (same domain)
- **Analogical reasoning**: only relationships similar; objects, features, and values may differ entirely (cross-domain)

Cross-Domain Analogy
--------------------

Cross-domain analogy occurs when the target problem and source case come from different domains, sharing deep relational structure but not surface features.

**Duncker's radiation problem**: A physician must destroy a stomach tumor with a laser, but a full-intensity beam would kill healthy tissue. The analogous source: a rebel army must capture a fortified king, but marching a full army down any mined road would trigger explosions. Solution: decompose the resource (army/laser) into smaller units and converge on the goal from multiple directions simultaneously.

The objects differ entirely (physician/king, laser/army, tissue/mines), but the relational pattern — *decompose resource, converge from multiple directions to overcome obstacle* — transfers across domains.

Three Types of Similarity
--------------------------

- **Semantic similarity** — conceptual overlap between objects (woman/woman, ladder/step-ladder)
- **Pragmatic similarity** — shared external factors, especially goals (killing tumor ≈ capturing fort)
- **Structural similarity** — isomorphism between representational graphs; the relational structure matches even when objects and goals differ (solar system ≈ atomic structure)

Different theories of analogy weight these differently.

Analogical Retrieval
--------------------

Retrieval finds a source case relevant to the target problem. Key distinction:

- **Superficial similarity**: shared features, object counts, or objects themselves
- **Deep similarity**: shared relationships between objects, or relationships between relationships (higher-order relations)

Higher-order relationships indicate deeper similarity. For example, in Raven's Progressive Matrices:

- Unary: features of individual objects (size, fill)
- Binary: relationships between two objects (X is outside Y)
- Tertiary: relationships between relationships (the pattern of change from A→B matches C→D)

The mind judges two situations as more similar when similarity operates at the relational level rather than the object/feature level.

Analogical Mapping
------------------

Mapping solves the **correspondence problem**: what in the target corresponds to what in the source?

Without constraints, mapping is combinatorially explosive (m × n possibilities). The key heuristic: **prioritize higher-order relationships**. Instead of mapping king↔patient (superficial — both are people), we map king↔tumor (both are goals to be neutralized via a resource despite an obstacle). The deeper relational structure — goal/resource/obstacle — determines correct alignment.

Example — solar system ↔ atomic structure:

- Sun ↔ nucleus (both are central, massive bodies)
- Planet ↔ electron (both revolve around the central body)
- Gravitational force ↔ electrostatic force (both cause attraction and revolution)

Correct mapping requires deep models of both systems.

Analogical Transfer
-------------------

Once alignment is established, the agent:

1. Abstracts a relational pattern from the source (e.g., "decompose resource into smaller units, send from multiple directions")
2. Instantiates that pattern in the target using the mapping (laser → smaller beams, converge on tumor)

Transfer depends on correct mapping, which depends on successful retrieval. Goals often drive the process (pragmatic similarity).

In the solar system → atom example, the transferred knowledge is: "the electron revolves around the nucleus" (inferred from "the planet revolves around the sun" via structural similarity, even without semantic or pragmatic similarity).

Evaluation and Storage
----------------------

Analogical reasoning provides no correctness guarantees — proposed solutions must be evaluated (e.g., via simulation or prototyping). If evaluation succeeds, the target problem and solution are encapsulated as a new case for future reuse, enabling incremental learning.

If evaluation fails, the agent can revisit transfer (change what is transferred), mapping (realign), or retrieval (find a different source).

Design by Analogy
-----------------

**Biologically inspired design (biomimicry)** applies analogical reasoning to engineering:

- **Shinkansen 500 bullet train**: nose shape inspired by kingfisher beak — both transition between media (air/water, outside/inside tunnel) while minimizing shock waves
- **Basilisk lizard → water-walking robot**: functional model (walk on water) provides pragmatic similarity; structural model of the lizard's locomotion is mapped and transferred to robot design

Design by analogy uses **structure-behavior-function (SBF) models**. Mapping proceeds bottom-up: structural alignment enables behavioral transfer, which enables functional transfer. This is **compositional analogy** — analogy at multiple levels of abstraction.

Compound and Compositional Analogy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Compound analogy**: multiple source cases contribute to a single design (e.g., copepod for slow underwater motion + squid jet propulsion for fast motion → stealth microbot)
- **Compositional analogy**: mapping at one level (structure) supports transfer at the next level (behavior, then function)

The process is iterative — transfer may trigger new retrieval, mapping may trigger new transfer, evaluation may send the agent back to any earlier phase.

Advanced Issues
---------------

- **Common vocabulary**: cross-domain transfer may require shared terms or an alignment mechanism for different vocabularies ("revolve" vs. "rotate")
- **Problem abstraction**: the agent may need to abstract/transform the problem itself to enable retrieval
- **Compound analogy**: combining knowledge from multiple source cases
- **Visuospatial analogies**: analogies where causality is implicit and transfer is primarily spatial/perceptual
- **Conceptual combination**: creating new concepts by merging parts of existing ones via analogy

Cognitive Connection
--------------------

Analogy is considered a core cognitive process. Metaphors are everyday analogies ("we had grown far apart" — spatial metaphor for emotional distance; "All the world's a stage" — theater as metaphor for life). Raven's Progressive Matrices, a widely used intelligence test, is fundamentally based on analogical reasoning.
