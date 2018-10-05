Beyond MultiProcessing
======================

Eykholt, J.R., et. al., "Beyond Multiprocessing: Multithreading the Sun OS Kernel".

https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-eykholt-paper.pdf

Introduction
------------

It was important for the kernel to be capable of a high degree of concurrency on tightly coupled symmetric multiprocessors, but it was also a goal to support more than one thread of control within a user process.

We also wanted the kernel to be capable of bounded dispatch latency for real-time threads.

Real-time response requires absolute control over scheduling, requiring preemption at almost any point in the kernel, and elimination of unbounded priority inversions wherever possible.

Threads can be used by user applications as a structuring technique to manage multiple asynchronous activities.

Overview of the Kernel Architecture
-----------------------------------

Switching between kernel threads does not require a change of virtual memory address space information, so it is relatively inexpensive.

Kernel threads are fully preemptible and may be scheduled by any of the scheduling classes in the system, including the real-time (fixed priority) class.

Since all other exe- cution entities are built using kernel threads, they represent a fully preemptible, real-time ‘‘nucleus’’ within the kernel.

Kernel threads use synchronization primitives that support protocols for preventing priority inversion, so a thread’s priority is determined by which activities it is impeding by holding locks as well as by the service it is performing [Khanna 1992].

SunOS uses kernel threads to provide asynchro- nous kernel activity, such as asynchronous writes to disk, servicing STREAMS queues, and callouts.


Even interrupts are handled by kernel threads.

A major feature of the new kernel is its support of multiple kernel-supported threads of control, called lightweight processes (LWPs), in any user pro- cess, sharing the address space of the process and other resources, such as open files.

.. image:: https://dl.dropbox.com/s/4h0riy41e0shy9m/Screenshot%202018-10-04%2021.59.44.png?dl=0
   :align: center
   :height: 300
   :width: 450


While all LWPs have a kernel thread, not all kernel threads have an LWP

A user-level library uses LWPs to implement user-level threads. In addition, it allows a user process to have thousands of threads, without overwhelming kernel resources.

Data structures
---------------

The per-process data was divided between non-swappable data in the proc structure, and swappable data in the user structure.

The per-process data is contained in the proc structure. It contains a list of kernel threads associ- ated with the process, a pointer to the process address space, user credentials, and the list of signal handlers. The proc structure also contains the ves- tigial user structure, which is now much smaller than a page, and is no longer practical to swap.

The LWP structure contains the per-LWP data such as the process-control-block (pcb) for storing user-level processor registers, system call arguments, signal handling masks, resource usage information, and profiling pointers.


.. image:: https://dl.dropbox.com/s/p5wc0vhg1stafqa/Screenshot%202018-10-04%2022.46.57.png?dl=0
   :align: center
   :height: 300
   :width: 450

 The current LWP, process, and CPU structures are quickly accessible through pointers in the thread structure.

Kernel Thread Scheduling
------------------------

A scheduling class determines the relative priority of processes within the class, and converts that priority to a global priority.

scheduling classes currently supported are system, timesharing, and real-time (fixed-priority).

In addition, user code run by an underlying kernel thread of sufficient priority (e.g., real-time threads) will execute even though other lower priority kernel threads wait for execution resources.

System Threads
--------------

threads have no need for LWP structures, so the thread structure and stack for these threads can be allocated together in a non- swappable area.

.. image:: https://dl.dropbox.com/s/5swyk785aobjaok/Screenshot%202018-10-04%2023.12.43.png?dl=0
   :align: center
   :height: 300
   :width: 450

Synchronization Architecture
----------------------------

These are mutual exclusion locks (mutexes), condition variables, sema- phores, and multiple readers, single writer (readers/writer) locks.

Note that kernel synchronization primitives must use a different type name than user synchronization primitives so that the types are not confused in applications that read internal kernel data structures.

By default, the kernel thread synchronization primitives that can logically block, can potentially sleep.

Mutual Exclusion Lock Implementation
------------------------------------


Turnstiles vs Queues in Synchronization Objects
-----------------------------------------------

Instead, two bytes in the synchronization object are used to find a turnstile structure containing the sleep queue header and priority inheritance information [Khanna 1992]. Turnstiles are preallocated such that there are always more turnstiles than the number of threads active.


One alternative method would be to select the sleep queue from an array using a hash function on the address of the synchronization object.

Interrupts as Threads
---------------------

Lastly, interrupt handlers must live in a constrained environment that avoids any use of kernel functions that can poten- tially sleep, even for short periods.

The restructured kernel uses a primitive spin lock protected by raised priority to implement this. This is one of a few bounded sections of code where interrupts are locked out.


Implementing Interrupts as Threads
----------------------------------

When the interrupt returns, we restore the state of the interrupted thread and return.

Interrupts may nest. An interrupt thread may itself be interrupted and be pinned by another interrupt thread.

A flag is set in the cpu structure indicating that an interrupt at that level has blocked, and the minimum interrupt level is noted.

Interrupt Thread Cost
---------------------







