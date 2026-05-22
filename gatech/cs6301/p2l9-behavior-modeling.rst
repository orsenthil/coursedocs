.. title: P2L9 Behavior Modeling 
.. slug: P2L9 Behavior Modeling 
.. date: 2016-05-27 23:46:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P2L9 Behavior Modeling
======================

States and Events
-----------------

Structural models express properties true at all times but fail to convey how systems respond to external stimuli. UML provides behavioral modeling diagrams to address this.

**State**: An abstract description of a set of system values at a given point in time. Example: "it's raining" abstracts over the exact amount of precipitation.

The **state space** is the set of all possible states. Its size grows multiplicatively with the number of attributes and their possible values — the **state explosion problem**. Example: a 3×3 Tic-Tac-Toe grid with 3 possible values per cell has 3^9 = 19,683 possible states.

**Event**: A single, instantaneous, noticeable occurrence that serves as a stimulus for a state transition. Events may be:

- **Asynchronous** — randomly occurring, possibly in bursts
- **Synchronous** — at periodic intervals, controlled by a clock/event loop

UML event taxonomy:

- **Signals** — asynchronous notifications
- **Method calls** — synchronous
- **State changes** (data conditions) — changes in data values
- **Passage of time**

Modeling Approaches
-------------------

Systems that respond to events are called **reactive systems**. Three levels of behavioral modeling complexity:

1. **Combinatorial** — only inputs determine outputs (no memory/history)
2. **Sequential** — states with memory, linearly ordered transitions
3. **Concurrent** — multiple states, multiple events occurring unpredictably

Combinatorial Modeling
----------------------

The simplest form: only current inputs (not history) determine behavior.

**Decision tables**: Columns for input conditions and output responses; rows for each combination of input values. For n binary inputs: 2^n rows.

Example — workshop with 3 switches (master, light, drill) controlling 2 outputs (overhead light, power drill motor): 8 rows. If master switch is off, both outputs are off regardless of other switches.

**Decision trees**: Graphical equivalent of decision tables. Diamond nodes = decisions, rectangle nodes = actions, arcs = decision outcomes. Same information as the table but may contain duplicated nodes due to redundancy. Tables become unmanageable as input possibilities grow.

Sequential Systems
------------------

Differ from combinatorial systems by having **memory** — the previous state plus the current event determines the next state. Modeled as **finite state machines (FSMs)**.

**State Transition Table (STT)**: Four columns — current state, input event, output action, next state.

Example — garage door opener:

- 6 states: door open/motor off, door closed/motor off, door partially open/motor off, door partially closed/motor off, motor running up, motor running down
- 3 events: button press, sensor-door-up, sensor-door-down
- Key behavior: pressing button while motor runs down → stop then immediately reverse (safety)

**State Transition Diagrams**: Graphical FSM representation. Ovals or rectangles = states; directed arcs = transitions labeled ``event/action``. Layout has no semantic meaning. A filled circle indicates the start/default state.

.. mermaid::

   stateDiagram-v2
       [*] --> DoorClosed_MotorOff
       DoorClosed_MotorOff --> MotorRunningUp : button press
       MotorRunningUp --> DoorOpen_MotorOff : sensor door up
       MotorRunningUp --> DoorPartiallyOpen_MotorOff : button press
       DoorOpen_MotorOff --> MotorRunningDown : button press
       MotorRunningDown --> DoorClosed_MotorOff : sensor door down
       MotorRunningDown --> DoorPartiallyClosed_MotorOff : button press
       DoorPartiallyClosed_MotorOff --> MotorRunningUp : button press
       DoorPartiallyOpen_MotorOff --> MotorRunningDown : button press

Problems with STDs:

- Too many arrows (n states × m events)
- Too many states (multiplicative explosion)
- No concept of nesting/hierarchy

Statecharts
-----------

Developed by **David Harel** as an improvement to state transition diagrams. Part of UML with tool support. Key mechanisms for managing complexity:

**Nesting (depth)**: A state can contain its own sub-state-machine. Benefits:

- Transitions from the enclosing state apply to all sub-states (reducing duplicate arcs)
- Transitions into the enclosing state go to its default sub-state
- Can nest to arbitrary depth

**Concurrency**: A dashed line separates a state into concurrently executing sub-machines. Reduces states from multiplicative (n × m) to additive (n + m). Each concurrent region has its own current state, transitions, and actions.

Statechart Icons
~~~~~~~~~~~~~~~~

- **States**: rounded-corner rectangles ("roundtangles") with labels
- **Transitions**: directed arcs labeled ``event [guard] / action``
- **Initial state**: filled black circle
- **Final state**: filled circle inside a concentric ring

Synchronization
~~~~~~~~~~~~~~~

Concurrent machines must cooperate. Two mechanisms:

- **Broadcast/cascade events**: An action on one transition can emit an event (after the slash) that triggers transitions in other concurrent machines. Events are globally known.
- **Data conditions**: Boolean expressions in square brackets on transitions; terms correspond to class attributes globally accessible to all machines. Keywords ``in`` and ``not in`` test whether another concurrent machine is in a specific state.

Additional Features
~~~~~~~~~~~~~~~~~~~

- **Entry/exit actions**: Executed upon entering or leaving a nested state (keywords ``entry:`` and ``exit:``)
- **Internal transitions**: Self-transitions without triggering entry/exit actions
- **Activities** (keyword ``do:``): Long-running actions that take time (vs. instantaneous actions)
- **Deferred events**: Events queued for later processing
- **Event parameters**: Data passed on events and forwarded to action method calls
- **Time events**: ``after <duration>`` triggers after elapsed time; ``when <time>`` triggers at a specific clock time
- **History states** (H): Upon re-entry, resume the sub-state that was active when the machine was last exited. ``H*`` applies recursively to nested sub-states.

Relationship to Class Diagrams
------------------------------

- Each class in the class model diagram *could* have its own statechart (though most classes are too simple to need one)
- Statechart **attributes** = class attributes
- Statechart **actions/activities** = class methods
- Statechart **events** = signals (modeled as dependencies with ``<<send>>`` stereotype in the class diagram)
- Statecharts must be consistent with the class model: event names, attribute names, and method names must match

Beyond Statecharts
------------------

Other UML behavioral diagrams: activity diagrams, sequence diagrams, collaboration diagrams, use cases, communication diagrams, timing diagrams, interaction overview diagrams.

Non-UML behavioral modeling approaches:

- **Temporal logic / model checking** — verify that a system can never reach an undesirable state
- **Process algebras** — specify concurrency and read/write behavior between concurrent activities

Reactive systems are hard to build correctly. Careful behavioral modeling (especially statecharts) provides assurance against deadlocks, state explosion bugs, and unintended side effects.
