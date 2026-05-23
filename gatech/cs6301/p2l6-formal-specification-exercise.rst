Formal Specification Exercise
=============================

Formal Specification
--------------------

Specifications describe what a program is supposed to do. They may come from customers, end users, or an analyst team, expressed informally in text, in structured documents, or using formal mathematical notation. This lesson focuses on precise specification using mathematical notations.

Two notations are used:

- **First-Order Logic (FOL)** / Predicate Calculus — enables precise expression of propositions, combination via logical connectives (and, or, not), and quantification (∀, ∃)
- **OCL** (Object Constraint Language) — part of UML; provides FOL-equivalent syntax for annotating UML diagrams

The Specification Process
-------------------------

Mathematical specification proceeds in three stages:

1. **Signature** — name of the program, names and types of input arguments, name and type of the result
2. **Precondition** — assertion about the function's input arguments (what must be true for meaningful execution)
3. **Postcondition** — assertion about the output (how the result relates to the input)

SQRT Example
~~~~~~~~~~~~

**Signature**: ``Real y = SQRT(Real x)``

**Precondition**: ``x ≥ 0`` (defined over non-negative reals only)

**Postcondition**: ``y × y = x``

Notes on postconditions: For **pure functions**, output is completely determined by input. For **impure functions**, postconditions must also describe side effects (changes to global variables, I/O, changes to instance variables in OO contexts).

SORT Example
~~~~~~~~~~~~

**Signature**: ``Vector<int> y = SORT(Vector<int> x)``

**Precondition**: True (any vector of integers is valid input)

**Postcondition** has two parts:

1. The output is **ordered**
2. The output contains the **same elements** as the input (is a permutation)

Specifying ORDERED
------------------

**Signature**: ``Bool z = ORDERED(Vector<int> y)``

**Precondition**: True (even an empty vector is trivially ordered)

**Postcondition**: ``∀i (1 ≤ i < |y|) . y[i] ≤ y[i+1]``

For every index i from 1 up to (but not including) the length of y, the element at position i must be less than or equal to the element at position i+1. Using ``< |y|`` avoids indexing past the end.

**RORDERED** (reverse/descending order) is identical except: ``y[i] ≥ y[i+1]``

Specifying Permutation
----------------------

To express "same elements as," we use the well-defined mathematical concept of **permutation**.

**Signature**: ``Bool z = PERMUTATION(Vector<int> x, Vector<int> y)``

**Precondition**: ``|x| = |y|`` (vectors must have equal length)

**Postcondition** — three cases (recursive definition):

**Case 1 — Empty vectors**: If ``|x| = 0``, then x is a permutation of y (base case).

**Case 2 — First elements match**: If ``|x| > 0`` and ``x[1] = y[1]``, then x is a permutation of y if ``tail(x)`` is a permutation of ``tail(y)`` (where tail = everything except the first element).

**Case 3 — First elements differ**: If ``x[1] ≠ y[1]``, then:

- There exists some position j (where ``1 < j ≤ |y|``) such that ``y[j] = x[1]``
- x is a permutation of y if ``tail(x)`` is a permutation of ``y[1..j-1] ^ y[j+1..|y|]`` (concatenation of the segments of y excluding position j)

This recursive definition is well-founded because each recursive call operates on shorter vectors, and the base case (empty vectors) is handled.

The ``^`` symbol denotes **concatenation** of two vectors.

OCL Version of ORDERED
-----------------------

The same ORDERED specification in OCL syntax:

- Uses ``|`` for separating the quantifier variable from the proposition (instead of the dot in FOL)
- Limitations on the variable's value are separated from the main proposition by the ``implies`` keyword
- Uses OCL's built-in ``Sequence`` class instead of vectors

Takeaway
--------

Formal specification languages (FOL, OCL) with accompanying tools enable precise expression of system functionality. Although writing specifications requires careful thought about exactly what you want to say, the effort saves significant rework from misunderstood requirements. Industrial-strength tools exist for many formal specification languages.
