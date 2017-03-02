Bayes Net Calculation
=====================

.. image:: https://dl.dropbox.com/s/746tssbnukoyw1n/Screenshot%202017-03-01%2007.56.05.png
   :align: center
   :height: 300
   :width: 450


Given Tables
------------

::

    Cold

    T = 0.30
    F = 0.70

    LD

    T = 0.10
    F = 0.90


            Fever
    Cold

    T        0.65
    F        0.25


   Cold   LD   P(Cough) P(-Cough)

   T      T    0.80     0.20
   T      F    0.30     0.70
   F      T    0.75     0.25
   F      F    0.05     0.95



   Cold  P(Cough)
   T      0.80 * 0.10
   T      0.30 * 0.90

   Cold  P(Cough)
   F     0.75 * 0.10
   F     0.05 * 0.90

::

   P(+LD|+Cough) = P(+LD, +Cough) / P(+Cough)
   P(+LD|+Cough) = P(+LD, +Cough, Cold) / P(+Cough, Cold)

   # Do we need to include Fever too?

   No

   P(+LD, +Cough, Cold)

   For_all(Cold) = P(+LD, +Cough, Cold) * P(+Cough, Cold)
                 = P(+LD, +Cough, +Cold) * P(+Cough, +Cold) + P(+LD, +Cough, -Cold) * P(+Cough, -Cold)
                 = ((0.80 * 0.10)        *  ((0.80 * 0.10) + (0.30 * 0.90))) + ((0.75 * 0.90) * ((0.75 * 0.10) + (0.05 * 0.90)))
                 = 0.10900000000000003



::

  P(LD|Cough, Fever) = P(LD, Cough, Cold,Fever) / P(Cough, Cold, Fever) # NO.

  # “Each variable is conditionally independent of its non-descendants, given its parents.”

  = 0.10900000000000003
