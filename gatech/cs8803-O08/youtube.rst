Lectures from youtube
=====================


Elimination of left recursion and left factoring the grammars

https://www.youtube.com/watch?v=3_VCoBfrt9c


Tool for grammars

http://smlweb.cpsc.ucalgary.ca/start.html

Grammars

http://faculty.ycp.edu/~dhovemey/fall2010/cs340/lecture/lecture9.html


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

https://web.stanford.edu/class/cs143/lectures/lecture07.pdf


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

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/SH5F-rwWEog?list=PLEbnTDJUr_IcPtUXFy2b1sGRPsLFMghhS" frameborder="0" allowfullscreen></iframe>

::

    E -> i E'
    E' -> + iE' | e

* Top down parser.

::

    E()
    {
        if (l == 'i')
        {
            match('i');
            E'();
        }
    }

    l = getchar();

Other function.

::

    E'()
    {
    if ( l == '+')
    {
        match('+');
        match('i');
        E'();
    }
    else
    return;
    }

function match.

::

    match(char t) {
    if (l == t) {
        l = getchar();
    else
        printf("error");
    }

main program.

::

    main()
    {
        E();
        if( l == "$")
            printf("parsing success");
    }


Operator grammar and Operator precedence parser
-----------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/n5UWAaw_byw" frameborder="0" allowfullscreen></iframe>

* Operator Precedence Parser.
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

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/APJ_Eh60Qwo" frameborder="0" allowfullscreen></iframe>

* Canonical collection of LR(0) items.
* Canonical collection of LR(1) items.

::

    S -> AA
    A -> aA | b


LL(0) Parsing example and SLR(1) table
--------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/0kiTNN2kHyY" frameborder="0" allowfullscreen></iframe>


::

    S' -> S
    S -> AA1
    A -> aA | b


* Accepting state.
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


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/5s4CWn6GiwY" frameborder="0" allowfullscreen></iframe>

::

    E -> E + T | T
    T -> T F | F
    F -> F * | a | b


CLR(1) and LALR(1) Parsers
--------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/VSkfnRfNuwI" frameborder="0" allowfullscreen></iframe>


* LR (1) Item = LR(0) items + look ahead.

Conflicts and Examples of CLR(1) and LALR(1)
--------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Nxj0g1mk5Ak" frameborder="0" allowfullscreen></iframe>


Examples of CLR(1) and LALR(1) and and comparision of all the parsers
---------------------------------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/1XD2wk52-Cs" frameborder="0" allowfullscreen></iframe>


Syntax Directed Translation
---------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/queUceGJqh0" frameborder="0" allowfullscreen></iframe>

Example of SDT - involving a calculation
----------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/fmRgKPLEROg" frameborder="0" allowfullscreen></iframe>

S attributed and L attributed definitions
-----------------------------------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/rdnAJBoFKOw" frameborder="0" allowfullscreen></iframe>
