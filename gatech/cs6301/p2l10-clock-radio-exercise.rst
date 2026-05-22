.. title: P2L10 Clock Radio Exercise 
.. slug: P2L10 Clock Radio Exercise 
.. date: 2016-05-27 23:38:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P2L10 Clock Radio Exercise
==========================


Modeling with Statecharts
-------------------------

Statecharts are a precise way of modeling the behavior of complex **reactive systems**. This exercise models the behavior of a common clock radio to illustrate the statechart modeling process.


Clock Radio Description
-----------------------

**Physical controls:**

- **Volume knob** — top right, controls speaker loudness
- **Tuning knob** — right side, selects radio frequency
- **AM/FM switch** — top back edge, selects frequency band
- **Mode switch** — center front top, slides horizontally through four positions: **On**, **Off**, **Wake-Radio**, **Wake-Beep**
- **Hour / Min buttons** — top left, increment the currently selected timer
- **Wake button** — held while pressing Hour/Min to set alarm time
- **Sleep button** — held while pressing Hour/Min to set sleep timer duration
- **Snooze button** — large, center front top; silences alarm for 10 minutes per press

**Display and indicators:**

- 12-hour clock on left front
- AM/PM indicator light (upper left: off = morning, on = afternoon/evening)
- Wake indicator light (lower right: lit = alarm armed)
- Frequency indicator — small vertical white bar on right front

**Key behaviors:**

- If neither Wake nor Sleep is held, Hour/Min buttons set the current time of day
- Alarm automatically turns off after **one hour** to prevent all-day sounding
- Radio is powered by wall socket (no battery)


Percepts
--------

A **percept** is an externally sensible (visual, audible, tactile) aspect of a device. The clock radio's percepts include:

- **Speaker** — produces sound (radio audio or alarm beep)
- **Time display** — shows current time, wake time, or sleep time
- **AM/PM indicator light**
- **Wake indicator light**
- **Frequency indicator bar** — horizontal position tracks tuning knob
- **Volume knob** — rotational position provides tactile feedback
- **Mode switch** — physical position (On/Off/Radio/Alarm)
- **AM/FM switch** — physical position


Percept States and Finite State Machines
----------------------------------------

Each percept is modeled as a **concurrent finite state machine** within the statechart. The key modeling skill is choosing the right level of abstraction.

**Time display:** Theoretically 720 states (12 hours × 60 minutes). Using statechart concurrency, this reduces to 72 states (12 + 60). In practice, abstract to a **single node** labeled "ClockTime" and assume the underlying digit logic works correctly. The same abstraction applies to WakeTime and SleepTime, yielding a **three-state Display FSM**:

- ClockTime ↔ WakeTime ↔ SleepTime

**Mode switch:** Four states corresponding to physical positions:

- On, Off, Wake-Radio, Wake-Beep

**Station indicator:** Single state (Frequency) with no user-initiated transitions — position is driven by the tuning knob via inter-machine coordination.

**Speaker:** Two states — On, Off.

**Overall structure:** Seven concurrently executing sub-machines model the radio's percepts.


Events and External Controls
-----------------------------

An **event** is a spontaneous, instantaneous occurrence that state machines react to. Events for the clock radio include:

- Turning the volume knob (Event 1)
- Sliding the AM/FM switch left/right (Events 2, 3)
- Turning the frequency knob (Event 4)
- Pulling/inserting the plug (Events 5, 6)
- Pressing/releasing Hour, Min, Wake, Sleep, Snooze buttons (Events 7–11)
- Sliding the mode switch left/right (Events 12, 13)

Each event requires a documented **stimulus-response** entry specifying the system's expected behavior, including conditionals (e.g., "if in state On, sliding right → Off").


Outermost Statechart Layer
--------------------------

The outermost layer is a two-state machine:

- **Unplugged** ↔ **Plugged-In** (transitions: pull-plug / insert-plug)

All percept sub-machines are nested within the Plugged-In state. This mirrors Harel's digital watch example (batteries in/out).

.. mermaid::

   stateDiagram-v2
       [*] --> Unplugged
       Unplugged --> PluggedIn : insert plug
       PluggedIn --> Unplugged : pull plug

       state PluggedIn {
           state DisplayFSM {
               [*] --> ClockTime
               ClockTime --> WakeTime : press Wake
               WakeTime --> ClockTime : release Wake
               ClockTime --> SleepTime : press Sleep
               SleepTime --> ClockTime : release Sleep
           }

           state ModeSwitchFSM {
               [*] --> Off
               Off --> On : slide right
               On --> Off : slide left
               On --> WakeRadio : slide right
               WakeRadio --> On : slide left
               WakeRadio --> WakeBeep : slide right
               WakeBeep --> WakeRadio : slide left
           }

           state SpeakerFSM {
               [*] --> SpeakerOff
               SpeakerOff --> SpeakerOn : play
               SpeakerOn --> SpeakerOff : stop
           }

           state SetModeFSM {
               [*] --> NoneSet
               NoneSet --> ClockSet : Hour or Min pressed
               NoneSet --> WakeSet : Wake + Hour or Min
               NoneSet --> SleepSet : Sleep + Hour or Min
               ClockSet --> NoneSet : released
               WakeSet --> NoneSet : released
               SleepSet --> NoneSet : released
           }
       }


Setting the Time
----------------

A **SetMode sub-machine** tracks which timer is being configured:

- **None** (default) → **ClockSet** / **WakeSet** / **SleepSet**

Pressing Wake or Sleep while pressing Hour/Min determines which timer increments. This sub-machine ensures the same Hour/Min buttons affect different timers depending on context.


Stimulus-Response Table
-----------------------

A systematic table maps every event to its system response:

======  ==========================  =============================================
Event   Stimulus                    Response
======  ==========================  =============================================
1       Turn volume knob            Speaker loudness changes; knob position changes
2–3     Slide AM/FM switch          Band changes; switch position changes
4       Turn frequency knob         Station changes; knob position changes; frequency bar moves
5       Pull plug                   All state resets to Unplugged
6       Insert plug                 Transitions to Plugged-In (defaults)
12–13   Slide mode switch           Mode advances one position left/right (conditional on current state)
======  ==========================  =============================================


Timer Events and Internal States
--------------------------------

**Internal events** arise from timer logic:

- **Event 20:** Clock time reaches wake time → if mode is Wake-Radio, speaker plays; if Wake-Beep, speaker beeps
- **Event 19:** Alarm timer expires (1 hour) → alarm silences
- **Snooze timer expires** → alarm resumes
- **Clock time = wake time + 1 hour** → alarm off permanently

Internal timer sub-machines are added to the statechart to track these time-based triggers.


Coordination Mechanisms
-----------------------

**Guarded transitions:** Response to an event is conditioned on another sub-machine's state. Example: Event 20 triggers speaker → Playing only if mode switch is in Music state. The guard ``[in Music]`` appears in square brackets on the transition.

**Cascaded events:** A response to one event can broadcast a new internal event. Example: turning the frequency knob (Event 4) produces three responses — knob position changes, radio channel changes, and frequency bar moves. The bar is in a different sub-machine, so an internal event (Event A) is broadcast to coordinate them.


Validation
----------

After building the statechart, it must be **validated** through:

- **Review** — walk through use cases with a team, verifying each concurrent machine behaves correctly
- **Model checking** — encode all concurrent machines formally; use an automated model checker to verify properties
- **Simulation** — build an interpreter to execute the statechart and test scenarios interactively


Statechart Modeling Method Summary
----------------------------------

1. Prepare **use cases** for typical device usage
2. Determine **external percepts** (what users see/hear/feel)
3. Model percepts as **concurrent state machines**, choosing appropriate abstraction levels
4. Determine **external controls and stimuli** (events); add transitions
5. Build a **stimulus-response table** documenting every event's effect
6. Add **internal states/timers** for time-dependent behavior
7. Provide **coordination mechanisms** (guarded transitions, cascaded events)
8. Add default states, guards, and internal events
9. **Validate** the resulting statechart


Conclusion
----------

Even a common consumer device like a clock radio exhibits significant behavioral complexity. Statechart modeling helps expose subtle interactions — including potential bugs (e.g., alarm reactivating after time change within the one-hour window). Careful modeling and validation are essential for correct implementations of reactive systems.
