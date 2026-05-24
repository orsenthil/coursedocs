Simulated Annealing
===================

Optimization and Local Search
-----------------------------

Traveling Salesman Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Visit *n* cities exactly once and return to start, minimizing total distance.
- NP-Hard: no known polynomial-time exact algorithm.
- Heuristic improvement: iteratively uncross paths that intersect.
- Local search starts from a random tour, makes small modifications (e.g., 2-opt swaps).

N-Queens Problem
~~~~~~~~~~~~~~~~

Place *n* queens on an *n* x *n* board so no two attack each other.

- **Heuristic function**: number of attacking pairs (goal = 0).
- **Local search**: move one queen per column to minimize conflicts.
- Gets stuck in local minima — a configuration where every single move increases conflicts.

Hill Climbing
-------------

Local Maxima and Plateaus
~~~~~~~~~~~~~~~~~~~~~~~~~

Hill climbing greedily moves to the best neighbor. Failure modes:

- **Local maximum**: all neighbors are worse, but global optimum exists elsewhere.
- **Plateau (shoulder)**: flat region where no neighbor improves the objective.
- **Ridges**: sequence of local maxima not directly connected.

Step Size
~~~~~~~~~

- **Too small**: gets stuck on plateaus and shoulders; slow convergence.
- **Too large**: oscillates over sharp peaks; may never terminate.
- **Adaptive**: start with large steps, reduce over time.

Random Restarts
~~~~~~~~~~~~~~~

- Run hill climbing multiple times from random initial states.
- Avoids revisiting previously explored basins of attraction.
- With enough restarts, finds global optimum with probability approaching 1.
- Expected restarts: :math:`1/p` where :math:`p` is probability a single run succeeds.

Simulated Annealing Algorithm
-----------------------------

Annealing Intuition
~~~~~~~~~~~~~~~~~~~

Inspired by metallurgical annealing: heating metal and slowly cooling it allows atoms to settle into a low-energy crystalline structure. Analogous energy minimization produces globally optimal configurations.

* Reference

Algorithm
~~~~~~~~~

.. code-block:: text

   function SIMULATED-ANNEALING(problem, schedule) returns a solution state
     current ← initial state of problem
     for t = 1 to ∞ do
       T ← schedule(t)
       if T = 0 then return current
       next ← a randomly selected successor of current
       ΔE ← Value(next) - Value(current)
       if ΔE > 0 then current ← next
       else current ← next with probability exp(ΔE / T)

Key properties:

- **Temperature** :math:`T` starts high, decreases according to a cooling schedule.
- At high :math:`T`: accepts almost any move (exploration, like random walk).
- At low :math:`T`: behaves like hill climbing (exploitation).
- When :math:`\Delta E = 0` (plateau), random walk eventually escapes.
- Acceptance probability of a downhill move: :math:`P = e^{\Delta E / T}`.

Temperature Schedule
~~~~~~~~~~~~~~~~~~~~

- Must decrease slowly enough to allow exploration of the state space.
- Common schedules: linear (:math:`T = T_0 - \alpha t`), geometric (:math:`T = T_0 \cdot \alpha^t`), logarithmic (:math:`T = c / \ln(t+1)`).
- **Theoretical guarantee**: with a logarithmic schedule, SA converges to the global optimum (but impractically slow).

Local Beam Search
-----------------

- Maintain :math:`k` states ("particles") in parallel.
- At each step, generate all successors of all :math:`k` states, keep the best :math:`k` overall.
- Differs from :math:`k` random restarts: states share information (best regions attract more particles).
- **Stochastic beam search**: select successors probabilistically (proportional to fitness) to maintain diversity.

Genetic Algorithms
------------------

Representation
~~~~~~~~~~~~~~

Encode candidate solutions as strings (e.g., n-Queens: a sequence of row positions per column).

Fitness and Selection
~~~~~~~~~~~~~~~~~~~~~

Fitness function for n-Queens:

.. math::

   f = \binom{n}{2} - \text{number\_of\_attacking\_pairs}

For 8-Queens: max fitness = 28 (no attacks).

**Selection**: probability of selecting individual :math:`i` is proportional to its fitness:

.. math::

   P(i) = \frac{f_i}{\sum_j f_j}

Roulette-wheel selection: normalize fitness scores to percentages, roll to select parents.

Crossover
~~~~~~~~~

- Select a random crossover point.
- Combine the prefix of one parent with the suffix of the other.
- Produces offspring that inherit structure from both parents.

Mutation
~~~~~~~~

- Randomly alter one gene (e.g., change one queen's row position) with small probability.
- Introduces diversity not present in any parent.
- Prevents premature convergence to local optima.
- **Without mutation**, GA risks never reaching the global optimum if the necessary gene values are absent from the initial population.

GA Summary
~~~~~~~~~~

1. Initialize random population.
2. Evaluate fitness.
3. Select parents (fitness-proportional).
4. Crossover to produce offspring.
5. Mutate with small probability.
6. Replace population; repeat until convergence.
