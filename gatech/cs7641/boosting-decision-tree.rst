.. title: Assignment 1 - Boosting Decision Tree
.. slug: boosting-decision-tree
.. date: 2015-09-19 20:08:35 UTC-07:00
.. tags: exercise
.. category: exercise
.. link: 
.. description: 
.. type: text

Boosting is the property to improve the classification of the decision tree. I used the same
student dataset to perform boosting on the decision tree. But any number of iterations did not
improve the Percent correct of the decision algorithm with boosting.

For the student dataset, the boosting value turned out to be always lesser than non boosted output.

Performance of the algorithm with boosting vs non boosting.

.. image:: https://dl.dropbox.com/s/ng9gvoozl1uoens/J48_vs_Boosting_for_Student_Dataset.png
   :align: center
   :width: 400
   :height: 300


.. image:: https://dl.dropbox.com/s/x0bi8h5qyngnz6y/Boosting_Surprise.png
   :align: center

My assumption with reduction in effectiveness of boosting in this dataset is likely due to
overfitting of the data. The maximum percent with boosting at 67.29 was close the a good
performance of a J.48 algorithm, but overfitting is certainly coming into picture here.

I took another ensemble method, bagging in order to improve the decision tree classifier for the
the same student performance dataset. Here is what I found out.

The emsemble method, bagging constantly is better than J.48 Decision Tree for this dataset.

.. image:: https://dl.dropbox.com/s/m4nqratdcqxleuy/Algorithm_Performance_Student_Data.png
   :align: center
   :width: 400
   :height: 300

Boosting should give better performance on a dataset that can build shallow tree. To demonstrate
this aspect of boosting, I took an alternate dataset to compare and construct the boosting vs non
boosting approach.

Another dataset just to show the boosting and ensemble can be better.

**Ionosphere Dataset**

Ionosphere_ is another dataset, which has 35 attributes and 361 instances. This dataset is
popular for high accuracy of the decision tree model.

On a normal classification on this dataset, a J.48 learner can have 91.453 % accuraccy, a figure
that we were never able to get close in the student dataset.

We will see that boosting and other ensemble learning in the Ionosphere dataset.

.. _Ionosphere: http://archive.ics.uci.edu/ml/datasets/Ionosphere


.. image:: https://dl.dropbox.com/s/vz3eda4m9tw12vd/J48_Boosting_Bagging_Ionsphere.png
   :align: center
   :width: 400
   :height: 300


.. image:: https://dl.dropbox.com/s/gz1yeqrut2zqsp9/ionosphere_boosting.png
   :align: center

Bagging has a very high percentage correctness. It is noticeable that Boosting performs better than
normal decision tree.
