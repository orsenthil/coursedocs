Image Transformations
---------------------

1 - Intro
=========

So far,
we have looked at a variety of ways,
how we are going to find information
in images, to do things like alignment.
Let's also step back a little bit and
now ask the question how does
image transformation happen?
How do we actually figure
out how to transform or
warp an image, translate it, rotate it.
Also, look for things like projective
and affine warps and transformations.
In this lecture, we're going to talk
about how we can do this mathematically.

2 - Lesson Objectives
=====================
The specific objectives
of this lesson are for
us to look at how are we
going to transform the image?
specifically transformations
like Rigid Transformations.
Specifically Translation and Rotation.
Again, the emphasis is that we
are trying to do now is look inside
the image but not at the intensities,
but the number of rows and columns.
The number of pixels in the image and
transform those.
An additional part of it, where we will
also look at non-rigid transformations,
where we would actually look at our
final projective transformations.
But more importantly, what we
want to do now is start looking at,
how many numbers, how many parameters,
degrees of freedom we
want to be able to model in mathematics
of how to do these transformations.
So, let's get started.

3 - Image Transformations
=========================
To help me situate this let's look
at image transformations in general.
So far we have looked
at image filtering.
Now what we're going to talk about is
image warping or image transformation.
So here basically assume
we have an image,
f, and what we're interested in doing
is some sort of a transformation.
So for example,
what we have looked at is we have
transformed this image to a new one,
and here, hopefully you can see that
this image is now much brighter.
If you remember where
we've looked at before,
one of the best ways of doing this would
be to look, loop over the entire image,
and look at each and every intensity,
and perhaps do some calculations to it.
In this one, I just added, let's say,
20 more intensity points to it.
Now of course this image is brighter.
Here now,
let's do another form of transformation
to get the output image g.
Here, if you notice what we've done,
is we've actually now
stretched out the image.
So if you look at this
number of columns here,
there are more number of columns here.
Of course, so
far the same number of rows.
So in essence,
we've changed the width of the image,
keeping the height the same.
So in the case of doing filtering, what
we're basically doing is we're changing
the range of the image, the inside
values of the function itself.
So basically to get the output image,
what we basically have done is done
put in a function and transformed the
function itself to get the new image.
In case of changing the size of
the image and such, what we're basically
changing is the number of things
like rows and columns, the insight.
Not the content, but the indexes
of the matrix that we're changing.
To do this, of course,
we basically are now growing
a transformation of the insides.
That is the width and the height and all
of the information associated with it.
And that's changing the function.
So the transformation of course in
this one image is the change of
domain of the image as opposed
to change of range of the image.
Those of you curious about these terms,
I encourage you to look back
to your old calculus or
algebra material on defining what is
a range and domain of a function.
And, of course,
here our function is always at image.

4 - Parametric Global Warping
=============================
So now my goal is to start
thinking about how we going to
warp an image to a different size.
This is a global transformation, or
a global warping, and to help us,
we will need to start looking at if we
can come up with a set of parameters
that on easy adjustment
of these parameters.
We can basically take
a set of equations and
generate a new output
from a given input.
So now we want to actually start looking
at how to get an output image G if
the F is given and we have a certain set
of parameters to do this transformation.
To help us, lets create just
a simple coordinate axis here.
Usually if you remember I always put
the coordinates axis going down in y and
x this way.
Just for simplicity and consistency.
I'm going to start using
the traditional set of axis here.
Of course this would be the x-axis,
the y-axis, and this would be the (o,o).
All right?
Let's find another coordinate frame.
And here, so
assuming this is again the (o,o) and
this is x and y, you notice this
image has been moved a little bit.
Let's claim that this
has been translated.
By tx, and ty.
The translation's in x and y.
So this in essence kind of says,
that now I've translated the image.
So this is basically, warping, or
transformation of translation.
Another similar example would be when
I actually take the image, again,
the x and y axis,
that we've been paying attention to.
Origin except that now we notice.
This image has been rotated.
And if you draw this axis here,
you might say that this has
been rotated by amount theta.
And that's rotation actually now means
that basically the same pixel values
that I have here, now appear in a
different setup, and of course, thinking
hard about it, you might also thinking,
this is basically, change the way.
Rows and columns look, and
how my pixel values are looking.
So this is basically looking
at simple rotations.
Let's look at a few additional examples
of this kind of, parametric warping or
transformation of images.
Again, my input image.
In this one I've stretched the image.
Right.
In essence,
what I've done is I've scaled it.
I've added basic additional
dimension in the.
X axis then I have here,
y in this one is of course the same.
Result in of course my vit is larger and
in this case the height is the same.
This basically where we just
change one scale parameter is
the change of the aspect of the image,
and of course we could do this in both
directions x and y, and of course that's
the change in the scale of the image.
Very simple stuff so far.
Another example where
a basically have the same image.
So this time around if you
notice that we've actually done
an interesting thing.
What we've done here is,
we've added a little bit of
perspective projector warp.
Now the top row is much top numbers or
top part is much smaller.
Bottom is larger, and
in essence, the image seems to have
flipped on that side a little bit.
This is, referred to as Perspective,
and this, of course,
is an example where we have created
an affine deformation of the image,
where basically now, the image seems
to have, kind of have a lot more sheer.
Again different types of warps
are transformation applied
to the same pixel values.
And of course as you noticed the domain,
the number, how the x and
y's change depend on how,
what kind of function we could apply.
So let's now talk about what kind
of functions we could apply.

5 - Parametric Global Warping Functions
=======================================
So now what we're interested in asking
the question, given an image like this,
how do we transform it
to an image like this?
Again, here I'm basically showing
a little bit of scaling
in one direction only.
Let's start off by basically finding
two points on my original image, f.
This is my original image f.
And I'm trying to get my output image g.
Here, I basically have two
points that I've kind of marked.
Of course, what we're now interested is
seeing where these two points would be
on this image.
Where would they transform to?
So, call this one P1.
And we call this image,
or point here, P2.
This P1 and P2 have now moved
to different points here.
So of course this is now
all these two points.
And just for sake of parity we
will call this P2 prime, and
then we will call this P1 prime.
In essence, now what we have to
figure out is how to transform
the point P to P prime.
So in essence, what we need now is the
simple function that takes any point,
P, of course in this case, in this case,
they would have values of x and
y to generate a new point, P prime.
In this case, we want to find one
function, T, which has a set of
parameters that actually applies this
thing entirely to the whole image.
So in this case,
I'm basically talking about one function
that directly applies to each and
every pixel.
This basically means that
this would be a global warp.
Every, the same function,
the same parameter function would
be applied to the entire image.
So in essence, what we're talking
about is ,a global function,
that given a P,
we would always get a P prime.
And just to reiterate,
what basically I'm talking about is,
I want to come up with a few
set of simple parameters.
So by now, you've noticed I like to
convert everything to matrices because
that's a great representation for
us to be playing around with.
And, of course, this is true here.
What we really want to
do is find a matrix
that encodes all of
the transformation or
the parameters, and then when applied
it to point p, and again, remember,
this would be just simple x and
y, to generate a new x and y.
Basically, this is the simple
two-dimensional transformation
we're looking at.
Given a matrix M, that has certain set
of parameters, when applied to point
x and y, any variable in this f
function, which is my first one,
I would get an output, g, which would
have all x primes, and y primes.
So, by just looking at this,
you may note that this M should be two,
a two by two matrix, and
now we, let's start to figure out what
would be in this two by two matrix.

6 - Image Scaling 2D
====================
First, let's look at the simple example
of scaling an image in two dimensions,
which basically means I
have an image here, and
I want to generate another image.
And in this case,
this image is twice as big.
Again, we have simple set of things here
in terms of how I want to get x prime
and y prime from x and y.
Now let's think about what
would be in the matrix M.
Basically, the way I want to do
scaling would be a simple, right?
I would just multiply each component
by a fixed scaler, and uniform scaling
would basically be when the same
scaler's applied to both x and y.
The difference, of course,
is if they're not the same,
you would get a different aspect ratio.
So let's say if I multiply the, all of
the x's by 1 I would get the same width.
But if I multiply all the y's by 2,
I would get a different height.
So though similarly, you know, that
different aspect ratio would come in.
So uniform scaling would only be when
I apply the same constant both ways.
If I apply different ones in x and
y directions,
that would actually allow me to
now have different aspect ratios.
So what does that mean in
terms of our matrix here?
Basically, that mean is now we would
replace the M matrix by nothing else but
two scalers on the diagonal, a, which
would actually impact the scaling in
the x direction, and b, which would
impact the scaling in the y direction.

7 - 2D Image Transformations
============================
Let's look at other 2D
image transformations.
Again, let's look at this simple
equation that we're looking at.
Let's say I create
the simple equation here,
which basically takes a scale in x and
y directions, Sx and Sy.
And basically what that means is
that this image now would be scaled.
But the parameters Sx and Sy and
they would of course be scaled around
the origin point of the image, 0 and 0.
I mean, there would be a linear
scaling in that direction.
Here is an interesting transformation,
M matrix.
What would happen when I applied this?
If you think about it,
basically what it's going to do,
it's going to flip
the image in one direction.
So basically, what it's going to do is,
when I have the y-axis going this way,
it's going to flip all of
the values on the, this side.
That is the right side of the image,
to the left and
all the left ones to the right.
So basically,
that'll be a mirror operation.
If I put minus 1 on both of them, that
would be a mirror over the origin, so
basically it will flip both an x,
axis and
the y-axis to generate
a mirror flipped image.
Here is another interesting one which
basically now I put the terms on the two
off diagonal terms, and
we would refer to this as shear, so
shear in x and shear in y would give
us and image that would be sheared.
That basically would kind of have
the impact of kind of having top row of
the image,
kind of move towards the left.
And, I'm sorry, top part of the image
moving towards to the right and
bottom moving to the left.
We'll show examples of that in a bit,
too.

8 - 2D Rotation
===============
What about rotation?
So here,
I'm basically showing a simple example.
I have two points, x and, this would
be the original points here, and
x prime, y prime, where I want
the transformation to happen.
Of course, in this case,
these two vectors kind of show how the
transformation would be, and of course,
there would be an angle
associated with this.
Let's call that theta.
So in case now,
just looking at the simple 2D example,
let me ask the question.
So in this case of the simple
2D rotation by a theta,
where I have transformed points x and
y to x prime, y prime.
Question comes up is, how would I now
figure out the values of x prime,
y prime, given x and
y and this angle theta?
Now, if you may remember this from
your old trigonometry classes,
this can be done, and I encourage you
to look it up again if you haven't,
looked at such things recently.
And this would basically say that x
prime would basically be computed by
taking the cosine of the angle
theta here, with x the original x,
minus y sine theta.
And similarly y prime would be given
by x sine theta plus y sine theta.
So this basically now gives us an input,
interesting way.
Now of course I can write
this in a matrix form,
which basically would
mean I would move x and
y into a column, which would now give
me the elements of the M matrix.
So M in this case would be cosine
theta minus sine theta, sine theta,
cosine theta.
And if of course,
knowing this angle I can apply
this as an image transformation.
Again, I encourage you to look this up
or try to kind of do the derivation.
Just as a hint, to do this derivation,
you'd also need to
represent this angle and
then basically come up with equations
to kind of compare all of these.

9 - 2D Linear Transformations
=============================
So, now we've looked at 2D
linear transformations.
Let's look at that in a little
bit of an interesting way.
Here's my equation.
We know how to look at that.
Of course we basically talked that
now a simple way to do would be is,
in this case,
I can come up with four parameters.
And sometimes, for example,
a could be the scale and y, and
d could be the scale.
The for example, the numbers
negative kind of give it a flip not.
And similarly, things like c and
b kind of give it the share information.
And again, mixtures of this with sines
and cosines tell us how to do rotations.
So one interesting to note is all
that this means is we are only
look at linear combinations
of these parameters to
generate a newer set of x and
ys, given an x and y.
So x and y, x prime, y prime
are computed knowing what x and y are,
and again if I know the parameters a,
b, c, d.
Let's look at some of the features or
the kind of the details of what
these types of things for y.
They can be used to
generate scaling of images,
rotation of images, shear and
of course also mirroring.
We've looked at all of them so far.
Now let's look at some properties
of these linear transformations.
One thing to note is all of the time
the origin still remains where it is at
0, 0.
We haven't actually done so
far any translation, for example, right?
I gave you this example of looking at
these matrices where we just played
around with how to change them to
do scaling, rotation, shear, scale.
We haven't actually done translation,
so origin remains where it is, always.
Second thing to note in all of this
would be that lines would actually
generate lines again.
So if the image had a line,
same straight line would actually be
generated in the new image,
even with scaling.
Of course, it might look different
in terms of it might be stretched
because we may have stretched
the image more in y and less in x or
something like that, or it might
get flipped when I do the mirror.
But, it still appear as a straight line.
All parallel lines,
because of the fact that everything
is straight line, will also appear.
As a parallel in the new image.
And all ratios would actually be
preserved, as much as possible,
in that image.

10 - 2D Translation
===================
So now let's actually
look at translation,
something I had ignored before.
This is the way, the best way,
I can actually translate an image or
pixel points on an image.
Right?
Take any x and y value, and
actually have to give a translation,
tx and ty.
This simple addition would actually give
me newer x and ys, x prime, y prime.
Notice that this matrix representation
does not allow me to reconstruct this.
Right?
Because in this matrix representation,
shown by this, when I do a multi,
a matrix multiply becomes ax plus by for
x prime.
X prime would basically
become ax plus by.
And similarly,
y prime would become cx plus dy.
Notice almost impossible in this linear
combination formulation that we've
looked at that we can generate
an equation that matches this.
In essence, these terms are additive.
As opposed,
these are linear combinations.
So then, question to all of you,
how do we resolve this?
How do we come up with a way,
in this form of a matrix representation,
that will allow us to encode
things like translation?

11 - Homogeneous Coordinates
============================
So the answer is that we need to
consider a newer coordinate frame and
we would refer to this as
the homogeneous coordinate system.
Basically what we want to do is
actually take the two dimensions
that we were looking at before,
the x, y, and
the x prime and the y prime,
and a two dimensional matrix M.
Let's start seeing if we can actually
represent this as a three vector.
So so far we've looked at x and y.
So we want to be able to take
this two dimensional x y and
generate a new three vector.
We can basically refer to this as x y
and the third vector being 1, and for
just sake of completeness and
what we will do with it
next let's call this a w.
So what we basically doing is
we adding a third coordinate to
every two dimensional point.
So and what we did basically is
now we're coming up with x, y, w.
And the thing we want to remember is
what basically w implies is again,
my two dimensional vector, except
that now we are dividing both x and
y with that third point here, w.
Now of course there are certain subtle
things we need to pay attention to.
Here for example is my simple
two dimensional x and y.
I can basically look at
this point here 2 and 1,
of course just looking at x 1,
y 1, the values would be 2 1.
Now just keeping this convention
in mind, if I had omega,
or w to be 1 this still makes
unreasonable sense 2, 1, 1 applies, but
then of course,
imagine I could work w to 2,
then 4, 2, 2 applies and
if I make w be 3, 6, 3, 3 applies.
So, this point now can be
represented by this three vector
in all three of these values.
One thing to note, w cannot be 0
because if you make this 0 x and
y also would actually go to infinities,
so of course when w is 0 we can
refer to that as an infinite point.
This point, 0, 0, 0 is not allowed
because we cannot have 0 over 0.
That would be an indeterminate point.
But all of a sudden, now we have
a lot of strength in our hands,
when we actually now create
this new coordinate system,
the homogeneous coordinate system,
with x, y, and w.
Let's see what that buys us.

12 - Basic 2D Transformation
============================
Now remember,
we started off by saying we want
2D transformations where we
basically have a matrix M
to give us values of any point
p to give a point p prime.
Let's look at what we would do to
get something simple as translation.
So what we want to do for
translation is of course,
we would have the axis for x and y.
And we want to translate it into
a different location again from this and
x and y, so this has been translated.
Let's say for a lack of better
words by an amount, tx and ty.
Okay?
How we represent this in this new
homogenous coordinate system?
Well, again, this is what we interested
in x, y prime, x prime, y prime, 1.
X, y and of course,
now let's think about what M would be.
By just looking at this, you notice
that we can actually construct it.
Diagonal terms are all 1's, and these,
these two axis could just be tx and ty.
And if you actually do the math,
you'll basically notice
that what we will come up with
would be is x prime is going
to be equal to x plus tx and
y prime would be equal to y plus ty.
That gives us what we wanted.
So translation is easily
modelled this way.
What about scale?
Again, here, the goal is to go from
this image, to a larger image.
In this case, again,
what we did before, the same two by two
we had looked at before, with sx and sy,
can go into these two values here, and,
of course, the rest of it will work out,
because what will happen is x prime
times sx, x would be the result.
And that's exactly we want.
So this gives me a nice
three by three matrix for
being able to doing things like scaling.
What about rotation?
In rotation, basically I want to take an
image and being able to kind of rotate
it around where basically how I
need to know things like theta.
And here the theta would
be this value here.
All right.
And we know how to do this.
Again, we know when if, somebody
gave me a theta, I can compute using
this cosine theta minus sine theta,
just in this two by two.
And again, these are 0, 0, 1.
What gives me x prime, y prime.
And we know how to do this too.
The good thing with homogenous
coordinate system is,
these two parameters help us do
things like model translations.
We can also do shear the same way.
Start with an image.
We want to shear it.
Remember, this was when
shear happened like this.
And of course again, we would put
the shears in the off diagonal terms.
All the diagonals would be run.
You can play around with this yourself
in these matrix multiplies and
you'll see it works.

13 - Basic 2D Transformation p2
===============================
One of the things that's
important now to notice,
this these types of
transformations can be combined.
To achieve a transformation we
are taking single image and
then of course use that to
generate a translated image.
This has been translated.
Then of course I rotate
this image by amount theta.
And then of course I actually
add to it things like shear.
So in essence, this basically shows
that to get these set of parameters here
which basically now show translation,
this is where this comes in.
This kind of rotates the image
theta that we looked at.
And this of course,
also shears it by a certain amount and
shears it in this amount again
noted by these ratios here.
So of course x y w here can
be combined into this and
we can simplify this by looking at the
basically now there are nine parameters
here in this matrix and if we knew
these and combinations of these.
Of course, noting here that these
combinations can be done priory and
saved to and applied to imagery one.
Now one thing I may want to talk
about right here is most of the time
this i value would be 1.
Because remember, the current
condition we had with the ws.
W always wants to come out
to be a w on both sides.
And that would be the case here.
So most of the time,
we're looking for these 8 parameters.
Okay?
So let's look at what that means.

14 - Affine Transformations
===========================
So let's start off by looking at
affine transformation as an example of
something we want to understand and
figure out all the parameters for.
This would be an equation,
we would basically have these eight
parameters that would change to
create an affine warp which basically
means is now have an image like this.
Which after transformation or
warping would appear to be this way.
So an affine transformation basically we
are combining linear transformations,
the ones we looked at, that were
the you know the rotation scaling and
all of that stuff, with translations.
So in essence, this this image
is now moved over here and
it's also been warped.
[SOUND] The properties of an affine
transformation are that origin does not
necessarily map to origin.
For example, this could be
the original origin of this image,
we've translated it and then morphed it.
Lines map to lines if you notice,
all lines are still lines here.
They've just changed a little bit but
they're still lines.
And similarly,
parallel lines all remain parallel.
These are the basic properties
of affine transformations.
And one thing, if you noticed,
this could be achieved by actually
modeling these six parameters.
So, parameters a, b, c, d,
e, f, I have six parameters.
So in essence this is a six degree
of freedom on our presentation and
once we do this now,
we can actually figure out the
transformation going from here to there.

15 - Projective Transformations
===============================
Let's look at projective transformation.
In a projective transformation, what we
are interested in is taking an image and
warping it in this manner.
So basically,
a projective transformation is
a combination of an affine
transformation we've looked at, but
added to that, a projective warp.
Properties of that form
of transformation is.
The origin does not again
necessarily map to the origin.
You can see that this
could've transformed or
move translated over to this point.
But the line are still straight lines,
right?
Lines map to straight lines here.
But now parallel lines do not
necessarily remain parallel.
An example of this you may actually see.
That for example, if t and h,
if they were parallel here,
they're no longer parallel if I was
to draw an h here and a t here.
Let's just do that.
And they would actually
intersect somewhere.
While t and h, unlikely to intersect.
And of course ratios are not
preserved in this one either.
Here, of course, we have.
What do you think?
Nine parameters?
Nah.
Remember,
I always said this
will convert back to 1.
So in essence, we have 8 parameters.
Which basically means we
have 8 degree of freedom.

16 - Recovering Transformations
===============================
So now, move down all of this.
Let's ask the question,
what can we do about trying to now
be able to recover
transformations from images?
So basically what that means for
recovering is given f of x,
y, can I generate g of x, y?
But also, can I also kind of
learn the transformation itself?
So what it basically means is given an
image f and given the transformed image,
if I know the axis for both of them,
this would be x and y, and
of course this would be x prime,
y prime.
If we know what f and g are, can we
recover the transformation, t itself?
To achieve this,
one question would be is,
how many points on both these
images do I need to know?
For example,
would I need to know a point here that
would correspond to this point here.
I would need a point here that would
need to correspond to this point here.
I would need to know this point
corresponding to this, and
this point corresponding to this.
All right?
So, if I know these correspondences,
[SOUND] I would be able to
figure out the inverse,
by all this transformation function.
But how many do I need
to know is the question,
do I also need to know some inside?
Those are important questions,
so let's get to that.
And we would do this
in forms of quizzes.

17 - Translation
================
So look at this framework here.
Again, what we're interested
in is simple translation.
Have an image.
This image, in this case, has been
translated by certain tx and ty.
Question for you to think about is,
how many points do I need to have to be
able to now model this transformation?
So please put in,
how many points correspondences we need?
So in the previous case
I showed you before,
do we need all four of them here?
That's one question.
And also, how does, how many degrees
of freedom can be used to model this?
Please fill out these boxes.
And then, in this matrix,
tell me which parts of this three
by three matrix do we think that
the values would have to be, related to
the parameters that we need to change.
Just for simplicity sake, know that
we already know this will be one.
So, fill out the others, please.

18 - Translation Solution
=========================
The solution to this
one is pretty trivial.
All I really need is,
if I know where this point is, and
I know this point here, that's
the number of correspondence I need.
1, because if I get these points,
I can get Tx and Ty.
And that's all I need.
Number of freedom, of course,
is, degrees of freedom is tx, ty.
That's 2.
And, of course, the rest of this matrix
should simply be 1, 1, 0, 0, 0, 0.
Correct?

19 - Rotation
=============
Let's look at another example.
In this case, let's look at rotation.
So in essence, the image moves and
is also rotated.
And let's call the rotation be,
the rotation amount to be theta.
Okay.
So just simplicity's sake,
let's say that we can claim c
theta is equal to cosine theta.
And s theta is sine theta, okay?
How many degrees of freedom do we
need which would be the answer here.
How many points or correspondences do
we need between both these images and
what would this matrix
approximately look like.
I'm just giving you this coach so
you can now basically use c theta,
with sines here, here, here, here,
here, wherever they need to show up.
And, of course, also remember,
this would be 1.
And the question comes up,
how many degrees of freedom?
And, also more appropriately, how many
points of correspondence do we need?

20 - Rotation Solution
======================
All right, the answer for this one.
Let's look at the correspondences.
I need this point.
I need that again also.
That will get me the translation.
But this time around,
I have to also model this.
So I'll actually also
need another point.
So basically, we would need 2 points for
correspondences.
And how many degrees of freedom?
Well I need to know tx, ty.
And if I know theta, I should be
able to compute all of these, right?
So the answers would of course, here
would be, I would need to know tx, ty,
and then of course the cosines and
sines would show up with the theta.
So I need to know theta, tx and ty and
I can actually fill this out,
to be able to get the answers I want.
And these would be 0, 0.

21 - Affine
===========
The same question here this time for
an affine and
I mean here, warp or transformation.
Same drill as before.
Please enter the number of
points of correspondence I need,
the number of degrees of freedom, and
what would this matrix look like.

22 - Affine Solution
====================
So of course, we would again need this
point here because this we need for
translation.
Like in the case last time,
we would need this one.
[SOUND] And
that would give us theta, and
of course here I would
need one more point.
That would kind of give
me more information about
how this transformation happened or
the warp happened.
So I would need three points
of correspondences, 3.
Number of degrees of freedom, we have
looked at this example before and
if you remember four, basically the
answer is I would need to know a, b, c,
d, e, f, I already know this,
these would be 0.
So of course,
I need 6 degrees of freedom.

23 - Projective
===============
Last one is, of course, projective.
Same drill for this one.
Now, you want to look for,
of course, projector transformation.
How many correspondences do we need,
how many degrees of freedom?
And fill out this this
three by three matrix.

24 - Projective Solution
========================
So for this case,
we actually need all 4.
This point, and
that's the map to this one,
this to this one, this to this one,
and this to this one.
Number of degrees of freedom.
Well, if you remember right,
remember this is still 1.
Basically, we need a,
b, c, d, e f, g, h.
So, 8 degrees of freedom
is what we need here.
[SOUND]

25 - 2D Image Transformations
=============================
Now let me actually just recap for
a little bit.
So this is basically the 2D image
transformations we are looking at.
We have an object that
could be translated,
this could be the image itself.
We could scale it,
in this case I'm showing the scaling.
We could rotate it, an affine warp, and
a projective or
perspective warp would be this one.
So basically let's
summarize all of them.
I'm going to show this with
a simple kind of a table here and
of course we look at how we actually
want to do the transformation,
what the three by three looks like, and
what kinds of things does it preserve.
Of course, simple translation
two degrees of freedom, and
we know kind of how to
model this basically and
these are the two parameters we
would actually be kind of modeling.
And of course in this case you only get
translation, orientation is preserved.
Case if you clicked in where
there's a rigid transformation,
three degrees of freedom,
the object is rotated.
Here of course we would change if
there's translation involved in
these two values, but
also just the the cosine, theta, and
stuff like that would change
these four values here too.
This would still remain
one as it is here.
And, of course, zero, zero, zero, zero.
I'm not implying that
this would be a zero,
it just means that the cosines always
based on theta would be coming in.
In this case,
the lens would be preserved.
Third case similarity,
where now we have scaled things
out four degrees of freedom.
Basically what that means is now we
basically have the two parameters for
translation, assuming
there's translation going on.
And scale parameters would be here and
the rest would be the same.
For affine, we've looked at
this just in the quiz before.
Everything that would preserve,
a parallelism would be preserved.
Lines would be straight and
everything else.
We also know that the six parameters
here would be the ones we would need to
model and
that's the six degrees of freedom.
Projective eight degrees of freedom,
all of these.
This would be still one.
Straight lines are preserved,
parallelism is not preserved.
So if you notice as we down
this preserves orientation,
because it's only translation.
This doesn't preserve orientation, but
it preserves lens, but next time
all of the angles are preserved.
Parallel lines and lines are preserved
and only straight lines are preserved.
And if you notice this is
how we can go through and
look at different types of images from
starting here looking at translation,
rotation, scale, affine,
and perspec, projective.

26 - Translation Demo
=====================
Let me now show you an example of
a simple translation using our
browser code here.
Basically again, we start off by just
simply doing things like importing
a computer vision two kit and
numpy and there from there on,
we're going to look at basically
doing things like read the image.
How just reading the tech image itself,
get more information from it.
Again we can show it and
here basically just see me
creating a simple translation or
transformation matrix.
If you notice of course it's transform
by 100 pixels and 50 pixels and
the diagonal terms are one and
one in my matrix.
Of course, using this now,
this translation matrix we can print the
translation matrix, and then, of course,
apply the transformation using this
piece of this co, function here which
actually takes the transformation
matrix and applies this to this image.
Let's see what it looks
like when we run this.
So here, of course, you see the
translation matrix being printed out.
Here is my image.
This is the original image.
And of course, this is the final image
that has been translated by, of course,
100 pixels and 50 pixels.

27 - Rotation Demo
==================
So in this code example, I just want to
show you how we can do transformation f,
a specific form that is rotation.
First two lines, basically, are just
loading in computer vision and numpy,
then basically just load in
the image figure out the height and
width of the image,
of course show the original image.
Here we want to actually showcase
a rotation around the origin at zero and
zero, that is the point of
the image right at the top corner.
And of course, what we do is we
apply a rotation of 45 degrees.
So using that, of course, we have
now computed the rotation matrix.
We can print the rotation matrix here.
And that's shown here.
And of course, then we can apply
the transformation by this function cv
2 warpAffine.
Again, rotation matrix.
The image itself.
And that way we now can show the image
here with this line of code.
In this part of the code here, basically
now we apply the same transformation
except now that we are applying
at the center of the image.
Of course to achieve this we have
to transform the point to the half
the width and half the height of the
image, and again we are rotating this in
the other direction, minus 45 degrees,
and here one is still the scale.
We don't want to change the scale.
[SOUND] So, again, now we print out the
rotation matrix and apply it with new
new images transformation using the same
function above and display the image.
Let's see what this looks
like when we run it.
This is the rotation matrix when
we have the image at the origin.
That is the point top here,
of the image.
And the next one here is after
we've actually figured out
the center of the image.
That is we've basically moved to the
width half and half height of the image.
And then applied the same transformation
of basically rotating by 45 degrees.
Notice again this is minus 45 degrees.
This is plus 45 degrees and
therefore the signs are different.
This is our original image.
This is the image rotated
around the origin point.
And again as earlier stated I rotated
this image by 45 degrees, so of course,
now it's truncated or
cut at this top here, but
you can see that the image has
been rotated by 45 degrees.
This is the final one where again
this time around I've done the 45 degree
rotation at the center of the image.
That's why we actually
have put in this for
different terms in
the transformation matrix.
So actually our rotation
would be at this point.
And here you notice, of course,
the tech sign now has been
rotated this way 45 degrees and
shows a transformation of rotation by
45 degrees at the center of the image.

28 - Shear Demo
===============
Now let me show you a bit of code for
the scale and
shear transformations
applied to an image.
The usual preamble of loading
computer vision and numpy, and
wrote reading the image.
And here basically what we do now is
we want to actually be able to apply
a resize scale,
by basically what we're applying is,
transformations in x and y, 1.5.
These are various types of,
additional information we can to our
resize function to be able to scale it.
And that basically allows it to
kind of change the image and
scale the image here.
And I can, of course,
just show the image, by just scaling it.
This one of course if you notice,
I didn't spend time building
a transformation matrix because this
piece of code already takes
care of this kind of stuff.
The next example is where
we can apply a shear or
a skew in the horizontal axis only.
So of course now, for this,
we will create a matrix,
the diagonals are still ones.
We don't want to do any
kind of scaling here.
But of course now I'm applying
in the off diagonal terms,
a small scale in this case,
just in the x direction.
And I've given it a 0.5.
And using that now you've
actually computed a or or
come up with a new
transformation matrix.
You can print it and then apply it using
again our affine, warpAffine function,
take the image, and now here, we
basically just do some different types
of transformations, apply it,
and of course, can see the image.
Let's see what this looks like.
Here is just the printout
of the shear matrix.
This is the original image.
This is the original image scaled by 1,
1.5, that is, basically we've just
added a little bit more size to it.
And this is the output of a shear
transformation where we basically have
applied a 0.5 shear just in
the horizontal direction.

29 - Affine Warp Demo
=====================
Let me now demonstrate a bit of code to
do an affine transformation of an image.
The usual preamble of loading an image,
an out, open cv and
numpy, reading the image.
And here, rather than do other types of
things with transformations, we're going
to take much of a, approach where we can
identify the points of transformation.
So I basically now come up
with first user points.
And if you notice here, I'm giving it
three different points, in first image,
and three different points
in the second image.
Using these two points,
I can now create a, affine, basically
apply the affine transformation to
compute a transformation matrix.
And I'll, once we have the
transformation matrix, we can apply it
to the image that we already know all
the other information of like, for
example, width and height.
And after, of course, we have applied
it, we can display the image.
Just run this code here.
So, from those three points that we
used, we were able to compute an,
transformation matrix which
is actually printed out here.
This was my original image.
And this is the final output image after
the transformation matrix applied of
giving it an affine warp.
Now you can see the image have been
warped, but again, notice straight lines
are straddle straight lines as we
talked about earlier in the lecture.
It just basically has more of an affect
of being able to be, create a warp, or
a kind of a shear in two
different directions here.
All lines are still straight
as you can see here.
The straight line still remains
straight in this transformation.

30 - Perspective Warp Demo
==========================
So for my final example,
let me now showcase the perspective or
projective transformation of an image.
Again, the usual things.
Here just to be different we're going to
play around with a different image,
the Berlin Wall image.
We can actually compute the,
the height and width, and
all of that kind of stuff
here from the image itself.
And again it should be no surprise to
you so far that now we need four points.
So, for example, so in the first image
I'm going to find four different points,
so I've basically given them
those coordinates here.
And for the second image I've found
four other points, and we need those for
perspective transformation using these
two points, points one and point two.
In this code I'm going to compute
the matrix, transformation matrix that
actually uses these four points to
compute the perspective transformation.
We're going to print it out and
then of course, as we have done before,
we're going to just apply
this transformation here.
Let me just run this code.
Here you see the perspective transform.
Again, this should be no surprise.
This value is still 1.
But of course we have other
values in the rest of the matrix.
So this is the original Berlin Wall
image, and you'll see why actually this
image was chosen to showcase
this effect of perspective warp.
This is the perspectively corrected
image, now just being able to apply
the perspective warp, and
again the points were correctly chosen.
You notice now all of a sudden you
get a warp of actually seeing this
image right in front as opposed to,
in the previous case,
where you saw an effect
of foreshortening.
Again, notice here straight lines remain
straight, which is what we talked about
as one of the values of these
types of transformations.

31 - Warping
============
Now let me actually talk
a little bit about warping and
we are going to get into lot more
detail about this in the next lesson.
So here basically,
I'm just showing you two images.
Right, so I have a point here and I
want to generate a larger point which is
being rotated in the new word image
space where the domain is x prime,
y prime so this may coordinate xs, and
of course, I have my transformation.
So I take this pixel and
I warp it to this location here.
So in essence,
what we're doing is sending each pixel
from f(x,y) to its corresponding
location with a transformation
T(x,y) in the second image.
What happens if the new pixel
lands between two pixels?
Remember, this could be much bigger in
this open space that we coming up with.
In that sense,
we're taking a bigger image and
filling information from there.
In the forward mapping, what's really
done is that we would distribute
the color among the neighborhood pixels.
So, if this is the pixel I have there,
and it shows up there, I would kind of
distribute the color in the ones
around it to generate a new pixel.
And that's what I would actually do.
This is the forward warping process.
Another well-known process is when we
actually go inwards, backward warping.
Again, I take a pixel from here,
and I want to go and
figure out the inverse transformation to
find where would it actually end up, and
what would I do with it.
So again in this, what I will do is take
each pixel from the warped image and
find its corresponding location, and
move it to a new image as
long as I know the inverse.
Again, in this case, what happens
if it shows up in between pixels?
In this case,
what we would do is basically we
will interpolate the color values.
Those where we were redistributing.
Here we would interpolate
the color values and
fill it in here from the neighbors.
Again, how do we do this interpolation?
Remember how we did things like
filtering images and stuff like that.
We could use those types of
methods to help us do this.
Just to do a quick comparison,
forward versus inverse warping.
Which one do you think is better?
Well usually,
inverse mapping is a better map that,
because it eliminates holes.
We're always going from
something we know how to get to,
to much more of an original image.
And of course that allows us to
fill in all the color information.
If you sometimes go from one to the
other, we might run into places where we
don't have,
we'll have to do some sort of hole fill.
I'll talk a little a bit about
that when we talk about morphing.
But, the important part
is to do inverse warping,
we need an invertible warp function.
Now I want you all to think about how
we would actually create an invertible
warp function based on what
we've talked about before.
And see that in some instances,
especially for rigid warps and
stuff like that, that's the easily
computable inverse functions.
Especially when you have rotations and
translations and you're doing scales.
It does get harder when you do
a bunch of other things and
not all the time especially when
you do have, not a global warp.
It gets harder and
harder to compute those.

32 - Summary
============
So to quickly summarize,
we learned about image transformations,
not just about image filtering.
Remember, we talked a lot
about how to do warping in
things like even when we
played around with panoramas.
This is some of the foundations
that we're going to use.
We're going to talk about morphing,
but we're going to come back and
use these, not just image filtering,
but image transformations and warping
to help us do the kinds of computational
photography that we are interested in.
We basically looked at all kinds
of transformations, rigid,
projective transformations of images.
And we actually kind of
looked at what parameters and
how to do this simple types
of things using matrices.
If anybody's curious,
more, more detail exists on chapter
2 of the Rick Szeliski book.
I look it up.
And also, I just, of course, as usual,
relied on other people's slides to
generate the slides that you saw.
More information will be
available on the website.
