Challenge: Rubik's Cube Heuristic
==================================

**Problem**: Define a relaxed problem and admissible heuristic for Rubik's Cube.

Cube Properties
---------------

- 27 cubies (3×3×3); any turn affects 8 cubies (the center axis cubie is fixed)
- A 3D version of the sliding block puzzle

Heuristic: 3D Manhattan Distance
---------------------------------

For each cubie, compute the minimum number of moves to correctly position and orient it:

:math:`\text{dist}(c, \text{final}) = |x_1 - x_2| + |y_1 - y_2| + |z_1 - z_2|`

Sum over all cubies and **divide by 8** (since each twist moves 8 cubies) to maintain admissibility.

**Improved heuristic**: Take the maximum of:

- Sum of Manhattan distances of **corner cubies** ÷ 4
- Sum of Manhattan distances of **edge cubies** ÷ 4

Edge cubies have higher expected Manhattan distance (~5.5) vs corner cubies (~3), making the edge-only heuristic more informative despite the per-node computation cost.
