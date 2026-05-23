Scripts
=======

Scripts Overview
----------------

**Scripts** are structured knowledge representations for capturing causally coherent sets of events. They are the culmination of frames, understanding, and commonsense reasoning.

- **Causal**: one event sets off another
- **Coherent**: links between events make sense in context
- **Events**: observable occurrences in the world (some may be mental, like deciding)

Scripts enable agents to generate expectations about situations, understand multi-sentence stories, and select appropriate actions without planning from scratch at runtime.

Motivating Example
~~~~~~~~~~~~~~~~~~

Story: "Bob went to a restaurant and sat down. Nobody served him for a while. The hamburger took long and was burned. Bob was not happy. He didn't finish. Did Bob leave a large tip?"

You infer "no" because your restaurant script tells you: poor service + poor food → unhappy customer → no tip. The script connects otherwise disparate events into a coherent narrative and enables inferences not explicitly stated.

Parts of a Script
-----------------

A script has six components:

1. **Entry conditions** — prerequisites for the script to execute (e.g., customer is hungry, customer has money)
2. **Results** — conditions true after the script completes (e.g., customer is not hungry, customer is pleased, owner has more money, customer has less money)
3. **Props** — objects involved (e.g., tables, menus, food, check, money)
4. **Roles** — agents involved (e.g., customer S, waiter W, cook C, cashier M, owner O)
5. **Tracks** — variations/subclasses of the script (e.g., coffeehouse, fast food, casual dining, formal dining)
6. **Scenes** — specific sequences of events within the script

Example: Restaurant Script (Formal Dining)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entry conditions: S is hungry, S has money

Results: S has less money, S is not hungry, S is pleased, O has more money

Scene 1 (Entering):

1. S moves self to restaurant (place P)
2. S sees a table
3. S decides to move to table
4. S moves self to table
5. S moves body into sitting position
6. W sees S
7. W moves self to S
8. W moves menu to S

Additional scenes follow: ordering, eating, paying, leaving. Each event is represented as a primitive action frame.

Form vs. Content
----------------

The abstract script is like a class; specific situations are instantiations. When Salwa (the customer) enters a restaurant with Lucas (waiter), the script instantiates with those specific values.

Scripts compose from the same **primitive actions** used in commonsense reasoning. Primitive action frames are the fundamental units; causally coherent sequences of these frames form scripts. Knowledge structures compose hierarchically — frames build into scripts.

Scripts as compiled plans: rather than generating a plan at runtime (computationally expensive), scripts provide pre-stored plans that can be invoked immediately. This addresses the conundrum of how agents handle complex problems with limited resources in near real-time.

Generating Expectations
-----------------------

Scripts generate expectations about what will happen next. When expectations are violated:

- Something has gone wrong (error detection)
- The situation is surprising, amusing, or upsetting
- Creativity may be at play (novel + valuable + unexpected)

This connects to theories of humor (violated expectations in familiar scripts) and creativity.

Tracks and Hierarchies
----------------------

Tracks represent sub-types of a script. Restaurant tracks: coffeehouse, fast food, casual dining, formal dining. Common elements across all tracks: enter, order, eat, pay, leave. Track-specific elements differ (e.g., counter service vs. table service).

Scripts organize into **semantic hierarchies**: Restaurant script > {Coffeehouse, Fast Food, Casual, Formal}. Higher-level scripts (e.g., "social event") can contain restaurant-going as a sub-script.

Script invocation is a **classification** problem: the agent classifies the current situation into the most appropriate script in long-term memory, then walks down the hierarchy (restaurant → fast food) as more information arrives.

Learning and Using Scripts
--------------------------

Learning scripts connects to:

- **Incremental concept learning** — refining script knowledge from new experiences
- **Frames** — scripts are built from frame-like knowledge structures
- **Understanding** — comprehending events to encode them into scripts
- **Common sense reasoning** — filling gaps using background knowledge

Using scripts connects to:

- **Classification** — selecting the right script for the current situation
- **Planning** — scripts are pre-compiled plans
- **Frames** — interpreting incoming events against script expectations

Both case-based reasoning and scripts are memory-intensive — memory supplies most of the answer. The difference: cases are specific instances; scripts are abstractions over instances.

Cognitive Connection
--------------------

Scripts align with the theory that the brain is a **prediction machine**: rapid bottom-up processing followed by mostly top-down processing based on expectations, then action on those expectations. When expectations fail → amusement, surprise, or anger.

Open question: do we store scripts or generate them at runtime?

Scripts relate to **mental models** — not just for social situations (restaurants, movies) but for how programs work, how economies function, how car engines operate. Scripts are culture-specific (tipping is expected in the U.S. but insulting in some countries) and evolve through cultural interaction, but once established they are a powerful source of knowledge.
