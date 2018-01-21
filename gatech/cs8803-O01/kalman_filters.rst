Kalman Filters
==============

Introduction
------------


Stanley: The Robot that Won the DARPA Grand Challenge
+++++++++++++++++++++++++++++++++++++++++++++++++++++

* https://en.wikipedia.org/wiki/Stanley_(vehicle)
* http://robots.stanford.edu/papers/thrun.stanley05.pdf

The robots software system relied predominantly on state-of-the-art artificial intelligence technologies such as
machine learning and probabilistic reasoning.

Tracking intro
--------------

* Kalman Filter - Continuous - Uni-modal distribution.
* Monte Carlo localization. - discrete - multi-modal distribution.

.. image:: https://dl.dropbox.com/s/sltbfawwq2q0lun/Screenshot%202018-01-21%2011.39.54.png?dl=0
   :align: center
   :height: 300
   :width: 450

Gaussian Intro
--------------

.. image:: https://dl.dropbox.com/s/30ql57x15keiqtt/Screenshot%202018-01-21%2011.48.10.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/y8hnmvpf0iov3u9/Screenshot%202018-01-21%2011.49.51.png?dl=0
   :align: center
   :height: 300
   :width: 450

Variance Comparison
-------------------

* Co-variance.
* What's the difference between variance and co-variance?


Preferred Gaussian
------------------

.. image:: https://dl.dropbox.com/s/5sgv07choujs8hk/Screenshot%202018-01-21%2012.08.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

Evaluate Gaussian
-----------------

.. code-block:: python

    def gaussian(u, s2, x):
        # u is mu, s2 is sigma-squared, x is variable x.
        return (1.0/math.sqrt(2 * math.pi * s2)) * math.exp(((-1.0/2) * (x - u) * (x-u)) / s2)

Maximize Gaussian
-----------------

.. code-block:: python

    from math import *

    def f(mu, sigma2, x):
        return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

    print f(10.,4.,10.)


Measurement and Motion 1
------------------------

Kalman Filter
+++++++++++++

Measurement updates and motion updates.

.. image:: https://dl.dropbox.com/s/ra2vy5p9vo1fmz9/Screenshot%202018-01-21%2012.25.21.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. attention::

   What's a Convolution?

   A function derived from two given functions by integration that expresses how the shape of one is modified by the
    other.
