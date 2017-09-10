Numpy References
================

numpy arrays
------------

::

    matrix = numpy.zeros([rows, columns])

    Access using matrix[2,3] which will return the value in row 2 and column 3.


sum of log probabilities
------------------------

* scipy.misc.logsumexp()

::

    logsumexp([-2,-3]) = numpy.log(numpy.exp(-2) + numpy.exp(-3))
    logsumexp(a, b) = log(e^a + e^b).

References
----------

* https://mubaris.com/2017-09-09/introduction-to-statistics-using-numpy