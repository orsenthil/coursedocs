Planning Under Uncertainty
==========================

Markov Decision Processes
-------------------------

Core Concepts
~~~~~~~~~~~~~

An **MDP** is defined by the tuple :math:`(S, A, T, R, \gamma)`:

- :math:`S` — set of states
- :math:`A` — set of actions
- :math:`T(s, a, s') = P(s' | s, a)` — transition model (Markov property: depends only on current state)
- :math:`R(s)` or :math:`R(s, a, s')` — reward function
- :math:`\gamma \in [0, 1)` — discount factor

A **policy** :math:`\pi(s) \to a` maps each state to an action. The goal is to find the **optimal policy** :math:`\pi^*` that maximizes expected cumulative discounted reward.

MDP Grid World
~~~~~~~~~~~~~~

Classic example: agent on a grid with stochastic movement.

- Action ``North`` moves North with 80% probability, East or West with 10% each.
- Terminal states with positive (+1) or negative (-1) reward.
- Step cost (e.g., -0.04) encourages finding the goal quickly.
- Walls: attempted move into wall leaves agent in place.

Problems with Conventional Planning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Branching factor too large**: stochastic actions create exponential branching.
- **Plans become contingency trees**, not sequences — need policies instead.
- A **policy** assigns an action to every state, handling any outcome automatically.

Policy and Costs
~~~~~~~~~~~~~~~~

The optimal policy depends on the reward structure:

- High step cost → agent takes risks to finish quickly (e.g., walks near -1 terminal).
- Low step cost → agent takes safe detours to avoid negative terminals.
- Negative step cost < -1 → any terminal is preferable to continuing, even the -1 terminal.

Value Iteration
~~~~~~~~~~~~~~~

Computes optimal state values via iterative Bellman updates:

.. math::

   V_{k+1}(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} T(s, a, s') \, V_k(s') \right]

Algorithm:

1. Initialize :math:`V_0(s) = 0` for all states.
2. For each iteration, update every state using the Bellman equation.
3. Repeat until :math:`\max_s |V_{k+1}(s) - V_k(s)| < \epsilon`.
4. Extract policy: :math:`\pi^*(s) = \arg\max_a \left[ R(s,a) + \gamma \sum_{s'} T(s,a,s') V(s') \right]`.

**Convergence**: guaranteed because :math:`\gamma < 1` makes the Bellman operator a contraction.

Example computation (stochastic grid world)::

   >>> 77 * 0.8 + (0.1 * -100) - 3
   48.6

Policy Iteration
~~~~~~~~~~~~~~~~

Alternates between evaluation and improvement:

1. **Policy evaluation**: given fixed policy :math:`\pi`, solve for :math:`V^\pi(s)` (system of linear equations).
2. **Policy improvement**: for each state, set :math:`\pi(s) = \arg\max_a Q(s, a)`.
3. Repeat until policy is stable.

Converges in fewer iterations than value iteration but each iteration is more expensive (solves a linear system).

MDP Summary
~~~~~~~~~~~

- MDPs model sequential decision-making under stochastic transitions.
- Value iteration and policy iteration both converge to optimal policy.
- Discount factor :math:`\gamma` ensures finite utility for infinite horizons.
- Optimal policy depends on transition probabilities, rewards, and discount factor.

Partially Observable MDPs
-------------------------

Overview
~~~~~~~~

When the agent cannot directly observe the full state, use a **POMDP**.

* Reference: `Emery & Montemerlo (2004) <http://robots.stanford.edu/papers/EmeryMontemerlo04a.pdf>`_

POMDP vs. MDP
~~~~~~~~~~~~~~

===============  ====================================  =========================================
Property         MDP                                   POMDP
===============  ====================================  =========================================
State            Fully observable                       Partially observable
Agent tracks     Current state                          Belief state :math:`b(s)` (distribution)
Policy input     State :math:`s`                        Belief state :math:`b`
Action choice    :math:`\pi(s)`                         :math:`\pi(b)`
===============  ====================================  =========================================

POMDP Definition
~~~~~~~~~~~~~~~~

Extends MDP with:

- :math:`O` — set of observations
- :math:`Z(o | s', a)` — observation model (probability of observation given resulting state and action)

The agent maintains a **belief state** :math:`b(s)` — a probability distribution over states, updated via Bayes' rule after each action and observation:

.. math::

   b'(s') = \eta \; Z(o | s', a) \sum_s T(s, a, s') \, b(s)

where :math:`\eta` is a normalizing constant.

Solving POMDPs
~~~~~~~~~~~~~~

- The belief space is continuous (simplex over states), making exact solutions intractable for large problems.
- **Belief-space MDP**: convert POMDP to an MDP over belief states; apply value iteration in belief space.
- Optimal finite-horizon value function is piecewise-linear and convex over the belief simplex.
- **Approximations**: point-based value iteration (PBVI), POMCP (Monte Carlo tree search over beliefs).

Reinforcement Learning Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the transition model :math:`T` and/or reward function :math:`R` are unknown, the agent must learn from interaction:

- **Model-based RL**: learn :math:`T` and :math:`R`, then solve the MDP.
- **Model-free RL**: learn :math:`Q(s, a)` directly (e.g., Q-learning, SARSA).

Further Study
~~~~~~~~~~~~~

- `Markov Decision Processes (Isbell & Littman) <https://classroom.udacity.com/courses/ud262/lessons/684808907/concepts/last-viewed>`_
- `Reinforcement Learning (Isbell & Littman) <https://classroom.udacity.com/courses/ud262/lessons/643978935/concepts/last-viewed>`_
- `Reinforcement Learning (Norvig & Thrun) <https://classroom.udacity.com/courses/cs271/lessons/48724471/concepts/last-viewed>`_
