.. title: 01 - Introduction to Knowledge-Based AI 
.. slug: 01 - Introduction to Knowledge-Based AI 
.. date: 2016-01-23 06:32:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

========================================
01 - Introduction to Knowledge-Based AI
========================================

Conundrums in AI
----------------

Five fundamental conundrums of AI:

1. **Limited resources vs. intractable problems** — Agents have finite computational resources (processing speed, memory), yet most interesting AI problems are computationally intractable. How can agents achieve near real-time performance?

2. **Local computation vs. global constraints** — All computation is local, but most AI problems have global constraints. How can agents address global problems using only local computation?

3. **Deductive logic vs. abductive/inductive problems** — Computational logic is fundamentally deductive, but many AI problems require abduction or induction.

4. **Dynamic world vs. limited knowledge** — The world is dynamic and knowledge is limited, yet an agent must begin with what it already knows. How can it address novel problems?

5. **Complexity of explanation** — Problem solving, reasoning, and learning are already complex; explanation and justification add further complexity. How can an agent explain or justify its decisions?

Characteristics of AI Problems
-------------------------------

Six key characteristics of AI problems:

1. **Incremental data** — Data arrives incrementally, not all at once
2. **Recurring patterns** — The same kinds of problems recur
3. **Multiple abstraction levels** — Problems occur at many levels of abstraction
4. **Computational intractability** — Many interesting problems are computationally intractable
5. **Dynamic world** — The world constantly changes, but knowledge remains relatively static
6. **Open-ended world** — The world is open-ended, but knowledge is relatively limited

Characteristics of AI Agents
-----------------------------

Five properties of AI agents:

1. **Limited computing power** — Finite processing speed and memory
2. **Limited sensors** — Cannot perceive everything in the world
3. **Limited attention** — Cannot focus on everything simultaneously
4. **Deductive logic** — Computational logic is fundamentally deductive
5. **Incomplete knowledge** — Knowledge of the world is incomplete relative to the world's complexity

The central question: how can agents with such **bounded rationality** address open-ended problems?

What is Knowledge-Based AI
--------------------------

KBAI centers on three fundamental, interconnected processes:

- **Reasoning** — Understanding natural language, making decisions, generating responses
- **Learning** — Acquiring new knowledge, storing correct answers, updating from mistakes
- **Memory** — Storing what is learned and providing access to knowledge needed for reasoning

These three processes form a tightly coupled cycle: we learn so we can reason; reasoning produces additional learning; learning is stored in memory; reasoning requires knowledge that memory provides. The more we know, the more we can learn. Together, these processes constitute **deliberation**.

The full cognitive agent architecture maps percepts (input) to actions (output) through three layers:

- **Reaction** — Direct mapping of percepts to actions (no planning)
- **Deliberation** — Reasoning, learning, and memory working together
- **Metacognition** — Reasoning about one's own deliberation and reaction

The Four Schools of AI
----------------------

AI can be categorized along two dimensions:

- **Thinking vs. Acting** — Planning a route (thinking) vs. driving a car (acting)
- **Optimal vs. Human-like** — Optimizing for a specific task vs. exhibiting general human-like intelligence

This yields four quadrants:

- **Thinking optimally** — Many machine learning algorithms that analyze large datasets for optimal patterns
- **Acting optimally** — Airplane autopilots
- **Acting like humans** — Improvisational robots that dance to music
- **Thinking like humans** — Semantic web technologies; Knowledge-Based AI

KBAI falls in the **thinking like humans** quadrant. An autonomous vehicle might belong to "acting optimally," but studying how humans drive can inform robot design, and robot design can illuminate human cognition — this bidirectional relationship is a key pattern in KBAI.

Cognitive Systems
-----------------

The course subtitle is **Cognitive Systems**:

- **Cognitive** — Dealing with human-like intelligence
- **Systems** — Multiple interacting components (learning, reasoning, memory)

A cognitive system is situated in both a physical world and a social world. It takes percepts as input (via sensors) and produces actions as output (via actuators). Multiple cognitive systems can interact with each other.

The **three-layered architecture** of a cognitive system:

1. **Reaction** — Direct percept-to-action mapping. Example: seeing brake lights turn red and immediately pressing your brakes. No planning involved.

2. **Deliberation** — Goal-directed reasoning using learning, reasoning, and memory. Example: planning a lane change by assessing positions of surrounding cars and choosing left vs. right.

3. **Metacognition** — Reasoning about one's own reasoning. Example: after a poorly executed lane change (cars honked because insufficient space was left), reflecting on the deliberation that produced the suboptimal plan and adjusting future behavior.

Intelligence is about mapping percepts to actions — selecting the right action given a particular world state. The three layers represent increasingly sophisticated ways to achieve this mapping.

Course Topics
-------------

The course is organized into eight major units:

1. **Fundamentals** — Knowledge representations (Semantic Networks, Production Systems) and reasoning strategies (Generate & Test, Means-End Analysis, Problem Reduction)
2. **Planning** — Logic as a knowledge representation, then systematic planning for achieving goals
3. **Common Sense Reasoning** — Reasoning about everyday situations (e.g., inferring who has the book after "John gave the book to Mary"); uses frames as a knowledge representation
4. **Learning** — A recurring theme throughout the course, with a dedicated unit covering multiple learning methods
5. **Analogical Reasoning** — Reasoning about novel problems by analogy to familiar ones; includes learning by recording cases and explanation-based learning
6. **Visuospatial Reasoning** — Reasoning with visual knowledge (e.g., diagram-based reasoning); uses constraint propagation
7. **Design & Creativity** — Building AI that handles novel situations with creative solutions
8. **Metacognition** — Thinking about thinking; course concludes with Ethics in AI

Topics are interleaved across units rather than covered sequentially.

The Cognitive Connection
------------------------

KBAI is richly connected to cognitive science. Many course topics relate to human reasoning, learning, and memory. A key course goal is learning to use AI agent design to reflect on human cognition.
