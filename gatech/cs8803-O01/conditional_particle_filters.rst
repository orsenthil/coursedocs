Conditional Particle Filters
============================

**Senthil Kumaran <skumaran@gatech.edu>**


A Summary on **Conditional Particle Filters for Simultaneous Mobile Robot Localization and People Tracking** by Michael Montemerlo, Sebastian Thrun, William Whittaker.

* http://ieeexplore.ieee.org/document/1013439/
* http://www.cs.cmu.edu/~mmde/
* https://pdfs.semanticscholar.org/9ec1/16137bf6b3ca6a14903472725f4460eeab7d.pdf


This paper presented Conditional Particle filter, an extension of to traditional particle filters that breaks high dimensional particles into two lower dimensional particles, one conditionally dependent on the other.

The algorithm was demonstrated in the context of the Mobile Robot Localization and People-Tracking. It considers the problem where the pose of the robot and positions of the peole in the map are both unknown. It terms that as "Joint estimation problem."  By approximating the joint distribution as large set of particles representing people locations conditioned upon a smaller set of particles representing robot pose, the expressive power of the joint hypothesis can be exploited in a way that is still computationally tractable.


Particle filters estimate the posterior over unobservable state variables from sensor measurements. The same principle applies to Conditional Particle filters too, but the posterior is conditioned on the variable that we choose.

The paper illustrates this using the equation.

.. math::

    x_t = \{ r_t, y_{t,1}, y_{t, 2}, y_{t, M} \}


where :math:`r_t` denotes the robot pose at a time t and :math:`y_1, .. y_M` denote the locations of the M people

Conditional particle filters uses the following representation

.. math::

    p(x_t | z^t, u^t) = p(r_t | z^t, u^t) \Pi_{m=1}^M p(y_t, m | r_t, z^t, u^t)


The resulting particle filters had very high local reliability. The conditional particle filter described in this paper tend to scale linearly with the number of people, making the algorithm easier to implement in real time in environment with large number of people.

**Combined particle filter algorithm**

1) Does N samples like regular particle filter.

2) For each value in N, pick up a robot position.

    2a) For all the people in the room, calculates the conditional probablilty of the position based on the robot.

    2b) The weight vector is determined in the step 3.

3) Select the possible positions based on the weight vector.


This is a simple paper, and builds on top of "particle filter" exposition elegantly.

This paper was published in 2002 with the hypothetical demonstration and solving the problem of people finding or robot finding in an environment where the location of both people and the robot is unknown.
However,  I see how the concept can be very well utilized in production with `Amazon Go`_ like grocery store where multiple cameras need to track the person and the position of the person can vary at different instances. Amazon does not give much detail on the technology and seems to suggest that it is using `Deep learning for computer vision`_ with these Amazon go stores. But the robot localization and conditional particle filtering seems like extremely suitable approach to solve the problem. And perhaps, if the problem domain scales to a motion tracking in real time for very large store, during crowded event, like Black Friday sale in US, then efficient algorithms are needed over feature recognition methods.


.. _Amazon Go: https://www.amazon.com/b?node=16008589011
.. _Deep learning for computer vision: https://aws.amazon.com/rekognition/


