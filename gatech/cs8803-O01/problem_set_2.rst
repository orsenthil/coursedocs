1 - Measurement Update
======================
[Homework Assignment #2] This is homework assignment #2 in CS 373,
and it's all about Kalman filters. [Kalman Filters]
[Measurement Update] So question #1 is measurement update.
Let's start with 2 Gaussians and say they have identical variances. Let's multiple them.
We know that the resulting Gaussian's mean will be just at the center between those 2 Gaussians.
I wonder if the variance Σ² is now smaller, larger, or the same as either of the individual Gaussian.
Please check one of the three.

2 - Measurement Update Solution
===============================
And the correct answer is smaller. We are more certain afterwards.
You get a more peaky Gaussian whose standard deviation is smaller.
This is the correct answer.

3 - New Variance
================
Say we have a prior of a Gaussian with a mean mu and covariance sigma squared,
and our measurement has exactly the same mean and same covariance.
Suppose we multiply both and get a new mean, which is the same as the old mean,
and we get a new covarience, sigma squared,
which as you all know, corresponds to a more peaked Gaussian.
I want you to express nu squared as a multiple of sigma squared.
Just put the answer here as a real number.

4 - New Variance Solution
=========================
The answer is a ½ or 0.5
To see, let us multiply these two gaussians over here--
which the exponent becomes an addition--
we can now rewrite this as follows--
when we bring the factor 2, for these two terms in to the numerator
as our 2 sigma square,
and from that we see that the new variance is 0.5
as large as the old one when applied to the squares.
So, as a result, you would have this equation over here.

5 - Heavytail Gaussian
======================
I have another Gaussian question for you--
this is called a heavytail Gaussian.
So, as you go to +/- infinity,
the Gaussian levels off at some finite value alpha,
as opposed to zero.
My question is--
"Is it possible to represent this function as a Gaussian?"
This is the formula for the Gaussian again.
Particularly, can you find a Mu and a sigma square
for which this exact function over here is obtained?
Please just check one of these two boxes.

6 - Heavytail Gaussian Solution
===============================
The correct answer here is no.
Suppose we let "x" go to infinity,
then x-Mu2 for any fixed Mu would go to infinity.
So if x with a -infinity would go to zero--
because it is a constant--
Therefore, we know that in the limit of x goes to infinity--
this expression must be zero.
However, in this graph--it stays at alpha, and doesn't go to zero--
So, therefore, there can't be a valid Mu at sigma square.
If a deep improbability, you know that the area in the Gaussian
has to integrate into one,
and this area diverges, it is actually infinite in size,
so it's not even a valid execution.

7 - How Many Dimensions
========================
My next question pertains to the tracking problem that we talked about in class.
In class we addressed a 1-dimensional tracking problem where we estimated the location of the system and its velocity.
I'd like now to generalize this to a 2-dimensional problem.
We'll be given coordinants x and y,
and the object we're tracking moves in 2-dimensional space,
and we wish to use a Kalman filter to understand where the object is, what its velocity is,
and even be able to predict a future location based on the estimate of the position and its velocity.
So the only difference, class, is that our object now moves in a 2-dimensional space,
where as in class, it moved in a 1-dimensional space.
So my first question is what's the dimension of the state vector in the Kalman filter? [Dimension of the state vector?]
In the class, it was this kind of state vector. Now, we have a new one.
How many dimensions or how many variables are there?

8 - How Many Dimensions  Solution
=================================
And the answer is 4.
So rather than X and Ẋ, we have X and Y
and Ẋ and Ẏ as our state vectors.
And there's 4 variables

9 - State Transition Matrix
===========================
Now comes the tricky question. In the Kalman filter program that we studied,
the 2-D Kalman filter, we had a matrix F.
And for delta T equals 0.1, our F matrix, the state transition matrix,
had a main diagonal of 1, which means in exportation our location stays the same
and our velocity stays the same. And we also knew
that the velocity affected our state in the following way.
And you could now place 0.1 instead of the delta T
to get this specific F matrix.
Now I want to know from you for this new 2-D case with a 4-dimensional state vector
what is the new F? It is a 4 by 4 matrix, so I want you to fill in
all of those values. Again please assume that delta T is 0.1,
and don't write delta T, write 0.1.

10 - State Transition Matrix Solution
=====================================
And the answer is the main diagonal remains one.
This expresses the effect that in the absence of any velocity,
we expect the x-coordinate and the y-coordinate not to change.
We also don't expect the velocities to change.
But the x-velocity will impact the x-position through a 0.1 over here.
The third coordinate is the velocity, and it affects the first coordinate.
The same over here. All the other values should be zero.
So this is the 4-dimensionalization
of this 2-dimensional state-transition matrix over here.

11 - Programming Exercise
=========================
Let's now come to our programming exercise
I want you to program exactly what we just talked about.
We're given a two-dimensional world
where we observe in 2D measurements of a moving object
with an unknown but fixed velocity.
Using a state vector of this type, I'd like you to implement the Kalman filter.
Now, this Kalman filter now has 4 state variables
whereas the one we used before had 2 state variables.
I will give you the entire code for the Kalman filter,
but I want you to set up the state vector x, the motion u, P, F, H, R, and I,
which are all those variables that define the Kalman filter.
Start with the assignment that we had in 2D
and make it work in 4D.
Here is exactly the same matrix class that I wrote you before.
Here is the Kalman filter procedure.
We'll go through our measurements and apply the Kalman filter equations.
I should point out there's a slight difference to the code I gave you previously
where I insert a zeta transpose.
It makes it a little bit easier to work with multidimensional measurements than how I had it before.
But you don't have to pay attention to this. It's just fixed. There was a kind of a bug before.
As I scroll down, the output of the Kalman filter routine will be an x and a P.
In our example, the measurements will be a sequence of measurements
in two-dimensional spaces now--in x and y.
Look at the x's 5, 6, 7, 8, 9, and 10.
The y's go 10, 8, 6, 4, and 2.
You can imagine what the regularity is and what the velocity is.
We assume a dt of 0.1.
That means when it goes from 5 to 6 the velocity is actually 10, not 1.
We won't tell the system, but we will tell the system our initial x,y location, which is 4.
That goes nicely into 5, 6, 7, and it's 12. That blends nicely into 10, 8, and 6.
Our initial state vector I have already given you, which is the initial x and y.
and 0, 0 for the two unknown velocities.
The motion vector, just for completeness, will just be 0, 0, 0, 0.
We have no external motion.
That's a bit confusing, because there is actually motion in the system itself,
but this will be more like an external change of the motion
as if someone hit the object with an external force.
So it's 0, 0, 0, 0--please don't change it.
P is the initial uncertainty,
and I want you to initialize it so that the uncertainty for the x,y coordinates is zero,
but the covariance term for the velocities is 1000,
indicating that we really don't know the initial velocity.
We just know the initial position.
I want you to plug in the f matrix.
I want you to design an H matrix that's a projection matrix
from 4-dimensional state space to 2 dimensions,
reflecting the fact that we can only observe the first two state variables--x and y--
but not the velocities.
I want you to define the measurement uncertainty matrix, which now is a 2 x 2
that has 0.1 as the main diagonal as measurement noise.
This is an identity matrix over here.
Once you design all those, you should get the following output.
So when I run this, I get as an output
for my 4-dimensional example the x coordinates 10 and 0.
This makes sense given that these sequences over here
has a final measurement 10 and 0--5, 6, 7, 8, 9, 10--10, 8, 6, 4, 2, 0.
The interesting thing that I want your program to produce is the velocities.
They are approximately 10, which makes sense given out delta-t of 0.1
gives us per time step a 10 divided by 10 equals 1 increment over here.
The second velocity is -20 multiplied by 0.1 gives us a -2.
You can see it over here--10, 8, 6, 4, and 2.
I also want you to output the covariance matrix,
which has certain elements that are still 0, like these guys over here.
We find that along the main diagonal our uncertainty has shrunk substantially.
It's 0.03 for the coordinate estimates and 0.1 for the velocity estimates.
Remember, this number over here was 1000 before.
Here is a second example where we have an initial coordinate of -4 and 8.
We can see the measurements 1, 6, 11, 16.
It seems the increments are in x direction 5.
In the y direction they are -4--8, 4, 0, -4, -8.
If I now run this, I get for my x vector approximately 16--the number over here,
approximately -8--the number over here.
These are velocities--50 and -40 in approximation,
which multiplied with 0.1 is our plus 5 and our -4.
Here is yet another example. Initial state 1 and 19.
You can see the first coordinate doesn't change at all. You should get a velocity of 0.
The second coordinate goes 19, 17, 15, 13, and 11.
Running it gives us 1--unchanged--and 11.
Velocities are 0 and -20 for the decrements of -2.
Going into the covariance, we see values along the main diagonals--
0.05, 0.05, 0.33, and 0.33 for the velocities.
There are certain off-diagonal elements.
Make sure those all match what your code produces.
I can now change some of these measurements to make a noisy measurement.
One way to do this is to set an oscillating measurement between 2 and 0.
Remember that this Kalman filter assumes a fixed velocity.
There is no way to explain these measurements with a fixed velocity,
so there has to be measurement noise.
We can run the Kalman filter again.
Your filter should output the following values:
0.7 for the current state, 11 as before, and here are our two velocity estimates.
It actually believes there is a slight velocity of -0.66
in the x direction where we had noisy sensor input.
The covariance matrix would look exactly as before,
because it's not affected by the measurements themselves.
Your job is to fill in these various matrices. Good luck.

12 - Programming Exercise Solution
==================================
Here's my solution for the programming assignment.
There are many different ways to structure this, but that's what I've done.
I have a dt equals 0.1.
I set my initial state vector to be the initial x and y coordinates,
and for the two velocities I set them both to 0.
My u vector, as I said in the statement of the problem, is zero everywhere,
so just ignore it.
Interesting is my P matrix that measures the uncertainty.
I set the uncertainty initially for the locations to be zero.
These are the two main diagonal elements over here,
and the uncertainty for the velocity is to be really high--it's 1000.
So this is my initial uncertainty matrix.
That guarantees that I can really estimate the velocity based on data,
and I believe the initial state estimates are correct.
Our F matrix is a 4-dimensional generalization of the F matrix we had before
where we have 1 along the main diagonal.
This one says that the position is retained in expectation and the velocity is retained,
and we have two dt's over here.
The x dot, which is my third state vector influences
the x by a factor of dt for each time stamp.
The same is true for y dot.
These are the places where our velocities impact our position estimate.
As I scroll down, the H matrix is a 4 x 2 projection matrix
where we project out the x dimension and the y dimension without any velocities.
For the measurement uncertainty I assume
that each measurement has uncertainty covariance of 0.1,
and these are along the main diagonal of the 2 x 2 measurement noise uncertainty matrix.
This is obviously how a 4-dimensional identity matrix looks over here.
If I run this for my first example where the measurements are 5, 6, 7, 8, 9, and 10,
and the second dimension is 10, 8, 6, 4, and 2 and you can't see it but it's 0 over here.
In my output, I correctly get the estimate of 10 for my x and 0 for my y.
Velocity is 10 and -20.
As we had before, because dt equals 0.1,
a step from 5 to 6 within a 10th of a time unit
requires velocity of 10 and from 10 to 8 one of 20.
These numbers are correct.
But we want to look at the covariance matrix.
It's hard to read anything off it other than we are fairly certain as to what our location is,
and we have a fairly good estimate of what our velocities are.
Our covariance of velocity uncertainty is 0.1, and this is down from 1000,
which was the initial value in these uncertainties.
Going to the second example, I now commented away
the first example and put in place a second example.
If I run it again, here we see the first dimension go for -4, 1, 6, 11, 16.
The second dimension 8, 4, 0, -4, -8.
These are the exact same values over here--16 and -8.
For velocities I get 50 and -40, which are exactly the correct velocities.
Finally, for our third example, where the first coordinate doesn't change at all,
we get the correct 1 over here and velocity of 0.
Second coordinate goes from 19, 17 all the way to 11.
We get 11 over here and velocity of -20.
This is the implementation I wanted you to do.
If you implemented this thing over here, you got it right
and congratulations--you implemented a fairly nontrivial Kalman filter in stages,
but through this class, we now have code that allows you
to run Kalman filters on complicated problems,
and I hope you really got an understanding how the Kalman filter works.

13 - Congratulations
====================
So congratulations.
You just made it through the Kalman filter class and the second homework assignment.
You've implemented Kalman filters,
you learned a lot about Gaussians,
and you wrote your first vehicle tracking software. Congratulations.
That's actually really, really cool.
Next week, we'll talk about particle filters as yet another method for state estimation.
It is very interesting and very fascinating.
We're going to implement our first. See you next week in class.
