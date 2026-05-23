Database Design Case Study
--------------------------

This section walks through a complete database design methodology using a case study for Georgia Tech Professional Education (GTPE) online programs.

Information Flow Diagram (IFD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An **Information Flow Diagram** captures the high-level data flows between the user interface (forms), application tasks, and the database. It identifies:

- **Forms** — the user-facing screens for input/output
- **Tasks** — the application logic that mediates between forms and the database
- **Data stores** — the database tables involved

Data Formats
~~~~~~~~~~~~~

Data formats specify the input and output types for each form field. These formats map directly to the **attribute types** of the entities in the EER diagram. Use the "beg, steal, borrow" approach — reuse formats from existing systems wherever possible.

Constraints
~~~~~~~~~~~

- Constraints on data values should be programmed into the application.
- For each task identified in the IFD, decide which constraints the task must enforce (e.g., uniqueness, referential integrity, domain restrictions).

Task Decomposition
~~~~~~~~~~~~~~~~~~

Each task identified in the IFD is decomposed into subtasks. The decomposition follows a **mother task** pattern:

- A top-level task is broken into atomic subtasks, each responsible for a single database operation or form interaction.
- Subtasks are classified by whether they **read** or **write** the database.

**Example — View Profile**: Decomposed into subtasks that read user attributes and relationship data from the database.

**Example — Edit Profile**: Decomposed into subtasks that read current values (for display) and write updated values back.

Abstract Code
~~~~~~~~~~~~~

- **Abstract code** is the penultimate step before writing SQL — a pseudocode description of each task's logic.
- There is no formal syntax; the goal is to clarify the sequence of database reads/writes and application logic.

**Example — Friend Requests**:

- **Request Friend** task: updates the database with a new friendship request; supports the request form.
- **View/Cancel/Accept/Reject Requests** task: supports the pending-requests form; decomposes into two subtasks:

  1. View pending requests (reads User, RegularUser, Friendship data)
  2. Accept/Reject/Cancel (updates the Friendship relationship)

EER Review and SQL Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After task decomposition and abstract code, the final step maps each task to concrete **SQL statements**:

- **View Profile** — ``SELECT`` queries joining user and profile tables
- **Edit Profile** — ``UPDATE`` statements with appropriate ``WHERE`` clauses
- **Request Friendship** — ``INSERT`` into the friendship/request table
- **View Pending Requests** — ``SELECT`` with join on friendship status
- **Accept/Reject/Cancel** — ``UPDATE`` or ``DELETE`` on friendship records
