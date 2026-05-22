Efficiency
==========

Physical database design concerns how data is stored on disk and how access structures (indexes) speed up queries.

Storage Hierarchy
-----------------

The **storage hierarchy** (registers → cache → main memory → disk → tape) has increasing capacity but decreasing speed at each level. Database performance is dominated by **disk I/O** — minimizing disk accesses is the primary optimization goal.

Disk Structure
--------------

- Data is stored on **platters** with concentric **tracks**, divided into **sectors**.
- Access time = **seek time** (move head to track) + **rotational latency** (wait for sector) + **transfer time**.
- Sequential access is much faster than random access.

Records, Blocks, and Files
--------------------------

- A **record** is the physical storage unit for a tuple.
- Records are grouped into fixed-size **blocks** (pages) — the unit of disk I/O.
- A **file** is a collection of blocks storing records of one or more relations.

File Organizations
------------------

Heap (Unsorted)
~~~~~~~~~~~~~~~

- Records are inserted at the end of the file.
- **Insert**: O(1) — fast (append to last block).
- **Search**: O(n) — requires linear scan.
- **Delete**: Search + mark/overwrite.

Sorted File
~~~~~~~~~~~

- Records ordered by a **sort key**.
- **Search**: O(log n) via binary search on blocks.
- **Insert**: Expensive — requires shifting records to maintain order.
- **Range queries**: Efficient once the start point is found.

Indexing
--------

Primary Index
~~~~~~~~~~~~~

- Built on the **ordering key** of a sorted file.
- **Sparse index**: One index entry per block (points to the first record in each block).
- **Dense index**: One index entry per record.
- Sparse primary indexes are smaller and fit in fewer blocks.

Secondary Index
~~~~~~~~~~~~~~~

- Built on a **non-ordering field** — always a **dense index**.
- Supports **point queries** only (not efficient for range queries without additional structure).

Multi-Level Index
~~~~~~~~~~~~~~~~~

- When a single-level index is too large to search efficiently, build an index on the index.
- Each level reduces the search space by the **blocking factor** of the index.
- The **B+ tree** is the standard multi-level index structure:

  - Balanced — all leaf nodes at the same depth
  - Internal nodes contain keys and pointers to children
  - Leaf nodes contain keys and pointers to data records, plus pointers to sibling leaves for range scans
  - Typical fan-out keeps tree height at 3–4 levels for very large tables

Hashing
-------

**Static hashing** maps a key to a fixed number of buckets via a hash function.

- **Insert/Search/Delete**: O(1) average case.
- **Overflow chains** degrade performance when buckets fill up.
- No support for range queries.
- **Extendible hashing** and **linear hashing** are dynamic schemes that grow/shrink the hash table as data changes.

Indexing Decisions
------------------

When deciding whether to create an index, consider:

- **Table size**: Small tables (fitting in a few blocks) gain little from indexing.
- **Multiple access paths**: Each additional index adds write overhead (every insert/update/delete must maintain all indexes).
- **Read vs write ratio**: Indexes help reads but slow writes. Favor indexes on read-heavy tables.
- **Existing indexes**: Check whether a needed access path is already covered by an existing index.
