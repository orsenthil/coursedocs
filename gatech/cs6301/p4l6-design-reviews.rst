Design Reviews
==============

Reviews (also called inspections or walkthroughs) are systematic readings of software artifacts to detect defects. They complement testing and proofs — each technique finds problems the others miss.

Purpose and Scope
------------------

**Purpose:** Detect defects (bugs, faults, standards violations). Reviews should **not** be used for education, status reporting, or problem-fixing.

**Applicable artifacts:** Requirements documents, specifications, architectural designs, detailed designs, new code, fixes, test plans, documentation.

**Defect categories** (from code review example):

- **Bugs** — logic errors, incorrect results
- **Documentation issues** — missing/wrong comments
- **Standards violations** — formatting, naming inconsistencies
- **Inefficiencies** — redundant computation, missed optimizations

**Key insight:** Groups find more defects than individuals ("many eyes" phenomenon), but group time is expensive — reviews must be structured to be cost-effective.

The Review Process
-------------------

Step 1: Planning
~~~~~~~~~~~~~~~~~

- Select participants, schedule meeting, assign roles
- Specify the artifact (or portion) under review
- Distribute materials (artifact, review form, background docs)
- Complete ~5 days before meeting

Step 2: Preparation
~~~~~~~~~~~~~~~~~~~~

- Participants individually study material and note potential defects
- Expected rate: ~10 pages of text or ~100 LOC per hour
- Superficial issues reported before the meeting to save meeting time

Step 3: Review Meeting
~~~~~~~~~~~~~~~~~~~~~~~

- Duration: ≤ 2 hours (fatigue reduces effectiveness beyond this)
- Review rate: ~100 LOC/hour (same as preparation)
- Collect individually-noticed defects; generally do not discuss/debate them in depth

Step 4: Rework
~~~~~~~~~~~~~~~

- Author investigates raised issues
- Confirmed defects are corrected or logged in issue tracking system

Step 5: Follow-Up
~~~~~~~~~~~~~~~~~~

- Author reports rework results to moderator
- Moderator verifies fixes are properly implemented
- Moderator collects review metrics (defect counts, types, time spent)
- Moderator suggests process improvements

Participant Roles
------------------

**Moderator:**

- Verifies participants prepared; aborts if team is unprepared
- Checks artifact readiness (compiled, unit-tested, etc.)
- Runs the meeting: keeps on track, arbitrates, manages time
- Technically competent but need not be domain expert
- Collects follow-up data and drives process improvement

**Recorder:**

- Records issues on the review form (location, description, type, severity)
- Proactively clarifies issues during discussion
- Ensures essence of each concern is captured accurately

**Reader:**

- Leads participants through the artifact systematically (line-by-line or element-by-element)
- Paraphrases what the artifact expresses (descriptive, not justificatory)
- Uses impersonal pronouns ("it does X") to avoid defensiveness
- Some organizations forbid the author from being the reader

**Reviewers (3-6):**

- Primary responsibility: raise issues
- Phrase concerns as questions, not assertions
- Ask "what happens if..." rather than "that's wrong"
- Do not suggest fixes during the meeting

Review Meeting Structure
-------------------------

1. Introduce participants
2. Moderator states objectives (raise concerns, not solve problems)
3. Evaluate preparedness (abort if insufficient)
4. Systematic walkthrough of the artifact
5. Record issues on review form
6. Summarize issues, determine severities and priorities
7. Assign responsibility for investigation/resolution
8. Agree on verification method (moderator check vs. re-review)

Severity Classification
~~~~~~~~~~~~~~~~~~~~~~~~

- **Minor** — rework verified by author (e.g., comment fixes, style issues)
- **Moderate** — conditional rework verified by moderator
- **Major** — reinspection required (threshold: >20% of document, >20 hours of work, or >100 LOC affected)

Ensuring Thoroughness
----------------------

- **Line-by-line / element-by-element coverage** — systematic traversal
- **Checklist-based review** — checklists derived from common defect types or company-specific data
- **Verification conditions** (Cleanroom methodology) — specific rules for specific constructs (e.g., "does this loop always terminate?")

Metrics
--------

- **Review rate** — lines of artifact per staff-hour
- **Defect rate** — defects detected per staff-hour
- **Defect density** — defects per line of artifact (indicates production process quality)
- **Process yield** — review-detected defects / total defects (including those found by testing and field reports)

Process Improvement Data
~~~~~~~~~~~~~~~~~~~~~~~~~

Collect per review: artifact identity, development stage, date/duration, participants, preparation time, issues raised, confirmed defects (type + severity). Store in database for aggregate analysis. Distribute post-review effectiveness questionnaires.

Alternative Review Styles
--------------------------

- **Fagan inspections** — formal structured reviews (described above)
- **Pair programming** (Laurie Williams / XP) — synchronous review during coding
- **Pass-around reviews** — asynchronous via email/SCM notifications (common in open source)
- **Tool-assisted** — diff tools, SCM alerts, static analyzers (Lint, CodeCheck/Eclipse plugins)

Guidelines
-----------

**Participants:**

- Never use reviews for personnel evaluation; managers should not attend unless technically involved
- No non-participant observers (distracting)
- Do not use reviews for training (hold separate sessions)
- Author should not be moderator or recorder

**Content:**

- Avoid style debates (consistency > preference)
- Avoid problem-solving during the meeting
- Avoid "you" — use impersonal phrasing to reduce defensiveness

**Process:**

- Spread reviews over time; limit to 250 LOC or 2 hours per session
- Each review type should have predetermined thoroughness criteria
- Treat review as a go/no-go gate for the next development stage
- Consider sign-off requirements for accountability

Effectiveness
--------------

- Formal reviews find **70-90% of defects** in the reviewed artifact
- Cost: **10-20% of total development cost** (staff time for prep + meeting)
- Detection rates vary with artifact complexity and review quality
- Lightweight reviews (author + 1-2 others) may be more efficient per staff-hour but find fewer total defects

Other Benefits and Costs
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Skill enhancement** — reviewers learn from others' work
- **Ego effect** — knowledge of upcoming review improves artifact quality
- **Damaged egos** — confrontation with defects can be stressful
- **Big-brother effect** — measurement awareness raises stress levels

Summary
--------

Defects found late are expensive to fix. Reviews are a cost-effective early detection method for all artifact types. Deep design problems require exposure to experienced designers — reviews must be focused and well-run to justify their cost. Institutionalizing reviews (formal process element + corporate culture) yields long-term savings in reduced maintenance and increased customer satisfaction.
