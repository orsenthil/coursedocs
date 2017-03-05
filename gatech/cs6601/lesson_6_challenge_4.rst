Bayes Net Calculation
=====================

.. image:: https://dl.dropbox.com/s/746tssbnukoyw1n/Screenshot%202017-03-01%2007.56.05.png
   :align: center
   :height: 300
   :width: 450


Given Tables
------------

::

    P(LD=T | Cough=T) =  P(Cough=T |LD=T)  *P(LD)
                        ---------------------------
                                P(Cough)
                      =  (0.80 * 0.30 + 0.75 * 0.70) * P(LD)
                         ------------------------------------
                                P(Cough)

                      = (0.80 * 0.30 + 0.75 * 0.70) * (0.10)
                        ------------------------------------
                                    P(Cough)

                      = (0.80 * 0.30 + 0.75 * 0.70) * (0.10)
                      ---------------------------------------
                      (0.80 * 0.30 * 0.10) + (0.30 * 0.30 * 0.90) + (0.75 * 0.70 * 0.10) + (0.05 * 0.70 * 0.90)

                      = 0.0765
                        -------
                        0.189

                      = 0.40476190476190477



----


2. Question

.. math::

   P(LD=T|Cough=T,Fever=T)


// Bayesian

::

    P(LD=T|Cough=T,Fever=T) = P(Cough=T, Fever=T | LD=T) * P(LD=T)

                            = Sum(cold) [P(Cough=T,Fever=T| LD=T,cold) * P(cold) * P(LD=T) ] // Skipped a step = that was the mistake

                            = Sum(cold) [P(Cough=T| LD=T,cold) * P(Fever=T| LD=T, cold) * P(cold) * P(LD=T) ]

                            = P(LD=T) * Sum(cold) [P(Cough=T| LD=T,cold) * P(Fever=T| cold) * P(cold)]

                            = P(LD=T) * [P(Co=T|LD=T,C=T) * P(F=T|C=T) * P(C=T) + P(Co=T|LD=T,C=F) * P(F=T|C=F) * P(C=F)]
                            = 0.10 * ((0.80 * 0.65 * 0.30) + (0.75 * 0.25 * 0.70))

                            = 0.028725

                          = P(Cough=T, Fever=T | LD=F) * P(LD=F)


                          = P(LD=F) * Sum(cold) [P(Cough=T| LD=F,cold) * P(Fever=T| cold) * P(cold)]
                          = P(LD=F) * [P(Co=T|LD=F,C=T) * P(F=T|C=T) * P(C=T) + P(Co=T|LD=F,C=F) * P(F=T|C=F) * P(C=F)]
                          = 0.90 * ((0.30 * 0.65 * 0.30) + (0.05 * 0.25 * 0.70))

                          = 0.060524999999999995

                          = 0.32184873949579834






References
----------

* http://web.mit.edu/jmn/www/6.034/d-separation.pdf
