Methodology IV: Implementation
==============================

The implementation phase translates the logical database design into a running system using a specific technology stack.

AMP Solution Stack
------------------

A common implementation stack:

- **A** — Apache (web server)
- **M** — MySQL / MariaDB (relational database)
- **P** — PHP / Python / Perl (server-side scripting)

Modern alternatives include MEAN (MongoDB, Express, Angular, Node.js) and similar stacks, but the relational model and SQL remain the foundation.

Indexing Decisions
------------------

The choice of whether to index a column depends on several factors:

- **Table size**: Indexing very small tables provides negligible benefit since a full table scan is already fast.
- **Access path overhead**: Each index adds storage and maintenance cost — every ``INSERT``, ``UPDATE``, and ``DELETE`` must update all affected indexes.
- **Read vs write ratio**: Heavy-read workloads benefit from indexes; heavy-write workloads suffer from index maintenance overhead.
- **Existing indexes**: Before adding a new index, check whether the query's access pattern is already covered by a composite or covering index.

**General advice**: Index primary keys (usually automatic), foreign keys used in joins, and columns frequently appearing in ``WHERE`` clauses or ``ORDER BY``. Avoid indexing columns with low cardinality or tables with heavy write loads.
