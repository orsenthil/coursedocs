Search
======

* http://norvig.com/


Challenge 1 Tri City Search
---------------------------

.. image:: https://dl.dropbox.com/s/9hrrmfgnc7sc1ix/Screenshot%202017-03-11%2016.50.57.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Tri-directional A* search

Challenge 2 Rubik’s Cube
------------------------

.. image:: https://dl.dropbox.com/s/f3e3lapwf16ii40/Screenshot%202017-03-11%2016.52.48.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/7k6rxfsnrgr9syx/Screenshot%202017-03-11%2016.53.15.png?dl=0
   :align: center
   :height: 300
   :width: 450

* `Finding Optimal Solutions to Rubik's Cube Using Pattern Databases`_

* `God's Number is 26 in the Quarter-Turn Metric`_

.. _Finding Optimal Solutions to Rubik's Cube Using Pattern Databases: https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf

.. _God's Number is 26 in the Quarter-Turn Metric: http://www.cube20.org/qtm/

Problem Solving
---------------

.. image:: https://dl.dropbox.com/s/cw98aqwstjw1mrj/Screenshot%202017-03-11%2016.54.27.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Complexity from the many choices.

.. image:: https://dl.dropbox.com/s/fktehlsp8b76hpe/Screenshot%202017-03-11%2016.55.08.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Complexity comes from partial observability.


Question: Can we find the direction from Arad to Bucharest from this map?

.. image:: https://dl.dropbox.com/s/xioo8g9rmnbmulu/Screenshot%202017-03-11%2016.56.53.png?dl=0
   :align: center
   :height: 300
   :width: 450

What is a problem
-----------------

Agent is given a problem of coming up with a sequence of actions to find a path from Arad to Bucharest.

.. image:: https://dl.dropbox.com/s/9tov18zruhnbxh5/Screenshot%202017-03-11%2016.58.37.png?dl=0
   :align: center
   :height: 300
   :width: 450

**Definition of the problem**

* Initial State
* Actions(s) -> {a1, a2, a3 }
* Result(s, a) -> s'
* GoalTest(s) -> T|F
* Path Cost

.. image:: https://dl.dropbox.com/s/z8pjwwntc678y6u/Screenshot%202017-03-11%2017.09.26.png?dl=0
   :align: center
   :height: 300
   :width: 450

Example Route Finding
---------------------

.. image:: https://dl.dropbox.com/s/vwfcrvjjwfwicoy/Screenshot%202017-03-11%2017.13.28.png?dl=0
   :align: center
   :height: 300
   :width: 450

Tree Search
-----------

.. image:: https://dl.dropbox.com/s/jaygycapiax8t1f/Screenshot%202017-03-11%2017.15.33.png?dl=0
   :align: center
   :height: 300
   :width: 450


**Breadth-First Search**

.. image:: https://dl.dropbox.com/s/gq6xr3yxvcnwm15/Screenshot%202017-03-11%2017.17.54.png?dl=0
   :align: center
   :height: 300
   :width: 450

Tree Search Continued
---------------------

.. image:: https://dl.dropbox.com/s/zi6hnouw0x3hf8g/Screenshot%202017-03-11%2017.19.15.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image::  https://dl.dropbox.com/s/74uvaa3krzyh7qb/Screenshot%202017-03-11%2017.20.29.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/v8kdyacspkdaxr9/Screenshot%202017-03-11%2017.20.57.png?dl=0
   :align: center
   :height: 300
   :width: 450

In the preliminary algorithm, A is repeated since we are not keeping track
of explored states. Ideally, we would not add duplicates from backtracking.


Graph Search
------------

.. image:: https://dl.dropbox.com/s/7hp7h5hhp81eoj4/Screenshot%202017-03-11%2017.22.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

Breadth First Search-1
----------------------

.. image:: https://dl.dropbox.com/s/ra52b797qflj2qw/Screenshot%202017-03-11%2017.23.22.png?dl=0
   :align: center
   :height: 300
   :width: 450

Breadth First Search 3
----------------------

.. image:: https://dl.dropbox.com/s/k838t1nbn743xsj/Screenshot%202017-03-11%2017.28.05.png?dl=0
   :align: center
   :height: 300
   :width: 450

Uniform Cost Search
-------------------

* Cheapest path cost search.

.. image:: https://dl.dropbox.com/s/b4454ghdkkpmn3g/Screenshot%202017-03-11%2017.31.07.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/zqog7y1l32nk1l9/Screenshot%202017-03-11%2017.32.21.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/bynvzvkyrgjxwyg/Screenshot%202017-03-11%2017.33.42.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/5vtnf4tq4zvcabe/Screenshot%202017-03-11%2017.34.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/s4nhgdrqk96pu8o/Screenshot%202017-03-11%2017.35.51.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/lokqughck4vcnqe/Screenshot%202017-03-11%2017.38.24.png?dl=0
   :align: center
   :height: 300
   :width: 450


Search Comparison
-----------------

.. image:: https://dl.dropbox.com/s/1ynre2ilbo651w2/Screenshot%202017-03-11%2017.39.24.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/bvrgjux6xkm6l0s/Screenshot%202017-03-11%2017.40.51.png?dl=0
   :align: center
   :height: 300
   :width: 450

Search Comparison - 1
---------------------

.. image:: https://dl.dropbox.com/s/tmkg51idgy7sggk/Screenshot%202017-03-11%2017.42.45.png?dl=0
   :align: center
   :height: 300
   :width: 450

Search Comparison 2
-------------------

.. image:: https://dl.dropbox.com/s/d0akq8tmrt3badd/Screenshot%202017-03-11%2017.44.16.png?dl=0
   :align: center
   :height: 300
   :width: 450


Are these algorithms complete?

.. image:: https://dl.dropbox.com/s/zy6043vs3ig1b42/Screenshot%202017-03-11%2017.45.13.png?dl=0
   :align: center
   :height: 300
   :width: 450

More On Uniform Cost
--------------------

.. image:: https://dl.dropbox.com/s/yza7askvs5usxao/Screenshot%202017-03-11%2017.47.28.png?dl=0
   :align: center
   :height: 300
   :width: 450

**Greedy Best-First Search**

.. image:: https://dl.dropbox.com/s/aua84jir6v725uu/Screenshot%202017-03-11%2017.49.11.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/pqldcllvcv93uok/Screenshot%202017-03-11%2017.50.12.png?dl=0
   :align: center
   :height: 300
   :width: 450


A* = Greedy Best First Search + Uniform Cost Search


A* Search
---------

.. image:: https://dl.dropbox.com/s/jg6ijzqml33r9mi/Screenshot%202017-03-11%2017.53.16.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/2me6ldgipmc8wem/Screenshot%202017-03-11%2017.53.50.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/mpnflh4bu1vnv01/Screenshot%202017-03-11%2017.56.02.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/hk4r585m7m6wsg7/Screenshot%202017-03-11%2017.57.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/l1r7e0ubl7o5uru/Screenshot%202017-03-11%2017.58.18.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/npc2k23bs1gwnsn/Screenshot%202017-03-11%2017.59.21.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/a4onhk9xayz0nv5/Screenshot%202017-03-11%2018.00.59.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/b7bn4nwlomzbi4v/Screenshot%202017-03-11%2018.01.38.png?dl=0
   :align: center
   :height: 300
   :width: 450

Admissible Heuristic Function
-----------------------------

Heuristic function is admissible if h(s) <= true cost, rather
than necessarily being strictly smaller than the true cost.


* h should never overestimate the distance to the goal.
* h should be optimistic
* h is admissible.

Optimistic Heuristic
--------------------

.. image:: https://dl.dropbox.com/s/mpxiux0z5x8jvkk/Screenshot%202017-03-11%2018.03.51.png?dl=0
   :align: center
   :height: 300
   :width: 450

State Spaces
------------

.. image:: https://dl.dropbox.com/s/l53hhz0iclp8e8x/Screenshot%202017-03-11%2018.05.24.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/5vnahasoimx6bfb/Screenshot%202017-03-11%2018.06.11.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Robot can be A or B = 2

World itself

* State A can be dirty or not = 2

* State B can be dirty or not = 2

Total = 2 x 2 x 2 = 8 state spaces.

State Spaces 2
--------------

.. image:: https://dl.dropbox.com/s/u2oocwpyrzv27kp/Screenshot%202017-03-11%2018.10.18.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/9aj4zpi7vryjngn/Screenshot%202017-03-11%2018.11.31.png?dl=0
   :align: center
   :height: 300
   :width: 450

Sliding Blocks Puzzle
---------------------

.. image:: https://dl.dropbox.com/s/disppsbj849av7u/Screenshot%202017-03-11%2018.13.41.png?dl=0
   :align: center
   :height: 300
   :width: 450

Sliding Blocks Puzzle 2
-----------------------

.. image:: https://dl.dropbox.com/s/zpx12n437kjy5fb/Screenshot%202017-03-11%2018.16.57.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Generating a relaxed problem.


Problems With Search
--------------------

.. image:: https://dl.dropbox.com/s/6xv9y25454x7in3/Screenshot%202017-03-11%2018.19.42.png?dl=0
   :align: center
   :height: 300
   :width: 450

A Note On Implementation
------------------------

.. image:: https://dl.dropbox.com/s/zkdn86iy1tfsejy/Screenshot%202017-03-11%2018.22.05.png?dl=0
   :align: center
   :height: 300
   :width: 450

References
----------


* Korf, 1997, `Finding Optimal Solutions to Rubik's Cube Using Pattern Databases.`_
* Goldberg, 2011. `Reach for A* An Efficient Point-to-Point Shortest Path Algorithm`_
* Goldberg & Harrelson, March 2003. `Computing the Shortest Path A* Search Meets Graph Theory.`_
* Gutman, 2004. `Reach-based Routing A New Approach to Shortest Path Algorithms Optimized for Road Networks.`_


.. _Finding Optimal Solutions to Rubik's Cube Using Pattern Databases.: https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf

.. _Reach for A* An Efficient Point-to-Point Shortest Path Algorithm: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/02-search-01-Astart-ALT-Reach.pdf

.. _Computing the Shortest Path A* Search Meets Graph Theory.: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/02-search-Goldberg03tr.pdf

.. _Reach-based Routing A New Approach to Shortest Path Algorithms Optimized for Road Networks.: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/02-search-Gutman04siam.pdf
