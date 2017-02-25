Bayes Nets
==========

Bayes Nets take the idea of uncertainty and probability  and marry it with efficient structures. We can understand
what uncertain variable influences other uncertain variable.


Challenge Question
------------------

**GOLD-1**


.. image:: https://dl.dropbox.com/s/pvo18qlb1gekh1b/Screenshot%202017-02-24%2001.31.30.png
   :align: center
   :height: 300
   :width: 450

* This requires creativity to connect O1 and O2.
* We have to use g somehow.
* We will use Capital case letters to indicate our Variables.
* We will use lower case letters to indicate when the variable is true, and - in front of it to indicate when it is
  not true.

.. image:: https://dl.dropbox.com/s/zs0lzjj1yjppw7u/Screenshot%202017-02-24%2001.37.42.png
   :align: center
   :height: 300
   :width: 450

* We solve for all the situations were o2 is true given o1 is true (this is subtler meaning with involving both G and
 o1)
* Over all the situations were o1 is true. Here we go for every o2 and G.
* Why are we doing this is not explained in this video.


We define the numerator

.. image:: https://dl.dropbox.com/s/cz3atf9kxehtpyo/Screenshot%202017-02-24%2001.42.50.png
   :align: center
   :height: 300
   :width: 450

We define the denominator

.. image:: https://dl.dropbox.com/s/smv3gpgs25fumh3/Screenshot%202017-02-24%2001.44.10.png
   :align: center
   :height: 300
   :width: 450

* We calculated this result by summing up the results for all the relevant situations. But
we can also get the results by sampling that can take care for more complex networks.


Bayes Network
-------------

* We care about diagnostic reasoning.

.. image::  https://dl.dropbox.com/s/uxu1x138ciwkph3/Screenshot%202017-02-24%2002.25.44.png
   :align: center
   :height: 300
   :width: 450

How many parameters?

* We need one with the evidence positive.
* We need once with the evidence negative.
* One probability for the evidence itself.


.. image:: https://dl.dropbox.com/s/zhexycql503lp27/Screenshot%202017-02-24%2002.27.40.png
   :align: center
   :height: 300
   :width: 450


Computing Bayes Rule
--------------------

* We compute the posterior probability not normalized, but ditching the probability B.

.. image::  https://dl.dropbox.com/s/a3y7xt379zumi17/Screenshot%202017-02-24%2002.31.42.png
   :align: center
   :height: 300
   :width: 450

* We calculate the normalizer indirectly using the terms itself.

.. image:: https://dl.dropbox.com/s/d1t91jrqma5l8op/Screenshot%202017-02-24%2002.33.07.png
   :align: center
   :height: 300
   :width: 450


Two Test Cancer
---------------

** GOLD **

.. image:: https://dl.dropbox.com/s/tmirw03l9x2fppb/Screenshot%202017-02-24%2002.45.44.png
   :align: center
   :height: 300
   :width: 450

* Clueless
* Trick shown before. Which one?
* Running Count for Cancer and - Cancer.
* Integrate various multiplications in Bayes Rule.
* Why are we multiplying? We are following non-normalized bayes rule.
* Why are we multiplying twice? Like how can we rationalize + combing two times with multiplying twice.

::

   n1 = 0.01 * 0.9 * 0.9
   d1 = 0.99 * 0.2 * 0.2

   n1 / (n1 + d1)
   0.169811320754717


.. image:: https://dl.dropbox.com/s/i2e1s2e8v120scs/Screenshot%202017-02-24%2002.56.24.png
   :align: center
   :height: 300
   :width: 450

Conditional Independence
------------------------

.. image:: https://dl.dropbox.com/s/6rxgvmxfphe8298/Screenshot%202017-02-24%2002.59.44.png
   :align: center
   :height: 300
   :width: 450

* Conditional Independence is a big thing in Bayes network.

.. image:: https://dl.dropbox.com/s/16dy6pv5faer4tv/Screenshot%202017-02-24%2003.01.37.png
   :align: center
   :height: 300
   :width: 450

* Without A, B and C are independent.
* Given A, B and C are not independent. They are both conditioned on A.

Conditional Independence 2
--------------------------

** GOLD  GOLD **

* Tricky again.
* Apply Total Probability.

.. image:: https://dl.dropbox.com/s/332s5ikar2v0zwq/Screenshot%202017-02-24%2003.20.48.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/7ygv4e7fuf4ak8s/Screenshot%202017-02-24%2003.24.27.png
   :align: center
   :height: 300
   :width: 450

* Right here is the Magic. How did we bring this in?
* Why do we not have any denominator.


.. image:: https://dl.dropbox.com/s/kns1stjd71zjbjw/Screenshot%202017-02-24%2004.09.18.png
   :align: center
   :height: 300
   :width: 450

* A Lot has happened in here. This is short-circuiting.

.. image:: https://dl.dropbox.com/s/55g9nnv0fyvcok6/Screenshot%202017-02-24%2004.16.23.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/asqdlqjzsmxnx2d/Screenshot%202017-02-24%2004.17.38.png
   :align: center
   :height: 300
   :width: 450

Compare
-------

* Same thing approached. Two different situations.

.. image:: https://dl.dropbox.com/s/smv3gpgs25fumh3/Screenshot%202017-02-24%2001.44.10.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/55g9nnv0fyvcok6/Screenshot%202017-02-24%2004.16.23.png
   :align: center
   :height: 300
   :width: 450

Absolute and Conditional
------------------------

.. image:: https://dl.dropbox.com/s/bbrqxphfi6nmomr/Screenshot%202017-02-24%2020.29.05.png
   :align: center
   :height: 300
   :width: 450



Confounding Cause
-----------------

.. image:: https://dl.dropbox.com/s/ejn4qwdu4isw3h1/Screenshot%202017-02-24%2008.50.54.png
   :align: center
   :height: 300
   :width: 450

Explaining Away
---------------

.. image:: https://dl.dropbox.com/s/g1jiqnre3ia32d3/Screenshot%202017-02-24%2008.52.17.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/yeutvmix4hyq57f/Screenshot%202017-02-24%2008.53.30.png
   :align: center
   :height: 300
   :width: 450

Explaining Away 2
-----------------

.. image:: https://dl.dropbox.com/s/jxn9a02cutmwpcr/Screenshot%202017-02-24%2021.13.27.png
   :align: center
   :height: 300
   :width: 450

Explaining Away 3
-----------------

.. image:: https://dl.dropbox.com/s/a2k3gjkpfsh6f5g/Screenshot%202017-02-24%2021.19.44.png
   :align: center
   :height: 300
   :width: 450


Conditional Dependence
----------------------

.. image:: https://dl.dropbox.com/s/04ab2uph1r2vkzz/Screenshot%202017-02-24%2021.21.12.png
   :align: center
   :height: 300
   :width: 450


General Bayes Network
---------------------


.. image::  https://dl.dropbox.com/s/nbf2tor4yz0bbp5/Screenshot%202017-02-24%2021.22.38.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/vt82z3mdkplpufi/Screenshot%202017-02-24%2021.24.20.png
   :align: center
   :height: 300
   :width: 450


D Separation
------------

.. image:: https://dl.dropbox.com/s/xb21x38u6qc1lmx/Screenshot%202017-02-24%2021.25.32.png
   :align: center
   :height: 300
   :width: 450

* Not Independent, if linked by *unknown* variable.

.. image:: https://dl.dropbox.com/s/uhzgjhwfc2vxoqi/Screenshot%202017-02-24%2021.26.33.png
   :align: center
   :height: 300
   :width: 450

D Separation
------------

.. image:: https://dl.dropbox.com/s/1d9cb70w42f99qq/Screenshot%202017-02-24%2021.28.08.png
   :align: center
   :height: 300
   :width: 450


Conclusion
----------

.. image:: https://dl.dropbox.com/s/imppwbjtti4pkua/Screenshot%202017-02-24%2021.29.41.png
   :align: center
   :height: 300
   :width: 450

Probabilistic Inference
-----------------------

* Probability Theory
* Bayes Net
* Independence
* Inference

.. image:: https://dl.dropbox.com/s/fmbg4knfrkdz5qs/Screenshot%202017-02-25%2005.52.20.png
   :align: center
   :height: 300
   :width: 450

* What kind of questions can we ask?
* Given some inputs what are the outputs?
* Evidence (know) and Query (to find out) Variables.
* Hidden (neither Evidence or Query. We have to compute)variables.
* Probabilistic Inference, output is going to be probability distribution over query variables.

.. image:: https://dl.dropbox.com/s/r09675e4drswgfd/Screenshot%202017-02-25%2005.55.57.png
   :align: center
   :height: 300
   :width: 450

Enumeration
-----------

* Start by stating the problem
* Using conditional probability

.. image:: https://dl.dropbox.com/s/xbhakaxuezhxnep/Screenshot%202017-02-25%2005.59.12.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/6pyyuk13ymf4c01/Screenshot%202017-02-25%2006.01.44.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/w9lajc4h2wqvnmz/Screenshot%202017-02-25%2006.02.35.png
   :align: center
   :height: 300
   :width: 450

* We denote that product of 5 numbers term as a single term called f(e,a)
* Then the final sum is the answer to sum of four terms where each term is a product of 5 numbers.

.. image:: https://dl.dropbox.com/s/6rqq7gv64ko5ywq/Screenshot%202017-02-25%2006.04.57.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/h1do4kipzng82t3/Screenshot%202017-02-25%2006.05.27.png
   :align: center
   :height: 300
   :width: 450

Speeding up Enumeration
-----------------------

.. image:: https://dl.dropbox.com/s/h1kqmgznefudqzt/Screenshot%202017-02-25%2006.18.58.png
   :align: center
   :height: 300
   :width: 450

* Reduce the cost of each row in the table.
* Still the same number of rows.


**Using dependence**

.. image:: https://dl.dropbox.com/s/ztn5wq66p08c6pq/Screenshot%202017-02-25%2006.23.33.png
   :align: center
   :height: 300
   :width: 450


Casual Direction
----------------

* Bayes Network is easier to do inference on, when the network flows from causes to effects.


Variable Elimination
--------------------

* NP Hard computation to do inference over Bayes Nets in general.
* Requires algebra to manipulate the arrays that come out the probabilistic terms.

.. image:: https://dl.dropbox.com/s/q0ufdgn4h6ci0p4/Screenshot%202017-02-25%2006.35.05.png
   :align: center
   :height: 300
   :width: 450

* Compute by Marginalising out and we have smaller network to deal with.

.. image:: https://dl.dropbox.com/s/7zms1cwvz9l2ggc/Screenshot%202017-02-25%2006.38.29.png
   :align: center
   :height: 300
   :width: 450

* We apply elimination, also called marginalization or summing out to apply to the table.

.. image:: https://dl.dropbox.com/s/yij3e5xs0mib8gx/Screenshot%202017-02-25%2006.41.32.png
   :align: center
   :height: 300
   :width: 450

Variable Elimination - 2
------------------------

* We sum out the variables and find the distribution.

.. image:: https://dl.dropbox.com/s/7tnknw21tihfz0j/Screenshot%202017-02-25%2006.43.37.png
   :align: center
   :height: 300
   :width: 450

Variable Elimination - 3
------------------------

.. image:: https://dl.dropbox.com/s/z706dpnoslrfxl1/Screenshot%202017-02-25%2006.46.06.png
   :align: center
   :height: 300
   :width: 450

* Summing out and eliminating.
* If we make a good choice, then variable elimination is going to be more efficient than enumerating.


Approximate Inference
---------------------

* Sampling

.. image:: https://dl.dropbox.com/s/uvfz2og3pbsbp33/Screenshot%202017-02-25%2006.51.24.png
   :align: center
   :height: 300
   :width: 450

* Enough counts to estimate the joint probability distribution.
* Sampling has an advantage over elimination as know a procedure to come up with an approximate value.
* Without knowing the conditional probabilities, we can still do sampling.
* Because we can follow the process.

Sampling Exercise
-----------------

* Sample that randomly
* Doubt: Weighted Sample or the Random Sample. Video suggests that it is a weighted sample.

.. image:: https://dl.dropbox.com/s/c34wjhd6p3heqvs/Screenshot%202017-02-25%2007.02.35.png
   :align: center
   :height: 300
   :width: 450

Approximate Inference 2
-----------------------

* In the limit, the sampling will approach the true probability.
* Consistent.
* Sampling can be used for complete probability distribution.
* Sampling can be used for an individual variable.

* What if we want to compute for a conditional distribution?

.. image:: https://dl.dropbox.com/s/dlvkzx2r6dudecx/Screenshot%202017-02-25%2007.13.39.png
   :align: center
   :height: 300
   :width: 450

Rejection Sampling
------------------

* Evidence is unlikely, you will reject a lot of variables.

.. image:: https://dl.dropbox.com/s/i3qv2e1svcmecer/Screenshot%202017-02-25%2007.22.37.png
   :align: center
   :height: 300
   :width: 450

* We introduce a new method called *likelihood weighting* so that we can keep everyone.
* In likelihood weighting, we fix the evidence variables.

.. image::  https://dl.dropbox.com/s/4osmw87r1l3u4ft/Screenshot%202017-02-25%2007.23.40.png
   :align: center
   :height: 300
   :width: 450

Likelihood Weighting
--------------------

.. image:: https://dl.dropbox.com/s/xjhlsqbshnp4mik/Screenshot%202017-02-25%2007.26.11.png
   :align: center
   :height: 300
   :width: 450

* It is a weighted Sample.

.. image:: https://dl.dropbox.com/s/cc4jr3zd3dwtly5/Screenshot%202017-02-25%2007.28.37.png
   :align: center
   :height: 300
   :width: 450

* We make likelihood weighting consistent.

Gibbs Sampling
--------------

* Josiah Gibbs, takes all the evidence into account, not just upstream evidence.
* Markov Chain Monty Carlo
* We have a set of variables, we re-sample just one variable at a time conditioned on all the others.
* Select one non-evidence variable and resample it on all other variables.

.. image:: https://dl.dropbox.com/s/rnr442leqpjpuuu/Screenshot%202017-02-25%2007.34.54.png
   :align: center
   :height: 300
   :width: 450

* We end up walking around the variables.
* The samples are dependent.
* They are very similar.
* The technique is consistent.
