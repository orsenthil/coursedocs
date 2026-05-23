Acme
====


Architectural Description Languages
------------------------------------

As awareness of software architecture has grown, so have tools for drawing, simulating, analyzing, reverse engineering, and reporting on architectures. A prerequisite for tool interoperation is a standard **Architectural Description Language (ADL)**.


ACME Overview
-------------

**Acme** is an extensible ADL developed at Carnegie Mellon University and USC/ISI, specifically designed to facilitate **interchange of architectural descriptions among tools**.

Tools in the Acme ecosystem:

- **AcmeStudio** — graphical editor for drawing architectural diagrams
- **AcmeLib** — API (Java, C++) for programmatic interaction with Acme artifacts
- **AcmeWeb** — document generator

Key features:

- Defines a **vocabulary** for talking about architectures
- **Extension mechanism** for embedding tool-specific sublanguages (e.g., timing info for simulators)
- **Generics, families, and types** for defining architectural styles
- Descriptions can be converted to **first-order logic** for use by automatic reasoning tools


Architecture Vocabulary
-----------------------

Acme's seven core terms:

1. **Components** — computational elements and data stores
2. **Connectors** — communication and coordination among components
3. **Ports** — component interfaces (may include protocols)
4. **Roles** — connector interfaces
5. **System** — Acme's term for a configuration; the set of components and connectors
6. **Attachments** — bindings of ports to roles (specifying the configuration)
7. **Representations** — hierarchical decomposition across multiple levels of abstraction, with **rep-maps** binding between levels


Simple Client-Server Example
-----------------------------

An Acme description of a client-server system:

- ``System SimpleCS`` contains two **components** (``client``, ``server``), one **connector** (``RPC``), and two **attachments**
- ``client`` has port ``sendRequest``; ``server`` has port ``receiveRequest``
- ``RPC`` connector has roles ``caller`` and ``callee``
- Attachments: ``client.sendRequest`` → ``RPC.caller``; ``server.receiveRequest`` → ``RPC.callee``

To add error communication: add new ports (``err-trap`` on client, ``alert`` on server), a new ``error`` connector with ``source`` and ``sync`` roles, and two more attachments connecting them.

AcmeStudio can render these descriptions graphically (components as rectangles, connectors as circles) and generate textual Acme code from diagrams.


Decomposition
-------------

Two kinds of decomposition for managing complexity:

- **Horizontal** — dividing at the same level of abstraction (e.g., body → digestive, respiratory, immune systems). Handled by Acme's components and connectors.
- **Vertical** — going deeper into the abstraction hierarchy (e.g., respiratory → lungs, trachea, diaphragm). Handled by Acme's **representations**.


Representations and Rep-Maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any component or connector can have one or more lower-level **representations** (supporting multiple views of the same element).

Example: a component with ports ``easyRequests`` and ``hardRequests`` can have a representation containing sub-components ``fastButDumb`` and ``slowButSmart``. The **binding section** (rep-map) maps ``easyRequests`` → ``fastButDumb.P`` and ``hardRequests`` → ``slowButSmart.P``.


Extending ACME
--------------

Property Sublanguage
~~~~~~~~~~~~~~~~~~~~~

Acme's extension mechanism allows embedding **tool-specific name-value pairs** (properties) within descriptions. Acme checks syntax but passes properties through to external tools.

Uses include:

- **Visualization** properties for external rendering tools
- **Temporal constraints** for simulators
- **Type checking** on port/role data
- **Protocol** specifications
- **Scheduling** and **resource consumption** constraints

Example: a client component might include ``property Aesop-style : style_id``; a server might specify ``property idempotence : boolean = true`` and ``property max-concurrent-clients : integer = ...``; a connector might declare ``property synchronization`` and ``property protocol`` (e.g., using the Wright ADL).


Families (Architectural Styles)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Families** define new terms describing sets of architectures — Acme's mechanism for architectural styles. Style rules can be encoded as properties.

Example: a ``PipeAndFiltersFamily`` defines component type ``FilterType`` and connector type ``PipeType``. Systems declared with type ``PipeAndFiltersFamily`` then use ``filter1 : FilterType``, ``pipe1 : PipeType``, etc.


Open Semantic Framework
~~~~~~~~~~~~~~~~~~~~~~~~

Acme descriptions can be exported as **first-order logic** for use by external automated reasoning tools (e.g., theorem provers). Example: ``∃ client, server, RPC such that client is a Component ∧ server is a Component ∧ RPC is a Connector ∧ attached(client.sendRequest, RPC.caller) ∧ ...``


ACME Limitations
----------------

Acme's primary goal is **interchange** — enabling architectural descriptions to move between tools. As a result, it intentionally lacks:

- **Behavioral specifications** — what components/connectors actually do
- **Functional property representation** — structure is well-described, but function/behavior is not
- **Code-to-architecture mapping** — no direct connection between code and architectural elements (neither code generation nor reverse engineering)
- **Non-functional requirements** — only expressible through the property sublanguage, with no standard vocabulary

Despite these limitations, Acme demonstrates the importance of ADLs and provides a foundation for architectural description and tool interoperability.
