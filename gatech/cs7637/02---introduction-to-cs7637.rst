.. title: Course Introduction
.. slug: Course Introduction
.. date: 2016-01-23 06:33:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Course Introduction
===================

Class Goals and Outcomes
------------------------

Four major learning goals:

1. **Core KBAI methods** — Knowledge representation schemes, memory organization, reasoning methods, learning methods, cognitive architectures, and meta-reasoning (reasoning about reasoning)
2. **Common KBAI tasks** — Classification, understanding, planning, explanation, diagnosis, and design
3. **Methods-to-tasks mapping** — How AI agents use specific methods to address specific tasks
4. **KBAI and cognitive science** — Using theories of human cognition to inspire human-like AI design, and using AI techniques to generate testable hypotheses about human cognition

Learning outcomes: upon completion, students can (1) design, implement, evaluate, and describe knowledge-based AI agents, (2) apply KBAI strategies to practical problems, and (3) use AI agent design to reflect on human cognition.

Class Strategies
----------------

Five learning strategies used in the course:

1. **Learning by Example** — Each lesson starts with an example of the target reasoning
2. **Learning by Doing** — Lessons end with exercises requiring the same reasoning
3. **Project-Based Learning** — The course is structured around challenging programming projects
4. **Personalized Learning** — Lessons can be watched in any order, at any pace
5. **Learning by Reflection** — Each lesson and project concludes with reflection on what was learned

Computational Psychometrics
---------------------------

**Psychometrics** is the study of human intelligence, aptitude, and knowledge. **Computational psychometrics** is the design of computational agents that take the same tests humans do for intelligence, knowledge, or aptitude.

The approach: design an AI agent to take an intelligence test, then compare its performance and error patterns with those of humans. If the agent performs comparably and makes similar errors, one might conjecture that its reasoning mirrors human reasoning.

Raven's Progressive Matrices
-----------------------------

The class projects center on **Raven's Progressive Matrices** (RPM), the most widely used and reliable test of human intelligence. Created in the 1930s, it consists of 60 multiple-choice visual analogy problems — strictly visual, no words.

Three problem types:

- **2x1 matrices** — Given A:B :: C:?, pick D from six choices. The relationship between A and B must hold between C and D.
- **2x2 matrices** — A four-cell grid where A:B :: C:D horizontally *and* A:C :: B:D vertically. Diagonal relationships (A:D :: B:C) can also constrain the answer.
- **3x3 matrices** — A nine-cell grid (A–I, with I unknown). Relationships must hold across all rows, columns, and diagonals. These are the most complex problems.

Key observations from working through examples:

- **Multiple valid interpretations** — A transformation between A and B might be described as rotation *or* reflection, sometimes yielding different answers. The challenge for AI: which interpretation to prefer?
- **Generate and test** — A common strategy is to generate a candidate answer, test it against the choices, and revise if the test fails. This is a recurring KBAI reasoning pattern.
- **XOR relationships** — In harder 3x3 problems, the relationship between cells can be an exclusive-or operation on sub-elements (a cell contains an element iff it appears in exactly one of the two preceding cells in its row/column).
- **Varying strategies** — Different problems require fundamentally different reasoning processes; no single strategy works for all.

The question of intelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an AI agent passes an intelligence test, is it intelligent? At a certain level, humans too are "just processing signals and inputs." Intelligence is hard to define — just as life scientists study life without a universal definition, cognitive scientists study intelligence without necessarily defining it. KBAI takes the view that **knowledge is central to human-level intelligence**.

Principles of CS7637
--------------------

Seven recurring principles that organize the course:

1. **Knowledge structures guide reasoning** — Agents use knowledge to guide reasoning and organize it into knowledge structures
2. **Incremental learning** — Learning is often incremental, matching the incremental nature of experience and data
3. **Top-down reasoning** — Reasoning is top-down, not just bottom-up; agents use data to retrieve knowledge from memory, then use that knowledge to generate expectations
4. **Methods-task matching** — Agents match methods to tasks, and can integrate different methods for complex tasks
5. **Heuristic solutions** — Agents use heuristics to find solutions that are good enough (not necessarily optimal), trading optimality for computational efficiency to achieve near real-time performance
6. **Recurring patterns** — Agents exploit recurring patterns in the world's problems
7. **Unified reasoning, learning, and memory** — These three processes constrain and support each other; theories should unify all three into one cognitive system

The Cognitive Connection
------------------------

**Computational psychometrics** provides a bridge between AI and cognitive science. Building AI agents for the Raven's test creates opportunities to think about human cognition:

- Comparing AI error patterns with human error patterns can generate hypotheses about human thinking
- People with autism perform comparably to neurotypical people on Raven's test (unlike other intelligence tests), possibly because Raven's is purely visual — suggesting their thinking strategies may be better aligned with visual reasoning
- Raven's is unique among intelligence tests in being entirely visual; all other tests include substantial verbal components

References
----------

Key textbooks for the course:

- *Artificial Intelligence* — Patrick Winston
- *Knowledge Systems* — Mark Stefik
- *Artificial Intelligence* — Elaine Rich and Kevin Knight
- *Artificial Intelligence: A Modern Approach* — Stuart Russell and Peter Norvig
