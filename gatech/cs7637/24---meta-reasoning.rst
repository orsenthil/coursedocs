Meta-Reasoning
==============


Introduction
------------

**Meta-reasoning** is thinking about thinking — knowledge about knowledge. The agent reasons not about the external world but about its own knowledge, reasoning, and learning. A simple demonstration: you can immediately answer "I don't know" to "What is Obama's phone number?" — but *how* do you know that you don't know?

Meta-reasoning addresses:

- Errors and gaps in knowledge
- Errors and gaps in reasoning
- Errors and gaps in learning
- Strategy selection and integration
- Goal-based autonomy


Mistakes in Knowledge, Reasoning, and Learning
-----------------------------------------------

**Knowledge errors** — The learning-by-correcting-mistakes approach: the agent reflects on its stored knowledge (e.g., an explanation proving an object is a cup), identifies false suspicious features, and repairs the knowledge.

**Reasoning errors** — Example from means-ends analysis in the blocks world: the agent pursues multiple goals and reaches a cul-de-sac where no progress is possible without undoing earlier work. Metacognition detects the reasoning error and selects a different strategy (e.g., problem reduction to decompose into independent subgoals).

**Learning errors** — The agent reflects on the *process* that produced incorrect knowledge. If explanation-based learning built a faulty explanation, the agent asks: "What went wrong in my learning process? How do I fix the process itself so the same class of error doesn't recur?"


Knowledge Gaps
--------------

Beyond errors (incorrect knowledge), agents face **gaps** (missing knowledge). Example from explanation-based learning: the agent builds part of an explanation but cannot connect two pieces because the bridging knowledge is absent.

When the agent detects a gap, it **spawns a learning goal** — acquire knowledge that connects the two pieces. The goal may be satisfied by:

- Retrieving a relevant precedent from memory
- Seeking information from the external world (e.g., asking a teacher)

Similarly, **reasoning gaps** can be addressed by spawning a new reasoning goal. In the blocks-world cul-de-sac, the agent sets up a goal to resolve the impasse, selects problem reduction as a strategy, decomposes into independent subgoals, then returns to means-ends analysis for each.


The Blurred Line Between Cognition and Metacognition
----------------------------------------------------

The three-layer architecture (reaction, deliberation, metacognition) is conceptual — in practice, the boundaries between deliberation and metacognition are blurry. Many deliberative processes can be viewed as metacognitive and vice versa.

Rather than worrying about which box a process belongs in, focus on:

- What knowledge is needed to carry out the process?
- What is the process itself?

Think of deliberation and metacognition as overlapping spaces rather than disjoint layers.


Strategy Selection
------------------

Given a problem, an agent may have many applicable methods (case-based reasoning, constraint propagation, means-ends analysis, generate & test, etc.). Metacognition selects among them using three criteria:

1. **Knowledge availability** — Each method requires specific knowledge (cases, constraints, operators, etc.). If the required knowledge isn't available for the given problem, the method cannot be used.

2. **Computational efficiency** — For problems very similar to prior cases, case-based reasoning is efficient. For problems with a single clear goal, means-ends analysis works well. For complex multi-goal problems, means-ends analysis may be inefficient due to cul-de-sacs.

3. **Quality of solutions** — Some methods (e.g., logic) provide guarantees of correctness but may be computationally expensive. When solution quality is paramount and efficiency is secondary, prefer methods with quality guarantees.

The same analysis applies to selecting among learning methods (e.g., incremental concept learning for sequential examples vs. decision-tree learning for batch examples).


Strategy Integration
--------------------

An agent is not locked into a single strategy. As problem-solving evolves, metacognition can shift between strategies:

- Case-based reasoning is selected at the top level
- It spawns sub-tasks (retrieval, adaptation, evaluation, storage)
- For the adaptation sub-task, metacognition may select rule-based reasoning
- At the next level down, meta-rules select which specific rule to apply

Example of seamless integration: means-ends analysis reaches a cul-de-sac → metacognition sets up a reasoning goal → selects problem reduction → decomposes into independent subgoals → returns to means-ends analysis for each subgoal.


Meta-Meta-Reasoning
-------------------

Does metacognition need an additional meta-meta layer reasoning over it? No — metacognition uses the same structures (cases, rules, models) as deliberation, so it is already equipped to reason about itself recursively. Current theories model this as a two-layer system (deliberation + metacognition) where metacognition monitors itself without requiring infinite regress.


Goal-Based Autonomy
-------------------

**Goal-based autonomy** arises when an agent receives a *new* goal it wasn't explicitly programmed for. Rather than failing brittly, a robust agent uses metacognition to adapt its reasoning and learning methods to the new goal.

Example: A robot programmed to assemble cameras is asked to *disassemble* one. Metacognition enables dynamic, flexible selection and integration of strategies to achieve goals the agent was not originally designed for — mirroring the robustness and flexibility of human cognition.


Connections Across the Course
-----------------------------

Metacognition has been implicit throughout the course:

- **Learning by correcting mistakes** — agent reflects on its own knowledge
- **Partial-order planning** — agent reasons about conflicts between its own plans
- **Production systems** — agent reaches an impasse, spawns a learning goal, uses chunking to extract a rule from episodic memory
- **Version spaces** — agent monitors convergence of its specific and general models
- **Diagnosis** — when treatment fails, the agent diagnoses its own diagnostic process


Cognitive Connection
--------------------

Meta-reasoning is arguably the most critical process in human cognition. Research suggests that developing metacognitive skills early in life may be the best predictor of academic success. Meta-reasoning is not about learning new information — it is about learning *how to learn* and acquiring new reasoning strategies.

Meta-reasoning is also connected to creativity: the agent monitors its own reasoning, spawns goals, suspends or abandons goals — all part of the creative process. Creativity is not just about novel products but about novel *processes* that lead to interesting products.
