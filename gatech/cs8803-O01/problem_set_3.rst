1 - Empty Cell
==============
Welcome to homework assignment number 3.
This is all about particle filters. All ask you three questions.
Then we have a fairly involved programming assignment.
Here is my first question.
Consider the following world with 4 states--A, B, C, and D.
Suppose we wish to initialize our estimate with uniformly drawn particles.
My question is what is the probability that cell A is empty?
I'm asking this for different values of N--
N equals 1, 4, and 10.

2 - Empty Cell Solution
=======================
For N equals 1 it is 0.75 with 3/4 chance that particles will find themselves in B, D, or C,
and there's only a 1/4 chance that a particle is in A.
For N equals 4, it's 0.316, which is the same as 0.75^4.
For each particle we have a 75% chance to be outside A,
and 0.75^4 are the chances of 4 particles are outside A.
As we move on, we get 0.75^10 with a 0.0563.

3 - Motion Question
===================
Question 2--consider the same world as before with 4 states.
Now we're facing a situation in which there are 5 particles in A, 3 in B, 3 in C, and 1 in D.
We will now take a motion step. This is not about measurements, just motion.
Our robot moves with a 50% probability horizontally.
For example, if it was in D, it would move to C.
It moves with a 50% chance vertically but never diagonally,
and it never stays in the same cell.
After 1 motion step, how many particles do we expect in cell A, B, C, and D?
Answer the same for the asymptote.
If we move infinitely often, what is the distribution that we expect this to converge to?
I somewhat sloppily wrote "after infinite steps."
This is really what does it converge to in the end.

4 - Motion Question Solution
============================
The correct answer of the 1 step is 3, 3, 3, and 3.
For example, for cell A we can only get particles from B or C.
Those will come to A with a 50% chance each.
So 6 times 0.5 is 3 for A.
Each cell has exactly 6 particles in its total neighbors,
so therefore, each of those cells gets a 3.
Asymptotically, this won't change. It's again 3, 3, 3, and 3.
I apologize it is a little bit misleading here that all these answers are the same number,
but that's what this example gives us.

5 - Single Particle
===================
In question 3 I'd like to quiz your intuition.
Suppose we run a particle filter with N equals 1 particle.
What will happen?
It'll work just fine, perhaps with a slightly larger error.
It ignores robot measurements.
It ignores robot motion.
It likely fails.
Or none of the above.
You can check multiple boxes on the left.

6 - Single Particle Solution
============================
The correct answer are it ignores measurements and will likely fail.
It ignores measurements, because the measurement sets the weighting factor
in this resampling process, but with only 1 particle
the same particle will be resampled no matter what.
So the chances of the particle to be resampled is 1.
Therefore, it's independent of the actual measurement.
The robot truly ignores the measurements.
Because it ignores the measurements, it'll likely fail, so works fine is incorrect.
For ignoring robot motion--that's not the case.
Even a single particle can be sampled forward.
So these are the two correct answers over here.

7 - Circular Motion
===================
Here's our programming assignment.
In class you already programmed a particle filter for a really simplistic robot
that was able to measure ranges to landmarks and moved pretty much like a trashbin.
Now I'd like replace it with a more interesting robot that's more realistic.
In particular, I'd like you to use a car. Here's a car.
A car tends to have fixed tires and two steerable in the front.
Suppose the location of our car in a coordinate system
is given by its x-coordinate and its y-coordinate--
I'm picking the halfway point on the rear axle as the reference point--
and by its heading dire theta.
The state will be x, y, and the orientation theta.
Then this car also has a steering angle that is called the alpha.
The question is how is the state effected by driving a certain distance d
with a fixed steering angle, assuming the initial state is x, y, and theta.
It turns out to answer this, I also need to know the length of the vehicle,
which I will just call L for length that is a constant throughout out consideration.
This is usually called a bicycle model.
Obviously, it suffices to look at one pair of tires because the other one--
at least in approximation--runs pretty much parallel.
If we look at the robot locally where we have a steering angle, alpha,
robot length L, and we're driving the rear tire forward by distance D,
then the robot will turn to the left, and it's turning angle, beta, is proportional
to the distance that the rear tire moves forward divided by the length of the vehicle
times the tangent of the steering angle.
Let's now compute the changes of x, y, and theta in the local coordinate system.
Realize the turning radius R of this robot
is simply the distance that we drive forward divided by beta.
It's relatively simple math, which I don't want to explain in detail.
This means that the robot is turning around a point over here at cx and cy.
After the turn, the vehicle is located somewhere over here.
In global coordinates, here is the way we describe this.
Cx is the x coordinate of the robot x minus--now we go to the left--
the sine of the robot orientation before motion times radius R.
Similarly, cy is this expression over here--y plus cosine of the orientation times R.
Then after motion, we can go back from cx to cy to a new state over here
simply by adding in the turning radius beta.
That is, our new x is cx plus sine of theta plus beta times radius.
Notice how this parallels this guy over here, except for two changes.
What we previously subtracted we're now adding,
and we're adding beta to the argument of the sine.
The same with y, and the orientation is just increased by beta--modulo 2π.
This all works if the robot is actually turning.
If the robot were to go straight, then R would become infinity by this division over here.
For small betas--that's smaller than 0.001--we can approximate this all as straight motion.
Our new x is the old x times our driven distance pointed in the cosine of the heading direction.
Similarly for y we go in sine of heading direction, and the heading direction stays the same.
You could add beta, which is basically zero, to be slight more precise
or you could just use theta. It doesn't really matter.
In this programming assignment, I'd like you to implement this piece
of math over here in our particle filter.
To make sure we increment it correctly, I will give you some example data that you can check.
In our first part, I've prepared a lot of software for you,
basically copying the old particle filter software over,
and removing the motion and the measurement model for now.
In this I just want you to practice the motion model.
We assume a length of the road of 20.
We initialize the road with this length parameter,
and for this first iteration we assume no steering noise and no distance noise.
I set the robot to (0.0, 0.0, 0.0) in the beginning,
and then I cache away a number of motions,
The way to read those is this robot is moving by 10 total with the steering angle of zero.
Then it moves another 10 with a steering angle of pi divided by 6.
Then it moves 20, again with a steering angle of zero.
A pi over 6 is a left steering,
so the robot should change its coordinates in the beginning just in the x direction,
because it's facing an x direction over here.
Then turn left a little bit, go forward, and go straight again.
Scrolling down a little bit, I also give you the code to run the robot.
We've created the robot here. You print the initial coordinate.
Then for each of the motions in this list over here,
we apply the myrobot equals myrobot.move command,
and we print out the successive command.
If you get this right, these are the numbers I would like to see.
Initially, the robot position is 0, 0, 0, 0. That's just the one over here.
It's out first print command. It then moves forward in the x direction by 10.
The orientation stays 0 and so does y, because there's no steering.
Now we steer. This affects x. It doesn't quite move 10. It only moves 9.86.
In the y direction it only moves 1.433, and its new orientation is 0.2886.
Then we move straight again, and now the x coordinate becomes 0.3903,
y coordinate becomes 7.12, orientation 0.28.
Your code should output exactly the same values also over here.
Just to give you a second test--this is a sequence of 10 motions
where the robot moves 10 forward and always turns right but an angle of 0.2 in radians.
We look at the outputs we get the following array.
You can see that the orientation starting at zero, which is the same as 2π,
decreases all the way to 5.26,
and you can also see that the robot starts running in a circle
whereas initially we add almost 10 to the x direction and almost nothing in the y direction.
As you come down here, we subtract quite a bit in the y direction,
because now the robot is going in a circle.
You should look at these numbers over here and see if your code matches
these exact numbers that my code outputs.

8 - Circular Motion Solution
============================
Here's a function "move" as a class function of the class robot
that implements where I get my motion vector,
and the motion vector is defined to be steering first, then distance.
I have a few error checks here to make sure the steering doesn't exceed
the max steering angle, and the same is true for distance.
I want it to be non-negative.
As I go down, I now implement the motion model.
Let's just look a little bit more.
I make a new robot copy as in my sample code in class.
I copy all the narrowing parameters--length, bearing noise, steering noise, and distance noise.
Nothing surprising here.
Here I'll apply the noise, which you don't need it for the first implementation,
but later on as we go on, you need it to actually add noise.
I just add Gaussian noise with the corresponding steering noise and distance noise parameters.
If I set the mean of the Gaussian to be the steering command
and the distance command then this adds noise.
I could have equally written steering plus random.gauss,
zero, comma, and then the noise parameter.
As I go down further, here is my execution of motion.
My turning angle, I called "turn."
This is the tangents of the noisy steering
times the distance moved divided by the robot length.
As in my explanation of this question, I'm going to branch and see if my turn is significant enough.
It's smaller than tolerance, and tolerance was set about to 0.001.
Then I just model a straight motion.
I get my new robot coordinates by the old robot coordinates,
moving in the orientation of the robot--cosine for x and sine for y.
I increase my orientation by turn, which is likely essentially zero.
In case I go beyond 0 or 2π,
I do the modal operation here just to make sure my angles are nicely between 0 and 2π.
The more interesting case--as we go down
in this program you can see that I now calculate the radius
as the noise distance divided by turning.
Then I find the center of the circle around which I'm turning,
using the exact same math I just gave you.
I now first change the orientation to be the new orientation
by adding turn to the old orientation, modal, or 2π.
Then I plug the new orientation into the sine and cosine argument,
multiply by radius, add to the center of the circle to get my result.
This routine over here gives me exactly what I wanted.

9 - Sensing
===========
Now I want you to implement a measurement model,
using the function sense, that is more characteristic
of what's often in the literature on robotics.
Say we have a robot
and we have a landmark, then the robot can measure their bearing or angle
to this landmark relative to its own local coordinate system.
Whereas before we measured ranges or distances,
now we measure bearings or angles.
We assume in the world there are 4 landmarks--
L1, L2, L3, and L4. All of those are distinguishable.
The measurement vector is a set of 4 bearings
that correspond to those four different landmarks.
When you implement this, I recommend you use the function
arctan2, which is the generalization of arctangent
that takes as input delta y and then delta x.
Arctan 2 would give you the orientation of a vector in global coordinates.
We then have to adjust for the fact that it's relative to the robot's local coordinates,
which is done by subtracting the orientation of the robot.
This should give you the implementation of a bearing to a landmark.
With this implementation I add a variable called "bearing_noise,"
which you probably already used because it was already referenced before.
I set it to 0 just so that we have no noise, and you can just your code.
We initialize the robot coordinates as 30 and 20.
Motions are now irrelevant.
But as I go down, I now give the following two lines of code.
I print the coordinates as before, and I print the measurements.
The robot is at 30/20, and the bearings for these landmarks will be
6.00, 3.72, 1.92, and 0.85.
My question for you is can you implement the software the measures those bearings.
If I changed the initial orientation of the robot to be pi over 5,
I now get my new robot coordinates over here,
and my measurement vector outputs me very different values.
That's because this robot is now rotated
and therefore all the bearings to the landmarks do change.
It's 5.3, 3.1, 1.3, and 0.22.
Implement a measurement function that gives me exactly those values.

10 - Sensing Solution
=====================
Here's my implementation of sense, the measurement model,
as a function in the class robot.
I produce a vector called Z, which I return in the end, which has 4 bearings.
Then I go through all my landmarks, and you already have the landmarks in your code--
--there's 4 of them--and I use the atan2 function,
which is the mathematical function for computing the angle.
It takes the y value as the first argument, and the x value as the second argument.
This is the local angle of a landmark relative to the robot coordinate.
Because the robot has a global heading direction,
I need to subtract this to get my bearing value.
If I were to add noise, which is a flag over here,
then I just produce a random noise adding variable.
This is something you shouldn't have implemented,
but you need later as you implement the noise.
Of course, I make sure that the bearing is normalized between 0 and 2π.
I append them to the list and return it.

11 - Final Quiz
===============
Now, in our final programming exercise,
I want you to put everything together and build a particle filter.
I'm supplying you with code that has as gaps
pretty much the 2 functions you just programmed--move and sense,
and some additional code that I copied from class--
the particle filter code that you're familiar with and also code
that helps you test your routines so you can make sure they're correct.
The key new thing you have to do is you have to work on the noise.
There is now bearing noise and steering noise and distance noise.
The code that you wrote didn't have any of those.
I want you now to modify your procedures to accommodate this noise--
steering noise, distance noise, and bearing noise--
and all of it should be Gaussian.
Let's go all the way to the end. There are two test cases.
The first test case, which are uncommented so we can run it.
What this is is it creates a sequence of robot motions.
At each of these time steps the robot turns a little bit and moves forward.
It also has 8 measurements, which are the bearings to the those 4 different landmarks.
If I go up a little bit in the code,
then you'll find that the ground true final position was 93, 75, and 5.2.
When I run it, it runs the routine particle filter with those motions
and those measurements as an input.
It produces an estimate, which is 94, 71, and 5.2,
which isn't exactly the same as up here, but it's close.
This is a particle filter working.
I'm supplying quite a few functions for you. You should look around.
One is called particle filters.
That's exactly the same code we used in class and constructed together.
I just copied it over, so if you look through this you'll find, hopefully, no surprise here.
I'm also supplying you the measurement probability function, which is part of implementation.
Lets just go there.
Here is the measurement probability function. There is something non-trivial here.
I compute the predicted measurements,
and then I compute a Gaussian that measures the distance between
the measurements passed into the routine
and the predicted measurements computer over here.
That's all happening down here. Here's my Gaussian function with the exponential.
Then I return my Gaussian error. There should be no surprise here.
What's important is a little modification to the sense function that we haven't seen before.
I can now give the sense function a parameter, and I give it the parameter 0.
It switches off the noise model, so you will need the noise model
for forward simulation of the robot,
but you don't need it for computing the probability of the measurement.
It augments your sense function to have a flag
that if it's set to 0 it switches off the noise modeling
and gets you the predicted best possible measurements.
What you have to do is you have to find the part in the code
that says "only add/modify code below here."
You have to copy over your move function and then work in,
as it says in the instructions, the steering noise and the distance noise
and it's Gaussian--I hope you know how to do this.
Then you also have to plug in the sense function,
and you also have to plug in bearing noise and make sure there's
a flag that allows you to switch off the bearing noise.
It should be an optional flag,
so it has to have a default value of the bearing noise being on.
Otherwise your code won't run.
Here is how we will test your code.
If you go to test case number 2,
then I wrote a few extra functions for you that allow you to test your particle filters
on many, many instances just like the ones we were using
for testing that are all randomly generated.
Let me just go through that code line-by-line.
Our test case will be 8 steps long.
There is the same motions vector we had before of a slight turn on the circle.
"Generate<u>ground</u>truth" gives us a sequence of measurements and a robot position
that we can split as follows, using a robot simulation.
Then you run your particle filter over here, and the function
"check_output" down here compares the final robot position, the ground truth position,
with your particle filter position, estimated position, from here
and gives us a single flag whether this is all correct. Let me just do this.
We generate a robot that finished with final location 20, -29, and this orientation over here.
The particle filter came up with 22, -31, and 0.14, which is close to the original.
My code check said "True." Let me run it again.
Different values--still true. Run it again. Different values--still true.
Now, it could happen that the code check says "False."
I just ran it 20 times, and it said true for me every single time.
But I've seen it say "False."
The reason is it's a randomized algorithm. It's a particle filter.
It might actually not have a particle at the right place.
So when we test your routine, we're going to code our own code check, check_output.
We have our own function for this, but we're going to run it multiple times.
If you get it wrong once it's not a big deal.
In summary, you will have comment out all the test cases again.
All you have to do is supply the missing function. You can test the correctness yourself.
You can basically grade yourself with this test case over here,
but when you submit it, have those commented out,
because we have our own test software.
All we're going to test is whether your particle filter gives us a good estimate
when we choose randomly the initial position
of the robots, measurements, motions, and so on.

12 - Final Quiz Solution
========================
So to implement the full particle filter,
the only thing is really missing is the measurement_prob function.
And that's a little bit more involved because I have to
really compare what the exact measurement would be for any ove, overt particle.
And what I sensed and compute the probability correspondence between
the correct measurements, and what I sensed over here.
To do this, I calculate predicted measurements using the sense function.
Here comes a little flag that I defined.
If I set it to 0, than the sense function acts noise free.
Which is what I want, it could be the measurement model.
But even we you left this out, you're going to get a fine answer on my opinion.
But that makes it a little bit more accurate.
So that allows me to compute the exact bearings of the landmarks for
my particle.
And then I can compare these correct bearings called predicted measurements
with the ones that I received.
Now do this, down here, in the compute errors routine.
Where I go through each measurement and in two steps,
I calculated the error in bearing.
First, it's the absolute difference between my measurement that I observed,
minus the predicted measurement, and there's an i at the end over here.
Let's see if you can see this.
Right there.
And this difference might fall outside minus pi plus pi.
So this line over here just brings it back
to the smallest possible value in this cyclic space of 0 to 2 pi.
So adding pi, adding more load 2 times pi and I subtract pi again.
So this gives me a value between minus pi and plus pi.
I then pluck this error_bearing into a Gaussian.
And here is my Gaussian where I squared it,
I divide it by my bearing-noise squared, complete the exponential, and
use my normalizer to strictly speaking of, don't really need for
the implementation, I can safely omit it because weights are self-normalized.
But I left it in, so it's actually really a Gaussian.
And I take this Gaussian value and multiply it up into my error function.
So for each of the measurements, I multiply in one Gaussian.
And the final Gaussian is my importance whether I return in this
function over here.
So this is not easy to implement.
I hope you got it right.
Scrolling further down in my code,
I now implement the particle field as follows.
It uses a thousand particles.
And this is exactly the same routine we had before,
where we generate our initial particles.
Here, I set the noise for
these particles, to be bearing_noise, steering_noise and distance_noise.
I don't comment out the measurement generation step, I just take the input.
And then as I go further down, I just run my particle theta.
This is the exact same code you're familiar with.
There's a motion update,
there's a measurement update, and there's a resampling step over here.
All those are the same as before.
And at the very end I just print the result of get_position.
So if I do this for my example, here is the position I get.
And I guess for, I forgot to uncommon the Robot coordinate over here.
But if you look at the values over here, 7.0 is about the same as 8,
49 is about the same as 48, and 4.31 is about the same as 4.35.
So this particle filter,
clearly does a pretty job in estimating the forward position
