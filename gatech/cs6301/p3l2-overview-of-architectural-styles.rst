.. title: Overview of Architectural Styles
.. slug: Overview of Architectural Styles
.. date: 2016-05-27 23:49:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Overview of Architectural Styles
================================


Introduction
------------

Software architecture is the highest level of expression of a design problem. In practice it often amounts to a **box-and-arrow diagram** depicting major components and their dependencies (control flow, data flow). This lesson takes a more principled look at what architecture entails.


Informal Definition
-------------------

Software architecture is the **organization of a system into component subsystems or modules**. It is almost universally done in layers — from an abstract top-level decomposition down to implementable units. Architects often employ **stereotypical architectural styles** to guide the decomposition.


Analysis Models vs. Architecture
---------------------------------

When determining components solely from an analysis model:

- **True:** Analysis models adapt well to changing customer requirements (constructed before design, not constrained by it)
- **False:** Analysis models should represent the design approach (mixing analysis and design biases the solution)
- **True:** Analysis models are resilient to hardware changes (no assumptions about running environment)
- **False:** Analysis models include all required components (utility/collection classes are added during design)


Definitions of Software Architecture
-------------------------------------

**Unified Software Process (USP):** Architecture is a set of **decisions** about structural elements, their interfaces, collaborations, and composition into subsystems — guided by architectural styles. Decisions also address usage, performance, comprehensibility, economics, technology constraints, trade-offs, and aesthetics.

**Perry & Wolf:** Architecture = **elements + forms + rationale** (rationale = decisions and reasons behind them).

**IEEE:** Architecture involves the **fundamental organization, components, and relationships** of a system.

**Parnas/Verhoff:** Components should be determined by **hiding away what is hardest to change**, reducing downstream maintenance cost.

**Garlan & Shaw** (primary framework for this lesson):

- **Component** — computational or data element + its interfaces (**ports**). Ports express what the component *requires* and *provides*.
- **Connector** — communication **protocol** among components. Defines who speaks, in what order, what information passes, and error handling. May have code to enforce the protocol.
- **Configuration** — the **topology** of components wired together via connectors (plugging ports into connector ends).


Components
----------

- **Taylor:** A software component is an architectural entity concerned with a unit of functionality or data, defined by its interfaces and its required execution context.
- **Szyperski:** A component is a **unit of composition** with contractually specified, explicit, checkable, and enforceable interfaces.

**Selecting components** — factors beyond required functionality:

- Existing **reusable components** from libraries
- **Physical machine architecture** (e.g., multi-core opportunities)
- **Staff structure** — Conway's Law: system structure mirrors organization structure
- **System lifetime trajectory** — anticipated evolution should influence decomposition


APIs
----

A component's **Application Programming Interface (API)** specifies names, methods, argument types, return types. It can be expressed as:

- A **language binding** (in a specific programming language)
- A higher-level abstraction (e.g., OCL)
- An **Architectural Description Language (ADL)**


Connectors
----------

**Taylor:** A connector is an architectural element tasked with effecting and regulating interactions among components. Its key characteristic is the **protocol** it defines.

**Example — Procedure Call & Return:**

- Two messages: call (with typed parameters) and return (with typed value)
- **Asymmetric** relationship (caller/callee)
- **Synchronous** — caller blocks until callee returns


Configuration
-------------

A configuration is a set of specific associations between components and connectors — the wiring of the system. It defines the overall topology.


Terminology
-----------

- **Conceptual architecture** — high-level, early-stage architecture produced before complete requirements; used to begin planning (team structure, schedule estimation)
- **As-Intended vs. As-Built architecture** — the planned architecture vs. what is actually constructed
- **Architectural drift** — divergence of As-Built from As-Intended during development (e.g., incorporating an available component that doesn't perfectly match the plan)
- **Architectural erosion** — divergence during **maintenance** phase, often from time-pressured fixes that don't update architectural documentation


Architectural Styles
--------------------

An **architectural style** is a named collection of design decisions appropriate in particular circumstances. It constrains possible components and interactions and provides benefits such as:

- **Encoded experience** — known solutions, known pitfalls
- **Standards** (reference architectures) supporting validation
- **Reuse** of standard components (e.g., database servers for client-server)
- **Process guidance** — team organization, development steps, validation timing

**Example:** Client-server — physically separated components; requesters (clients) ask service providers (servers). Servers are unaware of client identities; clients are isolated from each other; multiple servers can scale dynamically.


Catalog of Architectural Styles
-------------------------------

- **Abstract Data Type (ADT)** — components organized around hidden data structures
- **Batch Sequential** — sequential processing stages
- **Blackboard** — components post results/requests to a shared repository; others react
- **Big Ball of Mud** — absence of architecture (often from erosion or no design process)
- **Client-Server** — service requesters and providers, typically over a network
- **Component-Based** — pluggable, independently deployable components
- **Coroutines** — symmetric calling (A calls B, B resumes where it left off); useful for interleaved streams (e.g., formatted printing)
- **Data-Centric** — stored database procedures (e.g., SQL + custom functions)
- **Domain-Driven Design** — architecture follows domain vocabulary and update patterns (e.g., tax preparation software)
- **Implicit Invocation** — event-based registration/broadcast (publish-subscribe)
- **Layered** — each layer is a virtual machine providing capabilities to layers above
- **Master Control** — historically the first pervasive style; top-level routine orchestrates lower-level routines
- **Message Bus** — asynchronous message passing over a common data channel
- **Mobile Code** — remote evaluation, agents on network nodes (mobile/smartphone constraints)
- **Object-Oriented (architectural)** — objects with independent threads, sending asynchronous messages to cooperate
- **Peer-to-Peer** — equal parties sharing responsibility for services
- **Plug-in** — extensibility via a registry of additional functionality (e.g., Eclipse)
- **Pipe and Filter** — chain of filters connected by pipes; each filter transforms its input
- **Process Control** — feedback loop controlling an ongoing hardware process (e.g., cruise control, nuclear reactor)
- **Production Systems** — collection of rules with firing conditions (from AI); no clear control flow
- **REST** — representational state transfer; stateless HTTP-based client-server with caching
- **Service-Oriented Architecture (SOA)** — self-contained services for enterprise applications, typically internet-connected
- **Shared Nothing** — distributed database with no sharing across nodes
- **State-Transition Systems** — event-driven reactive systems (GUIs, real-time systems)
- **Shared Memory** — components share a common memory space
- **Table-Driven Interpreter** — requests as expressions in a language; parsed and dispatched by an interpreter


Style Issues
------------

- **Heterogeneous systems** — real systems often require **multiple styles** (e.g., client-server + GUI event-driven + layered)
- **Domain-Specific Software Architecture (DSSA)** / **Reference Architecture** — a shared architecture for a family of related systems (e.g., variants of military aircraft control systems); describes commonality, with per-variant extensions
- **Semantics** — precise definitions of styles are needed to enable reuse and tool support


Architecture Description Languages
-----------------------------------

**ADLs** are formal notations for describing architectures, providing precision beyond diagrams. They enable tool support:

- **Diagramming** with structural checking
- **Analysis** of structural and behavioral properties
- **Simulation**

Notable ADLs include **Acme**, Wright, Rapide, Darwin, and UniCon.


Architectural Evaluation
-------------------------

Early detection of architectural problems is critical because mistakes are costly to fix later.

**Architecture Review Boards:** Stakeholders (especially development teams) periodically evaluate proposed changes and their impacts across the system.

**SAAM (Software Architecture Assessment Method):**

1. Generate the architecture and usage **scenarios**
2. Walk through each scenario to determine which architectural elements are affected
3. Compare alternative proposals by impact
4. Select the solution with least negative impact

**ATAM (Architecture Tradeoff Analysis Method):** A more formal evaluation method developed at the Software Engineering Institute; systematically analyzes trade-offs among quality attributes.


Summary
-------

Software architecture aims to produce high-quality systems at reduced cost through **early detection of problems**. Key principles:

- Explicit recognition of issues and rationale for decisions
- Leverage existing assets and reusable components
- Construct architecture at a sufficient level of **abstraction** to communicate effectively to all stakeholders
