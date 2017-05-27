Overview of Compilation
=======================


1.1 Introduction
----------------


Why Study Compiler Construction
_______________________________


A good compiler contains a microcosm of computer science. It makes practical use of greedy algorithms
(register allocation), heuristic search techniques (list scheduling), graph algorithms (dead-code
elimination), dynamic programming (instruction selection), finite automata and push-down automata
(scanning and parsing), and fixed-point algorithms (data-flow analysis). It deals with problems
such as dynamic allocation, synchronization, naming, locality, memory hierarchy management, and
pipeline scheduling. Few software systems bring together as many complex and diverse components.

Working inside a compiler provides practical experience in software
engineering that is hard to obtain with smaller, less intricate systems.


The Fundamental Principles of Compilation
_________________________________________

* The compiler must preserve the meaning of the program being compiled.

* The compiler must improve the input program in some discernible way.



1.3.1 The Front End
-------------------

Checking Syntax
_______________

The first step in understanding the syntax of this sentence is to identify distinct words in the input
program and to classify each word with a part of speech. In a compiler, this task falls to a pass
called the scanner. The scanner takes a stream of characters and converts it to a stream of classified
words—that is, pairs of the form (p,s), where p is the word’s part of speech and s is its spelling.


The process of automatically finding derivations is called parsing.
