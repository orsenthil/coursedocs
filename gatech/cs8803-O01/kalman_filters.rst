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


1 - Introduction
================
Welcome to my second class on Kalman filters.
I want to take you on a little tour to where it all began--Stanford University.
Behind me is Vale, Stanford's Research Center.
Let's go inside.
This is Junior, Standord's most recent self-driving car.
It's the child of Stanley, whom you can find
in the National Museum of American History in Washington, D.C.
Let me tell you something about the equipment that's on this car that makes it self-driving.
This rotating thing over here is a laser-range finder
that takes distance scans 10 times a second, about a million data points.
It'll be really important for the Kalman filter class I'm teaching you today.
It's major function is to spot other cars so you don't run into them.
There is also a camera on top. There is a stereo camera system over here.
In the rear there are antennas for a GPS--global positioning system--
that allows us to estimate where the car is in the world.
This is a supplemental system to the localization class I just taught you.
This is the data that comes from the laser.
This is the car parked in the garage right now. We see the back wall.
These are all range measurements that tell you how far things are away,
and they are essential as the input to the Kalman filter that we're going to learn about today.

2 - Tracking Intro
==================
I'd like to take my students on a little journey to Stanford
and show them our self-driving car that uses sensors to sense the environment.
So let me dive into the class pretty much right now.
In our last class, we talked about localization.
We had a robot that lived in an environment and that could use its sensors
to determine where in the environment it is.
Here you can see the Google self-driving car using a road map localizing itself.
But in addition, what is shown here in red are measurements of other vehicles.
The car uses lasers and radars to track other vehicles and today we're going to talk about how to find other cars.
The reason why I would like to find other cars is because we wouldn't want to run into them.
We have to understand how to interpret sensor data to make assessments,
not just where these other cars are as in the localization case,
but also how fast they're moving
so you can drive in a way that avoids collisions with them in the future.
That's important--not just for cars.
It matters for pedestrians and for bicyclists.
Understand where other cars are an making predictions where they're going to move
is absolutely essential for safe driving in the Google car project.
[Tracking]
So in this class we're going to talk about tracking.
The technique I'd like to teach you is called a Kalman filter.
This is an insanely popular technique for estimating the state of a system.
It's actually very similar to the probabilistic localization method
we taught in the previous class--Monte Carlo localization.
The primary differences are that Kalman filters estimate a continuous state
whereas in Monte Carlo localization we are voiced to chop the world into discrete places.
As a result, the Kalman filter happens to give us a unimodal distribution--
and I'll tell you in a second what that means--
whereas Monte Carlo was fine with multimodal distributions.
Both of these techniques are applicable to robot localization and tracking other vehicles.
In fact, in a later class, we're going to learn about particle filters,
which are yet another way to address the same problem,
and indeed they are actually continuous and multimodal.
But for the time being let's look into Kalman filters
and ignore these other two families of methods.
Let me start with a example. Consider the car done here.
Let's assume the it sees as its measurement, an object here, here, here,
here, and here for the times t = 0, t = 1, t = 2, and t = 3.
Where would you assume the object would be at t = 4? Check one of those 3 boxes.

3 - Tracking Intro Solution
===========================
And he asked you to expect it right over here.
From those observations you would say that the velocity
points in the direction of this vector.
Assuming no drastic change in velocity,
you expect that the 5th position would be over here.
The common filter takes observations like these
and estimates future locations and velocities based on data like this.
Today I'm going to teach you how to write a piece of software
that let's you take points like those--even if they're noisy and uncertain--
and estimate automatically where future locations might be
and at what velocity the object is moving.
The Google self-driving car uses methods like these to understand
where other traffic is based on radar and laser-range data.
So let's dive in!

4 - Gaussian Intro
==================
You remember our Markov model where the world was divided into discrete grids,
and we assigned to each grid a certain probability.
Such a representation of probability over spaces is called a histogram
in that it divides the continuous space into a finite many grid cells
and approximates the posterior distribution by a histogram over the original distribution.
The histogram is a mere approximation for this continuous distribution.
In Kalman filters the distribution is given by what's called a Gaussian.
A Gaussian is a continuous function over the space of locations,
and the area underneath sums up to 1.
Here's our Gaussian again.
If we call the space x, then the Gaussian is characterized by two parameters--
the mean, often abbreviated with the Greek letter μ, and the width of the Gaussian,
often called the variance, and for reasons I don't want to go into,
it's often written as a quadratic variable σ^2.
And Gaussian in 1D, which means the parameter space over here is 1 dimensional,
is characterized by μ and σ^2.
Rather than estimating the entire distribution as a histogram,
our task in Kalman filters is to maintain a μ and a σ^2 that is our best estimate
of the location of the object we're trying to find.
The exact formula is an exponential of a quadratic function where we take
the exponent of this complicated expression over here.
The quadratic difference of our query point x relative to the mean μ
divided by σ^2 multiplied by -1/2.
Now, if x equals μ then the numerator becomes 0,
and we have x of 0, which is 1.
It turns out we have to normalize this by a constant--
1 over the square root of 2πσ^2--
but for everything we'll talk about today, this constant won't matter, so ignore it.
What matters is we have an exponential of a quadratic function over here.
Let me draw you a couple of functions, and you tell me which ones you believe
are Gaussian by checking the box on the right side.
Please excuse my poor drawing skills here.

5 - Gaussian Intro Solution
===========================
The answer is this one is a Gaussian, this one, and this one.
They are all characterized by this exponential drop-off on both sides
that are symmetrical, and they have a single peak.
They are what's called "unimodal."
This is a bimodal function that has two peaks and as a result is not Gaussian.
The same is true over here and over here,
so these guys don't qualify.

6 - Variance Comparison
=======================
Let me ask you again about your intuition
and draw three more Gaussians, and, again, excuse my poor drawing skills here.
Now I'm going to ask you about the covariance.
For each of those check exactly one box.
Is the covariance large, medium, or small?
Obviously, one of those is the largest, one is a medium, and one is small.

7 - Variance Comparison Solution
================================
The answer is this is the largest covariance. It's the widest spread.
This is the smallest, and this is medium.
To see how this is being found in the formula over here,
the difference between x and y is being normalized by the covariance.
The larger this value, the less the difference over here matters,
and, as a result, the more the function is spread out.
So functions with a very wide spread have the largest covariance,
whereas functions with small spread have the smallest covariance.
Put differently, the sigma-squared covariance is a measure of uncertainty.
The larger sigma-squared, the more uncertain we are about the actual state.
This is a very certain distribution where expected deviation is small.
This is a relative uncertain distribution where we know very little.

8 - Preferred Gaussian
======================
[Which to prefer]
If we track another care with our Google self-driving car,
which Gaussian would we prefer?
The first, second, or third?

9 - Preferred Gaussian Solution
===============================
The answer is the third, because that's the one that's most certain,
and because it is most certain, it makes a chance of accidentally
hitting another car the smallest just by the fact that we know more about the car
than in the two other distributions.
You learned something really important.
You learned the definition of a Gaussian.
You learned about the fact that these are unimodal distributions.
They are also symmetrical.
And you learned a little bit about how to use them as a belief in a probabilistic filter.
Let's go and program a Gaussian.

10 - Evaluate Gaussian
======================
Let me ask you to calculate the value of x--
you will need a calculator for this--
for the following values: mu equals 10, sigma-squared equals 4, and x equals 8.

11 - Evaluate Gaussian Solution
===============================
The approximate answer is 0.12.
x minus mu squared is 4, this is 10 minus 8 to the square
divided by 4 equals 1.
The expression of the exponential is -1/2,
which is about 0.6.
This guy over here is approximately 0.2, which gives us as a product 0.12
I won't torture you with any more questions like these, because they're really not fun,
but we can program this now.

12 - Maximize Gaussian
======================
Starting with the following source code,
I'm looking for a completion of this one line over here that returns the Gaussian function
with arguments mu = 10, sigma2 = 4, and x = 8,
and I want the output to be approximately 0.12.
Here's my solution. This is the constant: 1/sprt(2<i>pi</i>sigma2).
Then I multiply with the exponential of (-.5<i>(x-mu)</i>*2/sigma2).
Applying that to the following numbers over here gives me 0.12.
Now, here's a question for you.
How do I have to modify x = 8 to be the maximum return value for this function f?

13 - Maximize Gaussian Solution
===============================
The answer is assess with the same value as mu,
in which case this expression over here becomes zero, and we get the maximum.
We get the peak of the Gaussian.
We set x to the same value as mu, to 10, and the output is 0.2 approximately.

14 - Measurement and Motion 1
=============================
Now let's look at the Kalman filter.
The Kalman filter represents all distributions but Gaussians.
Just like in the last class where we talked about measurement cycles and motion cycles,
the Kalman filter iterates two different things--measurement updates and motion updates.
This is identical to the situation before in localization
where we got a measurement and then we took a motion.
Here the max changes, but the basic principle applies.
Let's do a quiz to see if we remember the material from the last class.
You might remember that one of the two steps, measurement or motion,
required a convolution and the other one a product.
Please check the corresponding box.

15 - Measurement and Motion 1 Solution
======================================
Measurements were implemented using products,
and motions using a convolution.
If you don't know this, please go back and check the last class on localization.

16 - Measurement and Motion 2
=============================
In fact, we talked about Bayes Rule,
and we talked about total probability.
Please, again, check, whether Bayes Rule and total probability apply
to measurements or motions.

17 - Measurement and Motion 2 Solution
======================================
The answer is the measurement, the product, was using Bayes Rule,
and motion was using total probability.

18 - Shifting the Mean
======================
In Kalman filters we iterate measurement and motion.
This is often called a "measurement update,"
and this is often called "prediction."
In this update we'll use Bayes rule, which is nothing else but a product or a multiplication.
In this update we'll use total probability, which is a convolution,
or simply an addition.
Let's talk first about the measurement cycle and then the prediction cycle,
using our great, great, great Gaussians for implementing those steps.
Suppose you're localizing another vehicle,
and you have a prior distribution that looks as follows.
It's a very wide Gaussian with the mean over here.
Now, say we get a measurement that tells us something about
the localization of the vehicle, and it comes in like this.
It has a mean over here called "mu,"
and this example has a much smaller covariance for the measurement.
This is an example where in our prior we were fairly uncertain about a location,
but the measurement told us quite a bit as to where the vehicle is.
Here's a quiz for you.
Will the new mean of the subsequent Gaussian be over here, over here, or over here?
Check one of these three boxes.

19 - Shifting the Mean Solution
===============================
The answer is over here in the middle.
It's between the two old means--the mean of the prior and the mean of the measurement.
It's slightly further on the measurement side,
because the measurement was more certain as to where the vehicle is than the prior.
The more certain we are, the more we pull the mean in the direction of the certain answer.

20 - Predicting the Peak
========================
Now, here's a question that's really, really hard.
When we graph the new Gaussian, I can graph one that's very wide and very peaky.
If I were to measure where the peak of the new Gaussian is,
this would be a very narrow and skinny Gaussian.
This would be one that's width would be in between the two Gaussians.
This is one that's even wider than the two original Gaussians.
Which one do you believe is the correct posterior after multiplying these two Gaussians?
This is an insanely hard question.
I'd like you to take your chances here,
and I'll explain to you the answer in just a second.

21 - Predicting the Peak Solution
=================================
Very surprisingly, the resulting Gaussian
is more certain than the two component Gaussians.
That is, the covariance is smaller than either of the two covariances in isolation.
Intuitively speaking, this is the case because we actually gain information.
The two Gaussians together have a higher information content
than either Gaussian in isolation. It'll look something like this.
That is completely not obvious.
You might have to take this with faith, but I can actually prove it to you.

22 - Parameter Update
=====================
Suppose we multiply two Gaussians as in Bayes rule--
a prior and a measurement probability.
The prior has a mean of mu and a variance of sigma-squared.
The measurement has a mean of nu and a covariance of r-squared.
Then the new mean, mu prime, is the weighted sum of the old means
where mu is weighted by r-squared and nu is weighted by sigma-squared
normalized by the sum of the weight factors.
The new variance term--I'm going to write sigma-squared prime here
for the new one after the update--is given by this equation over here.
Let's put this into action.
We have a weighted mean over here.
Clearly, the prior Guassian has a much higher uncertainty.
Therefore sigma-squared is larger.
That means that nu is weighted much, much larger than the mu.
So the mean will be closer to the nu than the mu,
which means that it'll be somewhere over here.
Interestingly enough, the variance term is unaffected by the actual means.
It just uses the previous variances and comes up with a new one that's even peakier.
The result might look like this.
This is the Kalman situation for the measurement update step
where this is the prior, this is the measurement probability, and this is the posterior.
Let's practice these equations with a simple quiz.
Here are our equations again.
Suppose I use the following Gaussians:
[μ = 10, σ^2 = 4, ν = 12, r^2 = 4]
These are Gaussians with equal variance but different means that might look as follows.
Compute for me the new mean after the update and the new sigma-squared.

23 - Parameter Update Solution
==============================
The answer for the new mean is just the one in the middle,
and reason is both weights over here are equivalent,
so we take the mean between mu and nu, which is 11.
Then with sigma-squared it's 2.
If you take 1/4 plus 1/4, then you get 1/2, so 1 over 1/3 equals 2,
which means the new variance term is half the size of the previous variance terms.

24 - Parameter Update 2
=======================
Let's do this again.
Suppose our mean is 10 and 13, and the variances are imbalanced--8 and 2--
which corresponds to the following picture.
There's a relatively shallow distribution centered on 10
and a much more peaked distribution centered on 13.
Compute for me what the resulting mu prime and sigma-squared prime are.

25 - Parameter Update 2 Solution
================================
With a little bit of math we find that the new mean is 12.4,
and the new sigma-squared is 1.6.
12.4 is much closer to 13 than 10, and that's because the Gaussian centered on 13
has a much narrower variance than the one on 10.
We find the resulting variance is smaller than each of the two variances over here.
In particular, let's start with the variance.
1 over 1/8 plus 1/2 is the same as 1 over 5/8, which results in 8/5 or 1.6.
This is just applying this formula over here.
For the weighted average we get 2 times 10 plus 8 times 13.
Then we normalize by the sum of those two things over here.
So this is 124 divided by 10, which gives us 12.4.

26 - Separated Gaussians
========================
Let me ask you a different quiz,
which from the math, but it tests your intuition.
Suppose we have a prior that sits over here
and a measurement probability that sits over here--really far away--
and both have the same covariance.
Let me first quiz you where the new mean would be.
Is it going to be here, here, here, or here?
Please check the corresponding check mark.

27 - Separated Gaussians Solution
=================================
The answer is here. It's in the middle.
It's in the straight middle, because these two variances are the same,
so we just average the means.

28 - Separated Gaussians 2
==========================
Let me ask the hard question now.
Will it be a Gaussian like this where the variance is larger,
a Guassian with the exact same variance,
or an even more peaked Guassian that's more certain
than the two original factors in this calculation.
Please check exactly one of the three boxes over here.

29 - Separated Gaussians 2 Solution
===================================
The answer is it's the more peaked Gaussian.
That is somewhat counter-intuitive.
You'd think if this was your initial measurement probability
you really don't know where you are, and you should pick a very right Gaussian.
But the truth is our new sigma-squared is obtained independent of the means.
It's this formula over here.
Now because both means are the same, this resolves to 1 over 1/σ^2.
That's the same as σ^2 over 2,
which means a new variance squared is half of the old one.
That makes it a narrower Gaussian,
so the green one here that's the most peaked is indeed the correct answer.
This is very counter-intuitive, but now we understand why.
I hope you feel comfortable with the fact that we have actually gotten
more information about the location, which is manifest by a more focused estimate.

30 - New Mean and Variance
==========================
Let's now go back and write a program
in which we calculate the new mean and the new variance term.
I really just want you to write a Python program
that implements those equations so that we can test them.
I'm giving you a skeleton program, which has a function update,
that takes as an input a mean and a variance for the first distribution
and a mean and a variance for the second distribution
and outputs the new mean and the new variance of the product of those.
Here I am testing it with a mean of 10 and a variance of 8
and a mean of 13 and a variance of 2, which was one of our examples.
Out should come the answer over here--12.4 and 1.6.
Of course, Python tends to not give you the exact output,
so there are a couple of zeros over here but ignore those.
The answer is effectively 12.4 and 1.6. Can you fill in those gaps?

31 - New Mean and Variance Solution
===================================
Here's my answer. This is the expression for the mean.
This is the one for the variance.
I run it, and I get the exact same answer.
I run it again for my other example of equal variances and 10 and 12 as means,
and miraculously, the correct answer comes out--
11 for the new mean and 2 for the new variance.
If you programmed this correctly, then congratulations.
You've just programmed an essential update step in the Kalman filter--
the measurement update step.
That's really the difficult step in Kalman filtering.
The other one--the prediction step or the motion step--is much, much easier to program.

32 - Gaussian Motion
====================
[Thrun] So let's step a step back and look at what we've achieved.
We knew there was a measurement update and a motion update,
which is also called prediction.
And we know that the measurement update is implemented by multiplication,
which is the same as Bayes rule,
and the motion update is done by total probability or an addition.
So we tackled the more complicated case.
This is actually the hard part mathematically.
We solved this. We gave an exact expression.
We even derived it mathematically,
and you were able to write a computer program that implements this step of the Kalman filter.
I don't want to go into too much depth here.
This is a really, really easy step. Let me write it down for you.
Suppose you live in a world like this.
This is your current best estimate of where you are,
and this is your uncertainty.
Now say you move to the right side a certain distance
and that motion itself has its own set of uncertainty.
Then you arrive at a prediction that adds the motion of command to the mean,
and it has an increased uncertainty over the initial uncertainty.
Intuitively this makes sense.
If you move to the right by this distance,
in expectation you're exactly where you wish to be
but you've lost information because your motion tends to lose information
as manifested by this uncertainty over here.
The math for this is really, really easy.
Your new mean is your old mean plus the motion, often called U.
So if you move over 10 meters, this will be 10 meters.
And your new sigma square is your old sigma square
plus a variance of the motion Gaussian.
This is all you need to know. It's just an addition.
I won't prove it to you because it's really trivial.
But in summary, we have a Gaussian over here,
we have a Gaussian for the motion, with U as the mean
and R square as its own motion uncertainty,
and the resulting Gaussian in the prediction step just adds these 2 things up--
mu plus U and sigma square plus R square.
Since this was so simple, let me quiz you.
We have a Gaussian before the prediction step
which mu equals 8 and sigma square equals 4.
We then move to the right a total of 10,
with a motion uncertainty of 6.
Now describe to me the predictive Gaussian
and give me the new mu and the new sigma square.

33 - Gaussian Motion Solution
=============================
[Thrun] And the answer is just add those up.
8 + 10 = 18
4 + 6 = 10
And that's it.

34 - Predict Function
=====================
[Thrun] Let's program this.
I'm giving you a skeleton code.
This is the same update function as before.
Now I would like you to do the predict function,
which takes our current estimate and its variance
and the motion and its uncertainty
and computes the new updated prediction, mean, and variance.
So for example, if our prior is 10 and 4, our motion is 12 and 4,
I would like to get out to 22 and 8 according to the formulas I've just given you.

35 - Predict Function Solution
==============================
And yes, it's as easy as this. We just add the two means and
the two variances. It's amazing, this entire
program over here implements a one-dimensional common feature.

36 - Kalman Filter Code
=======================
So now let's put everything together.
Let's write a main program that takes these 2 functions, update and predict,
and feeds into a sequence of measurements and motions.
In the example I've chosen here are the measurements of 5., 6., 7., 9., and 10.
The motions are 1., 1., 2., 1., 1.
This all would work out really well if the initial estimate was 5,
but we're setting it to 0 with a very large uncertainty of 10,000.
Let's assume the measurement uncertainty is constant 4,
and the motion uncertainty is constant 2.
When you run this, your first estimate for position should basically become 5--
4.99, and the reason is your initial uncertainty is so large,
the estimate is dominated by the first measurement.
Your uncertainty shrinks to 3.99, which is slightly better than
the measurement uncertainty.
You then predict that you add 1, but the uncertainty increases to 5.99,
which is the motion uncertainty of 2.
You update again based on the measurement 6, you get your estimate of 5.99,
which is almost 6.
You move 1 again. You measure 7. You move 2. You measure 9. You move 1.
You measure 10, and you move a final 1.
And out comes as the final result, a prediction of 10.99 for the position,
which is your 10 position moved by 1,
and the uncertainty--residual uncertainty of 4.
Can you implement this so you get the exactly same outputs as I've gotten over here?

37 - Kalman Filter Code Solution
================================
This piece of code implements the entire Kalman filter.
It goes through all the measurement elements and quietly assumes there are
as many measurements as motions indexed by n.
It updates the mu and sigma using this recursive formula over here.
If we plug in the nth measurement and the measurement uncertainty,
it does the same with the motion, the prediction part over here.
It updates the mu and sigma recursively using the nth motion
and the motion uncertainty, and it prints all of those out.
If I hit the Run button, I find that my first measurement update
gets me effectively 5.0.
It's 4.98.
And that makes sense because we had a huge initial uncertainty,
and [inaudible] of 5 with a relatively small measurement uncertainty.
And in fact the resulting sigma square term is 3.98,
which is better than 4 and 1,000, slightly better than 4.
We're slightly more certain than the measurement itself.
We now apply the motion of 1.
We get to 5.9.
Our uncertainty increases by exactly 2, from 3.9 to 5.98.
And then the next update comes in at 6,
and it gives us a measurement of 5.99
and now a reduced uncertainty of 2.39.
And then we go to move to the right again by 1,
which makes the prediction 6.99.
Uncertainty goes up.
We measure 7. We get to 6.99, almost 7.
Uncertainty goes down.
We move 2 to the right, measure 9, 1 to the right,
measure 10, and move 1 again.
The final thing is the motion.
And if you look at the end result, our estimate is almost exactly 11,
which is the result of 10 + 1.
And the uncertainty is 4.0 after the motion
and 2.0 after the measurement.
This code that you just wrote
implements a full Kalman filter for 1D.
If you look at this,
we have an update function that implements
what actually is a relatively simple equation,
and a prediction function which is an even simpler equation
of just addition.
And then you apply it to a measurement sequence and a motion sequence
with certain uncertainties associated,
and this little piece of code over here
gives you a full Kalman filter in 1D.
I find this really amazing.
Let's plug in some other values.
Suppose you're really certain about the initial position.
It's wrong. It's 0.
It should be 5, but it's 0.
And now we assume a really small uncertainty.
Guess what's going to happen to the final prediction?
As I hit the Run button,
we find this has an effect on the final estimate.
It's not 11. It's only 10.5.
And the way this takes place is initially,
after our first measurement update, we believe in the position of 0.
This is 1.24 to the - 10th,
but a really small uncertainty, even smaller than this one over here.
We apply our motion update. We add a 1.
We have a higher uncertainty.
And now when the next measurement comes in, 6,
we are now more inclined to believe the measurement
because uncertainty is now basically 2 as opposed to 0.001.
We update our position to be 2.666,
which is now a jump away from 1, and we reduce our uncertainty.
Motion comes in, 3.66.
Uncertainty goes up.
We now are willing to update even more.
As you see the 7, we're willing to go to 5.1,
but not quite all the way because we feel fairly confident on our wrong prior estimate.
And this confidence makes it all the way to the end
when we predict 10.5 as opposed to 11
with an uncertainty of 3.98.
We've corrected some of it.
We were able to drag it into the right direction but not all the way
because our false initial belief has such a strong weight
in the overall equation.

38 - Kalman Prediction
======================
Now we understand a lot about the 1D Kalman filter.
You've programmed one. You understand how to incorporate measurements.
You understand how to incorporate motion,
and you really implement something that's actually really cool,
which is a full Kalman filter for the 1D case.
Now in reality, we often have many Ds,
and then things become more involved, so I'm going to just tell you how things work
with an example, and why it's great to estimate in higher dimensional state spaces.
Suppose you have a 2-dimensional state space of x and y--like a camera image,
or in our case, we might have a car that uses a radar to detect the location
of a vehicle over time.
Then what the 2D Kalman filter affords you is something really amazing,
and here is how it goes.
Suppose at time t = 0, you observe the object of interest to be at this coordinate.
This might be another car in traffic for the Google self-driving car.
One time step later, you see it over here.
Another time step later, you see it right over here.
Where would you now expect at time t = 3 the object to be?
Let me give you 3 different places.
Please click at the most likely location.

39 - Kalman Prediction Solution
===============================
The answer is here.
What the Kalman filter does for you, if you do estimation and high dimensional spaces,
is to not just go into x and y spaces,
but allows you to implicitly figure out what the velocity of the object is,
and then use the velocity estimate to make a really good prediction about the future.
Now notice the sensor itself only sees position.
It never sees the actual velocity.
Velocity is inferred from seeing multiple positions.
So one of the most amazing things about Kalman filters in tracking applications is
it's able to figure out, even though it never directly measures it,
the velocity of the object, and from there is able to make predictions about future locations
that incorporate velocity.
That is just really, really, really great.
That's one of the reasons that Kalman filters are such a popular algorithm
in artificial intelligence and in control theory at large.

40 - Kalman Filter Land
=======================
To explain how this works, I have to talk about high dimesional gaussians.
These are often called multivariate gaussians.
The mean is now a vector with 1 element for each of the variance.
The variance here is replaced by what's called a co-variance,
and it's a matrix with D rows and D columns,
if the dimensionality of the estimate is D.
The formula is something you have to get used to.
I'm writing it out for you, but you never get to see this again.
To tell you the truth, even I have to look up the formula for this class,
so I don't have it in my head, and please, don't get confused.
Let me explain it to you more intuitively.
Here's a 2-dimensional space.
A 2-dimensional gaussian is defined over that space,
and it's possible to draw the contour lines of the gaussian. It might look like this.
The mean of this gaussian is this x0, y0 pair,
and the co-variance now defines the spread of the gaussian
as indicated by these contour lines.
A gaussian with a small amount of uncertainty might look like this.
It might be possible to have a fairly small uncertainty in 1 dimension,
but a huge uncertainty in the other.
Huge uncertainty in the x-dimension is small, and the y- dimension is large.
When the gaussian is tilted as showed over here,
then the uncertainty of x and y is correlated, which means if I get information about x--
it actually sits over here--that would make me believe that y probably sits
somewhere over here. That's called correlation.
I can explain to you the entire effect of estimating velocity and using it in filtering
using gaussians like these,
and it becomes really simple.
The problem I'm going to choose is a 1-dimensional motion example.
Let's assume at t = 1, we see our object over here.
A t = 2 right over here.
A t = 3 over here.
Then you would assume that at t = 4, the object sits over here,
and the reason why you would assume this is--even though it's just seen these different
discrete locations, you can infer from it there is actually velocity that drives the object
to the right side to the point over here.
Now how does the Kalman filter address this?
This is the true beauty of the Kalman filter.

41 - Kalman Filter Prediciton
=============================
In Kalman filter land, we're going to build a 2-dimensional estimate.
1 for the location, and 1 for the velocity denoted x dot.
The velocity can be zero. It can be negative, or it can be positive.
If initially I know my location, but not my velocity,
then I represent it with a Gaussian that's elevated around the correct location,
but really, really broad in the space of velocities.
Let's look at the prediction step.
In the prediction step, I don't know my velocity,
so I can't possibly predict for location. I'm going to assume.
But miraculously, they'll be some interesting correlation.
So let's for a second, just pick a point on this distribution over here.
Let me assume my velocity is 0.
Of course, in practice, I don't know the velocity,
but let me assume for a moment the velocity is 0.
Where would my posterior be after the prediction?
Well, we know we started in location 1.
The velocity is 0, so my location would likely be here.
Now let's change my belief in velocity and pick a different one.
Let's say the velocity is 1.
Where would my prediction be 1 time step later starting at location 1 and velocity 1?
I'll give you 3 choices.
Here? Here? Or here?
Please pick the one that makes the most sense.

42 - Kalman Filter Prediciton Solution
======================================
The answer is right over here. Why?
If a cars starting point is the point over here, for which we know the location is 1,
and the velocity is 1, and if we predict 1 time step in the future,
then for that prediction, we know the location will be 2,
and the velocity might be a little uncertain, but it stays about the same.
So we end up with a point over here. Let's do this again.

43 - Another Prediction
=======================
Let me consider a velocity of 2,
which means this is our starting point.
Let me ask you where you would expect among those choices
to be the most plausible prediction to be.

44 - Another Prediction Solution
================================
Just like before, it'll be over here with a velocity of 2, initial position of 1,
we find ourselves in 3.
And again, this model assumes that in the absence of more knowledge,
the velocity shouldn't really change.

45 - More Kalman Filters
========================
When you put all this together, you find that all these possibilites on the Gaussian over here,
link to a Gaussian that looks like this.
This is a really interesting 2-dimensional Gaussian, which you should really think about.
Clearly, if I were to project this Gaussian uncertainty into the space of possible locations,
I can't predict a thing. It's impossible to predict where the object is.
The reason is, I don't know the velocity.
Also, clearly if I project this Gaussian into the space of x dot,
it is impossible to say what the velocity is.
A single observation or single prediction is insufficient to make that observation.
However, what we know is our location is correlated to the velocity.
The faster I move, the further on the right is the location.
This Gaussian expresses this.
If I, for example, figure out that my velocity was 2, then I was able, under this Gaussian,
to really nail that my location is 3.
That is really remarkable.
You still haven't figured out where you are, and you haven't figured out how fast you're moving,
but we've learned so much about the relation of these 2 things with this Gaussian.
To understand how powerful this is, let's now fold in the second observation at time t = 2.
This observation tells us nothing about the velocity and only something about the location.
So if I were to draw this as a Gaussian--it's a Gaussian just like this,
which says something about the location but not about the velocity.
But if we multiply by prior from the prediction step with the measurement probability,
then miraculously, I get a Gaussian that sits right over here.
This Gaussian now has a really good estimate what my velocity is
and a really good estimate where I am.
If I take this Gaussian, and predict 1 step forward, then I find myself right over here.
That's exactly the effect we have over here.
After that I get a Gaussian like this, I predict right over here.
Think about this. This is really deep insight about how Kalman filters work.
In particular, we've only been able to observe 1 variable.
We've been able to measure observation to infer this other variable,
and the way we've been able to infer is that there's a set of physical equations
which say that my location, after a times step, is my old location plus my velocity.
This set of equations has been able to propagate constrains from subsequent measurements
back to this unobservable variable, velocity, so we are able to estimate the velocity as well.
This is really key to understanding Kalman filter.
It is key to understanding a Google self-driving car,
estimates and locations of other cars, and is able to make predictions
even if it's unable to measure velocity directly.
There's a big lesson here.
The variables of a Kalman filter--they're often called states because they reflect states
of the physical role like where is the other car and the fastest moving.
They separate into 2 subsets--the observables, like the momentary location,
and the hidden, which in our example is the velocity, which I can never directly observe.
But because those 2 things interact, subsequent observations of the observable variables
give us information about these hidden variables, so we can also estimate
what these hidden variables are.
So from multiple observations of the places of the object--the location--
we can estimate how fast it's moving.
That is actually true for all of the different filters but because Kalman filters happen to be
very efficient to calculate, when we have a problem like this,
you tend to often use just a Kalman filter.

46 - Kalman Filter Design
=========================
When we design a Kalman filter, you need effectively 2 things.
For the state, you need a state transition function,
and that's usually a matrix, so we're now in the world of linear algebra.
For the measurements, you need a measurement function.
Let me give you those for our example of the one demotion of an object
Be known that the new location is the old location + velocity,
turns into this matrix. You have a 1 over here and a 1 over here.
The new velocity should just be the old velocity, which gives us 0 over here and a 1 over here.
If you multiply this matrix by this vector, this is exactly what you're getting.
For the measurement, we only observe the first component of place, not velocity,
and that uses a matrix like this.
This matrix would be called F and this H.
The actual update equations for a Kalman filter are involved,
and I give them to you, but please, don't memorize them, and I won't prove them for you.
Even the proof is very involved.
Every time I use them, I just look them up.
There's a prediction step where I take my best estimate x,
multiply it with a state transition matrix--matrix F,
and I add whatever motion I know--u.
That gives me my new x.
I also have a covariance that characters my uncertainty,
and that is updated as follows, where T is the transpose.
There's also a measurement update step where we use the measurement z.
We compare the measurement with our prediction where H is the measurement function
that maps the state to measurements.
We call this this the error.
The error is mapped into a matrix s, which is obtained by projecting the system uncertainty
into the measurement space using the measurement function projection
+ the matrix R, the characters of measurement noise.
This is then mapped into a variable called K, which is often called the Kalman gain,
where we invert the matrix s,
and then finally, we actually update our estimate and our uncertainty
using what ought to be the most cryptic equation that you've seen in a long time.
Now I wrote this down so that you have a complete definition,
but this is something you should not memorize.
If you really wish to understand this math, it happens to be just a generalization of the math
I gave you to higher dimensional spaces,
but I would recommend just not to worry about this.
There's a set of linear algebra equations that implement the Kalman filter
and higher dimensions.

47 - Kalman Matrices
====================
I have a new, challenging programming assignment for you that will take you a while,
but I would like you to implement a multidimensional Kalman filter for the example
I've just given you.
The matrix class is a class for manipulating matrices that should make it really easy.
It has a function that initializes matrices--I'll show you an example in a second.
It can set them down to 0.
It can compute an identity matrix.
It can print out a matrix with show.
It overloads operators like addition, subtraction,
multiplication, and even computes the transpose of a matrix,
and in some more extended code, it can actually invert a matrix
using Cholesky factorization.
There's a function here called inverse.
This matrix class is available.
It's a small version of what is found in typical libraries.
I want to demonstrate it for you just for a second.
You can make a matrix with a command like this with the argument in the parenthesis.
It's a 2-dimensional matrix.
In this case it's a vertical vector.
With the show command, you can print out the result of the vertical vector.
You can put the transpose as follows.
If you run this, you'll find the horizontal vector.
Say you wish to multiply a matrix by a vector,
then we can make a 2 x 2 matrix with this initialization over here,
a matrix of [12., 8.] and [6., 2.].
We can print this matrix.
Here it is: 12, 8, 6, 2.
These are these values over here.
And we can multiply F and a.
So here b = F x a.
And if we show the result, we get the vector 280.
That's obtained by 10 x 12 + 10 x 8 is 200.
10 x 6 + 10 x 2 is 80.
So using my matrix libraries, I set an initial state.
This is a tracking in 1D where the state is the position
and the velocity.
I initialized both with 0 because I don't know the actual location and the velocity.
I get an uncertainty matrix
where I have a really high uncertainty in the position
and a really high uncertainty in the velocity,
and they're both uncorrelated.
That's the matrix of 1000, 0, 0, 1000.
I specify an external motion, but it's 0, 0, so it has no effect,
so just ignore this.
I build the next state function, which is the one we just discussed,
[1., 1] [0, 1.].
That assumes that the velocity is just being added to the position,
and the velocity and expectation stays the same.
I build a measurement function that extracts just the first
of the 2 values, 1 and 0,
so I can observe the location but not the velocity.
I have a measurement uncertainty.
It happens to be 1 in this example.
And I have an identity matrix, [1., 0.] [0., 1.].
And then I run a filter with these 3 measurements over here,
and what should come out is that by running the filter,
I can estimate the velocity
and therefore make better predictions.
In the filter that I want you to program,
I want the measurement update first and then the motion update.
Every time we run the filter,
I want you to update the measurement first, then the motion.
Here is my empty procedure filter that we have to fill in
where I go through our measurements,
and it builds the measurement update and then the motion update,
the prediction, and then I just print out the resulting estimates.
I do this a number of times, 3 times in this case.
Once we fill this in and I hit the Run button,
I get the following output.
After my first measurement update,
I observed the location 1, which gets copied over
essentially to .99 over here.
I learn nothing about the velocity, so it's still 0, just the way I initialized it.
And then there's an updated uncertainty matrix
which now shows what happens to be a strong correlation,
1000, 1000, 1000, 1000.
That differs from the initial one only that we filled in
the off-diagonal elements.
It happens to be exactly what the Kalman filter does.
And then I'll observe again the 2.
I want the output to now tell me that my next prediction is 3.
It's the observation plus the prediction.
But now I have a really good estimate
on what the velocity is.
It's essentially 1, and the reason is
my Kalman filter was able to use
the Kalman filter equations to find this value.
There's a new covariance matrix,
and for the third observation followed by the prediction,
the prediction is correctly effectively 4, 3.999.
The velocity estimate is correctly 1, which is .99999,
and I have yet another uncertainty matrix which illustrates
I high certainty in the velocity estimate.
Notice a relatively high certainty in the position estimate
compared to my initial uncertainties.
So can you write the algorithm filter
that outputs those exact values over here?
This is an involved programming assignment.
What you have to do is you have to essentially
implement the equations I gave you.
You have to familiarize yourself with the matrix class
and then go and fill in the filter code
in accordance to the things that I showed you
for the multivariate Kalman filter.

48 - Kalman Matrices Solution
=============================
[Male] And here is my code.
If you've got this correct,
then I'm mightily impressed with what you've done because
you've taken something that often takes many, many classes
to explain to students, and within a single class,
you understood the gist of it and you wrote a piece of code
that is really non-trivial, that you can reuse many times,
and that's the core of the Google self-driving cars' ability to check other vehicles.
Here is the line by line implementation
of what I've shown you before for the measurement update
and the prediction, and you'll find
using my matrix class that it implements
step after step exactly what I've shown you.
A little non-triviality.
We have to make a measurement matrix of the nth measurement.
If you solve the problem, you have probably something like this.
The arrow calculation,
the matrix S with a transpose,
the Kalman gain K with the inverse,
back to my next prediction and my measurement update,
and this is the prediction step.
You can see it implements exactly what I showed you
in these 2 equations over here.
Now I know programming with this is involved,
and I'm really impressed if you were able to do this.
If you've done this, you've achieved something really, really major.
You now understand Kalman filters,
and you've implemented a multidimensional Kalman filter
all on your own using a fairly mechanical
matrix class that I wrote for you.
You ran it, and it's gotten really good results
in which a sequence of position estimates, 1, 2, 3,
led you to make a prediction
and understand the velocity of the moving object.
These are the equations you just implemented.
Congratulations.
You really understood something fundamental here
that I believe is really essential to artificial intelligence
and to building self-driving cars.
You implemented effectively our method for finding other cars.
Let me put this in context.
Here's a Google self-driving car.
Here's another car.
Our Google self-driving car uses radar on the front bumper
that measures the distance to vehicles
and also gives a noisy estimate of the velocity.
And it also uses its lasers,
and again, it measures the distance to other cars but no velocities.
If you take the same situation from above,
here is the Google car.
It is localized on a map.
Here is another vehicle, and another one.
Using radars and lasers, the Google car estimates the distance
and the velocity of all these vehicles,
and it does so using a Kalman filter.
We have feeds and range data from the laser,
and it uses state spaces like this one of the relative distance in x and y
and the relative velocity in x and y to get state transition matrices
of the type I've just shown you to find out
what these other cars are, and this is exactly what you've just learned
and programmed yourself.
I didn't tell you how to extract the location of other cars from radar and laser.
There's something called a correspondence problem.
Sometimes you don't know which one each car is,
and I won't talk in much depth about it.
But you understand the gist of the solution now,
and you've been able to program it.
If you were in a situation like this,
you can use range data like laser data and radar data
and come up with a rational algorithm that takes
momentary measurements of other cars
and not just estimates where they are but also how fast they're moving.
That's really a tremendous feat.
Congratulations on getting this far.
If you got this far in my class,
I promise you you've just digested the most difficult thing
I have to teach you in this entire class.
Congratulations.

49 - Conclusion
===============
So this completes my unit on Kalman filters. You learned actually quite a bit.
You learned about Gaussians, how to do measurement updates using multiplication,
how to do prediction or state transitions using convolution,
and you even implemented your first Kalman filter, which is really super cool.
You've implemented it in the context of vehicle tracking,
and you used this to estimate a nonobservable velocity for measurement data.
Now, next is your homework assignment.
I hope you can prove what you've learned and ace it.
Then, next week, we're going to move into particle filters, which is an exciting third method for state estimation.
So I'll see you for the homework assignment, and then I'll see you in class for particle filters.


