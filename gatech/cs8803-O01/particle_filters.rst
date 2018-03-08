Particle Filters
================

Field Trip
----------

* http://americanhistory.si.edu/

.. image:: https://dl.dropbox.com/s/3zuarzljc0o2q3l/Screenshot%202018-01-28%2016.28.57.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. attention::

   Information available by clicking on the image of the car.

.. image:: https://americanhistory.si.edu/sites/default/files/styles/blog_image/public/NMAH-ET2012-14098.jpg
   :align: center
   :height: 300
   :width: 450
   :target: http://americanhistory.si.edu/collections/search/object/nmah_1377824


.. image:: https://dl.dropbox.com/s/l74eze9fmg85bj6/Screenshot%202018-01-28%2016.37.58.png?dl=0
   :align: center
   :height: 300
   :width: 450

State Space, Belief, Efficiency
-------------------------------

Particle filters are

* Easiest to program
* Most flexible

.. image::  https://dl.dropbox.com/s/aoo0447ya40t5cw/Screenshot%202018-01-28%2017.05.46.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/4S-sx5_cmLU?rel=0&amp;controls=0&amp;showinfo=0&amp;start=85" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

* Global Localization
* Each of the red dot, is a discrete guess. There is a x-coordinate, y-coordinate, heading direction. These three values together comprise a single guess.
* `Posterior Predictive Distributions`_
* `Posterior Probability`_

.. _Posterior Predictive Distributions: https://en.wikipedia.org/wiki/Posterior_predictive_distribution
.. _Posterior Probability: https://en.wikipedia.org/wiki/Posterior_probability

Using Robot Class
-----------------

Using Radians

.. image::  https://upload.wikimedia.org/wikipedia/commons/4/4e/Circle_radians.gif
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/f5omxhxecxt1drr/Screenshot%202018-01-28%2018.52.00.png?dl=0
   :align: center
   :height: 300
   :width: 450


Filters
-------

.. image:: https://dl.dropbox.com/s/598o7c5c1l727xl/Screenshot%202018-01-29%2005.25.56.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/vks2hkeqh6vygij/Screenshot%202018-01-29%2005.27.08.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/vbf0e69xspbpge8/Screenshot%202018-01-29%2005.30.52.png?dl=0
   :align: center
   :height: 300
   :width: 450

Robot Movement
--------------

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/Ut0plKzMV0Q?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



1 - Field Trip
==============
So before I start today's class I'd like to take you on a trip that I recently
did to share some of the things that excite me in my life with all of you.
I actually went to Washington, D.C. and the highlight of the day for
me was to visit the National Museum of American History.
Some of you might know this.
In 1998 a team led by Wolfram Burgard and
myself put a robotic tour guide into this museum.
This robot was in the museum for about two weeks and it led kids and
visitors of the museum through the exhibit.
It did localization similar to what I taught you before.
It used a learned map of the environment.
We programmed by hand the specific location of exhibits and
was also able to say something.
It was also able to smile and to frown.
And as you can see in this video, sometimes even kids climbed onto it.
But today I'm here to see Stanley.
Stanley has been here for a couple of years now in exhibits our robot that won
the DARPA Grand Challenge, and it was really fascinating to see the thing
that we've built and visited in its own little room in the Smithsonian museum.
This exhibit has been made specifically to celebrate Stanley's victory.
And in exploring this exhibit again I found that the curators had
actually put some program code on the wall for people to understand.
Let's zoom in.
You can see common.
So, at the time you are already working with common faters and
in our parameter file, as shown here, the word common occurs many times.
So, what I've been teaching you last class about the common fater really had
a major role to play in making Stanley the robot win the DARPA Grand Challenge.
So these are deep emotional moments for me going back to the past and
seeing what we've done and how it's been preserved.
But I want to share with everybody here because it’s part of my life and
it’s part of what we’ve done in building self-driving cars, and
the methods I’m teaching you in this class are essentially the same methods as
we used back in Stanley and in Junior when we did the Urban Challenge.

2 - State Space
===============
[Narrator] So, in this class you will learn about particle filters.
In our sequence of algorithms for estimating the state of a system,
this is the third one and in many ways is the best one.
It's the easiest to program
and in most ways is the most flexible.
And to understand why I'm saying this let me start
with a little quiz that goes back into the first 2 classes.
In class 1, we learned about histogram filters,
in class 2 about kalman filters,
and we even had to prove there.
Today, I'll teach you about particle filters,
but we can't really know about particle filters quite yet.
So, my questions will only pertain to histogram filters and kalman filters.
First, I'd like to know whether the state space was discrete or continuous.
Please check exactly 1 of those 2 boxes over here,
and I understand these are not entirely non-ambiguous questions,
but in the spirit of the method please check whichever fits best.

3 - State Space Solution
========================
When a histogram filter was discrete
distribution was defined over a finite set of bins,
whereas the common filter had a continuous state space.

4 - Belief Modality
===================
[Narrator] So, let me ask you a second quiz.
In particular I would like to know whether distributions
that can be represented may be unimodal
or can also be multimodal.
So, check unimodal if this is all we can do,
whereas if we can have multiple bumps in our probability distribution,
check multimodal.

5 - Belief Modality Solution
============================
[Narrator] And here the histogram filter scores better.
Even though it was discrete, it was able to represent multiple bumps,
which the kalman filter couldn't, so it's unimodal.
If you forget this go back to the past class and look at this.
The kalman filter was a single Gaussian which is by definition unimodal,
whereas the histogram filter can have bumps over arbitrary grid cells.

6 - Efficiency
==============
[Narrator] The next question I wouldn't need to dwell on in the class,
but I think it's important.
When it comes to scaling in the number of dimensions of the state space,
the amount of storage we have to assign.
I give you 2 answers.
It could be quadratic or exponential.
So, we have quadratic exponential--quadratic exponential--and
I understand I didn't really discuss this,
but go back in your memory to how grids are represented
and how Gaussian's are represented,
and I promise you 1 of those answers is correct for either of the 2 filters here.

7 - Efficiency Solution
=======================
[Narrator] The histogram filter's biggest disadvantage is it scales exponentially,
and the reason is any grid that is defined over arcade dimensions
will end up having exponentially many grid cells in the number of dimensions,
which is really unfortunate because
we can't really represent high dimensional grids really well.
So, it works really well for low dimensional problems
like 3 dimensional robot localization problems.
The kalman filter in contrast, under certain assumptions,
is quadratic.
All we represented was a vector, the mean, and the covariance matrix,
and the covariance matrix is quadratic.
And it turns out all the computation, if your measurements space is a fixed size,
ends up to be quadratic without a proof here.
So, you just have to take it by faith,
but the queer thing is this is a much more efficient method.
So, if you have a 15, 20 dimensional state space,
the kalman filters will be more efficient than the histogram filters.

8 - Exact or Approximate
========================
[Narrator] Let me ask a last question.
When applied to robotics do we believe the histogram filter is exact or approximate?
Same here.
I know we've never talked about this.
Please just check the boxes you find most likely,
and then move on to see my explanation.

9 - Exact or Approximate Solution
=================================
[Narrator] While histogram filters tend to be approximate
because the world tends not to be discrete.
So localization, for example, it's clearly an approximate filter.
It turns out kalman filters are also approximate,
and it's a much more subtle observation.
It turns out kalman filters only are exact for linear systems,
whereas the world happens to be nonlinear.
Now this goes into a lot of deep math, which I don't want to get into here,
but you should understand that both of these filters are not exact.
Both of them tend to be just approximations of the correct posterior distribution.

10 - Particle Filters
=====================
[Narrator] Now let's look into particle filters, the subject of today's class,
and it's really interesting to see the answers for particle filters.
First, the state space for particle filters is usually continuous.
So, you can get into the more interesting version of state spaces,
but we're not confined to unimodal distributions.
We can actually represent arbitrarily multimodal distributions.
They are also approximate just like the other 2 filters,
and in terms of efficiency the world is still out there.
In certain incarnations, they clearly scale exponentially,
and it is a mistake to represent particle filters over anything more than say 4 dimensions.
But in other domains, mostly in tracking domains,
they tend to scale much, much better, and I've not seen a good treatment
yet of the complexity in practice for particle filters.
However, the key advantage of particle filters
is actually none of those things over here.
The key advantage, at least in my life, has been
they're really easy to program.
As you hopefully see today,
writing a particle filter is really, really easy.
In fact, you will write your own particle filter for a continuous value localization problem,
which is in many ways more difficult than any of the problems we talked about before.
So, let's dive in and see a particle filter in action.
So, here is a floor plan of an environment
where a robot is located and it has to perform what's called global localization,
which is it has no clue where it is and it has to find out
where it is just based on sensor measurements.
This provides his range sensors as indicated by the blue stripes
those use sonar sensors, which means sound, to range the distance of nearer obstacles,
and it has to use these range sensors to determine a good posterior distribution as to where it is.
What the robot doesn't know it's starting in the middle of the corridor.
In fact, it is completely uncertain as to where it is.
Now, the particle filter represents this using particles.
Each of these red dots of which there are several thousand here
is a discrete guess where the road might be.
It's structured as an X coordinate, a Y coordinate, and also a heading direction,
and these 3 values together comprise a single guess,
but a single guess is not a filter.
It is the set of several thousands of such guesses
that together comprise an approximate representation for the posterior of the robot.
So, let's start the video.
In the beginning the particles are uniformly spread,
but the particle filter makes them survive
in proportion of how consistent 1 of these particles is with a sensor measurement.
Very quickly the robot has figured out it's in the corridor, but 2 clouds survive
because of the symmetry of the corridor.
As the robot then enters 1 of the offices,
the symmetry is broken and the correct set of particles survive.
Let me play this again.
The essence of particle filters is to have
these particles guess where the road might be moving,
but also have them survive using effectively survival of the fittest
so that particles that are more consistent with the measurements
are more likely to survive and as a result
places of high probability will collect more particles,
and therefore be more representative of the robot's posterior belief.
Those particles together--those thousands of particles
are now clustered in a single location.
Those comprise the approximate belief of the robot as it localizes itself.

11 - Using Robot Class
======================
[Narrator] Hi, I'm Kathleen and Sebastian wrote a piece of code for you
that I am now going to demonstrate.
So, the main class is a class called robot.
This robot lives in a 2-dimensional world of size 100 meters X 100 meters.
It can see 4 different landmarks that are located at the following coordinates:
20, 20; 80,80; 20,80; 80,20.
So, here's how we make such a robot.
It's really easy.
All you have to do is call a function robot and assign it to a variable my robot.
So, now that we can do things with my robot.
For example, we can set a position.
These 3 values are the X coordinate, the Y coordinate, and the heading in radians,
and this command assigns those values to the robot.
So, let's print these things out
and down here you see the output
X=10, Y=10, and heading=0.
Next, let's make the robot move. This robot moves 10 meters forward and doesn't turn.
So, let's print the resulting position.
And here we go, you can see that it's now at 20, 10, and 0.
It moved 10 meters forward from 10,10 to 20,10.
Now, let's make the robot turn by pi/2 and move 10 meters.
So, now the robot is heading in the direction of pi/2,
and it moved forward 10 meters in the Y direction, instead of the X direction.
So, as you can tell it's really easy to program.
The last thing I want to show you is how to generate measurements.
There's a really easy command called sense
and all it does is give you the distance to the 4 landmarks, 1, 2, 3, and 4.
For now this is all you need to know about the class robot
that Sebastian has programmed for you.
You might want to spend some time familiarizing yourself with the code
to see how this is all configured.

12 - Robot Class Details
========================
[Sebastian:] Thank you Kathleen. I really appreciate it.
This code has a little bit more stuff than you just talked about.
It actually assimilates noise, but the noise filters are all set to 0,
and those noise filters are really important for particle filters
so you can play with those if you like.
In fact, there's a function over here called set noise.
It allows you to set them,
and then later on we have a function that makes kind of no sense right now,
but really important as we implement particle filters called measurement probability,
and this accepts a measurement and tells you how plausible this measurement is.
It's kind of the key thing for the survival of the fittest rule in particle filters.
So, if you look through the codes don't be confused by this function; we will actually use it later.

13 - Moving Robot
=================
[Narrator] Here's our first programming
exercise.
I'd like you to make a robot that starts
at coordinates 30 and 50,
and it heads north, which means its
heading direction is pi/2.
It then turns clockwise by pi/2, which
means you subtract pi/2 from the
heading direction, and it moves 15 meters.
It then senses, and I want you to print
out the sensor measurements.
It then turns clockwise by pi/2 again,
and moves 10 meters this time
and I just want you to print out the
sensor measurements after this entire
procedure. So, there are 2 print
statements for the sensor over here
and the sensor measurements over here. So,
here's the output I would like your
program to generate.
After the first motion, the first
measurements will be 39 plus something,
46, 39, and 46.
And then after the second motion I expect
to see 32, 53, 47, 40.
Of course, there's lots of decimal-point
numbers over here,
but these are the numbers I would expect
you to output.
So, have fun coding it!

14 - Moving Robot Solution
==========================
[Narrator] And here's my solution.
I initialized the robot--my robot--using the function robot.
I set the coordinates to be 30, 50, and pi/2.
I then apply the motion command, assign the result to my robot again
with minus pi/2 and 15.
I print the measurement values.
I move again, and I print the measurement filters again,
and when I hit run,
this is exactly what I get.

15 - Add Noise
==============
[Narrator] Next, I'd like you to play with the noise.
Our class robot has built-in noise variables.
One is for forward motion.
This is the added Gaussian noise variable to the motion you command.
The same for turn and the same for the sensor measurements.
And as I scroll down I find the function set noise
lets me set those values to values other than zero.
So, I want you to--into your code--set these values as follows:
forward noise equals 5.0, turn noise equals 0.1, and sense noise equals 5.0.
So, please fit this into your code.

16 - Add Noise Solution
=======================
[Narrator] And here is how I would do it.
I would just call the function set noise with the parameters as specified
for the object my robot, and when I hit run now
I get different values like those, or those, or those.
In fact, every single time I hit run
I get a different set of values.

17 - Robot World
================
[Narrator] So, now we know about our class robot
who can turn and then move straight after the turn,
and which it also can sense the distance to 4 designated landmarks,
L1, L2, L3, and L4, and these distances
comprise the measurement vector of the robot.
We told you the robot lives in a world of size 100 x 100,
and what this means if this robot falls off 1 end,
it disappears on the other.
So, it's a cyclic world.
So, let's now talk particle filters.

18 - Creating Particles
=======================
[Narrator] The particle filter that you're going to program
maintains a set of 1000 random guesses as to where the reward might be.
Now, I'm not going to draw 1000 dots here,
but let me explain how each of these dots looks like.
Each of these dots is a vector which contains an X coordinate,
in this case 38.2, a Y coordinate 12.4,
and a heading direction of 0.1,
which is the angle at which there are points relative to the X axis.
So, this one moves forward, it will move slightly upwards.
In fact, now a code--every time you call the function robot
and assign it say to a particle,
here the [i] particle,
these elements p[i]x, y, and orientation,
which is the same as heading,
are initialized at random.
So, to make a particle set of 1000 particles
what you have to program is a simple piece of code that assigns 1000 of those to a list.
So, let's do this; let me set N=1000 for 1000 particles.
Here's my initial set of particles; it's going to be an empty list,
and I want you to fill in some code
after which we have 1000 particles assigned to this vector over here.
So, when I print the length of this thing
I will get 1000 instead of 0.

19 - Creating Particles Solution
================================
[Narrator] Here's 1 possible solution if we iterate the following loop 1000 times
we create an object called robot, and we print this object to our growing list P,
and when we're done we have 1000 particles,
and let me do something I might regret,
which is let me just print out this entire set of particles with print P,
and what I get is 1000 items that look just like this over here.
If you have an X, a Y, and a heading direction all generated at random.
So, if you look through those you'll find there's a lot those.
So, we now have a set of 1000 particles,
each of which just looks like one of these dots over here,
and each of which has exactly 3 values associated,
an X, a Y, and an orientation.

20 - Robot Particles
====================
[Narrator] I now want you to take each of these particles
and simulate robot motion.
Depending on the heading direction,
this might yield a different direction.
So, each of these particles shall first turn by 0.1 and then move by 5 meters.
We already implemented something just like this for individual robot motion.
Now I'd like you to apply this to the entire particle set.
So, please go back to the code and make a new set P
that is the result of this specific motion turning by 0.1
and moving forward by 5.0
to all of those particles in P.

21 - Robot Particles Solution
=============================
[Narrator] So, here's one possible solution: reconstruct P2 as a temporary particle set
with a later set P equals P2, so this is just a temporary set.
We then go through all the particles, again, and here is the tricky line.
We append to list P2 the results of our motion of 0.1 and 5.0
applied to the [i] particle chosen from the original particle set.
So this applies the move command to each of the particles
exactly the same way we applied move to the robot motion before.
When we are done we reset P=P2.
So, we've done the full recursion of applying our motion update
to our full particle set.
If you've gotten this far then you got about half of particle filters implemented,
and fortunately it's the easy half,
but the difficult half isn't that much more difficult.

22 - Importance Weight
======================
[Narrator] Let me explain how the second half works.
Suppose an actual robot sits over here,
and it measures these exact distances to the landmarks over here.
Obviously, there some measurement noise that
would be just more or less an added Gaussian with 0 mean.
Meaning there would be a certain chance of being too short or too long
and that probability is governed by a Gaussian.
So, this process gives us a measurement vector of 4 values
of those 4 distances to the landmarks L1 to L4.
Now let's consider a particle that hypothesizes the robot coordinates
are over here and not over here, and it also hypothesizes a different heading direction.
We can then take the measurement vector and apply it to this particle.
Obviously this would be a very poor measurement vector
for this specific particle over here.
In particular, the measurement vector we would've expected looks more like this.
That just makes this specific location really unlikely.
In fact, the closer our particle to the correct position
the more likely will be the set of measurements given that position.
And now here comes the big trick in particle filters:
the mismatch of the actual measurement and the predicted measurement
leads to a so called importance weight
that tells us how important that specific particle is.
The larger the weight the more important it is.
Well, we now have many, many different particles and a specific measurement.
Each of these particles will have a different weight.
Some look very plausible, others might look very implausible
as indicated by the size of the circles over here.
We now let these particles survive somewhat at random,
but the probability of survival will be proportional to their weights.
If something has a very big weight like this guy over here
will survive at a higher proportion than
someone with a really small weight over here, which means
after what's called resampling,
which is just a technical term for randomly drawing N
new particles from these old ones with replacement
in proportion to the importance weight.
After that resampling phase,
those guys over here very likely to live on, in fact many, many times.
Whereas those guys over here likely have died out.
That's exactly what happened in our movie in the beginning
when we looked at localization in this corridor environment.
The particles that are very consistent with the sensor measurement
survive with a higher probability, and the ones with lower importance weight
tended to die out.
So, we get the fact that the particles cluster
around regions of higher posterior probability.
That is really cool and all we have to do is
we have to implement a method for setting importance weights
and that is, of course, related to the likelihood of a measurement,
as we will find out, and we have to implement a method for resampling
that grabs particles in proportion to those weights.
So, let's just do this.
So, let me add back the robot code.
We built a robot, and we make the robot move,
and we now get a sensor measurement for that specific robot using the sense function.
So, let's just print this out.
These are the ranges or distances to the 4 landmarks
and by adding your print my robot statement
you can also figure out weight importance as 33, 48, 0.5,
obviously this is a random output
because you randomly initialized the position of the robot.
What I want you to program now is a way to assign importance weights
to each of the particles in here.
I want you to make a list of 1000 elements
where each element on the list contains a number.
So, this number is proportional to how important that particle is,
and to make things easier I coded for you a function in the class robot
called the measurement probability.
This function accepts a single parameter, the measurement vector,
the Z edge as defined, and it calculates as an output
how likely this measurement is, and it uses effectively a Gaussian
that measures how far away the
predicted measurements would be from the actual measurements.
You can dive into this code and understand what's going on.
There's one last change we have to do to make this code run.
We have to actually assume that there is measurement noise.
If there is 0 measurement noise, then this function will end up dividing by 0.
So, let's put in a clause that specifies what we believe the actual measurement noise is.
I'm going to do this not for the robot,
but I do this for the particles.
In this line of code over here where we create the particles for the first time,
I now just initialized these positions remain numbers
but also assume a certain amount of noise that goes with each particle,
0.05 for the translational noise, 0.05 for the rotational noise,
and 5.0 for the measurement noise in those ranges.
So, this is the crucial number over here.
So, coming back to what I want you to do,
I wish you to construct a list of 1000 elements in W
so that each number in this vector reflects the output of the
function measurement probe applied to the measurement Z that we receive from
the rear robot, such that when I hit print W,
I actually get a list of 1000 importance weights.

23 - Importance Weight Solution
===============================
[Narrator] And this can be done in a single line of code.
You construct the list W by appending
the output of the function measurement prop applied to the [i] particle
with the augment of the extra measurement,
and as you can see over here most of them look insanely unlikely.
So, they have exponents -146, -24.
Some of them are more likely--the ones that are closer to the truth like -5.
Those are the particles that surely survive,
whereas those ones over here with a -126,
those are really ready to die off
because they are so far away from the truth we really don't need them anymore.
So, in the final step of the particle filter algorithm,
we just have to sample particles from P
with a probability that is proportional to its corresponding W value.
Particles in P that have a large value over here
should be drawn more frequently than the ones with a small value over here.
How hard can that be.

24 - Resampling
===============
[Narrator] And it turns out it's actually harder than you think,
but I'm going to show you how to do it,
and once you've done it, you can use the exact same code
forever for any particle filter.
But let me emphasize what resampling actually means.
We are given N particles, each of which has 3 values,
and there's N of them, and they also now have weights.
These are simple floats or continuous values.
Let's call big W the sum of all these weights,
and let's normalize them just for the consideration of what to do,
and it's called the normalized weights alpha.
So alpha 1 would be the weight 1 divided by the normalizer W,
and so on all the way to alpha N,
and obviously it goes without saying that the sum of all alphas is now 1,
since we normalized them.
What resampling now does is it puts all these particles
and then normalized weights into a big bag,
and then it draws with replacement N
new particles by picking each particle with probability alpha.
So, for example, alpha 2 might be large
so we're going to pick this one, P2.
Alpha 3 might also be large so we pick that one.
Alpha 4 might be really small but just by chance you might actually pick it.
So, we have P4 over here, and then we might pick alpha 2, again.
So, you get 2 versions of P2, perhaps even 3 versions of P2,
depending on the probabilities.
We have N particles over here.
We do this thing N times, which is why I said with replacement
we can draw multiple copies of the same particle,
and in the end those particles that have a high-normalized weight alpha over here
will occur likely more frequently in the new set over here.
That's called resampling.
So, to make sure you understand this
let me ask you a couple of quizzes.
Suppose we have 5 particles with the following importance weights:
0.6, 1.2, 2.4, 0.6, and 1.2.
If I, in the process of resampling,
randomly draw a particle in accordance to the normalized importance weights.
What is the probability of drawing P1,
P2,
P4 and P5?

25 - Resampling Solution
========================
[Narrator] And the answer is 0.1, 0.2, 0.4, 0.1, and 0.2,
and to see we just have to normalize those importance weights.
The sum of those numbers over here are 6.
So, we divide 0.6 by 6. We get 0.1.
1.2 divided by 6 is 0.2.
2.4 divided by 6 is 0.4.
Obviously those over here add up to 1.

26 - Never Sampled 1
====================
[Narrator] So, let me makes this alpha-wise expressive and ask another question.
Is it possible that P1 is never sampled
in the resampling step? Yes or no?
Please just check one.

27 - Never Sampled 1 Solution
=============================
[Narrator] And the answer is yes, in the random resampling process
something with an importance weight of 0.1 is actually
quite unlikely to be sampled into the next data set.

28 - Never Sampled 2
====================
[Narrator] Let me now ask the same question about P3
which is the particle with the largest importance weight.
Please check yes or no.
Is it possible that P3 is never sampled in the resampling step?
Yes or no?

29 - Never Sampled 2 Solution
=============================
[Narrator] And the answer is yes, again.
Even though this importance weight over here is large,
it could happen that in each of the 5 resampling steps
we pick one of the other 4.

30 - Never Sampled 3
====================
[Narrator] So, I'm going to ask you a tricky question and maybe you can calculate this.
So, what is the probability of never sampling P3?
To answer this question assume we make a new particle set
with N=5 new particles where particles are drawn independently and with replacement.

31 - Never Sampled 3 Solution
=============================
[Narrator] And the answer is 0.0777 approximately,
and the way to obtain this is
for this particle to never to be drawn in the resampling phase.
We always have to draw 1 of the following 4 particles.
Those together have a probability of 0.6 to be drawn,
which contrasts to the 0.4 for P3.
So for 5 independent samplings to draw 1 of those 4,
we get a total probability of 0.6 to the fifth,
which is approximately 0.0777.
Put differently, there is about a 7.7% chance that this particle over here is missing,
but with almost 93% probability we'd have this particle included.
If we hadn't set up P3, gone for P1 over here,
which has a much smaller probability of being drawn,
then this 0.07 will be as large as 0.59,
which is 0.9 to the fifth.
Now this means with about 60% chance
we will lose particle 1, and only with a 40% chance it will include it.
Put differently, the particles with small importance weights
will survive at a much lower rate than the ones with larger importance weights,
which is exactly what we wish to get from the resampling step.

32 - New Particle
=================
[Narrator] So, what I would like you to do next is to modify our algorithm
to take the lists of particles and importance weights
to sample N times the replacement and new particles
with a sampling probability proportional to the importance weights,
or in the code now that we calculated our new particles
and the corresponding importance weights, construct a new particle set P3,
which we will call P, again, when everything is said and done,
so that the particles in P3 are drawn from P according to the importance weight's W.
Now to warn you this is more difficult than it looks like.
I'm going to show you a trick in a second, so if you fail to do this don't worry.
I give you a chance to do it right now, but then I'm going to tell you
a little bit more about how to organize this
in an efficient way and you get a second chance.
So, try it out, see if you can do it, and if you fail
look for my advice and then try it again.

33 - New Particle Solution
==========================
[Narrator] Now it turns out this is not an easy thing to do and
obviously I think it might be to complete all this normalized alphas,
but you still have to be able to sample from those.
So, in the spectrum of our alphas you might draw a random variable
uniformly from the interval 0;1, and then find out the alpha
so that all the alphas leading up to it, and some are smaller than beta,
but if we add the new alpha to the sum you would get a value larger than beta.
Now that's doable. It's inefficient.
In the best case you get an N lock and implementation.
Let me show you what is commonly done, and I don't take any guaranty
that it's entirely unbiased, but there's a very simple trick.

34 - Resampling Wheel
=====================
[Narrator] So, here's an idea how to make this more efficient,
and it turns out empirically it also gives better samples.
Let's represent all our particles and importance weight in a big wheel.
Each particle occupies a slice that corresponds to its importance weight.
Particles with a bigger weight, like W5, occupy more space.
Whereas particles with a smaller weight occupy less space.
Very initially let's guess a particle index uniformly from the set of all indices.
I did note this as a uniform sample at U
from the discrete self choices of index 1 all the way to N,
and as a caveat in Python, of course, it goes from 0 to N-1.
So, say we pick W6.
Then, the trick is--then you're going to construct the function better.
Then, I initialize the 0 and to which I add--when I construct these particles--
a uniformly drawn continuous value that sits between 0 and 2 times W max,
which is the largest of the importance weights in the important set.
W5 is the largest, so we're going to add a random value that might be as large as twice W5.
Suppose the value we added brings us to here.
So, this is the value we actually drew,
measured from the beginning of the sixth particle which shows an initialization.
I now then iterate the following loop:
if the importance weights of the present particle doesn't suffice
to reach all the way to beta.
So, if W index isn't as big as beta, then I subtract from beta this very value W index
and I increment index by 1.
So, what have I done? I've moved index to over here,
and I removed this part of beta so the point over here is still the same as before.
We now get to the point where beta becomes smaller than W index,
which is the case in the next situation.
Now index=7.
Then, index is the index of the particle I pick in my resampling process.
So, I picked the particle index; I now iterate I add another uniform value to beta.
Say I add this one.
This is the value I add, this is the value beta previously had.
The same iteration now will make index flow up
reducing beta by all the slice over here, which is W7,
and then jump over here, and particle 1 is picked.
It can easily happen that the uniform value is so small
that the same particle is picked twice, and it's easy to see
that each particle is now picked in proportion to the total circumference
it spans in this wheel of particles.
So, this is essentially my implementation for the resampling step.
So, I want you--if you can--to implement that specific resampler in Python.

35 - Resampling Wheel Solution
==============================
[Narrator] So, here's my implementation of the resampling step,
and it follows the same logic that I gave you in a diagram.
We're creating a new set of particles called P3; it's an empty set in the beginning,
and inside this routine, every time I resample,
I add a particle from the previous particle set with the index index.
So, that's the main loop over here, and at the end I assign P3 back to P.
So, that's the resampling step.
My very first index is drawn at random.
This is a uniform random sampler of all the indices,
and then I had this running variable beta that I set to 0.0,
and I cash away the max of W just to be slightly faster.
You don't have to do this; they come in over here.
Doesn't really matter if we have max over here,
but then I go and produce exactly N particles, and the way I do this
I add to beta a uniform random that is twice as large
and maximum in the range as my max weight W.
Now, 2 times max weight W will be a very large step,
but by adding a random variable that sits between 0 and 1,
I have uniformity in 0 and 2 times MW,
and then while this beta variable is larger than the weight of the current index,
I subtract this weight from my beta value
and I increment index by 1 modeler N
the total number of particles, and when it's smaller I'm done.
I can just take that particle, add it, append it, and repeat.
So, this entire procedure over here is somewhat involved
if you got that right I'm impressed.
I hope you learn something from doing it.
It happens to be really easy to program once you know what to do,
and every time we write a particle filter you can just reuse it.
You never have to think about it again because there's nothing
domain specific in this specific procedure over here.
So, let's run it; if I run it nothing happens to that empty set.
So, let me print out the resulting set of particles.
So, now I have a print P over here.
Let me run it, and of course, I'm going to get 1000 particles, right?
A lot of particles but let's look through them.
If you just look at the first value over here, they are all about the same.
They are all between 76 and 82.
The second one--they're all about 42, 44, 43, 41, 39, 38.
So, what you've gotten here is a set of particles
that are all co-located .
So, instead of having a complete random set of particles, like we had before,
the resampling step--we can see this already gives me particles
of very similar X and Y positions.
Now it turns out the orientations are not very similar.
They jump like crazy, and the reason is--
--well, if you think about it, we only have 1 location so far,
our distances to landmarks are independent of the orientation.
Such as that our orientation plays no role in the protected measurement,
and therefore has no roll in the selection.
Let me make the point, again; here's our 4 landmarks,
and we measure the distances to those.
A robot facing this direction has a certain set of distances.
A robot facing a different direction, like this one,
has the exact same set of distances.
Therefore, in our particle future, the heading direction plays no role.

36 - Orientation 1
==================
Here's a quiz.
Will orientation or heading never play a role?
And the answers are:
Yes, Never--
so we always get a random set of orientations--
or No--eventually they matter?

37 - Orientation 1 Solution
===========================
And the correct answer is: of course they will eventually matter.
So No is the correct answer, and let me show this to you.
Again, assume our 4 landmarks
and consider our robot facing to the right, to this direction.
We get a certain set of distances
that is invariant to the orientation.
But now this robot moves, and we get a new set of distances.
And now orientation matters.
If we assume a different initial orientation,
like this one over here--
and that robot moves--
its measurements will be very, very different.
So orientation does matter in the second step of particle filtering
because the prediction is so different for different orientations.
Let's go and program this.

38 - Orientation 2
==================
So I want you to take this particle filter,
and program it to run twice.

39 - Orientation 2 Solution
===========================
And here's my answer: this is all initialization over here, so we shouldn't touch it.
But from here on, we want to do things twice.
So we're going to put a "for" loop here,
from "t in range(T):"
and then after in, add all the stuff below.
I end it all the way to the final statement,
but I only want to print the final distribution.
Let's run it--and surprisingly,
the orientations aren't really that well worked out.
If I go down I find, still, failure random orientations here.
But if I go to 10 steps forward,
which means the robot really moves quite a bit
across its environment,
and I hit the run button--
I actually get orientations that all look alike.
So you can see, they're all about 3.6, 3.8, 3.9, 3.7.
You can see the "y" values are all about the same
and the "x" values are all about the same.
So this is the particle failure working.

40 - Error
==========
What I'll do next is to give you
another program assignment.
Rather than printing out the particles themselves,
I want you to print out the overall
quality of the solution
and to do this, I've programmed for you an "eval" code
which takes in as a robot position
and a particle set,
and it computes the average error
of each particle, relative to the robot pos
in "x" and "y"--not in the orientation.
And the way it does it, it basically compares
the "x" of the particle with the "x" of the robot,
computes the Euclidian distance
of these differences, and averages all of those.
So it sums them all up
and it averages them, through the
number of particles over here, which is upper caps "m".
Now, there's some funny stuff over here.
The reason is, the world is cyclic
and it might be that the robot is at 0.0 or at 99.9.
It's about the same values
but, according to this calculation over here, they'd be different.
So while there's normalization over here,
I make sure that the cyclicity of the world
doesn't really affect negatively
the estimated error I've enclosed in the boundary.
You might parse this.
I'm adding "world_size" over to
the computer model operation and then
subtract the same thing over here--I can't even see it.
It's just too long a line.
Be that as it is, I want you to take the function, "eval",
and produce a sequence of performance evaluations.
And if we hit the run button,
I want you to produce something like this stuff over here:
4.9, 3.6, 2.9, 2.8, 3.1.
This is the residual error.
Remember, it's a world of size 100 by 100,
so this is actually a relatively small error,
compared to the world's size.
Can you code it so I get, for each iteration,
the error number produced by this routine over here?

41 - Error Solution
===================
So here's my solution.
It's the same command as: print eval(myrobot, p)--
I know it wasn't very hard,
but it gets you a kind of fun to play with it.
So here's the sequence of numbers I get out.
It turns out, we don't always get the same number.
Sometimes it doesn't work.
Here's the second run.
These are small values again--
another one, another one.
Here's one that's interesting, so we can look at these errors:
5, 5, 7, 1--
3, 5, 6, 7, 7, 6.
It is a good run, so the error is down to 6,
compared to whatever it would be
if you didn't do particle filters and had a random set of particles.
In fact, to understand this, let me just take the "print eval" command
and move it to the very beginning, where we have done no particle filters.
So hit run, and what you will find is
it goes from 38 to 4, 3, 3 in just one step of particle filtering,
which is a drastic reduction of error.
Now running many times, there will be cases where it fails,
where there's just no particle nearby.
Strangely, they don't show up right now.
When I was testing it and programming it, I actually got one of those.
I had an error of like 15 or 20.
Whenever I want to demo something it just doesn't work.
Well, this particle filter is just too good.
It just gets the answer relatively right really, really quickly.

42 - You and Sebastian
======================
So one thing I want to stress here is that
you've just programmed a full particle filter.
So you got, from me, kind of a very
primitive and rudimentary robot simulator
that uses landmarks as a way of doing measurements,
and it uses three-dimensional robot coordinates,
so it's a little bit better than the stuff we talked about in previous classes--
it's not quite a Google car yet.
And you solved the estimation problem.
In fact, you solved this problem in 30 lines of code.
That is an amazing small amount of code
for something that's amazingly powerful.
And you can reuse these 30 lines of code
in pretty much all problems you might study
that require particle filtering; they're very generic.
So let me get back to the theory of particle filtering.

43 - Filters
============
Let me ask you a few questions.
We had measurement updates and motion updates.
In the measurement update, the computer posterior over state
given the measurement.
And it was proportional to, up to normalization,
of probability of the measurement,
given the state times "p" of the state itself.
In the motion update, if you compute
a posterior over distribution, 1 times sublayer.
and that is the convolution of the transition probability
times my prior.
Now those formulas--those should look familiar.
This is exactly what you implemented.
You might not know you implemented this; let me explain
to you how you implemented it.
This distribution was a set of particles.
A thousand particles, together, represented your prior "x".
These were importance weights.
And technically speaking, the particles
with the importance weights
are a representation of distribution.
But we wanted to get rid of the importance weights
so by resampling, we work the importance weights
back into the set of particle so the resulting particles--
the ones over here--would represent the correct posterior.
You've implemented this.
I'm just telling you what the math is behind this.
This, you also implemented.
This was your set of particles again,
and you sampled from the sum
by taking a random particle over here
and applying the motion model with a noise model
to generate a random particle, "x-prime".
As a result, you get a new particle set
that is the correct distribution after the robot motion.
So you recognize the math, and hopefully
you understand how your code implements this math.
You can prove all kinds of interesting facts about this math.
For example, you can prove conversions if the number of particles goes to infinity.
It is obviously approximate.
Particles are not an exact representation.
And it was amazingly easy to program.
So when you go over your particle code
you realize you implemented a fairly involved
piece of math that is actually the same
for all the filters we talked about so far.
The same math underlies our histogram filter
we talked about in Class No. 1.
And the same math for Gaussians
is the Kalman filter we talked in Class No. 2.
So let me ask you an interesting question.
Which of the 3 filters did Sebastian use
in his Job Talk at Stanford?
Histogram Filters, Kalman filters,
Particle Filters or None of the above?
Check one or all that apply
and, of course, you can't really know unless
you Google me and look up my Home Page.
Then you might find out some evidence.
So just take a random guess
and I'll tell you the answer in a second.
I should say I was hired by Stanford,
in 2003, into a tenured Associate Professor position
so obviously my Job Talk wasn't that bad.

44 - Filters Solution
=====================
And the answer are those 2.
Those, I used in a Job Talk of 2003.
But I previously applied at Stanford and actually received an offer,
which I turned down, in 1998.
And in my earlier work, I didn't understand particle filters,
and I did everything with this filter over here.
But came 2003, I was a big, big fan of particle filters
and my Job Talk talked about a version of those
that applied them to the somewhat more involved
robot mapping problem.

45 - 2012
=========
Now fast forward to 2012.
We built the Google Car.
We're now using multiple methods.
We use histogram methods and particle methods.
The main difference to what you've learned, so far, is two-fold.
The main difference that we've learned so far
is the Robot Model.
The vehicle is actually modeled as a system
with 2 non-steerable wheels and 2 steerable wheels.
That's often called a Bicycle Model
because half of it--this thing over here--
acts like a bicycle.
The big difference is the Sensor Data.
Instead of using landmarks,
we get this really elaborate road map,
and then we take a single snapshot
and we match that snapshot into the map.
And the better the match,
the higher the score.
And then on top of it, we have additional sensors, like GPS.
We also have Inertial Sensors.
I am not going to go into those at all,
but the methods I taught you
are rich enough to handle these additional sensors.
So you've just learned about the jist of
the method in which the Google Car is able
to find where it is, and where other cars are.
When you build a system, you have to
try it with these more elaborate methods.
But I think it's very much doable.
It's very easy to replace
the current simple motion model with the slightly
more sophisticated, for what's called
a Bicycle Model, and it's easy to write
a correlation function of the map data
and computes normalized correlations
of measurement images in a big pixel map.
I'll leave this an an exercise
so if you want to hack your own car
and make it drive itself, have fun.
I just want to congratulate you.
You've actually, in these 3 classes,
learned pretty much as much as
any of my Stanford student learns
in my Specialized AI classes on robotics, when it comes to robot perception.
In fact, you've learned pretty much what there is to know
to become a successful practitioner in robotics.

46 - Preview
============
In the next class, I will tell you about
robot motion--how to make the robot move.
So we're going to move beyond the idea of
just state estimation--finding out where we are
or where the other cars are.
And we're going to move to the fascinating topic:
how to use all this to decide where to move.
So in the next class, I'll talk about a basic
AI method called "search"--.
in particular, "A* search"--which is an algorithm
invented by my colleague, Nils Nilsson, at Stanford
and I will apply it to the problem of planning
robot trajectories and making it move
in real time.
So I'll see you in the next class.

