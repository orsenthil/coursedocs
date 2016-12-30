Normalization
=============


Normalize
---------

* EER Diagram always produces the databases that are normalized.


.. image:: https://dl.dropbox.com/s/fik862fi4gl0fof/Screenshot%202016-12-11%2004.31.29.png
   :align: center
   :height: 300
   :width: 450


What is all about?
------------------

.. image:: https://dl.dropbox.com/s/zr07r6ysx78z58q/Screenshot%202016-12-11%2004.33.12.png
   :align: center
   :height: 300
   :width: 450


The Rules
---------

* No redundancy of facts.
* No cluttering of facts.
* Must preserve information.
* Must preserve functional dependencies.


Not a relation
--------------

* Multi-value attributes.
* Values of attributes are pull from set of atomic values.

NF2 = Non First Normal Form


.. image:: https://dl.dropbox.com/s/4owa0njcrz2uinn/Screenshot%202016-12-11%2004.35.43.png
   :align: center
   :height: 300
   :width: 450

Relation with Problems
----------------------

.. image:: https://dl.dropbox.com/s/e1fykdxxhfcfgms/Screenshot%202016-12-11%2004.37.06.png
   :align: center
   :height: 300
   :width: 450


Relation with Problems - Redundancy
-----------------------------------

.. image:: https://dl.dropbox.com/s/e2x3erylul0nqec/Screenshot%202016-12-11%2004.37.44.png
   :align: center
   :height: 300
   :width: 450

Relation with Problems - Insertion Anamoly
------------------------------------------

.. image:: https://dl.dropbox.com/s/34amdds3gv8n43r/Screenshot%202016-12-11%2004.38.43.png
   :align: center
   :height: 300
   :width: 450

Relation with Problems = Deletion Anamoly
-----------------------------------------

.. image:: https://dl.dropbox.com/s/ef3bvfkcggbi0p7/Screenshot%202016-12-11%2004.42.19.png
   :align: center
   :height: 300
   :width: 450

Relation with Problems - Update Anamoly
---------------------------------------

.. image:: https://dl.dropbox.com/s/1i568k7l76warda/Screenshot%202016-12-11%2004.42.52.png
   :align: center
   :height: 300
   :width: 450


Information loss
----------------

.. image:: https://dl.dropbox.com/s/navrsm7ma3vz4ia/Screenshot%202016-12-11%2004.43.56.png
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/f1s8djbkg0zpwhx/Screenshot%202016-12-11%2004.45.49.png
   :align: center
   :height: 300
   :width: 450

Dependency Loss
---------------

.. image:: https://dl.dropbox.com/s/t41ys6i1vl9xdb8/Screenshot%202016-12-11%2004.46.57.png
   :align: center
   :height: 300
   :width: 450


Perfect Decomposition
---------------------

.. image:: https://dl.dropbox.com/s/w4sdqd41h4o1gcr/Screenshot%202016-12-11%2004.48.13.png
   :align: center
   :height: 300
   :width: 450

Functional Dependencies
-----------------------

.. image:: https://dl.dropbox.com/s/wjhcf440u2fyd5q/Screenshot%202016-12-11%2004.53.09.png
   :align: center
   :height: 300
   :width: 450

Full Functional Dependency
--------------------------

.. image:: https://dl.dropbox.com/s/qs007cjxyi8bb8z/Screenshot%202016-12-11%2004.55.17.png
   :align: center
   :height: 300
   :width: 450


Functional Dependencies and Keys
--------------------------------

* How to enforce functional dependency.
* We use keys to enforce functional dependencies X->Y

.. image:: https://dl.dropbox.com/s/ln6esmz2o989o3o/Screenshot%202016-12-11%2004.56.34.png
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/aezx2lg75fuzcgs/Screenshot%202016-12-11%2004.56.56.png
   :align: center
   :height: 300
   :width: 450


Overview of Normal Forms
------------------------

* Non First Normal Forms Datastructures

.. image:: https://dl.dropbox.com/s/24oslo8mr37pz9z/Screenshot%202016-12-11%2004.58.43.png
   :align: center
   :height: 300
   :width: 450


Normal Form - Definitions
-------------------------

* NF^2: Non First Normal Form
* 1NF: R is in 1NF iff all domain values are atomic.
* 2NF: R is in 2NF iff R is in 1NF and every non-key attribute is fully dependent on the key.
* 3NF: R is in 3NF iff R is in 2NF and every non-key attribute is non-transitively dependent on the key.
* BCNF (Boyce-Codd Normal Form): R is in BCNF iff every determinant is a candidate key.
* Determinant: A set of attributes on which some other attribute is fully functionally dependent.

Kent and Diehr Quote
--------------------

All attributes must dependent on the key (1NF), the whole key (2NF), and nothing but the key (3NF), so help me codd!

1NF BCNF flow chart
-------------------

.. image:: https://dl.dropbox.com/s/mjqpuivz5l66g8o/Screenshot%202016-12-11%2005.07.07.png
   :align: center
   :height: 300
   :width: 450

Compute with Functional Dependencies with Armstrongs Rules
----------------------------------------------------------

.. image:: https://dl.dropbox.com/s/ppq1zlmy2cp69m0/Screenshot%202016-12-11%2005.09.00.png
   :align: center
   :height: 300
   :width: 450

How to guarantee lossless joins
-------------------------------

.. image:: https://dl.dropbox.com/s/o882lrutcylyvhm/Screenshot%202016-12-11%2005.10.29.png
   :align: center
   :height: 300
   :width: 450

How to guarantee preservation of FDs
------------------------------------

.. image:: https://dl.dropbox.com/s/1iis9f3rv0i0dzv/Screenshot%202016-12-11%2005.11.24.png
   :align: center
   :height: 300
   :width: 450

Email Interest - Good Decomposition
-----------------------------------

.. image:: https://dl.dropbox.com/s/0zv46277e6c9d1t/Screenshot%202016-12-11%2005.12.59.png
   :align: center
   :height: 300
   :width: 450

3NF and BCNF
------------

* There does exist relations which can only be decomposed to 3NF, but not to BCNF, while being lossless and dependency preserving.

* It can only happen when the relation has overlapping keys.

It Never Happens in Practice
----------------------------

* There does exists relations that exists in 3NF and not in BCNF. (Only in theory)


