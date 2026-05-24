Wrap-Up
=======

Cognitive Systems Architecture Revisited
-----------------------------------------

The three-space architecture for cognitive systems:

- **Reactive space** — directly maps percepts to actions (see → act)
- **Deliberative space** — mediates percept-to-action mappings through reasoning, learning, and memory (see → think → act)
- **Metacognitive space** — monitors and acts on the deliberative reasoning; can also act on itself recursively

These are best understood as overlapping spaces rather than disjoint layers. The cognitive system is continuously situated in and interacting with both the physical and social worlds — percepts, goals, communication, and feedback flow constantly.

Key points:

- If input is a goal → output may be a plan or action
- If input is new information → system learns and stores in memory
- If input is a percept → output is a reactive or deliberated action
- Metacognition is "situated in the internal world" — its objects are thoughts, learning processes, and reasoning strategies
- The system interacts with other cognitive systems (social world), learning from their actions and making sense of them (e.g., using scripts)

Principle 1: Represent and Organize Knowledge
----------------------------------------------

KBAI agents represent and organize knowledge into **knowledge structures** to guide and support reasoning.

Examples:

- **Semantic networks** — expose constraints clearly (guards & prisoners dilemma); organization eliminates irrelevant choices
- **Frames** — support reasoning about sentences ("earthquake killed 25 people") and common sense reasoning
- **Scripts** — organize actions into sequences, generate expectations, detect surprises
- **Explanation-based learning** — compose complex knowledge structures on the fly from smaller precedents to support reasoning about concept membership

Principle 2: Incremental Learning
----------------------------------

Learning in KBAI is typically **incremental** — information arrives one piece at a time rather than all at once.

Examples:

- **Learning by recording cases** — individual experiences are the increments
- **Case-based reasoning** — cases arrive one by one, organized into discrimination trees
- **Incremental concept learning** — positive/negative examples arrive sequentially; concept definition evolves with each
- **Version spaces** — examples arrive one at a time; specific model generalizes, general model specializes
- **Learning by correcting mistakes** — individual failures drive incremental knowledge repair

This mirrors human experience: we encounter the world experience by experience, not as a batch.

Principle 3: Top-Down and Bottom-Up Reasoning
----------------------------------------------

Reasoning in KBAI is both bottom-up (data-driven) and **top-down** (expectation-driven):

1. Low-level processing of input data invokes knowledge structures from memory
2. Those structures generate **expectations** about the world
3. Expectations guide further interpretation (top-down)

Examples:

- **Frames** — parsing "Angela ate lasagna at Olive Garden" invokes a dining frame that generates expectations (object is no longer alive, subject is happy, etc.)
- **Scripts** — predict the next action; violations signal surprises
- **Constraint propagation** — knowledge about valid junction types generates expectations for interpreting line drawings

Current cognitive science theories view brains as **predictive machines** — constantly generating expectations that guide reasoning and action.

Principle 4: Match Methods to Tasks
------------------------------------

KBAI agents match problem-solving **methods** to **tasks**:

- General methods (generate & test, means-ends analysis) are powerful but not optimal for any single task
- Specific methods (planning, constraint propagation) address narrower problems more effectively
- Tasks (configuration, diagnosis, design) can each be addressed by multiple methods
- Methods spawn sub-tasks, which may require different methods (strategy integration)
- Matching can be done by the designer or by the agent itself (via meta-reasoning)

Principle 5: Heuristics and Satisficing
----------------------------------------

KBAI agents use **heuristics** to find solutions that are good enough, not necessarily optimal (**satisficing**, per Herbert Simon).

Rationale: AI agents have bounded rationality (limited processing, limited memory) yet face computationally intractable problems. The tradeoff is between optimality and computational efficiency.

Examples:

- **Incremental concept learning** — require-link heuristic narrows concept definitions efficiently
- **Means-ends analysis** — heuristic: select operator that reduces difference to goal (efficient when it works, but no optimality guarantee)
- **Generate & test** — heuristic: don't generate states that duplicate previously generated states

Humans likewise rarely find optimal solutions — our plans for dinner, commutes, and daily tasks are "good enough" found in near real-time. The power lies in robust, flexible intelligence across a very large class of problems.

Principle 6: Exploit Recurring Patterns
----------------------------------------

KBAI agents leverage **recurring patterns** in problems:

- **Learning by recording cases** — assume a past solution applies directly to a new identical problem
- **Case-based reasoning** — adapt past solutions; the pattern is similar even if the new problem differs in specifics
- **Analogical reasoning** — abstract patterns from one domain and transfer to another
- **Configuration** — the overall design pattern recurs; only variable values change per instance

This is not at odds with addressing novel problems — agents use recurring patterns *in conjunction with* other reasoning methods to handle novelty.

Principle 7: Unified Reasoning, Learning, and Memory
-----------------------------------------------------

The KBAI architecture enables reasoning, learning, and memory to **support and constrain each other** — they are not independent modules.

- **Memory** stores and organizes knowledge
- **Learning** acquires knowledge
- **Reasoning** uses knowledge
- Knowledge is the glue connecting all three

Examples:

- **Production systems** — reasoning reaches impasse → memory supplies episodic knowledge → chunking (learning) extracts a rule → reasoning proceeds
- **Logic** — the knowledge base (memory) determines what can be proved (reasoning); reasoning needs drive what must be stored
- **Explanation-based learning** — memory supplies precedents → reasoning composes an explanation → learning captures the new connections
- **Correcting mistakes** — memory provides prior knowledge → reasoning identifies the fault → learning repairs it

This mirrors human cognition where reasoning, learning, and memory are inseparably intertwined.

Current Research
----------------

Active knowledge-based AI projects:

- **CALO** — Cognitive Assistant that Learns and Organizes (precursor to Apple's Siri)
- **Cyc** and **OMCS** (Open Mind Common Sense) — large knowledge bases for everyday commonsense reasoning
- **Wolfram Alpha** — search engine using structured knowledge representations

Georgia Tech projects:

- **VITA** — computational model of visual thinking in autism; solves Raven's Progressive Matrices using only visuospatial representations
- **Dramatis** — computational model of suspense in drama/stories
- **DANE** — supports biologically-inspired design through analogies to natural systems
