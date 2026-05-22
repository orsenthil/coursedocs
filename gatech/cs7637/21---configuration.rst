.. title: Configuration
.. slug: Configuration
.. date: 2016-01-23 06:51:57 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Configuration
=============

Design
------

**Design** takes needs, goals, or functions as input and produces a specification of the structure of an artifact that satisfies them. The artifact may be a physical product, a process, a program, or a policy.

Key property: in problem solving, the problem stays fixed while the solution evolves. In design, **problem and solution co-evolve** — understanding the solution space reshapes the problem specification.

Defining Configuration
----------------------

**Configuration** is the most common type of design — a **routine design task** where:

- All components are already known
- All variables for each component are known
- The ranges of values each variable can take are known
- The task is to assign specific values to all variables such that global constraints are satisfied

Examples: laying out a basement floor plan, configuring a computer, planning a route, following a recipe.

The Configuration Process
-------------------------

Configuration follows a **plan refinement** process:

1. **Specify constraints** from the input (e.g., total mass > 200g, total cost ≤ $20, 4 legs)
2. **Apply an abstract plan** to distribute constraints across components (e.g., divide $20 cost evenly among 4 components → ≤ $5 each)
3. **Refine and expand**: move from the whole to individual components, assigning values to more detailed variables
4. **Verify**: check whether the complete assignment satisfies all global constraints
5. **Iterate or revise**: if constraints are violated, either adjust variable assignments or revise the input specification

Knowledge Representation
~~~~~~~~~~~~~~~~~~~~~~~~

Configuration knowledge is represented using **frames**:

- A top-level frame (e.g., "chair") has slots for global properties (mass, cost) and pointers to component frames
- Component frames (e.g., "legs," "seat," "back," "arms") have slots for size, material, cost, count, etc.
- Each slot has a **range of legal values** (e.g., seat mass: 10–100g; material: wood/metal/plastic)
- Cost is computed from size and material using lookup tables (e.g., cost-per-gram by material)

Variable Ordering Heuristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With many variables, ordering matters. Common heuristics:

- **Most constrained first**: variables with the fewest legal values
- **Most constraining first**: variables that restrict the most other variables
- **Most important first**: variables with the greatest impact on overall design

Chair Configuration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given: mass > 200g, cost ≤ $20, 4 legs.

1. Distribute cost: ≤ $5 per component (legs, seat, back, arms)
2. For legs: count = 4 (given), cost ≤ $5 → choose 25g wood each
3. Repeat for seat, back, arms
4. Verify: total mass and cost satisfy global constraints

Different designers may use different plans and different variable orderings, potentially arriving at different valid configurations.

Connections to Other Methods
----------------------------

Classification
~~~~~~~~~~~~~~

Classification makes sense of the world by mapping percepts to categories. Configuration *creates* structure by mapping specifications to arrangements. They are complementary: classification is perception; configuration is construction.

Case-Based Reasoning
~~~~~~~~~~~~~~~~~~~~

Both address routine design. The difference:

- **Configuration**: starts from a prototypical concept and a plan abstraction hierarchy; assigns values top-down
- **Case-based reasoning**: starts from a specific prior design stored in case memory; tweaks it to fit new constraints

Configuration assumes enough past experience to extract general plans. CBR assumes specific past designs are stored for retrieval and adaptation.

Planning
~~~~~~~~

Configuration leverages **skeletal plans** — abstract plans with variables but no assigned values, organized in an abstraction hierarchy. A planner may generate these plans initially; the configuration process instantiates, refines, and expands them.

Cognitive Connection
--------------------

Configuration is an everyday cognitive activity with high economic value. Running errands (known roads, known vehicle, optimize for time), cooking (known recipes, assign ingredient quantities to optimize taste) — both are configuration tasks.

Configuration is a **task** that can be addressed by multiple **methods**: plan refinement, constraint propagation, case-based reasoning, and others. This task-method distinction is central to building a "periodic table of intelligence."
