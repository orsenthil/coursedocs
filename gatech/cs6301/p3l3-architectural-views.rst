.. title: Architectural Views
.. slug: Architectural Views
.. date: 2016-05-27 23:50:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Architectural Views
===================


Introduction
------------

Architecture is not simply a picture — it is a **set of design decisions**. Multiple graphical and textual notations called **views** are used to convey different aspects of those decisions, just as building architects use sketches and blueprints.

Software architecture specifies the components that together compute a solution while satisfying non-functional constraints. This lesson covers **Kruchten's 4+1 views** plus additional useful views: feature, non-functional, bug reporting, context, and utility views.


Kruchten's 4+1 Views
---------------------

Logical View
~~~~~~~~~~~~~

Conveys the **structural breakdown** of computational, communicational, and behavioral responsibilities.

**Notations:**

- **Box-and-arrow diagrams** — familiar, single-slide overview; but imprecise (arrow semantics undefined)
- **UML class model diagrams** — structural decomposition
- **Interaction overview / collaboration diagrams** — behavioral aspects
- **ADL components and connectors** — formal architectural elements

Development View
~~~~~~~~~~~~~~~~

Concerned with **source code** organization.

**Units:** packages, classes, subsystems, libraries, files.

**Notations:**

- **UML package diagrams** — imports, sub-component, merge relationships between packages
- **UML component diagrams** — components with dependency arrows showing "uses/calls upon" relationships
- **UML class diagrams** — generalization, association, dependency relationships
- Source control system module structure

Process View
~~~~~~~~~~~~

Shows **concurrently executing processes or threads** and how execution is divided among them.

**Primary notation:** UML deployment diagram — shows concurrent components and their communication.

Physical View
~~~~~~~~~~~~~

Shows how processes are **allocated to execution units** (physical hardware).

**Notations:**

- **UML deployment diagrams**
- **UML sequence diagrams** — columns = objects (possibly on separate processors); vertical axis = time; horizontal lines = messages. Useful for showing coordination of processes handling transactions.
- **Collaboration diagrams** — same content as sequence diagrams but laid out spatially with numbered messages showing order.

Use Case View (+1)
~~~~~~~~~~~~~~~~~~

Important execution sequences from the **external actor's/user's point of view**.

**Notations:**

- **UML use case diagrams** — ovals (use cases), stick figures (actors), labeled lines (include, extend, generalize). Conveys a *set* of use cases, not individual ones.
- **Sequence/activity diagrams** — for individual use cases
- **Structured text** — tabular format with columns for Actor, Action, and Object


Context View
------------

From OMT's functional view (not in UML). Uses **data flow diagrams (DFDs)** to convey system activities and their ordering. DFDs can be nested; the outermost is the **context diagram**:

- **Single oval** = the system as a whole
- **Rectangles** = external actors (users or external systems)
- **Lines** = data flows between actors and system

**Example:** Chess-playing program — one actor (human opponent), three flows: submit moves, receive moves, view board diagram.


Individual Use Cases
--------------------

A use case is a **story** illustrating a specific interaction between a user and system. Can be expressed as:

- **Narrative text** — unstructured prose
- **Structured table** — three columns: Actor, Action, Object (what is used/produced)


Feature View
------------

A **feature** is a conceptual unit of system behavior from the user's perspective — typically an optional capability (may require extra cost).

**Feature diagrams** model the set of possible features for a product family:

- **Root** = the concept/product (e.g., Car)
- **Children** = features and sub-features
- **Filled circle** at branch end = **required** feature
- **Open circle** = **optional** feature
- **Open arc** between siblings = **exclusive-or** (choose one)
- **Filled arc** = **inclusive-or** (can combine, e.g., hybrid engine)
- **Inter-feature constraints** can express dependencies (e.g., "pulls trailer" requires automatic transmission)

**Example — Car feature diagram:**

- Body (required, no sub-features)
- Transmission (required): Automatic XOR Manual
- Engine (required): Electric, Gasoline, or Hybrid (inclusive-or → 3 options)
- Pulls Trailer (optional)
- Total configurations: 1 × 2 × 3 × 2 = **12**

**Validity check:** A configuration must include all required features, respect XOR constraints, and not omit mandatory sub-trees (e.g., a car without an engine is invalid).


Non-Functional View
-------------------

Architecture must address non-functional requirements, which often involve **trade-offs**. Express using tabular text linking:

- The non-functional requirement (e.g., performance)
- The technique used to address it (e.g., caching)

**Example:** A web browser's core function is displaying web pages, yet its code is dominated by **cache management** (page caches, connection caches, image caches) — all driven by performance requirements. Other critical NFRs for a browser include **security** (online transactions), **extensibility** (plugins), and **portability** (cross-platform).


Bug Reporting View
------------------

Bug tracking tools contain fields for which **component** a bug relates to and which **feature** was in use. These should correspond to architectural components and feature model elements to avoid confusion and enable traceability.


Utility Views
-------------

Miscellaneous supporting information about system structure not covered by other views, conveyed in tabular text:

- Installation scripts
- Log file analysis tools
- Build files (Makefiles, configuration)
- Documentation
- Project manifests (delivery package structure)
- Supporting tools


Conclusion
----------

There is no single tangible artifact called "the architecture." An architecture is a **set of decisions** conveyed through multiple views — graphical and textual — whose sum communicates the architecture. Select appropriate views based on system complexity, application domain, and the audience that will read them.
