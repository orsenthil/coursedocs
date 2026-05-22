Machine Learning
================

Supervised Learning
-------------------

k-Nearest Neighbors (k-NN)
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Classify a new point by finding the k nearest examples in training data and applying majority label
* Distance metric (typically Euclidean) determines "nearest"
* k=1: decision boundary is Voronoi tessellation of training points
* Larger k smooths boundaries but may lose local structure
* Non-parametric: no assumptions about data distribution
* Lazy learner — stores all training data, no explicit model built

Cross-Validation
~~~~~~~~~~~~~~~~

* Split data into k folds; train on k-1, test on remaining fold; rotate and average error
* Estimates generalization performance without wasting data
* For time-series/sequence data, random fold selection is invalid — use temporal splits
* Leave-One-Out CV (LOOCV_): k = n; low bias, high variance of error estimate
* Use cross-validation to select hyperparameters (e.g., k in k-NN, tree depth)

.. _LOOCV: http://stats.stackexchange.com/questions/90902/why-is-leave-one-out-cross-validation-loocv-variance-about-the-mean-estimate-f

Gaussian Distribution and Bayes Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Gaussian (Normal) distribution: parameterized by mean μ and variance σ²
* Central Limit Theorem: sum of many independent random variables → Gaussian (https://en.wikipedia.org/wiki/Central_limit_theorem)
* Decision boundary between two Gaussians: point where posterior probabilities are equal
* Classification error = area of overlap between class-conditional distributions

**Bayes Classifier:**

* Optimal classifier minimizes total expected error
* Assigns class with highest posterior: argmax P(C|x) = argmax P(x|C)P(C)
* Requires knowing true class-conditional densities

**Naive Bayes:**

* Assumes features are conditionally independent given class: P(x₁,x₂,...,xₙ|C) = ∏ P(xᵢ|C)
* Maximum likelihood estimation for parameters from training data
* Works well even when independence assumption is violated
* Reference: `Naive Bayes Classifier with insect examples`_

.. _Naive Bayes Classifier with insect examples: http://www.cs.ucr.edu/~eamonn/CE/Bayesian%20Classification%20withInsect_examples.pdf

**No Free Lunch Theorem:**

* No single learning algorithm dominates all others across all possible problems
* Algorithm choice depends on problem structure and assumptions
* Reference: `No Free Lunch Theorems`_ (Wolpert & Macready)

.. _No Free Lunch Theorems: https://ti.arc.nasa.gov/m/profile/dhw/papers/78.pdf

**Naive Bayes vs k-NN:**

* Naive Bayes: fast training, works well with high-dimensional data, assumes feature independence
* k-NN: no training phase, captures complex boundaries, sensitive to irrelevant features and curse of dimensionality

Using Mixture of Gaussians
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Model complex distributions as weighted sum of Gaussians
* Kernel Density Estimation as non-parametric alternative
* Cross-validation to avoid overfitting when selecting number of components

Decision Trees
--------------

Basics
~~~~~~

* Hierarchical partitioning of feature space via axis-aligned splits
* Internal nodes: test on attribute; branches: attribute values; leaves: class labels
* Discrete attributes: multi-way split on values
* Continuous attributes: binary split on threshold (e.g., x > t)
* Decision trees are understandable and easy to explain
* Reference: `Decision Trees, Daniel Kohlsdorf`_

.. _Decision Trees, Daniel Kohlsdorf: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/notes/Machine-Learning/Decision-Trees_Kohlsdorf.pdf

Entropy and Information Gain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Entropy** measures impurity of a set S:

  H(S) = -Σ pᵢ log₂(pᵢ)

* H = 0 when all examples belong to one class (pure)
* H = 1 bit for binary classification with equal split
* Used to determine optimal attribute for splitting

**Information Gain** = reduction in entropy from splitting on attribute A:

  IG(S, A) = H(S) - Σ (|Sᵥ|/|S|) H(Sᵥ)

* Select attribute with highest information gain at each node
* Same attribute can appear at multiple levels in the tree
* Greedy top-down construction (ID3/C4.5 algorithm)

Minimum Description Length
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Occam's Razor applied to trees: prefer simpler models
* MDL: best hypothesis minimizes description length of data + hypothesis
* Pruning: remove subtrees that don't improve generalization
* Balance tree complexity against training accuracy

Random Forests
~~~~~~~~~~~~~~

* Ensemble of decision trees trained on bootstrap samples (bagging)
* Each tree considers random subset of features at each split
* Final prediction: majority vote across all trees
* Reduces variance/overfitting compared to single tree

Boosting
--------

* Ensemble method that combines weak learners sequentially
* Each new learner focuses on examples misclassified by previous learners
* Reweight training examples: increase weight of misclassified, decrease correctly classified
* Final classifier: weighted vote of all weak learners
* AdaBoost: exponential loss, weight α_t = ½ ln((1-ε_t)/ε_t) where ε_t is weighted error
* Highly resistant to overfitting in practice (margin theory)
* References: `Tutorial on Boosting`_, `Short Introduction to Boosting`_ (Freund & Schapire)

.. _Tutorial on Boosting: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/notes/Machine-Learning/Tutorial-on-Boosting_Freund-Schapire.pdf
.. _Short Introduction to Boosting: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/notes/Machine-Learning/Short-Introduction-to-Boosting_Freund-Schapire.pdf

Neural Networks
---------------

Perceptron
~~~~~~~~~~

* Single neuron: output a = f(w₀ + Σ wᵢxᵢ) where f is activation function
* Step activation: a = 1 if w₀ + w·x > 0, else 0
* Can represent linearly separable functions (AND, OR, NOT, NOR)
* Cannot represent XOR (not linearly separable)

**NOR gate example:**

::

   a = { true if w0 + i1*w1 + i2*w2 > 0, else false }

   Truth table for NOR:
   i1=0, i2=0 → 1
   i1=0, i2=1 → 0
   i1=1, i2=0 → 0
   i1=1, i2=1 → 0

   Weights: w0 > 0, w1 < -w0, w2 < -w0 (e.g., w0=0.5, w1=-1.0, w2=-1.0)

**Perceptron Learning Rule:**

* w ← w + α(y - ŷ)x where α is learning rate
* Converges if data is linearly separable (Perceptron Convergence Theorem)
* No convergence guarantee for non-separable data

Multilayer Networks
~~~~~~~~~~~~~~~~~~~

* Hidden layers allow representation of non-linear decision boundaries
* With one hidden layer and enough units: universal function approximator
* Sigmoid/logistic activation: σ(z) = 1/(1+e⁻ᶻ) — smooth, differentiable
* Network topology: input layer → hidden layer(s) → output layer

Back-Propagation
~~~~~~~~~~~~~~~~

* Gradient descent on network weights to minimize error
* Chain rule propagates error gradients from output back through hidden layers
* Weight update: wᵢⱼ ← wᵢⱼ - α ∂E/∂wᵢⱼ
* For output layer: δⱼ = (yⱼ - tⱼ)f'(netⱼ)
* For hidden layer: δⱼ = f'(netⱼ) Σ wⱼₖδₖ
* Issues: local minima, slow convergence, vanishing gradients in deep networks
* Reference: `Neural Networks Slides`_

.. _Neural Networks Slides: http://aima.eecs.berkeley.edu/slides-pdf/chapter20b.pdf

Deep Learning
~~~~~~~~~~~~~

* Multiple hidden layers learn hierarchical representations
* Techniques to train deep nets: pre-training, dropout, batch normalization, ReLU activations
* Resources: https://www.udacity.com/course/deep-learning--ud730, https://en.wikipedia.org/wiki/Deep_learning

Unsupervised Learning
---------------------

k-Means Clustering
~~~~~~~~~~~~~~~~~~

* Partition n points into k clusters by minimizing within-cluster sum of squares
* Algorithm: (1) initialize k centroids, (2) assign points to nearest centroid, (3) recompute centroids, (4) repeat until convergence
* Converges to local optimum; sensitive to initialization
* Hard assignment: each point belongs to exactly one cluster
* https://en.wikipedia.org/wiki/Unsupervised_learning

Expectation Maximization (EM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Generalization of k-means with soft (probabilistic) assignments
* E-step: compute posterior probability of each point belonging to each cluster
* M-step: update parameters (means, covariances, mixing weights) using soft assignments
* Guaranteed to increase likelihood at each iteration; converges to local maximum
* Reference: `Pattern Recognition and Machine Learning`_ (Bishop)

.. _Pattern Recognition and Machine Learning: https://s3.amazonaws.com/content.udacity-data.com/courses/ud954/notes/Machine-Learning/Mixture-Models-and-EM_Bishop.pdf

Gaussian Mixture Models (GMM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Model data as mixture of k Gaussians: P(x) = Σ πₖ N(x|μₖ,Σₖ)
* Parameters: mixing coefficients πₖ, means μₖ, covariance matrices Σₖ
* Trained using EM algorithm
* More flexible than k-means: captures elliptical clusters, soft boundaries
* Application: learning significant locations from GPS data (Ashbrook & Starner)
* Reference: `Using GPS to Learn Significant Locations and Predict Movement Across Multiple Users`_

.. _Using GPS to Learn Significant Locations and Predict Movement Across Multiple Users: http://www-static.cc.gatech.edu/~thad/p/journal/using-gps-to-learn-significant-locations.pdf

Resources
---------

* `Entropy and Information Gain`_
* Wild Dolphin Project: http://www.wilddolphinproject.org/
* CHAT (Cetacean Hearing and Telemetry): http://www.wilddolphinproject.org/our-research/chat-research/

.. _Entropy and Information Gain: http://www.math.unipd.it/~aiolli/corsi/0708/IR/Lez12.pdf
