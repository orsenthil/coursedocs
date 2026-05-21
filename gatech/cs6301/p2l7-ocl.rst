.. title: P2L7 OCL 
.. slug: P2L7 OCL 
.. date: 2016-05-27 23:44:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P2L7 OCL
========

Overview
--------

The **Object Constraint Language (OCL)** is a part of UML that provides precise specification of functional details that diagrams alone cannot express. It is declarative (not procedural), strongly typed, and describes values rather than activities — a pure expression language with no assignment statements.

OCL has one key concept: a **constraint** — a formal assertion of system properties.

Three main elements:

1. **Constraints** (invariants, pre/postconditions)
2. **Collection classes** (Set, Bag, Sequence)
3. **Navigation** (walking through class diagrams)

Tool support: Rational Rose, ArgoUML, Eclipse, Poseidon, Enterprise Architect, and others.

Why OCL
-------

UML diagrams describe structural relationships well but lack precision about functional details. OCL extends UML with:

- **Class invariants** — properties always true for a class
- **Pre/postconditions** — precise descriptions of operations
- **Guards** on state chart transitions

Uses of OCL
------------

- Specify invariants on classes in class model diagrams
- Describe pre/postconditions on operations
- Specify derivation rules for derived attributes
- Describe guards on statechart transitions
- Specify targets for messages and actions
- Specify type invariants for stereotypes
- Use as a query language over class model instances

Syntax
------

OCL has a single statement form::

    context <identifier>
    <constraint-kind>: <boolean-expression>

- **context** — names the class or operation in the UML diagram
- **constraint-kind** — one of: ``inv`` (invariant), ``pre`` (precondition), ``post`` (postcondition)
- **boolean-expression** — the actual constraint

OCL constraints are inherently connected to UML class model diagrams.

Invariants
----------

An **invariant** (keyword ``inv``) is a property that is always true — an essential relationship among object values in the system. Equivalent to integrity constraints in relational databases.

Example::

    context LargeCompany
    inv: numberOfEmployees > 50

Pre and Postconditions
----------------------

Used to specify what it means to invoke an operation:

- **pre** — circumstances under which the operation may execute
- **post** — what must be true after execution (relationship of return value to input parameters, and/or effects on instance variables)

Example — square root::

    context Real::squareRoot(): Real
    pre: self >= 0
    post: self = result * result

The ``result`` keyword refers to the return value of the operation.

Attribute Changes and @pre
--------------------------

Since OCL uses ``=`` for equality (not assignment), expressing state changes requires the ``@pre`` suffix to denote the value *before* the operation executed.

Example — bank deposit::

    context Account::deposit(amount: Real)
    pre: amount > 0
    post: balance = balance@pre + amount

Example — swap operation::

    context MyClass::swap()
    post: a = b@pre and b = a@pre

Built-in Types and Operations
-----------------------------

- **Boolean** — and, or, xor, not, implies
- **Integer** / **Real** — arithmetic operations (+, -, \*, /)
- **String** — toUpper, concat, size, substring

Keywords
--------

``inv``, ``pre``, ``post``, ``if-then-else-endif``, ``and``, ``or``, ``xor``, ``not``, ``implies``, ``context``, ``let``, ``in``, ``def``, ``derive``, ``init``, ``result``, ``self``, ``package``, ``endpackage``

Let Clause
~~~~~~~~~~

Introduces a local abbreviation to avoid repeating complex expressions::

    context Person
    inv: let income = self.jobs->collect(salary)->sum()
         in if isUnemployed then income < 100
            else income >= 100 endif

Navigation
----------

OCL uses dot notation to traverse class diagram relationships from the context class. Each step adds a period and the name of the next class or association.

Example (context: Customer)::

    self.order.date

- ``self`` = the context class (Customer)
- ``order`` = adjacent class via association
- ``date`` = attribute of Order

When navigation crosses a multiplicity boundary (1-to-many, many-to-many), the result is a **collection**. Operations on collections use the arrow notation ``->``::

    self.order.check.bankID->size()

Collections
-----------

Four built-in collection types:

- **Collection** — abstract parent class with shared operations: ``size()``, ``count()``, ``sum()``, ``includes()``, ``isEmpty()``, iteration operators
- **Set** — unordered, no duplicates
- **Bag** — unordered, allows duplicates
- **Sequence** — ordered, allows duplicates

Each subtype may have additional specialized operations (see OCL reference manual).

Other Features
--------------

- **Tuples** — struct/record-like compound values
- **Enumerations** — as in Java
- **Messages** — expressing UML messages
- **UML metamodel access**
- **Automatic flattening** — a set of sets becomes a single set; eliminates need for nested access syntax
