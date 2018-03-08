1 - Office Hours Week 5
=======================

Welcome to the 5th office hours.

We had a lot of great questions on twiddle and parameter optimization.
Let's get started.

The first question comes from George.
He wants to know, first, is twiddle really all that good?
Does it really give better results than other methods you might use for selecting parameters?
Well, George, that's a great question.
It's good in only one dimension, which is it's really easy to implement.
Sometimes people overlook this.
This is an entire literature on search parameter optimization.
In a lot of cases where twiddle would fail other methods would succeed.
You can write a PhD thesis about this, but the nice thing is twiddle takes no time to implement,
and I've never seen a piece of code that couldn't be made better with a twiddle around it.
That's why I explain it. I think it's just an easy method.
I literally use it all the time.
Another question from George about twiddle is local minima.
Are they a problem with twiddle? It seems like it's pretty easy to get caught in one.
That would be a fantastic final exam question.
Sorry for taking it out of the final exam.
Of course, it's susceptible to local minima.
It's essentially a hill-climbing technique.
It might on occasion jump over because of the step size,
but by and large we're going down the hill.
It's also can get stuck on ridges and other phenomena
that might occur in certain optimization spaces.
It really good if you have a good guess for the initial parameters.
It's pretty horrible if you want to search systematically.
Then you have to do things like grid search
or a kin of particle filters as randomized methods for searching as well.
Matt wants to know how you can smooth a vehicle's path and still
guarantee that it's going to be collision free.
It seems like sometimes that new path will run into an obstacles you had previously avoided.
Matt, you're absolutely right and that's regrettable for the obstacle and the car.
It turns out that in practice the smoothing techniques
that we use are a little bit more sophisticated.
That is, it's not just points in x-y space, but it's successive state vectors for cars.
The parameters from one to the next are the steering commands for the car,
and then you can actually often much better guarantee that you stay away from obstacles.
There is still this issue of how to--obstacles are repellent,
and you have to put into your optimization terms
a constraint that expels you away from these obstacles.
To be honest, this becomes a bit of a black art how to tune these parameters.
I had a PhD student work on very narrow openings with smoothing
where we used the distance between obstacles
as one way to scale the pressure that obstacles would assert
on the path to pull away from themselves.
The car would be able to go through very narrow passages
but in very wide passages wouldn't go straight to the middle of it.
It's a bit of a black art, and I'm really trying to scratch the surface here.
All right. Lauren wants to know--in the unit we had this PID exercise where we were driving
the car and trying to get it to align with this straight line at y equals zero.
He found that when halfway through his run he switched the target to y equals 2 instead
after the car had already gotten going along y equals zero pretty well, this went sort of haywire.
Do you have any idea what may have happened?
It seems like in reality a moving target is a pretty common thing to have in a car.
Don't do that. Don't do that with your own car. Okay? Your car will go haywire.
It turns out in a lot of controls there is something called the "basin of attraction."
It says a controller, when you look at it mathematically, is only guaranteed to succeed,
we called this "stable," if it's initial set point, the distance and the angle and so on
from the reference trajectory, is confined in a specific area.
If you were to analyze our controller, which happens to be a nice stable controller
so you can actually do this, you'll probably find that the set point
2 off is outside the basin of attraction, specifically if we have an integral term.
That would be particularly bad.
There are other ways to derail it.
You could have the car face the wrong direction,
and I believe the car would produce something that you wouldn't expect.
When you design the controller practically and theoretically it's useful
to guarantee to yourself or convince yourself that you're within this basin of attraction
where the controller actually works.
I love the fact that you're running this experiment,
because that's the kind of stuff that's really interesting to run.
I think it's much more interesting to break things than have things work,
because we can understand where the boundaries are.
And you found one, and that's really, really great. I didn't even talk about this in class.
Thank you.
Next question comes from Omar.
He's a high school student, and he's taking this course,
and he's going to be applying to colleges soon.
So Omar-- &amp;gt;&amp;gt;No, go on. Any advice. Go for it.
Omar, I'm your friend. &amp;gt;&amp;gt;That's it? &amp;gt;&amp;gt;No, go ahead with the question.
He wants to know if you have any advice for projects he could tackle,
hopefully, that would show college admissions committees how much he's learned in this class.
Omar, I'm your friend. Keep doing what you're doing.
You have your life ahead of you, which is wonderful.
You're asking the right question. You're taking my class.
You are audacious to take this class. That's fantastic.
All the high school students out there--you guys rock.
In the Darpa Grand Challenge, one of the top competitors was a team from
southern California, a high school. What was the name? Palo Verdes, I believe.
It was mostly girls, it turns out, and they were all under the age of 17,
and they actually beat MIT out of the prelims in the Grand Challenge.
I was insanely impressed, and these students to the present day are actually my heroes.
What can you do? There is a FIRST. My friend Dean came and started the competition.
It's a great way to be creative.
There is Lego Mindstorms that you can play with and have a lot of fun with
and be creative about it.
There are all kinds of mathematics/robots olympiads
where people do hard problems, hard programming problems and so on.
The only thing I take issue with is I think we pay way too much attention
to the admissions process and way too little attention to just having fun and learn something.
I have never worried about admission.
I ended up at Stanford because I couldn't decide and move on,
so I got older and older and eventually became a professor.
I think the focus on having fun and exploring something new and learning something new
to me is one that I wish you could maybe remember when you do this.
Because that's really the most important thing in life in my opinion.
That's good advice, I think. Thank you.
MJL talked about his own experiences driving a car and how his decisions on the road
don't just depend on where his car is and where he wants to go but also on how fast he's going.
That's something we haven't talked about much,
how to incorporate speed into robot decisions.
Coming from Germany we don't really worry about that--just kidding.
Absolutely correct, and there are multiple aspects to speed.
You bring up one--that is, if you take the same turning radius at a higher speed,
your lateral acceleration goes up--your sideways acceleration.
Eventually your car will spin, flip, slide, or similar, but it won't work anymore.
So in our work on the Google car and the Stanford car,
we put actually a limit on the level of acceleration and made that the thing.
It means on highways our turning radius is significantly larger than, say, on a parking lot.
That's true for any human driver as well.
The second part we didn't talk much about is selection of speed.
I didn't because the control methods are not quite
as interesting as the steering control methods.
Basically, you can imagine that you set the speed so that you can always come to a safe stop.
Every obstacle in your way, every pedestrian on the side, every car in front of you
puts a limit on the speed, as does, of course, the legal speed limit.
In the controller is one that uses the throttle and the gas to gradually pull back,
in a PID way actually, to the set speed that's the maximum legal speed
or drives at the speed given all these other constraints.
The lateral acceleration does impose on the maximum speed.
When we know we have to drive a turn, we can compute where we do the acceleration
based on different speeds and then back propagate those into the equation for speed.
That gives us a limit on speed as well.
Our car naturally slows down before turning.
Does that maximum lateral acceleration depend on things
like road condition, which I imagine it would?
A slippery road would, of course, have an effect. &amp;gt;&amp;gt;It should. It should.
I hope so. &amp;gt;&amp;gt;I think it presently doesn't. It will in the future.
We have a bit of a difficult time right now determining what the exact road conditions are,
partially because we don't have access to
the stability management systems on cars themselves,
but it absolutely should, I agree.
Laurent asked another question about twiddle.
This one's about correlated parameters.
It seems like with twiddle we're adjusting one parameter at a time.
What if we have a situation where we need to change both of these parameters
or two of the three or three parameters to really get a better minimum?
That's a fantastic question that a case where twiddle will just fail you.
If you have a small diagonal ridge and two parameters to co-evolve,
it'll just fail. There are fixes.
Again, there is an entire literature.
The easiest fixes, if you have happen to know the direction, the can twiddle in that direction.
There is something called adaptive samplers that actually learn
about this direction dynamically and build gradients to follow.
There are all kinds of other methods that look at the surface shape and model the surface shape
and model the surface shape and find the optimal direction to go.
Again, twiddle was only given because it's so simple,
and I hope you found it to be very effective.
It was partially given because I couldn't figure out what the right control parameters are,
so I just implemented this twiddle thing.
But yes, there are many, many ways to improve over twiddle.
Phillip points out that there's going to have to be some sort of time lag
between when you make your commands and when the car actually responds to them.
How do you account for that time lag?
Phillip, that's a great question. This is what a lot of our time goes into.
This is a really, really, really hard question.
The time lag basically kills everything.
If you take your car and control software, say, and you make a controller
and then you add, say, a 10th of a unit of time delay in there.
Just try it out and pretend that you're always acting on the previous sensor measurement.
You'll be amazed and how badly the car will drive,
because it would constantly over steer and under steer.
The best method we have right now is to use a predictive controller,
which is we have a model of the car.
We know at what time the control command was issued,
when the sensor measurement was taken, how much time the processing took,
and we kind of predict what the measurement would be at the time the processing is finished
and then use this as an input.
If you know about time delays in the vehicle itself to execute commands, you add this on.
The second thing we do is actually model the car more detailed than I pretended.
In the way I taught it it felt like we could set the steering wheel to any set point instantaneously
but a physical steering wheel has inertia.
Instead of modeling the set point, we have a secondary controller that understands
how much torque it takes to turn a steering wheel and uses that as its information.
The better your model the more accurate your control. It takes some work to get it right.
Thank you. The last question comes from Martin.
He wants to know what happens when the physical model
that we're basing all of our decisions on changes?
If the car gets a flat tire, or something along those lines, what happens?
What happens to people? People are actually quite amazing.
You can do the test yourself.
Pick up a box. You have no clue how heavy it is--someone puts a brick inside or not.
You lift it, You can completely adjust the dynamics of your body--
the posture of your body--to be able to walk with it.
If find this unbelievably amazing that we have this kind of intuition how to handle things,
and we really reconfigure our body.
Cars can do this to some extent.
They can do it specifically if they have a model of the change.
If they understand which way, say, a blown tire affects their dynamics.
There has been a lot of work on this.
You can run multiple predictive models--one with a blown tire and one without a blown tire--
and then when the one with the blown tire comes along,
then this model all of a sudden becomes the more plausible to explain what's happening.
That's kind of what people also do in a very, very fast way.
They understand, well, I tried something that didn't quite work.
Then they correct for it.
PID controller is somewhat robust,
like when we put the drift in the tire, there was a change like this.
But yes, a blown tire will very quickly leverage the PID controller out
of the basin of attraction for stable control.
As a result it could really happen that this thing flips.
In reality the number of things that can happen to a car are quite enormous--
from the mattress on the highway all the way to the blown tire to the defective computer,
which also effects the car.
I wouldn't claim we have solved this problem.
We are really working on this at Google right now through these different situations
to make the situation as robust as possible.
For me it's still an open problem how to control a car well
and also notice that a tire is blown. Thanks for asking this question.
Thanks a lot for all the good questions. Thank you for helping to answer them.
Next week we're doing SLAM, I think.
We don't know what slamming is. &amp;gt;&amp;gt;Whatever slamming is.
Who's being slammed? &amp;gt;&amp;gt;I don't know. I think--
Slam, slam, slam, slam, slam. We're doing SLAM.
Come see the SLAM lecture.
I want to say a word that--we've started with many tens of thousands of students.
There's still a huge number of students left,
but when you're at this point and ask this level of question,
you're a serious person. I totally appreciate this. This isn't an easy course.
In fact, this course is really hard.
Thanks for asking such insightful questions.
I'm going to go back to the discussion forum and answer some more questions there.
I guess I'll see you in class. &amp;gt;&amp;gt;See you next week.
