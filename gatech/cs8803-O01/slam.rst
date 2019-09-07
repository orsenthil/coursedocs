1 - Putting It All Together
===========================

[Sebastian:] Welcome to Unit 6 in CS373: Programming a Robotic Car.
This is the final unit focused on putting it all together.
Let's now review some of the things you've learned.
You learned about localization, tracking, planning, and control.
And you also learned about probabilities, so-called filters, you learned about A*, dynamic programming (DP),
and about PID control. This is a lot of stuff, and you implemented quite a bit.
So today, we take all those pieces, and we put them together to build a true, robotic, self-driving car.
Let's start with localizing.

2 - Localization
================

We learned about how maps are being used to localized a moving robot.
Here is a laser map being produced--in this case, Stanford's car,
and we used particles to localize this robot
by matching momentary measurements with the previously acquired map.
In doing so we were able to localize Junior in the Darpa Urban Challenge
with centimeter precision.
A similar method is being used by the Google Street View car,
and it is one of the secrets sources of the street-view car.
We heavily rely on a previously built map and a type of localization method
that you implemented to localize the robot and make it follow known lanes.
Here is a localization quiz.
We learned about the 3 filters, Kalman filters, histogram filters in our first class,
and particle filters.
Check the corresponding box if the attribute applies.
If any of those is multimodal in their distributions, please check the box,
exponential in the computation complexity relative to the number of dimensions,
and useful in the context of robotics.
Please check none, any, or all of those boxes.

3 - Localization Solution
=========================
Of course, we learned that the Kalman filter is unimodal, just a single bump,
whereas histograms and particles can have multiple bumps.
The Kalman filter was more efficient than the histogram and the particles
that both require exponentially many units in the number of dimensions in the worst case.
And yes, my god, they are all extremely useful--super, super useful
in case you didn't get this from the class.

4 - Planning
============
We also learned about planning--in particular, breadth-first planning,
A-star planning, and dynamic programming planning
that all address slightly different use cases.
Those are being used to plan the trajectory of the Google Street-View car
and the Darpa Grand Challenge cars.
In fact, you implemented a good number of those, which is quite amazing.
Here is my quiz for planning.
You learned about breadth first, A-star, dynamic programming,
and for the sake of this comparison I will also include the smoother,
which is more like plan refinement.
Check any or all of those boxes if the corresponding planner
acts in a continuous space, if it finds an optimal solution,
if it's a universal plan--
that means the solution, once found, can be applied to arbitrary states--
or if the solution is local, which means given an approximate initial solution,
it cannot really do anything more than just locally refine the solution.

5 - Planning Solution
=====================
Smoothing was the only planner that actually really worked in a continuous domain.
Everything else was very discrete.
Our breadth-first, A-star, and dynamic programming all find the optimal solution.
Dynamic programming is the only one that's universal,
and smoothing is the only local operation
whereas those over here all optimize a global planning problem.

6 - PID
=======
Then we also learned about control. You implemented your first controller.
Control is what makes things like the following experiment possible.
Here's my quiz.
You learned about PID control and, specifically, the P term, the I term, and the D term.
Which of the terms is most associated with the idea of avoiding overshoot,
minimizing error relative to a reference trajectory, and compensating drift.
I want you to check exactly one check box for P, one for I, and one for D.

7 - PID Solution
================
The primary function of P is to minimize the error. We steer in proportion to the error.
The D term avoids the overshoot, if used wisely.
Systematic drift and biases are best addressed by the I term.
That's the correct answer, which I'm sure you got right at this point.

8 - Your Robot Car - lang_en
================-===========

Now let's put them all together into a single piece of software.
Upfront it took me about a whole day to do this.
I'm not going to ask you to do it all yourself,
because it's going to cost you probably at least an hour if it takes me a day.
But I still want to be able to take all the lessons that we did together into a single system.
I'm going to help you a little bit--bits and pieces--
but up front here is the environment that I wrote for you,
which is very much derived from the environment we studied in the past.
We have a class robot that has certain kinds of noise characteristics you can find over here.
As I scroll down, you can see the familiar init function, the position-setting function,
the set_noise function, and then we have two checking functions--
whether we have a collision with the world called "grid," which I will show you in a minute.
and we have a check_goal function to see if we reached a goal
according to a certain distance threshold.
The move function should be very familiar at this point.
It applies noise to the motion command.
It the same code that you originally wrote.
Then we have a very simple sense function, which measures the robot's (x, y) location,
similar to a GPS on a car but with substantial measurement noise.
Corresponding to this sense function we have a measurement probability function
that you might want to use in your filter, and it evaluates the probability
of a measurement relative to the ground truth coordinates of the robot using Gaussians.
Armed with all this here is the problem.
I'm going to give you a grid. Here is an example grid. Let me draw this for you.
This specific one happens to be of dimensions 6 and 5,
and there are a number of blocked off cells like this.
If we look carefully into the code, you'll find information about the initial starting location
on the left upper corner and the goal location, which is the bottom right corner.
In putting everything together, you're going to build a robotic car using our bicycle model
that'll drive through the free space through the continuous free space
on something close to the shortest path all the way into the goal.
Here is my solution that I implemented
and that you will get to see for the most part towards the end of this class.
I am starting up over here. These are my obstacles.
They implement as circles through the center of these grid cells.
It's not exactly correct but good enough for my implementation.
Here are multiple runs using the same code, and you can see they're far from optimal.
They are non-optimal because there is control noise,
and there is also measurement noise.
But they all make it safely through free space into the corner where the goal objective is.
If we look at them in detail, like this solution over here.
You'll find that the spacing of the circles is somewhat variable.
You'll find that there's little corners over here that are either the result of control noise
or of measurement noise or of my somewhat deficient implementation.
You'll also find the control set points that are the smooth points of my A-star planner
as shown here in green.
In the version that I implemented for you, the controller does something very, very different.
It actually chooses as the control objective to head straight to the goal,
using the atan2 function, executes the action at a speed of 0.1,
and then reports a collision whenever the robot is moving.
Just looking down to the output where we see the robot's coordinates
along with the orientation there are very frequent collisions
that the robot undergoes in its attempt to reach the goal,
which it eventually does, but you can see 2 big regions of collisions
until the goal is finally reached.

8 - Your Robot Car
==================
Now let's put them all together into a single piece of software.
Upfront it took me about a whole day to do this.
I'm not going to ask you to do it all yourself,
because it's going to cost you probably at least an hour if it takes me a day.
But I still want to be able to take all the lessons that we did together into a single system.
I'm going to help you a little bit--bits and pieces--
but up front here is the environment that I wrote for you,
which is very much derived from the environment we studied in the past.
We have a class robot that has certain kinds of noise characteristics you can find over here.
As I scroll down, you can see the familiar init function, the position-setting function,
the set_noise function, and then we have two checking functions--
whether we have a collision with the world called "grid," which I will show you in a minute.
and we have a check_goal function to see if we reached a goal
according to a certain distance threshold.
The move function should be very familiar at this point.
It applies noise to the motion command.
It the same code that you originally wrote.
Then we have a very simple sense function, which measures the robot's (x, y) location,
similar to a GPS on a car but with substantial measurement noise.
Corresponding to this sense function we have a measurement probability function
that you might want to use in your filter, and it evaluates the probability
of a measurement relative to the ground truth coordinates of the robot using Gaussians.
Armed with all this here is the problem.
I'm going to give you a grid. Here is an example grid. Let me draw this for you.
This specific one happens to be of dimensions 6 and 5,
and there are a number of blocked off cells like this.
If we look carefully into the code, you'll find information about the initial starting location
on the left upper corner and the goal location, which is the bottom right corner.
In putting everything together, you're going to build a robotic car using our bicycle model
that'll drive through the free space through the continuous free space
on something close to the shortest path all the way into the goal.
Here is my solution that I implemented
and that you will get to see for the most part towards the end of this class.
I am starting up over here. These are my obstacles.
They implement as circles through the center of these grid cells.
It's not exactly correct but good enough for my implementation.
Here are multiple runs using the same code, and you can see they're far from optimal.
They are non-optimal because there is control noise,
and there is also measurement noise.
But they all make it safely through free space into the corner where the goal objective is.
If we look at them in detail, like this solution over here.
You'll find that the spacing of the circles is somewhat variable.
You'll find that there's little corners over here that are either the result of control noise
or of measurement noise or of my somewhat deficient implementation.
You'll also find the control set points that are the smooth points of my A-star planner
as shown here in green.
In the version that I implemented for you, the controller does something very, very different.
It actually chooses as the control objective to head straight to the goal,
using the atan2 function, executes the action at a speed of 0.1,
and then reports a collision whenever the robot is moving.
Just looking down to the output where we see the robot's coordinates
along with the orientation there are very frequent collisions
that the robot undergoes in its attempt to reach the goal,
which it eventually does, but you can see 2 big regions of collisions
until the goal is finally reached.

9 - Segmented CTE
=================
I spent a couple hours porting all the code over into this new format,
and I want to spare you all this editing work so in the final code
that is a little bit incomplete still, we have a grid.
We've got a function called "main."
Main then runs a path planner, A-star, smooths it, and then runs the controller, as in "run."
Then the controller even implemented for you our particle filter that you're familiar with.
There's nothing new here.
You're going to get the exact same code from class that you programmed yourself.
Then I go through a loop where I compute a crosstrack error,
apply my only PD controller--here is no I term here--
and I run my particle filter as before to estimate where the robot is.
What I would like you to do is to implement the crosstrack error function,
and I want you to use as an input the estimate, not the actual robot position,
but the best estimate, which you can get by running filter.get_position.
Now here is the difficulty, and I can tell you confidently it took me more than an hour
to solve this problem myself just for this class.
Our path now is a sequence of linear pieces.
When our robot drives along, it has a certain crosstrack error,
but as the robot state project beyond the end of a line segment, as is happening here,
we have to change the corresponding line segments to be the next one.
I addition, to calculating the assigned error relative to an arbitrary line segment,
not just the y-axis, we also have to detect when the robot steps beyond
the end of a line segment and switch over to the next one.
Now, suppose this is our line segment.
The path is given by the coordinates of the beginning point, p1, and the end point, p2,
both of which are (x, y) coordinates, which you get straight in the path.
Suppose our robot's position is something like this
where it has its own (x, y) estimate that comes out of the particle filter in your case,
and it has it's own orientation, theta.
Then both the cross track error as well as how far it has progressed
along the line segment--call this "U"--can be calculated using a dot product.
Specifically, let's call this vector over here delta x and delta y
as defined in x2 minus x1, and y2 minus y1--this vector over here.
Let's call this vector over here our Rx, which is x minus x1, and Ry.
Then U, the ratio of how far we've progressed along this segment is given
by the dot product Rx times delta x plus Ry times delta y
divided over the sum of squares delta x times delta x plus delta y times delta y. Why?
Well, this normalizes the vector length to 1, and this is the dot product of this vector over here
and the green vector, which happens to define the distance.
If this is larger than 1, we know we've left the segment and it's time to move onto the next one.
Finally, the crosstrack error--the red one over here--is given by a similar
but not identical dot product of Ry times delta--
notice we are now multiplying a y with an x--
minus--instead of plus--our x times delta y
with the exact same normalizer as down here.
You can see the normalizer over here.
What I want you to implement are these pieces of math over here.
When you run your controller, you will find that I setup for you a variable called "index"
that's the index into your path.
When U exceeds 1, we should increment this index
to make sure it never goes beyond what's legal in path length.
The crosstrack error should be computed relative to the current index
and is, of course, the assigned error using the exact same dot product I've shown you.
The last thing I want to tell you is what the path is.
I want you to use the following path.
The path is called "S" path.
It is given the run function as one of the parameters over here.
You can see it up here.
S path index is the indexth element of this path and 0 stands for x and 1 stands for y.
Please fill in the missing code over here.
I should tell you, when you run our controller with the missing code included,
you get actually a valid, nice path that mostly doesn't collide.
Occasionally it does, because of randomness in the system,
but it should be mostly collision free.
For this example, it will require about 130 or so robot steps.
Just so that you see a typical answer, here is a random run.
You read this as follows--true means the robot actually found the goal,
zero means zero collisions, and it took 137 steps.
Let me run it again, and here is another outcome.
The robot didn't collide and reached the goal in 145 steps.
I should warn you that sometimes I do get collisions here,
and it's because our obstacle surfaces are relatively large.
The noise in the system makes it hard to navigate.
But most of the time we should be able to get to the goal without difficulties
if we implement this piece of code correctly.
Just to warn you, it took me quite a while to work this out.

10 - Segmented CTE Solution
===========================
Here is my code.
I compute the dx and dy the way I told you by using the spath of index i + 1
minus the same at index.
My rx and ry, called drx and dry over here, are the robot estimates
as obtained by the filter minus the path.
Then I apply the exact same two equations that I gave you for the progress U
and the crosstrack error cte as shown over here.
Of course, if I advance too much I add 1 to the index.
You could have done this before computing the crosstrack error,
but I chose to do it afterwards.
So I add the missing bracket, and when I run it I get sometimes a collision.
There are two collisions here but I still reach the goal in 140 steps.
Let me run it again, and now I reach the goal without collision.

11 - Fun with Parameters
========================
In the final question, I'd like to explore something.
I don't have a good answer for this, but I'd like you to play with those parameters over here--
the data weight, the weight smoother, the control parameters p_gain and d_gain.
Play with them, try to find a setting that gives me fewer collisions on average
than my current parameters and maybe reaches the goal even faster.
I should warn you these are about the best variables I could find,
but I didn't really apply twiddle to this.
I did more of an approximate investigation of what a good parameter might be.
When you apply twiddle and try this, you will find that it's hard to apply
because your function might never return, so you have to build in the time somehow.
It's fun playing with those to see if you can find a better solution than what I gave you.
If you do so, don't expect the correct answer from me. I didn't implement it myself.
But I want to give you the opportunity to play with those parameters
and see what the effects are on this solution.

12 - Wrap Up
============
This finishes the lecture part of CS373, my basic introduction to robotic AI.
Even though we haven't done the final exam yet,
I want to congratulate you for getting this far.
The fact you got this far means you are really likely a very amazing student.
You put a lot of work into this--I know this.
It took me a lot of work to make those classes, but it probably took you even more to digest them.
I hope you learned a lot and had a lot of fun
and you feel empowered to program robots better than before.
What I taught you, I believe, is the very basic set of methods that any roboticist
should know about programming any robot intelligently.
All of those robots have tracking problems, state estimation problems,
planning problems, and control problems--be it a surgical robot, be it a robot maid,
or your intelligent future household robot ,
or even a flying robot, such as an autonomous plane.
I want to thank you for being with us so far.
The rest of this unit contains extra information on SLAM.
Otherwise, I'll just see you on the final.

13 - SLAM
=========
Hi, students. I am back to teach you a bit about SLAM.
There was a request--a popular request, actually, in email and the discussion forum.
SLAM is a method for mapping that's short for "simultaneous localization and mapping."
Some of the this might show up in the final exam, so do pay attention.
Mapping is all about building maps of the environment.
You might remember in the localization classes we assumed the map was given.
One of the big passions in my life has been to understand how to make a robot
make these maps like this map here, which is a 3D map
of an abandoned underground coal mine in Pennsylvania
near Carnegie-Mellon University.
Over the past 10 years or so, I have worked on a number of different methods
for buildings maps that are quite sophisticated,
like this particle filter method over here that you can see.
All these methods have in common that we build a model of the environment
while also addressing the fact that the robot itself accrues uncertainty while it moves.
When, in this example here, the loop is being closed,
you can see how our mapping technology is able to accommodate this
and find a consistent map despite the fact that the robot drifted a little along the way.
The key insight in building maps is the robot itself
might lose track of where it is by virtue of its motion uncertainty.
You accommodate this in localization by using an existing map,
but now we don't have an existing map. We're building a map.
That's where SLAM comes into play.
SLAM doesn't stand for "slamming" a robot.
What it really means is "simultaneous localization and mapping."
This is a big, big, big research field.
Most of my AI book is about this technology,
and today I want to show you my favorite method called "graph SLAM,"
which is also by far the easiest method to understand.
We will reduce the mapping problem to a couple of very intuitive
additions into a big matrix and a vector, and that's it.

14 - Is Localization Necessary
==============================
Here is a quick quiz.
When mapping an environment with a mobile robot, uncertainty in robot motion
forces us to also perform localization.
I'm going to give you two possible answers--yes and no.

15 - Is Localization Necessary Solution
=======================================
The answer is yes.
In nearly all cases of mapping, we have robot uncertainty in motion.
That uncertainty might grow over time.
We need to address this; otherwise the map looks really bad.
Let me give an example .
Suppose a robot drives down a corridor, and it senses surrounding walls.
If this robot has a drift problem and because of uncertainty it its motion,
it actually believes it drives a trajectory like this.
Then the surrounding map would look very much like that.
Now, these might be indistinguishable at first glance,
but if this robot ever comes back to the same place,
then it has an opportunity to correct all this.
A good SLAM technique is able to understand not just the fact that the environment
is uncertain but also the robot itself runs on an uncertain trajectory.
That makes it hard.

16 - Graph SLAM
===============
Let me tell you about my favorite method of all, called "Graph SLAM."
This is one of many methods for SLAM, and it's the one that is by far the easiest to explain.
Let's assume we have a robot,
and let's call arbitrarily the initial location x equals zero and y equals zero.
For this example, we just assume the road has a perfect compass,
and we don't care about heading direction just to keep things simple.
Let's assume the robot moves to the right in x-direction by 10, so it's now over here.
In a perfect world, we would know that x1, the location after motion,
is the same as x0+10 and y1 is the same as y0.
But we learned from our various robotic Kalman filter lessons and others
that the location is actually uncertain.
Rather than assuming in our (x, y) coordinate system the robot moved to the right by 10 exactly,
we know that the actual location is a Gaussian centered around (10, 0),
but it's possible the robot is somewhere else.
Remember we worked out the math for this Gaussian?
Here's how it looks just for the x variable.
Rather than setting x1 to x0 plus 10, we try to express the Gaussian
that peaks when these two things are the same.
If we subtract from x1 x0 and 10,
put this into a squared format and turn this into a Gaussian,
we get a probability distribution that relates x1 and x0.
We can do the same for y.
Since there is no change in y, according to our motion,
all we ask is that y1 and y0 are as close together as possible.
The product of these two Gaussians is now our constraint.
We wish to maximize the likelihood of the position x1 given the position x0 is (0, 0).
What Graph SLAM does is defining our probabilities using a sequence of such constraints.
Say we have a robot that moves in some space,
and each location is now characterized by a vector x0
and a vector x1, vector x2, vector x3. Often they are 3-dimensional vectors.
What Graph SLAM collects is initial location, which is a (0, 0, 0) initially--
although here it looks a little bit different--
then, really importantly, lots of relative constraints
that relate each robot pose to the previous robot pose.
We call them relative motion constraints.
You can think of those as rubber bands.
In expectation, this rubber band will be exactly the motion the robot sensed or commanded,
but in reality, it might have to bend it a little bit to make the map more consistent.
Speaking about maps, let's use landmarks as an example.
Suppose there is a landmark out here, and the landmark is being seen
from the robot with some relative measurement--z0, z1.
Perhaps I didn't see it it during time 2, but this is z3.
All these are also relative constraints
very much like the ones before.
Again, they are captured by Gaussians, and we get relative measurement contraints.
One such constraint is every time the robot sees a landmark.
Graph SLAM collects thosee constraints, and as we'll see,
they're insanely easy to collect, and it just relaxes the set of rubber bands
to find the most likely configuration of robot path along with the location of landmarks.
That is the mapping process.
Let me ask you a quick quiz that'll take thinking.
Suppose we have six robot poses--that is, one initial and five motions.
We have eight measurements of landmarks that we've seen.
These might be multiple landmarks. Sometimes the robot saw more than one.
The question now is how many total constraints do we have if we count each
of these constraints as exactly one constraint.

17 - Graph SLAM Solution
========================
The answer is 14.
There is 1 initial location constraint, 5 motions, which adds up to 6,
and 8 landmarks constraints.
That's the gist of what we're going to implement.
The key insight now is that this is insanely simple to do.

18 - Implementing Constraints
=============================
What we do is we make a matrix and also a vector.
We label the matrix, which is quadratic, with all the poses and all the landmarks.
Here we assume the landmarks are distinguishable.
Every time we make an observation, say between two poses,
they become little additions, locally,
in the 4 elements in the matrix defined over those poses.
For example, if the robot moves from x0 to x1,
and we therefore believe x1 should be the same as x0, say, plus 5,
the way we enter this into the matrix is in two ways.
First, 1 x0 and -1 x1--add it together should be -5.
So we look at the equation here--x0 minus x1 equals -5.
These are added into the matrix that starts with 0 everywhere,
and it's a constraint that relates x0 and x1 by -5. It's that simple.
Secondly, we do the same with x1 as positive, so we add 1 over here.
For that, x1 minus x0 equals +5, so you put 5 over here and a -1 over here.
Put differently, the motion constraint that relates x0 to x1 by the motion of 5
has modified incrementally by adding values the matrix for L elements
that fall between x0 and x1.
We basically wrote that constraint twice.
In both cases, we made sure the diagonal element was positive,
and then we wrote the correspondant off-diagonal element as a negative value,
and we added the corresponding value on the right side.
Let me ask you a question.
Suppose we know we go from x1 to x2 and whereas the motion over here
was +5, say, now it's -4, so we're moving back in the opposite direction.
What would be the new values for the matrix over here?
I'll give you a hint.
They only affect values that occur in the region between x1 and x2 and over here.
Remember, these are additive.

19 - Implementing Constraints Solution
======================================
Here is the answer.
Let me just re-transform this as is done over here--
x1 minus x2 is now +4, and x2 minus x1 is -4.
I have to add +1 over here, -1 over there,
+1 in this diagonal element over here, and -1 over here.
Let me just do this.
These numbers added in transform the first number over here to 2.
We get a -1 for the off-diagonal elements, and then 1 over here.
Now we add 4 to the 5, which gives us a 9, and a -4 to the 0 gives -4.
This is where we are now.

20 - Adding Landmarks
=====================
Let me do another quiz.
Suppose that at x1 we see landmark L0 at a distance of 9.
This gives me a relative constraint between x1, right over here,
and landmark 0, which is over here.
Just like before, these link two things together relatively--the x1's and the L0.
Now this doesn't look like a submatrix, but it is. It's spread a little bit apart.
But I want you to modify those 4 values in the matrix and those 2 values in the vector
to accommodate that we believe that the occasion
of L0 is 9 greater than the robot position x1.

21 - Adding Landmarks Solution
==============================
Here is the answer.
Obviously x1 minus L0 is -9, because L0 minus x1 is a measurement of +9.
Let's add this in. We add 1 over here on the main diagonal--1 and 1.
We subtract 1 off the main diagonal just like before--a simple pattern.
Then a 9 over here goes back to 0 but to 9 over here.
I hope this makes perfect sense to you.

22 - SLAM Quiz
==============
Let's summarize what we've learned in the form of a little quiz on Graph SLAM.
Check this box if Graph SLAM seem to be all about local constraints.
They require multiplications--if that's true check the box over here.
The require additions--check this box if this is correct or none of the above.

23 - SLAM Quiz Solution
=======================
The answer is obviously they are all about local constraints.
That's the entire point.
Every motions ties together two locations,
and every measurement ties together one location with a landmark.
Multiplication is just the wrong thing here, so they're all about additions.
These are the correct things to check.

24 - Matrix Modification
========================
I want to add one last thing here--the initial robot location.
If we define x0 to be 0, which is the origin of the map,
then what this means is we add 1 over here and 0 over here.
The reason why is this constraint is that x0 is 0.
Let's take a robot moving around and let's say it sees a landmark
from the first pose x0 and from the third pose x2 but not from the second pose.
I want you, in this matrix over here,
to check mark all the fields that are being modified by Graph SLAM--
it's a binary check--and the same for the vector without putting actual numbers in.
So go into this matrix and ask yourself which fields will be 0, the ones untouched,
and which ones will not be 0 that are the ones we modified.

25 - Matrix Modification Solution
=================================
The answer is our initial constraint would touch this guy over here.
The one to second motion touches these things over here.
The second to third, these guys, and then the landmark observation over here
puts something between x0 and the landmark
that sits here, here, here, here again, and here.
This observation over here puts something between x2 and the landmark--
these guys over here and the guys over here.
That means we have only the following places that are still 0.
This means there is no direct constraint between x2 and x0.
That is, there is no direct motion information between these guys,
and there is no direct constraint between x1 and L, which is this guy is missing over here.

26 - Untouched Fields
=====================
Let me do the same quiz again.
Now we have two landmarks,
and the picture I'm giving you is a robot with three total positions.
There's a landmark here and a landmark here,
and say this landmark is being seen in these two positions,
and this landmark these two poses, but landmark L1 is not seen at x2,
and landmark L2 is not seen at x0.
Of the 30 fields over here how many of them will never be touched?
Please put your answer over here.

27 - Untouched Fields Solution
==============================
The correct answer is 6 for the following missing links:
this guy here gives me two values in the matrix.
This guy here another two.
And this link here is also missing. That's another two. So 6 values are missing.
Let's prove it to ourselves. Moving from x0 to x1 fills up this area.
From x1 to x2, this area.
Seeing landmark L0 from x0 and x1 means we fill these guys over here.
and the main diagonal there.
Seeing the other landmark from x1 and x2 means we fill these guys over here.
Let's count the ones that are still open, and here are the ones.
My answer was actually wrong. It's 8.
I overlooked there is no direct link from L1 to L2 either.
My apologies that I gave you the wrong number,
but it proves to you this is actually not an easy question. It's harder than I thought.
The reason is there is also no direct link that constrains L1 and L2 directly.
Landmarks can't see, so they can't put a direct link between any two landmarks.
Or put differently, in this part over here our matrix will always be a diagonal matrix.

28 - Omega and Xi
=================
The last thing I want to tell you before we go into programming
is why this makes any sense.
Suppose you fill the matrix, which I call omega [Ω],
and the vector, which I give the Greek name of xi [ξ].
My apologies to my non-Greek students here.
You Greek students should be very proud.
You'll always have a special place in my mathematical heart.
Then I can find the best solution for all the landmark positions or the world positions
by a very simple mathematical trick that is completely counterintuitive.
I invert the omega, I right multiply with xi, and out comes a vector mu [µ],
which gives me the best estimates for all the robot locations and the landmark locations.
Now, that is quite amazing, because all it means in Graph SLAM is
that you keep adding numbers to these matrices every time you see a constraint.
When you're done with it, you run a very simple procedure
and out comes the best places for your robot.
Let's go and try it. I'm now going to ask you to program this.
I'm giving you my matrix class, so you can do this easily.
What I'm asking you to do is to build a 3 x 3 matrix and, of course, a 3 x 1 vector
about which you shall state that our initial location is -3.
X1 in exportation is obtained by adding 5 to x0 and x2 is obtained by adding 3 to x1.
In exportation what we should get out when we run
the mu equals omega minus 1 times xi trick is that x0 becomes -3,
x1 becomes 2, and x2 becomes 5.
Diving straight into our programming environment,
I'm giving you a matrix class--you might want to take a moment to look over it.
It's a little bit augmented to what I've given you before,
and I fixed a bug with the inversion code, which is quite essential.
If I run it, I construct an omega matrix piece-by-piece--
that's the one that you should come out with--
a xi vector, and then I run and print out, using the "show" command,
the result of omega to the -1 times c.
You can see -3, 2, and 5 are the correct results
that result from the omega matrix and the xi vector.
What I want you to do is write code that incrementally step-by-step constructs
the omega vector and the xi function and then returns to me those results over here.
There is an empty function in your code that accepts as parameter
the initial position, -3, and the two motion values, 5 and 3.

29 - Omega and Xi Solution
==========================
Here is my result.
I construct an omega matrix of size 3 x 3, and initially I set the top left corner to 1.
Then the vector xi, I set very first value to init. Everything else is 0.
Now come the important additions for the first move and the second move.
Both times I do exactly what I told you before.
For the two involved variables, I add a +1 on the main diagonal and a -1 off-diagonal.
Same over here.
Then I subtract move and add it 1 row later, and the same with move2 and move2 over here.
Look very carefully. This is exactly what I told you about.
I'm going to draw this graphically.
I begin with a matrix like this. I then add this guy and then this guy.
As far as the vector is concerned, I start with this, add this guy, and finally this guy.
Then these two together are being combined down here
where I compute the inverse of omega multiplied with xi.
That gives me the vector of res, and res is being output using those "show" command
and returned from the procedure.

30 - Landmark Position
======================
Now let's add the landmark.
Let's say the landmark is being seen at all time steps.
Let's say in the very first time the difference between position and landmark is 10.
Obviously this is a 1-dimensional example
and not 2-dimensional as the picture suggests over here.
Then it's 5, and then it's 2.
Now, what's the landmark position?
You can work this out in your head. It's a single number.
Please enter it here.

31 - Landmark Position Solution
===============================
The answer is 7.
Obviously, -3 plus 10 is 7,
-3 plus 5 plus 5 is 7,
-3 plus 5 plus 3 plus 2 is 7.
All of those work out to be 7. We have a fully consistent situation.
The landmark seems to be consistently seen. There seems to be no noise whatsoever.

32 - Expand
===========
Now I want you to extend your routine to accommodate the landmark
Specifically, I want you to use a function that I coded for you that is very useful
that is called "expand."
You can run omega.expand, xi.expand to take a 3 x 3 matrix or vector
and move it to a 4 x 4 vector that you actually need when you have to include
the landmark itself.
Give that a try and see if you can modify the code
to now have additional input parameters of measurement 0, 1, and 2.
In particular, here is our new doit routine.
It now has as input parameters my 2 motion commands
and the 3 measurement commands for the 3 different poses.
Here is the code that you produced before.
That's my version of it where we have the initial 3 x 3 matrix.
Then using the expansion command
you can now increase those to a 4 x 4 matrix and a 4 x 1 vector.
When you run it what comes out is this result over here-- -3, 2, 5, 7.
I want you to do this where -3 and 2 and 5 is the robot path,
and 7, as before, is the landmark location.
Please code this and realize that I can modify the input to doit just fine,
and your code should not just produce this one vector,
but it should implement the right math.

33 - Expand Solution
====================
Here is my answer. Here is the expand command.
It takes the omega vector and turns it in to a 4 x 4
and assigns the existing coordinate to 0, 1, and 2
and expands to make xi vector of 4 x 1
where it uses the previous dimensions of 0, 1, 2, and 0.
That turns out to make a larger matrix and larger vector.
Now, I go and add in the measurement constraints.
In all of those, I have to relate to the last coordinate,
which is my measurement coordinate from the first, the second, and the third pose.
And I have to subtract -z0, 1, and 2 from the corresponding robot poses
and add them all up back to the last pose.
If you implement this correctly, then you get a omega and xi
that, once you implement this solution equation, gets you this solution over here.

34 - Introducing Noise
======================
Here is a really tricky quiz. Let's look at the robot motion again.
Say I change the last measurement from 2 down to 1.
You might remember the robot poses were -3, 2, and 5.
Before that modification the landmark position was 7, but a 1 doesn't really add up.
A 1 suggests I might be at a different distance to the 7 than the 5 over here
that comes from this side.
Here is my quiz.
First, I want you to know if I make this modification what is the effect on x2?
Will the estimate be smaller than 5?
That is, we shrink the robot path a little bit?
Will it be exactly equal to 5 like before?
Or will it be larger than 5? Check exactly 1 of the three boxes.
I also want to know what is the effect on x0.
Will it be smaller than -3, equals -3, or larger than -3.
This is a completely nontrivial quiz.
It takes really some thinking.
Invest in thinking, and you can even go back and try it out.

35 - Introducing Noise Solution
===============================
I'm trying it out and see what happens.
Before it was a -3, 2, 5, 7, and now the first position is completely unchanged.
I'll explain to you in a second why.
The third one went from 5 to 5.5, and the landmark went down from 7 to 6.8.
Graphically, this guy becomes larger than 5, and this landmark even shifts a little bit
to the left to make these two things closer together than they were before
when they had a separation distance of 2.
Now this picture doesn't really explain it well, because it's a 2D picture,
but in 1D that's exactly what's happening.
Also interesting is the initial position is unchanged.
These are the correct answers.
Now, I would be blown away if you guessed them correctly.
The reason why the initial position doesn't change is the only information we have
about the absolute coordinate location is the very first initial position anchor
that we said was to be -3.
None of the relative rubber bands change the fact that we need this guy to be -3.
A relative change between these 2 things over here
means the rubber band is different, but it's a relative thing.
This is the only absolute constraint we put in.
Clearly the absolute location of the first position doesn't change.
The reason why becomes larger than 5 is--well, think about rubber bands.
Our landmark is around 7. We believe to be at position 5 in the noise-free case.
We just put a tighter rubber band between them. It's not 2 anymore; it's now 1.
That means we are inclined to move the landmark and this position closer together.
That's exactly what happens.
If you go to this solution over here, the final position becomes 5.5. It's now 5.5.
The landmark becomes 6.875 instead of 7.
Now, this is the case where the rubber bands don't add up.
This is one of the places where Graph Slam is just magical.
Before everything added up, but we have cycles in these structures.
These cycles might not added up, because we have noise and motion,
noise and measurements
What our method does by computing this thing--omega to -1 times xi--
we find the best solution to the relaxation of those rubber bands.
That, to me, is sheer magic.

36 - Confident Measurements
===========================
I'm going to give you a glimpse as to why it works.
Suppose we have two robot positions, x0 and x1, and we know they're 10 apart
with some Gaussian noise, and we know the Gaussian noise in exportation
moves the right robot position 10 off the left robot position, but there is some uncertainty.
When we talked about Kalman filters, we talked about Gaussians,
and this uncertainty might look at follows:
There is a constant exponential, and the expression that x1 minus x0
should relax to 10 but might deviate from it.
This Gaussian constraint over here characterizes the constraint between x1 and x0
and wishes them to be exactly 10 apart.
The Gaussian is maximum where this equation is fulfilled,
but if the residual is not equal to 0, there is still a probability associated with it.
Let's now model a second motion. Say x2 is 5 apart.
We now get an even bigger Gaussian relative to the very first one,
but the local constraint over here reads just like the constraint over there.
Let me just write it down.
X2 minus x1 minus 5 squared over sigma-squared.
Now, the total probability of this entire thing over here is the product of these two things.
If we want to maximize the product, we can play a number of interesting tricks.
First, the constant has no bearing on the maximum, just on the absolute value.
If we want to find the best values for x0 and x1 and so on, we can drop the constant.
Secondly, we can drop the exponential
if we're willing to turn the product into an addition.
Remember, we added things in omega and in sigma. That's why.
Finally, we can actually drop the -1/2.
It turns out that also plays no role in the maximization of this expression.
It turns out what you added where constraints just like these,
and you even added them at a certain strength of 1 over sigma-squared.
In particular, if you really believe that a constraint is true,
you should add a larger value in this matrix over here,
and on the right side you should multiply the right constraint with an even larger value.
Put differently, take an expression like this and multiply in the sigma-squared
you get something of this nature over here where 1 over sigma
regulates how confident you are.
For a small sigma, 1 over sigma becomes large.
So 5 is much larger than 1.
That means you have much more confidence.
Let's go back to the code and modify the code
so the last measurement has a really high confidence.
I want you to multiply the last measurement between x2 and our landmark
with a factor of 5 in your code. Hard code it.
That is, go in somewhere over here where the last measurement is being applied
and do the trick that I just showed you and see what the outcome is.
When I do this, I get -3, 2.1, 5.714, and 6.821 as the answers.
You'll see in this final result
the final robot position of 5.714 and the landmark position of 8.821
are really close to 1 in difference, which was the measurement,
because you know believe this measurement
over-proportionally over other measurements and motions.

37 - Confident Measurements Solution
====================================
Here is my answer.
In the omega, I replace all the 1's by 5's so we add 5, -5, -5, and 5 over here.
I also multiplied the measurement by 5. If you forget this, you get a very kooky answer.
You have to adjust these things over here in the same proportion
as the guys over here with a 5.
That gives you the result that I stated.

38 - Implementing SLAM
======================
So now we've learned all about Linear GraphSLAM,
and that's quite a bit--and it's really simple.
Every time there's a constraint--
Initial Position, Motion or Measurement--
we take this constraint and add something to Omega, Xi.
And what we add is the constraint itself,
but it's up multiplied by a strength factor.
There's nothing else but 1 over sigma--
the uncertainty in Motion or in Measurements.
And then when we're done with this adding--
we simply calculate this guy
and out comes our best possible PATH--
and along with the MAP of all the landmarks.
Isn't that something? Isn't that really cool?
So let's dive in and have you program your own real robot example.
This is a fairly complicated generalization of what we just saw.
I'm giving you an environment where you can specify
the number of landmarks that exist,
the number of time steps you want the robot to run,
the world_size, the measurement_range--that is
the range at which a robot might be able to see a landmark--
if it's further away than this--it just won't see it;
a motion_noise, a measurement_noise,
and a distance parameter.
The distance specifies how fast a robot moves in each step.
And then I'm giving you a routine which makes the data.
It takes all these parameters and it outputs a data field
that contains a sequence of motions and a sequence of measurements.
The code comments on the exact format of what data looks like.
Now I want you to program the function, SLAM,
that inputs the data and various important parameters
and it outputs my result--a sequence of estimated poses,
the robot PATH, and estimated landmark positions.
This is really challenging to program.
It's based on the math I just gave you.
The robot coordinates are now x and y coordinates.
The measurements are differences in x and y--
so you have to duplicate things for x and things for y.
I, myself, put them all into one big matrix,
but you could have them in 2 separate matrices, if you so wish.
You have to apply everything we learned so far,
including the weights of one with our measurerment_noise
and one with our motion_noise.
These happen to be equivalent, in this case--but they might be different.
And then you have to run SLAM
and return back to me a result data structure.
I'm also supplying you with the print_result routine
so you can go in and see how the result has to look like.
There's an example routine--that doesn't work--
that outputs all the correct formats,
but it tries not to implement the estimate that I want you to estimate.
You have to bring this to life
and turn this into an amazing SLAM routine
so that when you run it, you get the same results that I do
for the examples here,
where there's an estimated PATH
and estimated landmark positions.
There's one last thing I wanted to know--
is I assume the initial robot position
is going to be in the center of the world.
So it's the real-world set of 100
and it's going to be 50/50--or here it's printed as 49.999,
but this is the same as 50.
So you have to put in a constraint
that sets the initial robot pose
to the center of the world.

39 - Implementing SLAM Solution
===============================
So here is my solution: I've takan all the input parameters,
and the very first thing is I've set the dimension of the matrix and the vector:
the length of the Path, plus the number of Landmarks--
times 2--because I'm modeling x and y
for each of those, in the same data structures.
I then create a matrix for Omega and a vector for Xi,
give it the appropriate dimensions,
and subsequently I introduce the constraint
that the initial positions have to be world-size/2.0,
with a strength value of 1.0,
That tells it this has no bearing on the final solutions
because it's the only absolute constraint.
But you can see--I add 1.0 over here in the main diagonal:
1 for x and 1 for y--
and then now add the same thing over here.
It's important to understand how I set up the data structure.
There's our positions--and let me just, for a second, call them "S".
And there's our landmarks.
Each of those have an x-component and a y-component.
So in doing this, I'm taking this matrix and I'm setting it up,
not by a matrix of Path length plus the number of landmarks,
but each of those becomes a 2 by 2 matrix,
where I explicitly retain the x and the y value.
So the dimension here is 2 times N--the Path length--
plus the number of landmarks.
And the 2 is the result of modeling x and y: xy, xy, xy.
That's really important for my solution.
You might have done this differently--you might have said:
I'm going to build 1 matrix for x and 1 matrix for y.
and then each of those becomes just a single value,
which is closer to the way we discussed it in class.
And that's fine, in this case.
In general, it has disadvantages
in that it cannot correlate X and Ys.
So for a real robot that has real rotations, this doesn't work.
My solution is better, but for this specific example
this would have been perfectly fine.
Coming back to my example, I now process the data.
I go through all the data items
and my Path index is now the data item, times 2--
which is the xy thing.
I extract my measurements from the data--
my motion from the data--
using this command over here;
and then I go through all the measurements,
of which they are my multiple ones.
I find the index in my matrix of the measurement,
which is the Path plus the measurement index,
times 2--because there are X and Ys again.
And then the next routine just implements
the simple addition with the measurement_noise
as the inverse weighting factor.
So it adds: 1, 1, -1, -1
to the corresponding elements in the submatrix,
and in the vector, it adds the measurement--
all divided by the strength of the noise variable.
If you look at this carefully,
you'll take a minute to digest it
and what was the use in the auxilliary variable, b,
to account for the effect of this x and y.
So b goes from zero to 1.
And these are all the combinations.
You have to stare at them to make sure they are all correct,
but I can promise you--they're actually all correct.
Motion is handled very much the same way:
I extract the Motion command,
I add among, the main diagonal--
between the 2 variables that are being tied together--a "+1",
and then I add, in the off-diagonal elements,"-1".
So again, you have to stare at this
very carefully to see they're all correct.
And then I add the Motion itself to the vector, Xi.
That's what I had to implement.
I then solve, as before, and return the solution.
And that's exactly what's being printed out down here.
I have to say, we got this correct--I'm mightily impressed.
You understood a lot about Mapping
and you solved a really hard programming problem.
I'm responding to some of you online
who asked for challenging programming problems.
This is a challenging piece of code to write.
It took myself a number of hours to write,
and that would be wonderful if you got it right.

40 - Congratulations
====================
So congratulations.
I'm impressed you made it so far.
You really learned a lot about SLAM.
You learned about the MAP, which is a sequence of coordinates,
and you learned about Localization--
and "L" and "M" are really important letters here.
The Simultaneous and the And are not that essential.
We put all of those into a big Matrix, Omega, and a vector, Xi.
And every time, we got some relative information between poses.
We carved out some stuff in here
or we measured something.
We added some stuff in here, and over here.
These were all just additions
and, as we now understand,
those implement the straightforward constraints
that come from the motion--the measurements.
And then the key thing was that you could solve,
with a simple piece of equation,
for the Path and the Map at the same time.
That was quite an amazing achievement.
So you've implemented this,
you've implemented your first SLAM algorithm.
That was way beyond anything I ever taught
students at Stanford in a single class.
Congratulations for doing this.
So this is the last, and final, class.
I'm going to output a challenge to everybody, briefly,
where you can write a Robot program
that puts most of the stuff we talked about together.
But, for now, congratulations for making it so far.
That is really impressive.

