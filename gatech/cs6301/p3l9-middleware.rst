Middleware
==========


Distributed Systems Architecture
---------------------------------

This lesson focuses on architectures for **heterogeneous distributed systems** — multiple, potentially different computers collaborating to provide an application. A classic example is a client-server insurance system: web browsers on agent laptops → web server running business logic → database storing policy data.

**Middleware** is the collection of technologies between client and server that address **non-functional constraints** of the distributed system. Middleware is conceptually similar to architectural connectors. Material drawn from the Emmerich paper.


Context
-------

The Internet has driven explosive growth in distributed applications, bringing:

- More customers, heavier loads, increasing resource demands → **performance and resource concerns**
- Specialized hardware (ATMs, card readers, mobile phones, Square readers) → **device heterogeneity**
- Increasingly powerful applications requiring **integration** of existing components


Characteristic Issues
---------------------

Five major categories of issues in distributed systems:

1. Network communication
2. Coordination
3. Reliability
4. Scalability
5. Heterogeneity


Network Communication
~~~~~~~~~~~~~~~~~~~~~

Key concerns when applications span a network:

- **Error handling**: synchronous errors (request-response) vs. asynchronous errors (spontaneous notifications)
- **Reliable delivery**: strategies like retransmission risk duplicate processing
- **Data representation**: heterogeneous machines may represent data differently
- **Transactions**: concurrent readers/writers on shared databases risk inconsistency


Data Transportability
~~~~~~~~~~~~~~~~~~~~~

Also called serialization (Java), marshalling, or pickling. Differences to resolve:

- Bit order, byte order, character sets, alignment, word length (32-bit vs. 64-bit)
- Organization of complex data structures; compaction
- **Self-describing data**: data accompanied by its own schema

Standards: Internet standard x680, Google **Protocol Buffers**.


ACID Transactions
~~~~~~~~~~~~~~~~~

For reliable database access with multiple concurrent readers/writers:

- **Atomic** — the transaction's steps are treated as a single indivisible unit
- **Consistent** — database integrity constraints hold before and after
- **Isolated** — intermediate states invisible to other transactions
- **Durable** — committed transactions are permanently persisted

Not always required — e.g., a voting app where approximate vote counts are acceptable may skip ACID for performance.


Coordination
~~~~~~~~~~~~

Synchronization between distributed components:

- **Synchronous** — sender blocks until response arrives; often clocked
- **Asynchronous** — sender continues after sending; notified on response; more general but harder to reason about

Design decisions:

- **Push vs. pull**: server pushes updates to clients, or clients pull on demand
- **Robustness**: handling component failures (timeouts, acknowledgements)
- **Availability**: 24/7 vs. scheduled maintenance; handling load
- **Persistence**: database vs. file system for server state
- **Concurrency**: handling multiple simultaneous clients; transaction integrity


Reliability
~~~~~~~~~~~

Percentage of time the application provides expected services. Typical failure mode: undelivered/unacknowledged messages.

Strategies and their trade-offs:

- **Best effort** — send and hope
- **At most once** — prevent duplicates
- **At least once** — guarantee delivery, risk duplicates
- **Exactly once** — ideal but most expensive

Classic **reliability-performance trade-off**: replication improves reliability but costs time and resources.


Scalability
~~~~~~~~~~~

How easily the application grows (more users, greater load). Scaling typically means adding hardware. The key question: to what extent does adding machines change the architecture?

**Transparency** types:

- **Access transparency** — application doesn't need to know if a resource is local or remote
- **Location transparency** — physical location of resources is hidden
- **Migration transparency** — resources can move between machines without affecting the system
- **Replication transparency** — data replication is invisible to the application


Heterogeneity
~~~~~~~~~~~~~

Dimensions of heterogeneity: hardware (including embedded devices, phones), operating systems, programming languages, standards/protocols/APIs, browser families and versions.

Approaches to managing heterogeneity:

- **Standard APIs** from W3C, OMG, ANSI, ISO — must address backward and forward compatibility
- **Normative architectures** — e.g., OMG's **Model-Driven Architecture (MDA)** separating machine-independent from machine-dependent parts
- **Vendor platforms** — JEE (Oracle/Sun), .NET (Microsoft), WebSphere (IBM)
- **LAMP stack** — Linux (OS), Apache (web server), MySQL (database), PHP (server-side scripting)


Kinds of Middleware
-------------------

Four categories based on interaction mechanism:

Transactional Middleware
~~~~~~~~~~~~~~~~~~~~~~~~~

Handles distributed transactions with ACID guarantees. Uses policies like **two-phase commit** for reliability and consistency. Provides **location transparency**. Examples: CICS (IBM), Tuxedo (UNIX), Encina (HP).

Message-Oriented Middleware (MOM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on **asynchronous message passing** with message queues. Provides fault tolerance (queued messages survive component failures). Not particularly transparent — clients must implement coordination embedded in messages. Examples: IBM MQSeries, Sun Java Message Queues, Amazon queuing solutions.

Procedural Middleware
~~~~~~~~~~~~~~~~~~~~~~

**Remote Procedure Calls (RPC)** — make remote computation look like a local function call. Typically synchronous and OS-dependent. Available since the 1980s. Technologies: SUN RPC, NDR for data representation.

Object/Component Middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extension of RPC to remote objects — send messages to objects on remote machines. Issues include **object identity** (memory addresses not globally unique) and **cross-machine inheritance/delegation**. Provides synchronous and asynchronous messaging, marshalling, exception handling. Examples: CORBA, COM (Microsoft), Java RMI (Oracle).


Software Engineering Issues
----------------------------

- **Requirements**: non-functional requirements dominate; must be elicited from customers who may be uncertain about QoS needs
- **Architecture**: choosing connectors that map to available middleware solutions
- **Design**:

  - **Latency** — network delays require timeouts and retransmission protocols
  - **Statefulness** — web applications are often stateless; persistent state via databases or cookies
  - **Concurrency** — synchronization to avoid deadlock and ensure liveness

- **Service discovery**: naming/White Pages (URLs, IP addresses) vs. Yellow Pages (capability-based lookup, e.g., UDDI)
- **Reflection and meta-object protocols**: self-describing programs and data
- **Data representations**: relational databases vs. NoSQL for different application needs
- **Fat vs. thin clients**: trade-off between client-side functionality and simplicity (AJAX enables selective page updates without full round-trips)
- **Device constraints**: power, memory, processing limitations on mobile/embedded devices
- **Mobility**: handling intermittent connectivity


Web Services
------------

Software systems supporting **machine-to-machine interaction** over the web using agreed-upon APIs and standards:

- **Data protocols**: XML, SOAP, RDF, OWL, JSON
- **Service description**: **WSDL** (Web Services Description Language) — enables code generation
- **Discovery**: **UDDI** (Universal Description, Discovery and Integration) — Yellow Pages for services

Example platform: **J2EE** — web browser (HTML/applets) ↔ web server + EJB containers (business logic) ↔ database services.


Service-Oriented Architecture (SOA)
------------------------------------

An architectural style for creating and using **self-contained, self-defined, modular** services throughout their lifecycle.

Characteristics:

- Each service is a **meaningful vertical slice** of functionality
- Services are **stateless** (simpler code), **flexible** (composable), and **middleware-transparent**
- Architect decomposes functionality into a suite of sub-services that compose into user-facing services
- Services are published, located, and dynamically invoked

**Re-architecting risk**: converting legacy mainframe applications to SOA involves switching from control-driven to reactive/event-driven models — a major and costly transformation with significant risk.


Summary
-------

Middleware is a collection of technologies (APIs, protocols, tools, design patterns) for addressing **non-functional constraints** in heterogeneous distributed applications. As the Internet grows, standard middleware solutions become increasingly important.
