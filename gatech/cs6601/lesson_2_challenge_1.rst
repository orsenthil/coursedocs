Search Questions
================

**Q1: Advantage of DFS over BFS in resource usage?**

DFS space complexity is :math:`O(bm)` where :math:`b` is branching factor and :math:`m` is max depth. BFS must store all nodes at the current depth level — space complexity :math:`O(b^d)`. For large graphs with limited search depth, DFS uses far less memory.

**Q2: Two advantages of BFS over DFS?**

1. BFS always finds a path if one exists (DFS may loop in cyclic graphs without cycle detection)
2. BFS finds the shallowest (optimal for uniform cost) path first

**Q3: Admissible heuristic for A*?**

**(c)** A heuristic is admissible if and only if it **never overestimates** the cost to the goal.

**Q4: If h(s) = 0 for all states, A* becomes?**

**(d) Uniform Cost Search** — without heuristic guidance, A* degenerates to expanding nodes in order of path cost.

**Q5: Can we have negative path lengths?**

With standard search (wavefront expansion), negative path lengths can cause wavefronts to move backward, breaking optimality. Standard Dijkstra/A* assumes non-negative edge weights.

**Q6: Negative path lengths in directed acyclic graphs?**

Yes — in a DAG, negative edges are safe since there are no cycles. Use Bellman-Ford or topological sort-based relaxation.

**Q7: Negative heuristic values in A*?**

Negative heuristics don't necessarily overestimate, so they can be admissible. However, combined with negative path costs, they can break optimality guarantees. See StackOverflow discussion.
