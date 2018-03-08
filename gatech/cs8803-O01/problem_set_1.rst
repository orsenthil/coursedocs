1 - Probability
===============
So welcome to our very first homework assignment.
This is number 1. [Homework Assignment #1]
Just to recap, in the class we learned about localization. [Localization]
We learned about about histogram filters. [Histogram filters]
And we programmed some in Python. [Python]
So the homework assignment will cover this plus some very basic probability. [Probability]
[Question 1] In the first question, I'm going to ask you some very basic probability questions.
We have random variable X and the probability of 0.2.
What's the probability of the complement?
We have 2 random variables, X and Y, whose probability individually is 0.2.
And X and Y are independent. [X, Y independent]
What's the probability of the joint X, Y?
And we have the variable P(X) with probability of 0.2,
and we have 2 conditionals, P(Y|X) and P(Y|¬X), both 0.6.
What's the probability of Y?
Here you have to apply total probability.

2 - Probability Solution
========================
[Question 1] The correct answer in the first case is 0.8.
This is just 1 minus 0.2.
If X and Y are independent, then we just take the product of those 2 things, which is 0.04.
And in the last case, it turns out X and Y are independent but just by a coincidence
because the probability of Y is independent of what X says,
and therefore, the outcome is 0.6.
Put differently no what matter value X assumes, whether it's X or not X,
Y is always 0.6 probability so it must be that P(Y) is 0.6.
You can actually compute this using total probability
where P(Y) equals P(Y|X) times P(X) plus P(Y|¬X) times (P¬X).
When you plug in the numbers, you get 0.6 times 0.2 over here;
0.6 times 0.8 over here, the complement of 0.2.
And if you regroup this, or you put the 0.2 and the 0.8 together into one,
you end up with 0.6.

3 - Localization
================
Let me ask you a localization question.
You remember a robot operating in a plane environment has usually 3 coordinates.
It has an x-coordinate, a y-coordinate, and a heading direction--often called orientation.
Now, flying robots have more coordinates.
If you can orient the robot fully in free space then you have an x, y, and z,
and you also happen to have 3 rotation angles--
often called roll, pitch, and yaw.
If you built a localization system for robots with higher dimensional state spaces,
I wonder how the memory used will scale
for our histogram-based localization method.
Does memory scale linearly, quadratically, exponentially, or none of the above
in the number of state variables used in localization?
Again, for a robot operating on a plane, there will be three of them.
So the number of state variables will be three.
If you were to look at a flying robot where you have x, y, z, roll, pitch, and yaw,
You would get six such variables,
and I wonder how the memory use of the basic histogram localization scales.
Please check exactly one of those four boxes over here.

4 - Localization Solution
=========================
The answer is exponential.
Suppose we resolve each variable at a granularity of 20 different values,
so there's 20 different values for x and 20 for y and 20 for θ.
Then the joint table over all of those will be 20^N
where N is the number of state dimensions.
That's an exponential expression.
There is unfortunately no easy way around it.
The biggest disadvantage of the grid-based localization method
or the histogram method is that the scale of memory is exponential,
which means it's not applicable to even problems with 6 dimensions,
because you can't really allocate memory for 6 dimensions.

5 - Bayes' Rule
===============
I'm now going to quiz you on Bayes Rule.
Say you own a house, and you know that the house might catch fire in your absence,
but the probability of it catching fire--"f" over here--is small.
It's a 10th of a percent--0.001.
Let's say every afternoon you talk to your neighbor, and every afternoon
you ask your neighbor, "Does my house burn?"
Of course,you a little bit paranoid if you do this, but for the sake of the argument,
let's just assume you do this every afternoon.
This afternoon he comes back and says, "Yes, it burns," so B.
You happen to know that the neighbor is not very truthful.
In fact, every time you ask him a question,
you know there is a 0.1 chance--a 10% chance--the neighbor will just produce a lie
and a 0.9 chance the neighbor actually speaks the truth.
So you ask him exactly one question--"Does my house burn?"
He says, "Yes, it burns," but you know that the probability of this being a lie is 0.1.
So in applying Bayes Rule I like to first compute the non-normalized posterior--p bar--
bar now stands for non-normalized--of fire given the neighbor just called.
The same for the opposite event of no fire given the neighbor just said, yes, it burns.
After you've done this, I'd like you to compute the normalized values
that have to add up to 1.
Please enter all 4 values for this homework assignment.

6 - Bayes' Rule Solution
========================
Here are my answers.
The prior for fire is 0.001
times the probability that the neighbor now correctly said, yes, it burns, which is 0.9.
He lies with a probability of 0.1, so the complement is 0.9.
This gives us 0.0009.
For the complement, the prior of no fire, is 0.999,
but now the neighbor would have lied, which multiplies with 0.1,
which gives us 0.0999.
Now, these two values don't add up to 1.
The normalizer will be 1 over these two things, which is about 9.92.
Multiplying these with their normalizer gives us approximately 0.0089 and 0.991.
So the answer your neighbor gave you--yes, it burns--
raised your probability from 0.001 to 0.0089.
It's still small, but it's significantly larger.
In fact, it's approximately 0.9 times as large as the initial probability.
The reason why that is the case is it relates to the 0.9 probability of speaking the truth.
It's not exactly 0.9 because of normalization, but it's approximately 0.9.

7 - Localization Program
========================
This is our first programming assignment.
In class, we localized the robot in a 1D world
with a number of grid cells where each grid cell could have a different color,
and the measurement vector was a sequence of observations.
Our world was cyclic--if you fell off one end you would continue at the other end.
In this assignment, I want you to do the same for 2D roles of arbitrary dimension.
Just as before, begin with a uniform distribution as you always do in global localization.
Then we have a number of motion commands--[0, 0] is no move,
[0, 1] means you move to the right, [0, -1] means move left,
[1, 0] makes you move down, not up, and [-1, 0] makes you move up.
Again, the world shall be cyclic.
If you fall off one end, like over here, we continue at the other end, like the one over here.
Here is a simple example of the type code I give to you as a specification of the problem,
and then you have to compute what my code computes but that it can't see right now.
The world in this specific instance is a 3 x 3 matrix--3 row and 3 columns.
It has only 2 possible colors, green or red,
and this specific world has only a single red at the center location over here.
We have a motion vector and a measurement vector.
We start with a motion.
This one says stay in place, and this was says we're going to observe red.
Additionally, I give you two more variables called "sensor_right" and "p_move."
Sensor_right is the probability that the sensor measurement is correct.
In this specific instance, I set it to zero, which means the sensor value is always correct.
P-move tells you at what probability the motion is executed correctly.
Right now it's 1.0. It's always correct.
If it's a smaller value, then the motion might fail,
and when it fails, our robot won't move at all.
Let's execute this.
Here we didn't move, we observed red, and we had a noise-free sensor.
As a result, we get a matrix that says zero everywhere
except it's a 1 at the center location that has a red color.
Let's modify the world.
Let's make this grid cell red over here as well.
Then now let's just rerun the code.
What we get is a matrix just like the previous one,
but now we have winning grid cells, both of which have a 0.5 probability
so that all the probabilities add up to 1.
Let's now model a noisy sensor
and set sensor_right to 0.8.
Your code should now computer the following:
a 0.06 for almost all grid cells except the two winning ones,
which come in at 0.26 and 0.26 each.
Check that your code does this.
Let's now bring in some motion.
After not moving at all, I assume we're going to move 1 to the right,
and we always have to have as many measurements as motions.
So let me add a second measurement.
Let's say we sense red again.
Intuitively, this lands us in the square over here. Why?
Well, we didn't move in the beginning, we saw red--
there's two possibilities--but now we move again to the right side.
We see red again. That makes this cell over here the most likely.
Let's just check, and as predicted, almost all cells have a probability of 0.03.
Some have 0.13, but the one over here has a probability of 0.533.
If we set our sensor probability to 1.0, that is no sensor noise,
we get back this array over here, which assigns all probability to the rightmost cell.
Finally, I want to show you what happens if you modify the move variable.
Say our motion succeeds only with 0.5 probability
and with the remaining 0.5 we remained at the same location.
This doesn't affect the first motion command,
because success and failure is the same thing here. We don't move.
But with this one over here there is a 50% chance of moving
and a 50% chance of staying at the same location.
Let's run the code. Here is our posterior probability.1
The cell on the right still wins, but now with a smaller total probability of just 0.46.
If we now assume perfect sensors, by setting sensor_right to 1.0
we get this thing over here.
We have 0.66 chance associated with the right cell over here
and a 0.33 with the possibility that we moved this specific red here twice
by just not moving in between.
Check your code to make sure it gives you the exact same operative result.
Finally, I want your code to execute input as complex as this one.
This is a 4 x 5 world--4 rows and 5 columns, all with reds or greens.
There's only two colors.
There's a sequence of measurements of 5 elements and, correspondingly,
a sequence of motions of 5 elements.
All the measurements are green.
The motions don't move at all, move right, move down, move down, and move right again.
Then there are certain sensor probability and motion probabilities that I set at will.
I set it to 0.7 and 0.8 over here.
Now, if we look at the sequence, green, green, green, green, green,
we first don't move at all, then move right, down, down, and right,
you find that the most likely match in this world is we first sense this green over here.
We then moved right to this green.
We moved then down to this green, further down to this green, and right to this green.
This would be the cell with the largest posterior probability.
It is the 3rd row and the 4th column.
Let's run it.
And here is the result.
It's somewhat illegible, and I apologize for the poor formatting of my Python routine.
But if you look at these probabilities--0.011, 0.024, and so on--
you'll find that indeed the largest element is the one over here--0.3535.
And it's our 3rd row and our 4th column gives me this large probability.
I want your code to produce numbers just like those,
and we'll check that you got the code correctly.
In summary, read your colors, build a probability distribution of the same dimensions--
in this case 4 x 5--
Initialize distribution, execute a motion first, then measurement, motion, measurement,
motion, measurement, motion, measurement, and so on.
You can safely assume that the measurement vector is of the same length as the motion vector,
using the measurement correctness probability and motion success probability,
and then compute an output of just the final distribution.
If you've done this, you'll succeed.

8 - Localization Program Solution
=================================
Here is my solution to the programming assignment,
and it's quite straightforward given the class, but I'm really proud if you go it correct,
because it enabled you to program your own localization algorithm
very similar to the way we do it at the Google self-driving car.
First, I did two simple bookkeeping assignments.
I assigned a value to sensor_wrong as 1.0 minus the probability of sensor_right
and a probability of staying--that is, a motion failure--
as 1.0 minus the probability of p_move.
Let me scroll down very slowly.
Let me first go to my main routine.
I actually put a little check where the length of the measurements vector
is the same as the motions vector, and it would give me an error message if not.
Of course, this wasn't necessary for you.
I just did it because I want my software to look nice.
Then here is my initialization of my probability table.
I compute my initial uniform distribution by calculating the size of the array--
the number of rows times the number columns--
and then dividing 1.0 over the product of those
to be my initial distribution value.
This thing over here just builds up an array of the size of my colors array
but initializes it with the value of "pinit."
These two lines over here give me an initial uniform distribution, and then I iterate.
I go through the number of measurements, which is the same as number of motions.
I move first using the "move" command of which I provide my current distribution
and my motions command to obtain a new distribution.
Then I do the same with the sensing command.
I take my current distribution, the world itself, and the measurement vector
to obtain a new probability distribution.
When I've done this as many time as I have measurements and motions,
I output the final distribution.
So much for the main routine.
I now have to specify what move is and what sense is.
Let me start with sense.
This is my sense routine. It goes from here to down here.
As an input, I have a probability distribution and my world map--
they're both of the same size--and a specific measurement, which is either red or green.
I construct and cite my new posterior distribution.
I initialize this with zeros, and I set the same size as my vector p.
In the inner loop, I now iterate over all elements in my grid cell.
I compute whether the measurement matches the color in the cell,
in which case I call it a hit.
Now my non-normalized posterior is the prior times this big sum over here.
It uses sensor_right if the measurement was correct
and sensor_wrong if the measurement was incorrect.
Finally, I add up all the values in aux--I do this with the variable "s."
Down here, I can normalize aux to have a total probability of 1, and then I return it.
The "move" command takes as an input a distribution and a motion vector.
It constructs the next distribution just like before as aux variable and sets it to zero.
Now I go through each grid cell and for each cell, I collect possible cells
that the robot might have come from.
With probability p_move, it actually moved,
in which case its prior coordinate would've been i minus the motion command.
That's because you go backwards in time.
This is a truncation, indicating we have a cyclic array,
and we do the same with j--let me scroll very carefully.
It's j minus the motion command, again in a cyclic fashion.
But it might've been we didn't move, in which case you just use the probability
of that specific cell multiplied by the probability of staying.
Now, this line together gives me the correct probability for the variable i and j.
I don't have to normalize, because it's not Bayes Rule.
I just return the corresponding posterior distribution.
I also have a little routine called "show" that goes through the entire probability field
and computes out all these probability vectors of p
that makes it slightly better formatted than just printing p in a single command.
If I run my software with a specific word over here,
it initializes p as 1/20 because there are 20 grid cells,
then runs 5 times through the motion command and the measurement command,
updates those, and then shows me the final result,
which I already explained, which is the array over here.
If you got this correct, then you've done something quite amazing.
You've programmed the core of Google's self-driving car localization methods.
In Google's case, the world isn't as simple as just red and green.
In Google's case, these are carefully assembled 2D surface models of the road surface.
But that doesn't affect what we've programed here.
It makes the measurement function slightly more involved.
The fact is that the thing we programmed here captures the key
of the probabilistic inference necessary to localize the Google care.
If you programmed this, you just have to replace the simple matching
of a measurement of green with an image matching of an entire imagery record
with imagery map.
I leave this as an exercise, because I can't do this in this Python environment here.
But I congratulate you that you really managed to do something quite amazing,
which is build an amazing piece of localization software.

9 - Congratulations
===================
Congratulations. You made it through homework assignment number 1.
You learned about Monte Carlo robot localization
with a technique that I often call histogram filters.
You've implemented it successfully and learned a lot about statistics.
This is all just a single class. Congratulations. That's really awesome.
Now, next week we talk about common filters and tracking other cards in traffic,
and you're going to implement our common filter, so I'll see you in the next class.

