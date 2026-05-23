Computability and Complexity
============================

*From Computability, Complexity & Algorithms — Charles Brubaker and Lance Fortnow*

* Refer to the class notes in this Shared Google Drive - https://drive.google.com/drive/folders/1N7WgkJFYJRK1TL7Hgx3msN7ukAYHU-gD?usp=sharing
* http://omscs.wikidot.com/courses:cs6505
* Source: https://s3.amazonaws.com/content.udacity-data.com/courses/gt-cs6505/ComputabilityAndComplexity.html

This page is a comprehensive overview of the full course. Detailed notes for each topic
are in their own files. The sections below give the full arc from formal languages through
undecidability.

----

Part 1: Formal Languages and Countability
------------------------------------------

.. figure:: images/languagescountability/HSClassroom.png
   :alt: HSClassroom

   The distinction between procedural (algorithmic) and mathematical (set-theoretic)
   definitions of functions — the starting point for computability theory.

Functions vs. Computability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Procedural function:** a finite algorithm that computes output from input.
* **Mathematical function:** any set of ordered pairs :math:`(x, y)` with unique :math:`y` per :math:`x`.

Not every mathematical function is computable. Some functions require infinitely many
steps on some inputs — they lie beyond any algorithm's reach.

.. figure:: images/languagescountability/RulesofGame.png
   :alt: RulesofGame

   A machine processing input to produce output — the basic computational model.

Strings and Languages
~~~~~~~~~~~~~~~~~~~~~

A **string** is a finite sequence of symbols from a finite **alphabet** :math:`\Sigma`.
A **language** is any set of strings over :math:`\Sigma`.

.. figure:: images/languagescountability/SymbolStringLanguage.png
   :alt: SymbolStringLanguage

   Hierarchy: symbols → strings → languages.

Language operations:

.. figure:: images/languagescountability/LanguageOperations.png
   :alt: LanguageOperations

   Union :math:`A \cup B`, intersection :math:`A \cap B`, complement :math:`\overline{A}`,
   concatenation :math:`A \cdot B`, Kleene star :math:`A^*`.

.. figure:: images/languagescountability/LanguageOpsQuiz.png
   :alt: LanguageOpsQuiz

   *Quiz:* Evaluate language operation expressions.

Countability
~~~~~~~~~~~~

A set is **countable** if it is finite or in bijection with :math:`\mathbb{N}`.

.. figure:: images/languagescountability/OnetoOneCorrespondence.png
   :alt: OnetoOneCorrespondence

   A bijection between integers and permutations demonstrates countability.

.. figure:: images/languagescountability/BinaryLanguageEnumeration.png
   :alt: BinaryLanguageEnumeration

   Enumerating all binary strings by length — strings over any finite alphabet are countable.

.. figure:: images/languagescountability/CountableUnionFinite.png
   :alt: CountableUnionFinite

   A countable union of finite sets is countable.

.. figure:: images/languagescountability/CountableUnionCountable.png
   :alt: CountableUnionCountable

   A countable union of countable sets is countable — proved by diagonal traversal.

.. figure:: images/languagescountability/AFalseProof.png
   :alt: AFalseProof

   *Quiz:* Identify the flaw in this proof.

**Diagonalization — languages are uncountable:**

.. figure:: images/languagescountability/DiagTableIllustrated.png
   :alt: DiagTableIllustrated

   Assume an enumeration of all languages. Construct a language :math:`L_D` that differs
   from every enumerated language :math:`L_i` on string :math:`s_i` — :math:`L_D` is not
   in the enumeration. Contradiction: the set of all languages is **uncountable**.

**Key consequence:** Programs are finite strings — countably many. But languages
(equivalently, functions) are uncountable. Therefore uncountably many functions have
no algorithmic solution.

----

Part 2: Turing Machines
------------------------

.. figure:: images/turingmachines/TuringPortrait.png
   :alt: TuringPortrait

   Alan Turing (1912–1954), inventor of the Turing machine model.

.. figure:: images/turingmachines/PhysicalTM.png
   :alt: PhysicalTM

   A physical Turing machine — infinite tape, read/write head, finite control.

.. figure:: images/turingmachines/Arithbook.png
   :alt: Arithbook

   Motivating analogy: arithmetic done on paper with finite rules.

.. figure:: images/turingmachines/LongTheorem.png
   :alt: LongTheorem

   Human computation is bounded by perception — machines extend this without limit.

Formal Definition
~~~~~~~~~~~~~~~~~

A Turing machine is a 7-tuple :math:`(Q, \Sigma, \Gamma, \delta, q_0, q_\text{acc}, q_\text{rej})`:

.. list-table::
   :widths: 20 80

   * - :math:`Q`
     - Finite set of states
   * - :math:`\Sigma`
     - Input alphabet (excludes blank :math:`\sqcup`)
   * - :math:`\Gamma`
     - Tape alphabet (:math:`\Sigma \cup \{\sqcup\} \subseteq \Gamma`)
   * - :math:`\delta`
     - :math:`Q \times \Gamma \to Q \times \Gamma \times \{L, R\}` — transition function
   * - :math:`q_0`
     - Start state
   * - :math:`q_\text{acc}`
     - Accept state
   * - :math:`q_\text{rej}`
     - Reject state

.. figure:: images/turingmachines/TMDiagram.png
   :alt: TMDiagram

   Turing machine components: tape, head, and finite control.

.. figure:: images/turingmachines/TMNotation.png
   :alt: TMNotation

   Mathematical notation for specifying a Turing machine.

Examples
~~~~~~~~

.. figure:: images/turingmachines/TestOddnessExampleTM.png
   :alt: TestOddnessExampleTM

   TM testing whether a binary number is odd — check the last bit.

.. figure:: images/turingmachines/ConfigSequenceIllustration.png
   :alt: ConfigSequenceIllustration

   A **configuration** is a snapshot: current state, tape contents, head position.
   Computation is a sequence of configurations.

.. figure:: images/turingmachines/TMEqualityTestExample.png
   :alt: TMEqualityTestExample

   TM deciding :math:`\{w\#w \mid w \in \{0,1\}^*\}` — match symbols across the :math:`\#`.

.. figure:: images/turingmachines/TMEqualityTestComputation.png
   :alt: TMEqualityTestComputation

   State-by-state trace of the equality-test computation.

.. figure:: images/turingmachines/TMConfigQuiz.png
   :alt: TMConfigQuiz

   *Quiz:* Determine the next configuration in a computation.

.. figure:: images/turingmachines/RightShiftQuiz.png
   :alt: RightShiftQuiz

   *Quiz:* Design a TM that right-shifts its tape contents by one cell.

.. figure:: images/turingmachines/BalancedStringQuiz.png
   :alt: BalancedStringQuiz

   *Quiz:* Design a TM recognising balanced parentheses.

Deciding vs. Recognising
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/turingmachines/LanguageDeciders.png
   :alt: LanguageDeciders

   A **decider** halts on every input — accepting members, rejecting non-members.

.. figure:: images/turingmachines/DecidesContainsOneQuiz.png
   :alt: DecidesContainsOneQuiz

   *Quiz:* Build a decider for strings containing at least one ``1``.

.. figure:: images/turingmachines/DecideVsRecognize.png
   :alt: DecideVsRecognize

   A **recogniser** accepts members but may loop on non-members.
   Every decidable language is recognisable; the converse fails.

.. figure:: images/turingmachines/DefLanguageOfMachine.png
   :alt: DefLanguageOfMachine

   :math:`L(M)` = the set of strings :math:`M` accepts.

----

Part 3: Church-Turing Thesis
------------------------------

**Thesis:** Everything computable is computable by a Turing machine.

This is a thesis (not a theorem) — it cannot be formally proved, but is supported by
the equivalence of all known reasonable computational models.

.. figure:: images/churchturing/EquivalenceGraph.png
   :alt: EquivalenceGraph

   Computational models — multitape TMs, RAM machines, modern CPUs — are all
   equivalent in power to the standard single-tape TM.

Multitape Turing Machines
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/churchturing/MultitapeDiagram.png
   :alt: MultitapeDiagram

   A multitape TM has several tapes with independent read/write heads.

.. figure:: images/churchturing/DuplicateInputComputation.png
   :alt: DuplicateInputComputation

   Example: duplicating input using two tapes.

.. figure:: images/churchturing/SubstringSearchQuiz.png
   :alt: SubstringSearchQuiz

   *Quiz:* Design a multitape TM for substring search.

**Simulation:** A single-tape TM can simulate a :math:`k`-tape TM by interleaving
tape contents with markers for head positions.

.. figure:: images/churchturing/MultiVsSingleTapeDiagram.png
   :alt: MultiVsSingleTapeDiagram

   Single-tape encoding of a multitape configuration.

.. figure:: images/churchturing/MultiVsSingleTapeQuiz.png
   :alt: MultiVsSingleTapeQuiz

   *Quiz:* What is the overhead of the single-tape simulation?

.. figure:: images/churchturing/StayputMachine.png
   :alt: StayputMachine

   Simulating a "stay-put" head movement using left-then-right.

Random Access Machines (RAM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/churchturing/RAMDiagram.png
   :alt: RAMDiagram

   A RAM machine: registers, indexed memory, and arithmetic operations —
   resembles a modern CPU.

.. figure:: images/churchturing/RAMSimTuring.png
   :alt: RAMSimTuring

   Pseudocode: RAM simulating a Turing machine (tape ↔ indexed memory).

.. figure:: images/churchturing/TuringSimRAM.png
   :alt: TuringSimRAM

   Multitape Turing machine simulating a RAM using tapes for registers and memory.

.. figure:: images/churchturing/RAMVsMultiTapeQuiz.png
   :alt: RAMVsMultiTapeQuiz

   *Quiz:* What is the time overhead of TM-simulating-RAM?

----

Part 4: Universality
---------------------

A **Universal Turing Machine** (UTM) accepts an encoded machine description
:math:`\langle M \rangle` and input :math:`w`, then simulates :math:`M` on :math:`w`.
This shows that **programs are data**.

Encoding
~~~~~~~~

.. figure:: images/universality/TMEncodingExample.png
   :alt: TMEncodingExample

   Encoding a TM as a binary string: states as :math:`q_i`, symbols as :math:`a_j`,
   transitions as tuples.

.. figure:: images/universality/TMEncodingQuiz.png
   :alt: TMEncodingQuiz

   *Quiz:* Encode a set of TM transitions.

Simulation
~~~~~~~~~~

.. figure:: images/universality/TMInterpretation1.png
   :alt: TMInterpretation1

   Phase 1: the UTM reads the encoded description and sets up its tapes.

.. figure:: images/universality/TMInterpretation2.png
   :alt: TMInterpretation2

   Phase 2: the UTM matches the current (state, symbol) pair against encoded transitions
   and executes the corresponding step.

Recognisability vs. Decidability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/universality/RecognizeVsDecide.png
   :alt: RecognizeVsDecide

   Recognising: accept members, may loop on non-members.
   Deciding: accept members, *reject* non-members — always halts.

.. figure:: images/universality/RecognizabilityVsDecidability.png
   :alt: RecognizabilityVsDecidability

   Relationship diagram: every decidable language is recognisable.

**Theorem:** A language is decidable :math:`\iff` both it and its complement are recognisable.

*Proof idea — alternating machines:* Run two recognisers (one for :math:`L`, one for
:math:`\overline{L}`) in lock-step. Since every string belongs to exactly one, one
recogniser must eventually accept.

.. figure:: images/universality/AlternatingMachineCode.png
   :alt: AlternatingMachineCode

   Pseudocode for the alternating-machines decider.

.. figure:: images/universality/TwoRecognizersQuiz.png
   :alt: TwoRecognizersQuiz

   *Quiz:* Which languages are recognisable / decidable given two recognisers?

Dovetailing
~~~~~~~~~~~

.. figure:: images/universality/DovetailingEmpty.png
   :alt: DovetailingEmpty

   Empty dovetailing grid — rows are strings, columns are computation steps.

.. figure:: images/universality/DovetailingFull.png
   :alt: DovetailingFull

   Diagonal traversal ensures every cell is eventually reached — used to recognise
   :math:`\{\langle M \rangle \mid L(M) \neq \emptyset\}`.

Recognisability Quizzes
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/universality/CountingStatesQuiz.png
   :alt: CountingStatesQuiz

   *Quiz:* Is :math:`\{\langle M \rangle \mid M \text{ has } \leq 10 \text{ states}\}` decidable?

.. figure:: images/universality/Halt34Quiz.png
   :alt: Halt34Quiz

   *Quiz:* Is :math:`\{\langle M \rangle \mid M \text{ halts on } 34\}` recognisable?

.. figure:: images/universality/AcceptsNothingQuiz.png
   :alt: AcceptsNothingQuiz

   *Quiz:* Is :math:`\{\langle M \rangle \mid L(M) = \emptyset\}` recognisable?

.. figure:: images/universality/AlwaysHaltingQuiz.png
   :alt: AlwaysHaltingQuiz

   *Quiz:* Is :math:`\{\langle M \rangle \mid M \text{ halts on every input}\}` decidable?

----

Part 5: Undecidability
-----------------------

Diagonalization
~~~~~~~~~~~~~~~

.. figure:: images/undecidability/AdjectiveTable.png
   :alt: AdjectiveTable

   Diagonalization via English adjectives — the "heterological" paradox.

.. figure:: images/undecidability/HeterologicalTable.png
   :alt: HeterologicalTable

   The diagonal entry for "heterological" forces a contradiction.

.. figure:: images/undecidability/TMTable.png
   :alt: TMTable

   TM acceptance table — rows are machines :math:`M_i`, columns are encodings
   :math:`\langle M_j \rangle`.

.. figure:: images/undecidability/TMDiagonalization.png
   :alt: TMDiagonalization

   Flipping the diagonal shows that no machine :math:`M_L` can recognise
   :math:`L = \{\langle M \rangle \mid \langle M \rangle \notin L(M)\}`.

.. figure:: images/undecidability/DumaflacheQuiz.png
   :alt: DumaflacheQuiz

   *Quiz:* Does diagonalisation apply to other computational models?

Mapping Reductions
~~~~~~~~~~~~~~~~~~

.. math::

   A \leq_m B \;\iff\; \exists \text{ computable } f : w \in A \iff f(w) \in B

.. figure:: images/undecidability/MappingReducibility.png
   :alt: MappingReducibility

.. figure:: images/undecidability/ReductionConsequences.png
   :alt: ReductionConsequences

   If :math:`A \leq_m B` then: :math:`B` decidable :math:`\Rightarrow` :math:`A`
   decidable; :math:`A` undecidable :math:`\Rightarrow` :math:`B` undecidable.

.. figure:: images/undecidability/ConsequencesQuiz.png
   :alt: ConsequencesQuiz

   *Quiz:* Apply reduction consequences.

.. figure:: images/undecidability/SimpleReductionForm.png
   :alt: SimpleReductionForm

   Template: reduction from :math:`D_{TM}` to show a new language :math:`B` is undecidable.

.. figure:: images/undecidability/SimpleReductionProof.png
   :alt: SimpleReductionProof

.. figure:: images/undecidability/WhichReductions.png
   :alt: WhichReductions

   *Quiz:* Identify valid reduction directions.

The Halting Problem
~~~~~~~~~~~~~~~~~~~~

.. math::

   H_{TM} = \{ \langle M \rangle \mid M \text{ halts on } \varepsilon \}

.. figure:: images/undecidability/HaltingProblem.png
   :alt: HaltingProblem

   Reduction :math:`D_{TM} \leq_m H_{TM}`: given :math:`\langle M \rangle`, build
   :math:`N` that ignores its input and runs :math:`M` on :math:`\langle M \rangle`.
   A decider for :math:`H_{TM}` would decide :math:`D_{TM}` — contradiction.

.. figure:: images/undecidability/Filtering.png
   :alt: Filtering

   Filtering technique: reduction machines that conditionally simulate another machine.

----

Decidability Hierarchy Summary
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Category
     - Example
     - Status
   * - Decidable
     - String equality :math:`\{w\#w\}`
     - TM always halts with correct answer
   * - Recognisable (undecidable)
     - Halting problem :math:`H_{TM}`
     - TM accepts "Yes" instances; may loop on "No"
   * - Unrecognisable
     - Diagonal language :math:`L`
     - No TM can even semi-decide it

----

Key Formulas and Definitions
------------------------------

**Countability:**

.. math::

   |\Sigma^*| = \aleph_0, \qquad |\mathcal{P}(\Sigma^*)| = 2^{\aleph_0} > \aleph_0

**TM transition function:**

.. math::

   \delta : Q \times \Gamma \to Q \times \Gamma \times \{L, R\}

**Mapping reduction:**

.. math::

   A \leq_m B \;\Longleftrightarrow\; \exists \text{ computable } f,\; w \in A \iff f(w) \in B

**Decidability iff complement recognisable:**

.. math::

   L \text{ decidable} \iff L \text{ recognisable} \land \overline{L} \text{ recognisable}

**Diagonal language (unrecognisable):**

.. math::

   L = \{ \langle M \rangle \mid \langle M \rangle \notin L(M) \}

**Halting problem (undecidable, recognisable):**

.. math::

   H_{TM} = \{ \langle M \rangle \mid M \text{ halts on } \varepsilon \}
