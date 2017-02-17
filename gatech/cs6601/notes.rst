Course Introduction
-------------------

* Game Playing
* Smarter that yourself in playing a game.
* Adversarial Search
* Minimax Algorithms.
* Alpha-Beta Pruning
* Evaluation Functions
* Isolation game player.
* Multiplayer Probablistic Games.

* Same Algorithm, Same Code.
* Tic-Tac-Toe.

* Next Possible Move.

* Minimax
* Alpha-Beta Pruning

* Deterministic games.
* Backgammon
* Expectimax ( Considers all possible outcomes and chooses one that maximum return)

Game of Isolation
-----------------

* Game Board.
* Rules of Isolation.
* Fight to the correct.

Making a GameTree

* best Move, best possibility of winning.

* Back Propagate our Knowledge to the computer player to make the wise first move.

Quit on Branching Factor

https://classroom.udacity.com/courses/ud954/lessons/4747398595/concepts/53220985490923

after first two, 12 or fewer moves available. - that will be called the branching factor.

Average Branching Factor

* Do the simple thing first and always add intelligence when necessary.

* Depth Limited Search

* Evaluation Function my_moves - which moves lead to success and which lead to failure.

* Quiescent Search
* Not searching deep enough to get good answers.
* Quiescence Search
* We dont have to use the quiescense search all the time.
* Iterative Deepening might help us too.
* Iterative Deepening  - at each level.
* Surprisingly, the iterative deepening does not waste that much of a time.


.. image:: https://dl.dropbox.com/s/3q2czfyhvqfogh2/Screenshot%202017-01-19%2008.00.02.png
   :align: center
   :height: 300
   :width: 450


Minimax
-------

* Final Game States are ranked according to whether they are win, draw or loss.
* Intermediate Game States are ranked according to whose turn it is and the available moves.

   * If its X's turn, set the rank to that of the maximum move available. In other words, if a move will result in a win, X should take it.
   * If it's O's turn, set the rank to that of the minimum move available. In other words, if a move will result in a loss, X should avoid it.


How to use minimax
------------------

* https://www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html

How to design Rubik's Cube
--------------------------

Iterative Deepening with with A*

Problem Solving
---------------

* Comes from Many States


