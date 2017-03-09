Game Playing
============

Artificial Intelligence - A Modern Approach (AIMA): Chapter 5.1-5.2


Overview
--------

1. Aversarial Search
2. Minimax Algorithm.
3. Alpha-Beta Pruning
4. Evaluation Functions
5. Isolation Game Player
6. Multi-Player Probabilistic Games.

Challenge Question Introduction
-------------------------------


.. image:: https://dl.dropbox.com/s/lj86rr1zu2kz570/Screenshot%202017-03-07%2018.42.35.png?dl=0
   :align: center
   :height: 300
   :width: 450


Isolation
---------

.. image:: https://dl.dropbox.com/s/iloy4ls40m9scz3/Screenshot%202017-03-07%2018.47.36.png?dl=0
   :align: center
   :height: 300
   :width: 450

* http://www.cs.columbia.edu/~sal/notes/assign3-isolation-game.htm
* https://github.com/SashaZd/GaTech-AI-Isolation

Building a Game Tree
--------------------

.. image:: https://dl.dropbox.com/s/k30hks5zr6di44e/Screenshot%202017-03-07%2018.53.06.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/fs9tltf8fiqgm7v/Screenshot%202017-03-07%2018.53.31.png?dl=0
   :align: center
   :height: 300
   :width: 450


Which are valid moves for O
---------------------------

.. image:: https://dl.dropbox.com/s/pywd5xaw0elgl82/Screenshot%202017-03-07%2020.47.32.png?dl=0
   :align: center
   :height: 300
   :width: 450

Building a Game Tree
--------------------

.. image:: https://dl.dropbox.com/s/xp66yuh6pxogrw7/Screenshot%202017-03-07%2020.49.59.png?dl=0
   :align: center
   :height: 300
   :width: 450

How Do We Tell The Computer Not To Lose?
----------------------------------------

* `Full Isolation Game Board`_

.. _Full Isolation Game Board: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/images/isolation-L6_leafValues.svg

MIN and MAX Levels
------------------

.. image:: https://dl.dropbox.com/s/1w9skfznwcv4414/Screenshot%202017-03-07%2020.52.05.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Top of MIN-MAX Tree is always going to be a Max Level.

Propagating Values Up The Tree
------------------------------

.. image:: https://dl.dropbox.com/s/zbwc43igayxxb9c/Screenshot%202017-03-07%2021.22.41.png?dl=0
   :align: center
   :height: 300
   :width: 450


Computing MIN MAX Values
------------------------

.. image:: https://dl.dropbox.com/s/fndd269dyaq365j/Screenshot%202017-03-07%2021.23.23.png?dl=0
   :align: center
   :height: 300
   :width: 450

Choosing the Best Branch
------------------------

* Computer Player has to choose any of the best branches and it will win.


Max Number Of Nodes Visited
---------------------------

.. image:: https://dl.dropbox.com/s/f99zmfvb9zzrv3y/Screenshot%202017-03-07%2021.31.00.png?dl=0
   :align: center
   :height: 300
   :width: 450

Max Moves
---------

.. image:: https://dl.dropbox.com/s/kyrzkeb9z4vefkl/Screenshot%202017-03-07%2021.37.52.png
   :align: center
   :height: 300
   :width: 450

The Branching Factor
--------------------

.. image:: https://dl.dropbox.com/s/cu9u79bt2i1gd6g/Screenshot%202017-03-07%2021.41.04.png?dl=0
   :align: center
   :height: 300
   :width: 450


Number of Nodes In a Game Tree
------------------------------

.. image:: https://dl.dropbox.com/s/mit38y1u0tixnuq/Screenshot%202017-03-07%2021.42.31.png?dl=0
   :align: center
   :height: 300
   :width: 450

* Here 'b' is the average branching factor and 'd' is the depth of the game tree.


Depth-Limited Search
--------------------

.. image:: https://dl.dropbox.com/s/re1u5mghnrkx0qg/Screenshot%202017-03-07%2021.53.34.png?dl=0
   :align: center
   :height: 300
   :width: 450


Evaluation Function Intro
-------------------------

* Maximize the number of the moves left.

Testing The Evaluation Function
-------------------------------

.. image:: https://dl.dropbox.com/s/r7qtbgkch9jctra/Screenshot%202017-03-07%2021.55.36.png?dl=0
   :align: center
   :height: 300
   :width: 450


Testing The Evaluation Function Part 2
--------------------------------------

.. image:: https://dl.dropbox.com/s/3wdu1zgekr7ycy8/Screenshot%202017-03-07%2021.56.59.png?dl=0
   :align: center
   :height: 300
   :width: 450

* `Isolation Game Tree - Level 3`_

.. _Isolation Game Tree - Level 3: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/images/isolation-L3_minMax.svg


Testing Evaluation Functions
----------------------------

.. image:: https://dl.dropbox.com/s/x6txmhx9n2cyp01/Screenshot%202017-03-07%2021.59.03.png?dl=0
   :align: center
   :height: 300
   :width: 450

* `Isolation Game Tree - Level 2`_

.. _Isolation Game Tree - Level 2: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/images/isolation-L2_minMax.svg


Quiescent Search
----------------

.. image:: https://dl.dropbox.com/s/qxzxrmowaiutr0q/Screenshot%202017-03-07%2022.00.39.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/jx88e5j1yhkrlqa/Screenshot%202017-03-07%2022.01.09.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/6cvwrd9p09y2299/Screenshot%202017-03-07%2022.01.27.png?dl=0
   :align: center
   :height: 300
   :width: 450

Iterative Deeping
-----------------

* `University of British Columbia's slides`_ introducing the topic.
* 3.4.5 of Russel, Norvig
*  `Visually how Iterative Deepening is different from DFS`_

.. _University of British Columbia's slides: https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf
.. _Visually how Iterative Deepening is different from DFS: http://movingai.com/dfid.html

Understanding Exponential Time
------------------------------

.. image:: https://dl.dropbox.com/s/mc649domlgufxln/Screenshot%202017-03-07%2022.05.44.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/wzbfcamsog737fe/Screenshot%202017-03-07%2022.06.18.png?dl=0
   :align: center
   :height: 300
   :width: 450


Exponential B=3
---------------

.. image:: https://dl.dropbox.com/s/emzdg8az5yie2sm/Screenshot%202017-03-07%2022.07.02.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/81fitiz3x4e48nm/Screenshot%202017-03-07%2022.08.20.png?dl=0
   :align: center
   :height: 300
   :width: 450


Horizon Effect
--------------

.. image:: https://dl.dropbox.com/s/2a47wc45ljnfe6e/Screenshot%202017-03-07%2022.10.46.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Good Evaluation Functions
-------------------------------

.. image:: https://dl.dropbox.com/s/dz6jvscqojq0bwf/Screenshot%202017-03-07%2022.14.22.png?dl=0
   :align: center
   :height: 300
   :width: 450

Evaluating Evaluation Functions
-------------------------------

.. image:: https://dl.dropbox.com/s/0ltpi7kjsmadar6/Screenshot%202017-03-07%2022.16.06.png?dl=0
   :align: center
   :height: 300
   :width: 450


Alpha-Beta Pruning
------------------

.. image:: https://dl.dropbox.com/s/frkd2ve0wscifj1/Screenshot%202017-03-07%2022.19.10.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/dhsjvhdypxyguby/Screenshot%202017-03-07%2022.20.17.png?dl=0
   :align: center
   :height: 300
   :width: 450


Minimax Quiz
------------

.. image:: https://dl.dropbox.com/s/ibvffk4rjo70vtx/Screenshot%202017-03-07%2022.20.40.png?dl=0
   :align: center
   :height: 300
   :width: 450

Alpha Beta Pruning Quiz 1
-------------------------

.. image:: https://dl.dropbox.com/s/k2km031si3smp2e/Screenshot%202017-03-08%2020.10.22.png
   :align: center
   :height: 300
   :width: 450

Alpha-Beta Pruning Quiz 2
-------------------------

.. image:: https://dl.dropbox.com/s/us8h6eye7mhdmwn/Screenshot%202017-03-08%2020.12.25.png?dl=0
   :align: center
   :height: 300
   :width: 450

Searching Complex Games
-----------------------

* AIMA: Chapter 5.3-5.4

3-Player Games
--------------

.. image:: https://dl.dropbox.com/s/ghvix4o008zwn5n/Screenshot%202017-03-08%2020.22.39.png?dl=0
   :align: center
   :height: 300
   :width: 450

3-Player Games Quiz
-------------------

.. image:: https://dl.dropbox.com/s/vu0n6vctyi6my8p/Screenshot%202017-03-08%2020.23.27.png?dl=0
   :align: center
   :height: 300
   :width: 450

3-Player Alpha-Beta Pruning
---------------------------

.. image:: https://dl.dropbox.com/s/jrds4kwx94sh7g4/Screenshot%202017-03-08%2020.29.08.png?dl=0
   :align: center
   :height: 300
   :width: 450

Multi-player Alpha-Beta Pruning
-------------------------------

* `Korf 1991`_

.. _Korf 1991: http://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/Korf_Multi-player-Alpha-beta-Pruning.pdf

In the above paper, you will get a chance to generalize minimax search techniques to games with more
than three players. As you'll see, alpha-beta pruning doesn't work quite as effectively in this case
as in the general case. Here are a few questions to keep in mind while reading through this paper:

* Why might alphabeta pruning only work well in the two player case?
* How does the size of the search tree change with more than two players?

Probabilistic Games
-------------------

.. image:: https://dl.dropbox.com/s/2nb8d6d03kh2zu6/Screenshot%202017-03-08%2020.39.46.png?dl=0
   :align: center
   :height: 300
   :width: 450

Probabilistic Alpha-Beta Pruning
--------------------------------

.. image:: https://dl.dropbox.com/s/wnmy02gdmluvokr/Screenshot%202017-03-08%2020.40.26.png?dl=0
   :align: center
   :height: 300
   :width: 450



Further Watching
----------------

* `Game Playing`_
* `Game Theory`_

.. _Game Playing: https://classroom.udacity.com/courses/cs271/lessons/48720299/concepts/482718700923
.. _Game Theory: https://classroom.udacity.com/courses/cs271/lessons/48716317/concepts/484037340923

Resources
---------

* * https://www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html
