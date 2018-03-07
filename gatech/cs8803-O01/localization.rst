Localization
============


.. image:: https://dl.dropbox.com/s/rd7hs3zy1gffva2/Screenshot%202018-02-12%2008.29.34.png?dl=0
   :align: center
   :height: 300
   :width: 450

1 - Introduction
================
So welcome to Artificial Intelligence for Robotics.
You are entering at exciting 7-week class
in which you'll learn how to program self-driving cars.
And just to motivate what we're trying to achieve in this class,
let me show you some videos.
My interest in self-driving cars started with the DARPA Grand Challenge in 2004
in which my team at Stanford developed Stanley,
a robot that could drive itself through the Mojave Desert.
The vehicle was based on a Volkswagen Touareg
that was equipped with all kinds of sensors like GPS and laser,
and it was able to make its own decisions without any human input whatsoever.
The DARPA Grand Challenge was a government-sponsored race
that took place in 2005.
Here we see our robot Stanley moving through the desert
completely without a human on board.
The task was to drive a desert trail for about 130 miles,
and whoever was fastest would win the race.
Here we're passing a different robot by Carnegie Mellon University
about 110 miles into the race.
Our robot was able to navigate really steep mountainous roads
and able to avoid collisions with rocks or falling down a cliff
all based on its ability to use what I'm going to teach you in this class.
After almost 7 hours and 131 miles our robot returned all the way to the starting base
as the first robot to ever finish a DARPA Grand Challenge
winning Stanford University 2 million bucks
and Stanley a place in the Smithsonian Museum of American History.
This work led to the Urban Challenge, in which we built another robot called Junior
that eventually took second place.
The Urban Challenge was a followup race by DARPA
in which cars were asked to drive in traffic,
so whereas the Grand Challenge was kind of a motionless desert floor,
this was a mock urban city where the robot was able to interact with other traffic
and had to follow the traffic rules as in this left turn over here.
It had to be stay on lanes with very high precision,
accommodate oncoming traffic and just drive confidently
in a situation that really resembled a small city.
This led at Google to a sequence of experiments
known as the Google self-driving car.
I believe these are the best robotic cars out there today.
Here we see one of our Priuses on University Avenue in Palo Alto
they are undetected, driving just like a human driver,
but this car was driving by itself.
Our cars have been able to drive hundreds of thousands of miles
all across California and some of Nevada,
in downtown areas like San Francisco, on busy highways.
Here in Monterey, a small coastal city in California with lots and lots of pedestrians.
These are all completely self-driving moments where the car is able to accommodate
things like deer in the headlights in the middle of the night
or even crooked Lombard Street in San Francisco as shown in this video.
This is what I'm doing on my day job.
I really love, with my team, building self-driving cars.
We believe it's going to really change the world,
and in this class that's what I hope to enable you to do.
Let's dive in.

2 - Localization
================
The very first problem I'm trying to solve is called localization.
It involves a robot that's lost in space.
It could be a car. It could be a mobile robot.
So here is the environment, and the poor robot has no clue where it is.
Similarly, we might have a car driving on a highway,
and this car would like to know where it is.
It is inside the lane or is it crossing lane markers?
Now the traditional way to solve this problem is by using satellites.
These satellites emit signals that the car can perceive.
That's known as GPS, short for "global positioning system,"
and it's what you have in your dashboard if you have a car with GPS
that shows you the maps and shows you where you are.
Now unfortunately, the problem with GPS is its really not very accurate.
It's really common for a car to believe to be here but it has
2 meters all the way up to 10 meters of error.
So if you try to stay in the lane with 10 meters of error,
you're far off, and you're driving right over here, and you crash.
So for our self-driving cars, to be able to stay in lanes using localization,
we need something like 2-10 centimeters of error.
Then we can drive with GPS in lanes.
The question is, how can we know where were are with 10 cm accuracy?
That's the localization question.
In the Google self-driving car, localization plays a key role.
We record images of the road surface and then use the techniques
I'm just about to teach you to find out exactly where the robot is.
It does so within a few centimeters of accuracy,
and that makes it possible to stay inside the lane even if the lane markers are missing.
So localization has a lot of math, but before I dive into mathematical detail,
I want to give you an intuition for the basic principles.
I want to tell you the story of how we will localize this,
and then we can go through the math together so you can understand it.
I also want to let you program your own localizer
so you can program a self-driving car.

3 - Total Probability
=====================
Let me begin my story in a world where our robot resides.
Let's assume the robot has no clue where it is.
Then we would model this with a function--I'm going to draw into this diagram over here
where the vertical axis is the probability for any location in this world,
and the horizontal axis corresponds to all the places in this 1-dimensional world.
The way I'm going to model the robot's current belief about where it might be,
it's confusion is by a uniform function that assigns equal weight
to every possible place in this world.
That is the state of maximum confusion
Now, to localize the world has to have some distinctive features.
Let's assume there are 3 different landmarks in the world.
There is a door over here, there's a door over here, and a 3rd one way back here.
For the sake of the argument,
let's assume they all look alike, so they're not distinguishable,
but you can distinguish the door from the non-door area--from the wall.
Now let's see how the robot can localize itself by assuming it senses,
and it senses that it's standing right next to a door.
So all it knows now is that it is located, likely, next to a door.
How would this affect our belief?
Here is the critical step for localization.
If you understand this step, you understand localization.
The measurement of a door transforms our belief function,
defined over possible locations, to a new function that looks pretty much like this.
For the 3 locations adjacent to doors, we now have an increased belief of being there
whereas all the other locations have a decreased belief.
This is a probability distribution that assigns higher probability for being next to a door,
and it's called the posterior belief where the word "posterior" means it's after a measurement has been taken.
Now, the key aspect of this belief is that we still don't know where we are.
There are 3 possible door locations, and in fact, it might be
that the sensors were erroneous, and we accidentally saw a door where there's none.
So there is still a residual probability of being in these places over here,
but these three bumps together really express our current best belief of where we are.
This representation is absolutely core to probability and to mobile robot localization.
Now let's assume the robot moves.
Say it moves to the right by a certain distance.
Then we can shift the belief according to the motion.
And the way this might look like is about like this.
So this bump over here made it to here.
This guy went over here, and this guy over here.
Obviously, this robot knows its heading direction.
It's moving to the right in this example,
and it knows roughly how far it moved.
Now, robot motion is somewhat uncertain.
We can never be certain where the robot moved.
So these things are a little bit flatter than these guys over here.
The process of moving those beliefs to the right side is technically called a convolution.
Let's now assume the robot senses again, and for the sake of the argument,
let's assume it sees itself right next to a door again,
so the measurement is the same as before.
Now the most amazing thing happens.
We end up multiplying our belief, which is now prior to the second measurement,
with a function that looks very much like this one over here,
which has a peak at each door and out comes a belief that looks like the following.
There are a couple of minor bumps, but the only really big bump is this one over here.
This one corresponds to this guy over there in the prior,
and it's the only place in this prior that really corresponds to the measurement of a door,
whereas all the other places of doors have a low prior belief.
As a result, this function is really interesting.
It's a distribution that focuses most of its weight
onto the correct hypothesis of the robot being in the second door,
and it provides very little belief to places far away from doors.
At this point, our robot has localized itself.
If you understood this, you understand probability, and you understand localization.
So congratulations. You understand probability and localization.
You might not know yet, but that's really a core aspect of understanding
a whole bunch of things I'm going to teach you in the class today.

4 - Uniform Probability Quiz
============================
So let's move into our first programming exercise,
and let's program together the very first version of robot localization.
Here's a bit of program code--an empty list.
And what I'd like you to program is a world with 5 different cells or places
where each cell has the same probability that the robot might be in that cell.
So probabilities add up to 1.
Here's a simple quiz for the cells x1 all the way to x5.
What is the probability of any of those x's?
Index i goes from 1 to 5.

5 - Uniform Probability Quiz Solution
=====================================
And the answer is 0.2, which is the total probability, 1, divided by 5 grid cells.

6 - Uniform Distribution
========================
So now in our Python interface, I'd like to take this code over here,
which assigns to p an empty list and modified into code where p becomes
a uniform distribution over 5 grid cells as expressed in a vector of 5 probabilities.

7 - Uniform Distribution Solution
=================================
Here's an easy solution.
You just initialize the vector with five 0.2s.

8 - Generalized Uniform Distribution
====================================
Let's see if we can modify this to make a vector of length n
where I can vary the value of n and get a resulting vector with n elements.
So if n equals 5, we'd get the same result as before,
but for n equals 10, I should get a vector of length 10,
each of which would have value zero point one.

9 - Generalized Uniform Distribution Solution
=============================================
The answer is simple.
Use a for loop as shown here,
and you append to the list n elements, each of size of 1/n.
The dot over here is really important.
It gives you the floating point version.
Unfortunately, if we leave it out, the result will just be zeros,
which is not what you want.
Now we are able to initialize the initial belief of the robot in the world over here.

10 - Probability After Sense
============================
Let's look at the measurement of this robot in its world with 5 different grid cells--
x1 through x5.
Let's assume 2 of those cells are colored red whereas the other 33 are green.
As before, we assign uniform probability to each cell of 0.2,
and our robot is now allowed to sense.
What it sees is a red color.
How will this affect my belief over different places?
Obviously, the one's for x2 and x3 should go up,
and the ones for x1, x4, and x5 should go down.
So I'm going to tell you how to incorporate this measurement into our belief
with a very simple rule--a product.
Any cell where the color is correct--any of the red cells--
we multiply it with a relatively large number--say, 0.6.
That feels small, but as we will see later, it is actually a large number.
Whereas all the green cells will be multiple with 0.2.
If we look at the ratio of those, then it seems about 3 times as likely
to be in a red cell than it is to be in a green cell,
because 0.6 is 3 times larger than 0.2.
Now let's do the multiplication.
For each of those 5 cells, can you tell me what the result would be
multiplying in the measurement in the way I've stated.
Please, for these 5 boxes, fill out the number.

11 - Probability After Sense Solution
=====================================
The answer is obviously for the red cells we get a 0.12
whereas for the green cells we get a 0.04,
which is the product of 0.2 x 0.6 versus 0.2 x 0.2.

12 - Compute Sum
================
This is in principle our next belief.
It only has one problem, which is it isn't a valid probability distribution.
The reason why is probability distributions always have to add up to 1.
If I ask you what the sum of all these values,
then we find out it doesn't add up to 1.
Please type in the sum of all these values.

13 - Compute Sum Solution
=========================
If you add up all these values, you get 0.36.

14 - Normalize Distribution
===========================
To turn this back into a probability distribution,
we will now divide each of these numbers by 0.36.
Put differently, we normalize.
Please, in these 5 fields enter your result for dividing 0.04 or 0.12 by 0.36.
Please check that the sum of those truly adds up to 1.

15 - Normalize Distribution Solution
====================================
So 0.12 divided by 0.36 is the same as 12 divided by 36 is the same as 1/3 or 0.333.
And 0.04 divided by 0.36 is the same as 4 divided by 36,
that is 1/9.
If you look at that numbers, 1/3, there's 1/3 plus 3/9 is another 1/3 gives exactly 1.
So this is a probability distribution, which is often written in the following way.
The probability of each cell, i where i could range from 1-5,
after we've seen our measurement Z.
The probabilist would also call it posterior distribution of place xi given measurement Z.
Let's implement all this.

16 - pHit and pMiss
===================
Here's our distribution again.
Here's our factor for getting the color right or for getting it wrong,
and let's first start with a non-normalized version.
Write a piece of code that outputs p after multiplying in pHit and pMiss
at the corresponding places.

17 - pHit and pMiss Solution
============================
One way to do this is to go explicitly through all these 5 different cases from 0 to 4
and multiply in manually the miss or hit case.
This is not particularly elegant, but it does the job,
and as I hit the "Run" button, we get the correct answer that is not normalized.

18 - Sum of Probabilities
=========================
My next question is can you print out the sum of those to normalize them?
Modify the program so you get the sum of all the p's.

19 - Sum of Probabilities Solution
==================================
Well, it turns out Python gives you a function called "sum,"
and if you now hit the run button, you get the correct answer.

20 - Sense Function
===================
I want to make this a little bit more beautiful.
I will introduce a variable called "world,"
and for each of the 5 grid cells, world specifies the color of the cell--
green, red, red, green, green.
Further, I define the measurement Z to be red.
Can you define a function, called "sense," which is the measurement update,
which takes as input the initial distribution p
and the measurement Z and all the other global variables
and outputs a normalized distribution called "Q" in which Q reflects
the non-normalized product of our input probability,
which will be 0.2 and so on,
and the corresponding pHit or pMiss in accordance
to whether these colors over here agree or disagree?
When I call sense(p, Z), I expect to get the vector as output as before,
but now in the form of a function.
The reason I'd like to have a function here is because later on as we build our localizer
we will apply this to every single measurement over and over again.
This function should really respond to any arbitrary p and arbitrary Z,
either red or green, and give me the non-normalized Q,
which gives me the vector 0.04 or 0.12 and so on and so on.

21 - Sense Function Solution
============================
Here's my solution.
I start with an empty list over here, and I build it up
using the append command over time.
I do so by iterating over all the elements in my probability p,
and I set a binary flag whether my measurement that I received is the same
I would expect at the ith grid cell over here from this list over there.
If the case hit is positive, it's true, so we're going to multiply p with pHit.
If it's false, then the flag hit will valuate to zero, 1 - hit will be 1.
You're going to multiply pi with pMiss.
I build up the list, return it, and run it, and out comes
0.04, 0.12, 0.12, 0.04, and 0.04 as expected.

22 - Normalized Sense Function
==============================
Let's take that same piece of code
and modify it to give me a valid probability distribution.
Please modify this code so it normalizes the output of the function sense
so it add up to 1.

23 - Normalized Sense Function Solution
=======================================
Here are the three lines of code I used to program this in.
First I computed the sum of a vector Q using the function sum,
which makes it really easy.
Then I go through all the elements in Q and just divide it by s,
which is the normalization, and when I run it, I get 1/9, 1/3, 1/3, 1/9, and 1/9.
So I've just implemented the absolute key function of localization,
which is called the measurement update.

24 - Test Sense Function
========================
Let's just go back to our example and see what an amazing thing you've just programmed.
We had a uniform distribution over places.
Each place had a probability of 0.2.
Then you wrote a piece of code that used the measurement to turn this prior
into a posterior, in which the probability of the 2 red cells was
a factor of 3 larger than the posterior of the green cells.
You've done exactly what I gave you intuitively in the beginning as the secret of localization.
You manipulated a probability distribution over places into a new one
by incorporating the measurement.
In fact, let's go back to our code and test in your code whether we get a good result
when we replace our measurement red by green.
Please type green into your measurement variable and rerun your code
to see if you get the correct result.

25 - Test Sense Function Solution
=================================
I'm now replacing the red by green over here,
and I rerun my code and out come these funny numbers.
Somewhere in there is the division by 44,
but you can see that the 1st, the 4th, and the 5th grid cell have a much larger value
than the grid cells in the middle.
So let's dive in.

26 - Multiple Measurements
==========================
In fact, I'd like you to modify this code a little bit more
in a way that we have multiple measurements.
Instead of Z, we're going to make a measurement vector called "measurements."
We're going to assume that we're going to first sense red and then green.
Can you modify the code that so it updates the probability twice
and gives me the posterior after both of these measurements are incorporated?
In fact, can you modify it in a way
that any sequence of measurements of any length can be processed?

27 - Multiple Measurements Solution
===================================
The modification is simple.
We will call the procedure sense multiple times,
in fact, as often as we have measurements, which is the for loop over here,
we grab the kth measurement element and apply it to the current belief.
Then recursively update that belief into itself.
In this case, we run it twice. We print the output.
For this specific example, we get back the uniform distribution.
These are all 0.2s approximately.
The reason is we up multiplied each field once for the 0.6
and down multiplied for the 0.2.
And these effects were in total the same for each cell.
As a result, we get the same output over here. It's quite remarkable.

28 - Exact Motion
=================
Before we're done with localization, I'd like to talk about robot motion.
Suppose we have a distribution over those cells--
such as this one: 1/9, 1/3, 1/3, 1/9, and 1/9--
and even though we don't know where the robot is,
the robot moves, and it moves to the right.
In fact, the way we're going to program is we will assume the world is cyclic,
so if it drops off the right-most cell it finds itself in the left-most cell.
Suppose we know for a fact the world moved exactly 1 grid cell to the right,
including the cyclic motion.
Can you tell me for all these 5 values, what the posterior probability is after that motion?

29 - Exact Motion Solution
==========================
The answer is all of these are shifted to the right.
The 1/9 in the left-most cell goes over here, the 1/3 over here,
and finally the right-most 1/9 finds itself on the left side.
In the case of exact motion, we have a perfect robot.
We just shift the probabilities by the actual robot motion.
Now, that's a degenerate case. Let's program this one.

30 - Move Function
==================
I define a function "move" with a distribution p and a motion number "U,"
where U is the number of grid cells that the robot is moving to the right or to the left.
I want you to program a function that returns the new distribution Q after the move
where if U equals zero, Q is the same as p.
If U equals 1, all the values are cyclically shifted to the right by 1.
If U equals 3, they are cyclically shifted to the right by 3.
If U equals -1, they're cyclically shifted to the left.
Please call the function with argument p and a shift to the right by 1.
I've commented out my measurement part because for now
I don't want to do measurement updates.
In addition to this, I will use a very simple p,
that has a 1 at the second position and zeros elsewhere.
Otherwise, if we were to use the uniform p,
we couldn't even see the effect of the motion
whether that's programmed correctly or not.

31 - Move Function Solution
===========================
Here is the solution.
We start with the empty list. We go through all the elements in p.
This is the tricky line.
We will construct Q element-by-element by accessing the corresponding p,
and p is shifted by U and if this shift exceeds the range of p on the left,
we apply the modulo operator with the number of states as an argument.
In this case, it'll be 5.
Now, the reason why there is a minus sign is tricky.
To shift the distribution to the right, U = 1,
we need to find in p the element 1 place to the left.
Rather than shifting p to the right directly,
what I've done is I've constructed q by searching for
where the robot might have come from.
That's of course, in hindsight, from the left.
Therefore, there is a minus sign over here.
So think about this, as it's a little bit nontrivial,
but it's going to be important as we go forward and define
probabilistic convolution and generalize this to the noisy case.

32 - Inexact Motion 1
=====================
Let's talk about inaccurate robot motion.
We are again given 5 grid cells.
Let's assume a robot executes its action with high probability correctly, say 0.8,
but with 0.1 chance it finds itself short of the intended action,
and yet another 0.1 probability it finds itself overshooting its target.
You can define the same for other U values. Say U = 1.
Then with 0.8 chance it would end up over here,
0.1 it stays in the same element,
and 0.1 it hops 2 elements ahead.
Now this is a model of inaccurate robot motion.
This robot attempts to go U grid cells,
but occasionally falls short of its goal or overshoots.
It's a more common case robots as they move accrue uncertainty,
and it's really important to model this, because this is the primary reason
why localization is hard, because robots are not very accurate
We're now going to look into this first from the mathematical side.
I will be giving you a prior distribution,
and we're going to be using the value of U = 2,
and for the motion model that shifts the robot exactly 2 steps,
we believe there is a 0.8 chance.
We assign a 0.1 to the cases where the robot over or under shoots by exactly 1.
That's kind of written by this formula over here where the two gets a 0.8 probability,
the 1 and the 3 end up with a 0.1 probability.
I'm going to ask you now for the initial distribution that I'm writing up here,
can you give me the distribution after the motion?

33 - Inexact Motion 1 Solution
==============================
The answer is for our intended field over here 0.8,
the 2 neighbors 0.1 and a zero and zero over here.
Well done. Let's do this again for a different initial distribution.

34 - Inexact Motion 2
=====================
Let's assume we have a 0.5 in this cell and a 0.5 in this cell.
Remember that this is a cyclic-motion model,
so whatever falls off on the right side, you'll find on the left side.
Can you again for U = 2 fill in the posterior distribution?

35 - Inexact Motion 2 Solution
==============================
This is a pretty tricky question, which I'm going to answer in two phases.
Let's just look at the 0.5 over here, 0.8 of that, which is 0.4, ends up over here,
and 0.1 of this, which is 0.05 ends up over here.
The reason why I write it so small is because this is not the correct answer quite yet.
Let's look at the other 0.5.
0.4 goes two steps--1, 2--and ends up over here on the left side,
but 0.1 falls short and makes the 0.05 over here 0.05 in the second grid cell.
And interestingly enough, for the cell on the right side,
there's two possibly ways you could've gotten there.
Either by overshooting starting in the second cell,
or undershooting starting in the right cell.
So the total is the sum of these two things--0.1.
This is the final answer: 0.4, 0.05, 0.05, 0.4, and 0.1.

36 - Inexact Motion 3
=====================
Let me give you a final example in which I assume a uniform distribution,
and I want you to fill in for me the distribution after motion.

37 - Inexact Motion 3 Solution
==============================
The answer as it turns out will be just 0.2 everywhere,
and the reason is with every grid cell being equally likely,
applying this motion model will still make each grid cell equally likely.
Let's pick one of them--say this one over here.
We could have arrived here in 3 different ways.
Perhaps we started in x2 and our motion went well.
This gives us a 0.2 x 0.8.
Perhaps we started in x1 and we overshot,
which gives us a 0.2, for the cell x1, times a 0.1 for overshooting.
Or perhaps we started in x3 and we undershot, which gives us 0.2 x 0.1.
If we add those up, then we find it is the same as 0.2 x 1,
because the factors over here add up exactly to 1, which makes 0.2.
The result is 0.2.
You can apply this same logic to all the other cells.
This guy over here could have come from this guy, this guy, this guy,
where this one is weighted with 0.8 and the other two with 0.1.
That's called a convolution,
and as well see later, there's a very nice way to write this mathematically
as something called Theorem of Total Probability.
But for the time being, I'd like to program this in.

38 - Inexact Move Function
==========================
I'm going to give us a pExact of 0.8, pOvershoot of 0.1, and pUndershoot of 0.1.
I'd like you to modify the move procedure to accommodate these extra probabilities.

39 - Inexact Move Function Solution
===================================
Here's one way to implement this.
We're going to introduce the auxiliary variable "s,"
which we build up in three different steps.
We multiply the p value as before for the exact set off by pExact.
Then we add to it two more multiplied by pOvershoot or pUndershoot
where we are overshooting by going yet 1 step further than U
or undershooting by cutting it short by 1.
Then we add these things up and finally append the sum of those
to our output probability q.
When we run this, we get for our example prior of 0, 1, 0, 0, 0,
the answer 0, 0.1, 0.8, 0.1, and 0.

40 - Limit Distribution Quiz
============================
Here's a question for you that is somewhat involved,
and I really want to check your intuition.
Suppose we have 5 grid cells as before
with an initial distribution that assigns 1 to the first grid cell and 0 to all the other ones.
Let's assume we do U = 1, which means with 0.8 chance
in each action we transition 1 to the right.
With 0.1 chance we don't move at all,
and with 0.1 chance again we skip and move 2 steps.
Again, let's assume the world is cyclic,
so every time I fall off on the right side, I find myself back on the left side.
The question is suppose I run infinitely many motion steps.
Then I actually get a what's called a "limit distribution"
What's going to happen to my robot if it never senses but executes the action
of going 1 to the right on our little cyclic environment forever.?
What will be the so-called limit or stationary distribution be in the very end?

41 - Limit Distribution Quiz Solution
=====================================
You might have guess it correctly. It's the uniform distribution.
There's an intuitive reasoning behind this.
Every time we move, we lose information.
That is, in the initial distribution we know exactly where we are.
One step in we have a 0.8 chance, but the 0.8 will fall to something smaller
as we move on--0.64 and so on.
The distribution of the absolute least information is the uniform distribution.
It has no preference whatsoever.
That is really the result of moving many, many times.
There is a way to derive this mathematically,
and I can prove a property that's highly related, which is a balance property.
Say we take x4, and we'd like to understand how x4 at some time sub t
corresponds to the previous time distribution over all these variables.
For this to be stationary, it has to be the same.
Put differently, the probability of x4 must be the same as 0.8p(x2) + 0.1p(x1) + 0.1p(x3).
This is exactly the same calculation we did before where we asked
what's the chance of being x4.
Well, you might be coming from x2, x1, or x3,
and there's these probabilities are 0.8, 0.1, and 0.1,
they govern the likelihood you might have been coming from there.
Those together must hold true in the limit when things don't move anymore.
Now, you might think there are many different ways to solve this
and the 0.2 is just one solution,
but it turns out 0.2 is the only solution.
If you plug in 0.2 over here and 0.2 over here and 0.2 over here,
you get 1 x 0.2, and that's 0.2 on the right side.
Clearly, those 0.2s over here meet the balance that is necessary
to define a valid solution in the limit.

42 - Move Twice
===============
Now let's go back to our code and move many times.
Let's move twice, so please write a piece of code that makes the robot move twice,
starting with the initial distribution as shown over here--0, 1, 0, 0, 0.

43 - Move Twice Solution
========================
Here's a piece of code that moves twice by the same amount as before,
and the output now is a vector that assigns 0.66 as the largest value
and not 0.8 anymore.

44 - Move 1000
==============
Let's move 1,000 times.
Write a piece of code that moves 1,000 steps and give me the final distribution.

45 - Move 1000 Solution
=======================
Here's my code. We have a loop for 1,000 steps.
We move 1,000 times, and we print the corresponding distribution over here.
It's 0.2 in each case as expected.

46 - Sense and Move
===================
Wow, you've basically programmed the Google self-driving car localization
even though you might not quite known it yet.
Let me tell you where we are.
We talked about measurement updates, and we talked about motion.
We called these two routines "sense" and "move."
Now, localization is nothing else but the iteration of "sense" and "move."
There is an initial belief that is tossed into this loop if you.
If you sense first, if comes to the left side.
Then localization cycles through these--move, sense, move, sense, move, sense.
move, sense, move, sense cycle.
Every time the robot moves, it loses information as to where it is.
That's because robot motion is inaccurate.
Every time it senses it gains information.
That is manifest by the fact that after motion,
the probability distribution is a little bit flatter and a bit more spread out.
and after sensing, it's focused a little bit more.
In fact, as a foot note, there is a measure of information called "entropy."
Here is one of the many ways you can write it:
[-Ʃp(xi)log p(xi)]
as the expected log (logarithmic) likelihood of the probability of each grid cell.
Without going into detail, this is a measure of information that the distribution has,
and it can be shown that the update step, the motion step, makes the entropy go down,
and the measurement step makes it go up.
You really losing and gaining information.
I would now love to implement this in our code.
In addition to the 2 measurements we had before, red and green,
I'm going to give you 2 motions--1 and 1,
which means the robot moves right and right again.
Can you compute the posterior distribution if the robot first senses red,
then moves right by 1, then senses green, then moves right again?
Let's start with a uniform prior distribution.

47 - Sense and Move Solution
============================
Here's the routine. It's very short.
It goes through the measurements. It assumes it has as many motions as measurements.
It first applies the measurement as before. Then it applies the motion.
When it's done with it, it prints the output, and the output is interesting.
The world has a green, a red, a red, and a green, and a green field.
The robot saw red, followed by a right motion, and green.
That suggests that it probably started
with with the highest likelihood in grid cell number 3,
which is the right-most of the two red cells.
It saw red correctly. It then moved to the right by 1.
It saw green correctly, moved right again.
It now finds itself most likely in the right-most cell.
This is just looking at these values over here without any probabilistic math
and any code limitation.
Let's look at the output--0.2, 0.1, 0.08, 0.16, 0.38.
Very correctly, then it would most likely assign this position to the right-most cell
as should be, given the sequence of observations over here.

48 - Sense and Move 2
=====================
Let's pick a different base.
Let's assume the robot saw red twice.
It senses red, it moves, it senses red, it moves again.
What is the most likely cell?

49 - Sense and Move 2 Solution
==============================
Let's run the program, and we find that the most likely cell is the 4th cell.
That makes sense, because the best match of red, red to the world
is red over here and red over here.
After seeing the 2nd red, the robot still moved 1 to the right
and finds itself in the 4th cell as shown over here.
Now I want to celebrate with you the code that you just wrote,
which is a piece of software that implements
the essence of Google's self-driving car's localization approach.
As I said in the beginning, it's absolutely crucial that the car knows
exactly where it is relative to the map of its road.
While the road isn't painted green and red, the road has lane markers.
Instead of those green and red cells over here,
we plug in the color of the lane markings relative to the color of the pavement.
It isn't just one observation per time step, it's an entire field of observations,
an entire camera image,
but you can do the same with a camera image
as long as you can correspond a camera image in your model
with a camera image in your measurements.
Then a piece of code not much more difficult than what you coded yourself
is responsible for localizing the Google self-driving car.
You just implemented a major, major function that makes Google's car drive itself.
I think you should be really happy and proud of yourself.
You should say to yourself, I just implemented localization.
Now why on earth did it take Google that long to build a product that drives itself.
Well, the truth is the situation is a little more difficult.
Sometimes road get paved over and changed, and we're working on this.
But what you've implemented is the core of Google's self-driving car localization idea.
Let me just summarize the essential things we've learned.

50 - Localization Summary
=========================
We learned that localization maintains a function over all
possible places where a road might be,
where each cell has an associated probability value.
The measurement update function, or "sense," is nothing else but a product
in which we take those probability values and multiply them up or down
depending on the exact measurement.
Because the product might violate the fact that probabilities add up to 1,
there was a product followed by normalization.
Motion was a convolution.
This word itself might sound cryptic, but what it really means is
for each possible location after the motion, we reverse engineered the situation
and guessed where the world might have come from
and then collected, we added, the corresponding probabilities.
Something as simple as multiplication and addition solves all of localization
and is the foundation for autonomous driving.
I want to spend a few minutes and go over the formal definition of localization.
I'm going to introduce probability and ask you lots of questions.

51 - Formal Definition of Probability 1
=======================================
Formally, we define a probability function to be P(X),
and it's a value that is bounded below and above by 0 and 1.
X often can take multiple values.
We had the case of 5 grid cells.
Suppose it can only take 2 values--there's only 2 grid cells, x1 and x2.
If the probability for x1 is 0.2, what would be the probability for x2?
Please enter the number. It's a quiz, obviously.

52 - Formal Definition of Probability 1 Solution
================================================
The answer is 0.8. The reason being that probabilities always add up to 1.

53 - Formal Definition of Probability 2
=======================================
Let me ask a second question, and I know that's not particularly difficult.
What if P(X1) = 0?

54 - Formal Definition of Probability 2 Solution
================================================
The answer is 1. You got it.

55 - Formal Definition of Probability 3
=======================================
For our world with 5 different grid cells,
suppose we know that the first 4 of them have a 0.1 probability.
What would be the probability of the 5th and final grid cell?

56 - Formal Definition of Probability 3 Solution
================================================
The answer is 0.6.
They have to add up to 1.
We subtract 4 x 0.1, which is 0.4, which is 0.6.
That's a valid probability.

57 - Bayes' Rule
================
Let's look into measurements, and they will lead to something called "Bayes Rule."
You might have heard about Bayes Rule before.
It's the most fundamental consideration in probabilistic inference,
but the basic rule is really, really simple.
Suppose x is my grid cell and Z is my measurement.
Then the measurement update seeks to calculate a belief over my location
after seeing the measurement.
How is this computed?
Well, it was really easy to compute in our localization example.
Now I'm going to make it a little bit more formal.
It turns out that Bayes Rule looks like this.
That will likely be a little bit confusing,
but what it does is it takes my prior distribution, P(X),
and multiplies in the chances of seeing a red or green tile for every possible location
and out comes, if you just look at the denominator here,
the non-normalized posterior distribution we had before.
Recognize this? This was our prior. This was our measurement probability.
If we do this for all the grid cells, so we put a little index "i" over here,
then just the product of the prior of the grid cell times the measurement probability,
which was large if the measurement corresponded to the correct color
and small if it corresponded to a false color.
That product gave us the non-normalized posterior distribution for the grid cell.
You remember this because that's what you programmed.
You programmed a product between the prior probability distribution and a number.
The normalization is now the constant over here--p(Z).
Technically, that is the probability of seeing a measurement devoid of any location information.
But let's not confuse ourselves.
The easiest way to understand what's going on is to realize that
this is a function here that assigns to each grid cell a number,
and the p(Z) doesn't have the grid cell as an index.
No matter what grid cell we consider, the p(Z) is the same.
Here's the trick.
No matter what p(Z) is, because the final posterior has to be a probability distribution,
by normalizing these non-normalized products over here,
we will exactly calculate p(Z).
Put differently, p(Z) is the sum over all i of just this product over here.
This makes Bayes Rule really simple.
It's a product of our prior distribution with a measurement probability,
which we know to be large if the color is correct and small otherwise.
We do this and assign it to a so-called non-normalized probability,
which I'll do with a little bar over the p.
Then I compute the normalizer, which I'LL call "α," is the sum of all these guys over here.
Then I just normalize.
My resulting probability will be 1/α of the non-normalized probability.
This is exactly what we did, and this is exactly Bayes Rule.

58 - Cancer Test
================
Let me ask you Bayes Rule in the context of a completely different example
to see if you understand how to apply Bayes Rule.
This time it's about cancer testing.
It is an example that is commonly studied in statistics classes.
Suppose there exists a certain type of cancer,
but the cancer is rare--only 1 in a 1000 people has the cancer--
where as 999 in 1000 people don't have it,
illustrated by the probability of cancer and the probability of not cancer.
Suppose we have a test, and the test can come out positive or negative.
The probability that the test triggers positive if you have cancer is 0.8,
and the probability that the test comes out positive given that I'm cancer free is only 0.1.
Clearly the test has a strong correlation to whether I have cancer.
Here's a really difficult question.
Can you compute for me the probability of cancer given that I just received a positive test.
Let me emphasize this is not an easy question, but you should be able,
based on what I've taught you, to calculate this result.
Think of the cancer/non cancer as the robot position
and think of the positive as whether the colored door observed is the correct one.

59 - Cancer Test Solution
=========================
And the answer is 0.0079.
In other words, there's only 0.79% chance,
0.79 out of 100 that, despite the positive test result,
that you have cancer. And we're going to apply
the exact same mechanics as we did before.
The result of Bayes Rule, non-normalized of C given POS
is simply the product of my prior probability, 0.001 times 0.8,
which is the probability of a positive result in the cancer state.
And that ends up to be 0.0008.
The non-normalized probability for the opposite event,
the non-cancerous event, given a positive test,
is 0.999 times 0.1. And that's obviously 0.0999.
Our normalizer is the sum of both of those, which is 0.1007
just add these two values up over here.
So dividing 0.0008, the non-normalized probability,
by 0.1007 gives us 0.0079.
We just applied Bayes Rule to compute a really involved
probability of having cancer after seeing a test result.

60 - Theorem of Total Probability
=================================
Let's look at motion, which will turn out to be something we will call total probability.
You remember that we cared about a grid cell "xi,"
and we asked what is the chance of being in xi after robot motion?
Now, to indicate the after and before, let me add a time index.
T up here, is an index for time.
I write it superscript so there is no confusion with the index i, which is the grid cell.
You might remember the way we computed this
was by looking at all the grid cells the robot could have come from on time step earlier--
indexed here by j.
We looked at the prior probability of those grid cells at time t - 1.
We multiply with the probability that our motion command would carry us from xj to xi.
This is written as a condition distribution as follows.
This was exactly what we implemented.
If there was our grid cells over here
and we asked one time step later about a specific grid cell over here,
we would combine 0.8 from over here, 0.1 from over here, and 0.1 from over here
into the probability of this grid cell.
It's the same formula as here.
This is now xi, and the way we find the posterior probability for xi is to go through
all possible places from which we could have come, all the different j's.
Look at the prior probabilities, multiply it by the probability that I transition from j to i
given my motion command, which in this case is go 1 to the right side.
Now in probability terms, people often write it as follows:
P(A) = Ʃ p(A│B) p(B).
This is just the way you'd find it in text books,
and you can see directly the correspondence of A as a place i of time t
and all the different Bs as the possible prior locations.
That is often called the Theorem of Total Probability.
The operation of a weighted sum over other variables is often called a "convolution."

61 - Coin Flip Quiz
===================
Let me test total probability in a quiz.
Suppose I flip a coin, and the coin comes up tails or heads.
Suppose it's a fair coin.
The probability of tails or of heads is both 1/2.
Now let's say that the coin comes up tails, and I just accept and don't do anything.
But suppose it comes up heads, and I flip it again,
and after 1 flip, I accept the result.
My quiz for you is what is the probability that the final result is heads?
That's an example of total probability.

62 - Coin Flip Quiz Solution
============================
The answer is 1/4. It's easy to see that the probability of heads in step 2
is the probability of heads in step 2 conditioned on heads in step 1
times probability of heads in 1
plus, that's the sum, probability of heads in step 2
given we had tails in step 1 times probability of tails in step 1.
Now, the way I set it up, those things here are equally likely.
However, if we did have tails in step 1,
we would never toss the coin again and just accept it.
It's impossible that in step 2 I flip over the heads. It's probability zero.
Whereas if I found heads, I would flip again and then the 0.5 chance I arrive at heads.
If I look at this, then this all becomes zero,
and these guys multiply to 1/4, and the final answer is 1/4.

63 - Two Coin Quiz
==================
Let me make a final quiz in which I have a coin which probability I don't know.
There are multiple coins. One is fair and one is loaded.
The fair coin has a probability of heads of 0.5.
The loaded coin has a probability of heads of 0.1.
Here's what I'm going to do. I'm going to grab a random coin with 50% chance.
The fair coin will be chosen with 50% chance,
and the loaded coin will be chosen with 50% chance,
but I don't know which one it is.
I flip it and I observe heads.
What's the probability that the coin I hold in my hand is fair?
Apply anything you've learned before--
one of the rules you've learned before is exactly the right one to apply here.

64 - Two Coin Quiz Solution
===========================
Let's work this out.
What I'm really asking you is the probability of a fair coin "f" given that I observed H.
This has nothing to do with total probability
and all with Bayes Rules, because I'm talking about observations.
The non-normalized probability according to Bayes Rule is obtained as follows:
the probability of observing H for the fair coin is 0.5,
and the probability of having grabbed the fair coin is 0.5 as well.
The non-normalized probability of not F given H, which is the loaded coin,
is probability of H given not f,
which we know to be 0.1--that's the one over here--
times the probability of not picking the fair coin, which is 0.5,
ends up to be 0.05.
When we now normalize, we α = 0.25 + 0.05, which is 0.3.
If we now normalize the 0.25 over here with the 0.3, we get 0.833,
which is the same as 5/6.
That's our posterior probability we hold the fair coin after we observed H.


Terms
=====

* Monte Carlo Robot Localization
* Grid Based Localization
* Histogram Filters


Resources
=========

* http://www.deepideas.net/robot-localization-histogram-filter/

