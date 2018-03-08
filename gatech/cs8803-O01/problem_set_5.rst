Problem Set 5
=============


1 - Missing Parameters
======================
Welcome to homework 5.
In the first problem, you're going to build some intuition for what happens to a robot's path
when one of the these parameters, either toe p, toe d, or toe i, is set equal to 0,
so if we don't include that term in our steering angle equation.
In each of these 4 cases on the left, the black horizontal line is the intended track for the robot,
while the pink represents its actual motion.
In each of these cases, the robot has a 10 degree positive drift
and starts with a cross check error of 1.
For each of these 4 cases, you should go through and decide which of these radio buttons
is the correct selection.
So for example, if you thought that this was appropriate robot motion
and all the parameters were tuned correctly,
you would select no problem.
Keep in mind that each column should be selected exactly 1 time. Good luck!

2 - Missing Parameters Solution
===============================
This was actually a really tricky question.
So let's, first, mark down the answers,
and now we can talk about why.
So these were the answers and let's think about why.
We have some really interesting behavior over in some of these graphs,
and it's nice to think about what's causing that behavior.
So let's start with number 2.
Pretty straight forward. The robot does exactly what we want.
It starts off away from the track, then it approaches it, and stays right on the track.
That's exactly what we want PID to do, so this is no problem.
Number 3 looks similar to number 2 but not quite because now you can see the line
that we're approaching is not actually the track.
That's because we're reaching the steady state where the robot's upward drift
is being balanced by its downward tendency caused by this term,
and though we reach some sort of steady state, it's not the steady state we want,
which would be right on the track.
The key to understanding number 4 was realizing that the robot
starts by moving upwards.
This is the only case for the robot started going up,
and what's happening here is the drift is dominating since the toe p is equal to 0,
there is no initial term that steers the robot towards the goal,
and without that, the drift is going to take over.
Of course, as we accumulate error that gets corrected for and we steer down,
but eventually we get into this sort of oscillating behavior.
The oscillations are not as frequent, however, as they are in case number 1.
If we think of this differential CTE term as a sort of smoothing term,
which damps out these wild oscillations.
Then we can see how, if tow d is equal to 0, we would expect these sort of
growing oscillations, and this behavior is characteristic of any PID controller
where the differential term is too small.

3 - Cyclic Smoothing
====================
Welcome to homework assignment #5.
Today I only have programming assignments. One on smoothing and one on control.
In both cases, we are trying to drive a car on a racetrack as fast as we can.
Okay? You'll see in a minute what I mean by this.
But think of the car going on an oval just like that.
So in this first exercise, you're going to go through a sequence of improvements
of the code smooth.PI.
I'm giving you a path that is very much a box path.
It starts at 0,0, cranks up the estimation all the way to 6,
then increases the y all the way to 3.
It goes down on x all the way down to 0, and then uses the y all the way down to almost 0.
If I draw this, the way this looks like--
we start at 0,0, all the way to 6,0, then we go up here to 6,3, and you go left to 0,3,
and down to 0,1.
This is a cyclic course so we're smoothing before what's for an open path.
I'd now like you to modify smoothing, so it can smooth this path over here.
So I want you to run the function smooth with path as an input--
the weight_data of 0.1 and the smoothing parameter of 0.1 and tolerance of 0.000001.
When you run it, what it should produce is a path like this, that when you plot it,
it looks a little bit like an oval.
You can look at these numbers carefully.
It ranks the corner points more into the interior.
I want to do it in a way that is cyclic, so that the last point connects smoothly
to the initial point over here.
So please modify the code just to be a cyclic smoother as opposed to before
it wasn't a cyclic smoother, and make it so each point get uprooted.
You don't keep 2 of the points fixed.

4 - Cyclic Smoothing Solution
=============================
So here's my solution. I modified the code in trivial ways.
I go through all the i's as opposed to leaving out the first and last node,
and because we are cyclic, I now have to add the model of division by the length of the path
in this smoothing parameter.
That's it. So it's a very small modification.
I don't have a graphical interface, but what the points look like is very much like an oval,
like this, after the smoothing. It actually put all endmarks a little bit,
which is a bit of a concern, which we address in a minute.

5 - Constrained Smoothing
=========================
[Thrun] So in this next assignment, I'd like you to fix certain data points.
Just as much as you fixed the data points originally in our path,
the beginning and end point, now I want to fix you 4 points.
These are the corner points in our data points.
In our original data, it's the one over here, the one over here,
and I want those to be fixed so they can't move.
And the way I indicated this in the code is by giving you a fix array that looks like this
where each of these numbers corresponds to exactly 1 data point.
There's as many elements in fix as there is in path.
And then when I call smooth, I add fix as a parameter.
So when you change the procedure and run it,
I can tell you you should be surprised by the output
in that when I run my procedure it copies over the initial path into the output.
We'll talk about this in a second, but please go ahead and change your procedure
so that your output ends up to be giving you something very much like this.
The modification is simple.
As I go through my data points, I only apply the update if it's not fixed.
So if the fix flag is not set, they go in here.
This is all indented one compared to before.
It's a single line change.
Let me tell you why this doesn't work.
Consider a few data points like these.
If you fix this data point over here,
then this guy is perfectly happy with his 2 neighbors--
this is a smooth path--
and so is this guy over here.
The only data point that's unhappy is the one over here
because it's not part of a very smooth path,
but this one is never being updated.
So as a result, all the other ones stay where they are.
They already have the absolute minimum for smoothness and for the data fit.
No updates take change, and we don't have the desired result.
We don't get a nice round curve the way we wish to get it.
To get this, we are going to modify our rule a little bit now, and that's the interesting part.
For a node like this with coordinates xi and yi,
we add to it with a very small constant gamma--
in fact, it will be half our weight smoothing constant in a minute--
2 times the previous guy--
and of course that's cyclic, so you have to make sure this is really cyclic--
minus the guy 2 steps away and minus our node.
Why this makes sense we see when we go into the opposite direction.
Here we add a small gamma, 2 times this guy over here minus this guy here
minus our original data point.
And behind this is a certain desire.
We want the vector over here to be the same as the vector over here.
This vector is this difference over here of xi + 1 over yi + 1 - xi over yi.
That is this vector over here.
And the vector over here is similarly the difference of the point i + 2
minus the same for i + 1.
If you set these to be equal and bring yi to the right side,
then if you modify yi in proportion to this expression over here, we reduce the error.
In fact, the expression in the brackets is the same as this one, called (A),
minus this one, called (B).
So we're looking at the mismatch between these 2 vectors
and use it to adjust the xi factor over here.
We do those sequentially--this one first, this one second.
You might call them a little bit sloppy
because the first update already inferences the second update. But who cares?
We're just going to add lines of code that achieve this over here,
and when you do this, please make sure that your update
understands the fact that these indices are cyclic.
So I did this in my code and I'm running it,
and out come the following numbers that you can read over here.
These numbers are indeed a cycle.
So if we were to plot them--and this is the original data--
these are the points we would constant,
then the new data lies in over very much like this. You can plot them.
Unfortunately, I can't plot them in our environment here, but you could see this.
Now we are not shifting the racetrack inbound anymore.
Please go to your code and modify the function smooth by doing these new constraints.
For the update strength, I suggest you use half of weight_smooth for each update.
So in total, you add another 0.1 as update strength.

6 - Constrained Smoothing Solution
==================================
And here is my solution. These are two update
lines. They’re basically identical except one
goes in one direction and the other direction.
Let’s look at the first; we have an update
weight over here. We add two times our
new constraint with the index I minus 1. This
is the subtract part. We subtract I minus 2 and
we subtract the original on the right side over
here. It’s exactly the math I’ve given you.
Same over here. If you won this math , you
get this new smooth curve. I should warn you,
this can be unstable, it can give you results that
are very poor you have to adjust these parameters
very carefully and this is one of many ways to
smooth. There is many other ways to smooth,
but the nice thing that you achieve here is that
you get actually smooth two points that they
are holding fixed, which is actually
really, really useful.

7 - Racetrack Control
=====================
[Thrun] So here's my second piece of software assignments in controls.
In the class we talked about how to make a car follow a straight line.
We used the line x = 0
where the crossing arrow was defined as the y difference between this axis.
We just went off the y value.
So now I want to make a more interesting course, a cyclic course, a racecourse.
Here's my racecourse. It has the radius r, which you can set.
The way I'd like to define this racecourse is through a half cycle where we use r,
same half cycle over here, and the stretches in between I want to be 2r long.
So for example, if this radius equals 25 meters, then this would be 50 meters.
The whole thing would be 100 meters, and this measurement would also be 50 meters.
I want you to program it such that the initial car is stationed right over here,
pointed upwards, and then it drives onto the racecourse like this,
all the way around infinitely often.
The key in doing this is going to be to set a function.
I have already modified for you the function run from our control class
to use that crosstrack_error with the parameter radius,
which we're going to set to 25, but I can pick a different value in my testing.
And then I have modified a little bit the update over here
to maintain the differential and the integral crosstrack_error,
and here is our steering control law that you are familiar with.
Instead of twiddle I'm just going to give you parameters, 10, 15, and 0.
Those work fine for me,
and they're actually the result of running twiddle without the integral part.
And then when I run it, I get my output. And here it is.
The crosstrack_error by and large is very small.
You can see the steering tends to be on the negative side.
Here we're steering at the first turn, here we're on the straightaway.
You can see this by the numbers.
Here we go into a turn again, so the turning becomes larger.
In all of this you find the crosstrack_error to be relatively small,
about 0.1 or so--not very much--and this continues and continues.
The final crosstrack_error for the second half of the race is 0.005.
So you want this number to be really, really small.
The tricky part is when you code this up and code the function cte,
you need a different branch for this area here, for this area over here,
this area over here, this area over here.
Keep in mind that the robot is going to go in a cycle.
So it's going to traverse this one in the opposite direction with this one over here.
So good luck coding up the correct crosstrack_error function.

8 - Racetrack Control Solution
==============================
[Thrun] And here is my solution. We have 4 cases.
On the left side, if I'm on the left side of the racecourse,
as defined that x is smaller to radius,
then my crosstrack_error is defined by the distance to the circle,
centered at radius comma radius minus the radius itself.
So this is going to be 0 if I'm exactly on the circle.
If I'm more than 3 times over to the right side, I get a circle again.
It looks like the one before, but now the center of the circle is a little bit further to the right
by 3 times radius as opposed to 1 radius.
The rest is identical to the line over here,
so I'm subtracting the same radius on the right side.
You can't quite see it but it's there.
Interesting are the straightaways.
So if my y value is large on the upper part of the diagram--
in fact, it's larger than radius--then my crosstrack_error is the y coordinate
times 2 times the radius, which is the height of the racetrack.
If I'm down at the bottom, it's just the y axis,
but really important is the minus sign because I'm moving in the opposite direction.
So for your code, to run this correctly you would have gotten everything in this routine right.
So that finishes my homework assignment.
Congratulations. You were able to make a car drive on a racetrack.
That is actually quite a significant component of making cars drive.
The PID control methodology that you learned today
and the smoothing methodology are really, really essential
not just in controlling self-driving cars but in a great number of other control setups.
Thank you for taking the class so far. You learned a lot already.
You learned about localization, about planning and control,
and we almost learned talking about how to build a self-driving car.


