Course Lessons
==============

Slide PDFs for all lessons are in the course `Google Drive folder
<https://drive.google.com/drive/u/0/folders/1QCkexJoXsIev9KOC9opHVl8_o1AjkbIV>`_.


Lesson 1 — Introduction to Compilers
--------------------------------------

References
~~~~~~~~~~

* `Ratfor — first compiler <https://en.wikipedia.org/wiki/Ratfor>`_
* `Overview of lexing and parsing <http://savage.net.au/Ron/html/graphviz2.marpa/Lexing.and.Parsing.Overview.html>`_
* `Difference between lexer and parser <https://stackoverflow.com/a/3614928/18852>`_


Lesson 2 — Regular Expressions and DFA
--------------------------------------

Resources
~~~~~~~~~

* http://expressions.wingtiplabs.com/game — Regex Game
* http://www.txt2re.com/ — text to regex generator
* http://regexr.com/ — build and test regular expressions
* https://regexcrossword.com/ — Regex Crossword


Lesson 3 — Regex NFA
--------------------


Lesson 4 — CFGs and Ambiguity
-----------------------------


Lesson 5 — Recursive Descent Parser
-----------------------------------


Lesson 6 — Top Down Parsing: LL Parsing
---------------------------------------

LL(1) Parsing
~~~~~~~~~~~~~

* Top-down parsers push the start symbol onto the stack.
* Replace non-terminal on stack using grammar rules.
* If top of stack matches input token, discard both; mismatch is a syntax error.

First Set Algorithm
~~~~~~~~~~~~~~~~~~~

Example grammar::

    stmt -> if-stmt | other
    if-stmt -> if (exp) stmt else part
    else-part -> else stmt | e
    exp -> 0 | 1

::

    First(stmt) = {other} ∪ First(if-stmt) = {other, if}
    First(if-stmt) = {if}
    First(else-part) = {else, ε}
    First(exp) = {0, 1}

Follow Sets
~~~~~~~~~~~

Follow(A) = symbols that can appear after A; used to decide when to apply A → ε.

Example::

    stmt -> if-stmt | other
    if-stmt -> if (exp) stmt else-part
    else-part -> else stmt | ε
    exp -> 0 | 1

* Follow(exp) = { ) }
* Follow(else-part) = Follow(if-stmt) = Follow(stmt)
* Follow(stmt) = {$} ∪ First(else-part) − {ε} ∪ Follow(if-stmt) = {$, else}

Follow-set quiz grammar:

.. math::

    S -> ABCDE \\
    A -> a | \epsilon \\
    B -> b | \epsilon \\
    C -> c \\
    D -> d | \epsilon \\
    E -> e | \epsilon

Resources
~~~~~~~~~

* http://smlweb.cpsc.ucalgary.ca/start.html — grammar statistics
* http://jflap.org/ — JFLAP formal languages toolkit


Lesson 7 — Semantic Analysis
----------------------------

Topics: attribute grammars, inherited vs synthesized attributes, circularity, evaluation methods.

Video: https://www.youtube.com/watch?v=queUceGJqh0


Lesson 8 — IR Code Generation
-----------------------------

Topics: IR types, three-address code, lowering, short-circuiting, arrays, loops, function calls, code shape.


Lesson 9 — Control Flow Graphs
------------------------------

Topics: basic blocks, partitioning algorithm, control flow graphs, multigraphs.


Lesson 10 — Liveness Analysis
-----------------------------

Topics: compiler back end, information flow, live variable analysis, def-use chains, systems of equations.


Lesson 11 — Register Allocation
-------------------------------

Topics: interference graphs, graph coloring, spill costs, web splitting, register coalescing, interprocedural allocation.


Lesson 12 — Code Optimizations
------------------------------

Topics: redundancy elimination, local value numbering, super-local value numbering, SSA name space.


Lesson 13 — Instruction Selection
---------------------------------

Topics: ISA idioms, tree tiling, dynamic programming, rewrite rules, code generator generators.

* Idioms are cheaper than their constituent parts.


Lesson 14 — Procedure Abstraction
---------------------------------

Topics: variable scope, storage management, data areas, local name translation, blocks, variable-length data.
