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
