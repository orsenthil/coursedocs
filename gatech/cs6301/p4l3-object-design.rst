Object Design
=============

Object-Oriented Design (OOD) bridges the gap between analysis models (UML diagrams, OCL constraints, non-functional requirements) and a target implementation in an OO language.

Intermodel Consistency
-----------------------

Before design begins, verify consistency across analysis artifacts:

- Use case names must match their sequence/collaboration diagram representations
- StateChart events, actions, and activities must correspond to class methods
- Data conditions in StateCharts must reference attributes present in the class model

From Analysis to Design
------------------------

Key differences between OOA and OOD diagrams — four UML elements lack direct OO language equivalents:

1. **Associations** — must choose an implementation strategy
2. **Aggregation** — must select language features to represent part-whole relationships
3. **Invariants** — must be enforced programmatically
4. **StateCharts** — OO languages lack native state machines

Three guidelines for transitioning:

- Treat the entire system as an object; all program objects are its attributes
- Decide how to handle associations and invariants
- Expect to introduce additional classes beyond those in the analysis model

System Design Considerations
-----------------------------

- **Architecture** — choose style based on non-functional requirements
- **Concurrency** — spectrum from single process to one thread per object
- **Physical design** — allocate tasks to processors, handle peripherals
- **Data management** — database vs. files, locking, protocols
- **Control regime** — reactive (GUI-driven) vs. proactive (system-driven)
- **Error handling** — recovery techniques, error reporting strategies

Abstraction Mechanisms
-----------------------

Levels of reusable design vocabulary (from low to high):

- **Programming idioms** — memorized code snippets for specific tasks
- **Library classes** — pre-built classes from system libraries
- **Design patterns** — cataloged solutions to recurring design problems
- **Aspects** — mechanisms for cross-cutting concerns
- **Frameworks** — reusable patterns of cooperating classes
- **Architectural styles** — high-level structural approaches

Collaboration-Based Design
----------------------------

An alternative to noun-based OOA:

1. Start with use cases (user stories/scenarios)
2. Each actor plays a specific **role** in each use case
3. A role = the actions an actor performs in one use case
4. Combine all roles an actor plays across use cases → defines the class's full interface

Also called **role-based design**. Classes are synthesized from the union of their roles.

Sources for Methods
--------------------

Methods come from:

- Operations in the analysis model
- Signals, actions, activities, events from behavior models (StateCharts)
- Standard infrastructure methods: constructors, destructors, getters/setters, copy constructors, toString/print, selectors, iterators

New Classes in Design
----------------------

Beyond analysis classes, additional classes arise for:

- **Implementing relationships** — associations have no direct language support
- **Intermediate results** — storing reusable computed values
- **Abstraction** — abstract parent classes for maintainability

OOD preserves **traceability** from real-world objects → analysis classes → design classes → code.

Implementing Generalization
----------------------------

**Generalization vs. Inheritance:**

- Generalization: all instances of child are also instances of parent (semantic relationship)
- Inheritance: messages to child may be delegated to parent (implementation mechanism)

**Rules for safe inheritance (overriding):**

- Child methods must accept all arguments the parent accepts (contravariant inputs)
- Child methods must produce compatible results for the same inputs (covariant outputs)
- Children may add features but should not remove them

**Square/Rectangle example:** The parent-child relationship depends on class definitions — if Square is "a Rectangle with equal sides," Square is the child; if Square has one attribute (side) and Rectangle adds a second (width ≠ height), Rectangle is the child.

**Implementation techniques:**

- Strict inheritance following the rules above
- Single class with a type flag (discriminator)
- Java interfaces or enums
- **State pattern** — for cases where an object's "type" changes at runtime (e.g., a book changing loan duration category)
- Multiple inheritance (C++) — inherit selectively from multiple parents

Implementing Associations
--------------------------

OO languages lack native associations. Design factors:

- **Directionality** — unidirectional or bidirectional traversal?
- **Cardinality** — one-to-one, one-to-many, many-to-many?
- **Access patterns (CRUD)** — Create, Read, Update, Delete frequency
- **Invariant maintenance** — referential integrity constraints

**Strategies:**

+-------------------------------+-------------------------------------------+----------------------------+
| Approach                      | How                                       | Tradeoff                   |
+===============================+===========================================+============================+
| Pointer (1-way, 1:1)         | Attribute of target type                  | Simplest; one direction    |
+-------------------------------+-------------------------------------------+----------------------------+
| Vector of pointers (1-way, 1:N)| Collection attribute                    | One direction only         |
+-------------------------------+-------------------------------------------+----------------------------+
| Symmetric pointers (2-way)   | Pointers/vectors in both classes          | Referential integrity cost |
+-------------------------------+-------------------------------------------+----------------------------+
| One-way + search (2-way)     | Pointers in one direction, search reverse | Performance cost on search |
+-------------------------------+-------------------------------------------+----------------------------+
| Association class             | Reified pairs in a collection (hash/set)  | Extra traversal step       |
+-------------------------------+-------------------------------------------+----------------------------+

**Student-Course example tradeoffs:**

- Single reference in Student → student limited to one course
- Vector of Students in Course → hard to find courses for a student
- Association class → extra indirection step
- Symmetric vectors → general but referential integrity burden

Implementing Dependencies
---------------------------

Dependencies ("uses" relationships) can be implemented as:

- Attribute or global object of the target type
- Method parameter of the target type
- Method call or constructor call to the target
- Import of the target class/package

Implementing Control (StateCharts)
-----------------------------------

State = possible values of a class's attributes. Implementation approaches:

- **Ad hoc** — manually code state detection and transitions
- **Finite state libraries** — leverage existing implementations
- **Table-driven interpreter** — rows = (state, event) → action/next-state

Abstract Classes and Interfaces
--------------------------------

- **Abstract method** — signature only in parent; child must implement
- **Abstract class** — has at least one abstract method; cannot be instantiated directly; defines a contract for subclasses
- **Interface** (Java) — all methods abstract, no non-final attributes (e.g., ``Serializable``)

**OOA → Java mapping:**

- Generalization → subclassing
- Aggregation → Collection classes (ArrayList, Set, etc.)
- Invariants → methods and constructors (establish and maintain)
- States → enumerations (with optional behavior per instance)

Summary
--------

OOA determines much of the solution structure, but OOD must resolve how to implement UML elements (associations, state machines) that have no direct language equivalent. Tools like design patterns, architectural styles, and design guidelines help, but each situation requires evaluating tradeoffs before choosing a solution.
