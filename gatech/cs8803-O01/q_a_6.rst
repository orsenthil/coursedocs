1 - Office Hours Week 6
=======================
Hello, and welcome to the sixth office hours.
This will be the last office hours. Let's get started.
The first question comes from MJL.
He wants to know how Graph SLAM deals with non-distinguishable landmarks.
That's called the correspondence problem.
It actually turns out to be the harder of the two problems.
I gave you the problem of how to solve for known correspondence,
which becomes a continuance optimization problem,
but there is also a discrete problem here, which is does this lane marker correspond
with this guy over here or to that guy over here? There are solutions.
One of the best ones is called "ransack" where you randomly assign correspondences
for three or four landmarks, solve the set of equations and then look
for the best nearby matches and then fill them in.
You repeat this so you can get rid of the local minima.
In general, if your robot is very accurate, then just picking the nearest landmark is a good heuristic.
But if you go through a huge cycle, you might just not connect,
and there might be multiple ways to connect, and then you can use this ransack method
to try multiple choices. &amp;gt;&amp;gt;Okay. Thanks.
The next question comes from Marcello.
He wants to know in a real environment we don't know the number of landmarks.
In the unit it seems like we were always pretending like we knew.
In, for example, the mind mapping video that you showed, how do we deal with
encountering all these new landmarks?
Do we not get the same problem that we had with out position measurements
where this matrix just becomes unwieldy?
Marcello, that's a great question, and there are many different answers I can give you.
One is if we really had point landmarks the way I described them, like tree trucks or corners of rooms,
you can just grow the matrix using the functions I provided to you.
For every new landmark you just put a new row and a new column there.
That's basically it.
However, the more interesting version of your question is what is a landmark?
In our mine mapping, for example, we don't make distinct features like ??? landmark.
Instead what we've been doing is taking little small local maps
that are defined over 5 meters of robot motion.
We make these maps the basic entities.
Now, it turns out there aren't any landmarks in the traditional sense,
but they still have a location and you can still match them and see how they fit together.
In matching them, you can make a constraint that's very much like the graph-like constraint
that is like range and bearing or x and y distance.
You can toss them into the same set of equations.
That works really like a charm.
Great. Sounds sort of like when you're stitching together those panoramic photos.
Yeah. There is an entire field of people who stitch together these local images into global ones,
including image stitching, panoramic stitching, and so on.
They use very different methods like the 3D reconstruction of the boat Titanic
that sank a hundred years ago that is done with local stitches that is being stitched together this way.
If you go back all the way to Gauss 200 years ago when he invented the squares method
it was basically his attempt to map the land
and get these local constraints together of measurement points to make
a reasonable map of our land.
That's what this all dates back to.
In fact, he basically invented Graph SLAM 200 years ago. He just didn't know about it.
The next question comes from Emil, and he is talking about how we found all these
great ways of helping our robot make intelligent decisions.
But there has to be some situations where we've just hard-coded some things
into, like, the Google self-driving car.
Can you talk about any of those exceptions that have been hard coded in?
My aspiration usually is to have no exceptions and try to come up with a single framework.
The reason is in my experience every time we have an if, then, else rule
where you say this is the exception and this one isn't
at that border you introduce brittleness.
You often get the wrong behavior because most exceptions aren't clear-cut.
When I talked to my students at Stanford or my team at Google,
I try to get rid of any possible if, then, else statements.
Now, having said this of course there are exceptions.
There are motorcycles. There are cars.
It turns out cars stay in lanes, but in California--probably like the way it is in India--
motorcycles tend to be like between lanes and sneak between cars.
We sometimes have special rules for this.
For example, we have rules that say certain crosswalks have more likely pedestrians than other crosswalks.
Our car will behave differently for these crosswalks and react differently to people on the side of the street.
There is a good number of those exceptions.
The truth is the real world is messy.
You have to really go through those one after another and try to address them.
Have said this, from the mathematic perspective the fewer you have in your code the better.
All right. The next question comes from Quartz.
He wants to know how we use SLAM in a changing environment,
and whether there is a way to forget previous landmarks and acquire new ones.
Quartz is a great name. It must be non-American keyword, I guess. That's what it looks like.
Changing environments--there's a very simple fix to it,
which is as we added uncertainty to the robot position in our system of equations,
you can do exactly the same track for landmark positions.
It's a little bit cumbersome, but you could say let's make a landmark position at time T
and one at time T plus 1, and the one at T plus 1 has added uncertainty,
very much like the way the robot moved, but there is no motion, say.
The you marginalize out the estimate of time T using the same math we talked about,
and you get a new set of constraints that basically encompasses a landmark with more uncertainty.
You can even toss in things like estimates of where the landmark moves by putting
the velocity of the landmarks into the graph SLAM formulas
and it actually carries through, it turns out. I just didn't do this.
That's one way to deal with dynamic environments.
The next one comes from MJL again.
As a robot moves, its location uncertainty is going to increase.
Is there any way to pull out this uncertainty from our omega matrix?
Yes, there is. It turns out the omega matrix is the inverse covariance matrix.
I didn't really talk much about this, but it is really the inverse covariance matrix.
If you just invert that matrix, you get the full covariance for all of the landmarks and the robot.
If you care about, say, just one landmark, you just take the corresponding
columns and rows of the matrix.
The next one comes from George.
He wants to know what are some interesting trends in SLAM research these days.
Do you think there is any good problems that you could recommend
a young researcher getting involved with?
Tons of good problems. There are some really fantastic working coming out of
University of Washington by Steve Seitz on taking very large photo collections
and tossing them into a big optimizer to build a 3D map.
This is a project that is now at various universities.
People go to Flickr or other online photo sites--Picassa--
and they extract those photos that tourists have taken
and establish correspondence, say, for buildings and so on,
and then reconstruct how this object looked in dense reconstruction.
That's in computer vision--often called structure from motion--and we call it SLAM in robotics.
Anything having to do with dense data, like with going to Google maps, for example,
and get oblique shots and ground shots from street view and aerial shots
from an aerial probe or from a satellite and rectify this into a 3D model.
These are basically unsolved problems.
There is some really good progress, but at the moment you have bridges
and underpasses and occlusion.
There is a ton of opportunity.
You can actually take your cell phone camera or your camera
and just go through your environment and try to make a full model of your kitchen.
That in itself is very, very hard.
Then if you add the fact that the world might be dynamic,
like objects might be deformable, like this piece of paper over here.
If you want to model this in 3D, that's even harder.
That's a fantastic research area that will be with us for the next, at least, 2 decades.
The last question comes from Katembe.
He wants to know about using landmark correlation.
For example in our model of omega we assumed that 2 landmarks couldn't see each other,
but in reality sometime we have some correlation between landmarks.
For example, street lights come at regular intervals.
Do we ever implement this, and if we did would it help?
It would absolutely help. Any information you can bring to bear is good.
This question is like the same question as having a multi-robot situation
where multiple robots interact and move around, and they can see each other.
In seeing each other, you insert a constraint that is between these two robots.
If you had landmarks that either could sense each other--
maybe you have wifi beacons, and they can sense each other's strength and ability
or if you have external knowledge like the street view, this is super informative.
The formalism falls apart when there is negative information.
For example, there shall be no street lamp within a 100 foot radius of the current street lamp.
The reason is these negative constraints are very hard to express in a graph-like fashion.
Positive information, like this one is this far away from this guy,
is much easier to express.
But, yeah, in general any information you can bring to bear will help you solve these really hard problems.
All right. That was the last question.
Since this is the last office hours I want to say a big thank you to you, Sebastian.
Thank you for you. &amp;gt;&amp;gt;And a huge thank you to the students.
It's been really amazing working in the forums and helping you out with this course for the last 7 weeks.
I know I've learned a lot, and I hope you guys have too.
And I learned a lot. I really love your questions.
I love you interact. I love hanging out in the forum in the evenings.
I hope you guys learned a lot, and I hope these office hours and the course
enrich your lives and empower you to do things you've never done before.
