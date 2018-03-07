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

* https://en.wikipedia.org/wiki/Unimodality
* https://en.wikipedia.org/wiki/Multimodal_distribution

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

   A function derived from two given functions by integration that expresses how the shape of one is modified by
   the other.

In localization, performing a measurement meant updating our belief by a multiplicative factor, while moving involved performing a convolution.


Measurement and Motion 2
------------------------

.. image:: https://dl.dropbox.com/s/rlv7v2w0ncdwz2p/Screenshot%202018-01-21%2012.31.29.png?dl=0
   :align: center
   :height: 300
   :width: 450


The measurement meant updating our belief (and renormalizing our distribution). Motion meant keeping track of where
all of our probability "went" when we moved (which meant using the law of Total Probability).

Shifting the mean
-----------------

.. image:: https://dl.dropbox.com/s/1dv93nsbzx5w2zx/Screenshot%202018-01-21%2012.36.42.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/2nz7ya70893h0fp/Screenshot%202018-01-21%2012.38.27.png?dl=0
   :align: center
   :height: 300
   :width: 450

Predicting the Peak
-------------------

.. image:: https://dl.dropbox.com/s/quan7d72vvya3di/Screenshot%202018-01-21%2012.40.33.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. attention::

    The new belief will be more certain than either the previous belief OR the measurement.
    The takeaway lesson here: more measurements means greater certainty.

Parameter Update
----------------

.. image:: https://dl.dropbox.com/s/wvyuh12ylmowpza/Screenshot%202018-01-21%2012.52.53.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/lzbofx39l4r67l4/Screenshot%202018-01-21%2012.53.49.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. code-block:: python

    def new_mean(mu_1, sigma2_1, mu_2, sigma2_2):
        return (1.0/(sigma2_1 + sigma2_2)) * (sigma2_2 * mu_1 + sigma2_1 * mu_2)


    def new_sigma2(sigma2_1, sigma2_2):
        return (1.0/((1.0/sigma2_1) + (1.0/sigma2_2)))

.. image:: https://dl.dropbox.com/s/x6oq8de5zbn0x06/Screenshot%202018-01-21%2013.01.19.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. attention::

   New Variance term is half the size of the previous variance terms. Why is it drawn narrow?

Parameter Update 2
------------------


.. image:: https://dl.dropbox.com/s/m1cs3zbqkyhmz1o/Screenshot%202018-01-21%2013.10.26.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. attention::

   Notice that the new mean is between the previous two means and the new variance is LESS than either of the
   previous variances.

Separated Gaussians
-------------------

.. image:: https://dl.dropbox.com/s/mcy3tcratp4dl6b/Screenshot%202018-01-21%2013.15.33.png?dl=0
   :align: center
   :height: 300
   :width: 450

Since the Gaussian's have the same width (which means same certainty), than their product will be a Gaussian with a mean that is right in the middle.


.. image:: https://dl.dropbox.com/s/m338obmsu8x6t8p/Screenshot%202018-01-21%2013.19.21.png?dl=0
   :align: center
   :height: 300
   :width: 450

This can be hard to wrap your head around, but multiple measurements ALWAYS gives us a more certain (and therefore taller and narrower) belief.

New Mean and Variance
---------------------

.. code-block:: python

    # Write a program to update your mean and variance
    # when given the mean and variance of your belief
    # and the mean and variance of your measurement.
    # This program will update the parameters of your
    # belief function.

    def update(mean1, var1, mean2, var2):
        new_mean = (1.0/(var1 + var2)) * (var2 * mean1 + var1 * mean2)
        new_var = (1.0/((1.0/var1) + (1.0/var2)))
        return [new_mean, new_var]

    print update(10.,8.,13., 2.)


Gaussian Motion
---------------

.. image:: https://dl.dropbox.com/s/as8z5x56act1obt/Screenshot%202018-01-21%2013.28.27.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/8d1h1rfoh48tdr9/Screenshot%202018-01-21%2013.32.03.png?dl=0
   :align: center
   :height: 300
   :width: 450


Predict Function
----------------

This program implements the 1-dimensional Kalman filter.

.. code-block:: python

    # Write a program that will predict your new mean
    # and variance given the mean and variance of your
    # prior belief and the mean and variance of your
    # motion.

    def update(mean1, var1, mean2, var2):
        new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
        new_var = 1/(1/var1 + 1/var2)
        return [new_mean, new_var]

    def predict(mean1, var1, mean2, var2):
        new_mean = mean1 + mean2
        new_var = var1 + var2
        return [new_mean, new_var]

    print predict(10., 4., 12., 4.)


Kalman Filter Code
------------------

.. code-block:: python

    def update(mean1, var1, mean2, var2):
        new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
        new_var = 1/(1/var1 + 1/var2)
        return [new_mean, new_var]


    def predict(mean1, var1, mean2, var2):
        new_mean = mean1 + mean2
        new_var = var1 + var2
        return [new_mean, new_var]


    measurements = [5.0, 6.0, 7.0, 9.0, 10.0]
    motion = [1.0, 1.0, 2.0, 1.0, 1.0]

    measurement_sig = 4.0  # measurement uncertainty
    motion_sig = 2.0       # motion uncertainty

    mu = 0.0
    sig = 10000.0

    for mean2, motion_mean2 in zip(measurements, motion):
        mu, sig = update(mu, sig, mean2, measurement_sig)
        mu, sig = predict(mu, sig, motion_mean2, motion_sig)

    print([mu, sig])

Kalman Prediction
-----------------

* 1-D Kalman Filters.

.. image:: https://dl.dropbox.com/s/ppqpw566vv0s4ar/Screenshot%202018-01-21%2014.14.58.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/775tohhq5xjvvy8/Screenshot%202018-01-21%2014.18.50.png?dl=0
   :align: center
   :height: 300
   :width: 450

Kalman Filter Land
------------------

* Higher Dimensional Gaussians
* Multi-variate Gaussians

.. image:: https://dl.dropbox.com/s/bsg4trsuhnu3xzq/Screenshot%202018-01-21%2014.23.54.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/b7w6lux04juufa7/Screenshot%202018-01-21%2014.28.05.png?dl=0
   :align: center
   :height: 300
   :width: 450

Kalman Filter Prediction
------------------------

.. image:: https://dl.dropbox.com/s/uh7eoq7w0tdpmqr/Screenshot%202018-01-21%2014.31.24.png?dl=0
   :align: center
   :height: 300
   :width: 450

Our prediction is that we would move forward in the x direction by one and that our velocity is still one.

Another Prediction
------------------

.. image:: https://dl.dropbox.com/s/4eqs367v2wqdqok/Screenshot%202018-01-21%2014.34.15.png?dl=0
   :align: center
   :height: 300
   :width: 450

We'd expect our velocity to remain unchanged, but we should move forward in the x direction
by two (since the velocity was two).

More Kalman Filters
-------------------

.. image:: https://dl.dropbox.com/s/0q3cpfbgi0ab9z6/Screenshot%202018-01-21%2014.35.26.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/dxou9oli2kknhhe/Screenshot%202018-01-21%2014.37.24.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/znme1jw4oswep36/Screenshot%202018-01-21%2014.37.53.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/z6nz1rvds63255r/Screenshot%202018-01-21%2014.39.31.png?dl=0
   :align: center
   :height: 300
   :width: 450

The car **estimates** the velocity of the other vehicles based on the measurements of it's positions using Kalman
filters.

.. image:: https://dl.dropbox.com/s/ef1a6apkkavoqe5/Screenshot%202018-01-21%2014.40.23.png?dl=0
   :align: center
   :height: 300
   :width: 450

Kalman Filter Design
--------------------

.. image:: https://dl.dropbox.com/s/6bcy8p7rs5x27qs/Screenshot%202018-01-21%2014.43.08.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/6zqdmoxqsy6r1g0/Screenshot%202018-01-21%2014.44.58.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/KYEr4BXhD_E" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
