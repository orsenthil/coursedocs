Threads Birrell
===============

*An Introduction to Programming with Threads* — Andrew D. Birrell, January 6, 1989.

| Paper:

Introduction
------------

- A **thread** is a single sequential flow of control.
- **Multiple threads** means a program has multiple points of execution at any instant, one per thread.
- Threads executing within a **single address space** can read and write the same memory locations.
- Off-stack (global) variables are shared among all threads.
- Threads are **lightweight** — creation, destruction, and synchronization primitives are cheap.

Why Use Concurrency?
--------------------

- The alternative is multiple separate processes in separate address spaces — expensive to set up, and inter-address-space communication costs are high even with shared segments.
- Threads simplify I/O by treating device requests as sequential (suspending the invoking thread until completion) while the program does other work in other threads.
- Threads can **defer work** — e.g., return to the caller before re-balancing a tree. This is powerful even on a uniprocessor.
- Reducing latency improves responsiveness even if total work is the same.

Design of a Thread Facility
----------------------------

Four major mechanisms: **thread creation**, **mutual exclusion**, **waiting for events**, and **alert** (getting a thread out of an unwanted long-term wait).

Thread Creation
~~~~~~~~~~~~~~~

A thread is created by calling ``Fork``, giving it a procedure and an argument record. ``REFANY`` is a dynamically typed pointer to garbage-collected storage.

.. code-block:: modula3

   TYPE Thread;
   TYPE Forkee = PROCEDURE(REFANY): REFANY;
   PROCEDURE Fork(proc: Forkee; arg: REFANY): Thread;
   PROCEDURE Join(thread: Thread): REFANY;

The following executes ``a(x)`` and ``b(y)`` in parallel, assigning the result of ``a(x)`` to ``q``:

.. code-block:: modula3

   VAR t: Thread;
   t := Fork(a, x);
   p := b(y);
   q := Join(t);

- Most forked threads are permanent daemon threads, have no results, or communicate results via synchronization rather than ``Join``.
- If a thread's initial procedure returns with no subsequent ``Join``, the thread quietly evaporates.

Mutual Exclusion
~~~~~~~~~~~~~~~~

- The simplest thread interaction is through shared memory access.
- **Mutual exclusion** (critical sections) ensures only one thread executes a particular region of code at a time.
- Achieve mutual exclusion by associating variables with a **mutex** and accessing them only from a thread holding the mutex (inside a ``LOCK`` clause).

.. code-block:: modula3

   TYPE Mutex;
   LOCK mutex DO ... statements ... END;

Condition Variables
~~~~~~~~~~~~~~~~~~~

The shared memory accessed inside the ``LOCK`` clause is the scheduled resource; the scheduling policy is one thread at a time.

.. code-block:: modula3

   TYPE Condition;
   PROCEDURE Wait(m: Mutex; c: Condition);
   PROCEDURE Signal(c: Condition);
   PROCEDURE Broadcast(c: Condition);

- A thread locks the mutex and examines shared data. If the resource is available, it continues. If not, it unlocks the mutex and blocks by calling ``Wait``.
- Another thread later makes the resource available and awakens the waiting thread via ``Signal`` or ``Broadcast``.

Alerts
~~~~~~

Alerts are the exception mechanism for threads — used to interrupt a thread stuck in an unwanted long-term wait.

Deadlocks
~~~~~~~~~

The most effective rule for avoiding deadlocks: apply a **partial order** to mutex acquisition. For any pair of mutexes {M1, M2}, every thread that needs both must lock them in the same order (e.g., always M1 before M2). This completely avoids mutex-only deadlocks, though condition variables can introduce additional deadlock scenarios.

Complexity
~~~~~~~~~~

Spurious wake-ups, lock conflicts, and starvation add complexity to concurrent programs.
