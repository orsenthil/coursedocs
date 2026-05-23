Advanced Topics
===============


Visuospatial Reasoning
----------------------

**Visuospatial reasoning** is reasoning with visuospatial knowledge, which has two components:

- **Visual** — the "what" (objects, identities)
- **Spatial** — the "where" (locations, spatial relations)

A defining characteristic of visuospatial knowledge is that causality is at most *implicit*. A picture of a fallen cup with a pool of water doesn't explicitly state causation, but we infer the cup fell and spilled. Visuospatial knowledge enables inferences about causality without representing it directly.


Propositional vs. Analogical Representations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two approaches to handling visuospatial knowledge:

**Propositional representations** (amodal):

- Extract symbolic descriptions from figures (e.g., "triangle, apex right, rotated 90°")
- Manipulate these descriptions using logic or production rules
- Divorced from perceptual modality
- This is how most AI systems currently work

**Analogical representations** (modal):

- Maintain structural correspondence between the representation and the external figure
- Apply affine/set transformations directly (rotation, reflection)
- Close to the perceptual modality
- Human mental imagery appears to use analogical representations

The same distinction applies to other modalities (e.g., auditory). Open questions in cognitive science: When a melody reminds you of another, are you matching propositional extractions or directly matching analogical representations?


Knowledge Content and Encoding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+----------------+---------------------+
| Content        | Encoding       | Example             |
+================+================+=====================+
| Visuospatial   | Analogical     | Mental image of cup |
+----------------+----------------+---------------------+
| Visuospatial   | Propositional  | "circle at (3,4)"   |
+----------------+----------------+---------------------+
| Verbal         | Propositional  | Script with slots   |
+----------------+----------------+---------------------+
| Verbal         | Analogical     | Short mental movie  |
+----------------+----------------+---------------------+

Most of KBAI deals with verbal/propositional knowledge. Fully understanding and leveraging visuospatial + analogical representations remains an open challenge.


Galatea: Visuospatial Analogical Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Galatea** (Jim Davies, Georgia Tech) demonstrated analogical problem-solving using purely visuospatial knowledge without extracting causal patterns.

The Duncker radiation problem: A physician must destroy a tumor with a laser, but the beam at full strength kills healthy tissue. The analogical source is a story of an army decomposing into small groups to converge on a fortress from multiple directions (avoiding mines that trigger on large forces).

Most computational models extract a propositional causal pattern: "if resource can achieve goal but obstacle blocks it, decompose resource and converge from multiple directions."

Galatea instead transferred the *visuospatial* structure step-by-step — mapping spatial elements (top road → top body part, fortress → tumor) without abstracting a causal pattern. The causality remains implicit but the problem-solving procedure transfers purely through spatial correspondence.


Archytas: Causal Models from Drawings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Archytas** (Patrick Yaner, Georgia Tech) extracted causal/functional models from vector graphics engineering drawings.

Process:

1. Library of known drawings with pre-built hierarchies: line segments → basic shapes → composite shapes (piston, cylinder) → behavioral models → functional specifications
2. New drawing input → generate line segments and arcs
3. Map to closest known drawing via analogical matching
4. Transfer labels up the abstraction hierarchy (shapes → components → behavior → function)

Result: Given a new piston-crankshaft drawing, Archytas assembles a causal model ("linear motion converts to rotational motion") by analogy to known drawings — extracting causal information from visuospatial representations.


Raven's Progressive Matrices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple computational approaches to Raven's test use visuospatial representations:

- Maithilee Kunda's VITA system uses purely visual-spatial representations (no propositional extraction)
- Keith McGreggor's system uses fractal representations

Both achieve good accuracy, demonstrating that analogical/visuospatial representations can support complex reasoning without propositional intermediaries.


Systems Thinking
----------------

The external world consists of **systems** — heterogeneous interacting components whose interactions produce processes at multiple levels of abstraction, some invisible.

Examples:

- Ecosystems: physical, biological, chemical processes interact across scales
- Businesses: manufacturing, marketing, delivery units at individual/team/organization levels

**Systems thinking** = reasoning about invisible properties and complex behaviors of systems; deriving invisible processes from visible structure.


Structure-Behavior-Function Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**SBF models** capture three levels:

- **Structure** — visible components and their connections (e.g., bulb, switch, battery connected in a circuit)
- **Behavior** — invisible causal processes as state transitions (e.g., switch closes → electricity flows from battery to bulb → bulb converts electricity to light)
- **Function** — the purpose/input-output characterization (e.g., "create light": stimulus on switch, 0 lumens → 30 lumens)

Key properties:

- SBF models are *nested* — the flashlight has an SBF model, and the bulb within it has its own SBF model
- They capture multiple levels of abstraction
- They enable diagnosis and design of complex systems by making invisible causal processes explicit


Design Thinking
---------------

**Configuration** (routine design): all components are known; the task is finding an arrangement and assigning variable values. Methods include plan refinement, case-based reasoning, model-based reasoning, rule-based reasoning.

**Creative design** goes beyond configuration — not all parts are known in advance. It involves:

- Problem-solution co-evolution (the problem evolves as the solution evolves)
- Ill-defined, underconstrained, open-ended problems


IDOL: Learning Design Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**IDOL** (Sam Bhatta, Georgia Tech) performed creative design by learning and transferring **design patterns** across domains.

Example:

1. A 1.5V battery circuit produces 10 lumens
2. Goal: produce 20 lumens, but no 3V battery exists
3. Solution: connect two 1.5V batteries in series (cascading pattern)

IDOL extracted the general pattern: *if a design achieves value X via behavior B1, achieve value 2X by replicating B1 through series composition.*

When later given the problem of designing a higher-capacity water pump, IDOL transferred the cascading pattern from electrical circuits — connecting multiple pumps in series. This is analogical transfer of design patterns across domains.


Creativity
----------

Defining creativity (one formulation): producing a **novel**, **unexpected**, **desirable** output.

- **Novelty** = newness (making soufflé for 20 people when you've only made it for 4)
- **Unexpectedness** = surprise (inventing a dramatically different soufflé recipe)

Processes of Creativity
~~~~~~~~~~~~~~~~~~~~~~~

Previously covered in this course:

- **Analogical reasoning** — transferring patterns across domains (water pump from electrical circuits; atomic model from solar system)
- **Explanation-based learning** — creative reuse (using a flower pot as a cup)

Additional processes:

- **Emergence** — drawing three lines produces a triangle; the triangle-ness doesn't belong to any single line and wasn't the intent
- **Re-representation** — when the original representation blocks problem-solving, restructure it (e.g., switching from verbal "revolves/rotates" to spatial diagrams to see the solar-system/atom analogy)
- **Serendipity** — a suspended goal connects with an unrelated discovery (Mestral's Velcro: stuck zipper problem + burrs on dog's legs under microscope)
- **Conceptual combination** — blending two concepts to produce something new


Can AI Be Creative?
~~~~~~~~~~~~~~~~~~~

Arguments against AI creativity (and their rebuttals):

- "Algorithm outputs can't be novel" → Combinations of algorithms for open-ended problems *can* produce novel outputs (e.g., design, scientific discovery)
- "Given same input, output is always the same" → Output depends on input + method + *context/situation*; same input in different contexts yields different outputs
- "If we can trace the process, it's not creative" → Creativity can be defined by the output alone (a black box producing interesting music is creative regardless of whether we understand the process)


AI Ethics
---------

Key ethical questions in AI:

1. **Economy and society** — AI agents replacing human jobs (e.g., assembly robots). Counter: new jobs in designing/maintaining AI. Hard tradeoffs remain.

2. **Military applications** — Drones and robot soldiers. Should we build morality into autonomous weapons? If so, what does this reveal about human morality?

3. **Civil rights for machines** — At what point do AI agents become sufficiently human-like that we must consider their rights? What are the criteria for considering machines equal to humans?

These are open questions without easy answers, increasingly relevant as AI capabilities advance.
