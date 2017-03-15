Problem 2
=========

::

    P(TOOTHACHE / CATCH) ~= P(TOOTHACHE / ~CATCH) ~= P(TOOTHACHE)

    P(TOOTHACHE /CATCH) = P(T|C, Ca)

                        = P(T|C, +Ca) * P(+Ca)  + P(T|C,-Ca) * P(-Ca) -> (1) (Joint Probability Expansion)

                        = (0.108 * 0.2) + (0.016 * 0.8)
                        = 0.0344



    P(TOOTHACHE / ~CATCH) =


                        = P(CATCH|T) * P(T)
                          -----------------	-> (2) (Bayes Rule)
                          P(CATCH)

