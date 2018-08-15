Resources
=========

* The four books recommended and paper listed on Course Wiki: https://www.udacity.com/wiki/ud923/resources/text

Outside of the suggested OS introduction books (especially Three Easy Pieces), I'd say the single book that seems to
have helped most students is "The Linux Programming Interface". I have a copy of this book and found it extremely
useful in understanding the concepts needed for projects 1 and 3. I use it every term for reviewing the material.


Beej's guides are also well regarded and free for browsing online (you can purchase copies as well).

The Linux Man-Pages Project is another excellent source of reference material that I use all the time (easy to browse
through and search for specific system calls). This is maintained by the author of The Linux Programming Interface.


C References:

* MIT course on C programming
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-087-practical-programming-in-c-january-iap-2010/lecture-notes/

* Learn C in X minutes
https://learnxinyminutes.com/docs/c/

http://lynda.gatech.edu (you have free access to Lynda resources, including many C programming tutorials)
C Q&A: coming soon (we have a nice reference from a previous student that we'll post shortly)

http://goshdarnfunctionpointers.com/ (nice resource on pointer syntax from TA Alex)

http://www.cprogramming.com/tutorial/function-pointers.html (another resource on function pointers from TA Hobin)

Presentation on programming with C from Chris D. (with some updates from TAs)
https://docs.google.com/presentation/d/1B7_q_FjpWau-1-A7NFKkDUHLHJMIDKSwCK4dM0nSlXg/edit#slide=id.p18

https://www.youtube.com/watch?v=UmLpG077DcU
Youtube of the Q&A C Video from Chris. D.

Mac GDB
https://www.youtube.com/watch?v=5xFlMD1XPDM

GDB help list
https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf


https://cs50.harvard.edu/
https://reference.cs50.net/
Harvard CS50 course on C and their reference site.

Network programming resources (From TA Eric):



https://beej.us/guide/bgnet/html/multi/syscalls.html
https://www.codeproject.com/Articles/586000/Networking-and-Socket-programming-tutorial-in-C
http://www.binarytides.com/socket-programming-c-linux-tutorial/



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

