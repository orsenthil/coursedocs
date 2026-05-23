Design Principles
=================

Design principles (also called heuristics or guidelines) are informal rules of thumb for producing high-quality OO designs. They complement architectural styles and design patterns as ways to learn from others' experience.

Foundational Concepts
----------------------

**Coupling** (Larry Constantine) — extent to which a module is independent from other modules. Goal: **low coupling** → easier maintenance.

**Cohesion** (Larry Constantine) — extent to which a module has a single purpose. Goal: **high cohesion** → better understandability and reuse.

**Orthogonality** (McGovern & Date) — extent to which system features can be varied independently. Benefits: more user options, clearer documentation, supports automatic generation.

**Information Hiding / Encapsulation** (David Parnas) — hide implementation details behind abstract interfaces. Reduces coupling. Note: inheritance can violate information hiding by exposing parent internals to children.

+---------------------------+-------------------------------+
| Concept                   | Key Benefit                   |
+===========================+===============================+
| Cohesion                  | Improves reusability          |
+---------------------------+-------------------------------+
| Orthogonality             | Enables maximum variability   |
+---------------------------+-------------------------------+
| Information Hiding        | Raises level of abstraction   |
+---------------------------+-------------------------------+
| Coupling (high)           | Requires more code reading    |
+---------------------------+-------------------------------+

Design Principles Catalog
--------------------------

Liskov Substitution Principle (LSP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Barbara Liskov* — Subclass instances must satisfy parent class contracts. If client code works with a parent instance, it must also work with any child instance.

**Implication:** Child classes must obey parent invariants, preconditions, and postconditions.

Law of Demeter
~~~~~~~~~~~~~~~

*Karl Lieberherr* — Limit what objects a method ``m`` of object ``o`` can reference:

- ``o`` itself
- Parameters of ``m``
- Objects created within ``m``
- Direct attributes of ``o``

**Implication:** Reduces coupling; may require extra wrapper classes.

Hollywood Principle (Inversion of Control)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Donald Wallace* — "Don't call us, we'll call you." In OO frameworks, calls should flow from framework to client classes, not the reverse (opposite of library usage).

Dependency Inversion Principle (DIP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Robert Martin* — High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Implication:** Layer by abstraction rather than by control/data access. Controlling policies live at the highest architectural level.

**Example:** Robot → iMotor ← Motor/FancyMotor. Robot depends on the interface, not concrete motor implementations.

Open-Closed Principle (OCP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Bertrand Meyer* — A class should be **open for extension** but **closed for modification**.

**Implication:** After release, enhance only via subclasses. Addresses the fragile base class problem.

Interface Segregation Principle (ISP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Robert Martin* — Clients should depend on focused interfaces to subsets of a large class's features, not on the entire class.

**Implication:** Break interfaces into small, use-case-specific pieces. Related to role-based design.

Reuse Principles
~~~~~~~~~~~~~~~~~

*Robert Martin:*

- **Release-Reuse Equivalency Principle** — Granule of reuse = granule of release. Release highly cohesive units (e.g., Java packages).
- **Common Reuse Principle** — Classes not reused together should not be grouped together.
- **Common Closure Principle** — Classes that change together should be released together.

Acyclic Dependency Principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Robert Martin* — Package dependencies must not form cycles.

**DSM test:** The Dependency Structure Matrix (Baldwin & Clark) should be permutable to lower-triangular form.

**Breaking cycles:**

- Extract shared dependency into a new module C; have both A and B depend on C
- Add an interface in B and have A implement it

Stable Dependency Principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Robert Martin* — Depend in the direction of stability (stability = hard to change = many dependents).

**Corollary — Stable Abstraction Principle:** Stable packages should be abstract (hard to change, easy to extend).

Bad Smells (Refactoring Principles)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Kent Beck & Martin Fowler* — Code situations suggestive of design problems: duplicate code, long classes, too many comments, etc. Each bad smell implies a "do not do this" design principle. Fowler's *Refactoring* book catalogs dozens.

Riel's Design Heuristics
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Arthur Riel* — Selected heuristics:

- Most methods should use most data members most of the time (else split the class)
- Check constraints in constructors, not method preconditions
- Factor commonality (data, behavior, interfaces) as high as possible in inheritance hierarchies
- Use inheritance only to model generalization, not to share implementation
- **Prefer composition over inheritance** (especially implementation inheritance)
- Never override a base method with a no-op (violates LSP)
- Do not change object state without going through its public interface
- Class should not depend on its users
- **Distribute intelligence horizontally** — avoid God classes/objects
- Distribute intelligence vertically down narrow, deep containment hierarchies

Single Choice Principle
~~~~~~~~~~~~~~~~~~~~~~~~

Replace case statements / else-if cascades with parallel factored subclasses. Choice-specific code belongs in subclass methods, not in conditional branches.

Transparency
~~~~~~~~~~~~~

Provide interfaces that let client code be written without concern for specific details (generalized from middleware transparency). Cost: extra design and testing work.

Intentionality
~~~~~~~~~~~~~~~

Design so that intent is manifest and localized in code. Minimize conceptual distance between problem and solution. Supports traceability, validation, and maintainability. Improved through cohesion and naming conventions.

Summary
--------

Design principles are abstract but serve as early-warning sensors for problematic designs. Familiarity with the catalog sensitizes you to issues as they arise, guiding you toward established solutions. They are guidelines, not rigid rules — apply judiciously based on context.
