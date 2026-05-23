Library Exercise (UML)
======================

Analyzing Requirements
----------------------

The process begins by examining requirements text and identifying **nouns** as candidate classes. Each relevant noun becomes a class in the class diagram, using domain vocabulary as class names.

Initial classes identified from library requirements:

- **Patron** — with attributes: name, address, phone number
- **Library Card** — with attribute: card number
- **Item** — with attribute: value (cost)
- **Fine**
- **Children** — with attribute: age
- **Date** — utility class for time-related concepts (due dates, loan periods, children's age)
- **Money** — utility class for currency (fines)
- **Book**, **Audio/Video Material**, **Reference Book**, **Magazine**
- **Best Seller**

The system and library themselves are not modeled as classes since there is only one of each — the model *is* the system.

Attributes like name, address, and phone number are not standalone classes but properties of Patron. Similarly, library card number is an attribute of Library Card.

Refining Classes and Attributes
-------------------------------

Several classes can be eliminated through refinement:

**Library Card → merged into Patron**: The card is just an ID number issued by an external vendor. It becomes an attribute (library card number) of Patron rather than a separate class.

**Children → merged into Patron**: Children are special patrons distinguished only by age (≤12) and a checkout limit (5 books). Making Child a subclass creates problems when a patron ages out — you'd have to destroy and recreate the instance, losing history. Instead, add an age attribute to Patron and vary behavior based on age.

**Best Seller → merged into Book**: A book's bestseller status is temporary. Representing it as a subclass creates the same type-change problem. Instead, add a boolean ``bestSeller`` attribute to Book.

Adding Attributes
-----------------

Additional attributes discovered from requirements:

- **Due date** (on Item) — when a checked-out item must be returned
- **Number of times renewed** (on Item) — generalized from "can only renew once"
- **Checked out** (on Item) — boolean tracking checkout status
- **Loanable** (on Item) — distinguishes items that can be checked out (books, AV material) from those that cannot (reference books, magazines)

Identifying Operations
----------------------

Operations are identified by examining **verbs** in requirements (specifically action verbs, not relationship verbs). Operations identified for Patron:

- ``itemsCheckedOut()`` — returns items currently checked out by the patron
- ``whenDue()`` — returns when an item is due
- ``outstandingOverdueFines()`` — returns any outstanding fines
- ``checkOut()`` — records checking out an item
- ``request()`` — requests a book/AV item not currently available

Adding Relationships
--------------------

**Associations** represent relationships between classes:

- **Checkout** association between Patron and Item — replaces the checked-out attribute; the existence of the link indicates checkout status
- **Request** association between Patron and Item — represents reservation of unavailable items

**Specialization (is-a)** hierarchy:

- Item → Loanable Item, Non-Loanable Item
- Loanable Item → Book, Audio/Video Material
- Non-Loanable Item → Reference Book, Magazine

This eliminates the ``loanable`` attribute — the hierarchy makes loanability explicit. Attributes ``value``, ``due date``, ``renewed``, and ``checked out`` move from Item down to Loanable Item.

The Checkout and Request associations should connect to Loanable Item (not Item), since non-loanable items cannot be checked out or requested.

Refining Relationships
----------------------

**Title class introduced**: A patron requests a *title* (e.g., "Tom Sawyer"), not a specific physical copy. Title has an **aggregation** relationship with Item (one title consists of multiple items, indicated by a diamond). The Request association moves from Loanable Item up to Title.

**Association class — CheckedOut**: Attributes ``renewed``, ``due date``, and ``fine`` are properties of the loan relationship, not of the loanable item itself (a book can be renewed once *per loan*, not once in its lifetime). These move into an association class called CheckedOut, attached to the Checkout association.

**Return operation** added to Patron. A ``whenReturned`` attribute is added to the CheckedOut class — a special value indicates an active loan; a date value indicates the item was returned (allowing the system to retain fine information until paid).

.. mermaid::

   classDiagram
       class Patron {
           +String name
           +String address
           +String phoneNumber
           +Integer libraryCardNumber
           +/Date age
           +itemsCheckedOut()
           +whenDue()
           +outstandingOverdueFines()
           +checkOut()
           +request()
           +return()
       }
       class Title {
           +String titleName
       }
       class Item {
           +Money value
       }
       class LoanableItem {
           +Date dueDate
       }
       class NonLoanableItem
       class Book {
           +Boolean bestSeller
       }
       class AudioVideoMaterial
       class ReferenceBook
       class Magazine
       class CheckedOut {
           +Integer renewed
           +Date dueDate
           +/Money fine
           +Date whenReturned
       }

       Item <|-- LoanableItem
       Item <|-- NonLoanableItem
       LoanableItem <|-- Book
       LoanableItem <|-- AudioVideoMaterial
       NonLoanableItem <|-- ReferenceBook
       NonLoanableItem <|-- Magazine
       Title o-- Item : 1..*
       Patron "0..*" -- "0..*" Title : Request
       Patron -- LoanableItem : Checkout
       Patron .. CheckedOut
       LoanableItem .. CheckedOut

Final Considerations
--------------------

**Derived attributes** (computed, not stored):

- ``age`` — derived from patron's birthday and current date
- ``fine`` — derived from due date and return date

**Cardinality** annotations on associations:

- Title to Item: one title → many items (``*``); each item → one title (``1``)
- Patron to Title (request): many-to-many (``*`` on both ends)

Key design insight: the analysis and design process itself reveals missing, implicit, or conflicting requirements — making the requirements better understood before implementation begins.
