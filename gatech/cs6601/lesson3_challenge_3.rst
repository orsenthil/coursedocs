Lesson 3 Challenge 2
====================


.. image:: https://dl.dropbox.com/s/4ui8j7mnms7alrw/Screenshot%202017-03-05%2022.07.48.png
   :align: center
   :height: 300
   :width: 450

1. delta(E) = (60 - 100) = -40 = P = e^(-40/50)
2. delta(E) = (120 - 200) = -80 = P = e^(-80/50)
3. delta(E) = (25 - 100) = -75 = P = e^(-75/150)
4. delta(E) = (210 - 200) = P = 1
5. delta(E) = (150 - 100) = P = 1
6. delta(E) = (40 - 200) = P  = e^(-160/300) = 0.58

----

00100 = 1 =  1/8
11000 = 2 = 1/4
01001 = 2 = 1/4
10010 = 2 = 1/4
00100 = 1 = 1/8

Sum = 8

   01001 -    01010  -> 01011  -> 3
   10010 ->   10001  -> 11001  -> 3


----

a) node names
b) arc names


x11 x12 x13 x14
x21 x22 x23 x24
x31 x32 x33 x34
x41 x42 x43 x44

a) all_different(x11, .. x14) and for all other rows
b) all_different(x11, .. x41) and for all other cols.
c) all_different(x11, x12, x21, x22)
d) all_different(x13, x14, x23, x24) ditto

Algorithm:

a) Forward Checking.
b) Minimum Remaining Value Heuristic.

----

appetizer
- v
- e

main-course
- f
- p
- f,p

Constraint: e -> (f, p, fp)



