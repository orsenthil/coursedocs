Threads Birrell
===============

.. code-block:: c

    * An Introduction to Programming with Threads.
    ** Andrew D. Birrell.
    ** Date: Jan-6, 1989
    ** Reading: Oct-3-2018

    * Introduction
    ** A “thread” is a straightforward concept: a single sequential flow of control.
    ** Having “multiple threads” in a program means that at any instant the program hasmultiple points of execution, one in each of its threads.
    ** Having the threads execute within a “single address space” means that the computer’saddressing hardware is configured so as to permit the threads to read and write the samememory locations.
    ** off-stack (global) variables are shared among all the threads.
    ** “lightweight”. This means that threadcreation, existence, destruction and synchronization primitives are cheap.

    * Why use concurrency?

    ** The alternative, with most conventional operating systems, is to configure your program asmultiple separate processes, running in separate address spaces. This tends to be expensiveto set up, and the costs of communicating between address spaces are often high, even inthe presence of shared segments.
    ** Threads by adopting an attitude that devicerequests are all sequential (i.e. they suspend execution of the invoking thread until therequest completes), and that the program meanwhile does other work in other threads.
    ** For example, when you add or remove something ina balanced tree you could happily return to the caller before re-balancing the tree.
    ** Adding threads to defer work is apowerful technique, even on a uni-processor.
    ** Even if the same total work is done,reducing latency can improve the responsiveness of your program.

    * The Design of a thread facility.

    ** four major mechanisms: thread creation, mutual exclusion, waiting for events, and some arrangementfor getting a thread out of an unwanted long-term wait.

    ** Thread creation.
    *** A thread is created by calling “Fork”, giving it a procedure and an argument record.
    *** The type REFANY means a dynamically typed pointer to garbage-collected storage.

        ~
        TYPE Thread;
        TYPE Forkee = PROCEDURE(REFANY): REFANY;
        PROCEDURE Fork(proc: Forkee; arg: REFANY): Thread;
        PROCEDURE Join(thread: Thread): REFANY;
        ~

    ***  following program fragment executes theprocedure calls “a(x)” and “b(y)” in parallel, and assigns the result of calling “a(x)” to thevariable “q”.

    ~VAR t: Thread;
    t := Fork(a, x);
    p := b(y);
    q := Join(t);~

    *** Most forked threads are permanent dæmon threads, orhave no results, or communicate their results by some synchronization arrangement otherthan “Join”.
    *** If a thread’s initial procedure has returned and there is no subsequent call of“Join”, the thread quietly evaporates.

    ** Mutual Exclusion.

    *** The simplest way that threads interact is through access to shared memory.
    *** primitive that offers mutual exclusion (sometimes called critical sections), specifying fora particular region of code that only one thread can execute there at any time.
    *** The programmer can achieve mutual exclusion on a set of variables by associatingthem with a mutex, and accessing the variables only from a thread that holds the mutex(i.e., from a thread executing inside a LOCK clause that has locked the mutex).

    ~
    TYPE Mutex;
    LOCK mutex DO ... statements ... END;
    ~

    ** Conditional Variables

    *** The resourcebeing scheduled is the shared memory accessed inside the LOCK clause, and the schedulingpolicy is one thread at a time.

    ~
    TYPE Condition;
    PROCEDURE Wait(m: Mutex; c: Condition);
    PROCEDURE Signal(c: Condition);
    PROCEDURE Broadcast(c: Condition);
    ~

    *** If a thread wants the resource, it locks the mutex andexamines the shared data. If the resource is available, the thread continues. If not, thethread unlocks the mutex and blocks, by calling “Wait”. Later, when some other threadmakes the resource available it awakens the first thread by calling “Signal” or “Broadcast”.

    ** Alerts

    *** Alerts are exceptions fot threads.

    ** Deadlocks

    *** The most effective rule for avoiding such deadlocks is to apply a partial order to theacquisition of mutexes in your program. In other words, arrange that for any pair ofmutexes { M1, M2 }, each thread that needs to hold M1 and M2 simultaneously locksM1 and M2 in the same order (for example, M1 is always locked before M2). This rulecompletely avoids deadlocks involving only mutexes (though as we will see later, thereare other potential deadlocks when your program uses condition variables).

    ** Complexity

    *** worrying about these spurious wake-ups, lock conflicts and starvationmakes the program more complicated.
