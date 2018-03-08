1 - Matrix Fill In
==================
[Narrator] Hi class, this is homework assignment #6 on SLAM,
and we're going to practice some more questions about the graph SLAM algorithm,
and I will ask you something new about how to make graph SLAM more efficient
towards the end of this homework assignment.
There's 3 questions and 1 new thing,
which comes with additional questions and a programming assignment.
Let's dive in.
In this example, picture a robot that starts at initial position 5.
This robot which lives in 1D, even though I'm drawing this in 2D,
sees a landmark with a relative measurement of 2.
It then moves to coordinate X1 by taking a step of 7.
It now sees a different landmark, L1, with a measurement value of 4.
Finally, it moves again with a motion 2,
and now it sees the same second landmark, not the original one,at a value of 2.
Obviously, when I work it out and solve this,
you find that the best coordinates over here are 12 and 14,
with landmark coordinates of 7 and 16,
but none of the numbers I just told you will be inserted in the question I'm about to ask.
Picture the matrix omega and the vector C.
I want you to add all these constraints into omega
with a caveat that for the initial constraint I assume the strength is just 1,
so enter it the way you're used to.
Now let's assume the motion update has a sigma of 1,
but the measurement update--the sigma for measurements has a value of 0.5,
and remember we weigh those updates with 1 over sigma,
which in the measurement case would therefore be 2.
I want you to fill in the values for sigma and for C for this specific example.
I gave you some of the sigma values and some of the C values,
and I want you to fill in the missing values over here.
You can check whether you got them correct by verifying that I got those numbers correct,
and you can also solve for omega minus 1 times C,
and out should come the right positions shown in the diagram over here.

2 - Matrix Fill In Solution
===========================
So here is the answer, I feed in all the missing
values for you. And let’s try to check a few.
For example, let’s take the elements related to
X1. We move from X0 to X1 which added one
of the remainder indiscernible . We move
from X1 to X2, which added another one, so
we have two, but we also had one observation
in X1, we incremented by two because of the
measurement string, 0.5. One over that is 2
so when we added the measurement end up
with 4. Let’s pick this off tagging element over
here. This was only affected when moving from
X1 to X2 and it was a minus 1. This element
over here was affected when we sensed L1 from
X1 and again the off tagging element is
negative. So we added minus 2 over here.
It’s quite involved, as you can see. Let’s
take a number on the right side, the minus 2
over here. This is adding up a re-contribution
to X2. The first one occurred when we moved
into X2 from X1 at which point we added two
. But in X2 we also measure length by L1 with
a measurement value of two. We have to multiply
that for a two to arrive at four and subtract it,
so we have made minus four, you get
the minus two. If you work out at all these
examples, using the math we explained in class
and working in the effective measurements get
a default effect of two for every value you add,
you arrive at exactly this matrix over
here. I hope you got a good number
of numbers right that was not an easy task.

3 - Online SLAM
===============
[Narrator] I now want to ask you the really challenging question over here,
and it goes as follows: one of the weaknesses of slam is
as we move along and map a world by seeing these landmarks,
the matrix omega which is the big thing here and of course the vector C
grow linearly with the length of the path.
Now this means if you go to your local supermarket and buy a robot,
and that robot lives for a long time, say a year or a decade,
then this thing here, the path will be a really, really large even though the environment
in which it might operate, the map might be of a fixed size,
and that means a robot programmed by graph SLAM
will eventually stop working because it gets slower and slower.
Now, we all know computer operating systems that have that property.
The older they are the slower they are, but we're not talking about how to fix operating systems.
We're just talking about how to fix SLAM.
The crucial idea that I want to tell you about and I want you to implement from scratch in our software
is the following: we can actually reduce the map we maintain
to one that only contains the most recent position in the path,
and all of the stuff over here can be safely erased when we build our map.
You don't know how to do it, but let me tell you.
Suppose we have a robot position and we have a matrix omega
that only contains the information pertaining to 1 position.
If the position is 1 dimensional, it's just 1 row and 1 column.
Whereas, you might have many different entries for the map.
Suppose the robot moves to a new position; let's call it XT+1.
Then, we'd do exactly the following: we'd grow the matrix in the vector
by using the expand function that you're already familiar with
such that we now have space for our new position.
The new area we added are these rows over here.
It's a single row of numbers of a position 1 dimensional.
It's 2 rows of number of a position that is 2 dimensional,
and it's this column, again, is just a single column if our position is 1 dimensional;
otherwise, it is 2 column, and we initialize those all by 0,
and then we can apply our regular motion update,
that as you know adds 1 or some number like 1 to the main diagonal
and -1s off diagonal, and the same on the right side for the vector C.
That is just a motion update but that runs the risk that our path increases.
Now we go back to a form like this.
We make X2+1 survive.
Simplified speaking, you might think about doing this by just cutting out the new sub-matrix that starts over here,
and the sub-vector that starts over here; however, if you do this
as you can easily verify, that sub-matrix doesn't give you the correct answer,
and here is where the meat is.
We now cut out 3 sub-matrices or values from the full matrix on the right side.
One sits here, that one I will call A.
One is over here; it's a single element for a 1D robot,
but is a 2 x 2 matrix for a robot in 2D coordinates,
and one that I'll call C, and it's obvious to see that this thing over here
that you want to cut out is called A-1.
These values carry a lot of importance.
We can't just erase them, but we can forward them back into the surviving matrix
by the following simple operation:
we take the surviving matrix to be called omega prime
and the surviving vector to be called X prime,
and you can get omega prime and X prime by using the function take that is in your own matrix library.
You have to look into how to make take take exactly those elements over here,
and then if we modify X prime and C prime with the following piece of math.
We subtract from omega prime A transpose times B to the -1, the inverse, times A.
If we implement this correctly this gives you a matrix of the same size as sigma prime,
and that's what you subtract to arrive at our reduced sigma.
Similarly you do the same for C.
You subtract A prime minus B to the -1 times C.
This tends to be the same as Gaussian where we technically do away
or we call it integrate away the variable X1,
and I don't want to go into detail why that's correct.
My book has a multi-page proof of that simple equation.
I just want to give you intuition here, which is these values do carry importance,
and to get rid of those you have to redistribute them into the remaining variables
and that over here happens to be the math.
It's A transpose times B times A that you subtract from the remaining omega prime,
and the same for C over here.
When you do this, you are now left with a matrix of the same original dimension
because we first added the post and then we subtracted one,
and as you can see when you do this many, many times
the final dimension of the matrix is only determined based on the size of the map
plus, well, a single entry which in the 1D case is 1 row and 1 column.
In the 2D case is 2 of those corresponding to the robot position.
That means SLAM scales to really large environments
because we can do the trick every single time a robot moves.
You asked for a challenging program assignment.
I promise you, you will be busy with it for awhile.
I'm giving you now my piece of code in which I implemented SLAM for you.
You're familiar with this.
You have all of that, and then I run SLAM with 3 landmarks,
3 time steps, a world size of 100, and a measurement range of 100.
I make data at random as you're familiar with and you'll complete the result,
and the result in this case contains a vector of omega C and U concatenated.
Then what I might get out looks as follows:
there's 3 landmarks.
There's a sequence of estimated positions leading up to the actual robot position.
They're both correct, and then there's estimates for where landmarks are.
Every time I run it, I get a different answer because my landmarks and my world is different every time.
Now I also implemented and that's your task now
a function called online SLAM.
It does exactly what I told you to do.
It resizes the matrix every time a new motion occurs
and then goes back to the original size,
and I've printed out here as an example the information matrix omega
and in the vector C that I obtained, and I also printed out the final result.
In the final result, we get exactly the same estimated pose as for the full SLAM algorithm
which is 86.0 and 33.7.
I go down, these are exactly the same number for the estimated pose; that's how you can verify this.
The same is true for the estimated landmark.
Those coordinates are identical despite the fact that I reduce the size of omega and C,
but when I print omega and C, we find that the dimensionality is reduced.
It's an 8 x 8 matrix omega, and the number 8 comes because there's 6 coordinates for the landmarks and 1 final robot pose.
That is substantially smaller than the matrix I would obtain
for the full SLAM case, and the same is true for the information vector of size 8; here's an example.
What you are asked to do is to fill the entire online SLAM routine and to do this,
every time you get a new pose, you want to expand to grow the matrix by inserting something right behind the existing pose.
You then run take to take out the sub-matrix.
You also calculate A, B, and for the information vector C,
and then as before your reduced omega is obtained with this equation,
and your reduced C is obtained with this equation.
If you make no mistake, then you get exactly the same area as you had before,
and you can test your routine and arbitrary maps and arbitrary data sets,
and it'll just be fine.
So, good luck; this is a wonderful programming assignment
because it gives you the first really scalable SLAM algorithm
and when you implement it, it's actually a major achievement.
I can tell you it took the scientific feat of SLAM easily 15 years to really discover this form,
and ever since what was really complex and involved lots of common failures,
and I can tell you lots of headaches, became amazingly easy.
So, implement it and you can call yourself a robotic mapper.

4 - Online SLAM Solution
========================
So here is my solution to the programming
assignment where I asked you to program an
online version of online SLAM. Let me run it
and compare it to the offline SLAM. When
I run it, I get random landmarks and a random
initial robot pose. My offline solution gives me
this long path over here and estimated landmarks,
and the remarkable thing here is that my online
version that I coded gives me the same final pose
and the same landmarks without retaining this huge
matrix for the path before. So how did I do this?
Here is my online SLAM routine. In large parts
it looks exactly like my offline SLAM routine.
I do it in 2D  I have a measurement and motion.
Step, here is my measurement update. I have to
get all these indices right so you can stare at
them for a while, but theyre all correct here,
there is a plus one and minus one over here.
And here is the first nontrivial thing. My
matrix so far has one robot pose and one
entry for each landmark, but now I need to
add space for the next robot pose. And the
way I do this is, I make an expansion list
using the expand command. And this expansion
list retains the original robot pose, which is
coded 0 and 1, these are two-dimensional
poses, and indices for the landmarks.
So, Im squeezing in two new rows and two new
columns for the next robot pose. Thats
happening in this code over here. With this
squeezed in, I can now do the update. The
update is being applied exactly at these two
new rows and columns that I put in. And here
is the math I gave you for factorization applied
to this problem, where I go and compute the
intermediate matrices A, B and C that I
explained in class. And then I use the take
command to kick out the very first row and
column, the first two of them, to remove the
old robot pose, using the exact same logic
that I gave you in class. So you can look at
this, this actually implements online SLAM.
