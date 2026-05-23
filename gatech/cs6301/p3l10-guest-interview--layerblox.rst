Guest Interview- LayerBlox
==========================


Background
----------

Guest: a Georgia Tech CS PhD (software architecture, software engineering, UI design), former Michigan State faculty (12 years, formal modeling of software architecture), then ~6 years at **LogicBlox** — a company specializing in smart databases that applies modeling and formal methods ideas in practice.

LogicBlox uses an **agile process** with short iterations (1–2 week cycles), demos at iteration end, and Jira for issue tracking. New projects start with an **architectural assessment** (~1 month of prototyping and scalability analysis), then scale up developers gradually.


LayerBlox
---------

**LayerBlox** is a **software generator** for producing different variants of products in the same **product line**.

Core concepts:

- Each variant is a different program in the same product line
- Product lines are organized around **reusable features** stored in a library
- Features are designed with a composability idiom — write once, reuse many times
- To generate a variant, write an **assembly specification** describing how features compose

Key properties:

- Assembly specifications make it easy to **compare variants** — see exactly how two variants are common and how they differ
- The generated components have a **layered, hierarchical** structure (hence the name "LayerBlox")
- Related to **layered architectures**: each layer is understood via its exported interface, independent of implementation or layers beneath it
- Layering and tiering are **independent** — generated code can go in any tier (middle tier, data tier, etc.)


Feature-Based Design
--------------------

- Decomposition and design are organized **by feature** (as in feature diagrams/feature modeling)
- Feature analysis identifies the different features that compose into a capability (e.g., forecasting)
- Features may be implementation-centric rather than customer-visible
- Feature-based design produces **small, highly reusable fragments** that are composable into different application variants


Assembly Specifications
-----------------------

An assembly specification describes one variant. It defines:

- **Components** — the programs being generated (e.g., a batch forecaster ``batch``, with sub-components like ``bFcst`` (baseline forecaster), ``mults`` (multipliers), ``iFcst`` (incremental forecaster))
- **Interfaces** — similar to Java interfaces; declare signatures that many different implementations can satisfy; represent abstract programs with specified table structures/calculations
- **Refinements** — generators that produce different implementations of an interface; each refinement fills in details differently

Different assembly specifications produce **different variants** (different components) that can coexist in the system.


Supporting Tools
----------------

Built on top of the code generator:

- **Graphical visualization** tool (dot-format graphs) showing dependencies and refinement composition — useful for tracking design simplification over time
- **Code metrics** tracking refinement size — over time, large refinements break into compositions of smaller ones; metrics identify candidates for proactive decomposition


Lessons Learned
---------------

- Product line generation (rooted in early 1990s software engineering) is effective for managing **many similar-but-different customer deployments**
- Feature-based decomposition with composable refinements enables high reuse
- Assembly specifications provide **precise, comparable** descriptions of product variants
- Visualization and metrics support ongoing design improvement
