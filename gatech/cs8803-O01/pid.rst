1 - Robot Motion
================
Welcome to Unit 5. Today we talk about actual robot motion.
In the previous unit we talked about how to find paths .
Now we'll talk about how to turn these paths into actual motion commands.
In particular, we'll talk about generating smooth paths.
Then we'll talk about control.
In particular, a method called PID control.
As usual, you get a chance to program all these wonderful things.
You might be remember that our planning took place in a discrete world,
and the type of plans we found look very much like this,
perhaps in response to obstacles over here.
Now, a path like this has lots of disadvantages.
You don't want to a robot to go straight, take a 90-degree turn and go straight again.
For one, a car can't even do this, but for another this will force the robot to move
really slowly around the corner over here.
A much better path would look like this.
This is a smoother path.
In the extreme case, you might even generate a path just like this.
The question becomes can we modify the blue path to look more like the red or the green path?
Suppose your car like a robot right over here wished to get to right over here.
Which path would you prefer?
The blue path, the red one, or the green one?
Just check one of the three.
This is a question where I check your intuition. This is not a mathematically precise question.

2 - Robot Motion Solution
=========================
The answer is subtle. I would actually prefer the red path.
The reason is as the robot is facing the right side over here,
it can't take a 45-degree turn onto the green path.
It should slowly move around the corner, go down here, and slowly move to the right.
The greet path might be shorter, but it requires two 45-degree instantaeous turns,
which are unfeasible for the robot.
To some extent, we'd like to find a smooth path that is executable by the robot.

3 - Smoothing Algorithm
=======================
In the path planning class, we specified paths as a sequence of points in a 2D grid
just like this over here.
For the smoothing purposes, we will call each point xi.
This is a sequence that goes from x0 to xn-1,
and each of the x's is really a 2-dimensional coordinate, but that should be immaterial to the smoothing.
You could do this in 1D, 2D, or 3D.
Here's the smoothing algorithm. Initially we create variable yi that are the same
as all the xi's. Remember that these are the non-smooth locations that the planner has found.
Then we optimize two criteria.
The first is minimizing this expression over here, and the second looks as follows.
In the first one we minimize the error of the ith original point with the ith smooth point,
and the second we minimize the distance between consecutive smooth points, both to the square.
Here's a little quiz.
If we only apply the first criteria--forget about the second one--will we get the original path,
and smooth path, or no path. Please check exactly one of those boxes.

4 - Smoothing Algorithm Solution
================================
The answer is if we just optimize this one over here, we get the original path,
and the reason is obvious. It's already zero for the original setting.
Further minimization doesn't make it any smaller. It's a quadratic error.
The minimization has no effect. We just get the original path.

5 - Smoothing Algorithm 2
=========================
Now let me ask the exact same question just for the second criterion.
Forget about the first one.
What happens if you only optimize this criterion over here.
Do we get the original path, smooth path, or no path.

6 - Smoothing Algorithm 2 Solution
==================================
The answer here is you get no path.
This criterion alone asks that all the y's are as similar as possible.
If it's minimized, then all the y's are the same, which means you only get a single point,
and we get no path at all.

7 - Smoothing Algorithm 3
=========================
Obviously these two criteria are in conflict to each other.
In reality, what we do is minimize both, and you do that with some sort of a weight, alpha,
which you can play with in the code.
The stronger alpha, the smoother the path.
The smaller alpha, the more we retain the original points.
Here's my next question. Suppose we optimize both at the same time with an appropriate alpha?
What do we get? An original path, a smooth path, or no path?

8 - Smoothing Algorithm 3 Solution
==================================
The answer is we get a smooth path.
To see why that's the case, let me just simulate the optimization.
Suppose we're given a solution to the planning problem like this,
and you run the optimization algorithm. Consider a place like this.
By shifting this point into that direction,
and perhaps shifting the other points in other directions,
we can decrease the second error term,
both for this pair of points, and this pair of points.
However, we do this at the expense of the first error term,
since we're now shifting the point away from the original x.
Depending on the weight of these error terms, we might arrive with like the following.
This new path suffers an error of the first type that we moved the points away
from the original points, but it drastically reduces the inter-point distance
as in this error term over here.
If you insist that the original points are not changed,
then just exclude those from the optimization.
In fact, in our exercise, we will not consider those points
Y0 will always been the same as x0, and yn-1 will always be the same as xn-1,
assuming we have n points starting in x0.
The optimization is only applied to the intermediary points.

9 - Path Smoothing
==================
How can we optimize these two terms over here?
The idea is to use gradient descent.
That is, every time step we take a small step in the direction of minimizing the error over here.
Here's the expression for the first objective.
When we iterate, we assigned to yi recursively the old yi,
but we subtract a term that's proportional to the deviation of yi to xi,
weighted by a weight function alpha.
That's not exactly the same alpha as before.
We set this alpha over here to 0.5.
For the second term, we could implement this as follows
where we retain the old y variable, but we move a little bit in the direction of yi+1 and away from yi.
But an even better implementation looks as follows.
This is combining the step on the left and the step on the right.
Realizing that each yi occurs twice in this optimization term,
one here and one here, we can now go and implement this in a single update rule
where we wish yi to be as close to yi-1 and simultaneously be as close as yi+1
by optimizing this combined term.
Think about this as little bit, but that's what I want you to implement.
We're going to set beta to 0.1.
Now let's go and implement this.
As a last hint, I don't want you to apply this optimization for the first or the last node in the sequence.
I want those to be unchanged, as we'll see in a second.
Here's the code I'll be giving you.
There's a path in a 5 x 5 grid, starting at [0, 0] to [4, 4].
If you look very carefully, it goes to the right at first, then straight down, then to the right again.
This is exactly the path we discussed so far and looks like this graphically.
I now want you to implement the function "smooth," which takes as an input the path,
our two weighting factors, and a small tolerance variable,
which I'll explain to you in a second, and it creates the new path,
which are the y's in our equations so far from the old path.
This is a deep copy over here.
Then below the line, I want you to implement the smoother.
What the smoother does is iteratively applies the two equations I just gave you to all nodes
except for the first and the last,
and it does so until the total change observed in the update step becomes smaller than tolerance,
at which point we consider the smoother to have converged.
Here is my command. I compute a new path as a result of the function smooth.
In your test, you should uncomment the "newpath" smooth routine
and the print routine that outputs my result,
"Thank to EnTeer," a student who posted a much better way to output matrices on the discussion forum.
I'm going to use his or her code. Thank you so much.
Here's the result. After hitting "Run," I have the original path over here--zeros all the way to [4, 4].
The two initial and the end position, should be the same as before, so please don't modify them,
but in between we get these interpolation positions over here.
If you look at this, my original path didn't vary the x's at all for the first three steps
whereas this one goes from [0, 0] to 0.17, so it got closer. It went down a little bit.
Also, it went less to the right side than my original path.
We went all the way to 2 over here to 1.8 over here.
What this means is that our new points lie a little bit like this.
As you go through the list over here, you'll find that our new points really smooth out
the path to something more like that.
Hi, I'm Andy, the assistant instructor for this class,
and I just wanted to provide some clarification about
how you're going to use gradient descent to minimize these functions.
First, I'd like to point out that there was a slight error
in the path used in Sebastian's code.
That [4,4] that he was using should actually be replaced with a [4,2].
Also, those minus signs that you saw here should actually be replaced with plus signs
if we want this gradient descent implementation to converge.
Finally, even though these yi's and xi's are two-dimensional vectors,
when you implement your code, it may be easier
to just iterate over each individual entry.
So, for example, these xi's would be these values here.

10 - Path Smoothing Solution
============================
One way to solve this is to define a variable called change and set it equal to tolerance,
where tolerance is a parameter in our function, and you can see its default value is very, very small.
And, as long as this change is greater than or equal to tolerance,
we're going to initialize change to zero,
and iterate over not quite every entry in the path.
You can see here that we want to exclude the first and last entries.
And so, for each entry, we're going to
set an aux variable equal to the new path value at that entry,
we're going to increment newpath, where these are the equations from gradient descent,
we're going to increment change by however much this newpath has changed in this step,
and we're going to keep doing this and doing this
until change becomes less than tolerance, at which point
we can return our new path.
And we see if we run this, we go from this right-angle, jerky path
to this nice, smooth path taking us from [0,0] to [4,4].

11 - Zero Data Weight
=====================
Here is a tricky quiz question.
Say we alpha, our data weight to zero, and better, our smoothing weight, to 0.1,
and we run this to completion. What do we get?
Your original path? The straight line connecting the initial the final location?
Or will everything collapse to a single point?
You can try this out in the RDE before answering this quiz.

12 - Zero Data Weight Solution
==============================
The answer is a straight line, and the reason is really subtle.
It's because we're not modifying the first and last point.
Otherwise, it would be a single point.
I just hit the run button, and if you look at these coordinates, they go in 0.5 increments
from 0, 1, 2, 3, 4, and the same is true with this coordinate over here.
This is obviously the coordinates of a straight line
as a result of our smoother applied with a smoothing weight of 0.1 and no data weight.
If we change this to no smoothing weight, we obviously get the original path.
If we look at the right side as well as the left side, it's not identical.
When you implement your algorithm, please test this on those settings,
and we will give you a different path in our testing to see if your algorithm is implemented correctly.
Congratulations!
You just learned how to produce a smooth path. There are a few caveats.
If you apply this algorithm in a robot world like this where an A-star planner might give you something like this,
the smooth path might then lead straight through the obstacle, which you don't want.
There are ways to accommodate this, which I'll just hint at.
One is to use dynamic programming with a stochastic action function.
You've learned this in the previous homework assignment.
That way we stay away from the obstacle.
The second one is to introduce a term that propels you away from obstacles.
I won't go into any depth here, but in your optimization you could have a term
that pushes you away from obstacles
by maximizing the distance between the nearest obstacle and data point.
When you toss that in, you get a path that might look more like this
that is still smooth but maximizes your clearance from obstacles.
We will revisit this in the homework assignment.

13 - PID Control
================
Let's now talk about the second part of this lesson called PID control.
PID control is a vast field in control, and many, many classes can be taught about this one subject matter.
What I'll do is I'll give you the very basics, and I'll let you implement the very basics.
I promise it'll be fun.
You'll be able to drive a car around, and the Google car to the present day uses a version
of this exact same controller that is, of course, much more tuned the specifics of our car.
But you get to see some of the essence of what it means to control a car.
Here is the problem. Consider the following car with a steerable front axle and 2 non-steerable wheels in the back.
Say we wished this car to drive along this line, which is the output of our smoother we just discussed.
Let's assume the car has a fixed forward velocity,
but you have the ability to set the steering angle of the car. How would you do this?
You would keep the steering constant?
You would use random steering commands?
Or you could set the steering angle in proportion to what's known as the "crosstrack error,"
which is the lateral distance between the vehicle and the so-called reference trajectory.
The third possibility is steer in proportion to the this crosstrack error or CTE.
Choose one of those that you think is best suited to control the car.

14 - PID Control Solution
=========================
And yes, you'll steer in proportion to the crosstrack error,
which means the larger the error, the more you're willing to turn towards the target trajectory.
You can see that this works. As you get closer to trajectory, your steering will be slower and slower.
You will reach the trajectory.
Clearly the other two answers are really bad.
A constant steering will put you in a circle and not in a straight line.
Random steering, if you ever implement this, is a really bad idea.
Believe me. We accidentally did this once.
It's a really bad idea.

15 - Proportional Control
=========================
What you just learned is called a "P-controller" where P stands for proportional.
Here is a really trick question by which I want to test your intuition--
one that doesn't have a unique answer, but it has a best answer.
Suppose you do what I just said. You steer in proportion to the crosstrack error.
That is, your steering angle is proportional by some factor of tau to the crosstrack error.
What will happen with the car?
It never quite reaches the reference trajectory? It overshoots?
Or either can happen?

16 - Proportional Control Solution
==================================
My answer is it actually overshoots.
The problem is no matter how small this constant is over here,
It will eventually turns its wheels quite a bit towards it's trajectory.
Then it'll move towards a trajectory more and more,
and when it hits it, it's wheels will be straight,
but the robot itself will still be oriented a little bit downwards, so it's forced to overshoot.
What this means is that applied to a car, a P-controller will act like this.
It'll slightly overshoot, and that could be okay. The overshooting is very small.
But it'll never really converge.
It'll be what's called "marginally stable" or often just "stable" in the literature.

17 - Implement P Controller - Artificial Intelligence for Robotics
==================================================================
I want you to implement such a controller.
Here is the code I've prepared for you.
There is a class robot with which you're familiar.
It has an "init." You can set the position using the function "set" as before.
There are steering_noise and distance_noise.
You're familiar with this.
There is also something called "drift," which you won't use right now,
but later on it'll become handy.
There is your move command, all the way we've implemented before.
I've improved a little bit the print out of the coordinates using floats.
I want you to implement the run command, which takes as input the control parameter
that governs the proportional response of the steering angle to the crosstrack error.
The robot has an initial position of 0, 1, and 0, a speed of 1,
and I wanted to simulate it for 100 steps.
Here is what I envision to happen.
Your robot is initially off the the x axis by 1.
I want it to drive along the x axis.
The y value is the same as the cross track error.
By turning, inversely proportional to the y value,
using a parameter tau that sets the response strength of the proportional controller.
I want the robot to turn towards the x axis, drive in that direction, overshoot,
turn around, and drive back.
To do this, simulate the world for a 800 steps, and use a proportionality term
that sets my steering angle alpha in proportion to the crosstrack error y.
Enter your code here, and when you're done with it, and you run it with the coefficient 0.1,
here's the output that I want you to produce. It's 100 lines.
You can see the robot position starting 1 off in y.
It then reduces y over time to go into negative territory.
On the right side you see this corresponding steering orientation,
and you can see as you move on the y coming back into positive territory,
and you can see how the robot overshoots slowly around the reference trajectory of the x axis.
Please go implement this.

18 - Implement P Controller Solution - Artificial Intelligence for Robotics
===========================================================================
Here is my implementation. It's really simple.
I execute the following loop 100 times.
I set the crosstrack error to my robot y.
The steering angle becomes minus my control parameter times the crosstrack error.
I call the move command with a steering angle and the given speed.
I print as an output my robot along with the steering direction.
This simple routine just does it.

19 - Oscillations
=================
Let's now modify the parameter to 0.3, and here is my quiz.
If you modify the control parameter from 0.1 to 0.3, what happens?
It oscillates faster? It oscillates slower? Or nothing?
Please check exactly one of those.

20 - Oscillations Solution
==========================
As we'll see, they'll oscillate faster.
You have to spend some time with this, but for the larger value of 0.3,
we reach a negative value in y already here, which means we just crossed the line.
This is just 13 steps in whereas if we were back to 0.1,
then our step 13 would still be 0.6 off.
So clearly the control oscillation is much slower, and we compensate much less

21 - PD Controller - Artificial Intelligence for Robotics
=========================================================
The basic next question is is there a way to void the overshoot?
It would be nice if we could do this, because driving in an oscillating car is no fun.
In fact, it makes you really seasick, believe me.
I've been in this car for months on end when we prepared for the Darpa Grand Challenge.
The trick is called "PD-control."
In PD-control my steering alpha is no just related to the crosstrack error by virtue
by virtue of the gain parameter tau p,
but also to the temporal derivative of the crosstrack error.
What this means is that when the car has turned enough to reduce the crosstrack error,
it won't just go shooting for the x axis,
but it will notice that it's already reducing the error.
The error is becoming smaller over time. It counter steers. It steers up again.
This will allow it to gracefully approach our target trajectory,
assuming appropriate settings of our differential gain--tau d versus the proportional gain tau p.
How do you compute this derivative over here?
Well, at time t this is the same as the crosstrack error at time t minus the crosstrack error
at time t minus 1 divided by the time span between t and t minus 1.
In our code, we assume delta t equals 1, so so we can omit this.
The difference of the current crosscheck error and the previous one is this term over here.
We now control not just in proportion to the error itself but also to this difference
of the error using a second constant tau d.
Let's implement this. Now I give the run command two parameters--param1 and param2.
I want you to implement a controller that varies the steering direction proportionally
according to parameter 1, and differentially proportionally to parameter 2.
Again, run for 100 time steps and see what happens.
When I run my new controller with proportionality parameter of 0.2
and the differentiation one is 3.0.
Then, I get a sequence of y values that converge much more gently to 0.
Miraculously, as time goes on, they really go down to 0 and stay at 0,
which we didn't achieve for the proportional controller.
Please write that routine so we can test it.

22 - PD Controller Solution - Artificial Intelligence for Robotics
==================================================================
Here is my solution. I build a variable called "diffcrosstrackerror,
which is in my differential, that is set to the momentary crosstrack error
minus the previous one which I the very first time initialize to the present one.
Then in the steering, I don't just steer proportionately to the crosstrack error,
but also proportionately to the differential crosstrack error times the parameter 2.
When I put this in and I run it, I will get exactly the output that I showed you.

23 - Systematic Bias
====================
Let's talk about a problem that often occurs in robotics called a "systematic bias."
It goes as follows.
When you ordered your car, you believed the front wheels were 100% aligned,
but your mechanic made a mistake, and he aligned the wheels a little bit at an angle.
Now, for people that isn't a big concern. When we notice this we just steer a little bit stronger.
But let's try this out with out our proportional controller.
I'm now adding a line that sets the steering drift to be 10 degrees,
which in radians is this expression over here, using setsteeringdrift command.
I now want you to run my proportional controller with parameter 0.2,
and for now we're going to set the differential controller to zero.
When you do this, what happens?
It works just as before or it causes a new, big crosstrack error?
Go try it out.

24 - Systematic Bias Solution
=============================
Of course it causes a new error.
If I go to my output for 100 steps, I find that the y value is between 0.7 and 0.9.
It really a lot of error.
Put differently, the robot oscillates a bit like this with a fairly constant
new offset error due to this bias.
Even though the bias was in steering, it manifests itself
as an increased crosstrack error in the y direction.

25 - Is PD Enough
=================
Here's a question for you that will require some thought,
and you can try it out before answering this.
Can the differential term solve this problem?
Yes or no?

26 - Is PD Enough Solution
==========================
The correct answer is no. Let us try this out.
Let's enter a 3.0 for the differential term, run everything,
and the y error is still large.
It converges now, 0.87, but it's still really, really large.

27 - PID Implementation - Artificial Intelligence for Robotics
==============================================================
What's the intuition?
If you drive a car and your normal steering mode leads you to a trajectory far away from the goal,
then what I submit you do is you notice over a long period of time you can't get closer.
So you start steering more and more the more time goes by to the right to compensate this bias.
As a result, when you drive you steer the car this way.
To do so, you need a sustained situation of large error.
That's measured by the integral or the sum of the crosstrack errors over time.
Let's make a new controller where steering is proportional to the crosstrack errors before.
It's equally proportional to the differential of the crosstrack error,
but now it's also proportional to what's called the integral or the sum
of all the crosstrack errors you ever observed.
This term is interesting. If we have a constant crosstrack error of, say, 0.8
and the sum will increase by 0.8 for each time unit, it'll become larger and larger and larger,
and eventually it'll correct the robot's motion.
This is called the PID controller.
This is the P or the proportional term, the D or the differential term, and the i for integral.
P-I-D.
Let's implement this, and the integrated crosstrack error
is the sum of all crosstrack errors you ever observed.
Let's implement this in our code.
I give you an integral factor of 0.004.
Let's not worry why I picked those. They're actually wisely chosen, as you will see in a minute.
But let's run our code and now modify our code to also allow for this parameter over here.

28 - PID Implementation Solution - Artificial Intelligence for Robotics
=======================================================================
Here is my solution. I implement a variable int crosstrack error outside my main loop
then initialize with zero.
I then add to the int crosstrack error my local crosstrack_error.
Then I have a controller that steers in proportion to the int<u>crosstrack</u>error.
When I hit run, I find that my y variable slowly converges all the way down to 0 or 0.05.
I get even faster conversions when I set this parameter to 0.01,
looking down you can see a little overshoot, but my controller converges to 0.0 fairly quickly
and then tends to stay close to 0.0.
This PID controller is kind of the best solution for the control problem at hand.
You just implemented one.
Now, here's the big question for you.
How can we find good control gains
where control gains are these parameters tau p, d, and i.
Now, this is my favorite part of this class.
Every one of my students has made it through it, and every one of my students
is puzzled why I insist on this, but when they implement it they get to love what I'm just about to show you.
The answer is to called "twiddle."
Twiddle is my favorite algorithm that I have used in my entire life.
Some people call it "coordinate ascent" to make it sound a little more sophisticated,
but I just called it twiddle, because it really gets to the heart of what's happening.

29 - Twiddle
============
In Twiddle, we're trying to optimize for a set of parameters.
To do so, our function run() must return a goodness.
This goodness value might be the average crosstrack error.
Say I wanted to implement Twiddle so as to minimize the average crosstrack error.
If that's the case, then the output of run depends on the three parameters.
Here's how Twiddle works.
Build a parameter vector of our 3-target parameters, and initialize it with zero.
Also, build a vector of potential changes that you want to probe and initialize them for now with 1.
Then you can run our command run( ) with our parameters,
and whatever it outputs is our best error so far.
Now we wish to modify p as to make the error smaller.
That's where Twiddle comes in. It's a really smart algorithm, I believe.
We sequentially go through these parameters.
Obviously, you shouldn't write 3. You should write len of p.
First we tried to increase p by our probing value,
compute a new error for this new modified p.
If this new error is better than our best error, then we do two things.
First, we set best_err to err, and we even modify our dp to a slightly larger value
by multiplying it with 1.1.
Otherwise, we try the other way.
We subtract dp from p--and we have to do it twice now because we added it before.
Then we do the same thing again as over here. I'm not going to write it out.
We check whether the error is better than our best error, we retain it, and we multiply dp by 1.1.
But if both of those fail--this one over here and this one over here--
we set p[ i ] back to the original value, and we decrease our probing thing over here,
say, by multiplying it with 0.9.
That's the core of Twiddle, and what it really does is for each coordinate in isolation
it moves our parameter down a little bit by this value over here.
If it then finds a better solution, it retains it, and it even increments the probing interval.
If it fails to find a better solution, it goes back to the original and decreases our probing interval.
We do this entire thing so long as the sum of the dp's is larger than the threshold.
Somewhere in here we say while some of dp is larger than 0.00001.
It's hard to read, but I hope you can follow it.
This is Twiddle. Let me put this into pictures.
We have three parameters--0, 0, 0.
Then in the first iteration, we bump one of the parameters up and see if it improves the error.
If that's the case, we retain it.
Then we go to the second parameter. We bump it up. It might not work.
We bump it down and maybe retain that one, and so on.
Now, as we keep bumping up, we might find that neither bumping up nor bumping down helps.
What we do instead is we retain the original solution but make our probing interval
smaller than before by a factor of 0.9.
In doing so, we can zoom in more and more into a detailed parameter until it finally converges.
It's local hill climber, but it happens to be really, really efficient.

30 - Parameter Optimization - Artificial Intelligence for Robotics
==================================================================
So to implement this I’ve modified the RAN
procedure to input a parameter vector of three
parameters. And for reasons that will be obvious
later, I have a print flag that I default to false.
I have the same initial parameters as before,
speed and arrow cross stick arrow – into the
cross stick arrow, I set my fifth parameter
and to make it a little bit more obvious how
what the effect of parameter selection has on
my arrow. I also set the total number equations
to N times 2 and when I count the total cross
stick arrow, I only counted from step N 1,
so I give the algorithm a chance to convert to
zero for N steps, they don’t count the cross
stick arrow, but like to know how the cross
stick arrow evolves quite dramatically from
step 101 on to 200. If the print flag is set, I
set the output here in degrees and not in variance
and I return my average arrow before value.
So I wanted to write the routine twiddle and
the routine should find the optimal parameters
and return them to me. So I want you to
implement the twiddle with a tolerance and
threshold of 0.001. In one twiddle, it shows
the parameters over time and the cross
stick arrow. And this cross stick arrow
very quickly goes to zero. In fact after a
few iterations, 107 in my implementation
we get a cross stick arrow of 3.611 to the
minus 17th. And here is the typical control
one, you see my X, my Y, my orientation,
my drift is constant, that’s my constant
drift parameters and the beginning of the
arrows are 195 on average. But after a short
amount of time, you find that my Y arrow
goes down to 10 to the minus 6 and stays
there, which means our controller is really,
really good in tracking our desired location.
In our final control error between time step
100 and 200 is 3.611. So I wanted to
implement twiddle, we might change something
on the vowel set up, but when you run it,
it will be such that if you want a full PED
controller and find the optimal parameters
that the final control error, will be really, really
small and that’s how we’ll checking.

31 - Parameter Optimization Solution - Artificial Intelligence for Robotics
===========================================================================
Here is my implementation of twiddle. This
is a routine that you can keep this way for
many, many different applications. All it
requires is a way to evaluate something that
depends on the parameters and gives you a
single arrow that you would like to minimize.
We have three parameters in total, I set the
parameters themselves to zero, but the deltas
to one and it’s just the counter, its unimportant.
If the sum of D params is still larger than our
tolerance which we initially have as 0.001 and they go through all
the parameter sequentially I increment that
by D params, find out what the arrow is if
the arrow is better than our best arrow,
which I initialize with the initial arrow
and I keep the best arrow and I even increment
D params. Otherwise, I try the other direction.
One, find out the arrow, if that succeeds,
I keep it, I increment D params. And here is
my last case, I didn’t succeed, so going to
set it back to the old parameter vector and
decrease my D params by 0.9. I increase my
counter, here is my little print out command
for debugging and I will turn the parameter
vector. So it will be comingout of the print
vectors over here and play with this a little more
. If I want twiddle, compute the best parameters
and then calculate the error using these
parameters and print out the parameters
along with the arrow, I get a parameter vector
and I get an arrow that’s basically zero.
Now let’s switch off the integral term.
And I can do this with a little trick.
I just set D params number two, which is the
final one to 0.0 as if I’ve already learned the
integral term. When I run this, I get a zero
integral term, but the arrow that’s somewhat
larger than the final arrow, the desired. And
that’s because the integral term is really
required to drive the arrow, down to zero. Let’s
also remove the D term and see what happens
and the result is a really large arrow,
0.55. That large arrow, sustains even if
I remove the over drift by commenting
it out. You still get an arrow, of 0.10 if
it does have a proportional controller, whereas
if I add in the differential parameter again,
by removing the D param 1 command the
0.103 goes down to 5.7 to the minus 11,
which is practically zero. So you can see
the importance of the D term for driving
the arrow, down to zero, in the case without
drift and for the integral term in cases for
vowels with a systematic bias. You play
a little bit more with this code for the
homework assignment. But this is it for now.

32 - Summary
============
Let me summarize. You learned two really important
things that we use every day in robot programming
and they were somewhat complementary. First
we talked about smoothing which took a discrete
path and turned it into continuous smooth path.
And then we turned about how the robot can
follow this smooth path, using a control
mechanism called PID. With this, you can
actually implement quite a bit of robotics,
with no matter what robot you have, apply
a planner, apply a smoother, apply a controller
and it will do just fine. In fact, this is about
the level at which our DARPA Robot Challenge
car won the DARPA Robot Challenge . The
Google car itself has a little bit more juice
in it. It considers the case that the steering
wheel itself has inertia and that the steering
wheel was driven by something called torque
, not by position, but leaving this aside, you
really got a gist out of what’s happening in
robotic driving. And now we’re able to really
control an actual robot. Congratulations,
that is really, really cool.
