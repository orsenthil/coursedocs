P1L6: Top Down Parsing: LL Parsing
==================================


LL(1) Parsing
-------------

* Top down parsers.
* They push the start symbol on to the stack.
* Replace non-terminal symbol on stack using grammar rules.
* If top of stack matches input token, both are to be discarded, mismatch is a syntax error.


Simple Example
--------------

* Demonstration of Parsing


LL(1) Parser
------------

Parse Table
-----------


Table Construction
------------------

How to construct the parsing table if grammar is complex?



First Set Algorithm
-------------------

**Real World Example**

::

    stmt -> if-stmt | other
    if-stmt -> if (exp) stmt else part
    else-part -> else stmt | e
    exp -> 0 | 1

::

   First(stmt) = {other} U First(if-stmt) = {other, if}
   First(if-stmt) = {if}
   First(else-part) = {else, :math:`\epsilon`}
   First(exp) = {0, 1}


First Set Example
-----------------


::

  E -> 
  T -> 
  X -> e, +
  Y -> e, *
  int -> 
  * ->  *
  + ->  +
  ) ->  )
  ( ->  (


First Set Quiz 2
----------------

::

   E  -> a, b, e, *, +
   E' -> e, +
   T  -> a, b, e, *
   T' -> e, *
   F  -> a, b


Follow Sets
-----------

Follow sets of A is those symbols which will follow after A and is used to
determined if a rule such as A -> e should be invoked to remove the A to expose
the tokens that follow A for matching them.

Follow Sets Part 3
------------------

**Grammar**

::


  stmt -> if-stmt | other
  if-stmt -> if (exp) stmt else-part
  else-part -> else stmt | :math:`\epsilon`
  exp -> 0 | 1


* Follow(exp) = { ) }
* Follow(else-part) =  Follow(if-stmt) = Follow(stmt)
* Follow(stmt) = {$} U First(else-part) - {:math:`\epsilon`} U Follow(if-stmt) = {$, else}


Follow Set Quiz
---------------


Given the following grammar, determine the follow sets:


S -> ABCDE
A -> a | :math:`\epsilon`
B -> b | :math:`\epsilon`
C -> c
D -> d | :math:`\epsilon`
E -> e | :math:`\epsilon`

