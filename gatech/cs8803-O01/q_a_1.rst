1 - Office Hours Week 1
=======================
[Sebastian Thrun - Professor CS373, Andy Brown - Course Manager CS373]
[Andy:] Welcome to our first office hours. We've seen a lot of really good discussion in the forums.
Now we have Professor Thrun here with me--I'm Andy the moderator in the CS373 forum.
We're going to divide the questions into the course content questions,
and we're going to after that talk about some other questions--
things that are specific to Sebastian's work.
First course content question that a lot of people seemed to have questions about was
when we're talking about the sensing, you introduce these multipliers called
p_hit and p_miss, and you assign values 0.6 and 0.2.
People were confused about where those numbers came from.
[Sebastian:] This is something I just put in ad hoc when I explained it,
and later on they've become the measurement probabilities,
but I didn't want to start talking about probabilities without programming them first.
P_hit would be what's the probability of, say, being next to a door and really seeing it,
and p_miss will be the probability of being next to a door and not seeing it.
There is usually actually four of those.
There are four measurement combinations--
the probability of seeing the right measurement under there is a door
and if there is no door,
the probability of seeing the wrong measurement under these two assumptions,
but two of them are sufficient for the math.
[Andy:] In a related question about your own work, how do you assign these?
You said it was done ad hoc in this little example, but in really designing a robot car,
how do you decide on what these values are going to be?
Is it done experimentally? Is it based on the parameters of the sensors?
[Sebastian:] That's where a lot of meat comes in, and it's certainly meat I didn't really cover in class.
I do cover it in my book.
It depends a lot on the sensor.
So if we use a camera, I use a different model than if we use a range finder.
We use a lot of laser range finders.
If I was using a laser range finder--they measure distances--
and it's not p<u>hit/p</u>miss anymore, it's the probability of measuring
a certain distance in a certain location.
The very first approximation is physics.
You can actually derive what the centrifugal noise in the sensor and characterize those.
But when you just use physics, you often have a very poor ??? on the actual uncertainty,
so when tuning those parameters, you often do this very experimentally.
We go in and try out certain parameters to see which ones work
and then often soften them to make them fit the math.
[Andy:] The next question a lot of people had was does this method we're using
depend on the robot already having a map of its environment?
[Sebastian:] Localization does depend on having a map of the environment.
Everything I taught so far assumes there is a map.
There is an entire field called simultaneous localization and mapping--
or for short, SLAM--that addresses the general problem of acquiring a map at the same time .
I haven't covered this in class.
[Andy:] Those were two of the most heavily voted course content questions.
In a real localizer--I guess you sort of addresses this--but what are we looking for?
We're not looking for doors. We're looking for--?
[Sebastian:] In the Google self-driving car, which is a good example,
we actually have a map of the ground that is not that dissimilar from the way
Google Earth project images on the ground.
Then if you think about the robot having a laser camera, but a camera, that
produces local maps, and these local maps have some of the same features
like lane markings, as our global map.
And then we probability match question is one where we take the local map,
superimpose it over the global map, and see where it matches the best.
It's a search usually in x and y space.
It's also a little search on orientation space, because you might have your orientation slightly wrong.
The likelihood function that replaces our p_hit and p_miss
is then usually a correlation function that says how well does the local map
that you see right now match the global map.
When you shift it to the right position, it usually matches much, much better,
and as a result you get a much larger probability.
[Andy:] Some people were worrying about whether changing road conditions,
whether weather or lighting conditions, things like that,
would greatly affect the usability of the robot car.
[Sebastian:] That's a great question, and we discuss this every day.
Turns out that in certain weather conditions the car is relatively robust right now.
Rain, for example, changes the total appearance of the street,
and we can adjust this with a single constant factor that adjusts
the total brightness of the laser map.
Other things like a complete snow-covered street we have no solution right now it turns out.
What we're doing right now is we just don't drive in snow.
We live in California. There's not much snow here.
When there is snow, we just tell the driver not to use the system.
That's something we have to work on.
I think as we move into things like snow and very massive changes, we have to reference other features.
Maybe there trees around or other structures or rocks.
Typically, snow comes in the mountains so maybe there's mountainous structure.
And we have to toss some of that information into the system.
[Andy:] People are getting very excited in the forums.
They want to actually build their own robotic car.
Some questions have been how much is it going to cost?
If I can't do it because the cost is too high, can I get some Legos and build a robotic car that way?
[Sebastian:] There are a lot of kits you can buy.
I love Lego Mindstorm, is which a wonderful way to experiment with these things.
There are a lot of low-cost robot platforms you can buy.
I don't really recommend to hack into your car.
The reason is the moment you start snipping wires, your car might actually become unsafe.
If you do work with a car, make sure you never, ever
drive this car manually again or you know what you're doing.
We've actually been really tapping into cars,
and we've done things like decoding and understanding
how you use an electric steering booster to turn this in to steering motor
so that the car would be able to steer on computer command not just on human command.
But it's a lot of work, and it's actually very risky, so don't do it yourself.
Rather go and buy yourself a Lego Mindstorm or something similar and play with it.
You can actually study a lot of the same stuff using a Lego kit.
If you make a Lego robot move from the kitchen to the living room, that's actually really impressive.
[Andy:] One last question is for the people who are especially enthusiastic about robotics and AI.
How do you get involved in this field? What can someone do after taking this course?
[Sebastian:] Take this class.
As you know, we've been handing the CVs of our top students onto various companies
like Amazon and Twitter and Facebook and Google.
That's one way to get involved.
That doesn't work for everybody.
The way I got involved is, for one, I had a lot of toys that you could program.
I had a computer. I had little things to move around.
There was a construction set in Germany which I could play with as a kid.
Then I really started becoming a scientist.
I started publishing papers.
I started solving problems that the literature left open--
look into those and see if I could make a contribution.
At the age of about 22, I had my first big, big paper that was at a major conference.
That kind of started me to get into the field and got me really hooked.
The nice thing is I think there are many, many problems around you that require the same technology.
There's tracking problems, estimation problems all over the place, right?
So if you can't afford a robot, why not just by a web camera and put it in your kitchen
and have it, for example, track whether your cooking is good or bad?
That's something that everybody can do with the same technology.
Like today, most cooks occasionally boil water over and it makes your stove wet.
Can you build a system that prevents this?
That's a robotic task that uses the same technology.
If you do this and do this really, really well, you might start a business.
You might find other people to work with you.
You might show it to a professor, and if they got excited about it, they might publish it at a conference.
There are many, many ways into the system, honestly.
Just be creative about it.
[Andy:] It sounds like you're emphasizing you have to think like a roboticist.
That's, I think, what this class is going to help to do.
[Sebastian:] Yeah, what I'm trying to do is make people think like roboticists.
I'm extremely excited that in this class you get to program it yourself.
That's a new thing. When I was a student, I didn't have that possibility.
In our previous class you couldn't do it.
We are not at the point where you can drive your own robot around yet.
I hope to get to this point where we have a good robot simulator so you can play with this.
But we have enough stuff you can just buy.
Most importantly a camera--like a camera on a phone.
You can do localization on a hand-held phone in a room using images.
If you do a really fantastic job, you can start a company and sell it to one of the major players.
It's an open problem to the present day how to do this really well.
There's a lot of technology available today that allows you
to think like a roboticist and still solve the interesting problems--with this class, I hope.
[Andy:] All right. Well, thank you very much.
[Sebastian:] Okay. Thank you.
[CS 373: Programming a Robotic Car - Taught by Professor Sebastian Thrun]
[Udacity - udacity.com]

