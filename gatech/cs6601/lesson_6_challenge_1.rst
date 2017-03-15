Problem 1
=========


::

    D = 'C' ( 0.33)

            (Choice) (0.33)
         /     |     \
    a=Head 	b=Head 	c=Head
    0.2      0.6	0.8


    P(Choice | Head, a=Head) =

    P(Choice | Head, b=Head)

    P(Choice | Head, c=Head)

    Which is maximum of the three?


    P(D |Head, a=Head) = P(Head |D) * P(a=Head/D)



Assuming you flip a coin, and it came up as Heads. Which coin is most likely to have produced that
result. The answer’s pretty obvious, so provide a probabilistic justification for why you think so.

---

**Bayes Rule**

::

    P(Choice=c | c=Head) =  P(c=Head|Choice=c)  * P(Choice=c)
                        = 0.8 * 0.3 * 0.3
                        =  0.072

    P(Choice=b)			= 0.6 * 0.3 * 0.3 =  0.054

    P(Choice=a)         = 0.2 * 0.3 * 0.3  = 0.018


    Max of these. Choice = c.

---

::

    P(C|c=Head) = P(c=Head|C) * P(C)


---

Independent Probability Multiplication

::

    P(HHT|C=a) = P(a=Head|C=a) * P(a=Head|C=a)  * P(a=Tail|C=a)
                = (0.2 * 0.33)  * (0.2 * 0.33) * (0.8 * 0.33)
                = 0.0011499840000000002

                = (0.2 * 0.2 * 0.8)

    P(HHT|C=b) = P(b=Head|C=b) * P(b=Head|C=b)  * P(b=Tail|C=b)
               = (0.6 * 0.33) * (0.6 * 0.33) * (0.4 * 0.33)
               = 0.0051749280000000005
               // Winner

               = (0.6 * 0.6 * 0.4)


    P(HHT|C=c) = P(c=Head|C=c) * P(c=Head|C=c)  * P(c=Tail|C=c )
               = (0.8 * 0.33) * (0.8 * 0.33) * (0.2 * 0.33)
               = 0.004599936000000001

               = (0.8 * 0.8 * 0.2)
