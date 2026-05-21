.. title: 06 - Production Systems 
.. slug: 06 - Production Systems 
.. date: 2016-01-30 10:01:45 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

=======================
06 - Production Systems
=======================

Cognitive Architectures
-----------------------

A **cognitive agent** is a function that maps perceptual history into action: P* → A. The central task of cognitive agents is action selection based on accumulated percepts.

Levels of Analysis
~~~~~~~~~~~~~~~~~~

Cognitive architectures can be analyzed at three levels of abstraction (following David Marr and Allen Newell):

1. **Task/Knowledge level** — What task must be performed? What knowledge is needed?
2. **Algorithm/Symbol level** — What methods and representations are used? (e.g., semantic networks, means-ends analysis)
3. **Hardware/Implementation level** — What physical substrate implements it? (e.g., brain, transistors)

These levels constrain each other bidirectionally:

- **Top-down:** The task level defines *content* for the algorithm level, which defines content for hardware.
- **Bottom-up:** Hardware constrains which algorithms are feasible, which constrains what tasks can be performed.

A smartphone illustrates this: at the task level, it enables long-distance communication; at the algorithm level, it uses specific protocols and data structures; at the hardware level, it runs on particular chips and circuits. All three descriptions are legitimate and necessary.

Assumptions of Cognitive Architectures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Six fundamental assumptions about cognitive agents:

1. **Goal-oriented** — agents have goals and act in pursuit of them
2. **Rich environments** — agents operate in complex, dynamic worlds
3. **Knowledge-dependent** — agents use world knowledge to pursue goals
4. **Symbolic abstraction** — knowledge is captured at an appropriate level of abstraction using symbols
5. **Flexible behavior** — behavior adapts as the environment changes
6. **Learning from experience** — agents continuously learn through interaction

Architecture + Content = Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The key equation: **architecture + content = behavior**.

If the architecture is fixed, changing knowledge content alone produces different behaviors. This simplifies both designing intelligent machines (put the right content into a fixed architecture) and understanding human cognition (explain behavioral differences through content differences alone). This parallels computer architecture, where fixed hardware runs different stored programs to produce different behaviors.

SOAR
----

**SOAR** (initiated by Allen Newell, John Laird, and Paul Rosenbloom) is a cognitive architecture primarily for deliberation, though it also covers aspects of reaction and metacognition. Its high-level structure consists of:

- **Long-term memory** containing three kinds of knowledge:

  - **Procedural** — how to do things (e.g., pouring water from a jug into a glass)
  - **Semantic** — generalizations, concepts, and world models (e.g., concept of a human, how planes fly)
  - **Episodic** — specific event instances (e.g., what you had for dinner yesterday)

- **Working memory** — holds current percepts, goals, and intermediate results

The arrangement of these components affords specific processes of reasoning and learning.

Production Rules
----------------

Procedural knowledge in SOAR is represented as **production rules** — if-then rules from which the term "production systems" derives. Each rule has the form:

**IF** <antecedents> **THEN** <consequents>

Antecedents and consequents can be connected by AND/OR operators.

Action Selection Example: Baseball Pitcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A pitcher's working memory contains percepts (inning number, top/bottom, runner positions, outs, batter identity, handedness) and goals (e.g., escape the inning without allowing runs). The pitcher explores an abstract **state space** — a combination of all states achievable by applying various operators from the initial state. Each state is described by features with values, and the pitcher searches for a path from the current state to a goal state.

Sample production rules:

- **R1:** IF goal=escape AND outs=2 AND runner-on-2nd AND no-runner-on-1st → suggest goal: intentionally walk batter
- **R2:** IF goal=escape AND outs=2 AND (runner-on-1st OR not-runner-on-2nd OR no-runners) → suggest goal: get batter out via pitching
- **R3:** IF goal=intentionally-walk-batter → select intentional-walk operator
- **R7:** IF only one operator selected → send operator to motor system and update working memory state

Execution Cycle
~~~~~~~~~~~~~~~

1. Working memory contents are matched against rule antecedents
2. Matching rules fire, writing consequences back to working memory
3. Changed working memory triggers further rule activations
4. Process continues until no more rules fire, yielding a final motor action

Key dynamics:

- **Working memory** contents change rapidly as rules fire
- **Long-term memory** contents change very slowly
- Different percepts activate different rule chains, producing different actions from the same rule set
- Goals appear in production rules, consistent with the assumption that cognitive architectures are goal-oriented
- Knowledge is detailed and specific enough that, in principle, some rule is available for any given set of percepts

When the pitcher's situation changes (e.g., runners now on 1st, 2nd, and 3rd after a successful walk), the same production rules produce different behavior because working memory contents have changed.

Impasses and Chunking
---------------------

An **impasse** occurs when the production system cannot decide — either because insufficient knowledge is available or because multiple actions are suggested with no way to choose between them.

**Chunking** is SOAR's learning mechanism for resolving impasses:

1. The impasse identifies the learning goal (e.g., choose between a curve ball and a fast ball against a left-handed batter)
2. SOAR searches **episodic memory** for relevant past events
3. If a past event involves the same choice and has a known outcome (e.g., throwing a fastball to batter Parra resulted in a home run), SOAR encapsulates this into a new production rule
4. Learned rule example: IF two-operators-suggested AND throw-fast-ball-suggested AND batter=Parra → dismiss throw-fast-ball
5. The new rule is added to procedural memory and breaks the impasse on subsequent encounters

Chunking demonstrates the tight integration of **memory** (procedural + episodic), **reasoning** (decision-making), and **learning** (rule acquisition) in cognitive systems.

Fundamentals of Learning
------------------------

Knowledge-based AI takes a reasoning-first approach to learning:

- Start with a theory of reasoning
- Use it to determine **what** to learn, **when** to learn, and **why** to learn
- Then address **how** to learn

In production systems, reasoning (rule matching) identifies when learning is needed (impasse), what should be learned (an impasse-resolving rule), and the source of learning (episodic memory). This exemplifies a unified theory where the demands of reasoning and memory constrain the learning process.

Cognitive Connection
--------------------

Production systems were proposed from the beginning as models of human cognition:

- **Working memory ↔ short-term memory** — Human short-term verbal memory holds approximately 7 ± 2 elements; working memory in production systems plays an analogous role
- **Behavioral parallels** — Studies comparing SOAR to human performance on closed-world problems (arithmetic, algebra) show strong behavioral similarities
- **Open questions** — Current models work well in constrained domains, but capturing human cognition in open-ended environments remains a major challenge
