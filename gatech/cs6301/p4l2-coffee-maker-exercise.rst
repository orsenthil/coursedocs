.. title: P4L2 Coffee Maker Exercise 
.. slug: P4L2 Coffee Maker Exercise 
.. date: 2016-05-27 23:58:20 UTC-08:00
.. tags: notes, mathjax
.. category: 
.. link: 
.. description: 
.. type: text

P4L2 Coffee Maker Exercise
==========================

This lesson walks through Robert Martin's coffee maker exercise, contrasting traditional OOA (noun-based) design with a **use-case-driven, role-based** approach, and applying the **Dependency Inversion Principle** to promote reuse.

The Mark IV Special Coffee Maker
---------------------------------

**Functional description:**

- Makes up to 12 cups of coffee
- User fills filter with grounds, slides filter into receptacle
- User adds water to the water strainer and presses the Brew button
- Water is heated to boiling; steam pressure forces water over grounds
- Coffee drips through filter into pot
- Warmer plate keeps pot warm (only activates when coffee is present)
- Removing pot mid-brew stops water flow (prevents spilling on warmer plate)

**Hardware components:**

- Boiler (heater + water sensor)
- Warmer plate (heater + pot/coffee sensor)
- Brew button
- Indicator light (brewing complete)
- Pressure relief valve (safety)

A Java API provides methods to query/control each hardware device and symbolic constants for device states.

Traditional OOA Approach
-------------------------

The noun-extraction approach identifies classes from the problem statement: coffee maker (facade), user interface (button, light), boiler (sensor, heater), warmer plate (sensor, heater). This yields an inheritance hierarchy with abstract Heater and Sensor classes.

**Limitations:** This approach over-centralizes knowledge and couples the design to the specific hardware. Things that change independently should be in separate classes. The resulting design is rigid and hard to extend to the Mark V.

Use-Case-Driven Approach
--------------------------

Instead of starting with nouns, Martin starts with **use cases**:

1. **User presses Brew button** — UI detects event, checks hot water source readiness, checks containment vessel readiness, starts boiler
2. **Containment vessel not ready** — if pot is absent (or removed mid-brew), stop water flow; when pot returns, resume flow
3. **Brewing complete** — turn off boiler, turn on warmer plate, signal "coffee ready" light, inform containment vessel that pot is full
4. **Coffee all gone** — turn off warmer plate, turn off "ready" indicator

Each use case is expressed as a **UML collaboration diagram** showing messages between objects. Diagrams are composed together (labeled A1, A2... B1, B2... for each use case) to build a complete picture of the system's behavior.

The result: three classes — **UserInterface**, **HotWaterSource**, **ContainmentVessel** — derived from their behavioral roles rather than from nouns.

Role-Based Design
------------------

The process:

1. Enumerate use cases
2. For each use case, construct/elaborate a collaboration diagram
3. Reinterpret the collaboration diagram as a class model (arrows = dependencies, rectangles = classes)
4. Each class participates in multiple roles (one per use case it appears in)
5. The overall behavior of a class is the **sum of its roles**

Dependency Inversion Principle
-------------------------------

**Problem:** If the three behavioral classes directly call the Mark IV hardware API, they cannot be reused for the Mark V.

**Solution — Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules. Both should depend on abstractions.

- Express the three classes as **abstract classes** with abstract methods
- Subclass each for the Mark IV; subclass implementations call the hardware API
- Inter-class communication uses abstract method calls, never Mark IV specifics

**Analogy:** A lamp depends on the abstract plug interface, not on the underlying wiring — enabling any device to be plugged in.

**Result:** A class model with three abstract classes (UserInterface, HotWaterSource, ContainmentVessel) and three Mark IV subclasses that implement the hardware-specific behavior.

.. mermaid::

   classDiagram
       class UserInterface {
           <<abstract>>
           +checkBrewButton()*
           +signalBrewingComplete()*
       }
       class HotWaterSource {
           <<abstract>>
           +isReady()*
           +start()*
           +stop()*
       }
       class ContainmentVessel {
           <<abstract>>
           +isReady()*
           +potPresent()*
           +setFull()*
       }
       class M4UserInterface {
           +checkBrewButton()
           +signalBrewingComplete()
       }
       class M4HotWaterSource {
           +isReady()
           +start()
           +stop()
       }
       class M4ContainmentVessel {
           +isReady()
           +potPresent()
           +setFull()
       }

       UserInterface <|-- M4UserInterface
       HotWaterSource <|-- M4HotWaterSource
       ContainmentVessel <|-- M4ContainmentVessel
       UserInterface --> HotWaterSource
       UserInterface --> ContainmentVessel
       HotWaterSource --> ContainmentVessel

Summary
--------

- Traditional OOA (noun extraction) does not always yield the best design
- **Use-case-driven role-based design** derives classes from behavior, not structure
- **Dependency Inversion** decouples high-level policy from low-level implementation, promoting reuse across product generations
