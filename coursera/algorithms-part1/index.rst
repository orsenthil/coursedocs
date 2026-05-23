Algorithms, Part I — Princeton University
=========================================

Course: https://www.coursera.org/learn/algorithms-part1/home/welcome


Union Find
----------

**Dynamic connectivity problem** — given a set of N objects, support:

- *Are objects p and q connected?*
- *Connect objects p and q.*

**Union-find data type** — implementations covered:

- Quick Find
- Quick Union
- Weighted Quick Union
- Weighted Quick Union with Path Compression

**Application: Percolation** — given a grid of open/blocked sites, determine whether fluid can percolate from top to bottom. Models problems in physical chemistry (electrical conductivity of composite materials, fluid flow through porous media).

A good algorithm (weighted quick union) makes the difference between solving this efficiently and not at all.

Resources
~~~~~~~~~

- `Lecture slides <https://www.coursera.org/learn/algorithms-part1/supplement/bcelg/lecture-slides>`_
- `Percolation assignment <https://www.coursera.org/learn/algorithms-part1/programming/Lhp5z/percolation>`_
- `Problem statement <http://coursera.cs.princeton.edu/algs4/assignments/percolation.html>`_


Queues
------

**Programming assignment:** http://coursera.cs.princeton.edu/algs4/assignments/queues.html


Programming Environment Setup
-----------------------------

Java
~~~~

- `Download and install Java 8 <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_
- If multiple JDKs are installed, set ``JAVA_HOME``:

.. code-block:: shell

    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk/Contents/Home

Princeton algs4 environment (Mac)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install from http://algs4.cs.princeton.edu/mac/ — the ``algs4.app`` installer sets up:

1. **Java 8** — verifies ``javac`` and ``java`` versions
2. **Textbook libraries** — ``algs4.jar`` at ``/usr/local/algs4/``
3. **Checkstyle** — code style checking (``checkstyle-algs4``, ``checkstyle-cos226``)
4. **FindBugs** — static analysis (``findbugs-algs4``, ``findbugs-cos226``)
5. **DrJava** — IDE with algs4 classpath preconfigured
6. **Wrapper scripts** — ``java-algs4``, ``javac-algs4``, ``java-cos226``, ``javac-cos226`` in ``/usr/local/bin/``

Installation log: ``/usr/local/algs4/log.txt``

Assignment submission
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    zip percolation.zip Percolation.java PercolationStats.java
