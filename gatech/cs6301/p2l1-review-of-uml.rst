.. title: P2L1 Review of UML 
.. slug: P2L1 Review of UML 
.. date: 2016-05-27 23:37:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P2L1 Review of UML
==================


History and Origins
-------------------

Diagrams have been part of software development since flowcharts. In the 1980s, object-oriented diagramming techniques emerged, including **OMT** (Object Modeling Technique), developed by James Rumbaugh at GE. OMT combined three views:

- **Class model** — structural aspects
- **State chart** — behavioral aspects
- **Data flow diagram** — functional aspects

The push to unify competing OO methods led to **UML** (Unified Modeling Language), standardized by the **Object Management Group (OMG)**. UML's three principal architects were Rumbaugh, Grady Booch, and Ivar Jacobson. UML diagrams serve both analysis (modeling the problem) and design (modeling the solution).


Diagram Types Overview
----------------------

UML 2 defines **14 diagram types** in two categories. No single project uses all of them — choose diagrams that illuminate the trickiest parts of your system.

- **Structural diagrams** — describe the system's static pieces and their relationships
- **Behavioral diagrams** — describe system executions (a single behavioral diagram may capture only one scenario)

Diagrams are valuable for communication (teammates, other teams, future maintainers), supporting development processes, enabling tool-based validation, and structuring design reviews. The trade-off: diagrams must be kept up to date.


Structural Diagrams
-------------------

Class Model Diagram
~~~~~~~~~~~~~~~~~~~

The most popular UML diagram. Shows classes and their relationships, with many possible adornments. Also called the static model or class structure diagram.

UML classes have up to three compartments:

- **Top** — class name
- **Middle** — attributes (instance variables)
- **Bottom** — methods/operations

Three main relationship types:

- **Dependency** (dashed line with arrowhead) — one class uses another
- **Association** (solid line, no arrowhead) — one class has/affects another; can be adorned with a diamond for aggregation
- **Generalization** (solid line with triangle) — one class is a kind of another

Object Diagram
~~~~~~~~~~~~~~

Same as a class model diagram but shows **instances** instead of classes. Labels are underlined with the format ``instanceName : ClassName``. Attribute fields contain specific values for that instance.

Composite Structure Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shows the internal structure of a class, emphasizing its interfaces:

- **Provides interface** (circle icon) — capabilities offered to the outside
- **Requires interface** (semicircle icon) — capabilities needed from the outside

Classes plug together by connecting provides to requires interfaces — a way to compose software architectures.

Component Diagram
~~~~~~~~~~~~~~~~~

A static implementation view of how components fit together. A **component** is a physical, replaceable system part that packages implementation and conforms to a set of interfaces. Used to model code entities (binaries, libraries). Components are depicted as rectangles with two sub-rectangles on their side. Can also convey architecture.

Deployment Diagram
~~~~~~~~~~~~~~~~~~

Shows configuration of runtime processing units and their component instances. **Nodes** correspond to computational devices; **arcs** indicate communication channels.

Package Diagram
~~~~~~~~~~~~~~~

General-purpose organizing mechanism providing namespace scoping (like Java packages). Depicted with a tabbed rectangle. Dependency arrows between packages abstract inter-element dependencies to the package level.

Profile Diagram
~~~~~~~~~~~~~~~

Used to extend the UML metamodel with new stereotypes, tag values, and constraints. Stereotypes appear in double angle brackets (e.g., ``<<metaclass>>``).


Behavioral Diagrams
-------------------

Use Case Diagram
~~~~~~~~~~~~~~~~

Shows system functionality provided to external actors. A **use case** is a sequence of user-visible actions and system responses — a story of a particular interaction.

- **Stick figures** — external actors (users, other systems, devices)
- **Ovals** — use cases
- **Lines** — participation (actor involved in use case)
- **Annotations** — ``<<extends>>`` (adding contingencies to a story) and ``<<uses>>`` (shared sub-behavior, like a subroutine)

Individual use cases can be expressed as unstructured text narratives or in tabular form (columns: actor, action, objects involved).

Context Diagram
~~~~~~~~~~~~~~~

A top-level dataflow diagram: a single oval (the system), rectangles (actors), and lines (data flows between them).

Sequence Diagram
~~~~~~~~~~~~~~~~

Conveys a single use case. **Columns** represent participants (usually objects), **time flows downward**, and **horizontal lines** indicate messages between objects. Evolved from telephony's message sequence charts. Semantically equivalent to communication diagrams.

Communication Diagram
~~~~~~~~~~~~~~~~~~~~~

Alternative view of a use case — looks like a class model diagram with rectangles (objects) and lines (communication instances). Lines are annotated with **numbered message indicators** showing execution order (e.g., 1, 2, 2.1, 2.2, 3).

Activity Diagram
~~~~~~~~~~~~~~~~

A variant of a state machine where **multiple states may be simultaneously active** (concurrent threads). Derived from Petri nets. Transitions are triggered by activity completion rather than external events. Used for workflows, process synchronization, and concurrency.

Key elements: start node (filled circle), states, diamonds (decision/merge points), heavy bars (synchronization/fork/join points), and end node.

Interaction Overview Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A kind of activity diagram where nodes correspond to lower-level interaction diagrams (sequence, communication, timing, etc.). ``ref`` denotes a specific interaction occurrence.

Timing Diagram
~~~~~~~~~~~~~~

Similar to digital chip timing diagrams. Time flows left to right; arrows indicate synchronization points. Used when specific timing constraints must be modeled.

State Diagram (State Chart)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most powerful and complex behavioral diagram. Extends finite state machines with aggregation, concurrency, history, and event broadcasting. States can contain sub-state machines separated by dashed lines, running concurrently. Transitions between states are triggered by events/stimuli.


Object Constraint Language (OCL)
--------------------------------

A textual extension to UML's visual notation for more precise specification. Used as annotations on class model and state chart diagrams. Combines first-order predicate logic, diagram navigation, and collection classes (sets, bags, sequences).

Example: An ``Account`` class with a ``deposit(amount: Real)`` operation can have:

- **Precondition** (``pre``): ``amount > 0``
- **Postcondition** (``post``): ``balance = balance@pre + amount``


UML Metamodel
-------------

The **UML metamodel** is UML described in terms of UML — a UML class model diagram of the UML language itself. Designers can extend the metamodel using **UML profiles**, adding stereotypes, tag values, and constraints on the diagrams themselves.

The more precisely you understand a problem, the fewer subsequent problems you will encounter in the system's lifetime.
