Design Concepts
===============


Definitions
-----------

- **Design** — Deliberative, purposive planning. In software: solving a problem given a set of requirements.
- **Engineering** — Adds science and mathematics (formal methods play a role in software design).
- **Craft** — Skilled occupation built on long experience; more experience with a problem domain yields better designs.
- **Art** — Conscious use of skill, taste, and creative imagination. Aesthetic principles can inform software design.


Programming vs. Software Design
--------------------------------

Two key differences:

- **Scale** — Programming targets hundreds to thousands of lines; software design addresses large systems (e.g., the ISS has 30 million lines of code).
- **Non-functional requirements** — Largely irrelevant in small programs but central to software design, which is fundamentally about managing trade-offs among non-functional constraints.


Software Design
---------------

**Software design** is the process of building a program while satisfying functional requirements and not violating non-functional constraints. It has two phases:

- **Architectural design** — Decomposing the system into components, assigning responsibilities, and defining inter-component interactions.
- **Detail design** — Designing data structures and algorithms within individual components.

Detail design notations include pseudocode, structured programming (sequences, conditions, repetition, sub-procedures), flowcharts, call graphs, and decision tables.

**Design trade-off example:** A weather prediction program using a mesh grid — arrays offer superior performance (hardware-tuned since Fortran), while objects offer flexibility for irregular grid geometries.


Approaches to Software Design
------------------------------

All approaches share three aspects:

1. **Method** — A systematic series of steps suggesting a particular problem view (e.g., OO design views problems as cooperating objects; structured design decomposes by function). The method disciplines how designers organize their thoughts.
2. **Representation** — The notation or diagrams used to express the design.
3. **Validation** — How the design is checked against requirements (typically reviews, inspections, or tool-based checking).

Design issues include:

- Top-down vs. bottom-up vs. inside-out
- Function-first vs. object-first decomposition
- **Conceptual integrity** vs. cooperative development
- Long-term maintainability vs. short-term delivery pressure
- Tool selection


Design Validation
-----------------

Validation is typically done through team reviews, walk-throughs, or inspections. Key issues:

- **Independence** — Design teams may be blind to their own oversights; independent validators improve effectiveness.
- **Method dependence** — Structured design has formal metrics; OO design reviews follow guidelines tied to the modeling approach.
- **Timing** — Continuous (daily/weekly) review vs. milestone-based reviews.

Early detection of design problems is far cheaper than discovering them at delivery time.


Design Documentation
--------------------

Large, complex systems require documentation for long-term maintenance. Traditional elements include component descriptions, responsibilities, data flows, performance considerations, and resource consumption.

**IEEE Standard 1016** adds: designer identity, inter-element dependencies, hidden assumptions, non-functional trade-off rationale, user/technology assumptions, and which architectural views are documented.

The **Leonardo Project** (MCC, 1980s) went further, capturing: stakeholders, design issues and their possible resolutions, design decisions with rationale, version/revision history, constraints, and artifact groupings.

**Design rationale** — the reasons behind design decisions — is critical for downstream maintainers. Capture documentation requirements upfront and record them as the design evolves.


Coupling and Cohesion
---------------------

**Conceptual integrity** is the most important consideration in system design (Brooks, *The Mythical Man-Month*). Descartes similarly observed that works by a single master surpass those composed of many separate parts by different hands.

- **Coupling** — The extent to which two components depend on each other. *Low coupling is good*: changing one module is less likely to require changing others, easing maintenance.
- **Cohesion** — The extent to which a single module has a single purpose. *High cohesion is good*: single-purpose modules are easier to reuse.

Java examples:

- **Packages** reduce coupling — encapsulating names and requiring explicit imports restricts unintended dependencies.
- **Class inheritance** increases coupling — the child depends on parent details, so parent changes can break children.


Information Hiding
------------------

Developed by **David Parnas**: encapsulate a module's capabilities behind an abstract interface. Clients depend only on the interface, giving freedom to change implementation details without breaking them.

Good candidates for information hiding: hardware device access, database/server access, algorithm specifics, and data structure implementations.


Abstraction and Refinement
--------------------------

All design methods support abstraction (managing complexity by thinking at higher levels) and refinement (elaborating abstractions into implementations). Language mechanisms supporting abstraction include:

- Specification (what vs. how)
- Aggregation constructs (arrays, structs, objects)
- Class hierarchies and generalization
- Parameterized procedures/functions
- Non-determinism at the specification level


Aesthetics in Design
--------------------

**Aquinas** resolved beauty into *wholeness, harmony, and radiance* — in software terms: completeness, consistency, and conceptual integrity.

**Pascal** apologized for writing a long letter because he lacked the time to write a short one — elegant, simple-looking solutions that satisfy complex requirements demand significant time and energy.


Design Philosophy
-----------------

Four philosophical perspectives on software design (per Danish researcher Piet Hein):

- **Descartes** — Analytic thinking; maps to the analysis phase of software design.
- **Marx** — Social processes; understanding the social context and involving users in design.
- **Heidegger** — Tools; IDEs and CASE tools automating the development process.
- **Wittgenstein** — Language games; inventing vocabulary to think about problems (e.g., the desktop metaphor, client-server, icons, firewalls).

Design is the most creative part of software development. System quality depends heavily on the design produced, and design quality correlates strongly with the team's experience on similar projects.
