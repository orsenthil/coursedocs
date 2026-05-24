Game Playing
============

AIMA: Chapter 5.1–5.4

Overview
--------

1. Adversarial Search
2. Minimax Algorithm
3. Alpha-Beta Pruning
4. Evaluation Functions
5. Isolation Game Player
6. Multi-Player & Probabilistic Games

Isolation Game
--------------

Isolation is a two-player, zero-sum, perfect-information game on a grid.
Players alternate moves; a player who cannot move loses.

* Columbia CS notes on the Isolation game
* Full Isolation Game Board

Building a Game Tree
~~~~~~~~~~~~~~~~~~~~

Each node represents a board state. Edges represent legal moves.
The tree alternates between the two players from the root down to terminal states
(win/loss). Terminal nodes are scored: +1 for a win, −1 for a loss.

Minimax Algorithm
-----------------

The **minimax** value of a node is computed recursively:

::

    function MINIMAX(node):
        if node is terminal:
            return utility(node)
        if node is MAX:
            return max(MINIMAX(child) for child in children(node))
        if node is MIN:
            return min(MINIMAX(child) for child in children(node))

* **MAX** picks the move with the highest minimax value.
* **MIN** picks the move with the lowest minimax value.
* The root is always a **MAX** node (the computer player).
* The computer chooses any branch that achieves the optimal minimax value.

Complexity
~~~~~~~~~~

For a game with average branching factor *b* and depth *d*:

* **Nodes in tree:** O(b^d)
* **Time:** O(b^d)
* **Space:** O(b·d) with depth-first exploration

For the 5×5 isolation game: max moves ≈ 25, branching factor varies per level.
Full game trees are intractable for non-trivial board sizes.

Depth-Limited Search
~~~~~~~~~~~~~~~~~~~~

Since full-depth minimax is infeasible for most games, search is cut off at
a fixed depth limit *ℓ*. Non-terminal nodes at depth *ℓ* are scored by an
**evaluation function** instead of exact minimax values.

Evaluation Functions
--------------------

An evaluation function estimates how favorable a position is without searching
to terminal states. Good evaluation functions:

* Correlate strongly with the true minimax value
* Are fast to compute
* Capture strategically important features

Common heuristic for isolation: **number of available moves** for the player,
or the difference ``my_moves − opponent_moves``.

* Isolation Game Tree - Level 2
* Isolation Game Tree - Level 3

Quiescent Search
~~~~~~~~~~~~~~~~

Depth-limited evaluation can be misleading in **volatile** positions (e.g., just
before a capture in chess). **Quiescent search** extends search selectively in
non-quiet positions until a stable state is reached, then applies the evaluation function.

Horizon Effect
~~~~~~~~~~~~~~

A fixed-depth search may "push" an inevitable loss beyond the search horizon by
making delaying moves, causing the agent to behave as if the bad outcome won't happen.
Quiescent search and singular extensions help mitigate this.

Iterative Deepening
-------------------

Run depth-limited search with increasing depth limits: 1, 2, 3, ...
Return the best move found when time runs out.

* Combines DFS space efficiency O(b·d) with BFS completeness.
* The overhead of re-expanding shallow nodes is small because most nodes are at the deepest level:
  for b=3, iterative deepening expands only ~50% more nodes than a single depth-*d* search.
* Natural fit for **time-limited** game-playing — always has a move ready.

* University of British Columbia's slides on iterative deepening
* Visually how Iterative Deepening is different from DFS

Alpha-Beta Pruning
------------------

Alpha-beta pruning reduces the search tree without affecting the minimax value.

::

    function ALPHA-BETA(node, α, β):
        if node is terminal:
            return utility(node)
        if node is MAX:
            v = −∞
            for each child:
                v = max(v, ALPHA-BETA(child, α, β))
                α = max(α, v)
                if β ≤ α: break    # β cutoff
            return v
        if node is MIN:
            v = +∞
            for each child:
                v = min(v, ALPHA-BETA(child, α, β))
                β = min(β, v)
                if β ≤ α: break    # α cutoff
            return v

Key properties:

* **α** = best value MAX can guarantee (lower bound)
* **β** = best value MIN can guarantee (upper bound)
* A subtree is pruned when α ≥ β — no move in that subtree can influence the result.
* **Best case** (perfect move ordering): examines O(b^(d/2)) nodes — effectively doubles search depth.
* **Worst case** (no pruning): O(b^d), same as minimax.

Multi-Player Games
------------------

3-Player Games
~~~~~~~~~~~~~~

With three or more players, each node stores a **vector** of utilities (one per player).
Each player maximizes their own component. Minimax generalizes:
each player picks the action maximizing their own utility at their turn.

Multi-Player Alpha-Beta Pruning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alpha-beta pruning is less effective with more than two players because
utilities are no longer zero-sum — one player's gain is not necessarily another's loss.
Pruning requires bounds on *all* players' utilities.

* Korf 1991 — generalizes alpha-beta to multi-player games.

Probabilistic Games
~~~~~~~~~~~~~~~~~~~

Games with chance elements (e.g., dice rolls) add **chance nodes** to the game tree.
The value of a chance node is the **expected value** over all outcomes:

  V(chance node) = Σ P(outcome) × V(child)

Expectiminimax extends minimax by averaging over chance nodes.
Alpha-beta pruning still applies but requires known bounds on utility values.

Further Reading
---------------

* Game Playing (Udacity CS271)
* Game Theory (Udacity CS271)
* Alpha-beta visualization
