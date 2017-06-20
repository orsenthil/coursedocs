Left Recursion
==============

We should eliminate the left recursion without changing the language.

.. math::

    A \rightarrow A \alpha \: \ \beta

The language the above generates is :math:`\beta \alpha^*`
The above representation is not in the grammar form.


We can convert the above language to left recursive form like this.

.. math::

    A \rightarrow \: \beta A'

    A' \rightarrow \: \epsilon | \alpha A'
