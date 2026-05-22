.. title: KWIC Exercise
.. slug: KWIC Exercise
.. date: 2016-05-27 23:47:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

KWIC Exercise
=============


Introduction
------------

This exercise, first described by David Parnas, asks you to design **four different architectures** for the same problem: producing a **Key Word in Context (KWIC) index**. It illustrates how architectural choices affect maintainability, performance, and resilience to change.


KWIC Index Definition
---------------------

A KWIC index system:

1. Accepts a sequence of **text lines** (e.g., titles) as input
2. Generates all **circular shifts** of each line — removing the first word and appending it to the end, repeated for each word
3. Outputs all circular shifts of all lines in **alphabetical order** by the key word

A line of *n* words produces *n* circular shifts (including the original). **Stop words** (e.g., "and", "of", "the") are typically excluded from indexing. Output is formatted so key words align in a column for easy scanning.

**Example:** "Gone With the Wind" produces shifts:

- **Gone** With the Wind
- With the Wind **Gone**
- the Wind Gone **With**
- Wind Gone With **the**


Four Architectural Solutions
----------------------------

Shared Data Decomposition
~~~~~~~~~~~~~~~~~~~~~~~~~

**Principle:** Decompose into components based on **functions they compute**; all components share access to common in-memory data structures.

**Components:**

- **Master Controller** ("System") — orchestrates the overall process
- **Input** — reads and parses lines into shared data structures (Lines, Words, Index)
- **Circular Shifter** — generates all circular shifts, stored in shared memory
- **Alphabetizer / Sorter** — sorts shifts alphabetically
- **Output** — writes the final result

**Communication:** Subroutine calls (solid arrows) for control flow; direct memory access (dashed arrows) for data.

**Characteristics:**

- (+) Simple, efficient — no function call overhead for data access
- (−) Fragile — any change to the shared data representation breaks all components

Pipe and Filter
~~~~~~~~~~~~~~~

**Principle:** Decompose into a linear chain of **independent filters** connected by pipes; each filter transforms its input stream and passes results to the next. No shared data storage.

**Pipeline:** Input → Circular Shifter → Alphabetizer → Output

**Characteristics:**

- (+) Intuitive; each filter is an independent, reusable unit
- (+) Easy to reorder or replace filters
- (−) Cannot support interactive use (batch-only, streaming model)
- (−) Not space-efficient — no persistent shared storage; data may be duplicated across filters

Abstract Data Type (ADT)
~~~~~~~~~~~~~~~~~~~~~~~~

**Principle:** Decompose based on **important data structures**; hide representations behind abstract interfaces with operations. Precursor to object-oriented design.

**Components:**

- **Lines** — ADT storing parsed input lines
- **Characters** — ADT for character-level access
- **Circular Shifts** — ADT with an operation to compute shifts (shifts as a data structure, not just a verb)
- **Alphabetized Shifts** — ADT for sorted results
- **Input / Output** — I/O components
- **Master Controller** — invokes other components

**Communication:** Need-to-know basis — Output queries Alphabetized Shifts, which queries Circular Shifts, which queries Lines.

**Characteristics:**

- (+) Excellent maintainability and reuse — hidden representations can change independently
- (+) Easy to add operations (e.g., deletion) to individual ADTs
- (−) Function call overhead through abstract interfaces may reduce performance

Implicit Invocation
~~~~~~~~~~~~~~~~~~~

**Principle:** Coordinate components via **registration-broadcast** (publish-subscribe). Clients register interest in state changes of servers; servers broadcast events without knowing client identities.

**Components:** Same as ADT, but interaction is event-driven:

- When data changes, the component **announces** the change
- All registered components are **called back** automatically
- Servers don't know client identities → loose coupling

**Characteristics:**

- (+) Maintainability — changing a component's representation only requires changes in one place
- (+) Facilitates reuse
- (−) Harder to reason about control flow and debug (implicit, not explicit invocation)
- (−) Performance overhead similar to ADT


Comparative Evaluation
----------------------

======================  ================  ===============  =============  ====================
Quality                 Shared Data       Pipe & Filter    ADT            Implicit Invocation
======================  ================  ===============  =============  ====================
**Performance**         Best (direct)     Moderate         Overhead       Overhead
**Maintainability**     Poor              Moderate         Excellent      Excellent
**Reusability**         Poor              Excellent        Good           Good
**Data change**         Worst (all break) Moderate         Good (hidden)  Good (hidden)
**Interactive delete**  Difficult         Very difficult   Easy (add op)  Easy
**Understandability**   Simple            Very intuitive   Clear          Harder to trace
======================  ================  ===============  =============  ====================


Resilience to Change
--------------------

Potential enhancements a customer might request:

- GUI interface for browsing the index
- Interactive search over sorted keywords
- Data persistence (add/remove titles without full reprocessing)
- Changed input formats (e.g., bibliographic databases)
- Reuse of components in other applications
- Algorithm changes (shift on read vs. shift after read, incremental sort)
- New functionality (stop word filtering, deletions)
- External storage (database on disk)
- Changed data representation (different in-memory library)

**Key insight:** The best architecture depends on which changes you anticipate:

- **Reusability** → Pipe and Filter (independent, pluggable filters)
- **Data representation change** → Shared Data is *worst* (shared assumptions break everything)
- **Interactive deletion** → ADT is *best* (just add a delete operation to the Line ADT)


Lessons
-------

- Multiple architectural styles can solve the same design problem
- Each style has distinct advantages and disadvantages
- Choose the style whose strengths match your system's most important requirements and anticipated evolution
