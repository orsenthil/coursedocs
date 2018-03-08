1 - Office Hours Week 3
=======================
Hello and welcome to the third office hours. Let's jump right in. &gt;&gt;All right.
Many students, myself included, had some questions about the resampling wheel.
Specifically, when you draw a random number between 0 and twice W max,
where did that number, twice W max, come from?
I have the same question. I made it up.
I wanted to make sure that these wheel can jump over entire particles
that wouldn't large enough, but if you make it really large then you have to search a lot.
I figured if it's 2^n it's going to be fine.
Does this bias the sample in any way, choosing this number.
I actually don't know.
I think there is certainly a correlation between adjacent particles in the selection of particles.
They're not independently drawn.
I just don't know what the effect on the particle filter will be, and I wish I did.
The next question, or two questions I should say, come from George.
He wants to know if there are any rules of thumb that we should keep in mind
when we're choosing what filter to use for a given situation.
When do we use the particle filter? When do we use the Kalman filter?
Absolutely, yes.
The particle filter is the easiest to implement, but the complexity scales exponentially
with the number of dimensions.
That's usually a problem, because if you have a high-dimensional space, you just can't apply it.
The Kalman filter is the only filter that does scale exponentially, so it's very nice.
If you have like a 15-dimensional space, you will usually use a particle filter,
but the problem with the Kalman filter is it's unimodal, so you can't really have multiple hypotheses.
There are extensions of the Kalman filter that does this
called mixed rough Kalman filter, multihypothesis Kalman filter that can do this.
They address some of these problems.
The histogram filter is applicable in situations similar to the particle filter
where you have a global uncertainty, and it's more systematic.
In the particle filter, if you loose track of the correct hypothesis, you might never regain it.
In a grid-based filter you have a chance of regaining it.
Grids are easily supported in many programming frameworks.
Sometimes there are better ones to use, but they also have a generic limitation
in the accuracy, which is related to the resolution of the grid.
My recommendation is if you have a multimodal distribution use particle filters if you can.
If it's really a continuous space with a unimodal distribution use Kalman filters.
Okay. That's a great segue this question about switching between filters on the fly.
For example, we have our particle filters that converges to a unimodal distribution.
Then can we switch to the Kalman filter?
It isn't done much that people switch.
The reason is when you switch between filters,
you end up getting moments of increased uncertainty.
You can see this when you buy commercial GPS receivers.
They tend to run multiple Kalman filters, it turns out, 3D
depending on whether it's 2D or navigation.
When they are switched, the behavior becomes a little bit iffy, and often that is bad for robots,
because they they a little bit because this is where it says this thing versus the other thing.
They're not quite consistent.
There are ways to combine multiple filters types.
The most common one is called the Rao-Blackwellized filter--Rao-Blackwellized--
after Rao and Blackwell.
What they found is that in a particle domain, sometimes if we nail certain dimensions with particles,
everything else conditional on the particle becomes Gaussian or unimodal.
Then you can exploit the efficiency of a Kalman filter that is now attached to individual particles.
I'm not going to go into depth here, but there's an entire field of Rao-Blackwellized filters
that sometimes can estimate in the spaces of hundreds of dimensions.
Great. Thank you. That actually predicted George's next question, so we'll move on.
Drew wanted to know about what happens to a particle filter when the motion modal
moves a particle into an invalid place.
For an example, in that corridor demonstration you gave, what if a particle gets moved into a wall?
Well, thanks Drew. Great question.
The obvious answer is you killed that particle.
The way to think about this is in the measurement model you've got to have
this kind of implicit sensor that says, "I'm just sitting inside a wall."
The truth is the robot never sits inside a wall, so that sensor would always say
with absolute certainty, "I'm not sitting in the middle of a wall."
This kind of hypothetical sensor would justify
that the weight of that particle that's in the middle of the wall would get weight 0, so you just kill it.
Okay. A couple more questions from Drew.
What about dynamically adjusting our big end, our number of particles
when we want to trade off between computational cost versus the accuracy of our filter?
Dynamically setting the number of particles has been done quite a bit,
and it's a good idea under certain circumstances.
Obviously, the fewer particles you have the faster you can compute.
If you're tracking really well and all the particles are centered in one location,
there isn't really a need to have as many around as when you're globally uncertain.
They way to set the number of particles is often done by looking
at the total non-normalized importance weights.
If all your importance weights are really large, then you're probably doing a great job tracking,
and you don't need that many particles.
Whereas if your importance weights are all very small,
then chances are you're doing a really lousy job tracking, and you need more particles.
That isn't perfect. An unlikely measurement can cause weights to be small,
but a good heuristic would be to say, let's particle sample
until our non-normalized importance weights reach a certain threshold,
and then let's stop sampling.
Now truth telling, many of the systems we're dealing with are real-time systems,
and you can't really afford using many particles sometimes and few other times,
because there's a fixed amount of time in which you want to do your estimates.
Then yes, it's more tricky, but in principle using few particles when you track well
is a very viable solution.
Thank you. Taka also had a question.
He wants to know how to distinguish between moving landmarks and non-moving landmarks.
The maps that we dealt with in class were all static, and the landmarks were fixed.
How does the Google car distinguish between these moving vehicles,
moving people, and these static landmarks?
That's a wonderful question.
First of all, the Google car assumes that the ground map,
like the surface map of the street, is basically fixed.
If lane markers would move along a little bit, then the Google car would probably get confused--
a little secret here--so please don't repaint the lane markers when the Google car comes by.
That's treated differently than stuff that sticks out of the ground,
and even that is used as a landmark.
What we do is we have a probabilistic threshold that says what's the chance of this thing being mobile or not?
We do this by establishing correspondence, which means we take measurements a time step earlier
and measurements a time step later, see which has the most likely
correspondence between these two measurements
and then see if there's a motion vector in between.
Sometimes we can explain it away by just noise, but for cars and people and so on,
there is very often a very clear and strong motion
in which case we assume this thing is moving and tracking.
It also turns out that the way we build our prior maps is sometimes we drive by multiple times.
We do differencing, and then we have most captures are static things in our maps.
We happen to know that in the middle of a street, there tend to be no static things.
There tends to be just moving things.
You can bias the estimate toward saying, well, in the middle of the street
what we'll see is likely not static.
Tossing this all together gives us a fairly good tracker.
Thanks a lot. That's all we had for this time. We'll see you all next week.
But I want to make a comment.
I hear that many people really positively received the homework assignment on particle filters,
which is great. It took me a while to make it.
On the discussion forum there is a posting of a graphical version of it,
and I downloaded it. It looks really great.
I couldn't get the curser keys to work on my computer, but it's a really great basis to visualize.
I think particle filters are really hard to understand without visualization,
so I'm really sorry that our current programming environment doesn't provide visualization.
I hope in the next round, we'll fix that. I'm pretty sure we'll fix this.
So please play with it.
The other thing I noticed in the discussion boards, and I wanted to just call for feedback,
and the same for the Facebook group, that people want harder homework assignments.
I'm not sure that's true universally, so if you have an opinion, why don't you just post it.
I'd like to get a sense of it.
I'm thinking of making an assignment where we toss everything togethera
and really build like a mini version of an actual car.
That's going to be really involved, so let me know what you feel like.
This course right now, I would argue, is really Stanford caliber.
What you guys are doing, and you girls are doing, is really
at a quality that I would expect my best Standford students to do.
The type of things you implement, certainly, is at the same pace I would teach at Stanford
and possibly faster.
But if I go to a general build-a-robot example, then I'm going to exceed beyond Stanford base.
It's up to you. Let us know.
All right. Keep us posted. I'll be reading the forums. I'm sure Sebastian will too.
Thank you very much and see you next week.
All right.
