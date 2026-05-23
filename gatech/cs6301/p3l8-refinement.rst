Refinement
==========


Complexity and Abstraction
--------------------------

The primary weapon against complexity is **abstraction** — hiding details to concentrate on the big picture. This lesson addresses managing complexity by carefully **refining** a design from an abstract version into an implementation.

Abstraction implies thinking at **different levels**. For abstraction to help solve a design problem, work done at a lower level must **contribute to** the solution at the higher level.


Decomposition
-------------

Horizontal Decomposition
~~~~~~~~~~~~~~~~~~~~~~~~~~

At any one level of abstraction, carve out pieces and fit them together. This is **horizontal decomposition**.

Vertical Decomposition
~~~~~~~~~~~~~~~~~~~~~~~

For each piece at one level, solve a whole sub-problem at a lower level. This lower level is a **refinement** of the upper level. Devising lower-level solutions and ensuring they satisfy upper-level needs is **vertical decomposition**.


Three Properties of Proper Refinement
--------------------------------------

All non-trivial design involves refinement across multiple levels. Three properties must hold:

1. **Property 1**: The top level faithfully represents the requirements
2. **Property 2**: Each level is internally consistent
3. **Property 3**: Each lower level faithfully represents the level above it


Property 1 — Requirements Satisfaction
----------------------------------------

The specification must satisfy its requirements. Verified using traditional methods: software testing, group reviews, customer acceptance criteria.


Notation
--------

First-order logic notation used throughout:

- **Abstract operations**: P₁, P₂, ..., Pₙ (Pᵢ = typical abstract operation)
- **Abstract states**: S = set of abstract states; s = typical element; s' = state after an operation
- **Concrete operations**: Q₁, Q₂, ..., Qₙ
- **Concrete states**: T = set of concrete states; t = typical element; t' = state after
- **Invariants**: invA (abstract), invC (concrete)
- **Pre/post-conditions**: Pre-Pᵢ(s, args), Post-Pᵢ(s, args, s', result)
- **Retrieve function**: retr(t) = s — maps concrete states to abstract states (many-to-one)
- **Symbols**: & = and, → = implies


Property 2 — Internal Consistency
-----------------------------------

Each level must be internally consistent: **operations preserve invariants**.

Formally, for each operation Pᵢ:

    invA(s) ∧ Pre-Pᵢ(s) ∧ Post-Pᵢ(s, s') → invA(s')

If the invariant was true before and the operation runs correctly, the invariant remains true afterward.

**Implication for developers**: when implementing a spec (even in one step), you must ensure each operation doesn't break any invariant — via testing, code reviews, or proof.


Property 3 — Faithful Representation
--------------------------------------

The most involved property. Three criteria must be checked:

Criterion 1: Adequacy
~~~~~~~~~~~~~~~~~~~~~~

The refinement must be **rich enough** to represent all abstract situations. For each abstract state satisfying the abstract invariant, there must exist a corresponding concrete state satisfying the concrete invariant, such that the retrieve function maps the concrete state back to the abstract state.

Formally:

    ∀s ∈ S: invA(s) → ∃t ∈ T: invC(t) ∧ retr(t) = s

Criterion 2: Totality
~~~~~~~~~~~~~~~~~~~~~~

The implementation cannot reach a concrete state with **no corresponding abstract state** (no "memory fault core dump" situations). The retrieve function must be total.

Formally:

    ∀t ∈ T: invC(t) → ∃s ∈ S: retr(t) = s ∧ invA(s)

Criterion 3: Modeling (Inputs and Outputs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each concrete operation must faithfully reflect its abstract specification.

**Inputs** — refinements can **weaken** preconditions (accept more inputs), but must accept at least everything the abstract spec requires:

    ∀t ∈ T: invC(t) ∧ Pre-Pᵢ(retr(t), args) → Pre-Qᵢ(t, args)

**Outputs** — the concrete operation's results and side effects must satisfy the abstract postcondition. The implementation can do more, but must do at least what the spec requires:

    ∀t ∈ T: invC(t) ∧ Pre-Qᵢ(t, args) ∧ Post-Qᵢ(t, args, t', result) → Post-Pᵢ(retr(t), args, retr(t'), result)


Bank Account Example
--------------------

Abstract specification:

- **Class**: Account
- **Attribute**: ``transactions : Sequence(Integer)`` — history of deposits (positive) and withdrawals (negative)
- **Operations**:

  - ``deposit(a: Integer)`` — pre: a > 0; post: transactions = transactions\@pre->append(a)
  - ``withdraw(a: Integer)`` — pre: a > 0 ∧ transactions->sum() ≥ a; post: transactions = transactions\@pre->append(-a)
  - ``balance() : Integer`` — post: result = transactions->sum()

- **Init**: transactions = empty sequence
- **No abstract invariant**

Refinement — adding ``runningTotal``:

- **New attribute**: ``runningTotal : Integer``
- **Invariant**: ``runningTotal = transactions->sum()``
- Updated operations:

  - ``deposit(a)`` — additionally: ``runningTotal = runningTotal@pre + a``
  - ``withdraw(a)`` — additionally: ``runningTotal = runningTotal@pre - a``
  - ``balance()`` — simply returns ``runningTotal`` (no summation needed)

- **Init**: ``runningTotal = 0``

Checking the properties:

- **Adequacy**: for any abstract state (transaction sequence), the corresponding concrete state adds the computed running total
- **Totality**: strip the running total to recover the abstract state
- **Consistency (Property 2)**: balance doesn't modify state; deposit and withdrawal maintain the invariant by inductive argument (the invariant is initially true and each operation preserves it)
- **Inputs**: only withdrawal is affected (has a precondition)
- **Outputs**: all three operations are affected (all concrete postconditions reference ``runningTotal``)


Summary
-------

Design mistakes are costly; abstraction and refinement are our chief weapons against complexity. Refinements must guarantee:

1. Top-level specification matches requirements
2. Operations at each level preserve invariants
3. Each refinement is **adequate** (covers all abstract states)
4. Each refinement is **total** (no unreachable abstract states)
5. Concrete pre/post-conditions **model** their abstract counterparts
