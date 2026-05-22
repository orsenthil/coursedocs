Terms
=====

- **Candidate Key**: A minimal set of attributes that uniquely identifies every tuple in a relation.
- **Superkey**: Any set of attributes that uniquely identifies tuples (a candidate key is a minimal superkey).
- **Prime Attribute**: An attribute that is part of any candidate key.
- **Functional Dependency** (X → Y): For any two tuples with the same X values, the Y values must also be the same.
- **Trivial Functional Dependency**: X → Y where Y ⊆ X (always holds).
- **Minimal Cover**: A reduced set of functional dependencies F equivalent to a given set E (F⁺ = E⁺), such that:

  - Every right-hand side is a single attribute
  - No dependency can be removed without changing the closure
  - No attribute can be removed from any left-hand side without changing the closure

- **Primary Index**: An index on the ordering key of a sorted file (typically sparse).
- **Secondary Index**: An index on a non-ordering field (always dense).
- **Sparse Index**: One index entry per disk block.
- **Dense Index**: One index entry per record.
