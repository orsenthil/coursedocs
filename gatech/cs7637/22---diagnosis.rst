Diagnosis
=========

Overview
--------

**Diagnosis** is the identification of the fault or faults responsible for a malfunctioning system. The system may be a car, a computer program, an organism, or an economy. Diagnosis builds on classification and configuration and can be viewed as "configuration in reverse" — instead of assembling a working system, we identify what went wrong in one.

Data Space and Hypothesis Space
-------------------------------

Diagnosis maps from a **data space** to a **hypothesis space**:

- **Data space**: observed signs and symptoms, ranging from specific ("temperature is 104°F") to abstract ("patient has a fever")
- **Hypothesis space**: candidate faults or diseases that could explain the data (e.g., flu, carburetor failure, software bug)

The mapping is complex because:

- The data and hypothesis spaces can both be large
- The mapping can be **many-to-many** (one datum explained by multiple hypotheses; one hypothesis explaining multiple data points)
- Hypotheses can **interact** (presence of H3 may exclude H4; H5 may imply H6)

Heuristic Classification
~~~~~~~~~~~~~~~~~~~~~~~~~

A common diagnostic method combines bottom-up and top-down classification:

1. **Abstract** raw data into higher-level categories (bottom-up: "104°F" → "high fever")
2. **Map** abstract data to abstract hypotheses ("high fever" → "infection")
3. **Refine** abstract hypotheses into specific diagnoses (top-down: "infection" → "bladder infection" → specific strain)

The goal is a refined hypothesis that explains all available data.

Diagnosis as Classification vs. Abduction
------------------------------------------

Viewing diagnosis purely as classification has limitations:

- Multiple diseases can co-occur
- Diseases can interact, canceling or amplifying each other's symptoms
- No single classification category may cover all observed data

A more powerful perspective is **diagnosis as abduction**.

Deduction, Induction, and Abduction
------------------------------------

Three fundamental forms of inference:

- **Deduction**: given a rule (if flu then fever) and a cause (flu), conclude the effect (fever). *Truth-preserving.*
- **Induction**: given multiple cause-effect observations, induce a general rule. *Not truth-preserving* — the rule may not hold for the entire population.
- **Abduction**: given a rule (if flu then fever) and an effect (fever), hypothesize the cause (flu). *Not truth-preserving* — fever has many possible causes.

Abduction is inherently uncertain because multiple causes can produce the same effect. Diagnosis is an instance of abduction.

The scientific method combines all three: observe data → **abduce** an explanation → **induce** a general rule → **deduce** predictions → observe new data → repeat.

Criteria for Choosing Hypotheses
--------------------------------

When multiple hypotheses could explain the data, three principles guide selection:

Explanatory Coverage
~~~~~~~~~~~~~~~~~~~~

Prefer hypotheses that explain more of the observed data. If H3 explains D1–D8 and H7 explains only D5–D9, prefer H3 (assuming data points are equally important).

Parsimony
~~~~~~~~~

Prefer the simplest explanation. If H4 alone explains D1–D8, prefer it over the combination H2 + H6 + H8 even if the combination covers slightly more data. In practice, balance coverage and parsimony — e.g., {H4, H8} may be optimal: two hypotheses covering all data, simpler than three.

Confidence
~~~~~~~~~~

Prefer hypotheses with higher prior likelihood. H3 explaining D1–D8 may be preferred over H5 explaining D1–D9 if H3 is considered more probable.

These criteria apply beyond diagnosis — any abductive task (e.g., intelligence analysis) benefits from balancing coverage, parsimony, and confidence.

Methods for Diagnosis
---------------------

Multiple reasoning methods can address the diagnostic task:

- **Rule-based reasoning**: if-then rules mapping symptoms to faults (common in car repair, program debugging)
- **Case-based reasoning**: retrieve a similar past case, adapt its diagnosis to the current data; tends to focus the hypothesis set efficiently
- **Model-based reasoning**: use a causal model of the system to reason about which faults could produce the observed behavior
- **Heuristic classification**: the bottom-up abstraction → mapping → top-down refinement method described above

Different methods may yield different solutions for the same problem. Method selection itself becomes a reasoning task (meta-reasoning).

Completing the Process
~~~~~~~~~~~~~~~~~~~~~~

Once faults are identified, the final step is **treatment/repair** — which can be viewed as a configuration task: given a set of identified faults, configure a set of interventions that address them.

Cognitive Connection
--------------------

Diagnosis is triggered whenever expectations are violated — we observe behavior that differs from what we expected and ask "why?" This happens constantly: unexpected traffic, a broken appliance, a failed software test, a puzzling interpersonal interaction. Diagnosis is a **task** addressable by multiple methods (rule-based, case-based, model-based reasoning), illustrating the task-method distinction central to knowledge-based AI.
