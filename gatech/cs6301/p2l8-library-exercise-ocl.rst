Library Exercise (OCL)
======================

Purpose
-------

The UML class model diagram from the earlier library exercise could not express all aspects of the requirements. OCL fills in the gaps — expressing numeric constraints, operation semantics, and derived data that diagrams alone cannot capture.

The class model has: Patron, Loanable Item, Title, and associations for Request and CheckedOut.

Of the 11 original requirements, only two (2 and 9) are fully expressed by the diagram alone. The rest require OCL specification.

Invariants
----------

**Requirement 6** — "Books are checked out for three weeks unless they are currently bestsellers, in which case the limit is two weeks."

Determining the constraint:

1. **Context**: Book (the first noun in the requirement)
2. **Constraint kind**: Invariant (a property always true of the class, not tied to a specific operation)
3. **Expression**::

    context Book
    inv: if bestSeller then checkOutPeriod = 2
         else checkOutPeriod = 3 endif

Unqualified names (``bestSeller``, ``checkOutPeriod``) are interpreted as attributes of the context class. To refer to attributes of other classes, use qualified names with dot notation.

**Requirement 7** — "AV material may be checked out for two weeks."

::

    context AudioVisualMaterial
    inv: checkOutPeriod = 2

No conditional needed — only one possibility.

Query Operations
----------------

Query operations return values without changing state (pure functions) and typically have no preconditions.

**Requirement 3** — "The library may need to calculate the items a patron has currently checked out."

::

    context Patron::itemsCurrentlyCheckedOut(): Set(LoanableItem)
    post: result = self.checkedOut.LoanableItem

The compound name ``checkedOut.LoanableItem`` navigates from Patron through the CheckedOut association to reach the set of associated LoanableItems.

**Requirement 4** — Children (age ≤ 12) may check out no more than 5 items.

::

    context Patron
    inv: age <= 12 implies
         checkedOut.LoanableItem->size() <= 5

Key features:

- ``implies`` — logical implication; restriction applies only to children
- ``->size()`` — the arrow operator invokes the ``size()`` collection operation on the result of navigation (which returns a collection due to multiplicity)

Operations with Side Effects
----------------------------

Operations that change state (impure functions) are more complex to specify than queries.

**Requirement 5** — "A patron can check out books or audio visual materials."

Context and signature::

    context Patron::checkOut(item: LoanableItem)

**Preconditions** (all must hold):

1. The item must be available (``item.isAvailable()``)
2. The item must not have been requested by someone else (``not item.isRequested()``)
3. Age restriction: if patron is a child, cannot exceed 5 items

These can be expressed as three separate preconditions or one precondition with ``and`` connectives. Helper operations like ``isAvailable`` and ``isRequested`` can be invented and specified separately (divide and conquer).

**Postconditions** express the state change — a new link is created in the CheckedOut association between the patron and the item.

Derived Data
------------

Derived attributes are computed rather than stored. OCL uses the ``derive`` keyword.

**Patron's age** — changes daily; computed from birthday::

    context Patron::age: Integer
    derive: OperatingSystem.getDate() - self.birthday

**Fine amount** — computed from due date and return date (number of overdue days × rate).

Note: type consistency matters — subtraction on dates must yield a value compatible with how age/fines are used elsewhere in the system.

Missing Pieces
--------------

A complete OCL specification of this library system would additionally require:

- Specifications for requirements 1, 3, 8, 10, 11
- Non-functional requirements
- Auxiliary operations (``isAvailable`` is itself complex)
- Operations implicit in requirements: returning items, paying fines, cancelling requests
- New issues: if one copy of a title is a bestseller, should all copies be?
- Specifications for Date and Money utility class operations
- Constructors for LoanableItem and Patron instances

Observations
------------

- Multiple valid OCL formulations may exist for the same requirement
- The specification process often reveals new requirements, ambiguities, or outright mistakes — requiring customer consultation
- Even a simple set of requirements has many subtle issues, illustrating the value of the careful thinking that formal specification demands
