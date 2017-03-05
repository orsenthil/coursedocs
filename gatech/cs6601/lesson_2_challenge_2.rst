Searching Rubik's Cube
======================

Define a relaxed problem for Rubik's Cube that we can use to help determine a good
heuristic for searching for the solution. Explain your heuristic and why it is admissible.

Cube's Properties
-----------------

1. 27 small cubes, called cubies (9 * 3).

2. Any turn can affect 8 cubes, one will be the axis and will not be affected by the turn.

Heuristic for solving Rubiks cube
---------------------------------

Rubiks cube is a 3D version of the sliding block puzzle. So, a 3D manhattan distance is a good heuristic.

The :math:`dist(c, final_pos) = |x1-x2| + |y1-y2| + |z1-z2|`

For each cube, compute the minimum number of moves required to correctly position and orient it, and sum these values
over all cubes. To be admissible, this value has to be divided by 8, since every twist moves 8 cubies.

Calculating it accurating seems to be taking separate heuristic over edge cubes and corner cubes.

This paper gives details: http://www.aaai.org/Papers/AAAI/1997/AAAI97-109.pdf

Still working out the details as I don't understand how the various values are gotten in that paper.

<pre>
A better heuristic is to
take the maximum of the sum of the manhattan distances
of the corner cubies, and the edge cubies, each
divided by four. The expected value of the manhattan
distance of the edge cubies is 5.5, while the expected
value of the manhattan distance of the corner cubies
is only about 3, partly because there are 12 edge cubies,
but only 8 corner cubies. As a result, if we only
compute the manhattan distance of the edge cubies,
ignoring the corner cubies, the additional node generations
are made up for by the lower cost per node
</pre>

