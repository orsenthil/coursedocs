Probability
===========

Introduction
------------


.. image:: https://dl.dropbox.com/s/vbzo7167yyoktur/Screenshot%202017-02-23%2022.04.41.png
   :align: center
   :height: 300
   :width: 450


Decomposition

.. image:: https://dl.dropbox.com/s/kt44t79es1uwjwa/Screenshot%202017-02-23%2022.46.18.png
   :align: center
   :height: 300
   :width: 450


* Whenever we see a conditional probability, the first thing we look at is Bayes rule.

.. image:: https://dl.dropbox.com/s/6qg864bhjdxob16/Screenshot%202017-02-23%2022.47.42.png
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/idrvkwkxub1b0q7/Screenshot%202017-02-23%2022.48.24.png
   :align: center
   :height: 300
   :width: 450

* We have to find out the probability of Y being True.
* At this point, we think of Venn Diagrams.

.. image:: https://dl.dropbox.com/s/cp7xzkx47auw1ij/Screenshot%202017-02-23%2022.51.01.png
   :align: center
   :height: 300
   :width: 450

* Final calculation

.. image:: https://dl.dropbox.com/s/bap04d96criww9e/Screenshot%202017-02-23%2022.51.45.png
   :align: center
   :height: 300
   :width: 450

*Strategy*

* Accurate Translation of the english into probability

::

   P (X) = 3% = 0.03
   P (-Y | X) = 1% = 0.01
   P (Y | -X) = 10% = 0.1

   P( X | Y) = ?

             = P (Y |X ) * P (X)
               -----------------
                    P (Y)

   P (Y | X ) = 1 - P (-Y | X)
              = 1 - 0.01
              = 0.99


   P ( Y ) = P ( Y |X) * P(X) + P(Y | -X) * P(-X)
            = 0.99 * 0.03 + 0.1 * (1-0.03)
            = 0.1267

   P ( X | Y ) = 0.99 * 0.03 / 0.1267
               = 0.23441199684293604



Intro to Probability and Bayes Network
--------------------------------------

.. image:: https://dl.dropbox.com/s/h5b6wcmnnw9h85k/Screenshot%202017-02-23%2023.14.29.png
   :align: center
   :height: 300
   :width: 450


Bayes network is a compact representation of distribution of this
very very large giant probability distribution of all these variables.

Using Bayes network, we have observe the probabilities of some
variables and compute hypothesis of the probability of other variables.


.. image:: https://dl.dropbox.com/s/sy8241ldrg0j4o3/Screenshot%202017-02-23%2023.20.31.png
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/i2us68rpkyhnyqp/Screenshot%202017-02-23%2023.21.14.png
   :align: center
   :height: 300
   :width: 450


Probability Summary
-------------------

* Probability of Independent Events = Product of the Probability of Marginals

* Independent Events

.. image:: https://dl.dropbox.com/s/z4lbzvrxrislrem/Screenshot%202017-02-23%2023.36.59.png
   :align: center
   :height: 300
   :width: 450


Dependence
----------

* I will use the term "given that" for describing the condition after the "|"


.. image:: https://dl.dropbox.com/s/3lnswbdkrkozmll/Screenshot%202017-02-23%2023.39.17.png
   :align: center
   :height: 300
   :width: 450

* Theorem of Total Probability

.. image:: https://dl.dropbox.com/s/qjlmr1wda5f6yvj/Screenshot%202017-02-23%2023.43.42.png
   :align: center
   :height: 300
   :width: 450


What We Learned
---------------

* Total Probability

* Probability of any random variable Y, can be written as, Probability Y, "given that" some other random variable
X_i_, times P(X_i_), summed over all possible outcomes of i for the random variable X.

* Negation of Probability

* P(-X | Y) = 1 - P( X | Y)

.. image:: https://dl.dropbox.com/s/cxvdq2g7tj2zhju/Screenshot%202017-02-24%2000.21.10.png
   :align: center
   :height: 300
   :width: 450

* Can never negate the conditional variables and assume that it will add up to 1.

Weather Quiz
------------

.. image:: https://dl.dropbox.com/s/ladq9f6ywagn7c3/Screenshot%202017-02-24%2000.27.36.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/jy1w2eswqrmqvh3/Screenshot%202017-02-24%2000.35.09.png
   :align: center
   :height: 300
   :width: 450

Cancer Example
--------------

**GOLD-1**

.. image:: https://dl.dropbox.com/s/udqutasb9kph0hi/Screenshot%202017-02-24%2000.37.37.png
   :align: center
   :height: 300
   :width: 450

* Before we calculate this, we are calculating the joint probabilities.
* Why are we calculating the joint probabilities?

Now, the joint probabilities are not independent events. They are joint probabilities of dependent events.

.. image::  https://dl.dropbox.com/s/omdjka927wf86ul/Screenshot%202017-02-24%2000.45.45.png
   :align: center
   :height: 300
   :width: 450

* The product of prior and the conditional

**GOLD-2**

.. image:: https://dl.dropbox.com/s/arqcnwj7r44pjdk/Screenshot%202017-02-24%2000.55.22.png
   :align: center
   :height: 300
   :width: 450

* We expand via Bayes Rule

::

   P (C | +) =  P ( + | C ) . P ( C)  / P ( + )

             =  (0. 9 *  0.01) /  (0.009 + 0.198)
             =  (0.9 * 0.01)  / 0.20700000000000002
             = 0.043478260869565216o


* Not using the term "Total Probability" for the P(+), but essentially doing that.

* The prior for cancer is so small that it is unlikely to have cancer.

* The additional information of positive test, only raised the posterior probability to 0.043

.. image:: https://dl.dropbox.com/s/cyiuea0ois24qzd/Screenshot%202017-02-24%2001.04.45.png
   :align: center
   :height: 300
   :width: 450

Bayes Rule
----------

**GOLD-3**

* The most important maths for this class in statistics called Bayes Rule.

* B is the evidence.
* A is the variable we care about.
* For the variable we care about, we have a Prior
* For the expression with evidence, we say it as  a marginal likelihood and likelihood for conditioned one.

.. image:: https://dl.dropbox.com/s/nbzxkelwz9lvmf8/Screenshot%202017-02-24%2001.10.48.png
   :align: center
   :height: 300
   :width: 450

* The evidence to cause, is turned into causal reasoning.

* Hypothetically given the cause, what is the probability of the evidence that just occured. And to correct for this
   reasoning, we multiply it by the prior probability of the cause, and divide the whole by the normalized evidence.

* The Probability of Evidence is expanded often by the theorem of total probability.

::

      Sum(forall a) P ( B | A = a)


.. image:: https://dl.dropbox.com/s/u7xr8zpci5ig2hi/Screenshot%202017-02-24%2001.16.27.png
   :align: center
   :height: 300
   :width: 450

