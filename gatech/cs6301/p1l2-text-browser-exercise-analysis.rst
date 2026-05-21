.. title: P1L2 Text Browser Exercise (Analysis) 
.. slug: P1L2 Text Browser Exercise (Analysis) 
.. date: 2016-05-27 23:35:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P1L2 Text Browser Exercise (Analysis)
=====================================


Problem Statement
-----------------

Design a text browser application — a widget for browsing text in a file — assuming no GUI toolkit provides one directly. The goal is a cleanly structured solution built from atomic GUI components.


Components
----------

Three structural components are needed:

- **ViewPort** — Displays textual content graphically. Assumptions: displays an integer number of lines (1–100), all text in the same font and point size.
- **ScrollBar** — A vertical scroll bar with a movable **handle** in a **tray**. The handle position denotes the file position to display (top = start, bottom = end). The handle size relative to the tray denotes the proportion of the file currently visible.
- **FileManager** — Supplies text from disk. Assumptions: entire file cannot be held in memory; line-oriented access is available; retrieves a limited-length consecutive sequence of lines on request.


Use Cases
---------

Three primary use cases:

1. User moves the scroll bar handle
2. User resizes the viewport
3. System displays the appropriate file content in response


Analysis Model
--------------

A **UML class-model diagram** expresses the analysis. Each class rectangle has three compartments: name (top), attributes (middle), and operations (bottom). Lines between rectangles denote relationships.

**Operations** (derived from use cases):

- ``ViewPort.resize(size: Integer): void`` — resizes the viewport
- ``ScrollBar.moveHandle(position: Integer): void`` — moves the scroll bar handle

UML types are used rather than language-specific types. Constraints not expressible in the diagram notation (e.g., viewport size must be between 1 and 100) are handled via **OCL**.

**Attributes (Percepts)** — visible properties the user can observe:

- ViewPort: ``height`` (number of visible lines), ``contents`` (displayed text)
- ScrollBar: ``handlePosition``, ``handleSize``
- FileManager: ``document`` (sequence of lines) — interacts with the external operating system actor


Relationships
-------------

Relationships among components are the hardest part of analysis. UML analysis models use three types: **associations**, **aggregations**, and **generalizations**.

LinesVisible Association
~~~~~~~~~~~~~~~~~~~~~~~~

The number of lines displayed equals ``min(fileSize, viewportSize)``. This dependency between ViewPort and FileManager forms the **LinesVisible** association, expressed in OCL as an invariant.

Displays Association
~~~~~~~~~~~~~~~~~~~~

The scroll bar handle position determines *which* lines are shown. The percentage down the tray corresponds to the percentage down the file, establishing the first visible line. Combined with the line count, this determines the full displayed content.

This is a **ternary association** (three-way) among ViewPort, FileManager, and ScrollBar — depicted in UML using a diamond connecting all three classes. The OCL specifies the mathematical relationship.

HandleProportion Association
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The handle size relative to the tray indicates the portion of the document visible in the viewport: ``handleSize / traySize = viewportSize / documentSize``. This is another **ternary association** with its own OCL constraint.


Modeling Benefits
-----------------

The modeling process forces consideration of subtle design questions that might otherwise be overlooked — for example, whether resizing the viewport should preserve the top visible line or the scroll bar position. This early analysis prepares the ground for design, where the key question becomes how the components will communicate and coordinate.
