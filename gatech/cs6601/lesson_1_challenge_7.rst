Lesson 1 Challenge #7: Expectimax 2
===================================

.. image:: https://dl.dropbox.com/s/9va8q1bkx8w9c11/Screenshot%202017-03-08%2006.36.38.png?dl=0
   :align: center
   :height: 300
   :width: 450


Solution
--------

.. image:: https://dl.dropbox.com/s/em5f149onwq4fw4/Screenshot%202017-03-08%2007.10.57.png?dl=0
   :align: center
   :height: 300
   :width: 450


* If any point it time, if we see that evaluating further is not going to "improve" the expectimax value, we stop and
  prune the nodes in that level.

* In the mid-branch, As soon as we reach 6, we know, that's the max we can get. While evaluating further will give
   lower value, we are not interested because that is not going to change the result, and thus we prune it.

* In the right-most branch, after getting -3.2 in the first left tree of the right most branch, without looking
   further, we can state that the max we can get it 2.8 (Because -3.2 + (10 * 0.6) = 2.8), so we prune those branches.


