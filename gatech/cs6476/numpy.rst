NumPy Reference
===============

Array Operations
----------------

.. code-block:: python

   import numpy as np

   matrix = np.zeros([rows, columns])
   matrix[2, 3]  # access row 2, column 3

Common types and functions:

- ``np.uint8``, ``np.uint16``, ``np.float32`` — common image data types
- ``np.around(arr)`` — element-wise rounding

Log-Sum-Exp
------------

For numerically stable sum of log probabilities:

.. code-block:: python

   from scipy.special import logsumexp

   logsumexp([-2, -3])  # = np.log(np.exp(-2) + np.exp(-3))
   # logsumexp(a, b) = log(e^a + e^b)

Resources
---------
