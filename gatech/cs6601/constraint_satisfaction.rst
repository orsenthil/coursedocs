Constraint Satisfaction
=======================



Challenge Question
------------------

.. image:: https://dl.dropbox.com/s/jshq91z8qkpgle7/Screenshot%202017-03-05%2019.49.10.png
   :align: center
   :height: 300
   :width: 450


* Backtracking
* Forward Checking
* Minimum Remaining Values (MRV)
* Least Constraint Value.


Map Coloring
------------

.. image:: https://dl.dropbox.com/s/64nvvjeys0l9cxm/Screenshot%202017-03-05%2019.51.18.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/c2pp2m8ucxpjely/Screenshot%202017-03-05%2019.51.50.png
   :align: center
   :height: 300
   :width: 450

Constraint Graph
----------------

.. image:: https://dl.dropbox.com/s/r9y9obplq8r9hdi/Screenshot%202017-03-05%2019.52.47.png
   :align: center
   :height: 300
   :width: 450

* The nodes are the variables.
* ARCs show the constraints between the variables.

Map Coloring Quiz
-----------------

.. image:: https://dl.dropbox.com/s/f9atvvr680n4i35/Screenshot%202017-03-05%2019.54.10.png
   :align: center
   :height: 300
   :width: 450

CSP Examples
------------

* Preferences Constraints are called - Optimization Problem.
* Solved using Linear Programming.

Constraint Hypergraph
---------------------

.. image:: https://dl.dropbox.com/s/fe9cugk4zfoxh1o/Screenshot%202017-03-05%2019.59.24.png
   :align: center
   :height: 300
   :width: 450


Backtracking Search
-------------------

.. image:: https://dl.dropbox.com/s/s0rdicyuid9qly0/Screenshot%202017-03-05%2020.00.47.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/zlbh6zhjl8voeme/Screenshot%202017-03-05%2020.01.46.png
   :align: center
   :height: 300
   :width: 450

Improving Backtracking Efficiency
---------------------------------

.. image:: https://dl.dropbox.com/s/9zop2vf2cs9hw1k/Screenshot%202017-03-05%2020.04.07.png
   :align: center
   :height: 300
   :width: 450

* Orange was the value that least constrainted the future choices.

.. image:: https://dl.dropbox.com/s/4hzt06su55wq33a/Screenshot%202017-03-05%2020.10.53.png
   :align: center
   :height: 300
   :width: 450

* The variable with the least number of values remaining is south australia, so we assign that next.

* When there is a tie, use degree heuristic. Choose the variable with the most constraints on remaining variables.

.. image:: https://dl.dropbox.com/s/o9kw0u2ridptwqv/Screenshot%202017-03-05%2020.12.51.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/6bzo1ssa7yiww6p/Screenshot%202017-03-11%2013.22.02.png?dl=0
   :align: center
   :height: 300
   :width: 450

Forward Checking
----------------

.. image:: https://dl.dropbox.com/s/33ajsgbb4jz5tbr/Screenshot%202017-03-05%2020.16.18.png
   :align: center
   :height: 300
   :width: 450


* Forward Checking is an early warning system to that helps us notify that our search is going in the wrong direction.


Constraint Propagation And Arc Consistency
------------------------------------------

.. image:: https://dl.dropbox.com/s/iv719mc5o7nloev/Screenshot%202017-03-05%2020.23.35.png
   :align: center
   :height: 300
   :width: 450


* What is ARC Consistency?


Constraint Propagation Quiz
---------------------------

.. image:: https://dl.dropbox.com/s/s51m6psst1equ1t/Screenshot%202017-03-05%2020.24.28.png
   :align: center
   :height: 300
   :width: 450


Structured CSPs
---------------

.. image:: https://dl.dropbox.com/s/v9cqnlknyt1wm81/Screenshot%202017-03-05%2020.26.34.png
   :align: center
   :height: 300
   :width: 450

* Break it down into smaller problems.

.. image:: https://dl.dropbox.com/s/jamhr59wo9q1pz8/Screenshot%202017-03-05%2020.29.27.png
   :align: center
   :height: 300
   :width: 450

* If we have CSP with no loops, we can solve the problem in :math:`O(nd^2)` times.
* `Topological Search`_

.. _Topological Search: https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf

.. image:: https://dl.dropbox.com/s/81f4wmojuaqpn2h/Screenshot%202017-03-05%2020.30.02.png
   :align: center
   :height: 300
   :width: 450


Iterative Algorithms
--------------------

.. image:: https://dl.dropbox.com/s/sfgrwch7yvuv8zt/Screenshot%202017-03-05%2020.31.13.png
   :align: center
   :height: 300
   :width: 450

* MinConflict Algorithm illustration.

Challenge Question
------------------

.. image:: https://dl.dropbox.com/s/ehrw30viveda41w/Screenshot%202017-03-05%2020.32.38.png
   :align: center
   :height: 300
   :width: 450
