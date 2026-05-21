.. title: Geeks in Black- The Code Review 
.. slug: Geeks in Black- The Code Review 
.. date: 2016-05-27 23:33:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

===============================
Geeks in Black- The Code Review
===============================

This lesson demonstrates a formal code review through a dramatized inspection of a short Java program (``BlankCount.java`` — counts blanks in a sentence). The educational content below distills the code review process, roles, defect taxonomy, and findings.

Code Review Roles
------------------

- **Moderator (Controller)** — runs the meeting, keeps participants on track, arbitrates disputes, ensures preparedness, manages time
- **Reader** — leads the team through the artifact line-by-line, paraphrasing what the code does (not why)
- **Recorder** — documents each defect with type, severity, location, and description; clarifies issues for accurate recording
- **Inspectors (3-6)** — raise issues by asking questions; identify defects across all categories

Code Review Process Observations
----------------------------------

Key process points illustrated:

- The moderator must control scope — participants frequently drifted into problem-solving, language debates, and personal criticism
- The reader should describe what the code does neutrally, not justify design decisions
- The recorder must actively seek clarification to accurately capture defect descriptions
- Style debates (comment format, brace placement) consume disproportionate time — pre-established coding standards prevent this
- Reviews should detect defects, not fix them or establish standards (those are separate activities)
- Personal attacks reduce effectiveness — use impersonal language ("the code does X" not "you did X")

Defect Classification
----------------------

Defect Types
~~~~~~~~~~~~~

- **Wrong** — code does not correctly implement the intended behavior
- **Missing** — required functionality or initialization is absent
- **Extra** — unnecessary code that adds confusion
- **Stylistic** — violates coding standards or conventions
- **Usability** — poor user experience in output/interaction
- **Performance** — inefficient implementation
- **Clarity** — confusing or misleading code/comments
- **Question** — uncertain whether something is a defect; requires investigation

Severity Levels
~~~~~~~~~~~~~~~~

- **Major** — affects correctness, causes wrong results or crashes; requires reinspection after fix
- **Minor** — cosmetic, stylistic, or documentation issues; verified by author

Defect Catalog from the Review
-------------------------------

The following defects were found in the ~40-line ``BlankCount.java`` program:

**Major defects (wrong/missing behavior):**

1. Line 20: ``==`` should be ``!=`` in while-loop condition (loop never executes as written)
2. Lines 19, 28: Characters printed as integers, not as characters
3. Line 20: No check for end-of-file — loop may never terminate if sentinel is missing
4. Line 34: Printing wrong variable (``next`` instead of ``count``)
5. Line 36: Catching generic ``Exception`` instead of specific ``IOException``
6. Line 37: Silent exit on exception — should log the error
7. Line 39: No explicit exit status on successful completion

**Minor defects (style/documentation):**

1. Line 1: Wildcard import (``import java.io.*``) pollutes namespace — import only needed classes
2. Line 2: Unnecessary import of ``java.lang.System`` (auto-imported)
3. Lines 4, 7, 8: Inconsistent comment style (``/* */`` vs ``//``)
4. Line 12: Should code to interface (declare as abstract type, instantiate concrete)
5. Lines 13-14: Local variables not initialized
6. Lines 13-14: Comment says "character" but type is ``int``
7. Line 16: Typos in user prompt ("charcter", "buy" for "by"), capitalization issues
8. Line 19: Inconsistent whitespace around arguments
9. Line 31: Confusing "assert" comment
10. Lines 32-35: Multiple print statements should be concatenated
11. No file header (author, revision history, date)
12. Lines 19, 28: Debug output to console belongs in a logger, not stdout
13. No consistent brace placement standard

Key Takeaways
--------------

- A short program (~40 lines) contained **19+ defects** across all categories
- Groups find more defects than individuals ("many eyes" phenomenon)
- Pre-established coding standards eliminate entire classes of style debates during reviews
- Major logic errors (wrong loop condition, wrong variable printed) coexist with minor style issues — both matter
- The review process must be disciplined: detect defects only, defer fixes and standard-setting to separate activities
- Reviews should not be used for blame — the dramatized review showed how personal criticism derails productivity
