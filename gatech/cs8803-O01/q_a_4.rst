1 - Office Hours Week 4
=======================

Hello, and welcome to the fourth Office Hours.
We've had a lot of really good discussion in the forums and some great questions.
Let's start with a question from Michael.
He asks, "In the last office hours, you mentioned something
about the possibility of a project at the end of the class.
What are your thoughts on the students building a robotic car?"
I just recorded the final class, and I actually spent some time putting everything together
into a simulation of a car at the level we've been operating--not a real car.
Honestly, it took me a whole day to put this all together.
It's substantial work, because at the surface these pieces fit together nicely,
but when you put them together, you realize that what the planner generates is not quite
isn't quite exactly what the controller really wants.
Tuning those parameters was actually a challenge,
but what I've done is for the final class, I'm giving you the environment first
and saying solve the problem of driving a car from A to B.
If you're really so inclined, you can go out and really try it,
but as the class goes on I give you most of my implementation, leaving bits and pieces out.
Then you can go and plug those bits and pieces and and hopefully make it work.
Unfortunately, I can't really give you a real car. That's the real fun thing.
As we'll see in the final example, the methods that we discussed are the core methods.
They give you a good path, but they won't give you a path good enough for actual driving.
There's a lot of work that goes beyond this class that could be done
to make things smoother and more elegant. Perfect.
Tangled asked, "In the Unit 4.14 video, you mentioned something about the other cars honking."
He wants to know if Junior can here.
Does he have a microphone sensor that affects his actions, and can he honk himself?
[Sebastian:] None of our cars hear, and none of our cars honk.
I know in certain parts of the world that's a recipe for not driving confidently and safely in traffic,
but we chose not to make audio communication part of that experiment.
George asked, "While it's possible to constantly re-plan
if enough computational power is available,
A-star assumes a static and deterministic world."
Can you comment on some of the possible pitfalls of using A-star?
And what are some of the alternatives to this algorithm?
Those are great and really deep questions,
to which I've dedicated a number or research years, it turns out,
and I've graduated a number of PhD students on that very topic.
A-star gives you a taste of how cool planning can be,
but there are many, many opens problems.
For example, A-star cannot deal with branching outcomes where you flip a coin,
and you have to pursue both outcomes. It just doesn't work.
It cannot deal with information gathering.
Sometimes in planning what you want to do is take
a specific action just for the sake of a reducing uncertainty.
For example, if I am going to a grocery store, and I don't know whether I have money with me,
I might just check, do I have my money here, and this checking action
has no other bearing than informing me that my money is in my pocket.
That is completely not doable with A-star now.
The dynamic programming stuff that I discussed has that flavor.
You can actually pursue multiple outcomes and bring them together.
It is computationally very inefficient, so you have to basically go over the entire state space.
The fact that we wrote the universal plans is just
a side effect of pursuing every possible combination.
The moment the state space gets very large, dynamic programming doesn't scale.
It's a big, open issue.
Now, if you go to something like Google Maps, what you'll find is
that you can do instant path planning between two points.
What Google has been doing is pre-caching a lot of the principal sub-plans,
so the remaining planning problem of finding the shortest path becomes mostly a table lookup.
They've done this in a way that's actually optimal.
They can prove it's optimal for path planning.
It's really an amazing achievement that's way beyond A-star.
The planning field is much more interesting than the lecture alluded.
I just want to get your juices flowing to have you use one.
Now, we did use A-star in our world,
and the way we addressed re-planning in the current environment
is that we just plan really, really fast.
We had a version of A-star that was super fast.
If we saw something new, it would just re-plan, and that was just fine for us.
You mentioned something about dynamic programming just now,
and a student had a very good question about that.
How large is the planning policy for Junior?
In Junior's case and the Google self-driving car cases,
we don't do that much planning.
We basically plan only within the visual horizon of the vehicle horizon of the vehicle itself.
We don't address the problem of how to get from here to Paris or what streets to take
We assume that's solved by Google Maps.
We assume a fixed route in all our driving, but once the fixed route is speced out,
all the planning that takes place is within the visual range of the robot.
They are typically 3-dimensional state spaces.
They're typically x, y, and orientation.
Now, in some of our experiments we also use velocity as a state variable,
because sometimes you want to take a little detour so you can straighten and be faster,
but they are relatively low-dimensional spaces.
Okay. Another question from George was about prohibitively expensive left turns.
Are the costs of actions--are these a dynamic variable
that's constantly being updated or are they static within the car?
The way we've handled the cost of action is we have a version that looks
at the global picture--like go from A to B and find the cost there--
then zooming back to the local picture.
And the local picture variable is to actually consider cars right now at this moment
whereas in the global picture we assume a static world,
and we make a fixed cost for left turns.
Now, as we go to the local picture, we do a lot of local roll outs,
local look-ahead plans--not dissimilar from A-star--
and then fill in the actual cost of left turns and replace them with the assume cost.
That's sometimes needs a different action.
There situations where we are planning to do a lane shift but we can't
because it's just too expensive right now.
We'd rather endure being stuck behind a slower car until the lane shift is cleared.
There's an interplay between two levels of planning going on.
A student wants to know about multi-goal environments.
An obvious example of a multi-goal environment would be a parking lot.
I want to get to an empty parking spot.
That's a great question I should've asked you the students,
because it has a really nice and obvious answer, which is--here's the answer.
In A-star, you can certainly designate multiple states to be goal states.
Nothing prohibits this. You just have to make sure your heuristic is admissible.
It takes a value that is underestimating or at least estimating correctly
the distance to any of those goal states. Then it's just fine.
The same is true for dynamic programming. You can certainly have multiple goal states there.
Nothing in the formulation is a problem.
Talking about heuristic functions, a student had a question,
and I think a lot of people are wondering,
since this is really where A-star gets its speed in the choice of the heuristic function,
are they deduced algorithmically or are they just done with intuition or trial and error?
How do we decide?
That's a fantastic question.
That's actually a really deep question as well.
In the car domain, we actually calculate heuristic function,
and we have two heuristic functions we kind of superimpose.
Both of them get at the gist of the problem, but are much easier to compute.
Suppose we have an environment with obstacles,
and your planning space is 3-dimensional--your x, your y, and your orientation.
One way to do your heuristic is to ignore the rotational degree of freedom
and assume you're moving a disk in any direction.
Obviously, moving a robot in any direction is easier
than being constrained by the filters or the car.
This becomes now a 2-dimensional problem, and by going from 3 dimensions to 2 dimensions,
we can solve the entire problem in no time.
We plan in 2D and use the 2D planning result as a heuristic for the 3D planner.
The reason why it works is because 2D planning is so much faster than 3D planning.
That's on that is basically ignoring the physical constraints of the car
and going to a simpler car model which can move in any direction any time.
The second heuristic we're using looks at the 3D problem but without obstacles.
We can pre-plan the optimal action of a 3D robot that has turning constraints
in the 3D space--x, y, and orientation--to any goal location in advance--
we do this once and it's true forever--without any obstacles.
What this gets us is that sometimes to get in a certain target orientation,
you have to take a certain turn, and that turn has to be taken no matter what,
and obstacles will only make it worse.
If you compute this obstacle-free heuristic,
you sort of get an underestimate that gets only worse with obstacles.
You have an admissible heuristic.
We toss both of their heuristics in as heuristics in A-star,
and we get a speed-up of a planner easily of a factor of 10^10 in practice.
That's very interesting. Great.
So it's actually--I'm giving this as an example.
I don't want you to really implement those right now, but that shows you how deep this question really is.
If you can come up with good ways of cheating and solving
the problem by lessening constraint and do it much faster,
that tends to be a great heuristic for A-star.
All right. Thanks a lot. We had a lot of great questions.
I'm sure we'll have a lot next week.
Can you give us a little preview of what's coming in Units 5 and 6?
Yes, first I want to thank you for these questions.
I really appreciate how deep they are, and how much you connect with the material.
I think that's great.
I honestly personally much prefer them over questions
such as, "When can I buy my next self-driving car?"
I think is really deep material I'm trying to teach you,
and I love the fact that many of you are diving in and really deeply,
because that's what I want to enable you to do, to apply it in a deep way.
So keep these questions coming.
In Unit 5 and 6 I'll dive into control.
Control is now the art of turning these abstract, discrete, and chucky paths
into actual steering motion.
It's a continuous thing, because your steering is continuous, and time is continuous.
We're going to go away from the discrete world and into the continuous world.
In Unit 6 I try to toss everything together.
In Unit 6 we program, hopefully, a robotic car with my help
where we go all the way to localization at the same time
and path planning at the same time and control
and hopefully generate some actual trajectories by our simulated car.
Can't wait. I'm sure the students feel the same way. Thanks a lot.
See you in class.
