.. title: P3L5 Non-Functional Reqs & Arch Styles 
.. slug: P3L5 Non-Functional Reqs & Arch Styles 
.. date: 2016-05-27 23:52:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P3L5 Non-Functional Reqs & Arch Styles
=======================================


Introduction
------------

Software architecture prescribes the high-level structure of a system. Beyond functionality, the system must satisfy a set of possibly **conflicting non-functional requirements** (NFRs). These qualities are often **crosscutting** — their implementation is spread across the entire system, strongly affecting overall structure. Material drawn from Bosch.


Functional vs. Non-Functional Requirements
-------------------------------------------

=====  ============================================  ====
Req    Description                                   Type
=====  ============================================  ====
1      Check for illegal moves                       **F** (part of system computation)
2      Respond to moves within 5 seconds             **NF** (quality of computation)
3      Must be written in Java                        **NF** (platform constraint)
4      Allow human to choose X or O as marker         **F** (part of what system computes)
=====  ============================================  ====


Quality Catalog
---------------

Performance
~~~~~~~~~~~

**Definition (SEI):** The attribute characterizing the **timeliness** of services delivered.

**Measures:** Response time, throughput, capacity, utilization.

**Devices:** Caching, concurrency, memory management.

**Example application:** Weather prediction (finer grid = better predictions = more computation).

Maintainability
~~~~~~~~~~~~~~~

**Definition:** The extent to which enhancements can be **readily added**. Also called evolvability, flexibility, adaptability.

**Measures:** Coupling, cohesion.

**Devices:** Encapsulation, published interfaces, sub-classing, indirection, wrapping.

**Example application:** Twitter API (stability enables dependent applications).

Reliability
~~~~~~~~~~~

**Definition:** The likelihood of system failure in a given time period — **continuity of service**.

**Measures:** Mean Time To Failure (MTTF).

**Devices:** Redundancy, fault tolerance, recovery blocks.

**Example application:** Traffic light controllers.

Safety
~~~~~~

**Definition:** The extent to which a system protects against **injury, loss of life, or property damage**.

**Measures:** System complexity, time coupling, fault tree analysis.

**Devices:** Hardware interlocks, fault containment strategies.

**Example application:** Cruise control software.

Security
~~~~~~~~

**Definition:** The extent to which a system protects against **unauthorized intrusion** or provides confidentiality.

**Measures:** Security levels (confidential, top secret); formal proofs.

**Devices:** Authentication, authorization, security kernels, encryption, auditing/logging, access control.

**Example application:** Online banking.


Architectural Styles Reviewed
------------------------------

Five styles examined against the five qualities:

- **Pipe and Filter** — chain of filters; output of each becomes input to the next
- **Layered** — functionality grouped into vertically stacked layers with explicit, loosely coupled communication
- **Blackboard** — common knowledge base iteratively updated by specialist knowledge sources
- **Object-Oriented** — individual reusable, self-sufficient objects with encapsulated data and behavior
- **Implicit Invocation** — components broadcast events; others register interest and are called back when events occur


Quality × Style Matrix
-----------------------

Pipe and Filter
~~~~~~~~~~~~~~~

- **Performance:** (+) Filters can run in parallel, improving throughput. (−) Individual filters may block waiting for input; single-processor overhead from context switching.
- **Maintainability:** (+) Each filter is independent → good encapsulation and reuse. (−) Data format changes affect all filters → increased coupling.
- **Reliability:** (−) Weakest-link problem — any broken filter/pipe breaks the whole pipeline.
- **Safety:** (−) Multiple dependencies reduce safety. (+) Single output source is easier to verify.
- **Security:** (+) Simple architecture increases opportunities for authentication, encryption, and security levels.

Layered
~~~~~~~

- **Performance:** (−) Events must pass up/down layers → overhead and context swapping.
- **Maintainability:** (+) Stable interlayer protocols → well-defined, reusable components; possible to replace or insert entire layers.
- **Reliability:** (−) Events handled across multiple layers make fault isolation harder. (+) Higher layers can provide oversight/redundancy.
- **Safety:** (+) Easy to insert safety monitoring layers.
- **Security:** (+) Straightforward to add a security layer between system and environment.

Blackboard
~~~~~~~~~~

- **Performance:** (−) Lack of well-defined control flow → redundant/polling behavior.
- **Maintainability:** (+) Independent components → flexibility. (−) Changes to control paradigm or repository format have pervasive effects.
- **Reliability:** (+) Component independence → system can degrade gracefully. (−) No overall behavior definition → hard to diagnose problems.
- **Safety:** (−) Common repository can spread bad data to all components.
- **Security:** (+) Common repository enables centralized access control. (−) Dynamic addition of components reduces confidence in security.

Object-Oriented
~~~~~~~~~~~~~~~~

- **Performance:** (−) Many small objects → context switching; delegation → indirection overhead.
- **Maintainability:** (+) Encapsulated data + message passing → independence. (−) Object references create inter-component dependencies.
- **Reliability:** (−) Decentralized control → reduced oversight. (+) Encapsulation reduces unintended interactions.
- **Safety:** (+) Correspondence between real-world entities and objects improves intentionality and accountability.
- **Security:** (+) Encapsulation reduces vulnerability. (−) Many small objects → fragmentation (more attack points); unconstrained message passing can spread problems.

Implicit Invocation
~~~~~~~~~~~~~~~~~~~

- **Performance:** (−) Extra communication overhead from bookkeeping and indirection → context swapping.
- **Maintainability:** (+) Component independence → increased reuse.
- **Reliability:** (+) Centralized event delivery can handle unexpected events. (−) Implicit interactions reduce system understandability.
- **Safety:** (−) Interaction complexity makes safety harder to ensure.
- **Security:** (−) Fragmentation from many independent components. (+) Encapsulation mitigates some risks.


Negative Side Effects
---------------------

**By architectural style:**

=======================  ==========================================
Style                    Primary negative side effect
=======================  ==========================================
Pipe and Filter          **Increased coupling** (data format changes affect all filters)
Blackboard               **Spread of bad data** (contaminated repository affects all components)
Object-Oriented          **Increased system fragmentation** (many small independent objects)
Implicit Invocation      **Reduced system understanding** (servers unaware of dynamically changing clients)
=======================  ==========================================

**By non-functional requirement:**

=======================  ==========================================
NFR                      Primary negative side effect
=======================  ==========================================
Reusability              **Increased fragmentation** (high cohesion → more modules → more connections)
Performance              **Reduced understanding** (special cases and arcane data structures)
Security                 **Increased coupling** (centralized data access control couples all modules)
Reliability              **Compromised delivery schedule** (extra checking/documentation code)
=======================  ==========================================


Summary
-------

Non-functional qualities can **dramatically affect** system architecture. Real-world systems have multiple conflicting NFRs requiring trade-offs. For each quality requirement, consider both its **positive and negative impacts** on the overall architecture when selecting and combining architectural styles.
