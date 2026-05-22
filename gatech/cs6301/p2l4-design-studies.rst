.. title: Design Studies
.. slug: Design Studies
.. date: 2016-05-27 23:41:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

Design Studies
==============

Design Studies
--------------

Design involves making decisions, generally trading off among nonfunctional criteria. Sources that inform these decisions include the customer, end users, technology specifications, and competitors' products. When more detailed analysis is required, tools such as simulations, prototypes, and **design studies** can help.

A **design study** is a rigorous and systematic evaluation of the factors that influence a design. It begins with determining relevant criteria, how they are measured, and what measurement values are deemed satisfactory. The study compares possible approaches, measuring each against predetermined criteria.

The process helps the designer explore a **design space** — the range of possibilities available as solutions. Factors for buildings might include cost, material availability, building codes, and traffic impact. For software, relevant factors include performance, memory footprint, and time to construct. Correctness is not among the comparison factors — all versions are assumed to work correctly but differ in nonfunctional ways.

Design Studies as Experiments
-----------------------------

A design study is essentially an empirical scientific experiment. It involves:

- Research questions
- Subjects of study
- Experimental conditions
- Methods and tools
- Metrics
- Independent and dependent variables
- Data collection and statistical analysis
- Conclusions

The overall goal is **repeatability** — someone else should be able to recreate the study conditions and reach the same conclusions.

Report Structure
----------------

The design study is presented in a report that may include charts, tables, graphs, and screenshots. It is not a narrative but a dispassionate description of a systematic exploration. The report should be professional quality with checked spelling and grammar.

**Section 1 — Context**: Background, motivation, and specialized vocabulary so an unfamiliar reader can understand the report.

**Section 2 — Research Questions**: Each tradeoff expressed as a neutrally-formulated question regarding dependent variables being measured and independent variables being varied. Example: "How are execution times and memory footprint affected as the amount of pre-processing computations vary?" Questions should be numbered for later reference.

**Section 3 — Subject**: Brief description of each subject (program version) being compared, differentiating it from the others.

**Section 4 — Experimental Conditions**: Hardware configuration (cores, RAM, clock speed, networking), operating systems, programming languages, virtual machines and versions, network details, build/execution parameters, input files, and confounding factors (e.g., other processes running).

**Section 5 — Variables**: Identification of independent and dependent variables with unique names, descriptions, and units of measurement. Includes a summary table mapping each research question to its independent and dependent variables.

**Section 6 — Method**: Number of trials, measurement devices/tools, randomization techniques, significant digits, which subjects will be run, arguments for each trial, and statistical techniques (e.g., linear regression).

**Section 7 — Results**: Data collected and statistical analysis. No speculation — just facts.

**Section 8 — Discussion**: Interpretation of data, explanation of unexpected values, reflections on the experimentation process, and suggestions for further work.

**Section 9 — Conclusions**: Summary of results with explicit answers to each research question from Section 2.

Deliverables
------------

Each course project has three deliverables:

1. Source code solving a specific problem in several ways
2. A project report with project-specific content
3. A design study report

The design study represents the explicit knowledge about design learned during the project. Design must be learned by doing — through systematic thinking, experimentation, and reflective write-up.
