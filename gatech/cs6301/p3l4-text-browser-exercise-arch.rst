.. title: Text Browser Exercise (Arch)
.. slug: Text Browser Exercise (Arch)
.. date: 2016-05-27 23:51:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Text Browser Exercise (Arch)
============================


Overview
--------

This lesson revisits the TextBrowser example from an **architectural design** perspective, demonstrating a systematic process for moving from analysis to architecture. The approach uses UML diagrams and OCL constraints to describe the system architecture (see Stirewalt & Rugaber paper).

**System components:**

- **Document** — source of textual data
- **FileManager** — file system interface to the document
- **ViewPort** — resizable window displaying lines of text
- **ScrollBar** — controlling device for selecting which lines appear (via a draggable handle)


Phase 0 — Preparation (Context Diagram)
----------------------------------------

**Goal:** Understand the system from the outside in — its relationship with its environment.

Construct a **context diagram** showing:

- **Single class:** TextBrowser
- **External actors:** User, Operating System (file system)
- **Events** (stimuli from actors):

  - Move scrollbar handle
  - Resize viewport window

- **Percepts** (system outputs visible to actors):

  - Viewport contents (displayed lines)
  - Viewport height
  - Handle size (proportional to visible portion of file)
  - Handle position in tray


Phase 1 — Decomposition
------------------------

**Goal:** Divide the system into components, allocate responsibilities, and specify guarantees using OCL.

**Starting point:** The analysis model provides candidate architectural components. Analysis **associations** must be translated into design **dependencies** (associations have no direct implementation in programming languages).

**Components from analysis:** ViewPort, ScrollBar, FileManager — with associations describing how they interact:

- A binary association for displaying contents
- Ternary associations for scrollbar-viewport-file coordination

**OCL constraints from analysis:**

Direct effect (postcondition) — move handle:
  After the user moves the handle, ``handlePosition`` equals the new position. Direct effects are simple — suitable for fast event handlers.

Direct effect (postcondition) — resize window:
  ``pre: newSize >= 0``; ``post: viewport.height = newSize``

Indirect effect (invariant) — display document:
  ``viewport.viewContents = document.subSequence(scrollbar.handlePosition, scrollbar.handlePosition + viewport.height - 1)``

  The visible contents are the subsequence of document lines starting at the scrollbar's handle position, continuing for ``height`` lines.


Phase 2 — Architectural Style Selection
----------------------------------------

**Goal:** Determine how components interact by selecting an architectural style.

**Chosen style:** Layered Implicit Invocation

- Components organized into **layers**
- Higher-level components **register interest** in lower-level events and are **called back** when events occur
- Lower layers handle external events, propagating status changes **upward**
- Upper layers receive notifications and prepare/present results
- Event announcement is made **without the source knowing the recipient** → reduced coupling

**Benefits:**

- **Improved reusability** — lower components don't depend on upper ones (portable to other applications)
- **Reduced complexity** — components know less about each other, easier to understand and maintain

**Costs:**

- **Increased overhead** — extra indirection from implicit invocation and callback mechanisms

Layer Assignment
~~~~~~~~~~~~~~~~

Both ViewPort and ScrollBar handle events *and* provide percepts, so neither can be purely "bottom" or "top." By convention, place the **ViewPort** (most central percept) at the top:

1. **Top:** ViewPort
2. **Middle:** ScrollBar
3. **Bottom:** FileManager

Dependencies replace the analysis associations as dashed UML lines between components.

OCL Updates
~~~~~~~~~~~

- **Component OCL** (event handler pre/postconditions) → unchanged
- **Association OCL** (invariants) → reassigned to appropriate layer components. The variable on the left-hand side of each constraint hints at which component should own it.

Three invariants to maintain:

1. **Handle scaling** — handle size proportional to viewport/document ratio
2. **Display document** — visible lines match file contents at handle position
3. **Line visibility** — visible lines correspond to viewport height


Phase 3 — Invariant Maintenance
--------------------------------

When an event occurs (e.g., user scrolls), it may **temporarily break invariants**. The system must re-establish them. This is the core architectural implementation challenge.

Three Strategies
~~~~~~~~~~~~~~~~

**Aggregated responsibility** — a single component (e.g., ViewPort) owns pointers to all others and orchestrates invariant restoration:

- ScrollBar change → ViewPort queries ScrollBar for new position → requests lines from FileManager → displays them
- All coordination logic is **centralized** in one component
- *Most centralized* strategy

**Distributed responsibility** — each component knows its dependents and delegates partial responsibility:

- ScrollBar receives event → determines new position → calls ViewPort with new position
- ViewPort realizes it needs new content → requests from FileManager → displays
- Knowledge of invariants is **spread across all three components**
- *Most decentralized* strategy

**Mediated responsibility** — a new **Mediator** object is introduced for each invariant:

- The Mediator knows both the independent component (event source) and dependent components
- Independent component alerts the Mediator when its state changes
- Mediator queries the source, coordinates with dependents, and restores the invariant
- **Mediator** is a design pattern; three invariants → three mediators
- Enables runtime flexibility (introducing/toggling invariants dynamically)

Trade-offs
~~~~~~~~~~

======================  =================================  ============================
Strategy                Advantage                          Disadvantage
======================  =================================  ============================
Aggregated              Single place to understand logic    Implementation can be complex
Distributed             Each piece is simple                Hard to debug (many parts)
Mediated                Clean separation per invariant      Extra objects/indirection
======================  =================================  ============================

The fundamental trade-off is between **locality** (understanding in one place) and **complexity** (concentration of logic).


Process Summary
---------------

**Phase 0 — Preparation:**

- Construct context diagram with single system class
- Identify external actors, events, and percepts
- Specify desired behaviors from use cases/scenarios

**Phase 1 — Componentization:**

- Decompose system into components (start from analysis model)
- Allocate responsibility for events and percepts
- Assign property guarantees (OCL constraints)

**Phase 2 — Architecture:**

- Choose architectural style (e.g., layered implicit invocation)
- Assign components to layers
- Determine inter-layer dependencies
- Update OCL (convert association constraints to component-owned constraints)
- Select invariant maintenance strategy
- Assign responsibility for maintaining each invariant


Conclusion
----------

This architectural design process yields a breakdown of system functionality into components with explicit responsibility for maintaining system invariants. The main open issue — addressing **non-functional requirements** — is covered in a later lesson.
