Planning under uncertainty
==========================

Introduction
------------

* Decisions under uncertainty.

Planning Under Uncertainty MDP
------------------------------

.. image:: https://dl.dropbox.com/s/4ayem8kvhuo9gvf/Screenshot%202017-04-23%2018.43.49.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/wnt0i78ygvooltt/Screenshot%202017-04-23%2018.45.20.png?dl=0
   :align: center
   :height: 300
   :width: 450

MDP = Markov Decision Processes
POMDP = Partially Observable Markov Decision Processes

.. image:: https://dl.dropbox.com/s/7ezkh8jqj6w8enf/Screenshot%202017-04-23%2018.47.22.png?dl=0
   :align: center
   :height: 300
   :width: 450

Robot Tour Guide Examples
-------------------------

.. image:: https://dl.dropbox.com/s/eodpq3q8dacplqt/Screenshot%202017-04-23%2018.48.56.png?dl=0
   :align: center
   :height: 300
   :width: 450

MDP Grid World
--------------

.. image:: https://dl.dropbox.com/s/f4fpbuxmhbcplp1/Screenshot%202017-04-23%2018.52.28.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/5ebzfmivqfhlb6d/Screenshot%202017-04-23%2018.53.00.png?dl=0
   :align: center
   :height: 300
   :width: 450

Problems with Conventional Planning 1
-------------------------------------

.. image:: https://dl.dropbox.com/s/t8419xkr6c3ms6u/Screenshot%202017-04-23%2018.54.40.png?dl=0
   :align: center
   :height: 300
   :width: 450

Branching Factor is too large
-----------------------------

Quiz: Branching Factor Question

For this problem (and only this problem) assume actions are stochastic
in a way that is different than described in 4. MDP Gridworld.

Instead of an action north possibly going east or west, an action north
will possibly go northeast or northwest (i.e. to the diagonal squares).

Likewise for the other directions e.g. an action west will
possibly go west, northwest or southwest (i.e. to the diagonals).

.. image:: https://dl.dropbox.com/s/z24rz96fwf0aero/Screenshot%202017-04-23%2018.55.49.png?dl=0
   :align: center
   :height: 300
   :width: 450

Problems With Conventional Planning 2
-------------------------------------

.. image:: https://dl.dropbox.com/s/c4029bxl10hqz32/Screenshot%202017-04-23%2018.57.36.png?dl=0
   :align: center
   :height: 300
   :width: 450


Quiz: Policy Question 1
-----------------------

Stochastic actions are as in 4. MDP Grid World.

An action North moves North with 80% chance otherwise East with 10%
chance or West with 10% chance. Likewise for the other directions.

.. image:: https://dl.dropbox.com/s/ih1nn4hl28fcpug/Screenshot%202017-04-23%2018.58.50.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Policy Question 2
-----------------------

Stochastic actions are as in 4. MDP Grid World.

An action North moves North with 80% chance otherwise East with 10%
chance or West with 10% chance. Likewise for the other directions.

.. image:: https://dl.dropbox.com/s/6hf9efi73eiju3v/Screenshot%202017-04-23%2018.59.33.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Policy Question 3
-----------------------

Stochastic actions are as in 4. MDP Grid World.

An action North moves North with 80% chance otherwise East with 10%
chance or West with 10% chance. Likewise for the other directions.

.. image:: https://dl.dropbox.com/s/xg3j0csgtvgcvqr/Screenshot%202017-04-23%2019.11.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

MDP And Costs
-------------

.. image:: https://dl.dropbox.com/s/sqn47yp8n6zw840/Screenshot%202017-04-23%2019.23.37.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/wbn07nf6a7vavv6/Screenshot%202017-04-23%2019.25.14.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/bvymyd4z0ku5p8p/Screenshot%202017-04-23%2019.26.18.png?dl=0
   :align: center
   :height: 300
   :width: 450

Value Iteration 1
-----------------

.. image:: https://dl.dropbox.com/s/yh9ynemskfugtc6/Screenshot%202017-04-23%2019.27.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/2rv714lbhg3bcnz/Screenshot%202017-04-23%2019.27.56.png?dl=0
   :align: center
   :height: 300
   :width: 450

Value Iteration 2
-----------------

.. image:: https://dl.dropbox.com/s/7hm158160xvvcmq/Screenshot%202017-04-23%2019.28.28.png?dl=0
   :align: center
   :height: 300
   :width: 450

Value Iteration 3
-----------------

.. image:: https://dl.dropbox.com/s/h1t9bd58ej5nhkx/Screenshot%202017-04-23%2019.29.22.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/yxwkql6adw6f7zm/Screenshot%202017-04-23%2019.32.01.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/ck02bgdqakd0j6s/Screenshot%202017-04-23%2019.32.37.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/jhjoayu7kdhkcq9/Screenshot%202017-04-23%2019.33.44.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/2vjifcjfia2qemv/Screenshot%202017-04-23%2019.34.36.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Deterministic Question 1
------------------------------

.. image:: https://dl.dropbox.com/s/rrup51mpa7rl1m2/Screenshot%202017-04-23%2019.36.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Deterministic Question 2
------------------------------

.. image:: https://dl.dropbox.com/s/86u0u9wgkc7dzfk/Screenshot%202017-04-23%2019.37.14.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Deterministic Question 3
------------------------------

.. image:: https://dl.dropbox.com/s/58e4aro6s1yd9l6/Screenshot%202017-04-23%2019.38.09.png?dl=0
   :align: center
   :height: 300
   :width: 450

Quiz: Stochastic Question 1
---------------------------

.. image:: https://dl.dropbox.com/s/w5a1876uoyzty8x/Screenshot%202017-04-23%2019.39.37.png?dl=0
   :align: center
   :height: 300
   :width: 450


Quiz: Stochastic Question 2
---------------------------

.. image:: https://dl.dropbox.com/s/9a05m0m60q3qd0u/Screenshot%202017-04-23%2019.42.05.png?dl=0
   :align: center
   :height: 300
   :width: 450

::

   >>> 77 * 0.8 + (0.1 * -100) - 3
   48.6


.. image:: https://dl.dropbox.com/s/1dzh0q1iyyd6k31/Screenshot%202017-04-23%2019.43.48.png?dl=0
   :align: center
   :height: 300
   :width: 450

Value Iterations and Policy 1
-----------------------------

.. image:: https://dl.dropbox.com/s/ejbn6keiw7k9wzv/Screenshot%202017-04-23%2019.44.57.png?dl=0
   :align: center
   :height: 300
   :width: 450


Value Iterations And Policy 2
-----------------------------

.. image:: https://dl.dropbox.com/s/t5mcvqukqaob2s7/Screenshot%202017-04-23%2019.45.43.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/u8b1n00hzol0e3t/Screenshot%202017-04-23%2019.46.29.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/xl4qgv4zh1h2pln/Screenshot%202017-04-23%2019.47.01.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image::  https://dl.dropbox.com/s/s4zngcev3mnuszv/Screenshot%202017-04-23%2019.47.42.png?dl=0
   :align: center
   :height: 300
   :width: 450

Markov Decision Process Conclusion
----------------------------------

.. image:: https://dl.dropbox.com/s/960vdbamvdzhdfy/Screenshot%202017-04-23%2019.49.31.png?dl=0
   :align: center
   :height: 300
   :width: 450

Partial Observability Introduction
----------------------------------

* http://robots.stanford.edu/papers/EmeryMontemerlo04a.pdf

POMDP Vs MDP
------------

.. image:: https://dl.dropbox.com/s/7j1tflgoq7s1g51/Screenshot%202017-04-23%2019.51.24.png?dl=0
   :align: center
   :height: 300
   :width: 450

POMDP
-----

.. image:: https://dl.dropbox.com/s/roxi06ebcz3horb/Screenshot%202017-04-23%2019.52.50.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/10e6a1imtgu6h3y/Screenshot%202017-04-23%2019.53.16.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/nn27k1tu75bml26/Screenshot%202017-04-23%2019.54.21.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/hqygtcsdcnncj4r/Screenshot%202017-04-23%2019.55.26.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/i4silyidx2qf6wi/Screenshot%202017-04-23%2019.56.48.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/1ln9l1d2bkw2exn/Screenshot%202017-04-23%2019.57.17.png?dl=0
   :align: center
   :height: 300
   :width: 450

Planning Under Uncertainity Conclusion
--------------------------------------

.. image:: https://dl.dropbox.com/s/2wu0tdkttvusci0/Screenshot%202017-04-23%2019.58.29.png?dl=0
   :align: center
   :height: 300
   :width: 450

Further Study

Charles Isbell and Michael Littmann’s ML course

* `Markov Decision Processes`_

* `Reinforcement Learning`_

.. _Markov Decision Processes: https://classroom.udacity.com/courses/ud262/lessons/684808907/concepts/last-viewed
.. _Reinforcement Learning: https://classroom.udacity.com/courses/ud262/lessons/643978935/concepts/last-viewed

Peter Norvig and Sebastian Thrun’s AI course:

* `Reinforcement Learning_2`_

.. _Reinforcement Learning_2:  https://classroom.udacity.com/courses/cs271/lessons/48724471/concepts/last-viewed







