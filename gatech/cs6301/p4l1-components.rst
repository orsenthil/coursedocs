Components
==========


Bottom-Up Design
-----------------

In contrast to top-down design (requirements → architecture → refinement), this lesson focuses on **bottom-up design**: starting with self-contained pieces called **components** and composing them into systems.

**Component** (Szyperski's definition): an executable unit of independent production, acquisition, and deployment that can be composed into a functioning subsystem.

Note: this usage of "component" differs from the architectural sense used in earlier lessons.


Buy vs. Build
--------------

A key industrial decision: acquire software assets externally or construct them in-house?

**Buying** (third-party component):

- **−** Reduced competitive uniqueness (competitors can buy the same component)
- **+** Less staff time required
- **+** Lower production costs (vendor's economies of scale)
- **−** Less control of development process

**Building** (in-house):

- Mirrors buying trade-offs: potentially higher cost, but tailored to needs
- Retain intellectual property control
- Increased delivery risk

**The Third Way** (Szyperski): use third-party components that you **customize during assembly** — combining the risk/cost reduction of buying with the flexibility of building.

Other third-party resource models: **software libraries** (PThreads), **cloud-based services** (NIST Time Service), **turn-key equipment** (TomTom GPS), **IDE plugins** (Checkstyle), **open source** (PHP).


Component Characteristics
--------------------------

- **Pre-existing and general** — reusable across contexts
- **Low manufacturing cost** — just copy
- **Configurable** — tailored to needs and target environment
- **Composable** — with other components and non-component code
- **Conform to a component model** prescribing syntax, semantics, and composition


Component Life Cycle
--------------------

Three phases (vs. the usual two of development/runtime):

1. **Design time** — components are specified and built
2. **Deployment time** — binaries are configured and deployed into the target execution environment
3. **Runtime** — components are instantiated and executed

Major differences between component technologies depend on **when composition occurs** and whether a component **repository** exists.


Component Models
-----------------

A **component model** (or framework) is a set of shared assumptions about:

- **Syntax** — how components are specified (may differ from implementation language)
- **Semantics** — what's in the component's contract; the execution environment
- **Composition** — how components work together

Example (WordPress plugins): "output appears at invocation location" = semantics; "use well-structured PHP and valid HTML" = syntax; "actions triggered by WordPress events, hooked via PHP" = composition.

Prominent component models:

- **Oracle/Sun**: EJB, J2EE, JSP
- **Microsoft**: COM, DCOM, OLE, ActiveX, COM+, .NET (CLI, CLR, ASP.NET)
- **OMG**: CORBA/CCM with OMA and IDL
- **Web Services**: WSDL, UDDI, SOAP


Component Issues
-----------------

Configuration
~~~~~~~~~~~~~~

Components are typically configurable (e.g., via configuration files), giving designers flexibility for trade-offs like space vs. time. Cost: configuration is **late binding**, making unit testing in actual usage environments difficult, and increasing documentation/deployment overhead.

Versioning
~~~~~~~~~~~

As new versions are released, **backward compatibility** is a persistent problem. Customers resist upgrades that risk breaking working systems. Multiple components with independent versions create a **combinatorial explosion** of configurations to support.

Versioning strategies: version numbers with compatibility checks, ad hoc compatibility rules, immutable interfaces, guaranteed backward compatibility, sliding windows of supported versions, breaking compatibility only on major releases.

Extensions
~~~~~~~~~~~

Adding features to components raises complications:

- **Singleton extensions** — only one instance allowed
- **Parallel extensions** — same feature across multiple components risks resource contention
- **Non-orthogonal extensions** — feature interactions when multiple features are configured simultaneously
- **Recursive extensions** — extensible components that can themselves be extended (vendor loses deployment control)

Callbacks
~~~~~~~~~~

A **callback** is a client operation invoked by the component when a specified event is detected.

**Advantage**: component provides a structured calling regime (e.g., event loop) that orchestrates operation order.

**Danger**: during callback execution, the component has yielded control to the client. The client may make calls that **break the component's invariants** (e.g., calling back into the component while its state is inconsistent). This vulnerability window exists from the moment the callback begins until the client returns control.

Example: a GUI toolkit invokes a callback on keypress; the callback code calls the GUI component to display a message, potentially invalidating the text box state before the callback returns.

Contracts and Guarantees
~~~~~~~~~~~~~~~~~~~~~~~~~

Four levels of guarantee (Beugnard et al.):

1. **Level 1 — Signature contracts**: names and argument types of operations (enables linking)
2. **Level 2 — Correctness contracts**: pre/post-conditions for all operations (guarantees successful execution); expressible in OCL
3. **Level 3 — Collaboration contracts**: allowed interactions among components (addresses synchronization, liveness, deadlock); defines the component's **protocol**
4. **Level 4 — Quality of service contracts**: non-functional requirements (availability, MTBF, MTTR, throughput, latency, data integrity, capacity)

When purchasing third-party components, customers need specifications covering all four levels to avoid discovering limitations late.

Objects as Components
~~~~~~~~~~~~~~~~~~~~~~

It's tempting to equate objects and components (e.g., JavaBeans) since both encapsulate state with operations. Problems:

- **Callbacks + self-references**: ``this``/``self`` calls compound the callback invariant problem
- **Multi-threading** makes contract guarantees even harder
- **Inheritance dangers**: subclass objects may violate component contracts if inheritance is used inappropriately
- **Fragile base class problem**: a new component version changes a base class, breaking existing derived classes — may require recompilation or rewriting

Industry Scaling
~~~~~~~~~~~~~~~~~

As the component industry grows:

- **Accounting**: how to charge for component use with multiple vendors
- **Packaging**: technologies include RPM, DMG, EPKG, Nix, OSGi
- **Disputes**: liability allocation when multi-vendor systems fail
- **QoS**: satisfying quality guarantees across independently developed components
- **Fault containment**: components detecting and containing faults when not in overall control of execution

Domain Standards
~~~~~~~~~~~~~~~~~

Tension between **proprietary** solutions (vendor lock-in) and **open standards** (encourage migration, benefit the community long-term but slow to gain approval/penetration).

Examples: HTML (domain standard, W3C), UNIX (proprietary, AT&T), Direct3D (proprietary, Microsoft), OpenGL (open standard), Java (now proprietary, Oracle), JavaScript (open/public domain).


Component Frameworks
--------------------

Shared attributes across major frameworks:

- Late binding, persistence, encapsulation, sub-typing
- Communication support: events, channels, uniform data transfer
- Packaging: Java JAR, COM CAB, CLI assemblies
- Deployment descriptors (configuration files), runtime reflection/metadata
- Component serving: application servers (EJB, COM+, CCM) or web servers (JSP, ASP.NET)

Key differences:

- **Memory management**: garbage collection (Java, CLR), reference counting (COM), none (CORBA)
- **Container-managed persistence**: EJB, CCM (yes); CLR, COM+ (no)
- **Versioning**: freezing, version numbers, compatibility rules, side-by-side execution
- **Target environment**: J2EE and COM → servers; COM also → desktop; CORBA → legacy
- **Development environments**: WebSphere (J2EE), Visual Studio .NET
- **Protocols**: Java/CORBA → IIOP, XML, RMI; COM/CLR → DCOM; CLR → XML, SOAP
- **Platform variability**: Java/CLI → single VM for all platforms; COM → Microsoft platforms only; CORBA → per-language IDL bindings, per-platform ORBs


Future Directions
-----------------

Open concerns as the component marketplace matures:

- **Liability** — apportioning responsibility when multi-component systems fail
- **Cross-cutting QoS** — satisfying quality guarantees across independent components
- **Contract persistence** — balancing new versions against support for existing features


Summary
-------

The viable component marketplace enables a new approach to software development — providing the flexibility of building without all the associated risk. Components and their frameworks will be part of design thinking for many future projects.
