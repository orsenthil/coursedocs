Lectures from youtube
=====================


Elimination of left recursion and left factoring the grammars

* https://www.youtube.com/watch?v=3_VCoBfrt9c


Tool for grammars

* http://smlweb.cpsc.ucalgary.ca/start.html

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


S     -> A B C D F.
A     -> a t | a u | a v |.
B     -> b |.
C     -> c.
D     -> d |.
F     -> f |.
