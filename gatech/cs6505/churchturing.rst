Church-Turing Thesis
====================

*From Computability, Complexity & Algorithms — Charles Brubaker and Lance Fortnow*

* Refer to the class notes in this Shared Google Drive - https://drive.google.com/drive/folders/1N7WgkJFYJRK1TL7Hgx3msN7ukAYHU-gD?usp=sharing
* http://omscs.wikidot.com/courses:cs6505
* Source: https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6505/churchturing.html

----

The Thesis
----------

**Church-Turing Thesis:** Everything computable is computable by a Turing machine.

This is a **thesis**, not a theorem — it cannot be formally proved since it is a claim
about the physical world (what any conceivable computing device can do). It is supported
by the fact that every reasonable computational model proposed so far has been shown
equivalent in power to the standard Turing machine.

.. figure:: images/churchturing/EquivalenceGraph.png
   :alt: EquivalenceGraph

   All known reasonable computational models — multitape TMs, RAM machines, modern CPUs,
   even quantum and probabilistic computers — are mutually equivalent in computational power.

Two machines are **equivalent** when they accept the same inputs, reject the same inputs,
loop on the same inputs, and halt with matching tape contents.

----

Multitape Turing Machines
--------------------------

A **k-tape Turing machine** has :math:`k` independent tapes each with its own
read/write head. The transition function generalises to:

.. math::

   \delta : Q \times \Gamma^k \to Q \times \Gamma^k \times \{L, R, S\}^k

where :math:`S` means "stay put" (head does not move).

.. figure:: images/churchturing/MultitapeDiagram.png
   :alt: MultitapeDiagram

   A multitape Turing machine with multiple independent read/write heads.

.. figure:: images/churchturing/StayputMachine.png
   :alt: StayputMachine

   Simulating a stay-put :math:`S` move: go left then immediately go right to stay in place.

Multitape machines simplify programming significantly. For example, duplicating input:

.. figure:: images/churchturing/DuplicateInputComputation.png
   :alt: DuplicateInputComputation

   A two-tape machine duplicating input separated by :math:`\#` — far simpler than the
   single-tape equivalent.

.. figure:: images/churchturing/SubstringSearchQuiz.png
   :alt: SubstringSearchQuiz

   *Quiz:* Design a two-tape TM for substring search.

Simulating Multitape on a Single Tape
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A single-tape TM can simulate a :math:`k`-tape TM by interleaving the contents of all
:math:`k` tapes on one tape, using **dotted symbols** to mark current head positions.

.. figure:: images/churchturing/MultiVsSingleTapeDiagram.png
   :alt: MultiVsSingleTapeDiagram

   Single-tape encoding of a multitape configuration: tapes separated by
   :math:`\#`, dotted symbols mark head positions.

**Simulation steps per multitape step:**

1. Scan rightward to read all dotted (marked) symbols — find the "virtual head" on each tape.
2. Scan leftward, updating symbols and shifting dotted markers as needed.

.. figure:: images/churchturing/MultiVsSingleTapeQuiz.png
   :alt: MultiVsSingleTapeQuiz

   *Quiz:* If the multitape TM runs in :math:`T(n)` steps, what is the single-tape
   simulation's running time?

**Answer:** :math:`O(T(n)^2)` — each simulated step scans the entire tape of length
:math:`O(T(n))`.

----

Random Access Machines (RAM)
------------------------------

The **RAM model** mirrors a modern CPU:

* Registers :math:`r_0, r_1, r_2, \ldots` storing non-negative integers.
* Infinite addressable memory indexed by non-negative integers.
* Instructions: ``read``, ``write``, ``load``, ``store``, ``add``, ``subtract``,
  ``jump``, ``halt``.
* A program counter sequencing instructions.

.. figure:: images/churchturing/RAMDiagram.png
   :alt: RAMDiagram

   RAM architecture: registers, memory, and instruction set resembling assembly code.

RAM Simulates Turing Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/churchturing/RAMSimTuring.png
   :alt: RAMSimTuring

   Pseudocode: RAM simulating a TM. Tape cells stored in memory; state and head
   position in registers. Each TM step is a constant number of RAM instructions.

Turing Machine Simulates RAM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A multitape TM can simulate a RAM by dedicating tapes to:

* The program (instruction sequence).
* The program counter.
* Each register.
* The memory array (stored as index-value pairs).

.. figure:: images/churchturing/TuringSimRAM.png
   :alt: TuringSimRAM

   Multitape TM simulating RAM — uses one tape per register and one for memory.

.. figure:: images/churchturing/RAMVsMultiTapeQuiz.png
   :alt: RAMVsMultiTapeQuiz

   *Quiz:* If a RAM runs in :math:`T(n)` steps using values :math:`\leq V`, what is
   the multitape TM simulation overhead?

**Answer:** :math:`O(T(n)^2 \log V)` — each RAM step requires scanning memory tapes,
and values need :math:`O(\log V)` bits to encode.

----

Implications
------------

Since Turing machines can simulate RAMs, and RAMs resemble standard CPUs, the
Church-Turing Thesis extends to:

* Multi-core processors
* Cloud computing clusters
* Probabilistic (randomised) computers
* Quantum computers
* DNA computing

All of these are provably no more powerful than a single-tape Turing machine in terms
of *what* they can compute (though they may differ in *how fast* they compute it).

**Profound consequence:** Because Turing machines cannot solve the halting problem
(proved by diagonalisation), **no physical computing device can solve it either** —
the limits of computation are absolute and device-independent.

----

Key Formulas
------------

**Multitape transition function:**

.. math::

   \delta : Q \times \Gamma^k \to Q \times \Gamma^k \times \{L, R, S\}^k

**Simulation overhead (multitape → single-tape):**

.. math::

   T_\text{single}(n) = O\!\left(T_\text{multi}(n)^2\right)

**Church-Turing Thesis (informal):**

.. math::

   \text{Computable} \;\equiv\; \text{Turing-computable}

----

Further Reading
---------------

* Alonzo Church's :math:`\lambda`-calculus and its equivalence to Turing machines
* Nondeterministic Turing machines and the P vs. NP question
* Oracle Turing machines and relativised complexity
