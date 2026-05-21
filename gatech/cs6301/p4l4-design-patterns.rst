.. title: P4L4 Design Patterns 
.. slug: P4L4 Design Patterns 
.. date: 2016-05-28 00:00:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P4L4 Design Patterns
====================

A **design pattern** is a reusable solution to a recurring design problem in context. Patterns capture design experience — the problem, solution, tradeoffs, applicability, and implementation options.

Origins and the Gang of Four
-----------------------------

- Christopher Alexander's *A Pattern Language* (1970s) — architectural building patterns (e.g., the atrium)
- **Gang of Four (GoF)** — Gamma, Helm, Johnson, Vlissides — *Design Patterns* (1995)
- GoF spawned analysis patterns, language-specific catalogs, and anti-pattern books

GoF Pattern Documentation Structure
-------------------------------------

Each pattern is documented with:

- **Intent** — summary of value provided
- **Motivation** — scenario demonstrating the problem
- **Applicability** — context/conditions where the pattern applies
- **Structure** — UML class/object/sequence diagrams
- **Participants** — roles of each class
- **Collaborations** — how participants interact
- **Consequences** — advantages and disadvantages/tradeoffs
- **Implementation** — choices, alternatives, pitfalls
- **Sample Code** — coded examples
- **Known Uses** — real systems using the pattern
- **Related Patterns** — patterns often used together (pattern density)

Pattern Categories
-------------------

GoF organizes 23 patterns into three categories:

- **Creational** — object construction mechanisms
- **Structural** — class/object composition and organization
- **Behavioral** — complex object interactions and algorithms

Creational Patterns
~~~~~~~~~~~~~~~~~~~~

- **Singleton** — ensure exactly one instance; global access point
- **Prototype** — clone existing objects instead of class-based instantiation
- **Builder** — separate construction of a complex object from its representation
- **Factory Method** — let subclasses decide which class to instantiate
- **Abstract Factory** — create families of related objects without specifying concrete classes (e.g., UI toolkit look-and-feel)

Structural Patterns
~~~~~~~~~~~~~~~~~~~~

- **Composite** — represent whole-part hierarchies; treat leaves and composites uniformly
- **Adapter** — convert one interface to another expected by clients
- **Bridge** — decouple abstraction from implementation
- **Decorator** — add responsibilities to an object dynamically
- **Facade** — provide a simplified interface to a subsystem
- **Flyweight** — share fine-grained objects to reduce memory (e.g., character objects in text processing)
- **Proxy** — control access to an object

Behavioral Patterns
~~~~~~~~~~~~~~~~~~~~

- **Chain of Responsibility** — decouple sender from handler; allow multiple handlers
- **Command** — encapsulate a request as an object
- **Interpreter** — represent a grammar and interpret sentences
- **Iterator** — sequential access to collection elements without exposing structure
- **Mediator** — encapsulate object interactions in a mediator object
- **Memento** — capture/restore object state (undo/redo)
- **Observer (Listener)** — notify dependents when an object changes
- **State** — change behavior when internal state changes (simulate class change at runtime)
- **Strategy** — family of interchangeable algorithms with the same interface
- **Template Method** — skeleton algorithm with hook methods for specific steps
- **Visitor** — apply operations to elements of a structure without modifying their classes

Composite Pattern (Structural, Detail)
----------------------------------------

**Problem:** Representing whole-part hierarchies where clients treat individual objects and compositions uniformly.

**Structure:**

- **Component** — abstract interface (operations, add/remove/getChild)
- **Leaf** — terminal elements with no children
- **Composite** — contains children (other Components); aggregation back to Component allows arbitrary depth
- **Client** — interacts only through the Component interface

**Consequences:**

- Simplifies client code (uniform treatment of leaves and composites)
- Possible safety cost: moving add/remove to Component makes the interface uniform but allows meaningless operations on leaves

**Implementation issues:**

- Parent pointers? (referential integrity cost)
- Shared children across composites? (reduces objects but increases complexity)
- Where to place child management (add/remove)? Higher = more uniform but less safe
- Data structure for children (array, hash, linked list)?
- Cascading delete (filled diamond = composition in UML)?

**Example:** Inventory management — Component=InventoryItem, Leaf=StainlessSteelHexBolt, Composite=BlueBirdBoxKit, Client=OutOfStockDetector

Singleton Pattern (Creational, Detail)
----------------------------------------

**Intent:** Ensure a class has exactly one instance; provide a global access point.

**Structure:** Single class with a static ``uniqueInstance`` attribute and a class-level ``getInstance()`` method. Constructor is private/protected.

**Implementation:**

1. Define a class (static) variable to hold the instance
2. ``getInstance()`` checks if instance exists; creates it if not
3. Make constructor private/protected to prevent external instantiation

**Consequences:**

- Controlled access (avoids global variable problems)
- Can be subclassed for flexibility
- Can generalize to exactly-N instances

**Implementation issues:**

- Global state in disguise (can compromise modularity)
- Thread safety — multiple threads may create duplicate instances (use synchronization or eager initialization)
- Eager vs. lazy construction
- Semantic questions: "at most one" vs. "exactly one"? "One ever" vs. "one at a time"?
- **Testing problem:** Singletons make unit test isolation difficult (tests share state within a single process)

Visitor Pattern (Behavioral, Detail)
--------------------------------------

**Intent:** Vary operations on elements of a complex structure without modifying the element classes.

**Motivation:** AST in a compiler — same tree, different operations (code generation, pretty-printing, type checking). Decouple structure from operations.

**Applicability:** Use when multiple unrelated operations needed on a stable structure; operations change frequently but element types do not.

**Participants:**

- **Visitor** (abstract) — declares ``visit(ConcreteElementX)`` for each element type
- **ConcreteVisitor** — implements operations for each element; may accumulate state
- **Element** (abstract) — declares ``accept(Visitor)``
- **ConcreteElement** — implements ``accept`` by calling ``visitor.visit(this)``
- **ObjectStructure** — the collection/tree; enumerates elements

**Behavior (double dispatch):**

1. ObjectStructure sends ``accept(visitor)`` to each element
2. ConcreteElement calls ``visitor.visit(this)`` — dispatches based on both element type and visitor type
3. Visitor operation can call back into the element's public interface

**Consequences:**

- Adds new operations easily (new ConcreteVisitor)
- Groups related operations in one class
- Breaks encapsulation (operations separated from data)
- Adding new element types is costly (must update all visitors)
- Can accumulate state during traversal

**Implementation issues:**

- Double dispatch (operation depends on both element and visitor types)
- Traversal responsibility: ObjectStructure, Visitor, or separate Iterator?

Problems with Patterns
-----------------------

1. **Added complexity** — extra objects and indirection levels
2. **Object schizophrenia (self problem)** — splitting functionality across delegated objects complicates debugging
3. **Preplanning problem** — patterns are most useful when anticipated early; retrofitting requires refactoring
4. **Traceability problem** — pattern usage invisible in code without explicit naming conventions and documentation; increases fragmentation risk

Summary
--------

Design patterns are essential vocabulary for developers. They are difficult to learn passively — hands-on experience is required for patterns to become instinctive. Despite costs (complexity, preplanning, traceability), the design leverage they provide makes them indispensable.
