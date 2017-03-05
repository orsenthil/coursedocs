Short search questions
======================

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

**c) if and only if it never over estimates the cost to the goal**

d) it produces a value between 1 and 0, inclusive

----

4) If the heuristic function of the A* search assigns zero to every state s such that (h(s) = 0) then A* becomes:

(a) Informed Search

(b) Iterative Deepening Depth First Search

(c) Depth First Search

**(d) Uniform Cost Search**

(e) None of the Above


----

5) Given the way we defined search, is it OK to negative path lengths?


- We define search like wavefronts. If we have negative path lengths, our wavefronts might go back and might not give
 us a result.



----

6) Can we have negative path lengths if graph is directed and acyclic?

- Yes. We can. (Just as any path). This might not a dijsktra's algorithm. But using an algorithm like `Bellman-Ford`_


----


7) What happens to A* if we use negative heuristic values?

- Negative heuristics might not over-estimate, and thus can produce admissible heuristics. But negative paths can be
break the heuristic function and lead us through a path which is not optimal.

* `StackOverFlow Reference`_

.. _StackOverFlow Reference: http://stackoverflow.com/questions/30067813/are-heuristic-functions-that-produce-negative-values
-inadmissible
.. _Bellman-Ford: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm


