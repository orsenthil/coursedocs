Lectures from youtube
=====================

Elimination of left recursion and left factoring the grammars

Tool for grammars — see grammar statistics resource in the lessons page.

Grammars

* Does followset follow the left-recursive grammar?
* Does parseTable follow the left-recursive grammar?

Note that the way that you deal with left recursion in an LL grammar is essentially by converting to right recursion
and then post-processing the parse tree to turn it back into left recursion. Breaking it down, you convert to

* Only Left Factoring needs to be handled. No Left Recursion.

::

    S    -> A
          |B
          |C
          |D
          |F.
    A     -> a t
           | a u
          | a v
          | .

    B   ->b
          |.

     C -> c
          |.

    D   -> d
          |.
     F -> f
          | .

First and Follow sets are needed for parse tables. There are a couple ways to check if
a grammar is an LL(1) grammar, a unique parse table is one way. And not all grammars
are LL(1) grammars, so if your input grammar is not LL(1) parsable you cannot proceed.

This shows the example that I should use left factored production.

Improvements
------------

* First set need to give references to non-terminals.

Test 1
------

::

    RHYME -> SOUND PLACE
          | PING.
    SOUND -> ding dong.
    PLACE -> dell.
    PING -> pong.

Test 2
------

::

    S   -> A B C D F.
    A  -> a |.
    B  -> b |.
    C  -> c.
    D  -> d|.
    F  -> f|.

Test 3
------

.. code-block:: guess

    S     -> A B C D F.
    A     -> a t | a u | a v |.
    B     -> b |.
    C     -> c.
    D     -> d |.
    F     -> f |.

Recursive Descent Parsers
-------------------------

-----------------------------------------------

* Operator Grammar.

Operator Grammar.

::

    E -> E + E | E * E | id

* There should not be two variables that are adjacent.
* Operation Relation Table.
* It is a bottom up parsing.

In order to decrease the size of the operator precedence table, we go for operator function table.

* Error detecting capability of function table is going to be lesser than Error detecting capability of relation table.

LR parsing, LR(0) items and LR(0) parsing table
-----------------------------------------------

* Canonical collection of LR(1) items.

::

    S -> AA
    A -> aA | b

LL(0) Parsing example and SLR(1) table
--------------------------------------

* LR(0)
* SLR(1)

Examples of LR(0) and SLR(1)
----------------------------

::

    S -> dA | aB
    A -> bA | C
    B -> bB | C

Figure out if the grammar is

i) LL(1)
ii) LR(0)
iii) SLR(1)

Examples of LR(0) and SLR(1)
----------------------------

--------------------------

--------------------------------------------

---------------------------------------------------------------------

---------------------------

----------------------------------------

-----------------------------------------
