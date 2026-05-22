Normalization
=============

Normalization is the process of decomposing relations to eliminate redundancy and anomalies while preserving information and functional dependencies.

- An **EER diagram** mapped to relations always produces normalized databases.

Goals of Normalization
----------------------

- No redundancy of facts
- No cluttering of facts
- Must preserve information (lossless joins)
- Must preserve functional dependencies

Non-First Normal Form (NF²)
----------------------------

A relation is **not in 1NF** if it contains multi-valued or composite attributes. All attribute values must be drawn from a set of **atomic values**.

Anomalies in Unnormalized Relations
------------------------------------

Poorly designed relations suffer from three types of anomalies:

- **Redundancy**: The same fact is stored multiple times across rows.
- **Insertion Anomaly**: Cannot insert certain facts without inserting unrelated data (e.g., cannot add a department without an employee).
- **Deletion Anomaly**: Deleting a tuple inadvertently removes unrelated facts.
- **Update Anomaly**: Updating a repeated fact requires changing multiple rows; partial updates cause inconsistency.

Decomposition Quality
---------------------

- **Information Loss**: A bad decomposition may lose information — the natural join of the decomposed relations does not reconstruct the original.
- **Dependency Loss**: A decomposition may fail to preserve functional dependencies, making some constraints unenforceable without joins.
- **Perfect Decomposition**: Achieves both lossless joins and dependency preservation.

Functional Dependencies
------------------------

A **functional dependency** X → Y means that for any two tuples with the same X values, the Y values must also be the same.

A **full functional dependency** X → Y means Y is functionally dependent on X but not on any proper subset of X.

Functional Dependencies and Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Keys enforce functional dependencies: if X is a key, then X → (all attributes).
- A **determinant** is any set of attributes on which some other attribute is fully functionally dependent.

Normal Form Definitions
-----------------------

- **NF²**: Non-First Normal Form — contains non-atomic values
- **1NF**: All domain values are atomic
- **2NF**: In 1NF, and every non-key attribute is **fully dependent** on the key (no partial dependencies)
- **3NF**: In 2NF, and every non-key attribute is **non-transitively dependent** on the key
- **BCNF** (Boyce-Codd Normal Form): Every determinant is a candidate key

**Kent and Diehr Quote**: "All attributes must depend on the key (1NF), the whole key (2NF), and nothing but the key (3NF), so help me Codd!"

Armstrong's Axioms
-------------------

Rules for computing the closure of functional dependencies:

- **Reflexivity**: If Y ⊆ X, then X → Y
- **Augmentation**: If X → Y, then XZ → YZ
- **Transitivity**: If X → Y and Y → Z, then X → Z

Derived rules: union, decomposition, pseudotransitivity.

Lossless Join Guarantee
------------------------

A decomposition of R into R1 and R2 is **lossless** if and only if the common attributes (R1 ∩ R2) form a superkey of either R1 or R2.

Dependency Preservation Guarantee
----------------------------------

A decomposition preserves dependencies if the union of the functional dependencies enforceable on the individual decomposed relations is equivalent to the original set of dependencies.

3NF vs BCNF
------------

- There exist relations that can be decomposed to **3NF** (lossless + dependency-preserving) but **not to BCNF** without losing dependencies.
- This can only happen when the relation has **overlapping candidate keys**.
- In practice, this situation rarely occurs.
