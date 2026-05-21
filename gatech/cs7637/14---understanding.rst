.. title: 14 - Understanding 
.. slug: 14 - Understanding 
.. date: 2016-01-23 06:44:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

==================
14 - Understanding
==================

Understanding Overview
----------------------

**Understanding** is making sense of stories, events, and situations in the world. It relies heavily on frames and sets up the infrastructure for commonsense reasoning. The key mechanisms:

- **Thematic role systems** — structured frame representations capturing who did what to whom, with what, for whom
- **Ambiguity resolution** — using constraints and background knowledge to select correct interpretations
- **Grammar and ontology** — guiding interpretation through sentence structure and world knowledge

Thematic Role Systems
---------------------

Consider: "Ashok made pancakes for David with a griddle." Three levels of analysis apply:

- **Lexical**: categorizing words (noun, verb, etc.)
- **Syntactic**: sentence structure (noun phrases, verb phrases)
- **Semantic**: meaning in terms of thematic roles

The semantic analysis is primary — it produces understanding:

- **Agent**: Ashok
- **Action**: make
- **Thematic object**: pancakes
- **Beneficiary**: David
- **Instrument**: griddle

This frame *is* the meaning. Evidence of understanding comes from the ability to draw correct inferences (e.g., "Who ate the pancakes?" → David, even though this isn't stated explicitly). The frame's default values enable such inferences, just as the frame for "eat" has defaults like "the eaten thing is dead."

Thematic role frames generate **expectations**. A frame for "throw" tells us to expect an agent, an object, a trajectory, a destination — even before seeing the full sentence.

Constraints from Prepositions
-----------------------------

Prepositions constrain which thematic roles a word can fill:

- **by** → agent, conveyance, or location
- **for** → beneficiary, duration, or purpose
- **from** → source
- **to** → destination
- **with** → co-agent or instrument

Examples:

- "written **by** Ashok" → Ashok is agent
- "went to New York **by** train" → train is conveyance
- "stood **by** the statue" → statue is location

Prepositions narrow possibilities but don't always determine meaning uniquely — additional knowledge is needed.

Resolving Ambiguity with Ontology
---------------------------------

An **ontology** provides the conceptual vocabulary for interpreting the world:

::

    Things → Agents (People: Ashok, David)
           → Objects (Conveyances: train, car)
           → Locations (statue, park)

When "by" constrains a word to {agent, conveyance, location}, the ontology resolves which applies:

- "by Ashok" → Ashok is People → Agent
- "by train" → train is Conveyance
- "by the statue" → statue is Location

Processing is a combination of **bottom-up** (data-driven lexical analysis) and **top-down** (knowledge-driven expectation generation). Bottom-up processing generates cues that probe memory; memory returns frames that make processing top-down.

Resolving Ambiguity in Verbs
----------------------------

Verbs frequently have multiple meanings. "Take" has at least 12 interpretations: to steal, to medicate, to measure, to transport, to assume control, etc. Each meaning has its own thematic role frame specifying expected slots.

Resolution process for "I took the candy from the baby":

1. Background knowledge about **candy** eliminates meanings requiring medicine, quantity, etc.
2. The preposition **from** requires a "source" slot — eliminates frames without source
3. Only the "to steal" frame remains, with source = baby

Similarly for "My doctor took my blood pressure" — background knowledge of "doctor" and "blood pressure" selects the "to measure" interpretation.

**Particles** further disambiguate: "take over" → assume control; "take off" → remove clothing.

The Earthquake Sentences
-------------------------

"The earthquake killed 25 people" vs. "The president killed 25 proposals":

- **Kill-1** (cause death): expects agent + victim → "25 people" fits victim, "earthquake" fits agent
- **Kill-2** (put an end to): expects agent + object → "25 proposals" fits object, "president" fits agent

Background knowledge determines which frame applies: people can die (Kill-1), proposals cannot die but can be ended (Kill-2).

Limitations: as sentence variations multiply ("took the candy for the baby," "took the medicine from the baby," "took a smile from the baby"), the number of disambiguation rules explodes. The theory covers common cases well but struggles with the full combinatorial space of natural language.

Cognitive Connection
--------------------

Understanding is a general-purpose cognitive task — not limited to language. We make sense of acoustic, visual, verbal, and numerical data using three sources of power:

1. **Constraints** about how the world behaves (physical, social, grammatical)
2. **Structured knowledge representations** — organization of knowledge itself provides power
3. **Bottom-up to top-down processing** — low-level processing activates knowledge structures that generate expectations, making subsequent processing top-down
