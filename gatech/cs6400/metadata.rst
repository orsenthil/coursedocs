Metadata
========

Metadata is "data about data" — it describes the structure, context, provenance, and preservation requirements of stored information.

Archival Metadata
-----------------

Archival metadata addresses the challenge of **long-term data preservation**: how to ensure data remains readable and interpretable decades or centuries later. Organizations dealing with this include:

- NASA
- U.S. Justice Department
- National Archives
- UCAR (University Corporation for Atmospheric Research)

The core question: **How do you make sure you can read your data 100 years from now?**

OAIS Information Model
----------------------

The **Open Archival Information System** (OAIS) is the reference model for long-term digital preservation.

* Reference: http://www.oclc.org/research/pmwg/

Key components of the OAIS model:

- **Content Information**: The data object plus its **Representation Information** (needed to interpret the bits as meaningful data).
- **Preservation Description Information (PDI)**: Metadata that supports long-term preservation:

  - **Reference** — identifiers for the content
  - **Provenance** — history of the content (origin, custody chain, transformations)
  - **Context** — why the content was created, relationship to other information
  - **Fixity** — integrity checks (checksums, digital signatures)

- **Packaging Information**: Binds content and PDI into information packages (SIP, AIP, DIP).

Metadata Representation Standards
----------------------------------

- **XML** / **XML Schema** — structured markup and validation
- **RDF** — Resource Description Framework for semantic metadata
- **OWL** — Web Ontology Language for formal knowledge representation
- **Dublin Core** — a minimal set of 15 metadata elements for resource discovery
- **METS** (XML) — Metadata Encoding and Transmission Standard for digital library objects
- **VERS** — Victorian Electronic Records Strategy (government records)
- **AIP** — Archival Information Package (OAIS packaging)
- **MOF** — Meta-Object Facility (OMG standard for metamodeling)

Key Takeaway
~~~~~~~~~~~~

Standards for archival metadata are **still maturing**. Multiple competing standards exist, and interoperability remains a challenge. Effective preservation requires a combination of content metadata, structural metadata, and provenance tracking.
