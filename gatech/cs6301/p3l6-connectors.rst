Connectors
==========

Overview
--------

Connectors are responsible for **mediating interactions among components** (Shaw & Garlan). They establish rules governing component interaction and specify auxiliary mechanisms required. Material drawn primarily from the Mehta et al. paper.

Atomic Elements
---------------

Connectors are built from atomic elements:

- **Ducts** — the base channel with no associated behavior (e.g., internet connections, OS system calls, sockets, programming language VMs). Ducts transmit data and control information among components.
- **Protocols** — the sequence of interactions layered on top of ducts.
- **Internal mechanisms** — storage (e.g., buffers) or computational elements (e.g., translation capabilities).

In pipe-and-filter style: **pipes** are the connectors, **filters** are the components.

Service Categories
------------------

Mehta et al. define four **service categories** representing the broad interaction role a connector fulfills:

- **Communication (T)** — transmittal of data
- **Coordination (O)** — transfer of control
- **Conversion (X)** — translation, particularly among data formats
- **Facilitation (F)** — mediation or optimization activity

Examples of category assignments:

- Data buffering → **F**
- Acknowledgement, guaranteed delivery, multiplexing, transactions, scheduling, synchronization → **O**
- Invocation → **O + T** (control and parameter data)
- Dynamic reconfiguration, load balancing → **F**

Procedure Call Connectors
-------------------------

The most pervasive connector, provided by all programming languages:

- **Coordination** role: flow of control from caller to callee
- **Communication** role: data transmission via parameters
- Basis for all composite connectors (e.g., Java method calls have fan-in = 1, fan-out = 1)

Variations:

- **Parameter passing**: call by reference, value, name; default values; keyword/inline parameters
- **Return values**: invocation records, hash tables
- **Evaluation order**: left-to-right, right-to-left, unspecified
- **Entry points**: single vs. multiple
- **Invocation**: explicit (method call) vs. implicit (delegation)
- **Synchrony**: synchronous (typical) or asynchronous
- **Fan-in/fan-out**: one-to-one or many
- **Accessibility**: private, protected, public

Event Connectors
----------------

Responsible for **coordination** (flow of control) and optionally **communication** (passing timestamps, data):

- Detect events or event combinations, then generate messages/method calls
- Particularly relevant for **distributed, asynchronous applications**
- The set of active event connectors is **dynamic** — the application can enable/disable event detection at runtime

Variations:

- **Cardinality**: number of producers, observers, event patterns
- **Delivery**: best effort, exactly once, at most once, at least once
- **Priority**: outgoing vs. incoming, embedded priorities
- **Synchrony**: synchronous, asynchronous, timeout-based
- **Notification**: polled, publish-subscribe, central registry, queues
- **Causality**: absolute vs. conditional/relative events
- **Source**: hardware (page faults, interrupts, traps) or software (signals, triggers, GUI input)

Data Access Connectors
----------------------

Responsible for access to data repositories:

- **Communication** service: data transfer
- **Conversion** service: character set translation, higher-level transformations

Variations:

- **Locality**: thread-specific, processor-specific, or global
- **Access type**: query/retrieval only, or read-write
- **Availability**: transient vs. persistent
- **Accessibility**: private, protected, public
- **Lifecycle**: who constructs and who destructs
- **Cardinality**: who defines messages, who receives them

Linkage Connectors
------------------

Describe the **structure** of a system — establishing ducts and enforcing interaction semantics:

- Provide a **facilitation** service
- May disappear after system setup is complete
- Unit of linkage: module, file, or object
- Related tools: configuration management, ``make``

Variations:

- **Implicit vs. explicit**: e.g., ``make`` infers build steps vs. explicit linking
- **Granularity**: variables, procedures, functions
- **Binding time**: compile time, run time, or pre-compile (templates/generics)
- **Semantics/cardinality**: defines/uses, provides/requires

Stream Connectors
-----------------

Primarily concerned with **data transfer** (communication service). Common examples: pipes, TCP sockets, proprietary client-server protocols.

Variations:

- **Delivery guarantees**
- **Bounded vs. unbounded**; buffering capability
- **Transmission units**: bytes vs. structured data
- **Stateful vs. stateless**
- **Named vs. unnamed**
- **Locality**: local vs. remote
- **Synchrony**: synchronous, asynchronous, timed
- **Structure**: raw vs. structured
- **Cardinality**: one-to-one, one-to-many, many-to-many

Arbitrator Connectors
---------------------

Primarily **facilitation** with **coordination** (control redirection):

- Negotiate service levels, support reliability and atomicity
- Handle scheduling, load balancing, fault trapping, synchronization

Variations:

- **Fault handling**: single decision vs. voting scheme (majority rules)
- **Concurrency mechanism**: semaphores, rendezvous, monitors, locks; lightweight vs. heavyweight
- **Transactions**: simple vs. nested; optional vs. required
- **Access**: reads, writes, or both
- **Security**: authentication, authorization, screening, durability (single vs. multi-session)
- **Scheduling** of arbitrator activities

Adaptor Connectors
------------------

Put together **components not originally designed to interoperate** — often involving translation:

- Provide **conversion/transformation** services

Variations:

- **Invocation conversion**: address mapping, marshalling, virtual memory translation, virtual function tables
- **Wrappers/packagers**
- **Protocol conversion**
- **Presentation conversion**: e.g., XSLT-driven output transformation

Distributor Connectors
----------------------

Primarily **facilitation** — identify interaction paths and route among them, assisting other connectors. Primary example: **DNS** (Domain Name Services).

Variations:

- **Naming**: structured (hierarchical or flat) vs. attribute-based
- **Delivery policy**: best effort, exactly once, etc.
- **Mechanism**: unicast, multicast, broadcast
- **Routing**: bounded list vs. ad hoc; static, cached, or dynamic paths

Composite Connectors
--------------------

Simple connectors can be composed into more complex ones:

1. **Science data server** — combines event, data access, stream, and distributor connectors. Supports synchronous/asynchronous clients, multiple producers/consumers, data transformation, public/private access, persistent/transient data, naming registry.

2. **FTP applications** (Globus, bbFTP, GridFTP) — combine procedure call, data access, stream, and distributor connectors. Typically synchronous, use web protocols (SOAP), involve authentication, exactly-once delivery, bounded buffering, unicast.

3. **Client-server distribution** (REST, HTTP, CORBA, FTP, SOAP) — combine procedure call, data access, stream, and distributor connectors. Involve remote invocation, named parameters, naming registry, unicast.

4. **Peer-to-peer data distribution** (BitTorrent) — combine arbitrator, data access, stream, and distributor connectors. Feature control flow redirection, protocol negotiation, scheduling, voting, at-least-once delivery semantics.

Connector Design
----------------

Design process:

1. Determine components and required interactions from the architecture
2. For each interaction, determine required services
3. Select a connector type providing those services
4. Choose among the type's variation dimensions
5. Define the connector
6. **Validate** using rules (see below)
7. Define a custom connector if no existing one fits

Validation Rules
----------------

Rules constrain combinations of connector dimension values:

- **Requirements**: one dimension's value requires certain values on another (e.g., event connectors with delivery notification require cardinality, synchronization, and mode rules)
- **Cautions**: certain combinations may be unstable/unreliable under specific concurrency or locality conditions
- **Restrictions**: certain combinations are invalid (e.g., pass-by-name + transient)
- **Prohibitions**: total incompatibility (e.g., streams + atomicity)

Linux Case Study
----------------

The Mehta paper's case study examines Linux as a provider of higher-order connectors:

- **File system** — a composite facade connector providing arbitration, adaptation, and coordination over raw bytes; handles contention and synchronization
- **Shared memory** — a data-access connector with synchronization concerns
- **Process scheduling** — an arbitrator connector controlling access to resources

Summary
-------

Determining how components correctly interact is as vital as determining the components themselves. Treating connectors as **first-class design elements** — understanding their types, services, variations, and composition — strengthens the overall architecture.
