Short search questions
======================

.. role:: underline
   :class: underline


1) Briefly describe the advantage of depth-first search has over breadth-first search in terms of resource usage.

Space Complexity of Depth First Search

.. math::

    O(|V|)


This is same as breadth-first in terms of resource usage.

For practical applications, the graph tends to be very large and search is done on limited depth. In such cases,
depth first search uses that limited depth (resource) where as for the breadth-first search at the same depth uses
more resource.

At a particular depth, breadth-first search by design has to keep track of all the nodes at the depth, and thus has
to keep track of more resources.

----


2) A breadth-first search can have advantages over a plain depth-first search,
despite the issue of resource usage. Briefly describe two such possible advantages.


XKCD answers this really well.

.. image:: https://d1b10bmlvqabco.cloudfront.net/attach/ix489xx12sl36q/i4le4lw9o4v752/izvkjpffqatt/dfs.png
   :align: center
   :height: 300
   :width: 450



A breadth-first search makes a lot of sense for dating in general, actually; it suggests dating a bunch of people casually before getting serious, rather than having a series of five-year relationships one after the other.

https://xkcd.com/761/

**Translating to technical terms.**

1) BFS always gives you a path (alternatively when DFS is still looking for next node to evaluate and going in circles).
2) At any given stage, BFS gives an optimal towards to the goal to evaluate.

----


3) A heuristic function for A* is considered admissible if

a) it can over estimate the cost to the goal

b) if and only if it always over estimates or precisely predicts the cost to the goal

:underline:`c) if and only if it never over estimates the cost to the goal`

d) it produces a value between 1 and 0, inclusive

----

4) If the heuristic function of the A* search assigns zero to every state s such that (h(s) = 0) then A* becomes:

(a) Informed Search
(b) Iterative Deepening Depth First Search
(c) Depth First Search
:underline:`(d) Uniform Cost Search`
(e) None of the Above


----

5) Given the way we defined search, is it OK to negative path lengths?


- Yes. We take into account only nodes and not path for visit.

- We will not go in circles.


----

6) Can we have negative path lengths if graph is directed and acyclic?

- Yes. We can.


----


7) What happens to A* if we use negative heuristic values?

-  Nothing. It is an admissible heuristic and it can work.




