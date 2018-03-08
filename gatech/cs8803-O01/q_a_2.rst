1 - Office Hours Week 2
=======================
Welcome to the second office hours. I have Sebastian here and myself.
We're going to do this the same way we did last time.
First we're going to talk about some content,
and then we're going to go into some applications,
referring mostly to Kalman filters but also talking a little bit about Stanley and Junior.
Okay, what's the first question?
The first question--both of the content questions actually have to do with linear algebra.
When we were talking about this state transition matrix f,
we have this equation x' equals f times x plus U.
You said that this U is the motion,
but the motion seemed to be embedded in this f matrix in that
the velocity was taken from the state with the f matrix.
What exactly is going on with U?
U allows you to apply a choice like when we just said
the position is a function of velocity that's describing physics
but doesn't give you a choice.
When you want to insert a choice into the system, like for example,
you might want to change accelerations and that affects velocity and affects state.
That choice is expressed with the vector U
We didn't really use it because we were tracking things.
We didn't know how they were being actuated, so we set U to zero in our example.
But if you have control over the system you're trying to track
and you can insert like a motion yourself, then you use the vector U.
Interesting--just one other piece of intuition we're hoping to get is
a lot of the matrices we talked about either didn't have off-diagonal elements
or we at least didn't initialize any off-diagonal elements.
Specifically, in the covariance matrix and the r matrix,
can you give us some intuition about what those off-diagonal elements would represent?
We actually ran into an example that did have off-diagonal elements.
We didn't initialize it, but then the velocity became correlated with the position,
and we realized the faster we moved the further we are to the right.
That was expressed by an off-diagonal element.
They turn into correlations, so the largest these elements are,
the more 2 variables are actually correlated.
The more knowledge about one variable correlates itself with another variable.
Now, let's get into some of the applications that the students seem especially interested in.
Specifically, this r matrix. Where does it come from? How do we get it in real life?
What are we doing with our sensors?
So the noise matrices express how noisy your sensor is,
and at first approximation you'd say let's just measure
what the variation of the measurement is and then plug it in.
But because these filters, a very subtle thing, assume conditional independence,
they assume that noise is independent from one type to the next whereas in reality it isn't.
Typically you start with a very large value, and you look a the result,
and if the result looks good to you, you leave it that way.
Unfortunately, there is no good science for it.
Awhile back, together with Andrew Ng, I published a paper
on how to learn the noise matrix, but that goes way beyond this class.
You mentioned that Stanley and Junior both use laser and radar.
Does each one offer something unique or are the both just doing the same thing?
Either way, how do we incorporate measurements from 2 sources into our Kalman filter?
These are two questions.
First of all, laser and radar at first approximation do the same thing.
They measure how far things are away.
Radar also measures how fast they're moving for the Doppler effect,
but their characteristics are very different. They measure different things.
There are certain things that can only be measured by laser, others just by radar.
In fact, laser tends to have much higher spatial resolution,
but events become foggy.
The wavelength of light tends not to be as good as a radar wavelength.
So they're somewhat complementary.
To incorporate both, Bayes rule allows you to incorporate sensor measurements one after another.
If you have a laser and a radar, you just multiply both of them in, and that's just fine.
Okay, great.
The top-rated question, actually, was about
the programming languages used in Stanley and Junior.
Was it Python? Was it something else? &amp;gt;&amp;gt;It was not Python, honestly. &amp;gt;&amp;gt;Okay.
At the time, we started out with C, but then C++ became very popular. I was popular.
And it was the better choice, so almost all the code is written in C++/
How do you make that decision when you're starting a project this big? Is there debate?
There is always debate.
The beauty of C++ is it is very efficient in execution,
and when you use it right it can be very powerful. If you don't abuse it.
It has way too many things built in, but some of the things like the classes are just really, really good.
Then you hire people, and you work with students, and some of them like Java,
so they write their code in Java, and others like C++ or Python or Ruby on Rails.
Then you just bring all the stuff together.
Okay--thinking of Stanley and Junior,
what were the major hardware and software differences between the two vehicles?
Stanley had about 6 embedded processors.
Junior had 2 PCs with quad cores so there was a more integrated system.
The biggest difference in the hardware was really the sensors.
Stanley had very, very cheap and simple laser-range finders as the main sensor.
We did have radars. We didn't use them much.
Whereas Junior had a much more ranging sensor suite.
Junior could look in all directions--we call this "surround sensing"--
whereas Stanley could only look straight ahead.
So that thing we saw spinning on the top of Stanley, that was the laser-range finder?
What you saw spinning on the top of Stanley was actually on Junior.
That was on Junior--okay.
Yeah, you never saw anything on Stanley, because there's nothing spinning there.
That was on Junior, and that was a laser-range finder.
Right, and that one spins because it looks in all directions.
That was important for city driving because what's behind you actually matters in cities
whereas if you drive in desert terrain there is no traffic. You don't have to look back.
That's a good segue into the next question, which is what's the next big challenge?
We've done deserts. We've done urban driving.
The next challenge is it'll take over our cars.
Basically get this technology into every single car and make sure driving is safe.
Every person has a special button that says, like I explained, my little chauffeur button.
I want to just drive automatically,
and then I'm just going to get home without having to pay attention.
Finally, how comfortable is it?
Do these cars drive similar to the way you or I would drive?
When we first started out, I would say the driving is effective but not elegant.
You would get in the car, and you'd know exactly what I mean.
The steering wheel would go like this all the time, and it would make a lot of noise.
It was pretty clear you were inside a robot.
On the outside it looked pretty great, but on the inside it didn't.
But as things moved on, if you get into a Google car right now,
you won't be able to distinguish from a human driver. It's really rock solid.
The steering wheel stays like this, but it turns it confidentally drags it around,
moves the right direction, comes back. It's actually come a long way.
To get from what you said to where we are now--was it low-pass filtering?
We will have a class on control,
and the control techniques ended up to be very sophisticated but also very, very good.
All the motion of the steering wheel are all related to inaccuracies.
They came from multiple sources.
Some of it was that we weren't processing our GPS date good enough yet and our map data.
Some of it was the map resolution--like if you have a 10-15 cm grid cell
and your estimate jumps from 1 grid cell to the next or your particle filter jumps a little bit around.
They might not look dramatic on a screen, but if you turned to steering motion
in your steering wheel, it goes by 2 or 3 or 4 degrees. That's really bad.
We had a sensor that tracks that angle of the steering wheel and the spatial resolution was about a degree.
That means you couldn't quite know what the angle was,
so you would drive a little blind--like up to a degree.
A degree of steering wheel doesn't sound like much, but it's actually a lot.
You can try this out.
If you drive a car and you only move it by a degree, you feel a noticeable effect.
You'd find out after a while we'll actually pulling in this direction. Let's drag it back.
And all that stuff we kind of fixed.
So we'll learn about that in, I think, Unit 5? PIT controllers? &amp;gt;&amp;gt;Yep.
Excellent. I can't wait. &amp;gt;&amp;gt; All right. &amp;gt;&amp;gt;Thanks a lot. &amp;gt;&amp;gt;All right. Take care.
