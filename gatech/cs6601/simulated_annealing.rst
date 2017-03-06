Simulated Annealing
===================

Traveling Salesman Problem
--------------------------

.. image:: https://dl.dropbox.com/s/41ydapm0xkm6w88/Screenshot%202017-03-05%2016.47.35.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/f6u24ixpdme18fn/Screenshot%202017-03-05%2016.49.01.png
   :align: center
   :height: 300
   :width: 450

* Salesman has to visit 5 cities.
* Must return back the same city he started from.
* What is the efficient order of flights to minimize the overall distance flown.
* NP-Hard. Non Deterministic Polynomial.
* Uncross the paths where the paths crossed.
* Doing this iteratively.


Methods to help find the global maximum
---------------------------------------

.. image:: https://dl.dropbox.com/s/ik7p38pb6e0njhi/Screenshot%202017-03-05%2016.58.35.png
   :align: center
   :height: 300
   :width: 450

4-Queens
--------

.. image:: https://dl.dropbox.com/s/8m7q0o5ehny05is/Screenshot%202017-03-05%2017.00.37.png
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/js51nyzucwvjlao/Screenshot%202017-03-05%2017.01.14.png
   :align: center
   :height: 300
   :width: 450

5-Queens
--------

.. image:: https://dl.dropbox.com/s/hmznjxrr5b8g5lm/Screenshot%202017-03-05%2017.03.36.png
   :align: center
   :height: 300
   :width: 450

n-Queens Heuristic Function
---------------------------

.. image:: https://dl.dropbox.com/s/fq6z15jws7ejxbx/Screenshot%202017-03-05%2017.20.01.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/4jyc22wi7lr6pht/Screenshot%202017-03-05%2017.20.25.png
   :align: center
   :height: 300
   :width: 450

n-Queens local Minima
---------------------

.. image:: https://dl.dropbox.com/s/i2i1g69hi4zwrpr/Screenshot%202017-03-05%2017.21.34.png
   :align: center
   :height: 300
   :width: 450

Local Maxima
------------

.. image:: https://dl.dropbox.com/s/0r57f8wvxugduwc/Screenshot%202017-03-05%2017.24.11.png
   :align: center
   :height: 300
   :width: 450


Random Restarts
---------------

.. image:: https://dl.dropbox.com/s/ti899qffhlrijbw/Screenshot%202017-03-05%2017.25.32.png
   :align: center
   :height: 300
   :width: 450

* Avoid the paths that we have already considered.

Hill-Climbing Quiz
------------------

.. image:: https://dl.dropbox.com/s/rvkia2t4n5pj397/Screenshot%202017-03-05%2017.29.23.png
   :align: center
   :height: 300
   :width: 450

Step Size Too Small
-------------------

.. image:: https://dl.dropbox.com/s/pxc19ybqhy5ig7r/Screenshot%202017-03-05%2017.30.57.png
   :align: center
   :height: 300
   :width: 450

* With Small Steps you can get struck in the flat "Shoulder".


Step Size Too Large
-------------------

.. image:: https://dl.dropbox.com/s/dv0mlxcn4q81uu8/Screenshot%202017-03-05%2017.31.55.png
   :align: center
   :height: 300
   :width: 450

* Miss Sharp Hills Completely.
* Infinite Loop and never Terminate.
* Algorithm can oscillate and never terminate.

* Start with a large step-size and reduce the step-size with the smaller step-size.

Hill-Climbing Quiz 2
--------------------

.. image:: https://dl.dropbox.com/s/rksd8v0ephdglbx/Screenshot%202017-03-05%2017.48.09.png
   :align: center
   :height: 300
   :width: 450

Annealing
---------

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/IronAlfa%26IronGamma.svg/640px-IronAlfa%26IronGamma.svg.png
   :align: center
   :height: 300
   :width: 450

* Wikipedia: https://en.wikipedia.org/wiki/Simulated_annealing
* Energy Minimization
* When the energy of the molecule reduces, the molecules arrange themselves in the lowest energy configuration and
  they form patterns like mud-cracks or honey combs.
* Honey-combs. Honeybees tries to optimize their storage space and minimize the structure they are building.

Simulated Annealing
-------------------

.. image:: https://dl.dropbox.com/s/pstt0hnnnbwz8a3/Screenshot%202017-03-05%2017.57.33.png
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/bqiyqpgcp8u6e3v/Screenshot%202017-03-05%2018.04.18.png
   :align: center
   :height: 300
   :width: 450

* T is the simulated temperature at time t, which reduces from a high value at the beginning to near zero eventually.

* :math:`\deltaE` is the change in energy going from current to next.

* When T is small, it is normal hill-climbing.

.. image:: https://www.dropbox.com/s/ak6llq06hpon7j2/Screenshot%202017-03-05%2018.07.57.png?dl=0
   :align: center
   :height: 300
   :width: 450

* When :math:`\deltaE` is 0, we will get struck in a plateau. But eventually, we will random walk off the plateau.

Local Beam Search
-----------------

.. image:: https://dl.dropbox.com/s/wvsf422tpvfdhe1/Screenshot%202017-03-05%2018.14.28.png
   :align: center
   :height: 300
   :width: 450

* K-particles.
* Each time frame, we keep track of randomly generated neighbours of these particles and keep the k best ones for the
  next iteration.

Representing n-Queens
---------------------

.. image:: https://dl.dropbox.com/s/ns7t6ggg4l2cnc9/Screenshot%202017-03-05%2018.16.06.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/dpabgd95llxh9ge/Screenshot%202017-03-05%2018.16.30.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/vcrahkjcqsbiovm/Screenshot%202017-03-05%2018.17.24.png
   :align: center
   :height: 300
   :width: 450

Genetic Algorithms
------------------

.. image:: https://dl.dropbox.com/s/jf8sv1x52qipln7/Screenshot%202017-03-05%2018.19.09.png
   :align: center
   :height: 300
   :width: 450

* The fitness function

.. math::

   28 - number_of_attacking_pairs


.. image:: https://dl.dropbox.com/s/iaqhibtl171g52o/Screenshot%202017-03-05%2018.23.48.png
   :align: center
   :height: 300
   :width: 450

* Add the four scores and normalize them to a percentage.

.. image:: https://dl.dropbox.com/s/pj10x1e5ub8nct7/Screenshot%202017-03-05%2018.44.14.png
   :align: center
   :height: 300
   :width: 450


* We roll a 100 sided die to select the first parent.
* 1-31 - First Board. 32 - to 60 second one, 61 to 90 - third one, 90 to 100 - fourth.

.. image:: https://dl.dropbox.com/s/s1vm7z3ehctnunt/Screenshot%202017-03-05%2018.54.08.png
   :align: center
   :height: 300
   :width: 450

* After rolling die, we selected the parents in the second column here.

.. image:: https://dl.dropbox.com/s/bpt7mo78jlorqzd/Screenshot%202017-03-05%2018.55.23.png
   :align: center
   :height: 300
   :width: 450

* Using Crossover.
* Take the first-part and tack them to the second part.

GA Crossover
------------

.. image:: https://dl.dropbox.com/s/pqqs6e2z4ehjq6w/Screenshot%202017-03-05%2018.58.03.png
   :align: center
   :height: 300
   :width: 450

GA Mutation
-----------

* What if there is a critical part of the solution that is in none of the parents.
* More randomness. Just like mutations in biology, we are going to use mutations in genetic algorithms.

.. image:: https://dl.dropbox.com/s/n0ild46s46jqwjv/Screenshot%202017-03-05%2019.07.49.png
   :align: center
   :height: 300
   :width: 450

* How many generations are needed to get a good answer.

GA Crossover Quiz
-----------------

.. image:: https://dl.dropbox.com/s/r3425jt4virfwqm/Screenshot%202017-03-05%2019.09.23.png
   :align: center
   :height: 300
   :width: 450

* Without mutation, we run the risk of never actually reaching the goal.

