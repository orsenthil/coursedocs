Resources
=========

* The four books recommended and paper listed on Course Wiki: https://www.udacity.com/wiki/ud923/resources/text

.. raw::

    Silberschatz, Galvin, and Gagne.
    Operating System Concepts.
    Wiley, 9th Edition, December 17, 2012.

    Silberschatz, Galvin, and Gagne.
    Operating System Concepts: Essentials.
    Wiley, 2nd Edition, November 18, 2013.

    Tanenbaum and Bos.
    Modern Operating Systems.
    Wiley, 4th Edition, December 17, 2012.

    Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau.
    Operating Systems: Three Easy Pieces.
    Arpaci-Dusseau Books, Version 0.80, May 2014.



Beej's guides are also well regarded and free for browsing online (you can purchase copies as well).

The Linux Man-Pages Project is another excellent source of reference material that I use all the time (easy to browse
through and search for specific system calls). This is maintained by the author of The Linux Programming Interface.


C References:

* `MIT course on C programming`_

.. _MIT course on C programming: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/lecture-notes/

* `Learn C in X minutes`_

.. _Learn C in X minutes: https://learnxinyminutes.com/docs/c/

* `Lynda`_

.. _Lynda: http://lynda.gatech.edu

* `Gosh Darn Function Pointers`_

.. _Gosh Darn Function Pointers: http://goshdarnfunctionpointers.com/

* `Function Pointers`_

.. _Function Pointers: http://www.cprogramming.com/tutorial/function-pointers.html

* `Presentation on programming with C from Chris D.`_

.. _Presentation on programming with C from Chris D.: https://docs.google.com/presentation/d/1B7_q_FjpWau-1-A7NFKkDUHLHJMIDKSwCK4dM0nSlXg/edit#slide=id.p18

* `Youtube of the Q&A C Video from Chris. D.`_

..  _Youtube of the Q&A C Video from Chris. D.: https://www.youtube.com/watch?v=UmLpG077DcU

* `Mac GDB`_

.. _Mac GDB: https://www.youtube.com/watch?v=5xFlMD1XPDM

* `GDB help list`_

.. _GDB help list: https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf

Harvard CS50 course on C and their reference site.

* `CS 50`_

* `CS 50 Reference`_

* `typedef example`_

.. _CS 50: https://cs50.harvard.edu/

.. _CS 50 Reference: https://reference.cs50.net/

.. _typedef example: https://overiq.com/c-programming/101/typedef-statement-in-c/#typedef-with-a-structure

CS Education
------------

* http://cs-education.github.io/sys/#

* Essential C (http://cslibrary.stanford.edu/101/)

* Pointers and Memory (http://cslibrary.stanford.edu/102/)

* Linked list Basics (http://cslibrary.stanford.edu/103/)

* Point Fun With Binky Video (http://cslibrary.stanford.edu/104/)

* Linked List Problems (http://cslibrary.stanford.edu/105/)


A pointer type in C is just the pointee type followed by a asterisk (*)...

::

   int* - type: pointer to int
   float* - type: pointer to float
   struct fraction* - type: pointer to struct fraction
   struct fraction** - type: pointer to struct fraction*


.. image::  https://dl.dropbox.com/s/i8j55mnop7p68cz/Screenshot%202018-08-14%2023.22.27.png?dl=0
   :align: center
   :height: 300
   :width: 450


Why are pointer bugs so common?

Try to remember to assign your pointers to refer to pointees. Don't be surprised when you forget.

