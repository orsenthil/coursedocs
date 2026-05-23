UML Class Models
================


Overview
--------

The **UML Class Model Diagram** (also called the Static Structure Diagram) is the most popular and most complex UML diagram type. It is a structure diagram used to model classes, interfaces, objects, relationships, and their properties. Not all features need to be used at once — start abstract and refine over time.


Classes
-------

A **class** is a description of a similar set of instances. Candidates include domain objects, roles, events, and interactions. In UML, a class is a rectangle horizontally partitioned into compartments:

- **Name compartment** (required)
- **Attributes compartment** (optional)
- **Operations compartment** (optional)
- Additional compartments for responsibilities, exceptions, etc. (optional)

Name Compartment
~~~~~~~~~~~~~~~~

Contains the class name (a noun, capitalized by convention). Additional features:

- **Abstract class** — indicated by *italics* on the name or an ``{abstract}`` tag. Abstract classes define contracts for subclasses and cannot be instantiated directly. Useful for factoring common features of related subclasses.
- **Stereotypes** — extend UML (shown in ``<<double angle brackets>>``)
- **Properties** — expressed in ``{curly braces}``

Attributes Compartment
~~~~~~~~~~~~~~~~~~~~~~

Each attribute can specify:

- **Visibility**: ``+`` public, ``-`` private, ``#`` protected, ``~`` package
- **Name** (required)
- **Type** (UML built-in types)
- **Multiplicity and ordering**
- **Initial value** (optional)
- **Derived** — computed rather than stored (indicated by ``/`` prefix)
- **Properties** — e.g., ``{frozen}`` means the value cannot change

Operations Compartment
~~~~~~~~~~~~~~~~~~~~~~

Each operation can specify:

- **Visibility** (same symbols as attributes)
- **Name** (required)
- **Return type**
- **Parameter list**: name, type, default value, direction (``in``, ``out``, ``inout``)
- **Properties**: ``{query}`` (read-only), concurrency properties, ``{abstract}``, class scope (underlined name — operates on the class, not an instance)

Example: A class-scoped operation could return the total count of instantiated objects, since no single instance can answer questions about other instances.


Advanced Class Features
-----------------------

- **Interfaces** — describe what a class provides to and requires from the rest of the system (as in Java interfaces)
- **Parameterized classes** — correspond to Java generics or C++ templates (e.g., a ``Set<Vehicle>``)
- **Nested classes** — classes defined within other classes (Java inner classes)
- **Composite objects** — objects containing other objects, depicted as class rectangles nested within class rectangles


Relationships
-------------

Three kinds of relationships in UML class model diagrams:

- **Association** — e.g., "people drive vehicles" (solid line)
- **Generalization** — e.g., "a car is a kind of vehicle" (solid line with triangle)
- **Dependency** — e.g., "cars depend on pollution laws" (dashed line with arrowhead)


Associations
------------

Denoted by solid lines connecting class rectangles. Notational affordances:

- **Name** — a label on the line (e.g., "Contains")
- **Reading direction** — a filled triangle indicating left-to-right or right-to-left reading
- **Navigability** — arrowhead(s) on the line indicating primary access direction
- **Multiplicity** — e.g., ``*`` (any number), ``3..*`` (three or more), ``1`` (exactly one)
- **Role names** — labels at each end describing the role a class plays in the association
- **Properties** — e.g., ``{ordered}``, ``{frozen}``, ``{addOnly}``
- **Qualifiers** — small rectangles on class edges containing a key attribute (like a database key)
- **N-ary associations** — associations involving more than two classes, depicted with a rhombus

Association Classes
~~~~~~~~~~~~~~~~~~~

An association that has class properties (attributes, operations). Depicted by a dashed line from the association line to a class rectangle.

Example: A "Job" association class between Company and Person, with a ``salary`` attribute. Salary is a property of neither the person nor the company alone, but of their association.

**Recursive associations** (a class associated with itself) should use role names — e.g., a Job that manages another Job has roles "boss" and "worker".

Links
~~~~~

Just as classes have instances, associations have **links**. Example: "IBM hires Bob" and "IBM hires Alice" are two links of the same "hires" association.


Aggregation and Composition
----------------------------

Both are special kinds of association indicating containment:

- **Aggregation** (open diamond) — a "has-a" relationship with independent lifetimes. Example: a room has a table; destroying the room need not destroy the table.
- **Composition** (filled diamond) — a stronger "has-a" with lifetime dependency. Destroying the whole destroys the parts. A part belongs to only one composition. Composition is transitive (house → rooms → closets).

Examples:

==============================  =================
Pair                            Relationship
==============================  =================
Courses and Students            Aggregation
Persons and Spouses             Association
Bank Accounts and Patrons       Aggregation
Fonts and Glyphs                Composition
==============================  =================


Generalization
--------------

Indicated by a solid line ending in an open triangle pointing to the superclass. All instances of the subclass are also instances of the superclass (subset relationship).

**Generalization ≠ inheritance.** Generalization is a modeling concept; inheritance is an implementation technique.

UML supports:

- **Multiple parent classes** and **multiple child classes**
- **Discriminators** — names for groups of subclasses (e.g., "power" → wind/motor; "venue" → land/water)

Subclass constraints (expressed in ``{curly braces}``):

- **Overlapping** vs. **disjoint** — can an instance belong to multiple sibling subclasses?
- **Complete** vs. **incomplete** — do the subclasses cover all possible instances of the parent?

Example: Athletes → {BaseballPlayer, FootballPlayer, BasketballPlayer} are **overlapping** (Deion Sanders) and **incomplete** (many other sports exist). Books → {Paperback, ComicBook, Hardbound} are **disjoint** and **incomplete**.

Superclass/subclass subtlety
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Omnivores vs. Vegetarians: Vegetarians are the **superclass** because generalization requires that subclass instances have all parent properties. Omnivores have an additional property (eating meat) that vegetarians lack, making omnivores the subclass.


Key Takeaway
------------

UML class model diagrams offer a rich vocabulary for modeling system structure. Each notational affordance implies a question to be answered about the system: What is the multiplicity? Are values ordered? What is the qualifier? One of modeling's key benefits is that it forces you to confront these questions early, before they become costly surprises.
