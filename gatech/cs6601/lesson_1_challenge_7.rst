Challenge: Expectimax Pruning
=============================

**Problem**: Can we prune in Expectimax trees?

**Key insight**: If at any point evaluating further cannot improve the expectimax value, we can prune.

Pruning Rules
-------------

- **Mid-branch**: If we reach the maximum possible value (e.g., 6), further evaluation can only give lower values. Since this won't change the result, we prune.
- **Right-branch**: After getting -3.2 in the first subtree, the maximum achievable is :math:`-3.2 + (10 \times 0.6) = 2.8`. If this is below the current best, prune remaining branches.

Unlike alpha-beta pruning in minimax, expectimax pruning requires knowing bounds on utility values to determine when further evaluation is futile.
