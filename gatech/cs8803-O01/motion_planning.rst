Motion Planning
===============

.. image:: https://dl.dropbox.com/s/k50n9yydv3x3gzp/Screenshot%202018-02-03%2012.14.28.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/7ssp2o4pcmx0x1y/Screenshot%202018-02-03%2012.16.11.png?dl=0
   :align: center
   :height: 300
   :width: 450


* The process of finding a path from start location to the goal location is called planning.
* Robot Motion Planning

Planning Problem
----------------

Given: Map, Starting Location, Goal Location, Cost

Goal: Find the minimum cost path

Compute Cost
------------

.. image:: https://dl.dropbox.com/s/z9um6zbfgxcm2k4/Screenshot%202018-02-03%2014.38.45.png?dl=0
   :align: center
   :height: 300
   :width: 450

Compute Cost 2
--------------

.. image:: https://dl.dropbox.com/s/emz2wsiokl25hjv/Screenshot%202018-02-03%2015.48.41.png?dl=0
   :align: center
   :height: 300
   :width: 450

Optimal Path
------------

.. image:: https://dl.dropbox.com/s/sbghgynlqwrwliu/Screenshot%202018-02-03%2015.50.53.png?dl=0
   :align: center
   :height: 300
   :width: 450

Optimal Path 2
--------------

.. image:: https://dl.dropbox.com/s/ltem6mqdlrhlsys/Screenshot%202018-02-03%2015.54.20.png?dl=0
   :align: center
   :height: 300
   :width: 450

Maze
----

.. image:: https://dl.dropbox.com/s/w8uiuuofky3ay2w/Screenshot%202018-02-03%2015.55.39.png?dl=0
   :align: center
   :height: 300
   :width: 450

Maze 2
------

.. image:: https://dl.dropbox.com/s/a6cu8ylez5ot8e3/Screenshot%202018-02-03%2016.05.28.png?dl=0
   :align: center
   :height: 300
   :width: 450

First Search Program
--------------------

.. image:: https://dl.dropbox.com/s/x8vez2r85611gaw/Screenshot%202018-02-03%2016.23.48.png?dl=0
   :align: center
   :height: 300
   :width: 450

.. image:: https://dl.dropbox.com/s/mnqkx66pagulk1s/Screenshot%202018-02-03%2016.26.04.png?dl=0
   :align: center
   :height: 300
   :width: 450

1 - Motion Planning
===================
Let's talk about motion planning.
The fundamental problem in motion planning is that a robot might live in a world like this,
and it might want to find its way to a goal like this
and has to device a plan to get there.
This same problem occurs for a self driving car
that might live in a city near a highway on a network of streets.
It has to find its way around and navigate to its target location.
If we zoom in and look at this intersection,
and this is my best rendering of a street-light environment.
We have also planning problems here.
Picture a car coming from here that wishes to go over here.
To take a left turn on this intersection over here,
this car would have to turn right first,
engage in a lane shift and then take the left turn to the goal location.
Now, a lane shift over here is a risky proposition.
If there's a bit truck parked over here,
the space might be insufficient to carry out the lane shift.
An alternative plan might be to go straight over here, take the detour around the block,
and then go straight to the target location.
The process of finding a path from a start location to a goal location
is called "planning."
For robots, it's often called "robot motion planning.
Today I'm going to talk about discrete methods for planning
in which the world chopped into small bins.
In the next class we're going to talk about continuous motion using those plans.
What's the planning problem? We're given a map of the world.
We're given a starting location.
We're given a goal location.
Usually, we're given some sort of a cost function.
The simplest way to think of cost is just the time it takes to drive a certain route.
The goal is find the minimum cost path.
Before we program anything, let me see if I can ask you a couple of questions
for minimum cost paths.

2 - Compute Cost
================
Suppose we live in a discrete world like this, and this is a world we'll be programming.
Let's for simplicity assume that the world is divided into little grid cells.
Our initial location is over here facing north or up.
This is the vehicle and the little arrow over here indicates where it's facing.
I'll call this "Start."
We wish to get to this area over here, presumably facing to the left side.
Let's assume at each time step I can either move forward or I can turn the vehicle.
I'm going to call these actions.
Each of those costs me exactly 1 unit of cost.
Then what's the total cost I have to endure to move from start to goal?
This is a number. Please put a number in here.

3 - Compute Cost Solution
=========================
The answer I want to see is 7 and not 6.
The reason why I want to see 7 is it takes 6 steps to go on the shortest path to the goal--
1, 2, 3, 4, 5, 6.
But in this cell over here I have to turn to the left side.
That turn also costs me a unit of 1.
That's in total 6 straight motions and 1 turn, gives me 7.

4 - Compute Cost 2
==================
Let me now change the action model into a different model.
We have 3 actions. Here is the first. I can go just forward.
The second one is I can turn left and then go forward.
The third one is I can turn right and then go forward.
In all of these actions, I take a step forward.
In the left one, I don't turn at all.
The center one over here I turn left and go forward.
This one over here I turn right and go forward.
Let's say for the time being the cost of each of those is 1.
What is now the total cost of the optimal path to the goal?

5 - Compute Cost 2 Solution
===========================
The answer is 6. We apply this action over here 3 times--1, 2, 3.
We're at this section over here.
Now we apply the left turn and go forward action, which is the center action over here.
We end facing over here. That's the fourth. Then we go straight again twice.
This action over here--5 and 6.
So we get a total of 6, as opposed to 7 when we counted the turning separately.

6 - Optimal Path
================
The reason why I change the actions this way is for my next quiz.
Suppose we punish left turns. Why would we do this?
Well, in real traffic, left turns are harder to do than the right turns.
Often you have to wait for oncoming traffic.
Let's say in our planning, left turns are more expensive.
In fact, I should mention that parcel delivery services
that plan for optimal routes of trucks like FedEx and UPS in the States,
they actually plan routes that try to avoid left turns during rush hours,
because it just takes much longer to do left turns.
If they can go right turns, they prefer those.
In this example here, let's now say that forward motion will cost you 1.
A left turn costs you 10, and a right turn costs you 1.
Now, what is the optimal path, and specifically what's the cost of the optimal path?

7 - Optimal Path Solution
=========================
This was a tricky question. It's 15 it turns out.
The path stays the same. I haven't punished left turns enough. Let me just try this.
If I were to go forward, forward, forward, left, forward, forward,
we accrue a total cost of 1, 2, 3, 13, 14, 15.
You can arrive at the same 15 by taking the 6 steps it takes to the goal
and add the extra 9 penalty it takes just for the turn itself,
which is 10 minus 1, and you get 15.
Let me look at the possible other path, which would take the loop over here
and avoid the left turn altogether--1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16.
The path around this loop over here has a cost of 16, which is more than 15.
We still prefer the left turn.

8 - Optimal Path 2
==================
So for this final version, let me punish left turns even more
Now they cost us 20.
What is now the total cost to get to the goal?

9 - Optimal Path 2 Solution
===========================
The answer is 16.
Now we're going to take the loop over here--
1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16.
With a cost of left turns this high, the left turn over here becomes prohibitively expensive,
and we'd rather take a detour on the right side
and do 3 right turns as opposed to 1 left turn.

10 - Maze
=========
Let me look at a different maze, and this is not a car example anymore,
but it's close to what we're going to program.
Suppose we start over here, and our goal is to go into this corner over here.
There are multiple blocked cells along the way.
In this case, we have a robot that can go up, down, left, or right.
How many steps does it take for the robot that starts over here
to reach the goal position?
Please enter your number over here.

11 - Maze Solution
==================
The answer is 7.
As you can see, the shortest path will lead along here.
Then it becomes ambiguous. We could either go right or up.
Let's say we randomly go up and hit the goal--
so 1, 2, 3, 4, 5, 6, 7 steps to the goal.

12 - Maze 2
===========
Let's look at the path planning problem as a search problem.
If you took my AI online class, you know what this is all about,
but I want to make sure that everybody can understand what I'm talking about.
Let's start with a little grid world of size 6 x 5
where our start location is in the top left corner, our goal in the bottom right corner.
I block off a few cells so there is still a safe path to the goal.
This could be a search through a city graph, through a parking lot,
or through a maze of streets for a mobile robot.
Just for simplicity, in this example let's assume the robot is given 4 actions.
It can go up, down, left, or right.
Also for simplicity, let's assume every action succeeds with absolute certainty.
We don't model uncertainty in this example.
The path planning or search problem is to find the shortest sequence of actions
that leads our robot from the start state to the goal state.
Just to check, tell me how many you think these are.
How many action are required to go from start to goal?

13 - Maze 2 Solution
====================
The answer is 11.
You go 2 down, 3 to the right makes 5, 1 up makes 6, 2 to the right is 8, 3 down is 11.

14 - First Search Program
=========================
The big question now is can we write a program that finds the shortest path from start to goal?
To do so, let's give the grid cell names.
We have 6 columns, named from 0 to 5, and 5 rows, from 0 to 4.
The basic idea I'll pursue is that I keep a list of notes that I wish to investigate further
or, as we call it in search, expand.
Let's call this list "open."
In the beginning we only have 1 state on this list at [0, 0]--my initial state.
Just to make sure I never pick this state again--I don't want any cycles in my path--
let me just check mark this state with a little red check.
I now can test whether this state is my final goal state.
Obviously, it's not. I'm not done with planning yet.
What I do next is expand this state.
I take it off my open list and look at all the successors,
of which there are 2 over here--[1, 0] and [0, 1].
Those two are now expanded, so I check them.
One last thing I maintain for each of these
states on the open list is how many expandages it took to get there.
This was 0 over here, and it's 1 for these 2 states in red.
That's called my "g-value."
When I'm done with planning, this will be the length of the optimal path.
Let's now go further and expand one of the two.
We always expand the one with the smallest g-value, but these are equivalent.
They both have a g-value of one, so it doesn't make a difference.
Let me expand the first one. This one over here.
This one has 3 neighbors--[0, 0], [1, 1], and [2, 0].
But because [0, 0] is already closed with a check mark, we don't consider it anymore,
which gives me [2, 0] and [1, 1],
both now with a g-value of 2, and we check those over here.
I now pick the node on the open list with the smallest g-value,
which happens to be this one over here. There's really no choice.
It's the node over here.
And this has 2 neighbors--[0, 0] and [1, 1]--but both are already checked.
Therefore, there is no expansion that takes place.
I only expand if I find an unchecked node.
The new open list are these two nodes over here.
What's going to happen is my nodes will expand gradually into the free space
until I eventually hit the goal node.
Without proof, the g-value when I hit the goal node will be exactly
the number of steps it takes to go from the start state to the goal node.
The secret here for that to be the case lies in the fact
that I always expand the node with the smallest g-value.
But we won't worry about this.
What I want you to do is to implement a piece of code
that implements what I just described.
To warn you, this is a bit of work. Here is my coding environment.
My grid is this one over here.
It's the same as the grid over here.
You can see the obstacles here and the T-shaped obstacle over here.
Our starting location is [0, 0], which is the first one you put on the open list.
Our goal happens to be [4, 5], which is the coordinate of the cell over here,
starting count of course at [0, 0].
I've also coded for you the 4 potential actions into a single field called delta,
so that when you go through the different successors on the list in the search
you can just go through these sequentially.
The first one goes up by subtracting 1 from this dimension.
The second one goes left. The third one goes down. The fourth one goes right.
Ignore for now the names of these actions. I will use them later.
I want to use the cost function of 1, so each step costs you exactly 1 for now.
I'd like you to write a piece of software that outputs triplets of this type
where the first value is the g-value and the next two are the coordinates x and y.
It then retrieves the element with the smallest g-value from the list,
expands it--the grid cells [0, 0] gets expanded to [1, 0] and [0, 1].
The g-value is incremented to 1 in both cases.
Then as I scroll down a little bit,
now it takes again one of the items with the smallest g-value,
breaking ties whichever way you want to break them. There's a tie over here.
I just happened to take the second one.
Expand this one into a new successor.
the only one that's not checked yet in the table is [1, 1], which gets a g-value of 2.
Now remove again the element with the smallest g-value, which is now the first one.
It's being taken down from the list over here
to produce a new open list that's sitting over here.
As it goes through this--I'm going to scroll down a little bit more.
You can see these different elements being taken.
You can see the g-value keep going up--3, 4, and so on, all the way to 7 here.
At the very end, when the g-value turns 11, it should expand node [3, 5],
which is this one over here, find it's only non-checked neighbor,
which is [4, 5]--this guy over here, and add to the list with the g-value of 11.
When it then looks at the remaining list and picks the one with the smallest g-value,
which is this one over here, it should identify that this is actually
the goal state and call the search a success.
Now, this is all intermediate debugging output.
What I want your code to output just for us to check
is just the final triplet of the g-value
and the coordinate of the very last item that is being retrieved.
This is the path length over here, and this is the coordinate of the goal,
which is the same as the one over here.
I want you to write the code to only output this one triplet over here.
Your code should output to this grid over here--[11, 4, 5],
and [4, 5] is the goal coordinates. There's nothing interesting here, but the 11 is the key thing.
It takes 11 steps to go from here to here.
If I change this, for example, by opening up this grid cell over here.
It now takes 2 steps less.
I want to see the 9 over here.
If instead I force a greater detour,
I see now a 15 over here for this maze where you have to go down,
left, up again, and down again.
If there's no way to reach the goal point,
as is the case if I block out this entire area over here.
Then I want the program to output "fail"--the single word "fail."
Please implement this using the algorithm idea that I've just given you.
It's going to be difficult. It's going to take you a while.
But if you do this, you're almost where I want you to be to learn about A*.

15 - First Search Program Solution
==================================
Here's my solution--I defined a function "search,"
which is the only function I'm going to run in the end. It's like the main routine.
To check cells once they're expanded so we don't expand them again,
I define an array called "closed" as the same size as my grid,
and it has two values, 0 and 1--0 being it's still open, 1 meaning it's being closed.
You could also use Booleans.
This over here assigns an array of the same size as the field grid.
I initialize the starting location as checked
and assign the coordinates to x, y, and a g-value of 0.
My initial open list is going to be just 1 element of my initial coordinates and the g value of 0.
So far what I've done is I've defined a array called closed of the same size.
All the check marks are not there except for the ones in the left corner,
and this is my starting location in my open list right over here with a g-value of 0.
Inside my code I use two flags--one is found,
which will be true when the goal position is found, and one is resign,
which will be true if I don't find a goal position and I've explored everything.
The second one will be the case when my open list just turns empty without finding the goal.
That's really important for the case where I can't find a path to the goal.
Those print commands were the ones I used to debugging.
You can look at them. They print out the existing open list. Nothing else.
But here is the code.
I repeat the following while I haven't found a path to the goal
and I haven't proven that the problem is unsolvable.
Both found and resign are false.
If my open list is empty, there's nothing to expand, then resign is true, and I print "fail."
This is one of the 2 terminating conditions.
You can convince yourself there's no path from S to G.
You'll expand every node on the left side
of the barrier until we finally run out of nodes to expand
at which point the open list will be empty, and our search failed.
If there is still elements in the open list, the else case comes into place.
Here is how I remove the element with the smallest g-value.
I use the list sort function, which sorts elements in increasing order
from the smallest g-value up.
Now I want to pop the element with the smallest number.
Unfortunately pop pops at the end, so I'll just reverse the list
and then pop the element with the smallest g-value from that list.
There's a little bit of a trick here. It's not very elegant.
It's also not very efficient, but it does the job for now.
That here gets me the element with the smallest g-value.
For that it's important that the g-value comes first in each of the triplets.
That's why I put it first, right before the x and the y.
I then assign the 3 values to x, y, and g, which is my expansion.
Again, g is the first, x and y are the second and third.
Now I'm in the position to test whether I reach the goal.
If x is the goal 0 and y is the goal 1, I'm done. I call found equals True.
I print out this triplet, and that gives me the triplet over here.
This "print next" over here is this triplet and that's the one I was looking for,
asking you about printing exactly this solution over here.
Now, if I'm not done yet, then here's the interesting case.
That's the meat of what I'm programming.
I'm going through all the possible actions. There are 4 of them.
Delta is an array of 4 different actions.
I apply the action to x and y with this addition over here
by applying the corresponding delta vector to construct x2 and y2.
If x2 falls into the grid and y2 falls into the grid and [x2, y2] is not yet checked,
which is tested by this field called "closed,"
and the grid cell is navigable--there is no obstacle here.
If all these things are correct, then I found an expansion that I now add to the open list.
I increment the cost from g to g2 by adding 1. In this case, cost is 1.
Then I append the new [g2, x2, y2] to my open list,
and I check the coordinate [x2, y2] so I never expand it again.
That is the recursion.
Put differently, when I drew down this element over here, for example,
I looked at possible ways the robot could move.
In my software, this means the robot has to stay inside the grid,
and the grid cell has to be unoccupied, which is this test over here.
I also check whether there was already a check mark by the cell,
which is this test over here. It is always true.
I added the new element to my open list
with the new g-value incremented and the new coordinates.
That is exactly happening over here.
I increment the g-value, and I add it with the new coordinates.
This is the key of a search algorithm.
The only remaining thing now is that I call the search routine
that prints me out this thing over here.

16 - Expansion Grid
===================
In the next programming quiz, I would like you to print out a table called expand,
which does not exist right now.
What expand is, is a table of the same size as grid
that maintains at what step each node was expanded.
So the very first node over here was expanded times 0.
The second node to expand was this one over here: 1, 2, 3, 4, 5, 6, 7.
In this table, every node that has never been expanded
including all the obstacle nodes should have the value of -1.
Like these guys over here - these are obstacles.
And when a node is expanded, it should get a unique number
that is incremented from expansion to expansion
and counts from 0, in this case, all the way to 22 for reaching the goal stated.
To give you a second example of how the quotes should work,
let me block off the goal by adding 1 over here
so there's an entire items that block the left side from the right side.
Now the switch fails, and in the expansion list you find
that all nodes on the right side have never been expanded.
You get 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
A little warning; this is not unique.
Depending on how you break ties you might expand in a different order,
so I don't expect your table to always look exactly the same way as this one over here.
So for example, you might have 0, 2 over here, and 1 over here
but what should be the case is when there is a full blockage
the right side should just never expand.

17 - Expansion Grid Solution
============================
And here is my solution.
Analogous to the closed table, I make an expand table
of exactly the same size but initialized it with -1.
I introduced a counter in the procedure that counts the expansion.
And then finally, there's a simple statement over here which implements all I need.
When I expand a note - the else statement - I set the expand index of the expanding note
to count, and I add 1 to the counter.
This constructs the table the way I want it.
When later on at the very end, I print out this table
using this command over here, I get the table down here.
So your implementation should show something just like this.

18 - Print Path
===============
Now I have a really challenging piece of software for you.
I would like you to augment this to print something entirely different,
which is the final solution.
This is nothing to do with expand,
and you have to implement a new delta structure for this similar to expand.
Here is the output I would like to see.
There is an arrow to the right, which is the optimal action to take in this cell over here.
Again, this is ambiguous.
There might be a different optimal action that is equally good,
but my software picked the one to the right.
Here I want to go down.
This little v over here is an arrow down.
An arrow to the right again, an arrow to the right, an arrow to the right,
an arrow to the right, down, down, down.
In the end we find a star, which indicates the location of the goal.
Let me modify the maze.
I'm closing up the wall over here, opening the wall down here, run it.
Here is my policy.
You can see in the grid this is the only way to make it to the grid over here.
You should write for me a piece of software that outputs this specific thing over here.
Part of this is the delta name that I kind of brushed over before.
These four symbols over here are the ones being used
to indicate arrows to the top, left, down, and right.
They correspond to the four actions over here: go up, left, down, and right.
So use those over here to print out the table over here.
It's very, very nontrivial to write this, as you will find out.
In the end it's not much code, but you have to carefully think about how to cache actions
and how to assign them to this table over here.
So take a while; do it.
It's challenging.
If you fail, not a big deal.
You can completely understand how the lecture works and not sure of the code
once you hit the submit button, and you move on.

19 - Print Path Solution
========================
So here is my solution.
I make a field called action of the same size as the grid,
where I memorize for each cell what action it took to get there.
So for example, if in the goal cell over here, it took an action of go down to get there
from the previous cell
then this cell over here would have the action index for the action down.
That's little a little bit tricky, but it turns out to be really easy to program.
In my node expansion routine, where I go from x to x2, which we talked about before,
I now add just a single command for the successive state x2 and y2.
I memorize the action it took to get there.
Notice I don't associate it with x and y, the from state.
The reason is in the from state I'm trying out many different actions,
and I don't yet know which one succeeds.
When I hit the 2 state and expand it for the first time
then this is going to be the expansion that's part of the optimal path.
So I associate the action with the successive state
not with the originating state over here.
Very subtle, very important.
If you got this right you know exactly what I'm talking about.
Now I have a field that memorizes for all these states over here
the action that it took to get in there,
but I don't have this wonderful representation as I have over here.
This will be compiled into a field called policy or plan,
which I initialize with blanks, but it is the same size grid as the field over here,
which I eventually print out down here.
In that field I set the location of the goal explicitly to be the star, resetting over here.
Then I go from the goal backwards.
I iterate from the goal location, x and y, now in backwards order all the way to the start.
Do this as long as x and y haven't become my initial location yet.
I apply the inverse action.
So I find the originating state by taking my current state
and subtracting the action exactly the same way I added it before using my action field
as finding out what action was actually being used.
In doing so the first time I do this, x and y was the goal state,
and x2 y2 become the state before.
I happen to know in the goal state that the action was a down action.
If I apply the negative of it I go up and find myself over here.
I then mark the policy field for the originating state
to be the special symbol associated with this specific action over here.
Then I recourse.
I set x and y to the state x2 y2, and I then go a step further.
In doing so I will reverse the path step by step, print the associated action,
and get exactly this state over here.
Very tricky, but look this is an advanced artificial intelligence class,
you might as well program something really tricky.
It took me a while to program it myself, but I finally got it right too.

20 - A*
=======
Now I want to come with you to the absolute meat of this class, which is called A-star.
A-star was invented by Nels Nelson at Stanford many years ago,
and is a variant of the search algorithm that's more efficient than expanding every node.
If you've gotten so far, and you understand the mechanism for searching
by gradually expanding nodes in the open list, A-star is almost the same thing
but not quite.
To illustrate A-star I'm going to use the same grid as before
but with a different obstacle configuration.
This is oine way A-star performs really well.
Obviously we are forced to go down to here,
but in here we still have to search for the optimal path for the goal.
Here is the same in problem code; you can see all the ones over here.
Start set is over here, goal set is over here.
If I run this code and give you my expand list, the ones you programmed before,
you'll find that the expansion goes down from here,
but then it expands into the open space.
Diagonally it expands into the open space and until it finally hits the goal node 15.
This took 16 expansions to get to this point.
Let me now switch on A-star and run the code again.
What we now find it only takes 10 expansions to get to this point, zero to nine over here.
So it expands down to four, but then it expands straight toward the goal
never touching this area over here, somehow magically knowing
that up here the path to the goal will be longer than going straight.
Now I didn't cheat.
I didn't tell it that there's a straight path over here.
So let me put an obstacle right here next to the goal and run A-star again.
What you'll find it does expand up to seven over here
but then moves to the second line over here,
expands up here, and then hits the goal again.
So it kind of does the minimum amount of work necessary
to make maximum progress to the goal.
That's A-star, and now we look into A-star in more detail.
A-star uses a so called heuristic function, which is a function that has to be set up.
If its all zeros then A-star resorts back to the search algorithm already implemented.
If we call the heuristic function h, then for each cell it results into a value.
So let me give you some values.
Here is one: Its number of steps it takes to the goal if there was no obstacle.
Clearly the number I'm putting in right now , 1, 2, 3, 4, 5, and so on,
are not reflective of the actual distance to the goal
because they don't consider the obstacles.
In a world without obstacles the heuristic function that I'm giving you
would actually measure the distance to the goal.
So the heuristic function has to be an optimistic guess how far we are from the goal.
So put differently, for any cell x y the heuristic function has to be an optimistic guess,
which means a smaller equal to the actual goal distance from the coordinate x and y.
Now that sounds a little bit ad hoc,
but very often you can give good heuristic functions really easily
like in this case over here.
If we just know that the agent can move left, right, up, or down,
it's really easy to say what is the number of steps it would take the agent
with no obstacles to get to the goal location, and that's this table over here.
That is easily generated automatically.
Now in reality this is an underestimate.
If obstacles, for example, look like this then from here it takes you more than 9 steps
to get to the goal.
It takes you 13 steps to over the hump over here.
Therein lies the beauty of the heuristic function.
It doesn't have to be accurate.
If it was accurate you probably already solved the planning problem.
There has to be a function that helps you understand
where to search next in the case of ties,
and it has to be just so that it underestimates or at best equals the true distance from the goal.
Many, many problems have functions like these in our self-driving car.
We use a function just like this; in fact the function I was just showing you,
we are using in our software for free-form navigation.
It boils down much to the number of which cell steps but for the Euclidean distance to a target location.
I hope you understand how heuristic function might look like.
It has many, many value heuristic function including setting everything to zero,
which would not really help me.
So let's work with this one heuristic function.
Here is the heuristic function in the code.
You can see the same heuristic function.
The key modification now for our search algorithm is really, really simple.
We again have an open list, and we add our state, we write down the g-value,
but we also write down the g-value plus the heuristic value.
G-value here is zero; heuristic value is 9.
So the sum of the two is 9, and I call this the f-value.
This is the cumulative g-value plus the heuristic value
as looked up in the table over here.
If I now expand I remove the element with the lowest f-value and not the lowest g-value.
That's all there is to A-star.
Let me give you an example.
Say we went to the open list all the way down here.
That is we expanded all these states over here,
and this is the one present here on the open list.
Our g-value will be 5.
Our heuristic will be 4, and the sum is 9 as before.
Let's now expand this node.
We get to this one over here, the g-value increases to 6.
G plus heuristic is still 9.
Now let's expand it more, and there's now two options finally:
This state over here and this state over here.
The one up here is called 3 2, the one on the right is called 4 3.
The g-value over here in both cases is 7,
but when we add the h-value we get a difference.
Up here we find the h-value to be 4.
We kind of moved a little bit away from the goal according to the heuristic.
That gives us a total of 11.
Whereas for the feed over here we find the h-value to be 2.
Here is the first time that A-star makes an actual difference.
It has a preference to expand this node over here over the node over here.
To see why the f-value, the sum of g and h, over here is 9 but over here is 11.
What this reflects is that, according to the heuristic,
this guy is actually 2 steps closer to the goal than this guy over here.
This guy, according to the heuristic, may be 2 steps away from the goal,
and the guy over here is at least 4 steps away.
A-star now will expand this node over here because its f-value is 9 versus 11.
So let's do this.
In expanding this node we find there is two valid neighbors:
the guy up here and the guy on the right.
The first guy's coordinate are 3 3.
The second guy is 4 4.
As before we increment the g-value by one.
It was eight in both cases.
Now we add the heuristic to the g-value, which for the first one over here is 3;
Whereas for the one on the right we get one as the heuristic.
That's the result of expanding the node over here.
Here is our new open list, and again we have a preference.
On the open list are these three states, and we prefer the one on the right
because its f-value is smaller than the other two f-values.
The one over here is 9; the ones over here have an f-value of 11.
So once again we expand, and in the expansion will be the goal state,
and then we find the goal set and we're done without ever expanding anything in the maze up here.
That feels like magic, but the key thing here is by providing additional information,
the so called heuristic function, we can guide the search.
When we have an impasse we can pick a node that looks closer to the goal state.
As a result we will likely make more progress towards the goal.

21 - Implement A*
=================
So with the heuristic function I've given you of simply the minimum number of steps
it takes to get to the goal in the absence of obstacles,
you can now construct an algorithm that implements a star
by maintaining not just the G-values but also the F-values,
which is G plus the heuristic.
Out should come an expand table that looks exactly like this
that are signs -1 not just to the obstacles but everything over here
that has not to be expanded according to the heuristic.
That's your task for the next quiz.

22 - Implement A* Solution
==========================
It turns out the actual implementation is really minimal
compared to what you already implemented.
With this modification you've implemented A-Star,
which is one of the most powerful search algorithms that they use for the present day
to drive self-driving cars through unstructured environments.
The very first thing we do is we expand elements in the open list
to not just contain g as before but also f.
I also included h over here.
That isn't necessary, but I did it anyhow.
So now we have five tubelets where g is defined as before.
H is the heuristic value of the cell x y, and f is the sum of the two.
The reason why I put f left is I need this for my sort trick
so that I can sort according to f when I sort the list.
So notice this has become two elements longer,
and by moving f to the left side I've implemented that the element I remove
will be the one with the lowest f-value not the lowest g-value.
As I go further down and expand the node as happened in these lines over here,
I now need to modify the index into the next structure a little bit.
X is now element number three, which is technically the fourth element in the list
when we start indexing with zero.
Y is element number four.
G is element number one.
F and h, I don't need to pop here because I compute them from scratch in just a minute.
So as I go further down where I expand a node from the list
and compute of all possible actions what the successive state is
and test whether these are legal states to expand.
I now, as before, increment g by the cross function but here two new lines of code.
First I compute the heuristic function for the new expanded node.
That's very straight forward.
I call it the h2.
Then the next line of code I compute the new sum of the g-value and the h-value.
I use those five things: the new f-value, the new g-value, the new h-value,
and the x and y of the expanded nodes to append to the open list.
So new here is most importantly the f-value but also the h-value.
That's all there is to implementing A-star.
So all I've done is I've just changed the logic according to which
I remove nodes from the stack to pick the one that has the minimum f-value
as opposed to the minimum g-value, and I have A-star.
So let me run it.
This is for the maze we looked at before.
Let me move the open spot to the top over here and put a wall back here.
It turns in this case A-star is not so efficient
and the area over here it has no preference to go either way.
It will finally find the go node.
That, however, changes when I put a big obstacle horizontally over here,
at which point it's really interesting to see A-star cannot decide whether
the horizontal path is best or the vertical path.
So it alternately pops nodes from either one of those.
The moment its over here the same trick applies as before.
It doesn't expand anything in the center anymore
and goes straight to the goal and reaches the goal over here.
That would not happen without A-star.
In fact, the way to rework back to the old search
is to give it an empty heuristic function.
So here is a definition of the heuristic function initializes h always zero everywhere
instead of the heuristic function over here, which I won't use for a second
and just call it heuristic old, and this is the current heuristic function.
If I run it with a heuristic function of all zeros I get back my original search algorithm.
You can see this search algorithm explores into the interior a little bit,
and the result expands more nodes than the A-star.
This might look very insignificant, but if you get to very large environments,
it can make a huge difference especially if there is a huge dead end somewhere
that can't reach the goal.
Then A-star performs much, much more efficiently than the simple search.

23 - A* in Action
=================
So here is an actual implementation from the DARPA Urban Challenge.
The Stanford trial car trying to find a way through a maze.
As you can see the maze is changing as the car moves.
This reflects of the fact that the car uses sensors to see obstacles,
and obstacles are sometimes included.
The car can only see them when they are nearby.
What's really remarkable here is that the car is able to
plan really complex maneuvers to the goal.
At any point in time we can see its best guess toward an open path to the goal.
The orange trees are A-star search trees.
They aren't exactly grid trees.
Our car moves differently from a grid-based robot.
It can turn at different angles, and each of these little steps is a different turning angle
combined with a different forward motion.
Leaving this aside you get these amazing trees
that find paths all the way to the goal using A-star.
This implimentation is so fast that it can plan these paths
in less than 10 msec for any location in this maze.
It was faster than any other driving team that I know of at the DARPA Grand Challenge
or the DARPA Urban Challenge.
The planning is repeated every time the robot cancels the previous plan.
You can see additional adjustments at place at times.
As you go through this video you can see how A-star planning
with a simple Euclidean distance heuristic is able to find a path to the goal.
When you implement this yourself the big difference
or grid implementation is a different motion model.
You have to implement a robot that is able to turn
and you have to write on the math of what it is able to turn and go forward.
This robot also can be reworked, so going backwards is a distinct different action.
Other than that it is essentially the same A-star algorithm you just implemented.
So if you want to build a self-driving car you now understand
to make a really complex, nice search algorithm to find a path to a goal.
So this is a scene where DARPA trapped our car using a barrier that went all across the street.
So the only way for the car to navigate this was to take a multi poled u-turn,
and it had to plan this all by itself using A-star planning.
The car pulls up to the barrier, realizes there's no path to go,
and invokes its A-star planner and comes up with a turn-around maneuver,
that is not particularly elegant, but it's super effective.
The car was able in this competition by itself to turn around using A-star,
find the optimal plan to do so, and move on.
Otherwise it would have been stuck forever behind this obstacle.
In this final video I'll show you a parking situation where the car has to back into a
parking space between two other cars, and you can see how the obstacles are visible,
how these other cars are visible, and how our vehicle, Jr, navigates an actual parking lot.
Again this is using A-star.
It finds its way optimally into this parking spot, backs in,
and backs out again all by itself.
The planning time for each of these A-star runs is less than 10 msec,
and the car was able to competently do this.
Even during the advance it had no clue where the obstacles were
and where the parking spot was.
That is A-star for robot path planning, and what you've implemented yourself is the core of it.
Again, if you want to turn it into a real robotic motion algorithm
you have to change the motion model.
You have to see the next class I'm teaching, when I go into
continuous models and I'm going to show you how to turn this into a continuous path.

24 - Dynamic Programming
========================
I now want to teach you an alternative method for planning.
This alternative method has a number of advantages and a number of disadvantages.
It's called dynamic programming,
and just like A-star, it's going to find you the shortest path.
You give it a map of the environment as in A-star, one or more goal positions--
let's assume just one goal position.
What it outputs is the best path from any possible starting location.
This planning technique is not just limited to a single
start location, but to any start location. Why would we worry about this?
Let me give you an example.
Suppose you are the Google self-driving car in an environment just like this.
You're in this little street over here, and you're asked to turn right,
but your goal is right over here.
As before, there are two different lanes over here--a left turn lane and a straight lane.
If you reach the straight lane, the only way to get to the goal
is to go around the block over here and proceed in this direction.
You've seen this example before.
Now, the point I want to make is a different one.
That is, your attempt to do a lane shift over here might fail. Why would it fail?
Well, it could be there's a big, big truck in this lane over here,
and as you go into the right lane when you're waiting for the truck to disappear,
there are these people behind you that honk their horns.
You really don't want to wait for the truck to disappear.
That means the environment is stochastic.
The outcomes of actions are non-deterministic.
In our planning so far we ignored this, but in reality that's the case.
In reality, you might find yourself--wow, I'm over here. How did that happen?
Well, it's happened because the world is stochastic, and this truck over here--
this stupid truck---didn't let you in.
What that means is you need a plan not just for the most likely position
but you might need a plan for other positions as well.
What dynamic programming gives you is a plan for every position.
If we redraw this environment as a grid with a goal location and certain obstacles,
they dynamic programming gives you an optimal action to do at every single grid cell.
As you can see, each grid cell now has a label.
That label is often called policy,
and policy is a function that maps the grid cell into an action
with the action in this case as a move left, move down, move right, or move up.
Now, we will compute a policy using dynamic programming.
That is, given a grid world like this and a goal state like that,
we will write software that will output for each of the grid cells
what the best thing is to do should the robot find itself there.
That requires a different algorithm than A-star.
It happens to be a more computation involved algorithm.
As I said before, it's called dynamic programming for robot path planning.

25 - Computing Value
====================
Let's look at a very simple piece of code that implements this planning algorithm.
We have a grid here as before with 0s and 1s. You're familiar with it.
The start location on the top left, the goal location on the bottom right.
We can set up arbitrary obstacles like a wall over here and a wall over here
that forces the robot into kind of an S-curve around the corner.
If I run this code with this table, what I get is a table that looks like this.
This for each of the states that is a non-wall state.
It tells me what's the optimal thing to do.
So over here it says go south. Here is says go right. Here is says go up.
Here is says go right again and go south.
Realize that even states I'm not likely to every reach,
like the one over here and the on over here, have an optimal policy
and action associated, because there is really no start state.
There is just a goal state over here.
The specification of the initial state has no bearing on this result.
How can we compute this efficiently?
Let me make a simple example of a world like this with an obstacle over here.
Say our goal state is the one in the corner over here.
Rather than telling you how to compute the optimal policy,
which assigns an action to each of these cells,
let me instead teach you about "value."
A "value function" associates to each grid cell the length of the shortest path to the goal.
For the goal, obviously, it is 0.
For each adjacent cell to the goal, it's obviously 1.
For the guys over here, 2, 3, 4, 5, 6, and 7.
This is recursively calculated by taking the optimal neighbor x-prime, y-prime,
considering its value, and by adding the costs it takes to get there,
which in our example will be plus 1.
By applying this update equation recursively,
we can attain this value function over here.
Once we have this value function, we find that the optimal control action
is obtained by minimizing the value, which is a hill-climbing type of action.
Let me give you a quiz.
In this world here with the goal location over here,
I'd like to understand what is the value of the cell in the bottom right.

26 - Computing Value Solution
=============================
The answer is 15,
because it takes 15 steps on the shortest path to go from here to here--
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, and 15.

27 - Computing Value 2
======================
What is the value of this cell over here?

28 - Computing Value 2 Solution
===============================
The answer is 3--1, 2, 3.
In fact, when you draw in all the values, you can see how the value propagates
in the structure and so on.

29 - Value Program
==================
Let's now implement something that calculates the value function.
Here's our familiar grid again.
We have a vertical obstacle over here, a T-shaped obstacle over here.
Our goal location is in the bottom right corner.
When I run it, I get this table over here, which is a little bit hard to read,
because I set the value for each obstacle in the grid to be 99.
So all the 99s over here correspond to actually obstacles in the grid.
From there on you see that the value of the goal location is 0--
1, 2, 3, 4, 5 for these two states over here, 6, and so on.
You should implement a function that takes this table as an input
and computes this table over here, which is unambiguous.
You should be able to output this exact table over here.
In fact, if I change the configuration--for example, open up a path over here--
then your function should compute a very different value function
where now we can see the value propagating straight to this line over here,
which wasn't the case before.
Before you implement this, as before I'm giving you the delta table
with different actions--up, left, down, and right.
I also give you something we'll be using in a later quiz
and the cost for the step is supposed to be 1.

30 - Value Program Solution
===========================
Here's my implementation, which should be relatively straight forward.
We have a value function that is the same size as my world,
and I initialize with 99 everywhere.
This has to be evaluated as large enough it doesn't conflict with any actual value.
I now update the value function a number times--I don't know how often--
but as long as change something, I update it.
Therefore, I introduced the variable "change," which I set to True in the beginning.
While change is the case, I update, but I neatly set change to False.
The only way to come back to True is that I actually changed something.
Now I go through all the grid cells in a fixed order.
It happens to be not very efficient, but certainly gets the job done.
I first check if the grid cell I'm considering is the goal.
Here is a typical case where I check for change.
If the value is presently correctly set to 0, I don't do anything.
If it's larger than 0, such as 99, then I set it down to 0, and I've just changed something.
Therefore, I set the change flag back to True.
If it's not a goal cell, then here is my full update function.
I go through all the actions.
I project a potential next state upon executing an action
by adding the corresponding delta to the x and y.
That gives me x2 and y2.
I test whether x2 and y2 are legitimate states.
For that they have to be inside the grid.
I check whether the numbers are larger than 0 and smaller than the dimension of the grid.
And it has to be an action that action navigable grid cell.
Therefore, I check that the coordinates in the grid has a 0.
If that's the case, I can propagate back the value.
My new value is the value of this future grid cell plus the cost per step,
which happens to be 1.
Now, if this value is better than the value I have already, which means it is smaller,
then I assign this new value to my original grid cell x and y, plus of course the cost step.
Then I know I've changed something.
Therefore I set change to "True," and the procedure repeats.
The only thing missing at the very end when I'm done,
I print out the value function using these commands over here.
I should warn you this is not very efficient.
The reason why it is not efficient is that value slowly propagates
from the end towards the beginning.
But leaving this concern aside, it actually computes the correct value function.
There are ways to make it more efficient.
It's also interesting to see what happens if I cut off any path to the goal.
The the resulting value function will retain 99s for most of the state variables--
exactly those where there is no valid path to the goal.

31 - Optimum Policy
===================
In this next quiz I'd like you to extend your software to print out the optimal policy.
That's happened over here.
If we look at the grid, there's an obstacle over here.
There's a T-shaped obstacle over here.
The goal is in the bottom right corner.
Obviously to get the goal, over here you want to go down
as indicated by these v's over here--down, down, down, down, down.
Up here you'll want to go either right or down.
Down here, in this little dead end, you want to go left, left, then up, and then right again
into this passage over here, up again over here, right, and down, down, down.
The optimal policy is ambiguous.
Sometimes there are multiple optimal actions.
For example, up here you go right or down.
For other places like the ones over here, it's not ambiguous.
There's only one optimal thing to do, which is going down.
I want you to write code that outputs this policy,
which is in many ways very similar to the path output by A-star.

32 - Optimum Policy Solution
============================
In dynamic programming, this happens to be really easy to program--
even easier than in A-star. Here is how I did it.
I defined a field called "policy" of the same size as my grid,
initialized it with lots of spaces.
Now in my dynamic programming procedure
check for whether we have reached the goal state, and we have.
Then I set the corresponding element to star,
using a single new command that just sets policy [x, y] to star.
Finally, in my big update loop where I assign an improved value to a grid cell [x, y]
based on its successor, I assign to the policy the character
that corresponds to the action that led to that update over here.
Put differently, as we look for a better value we look into all possible directions
by looping over all actions.
If one of those succeeds, I just memorize in my policy function what that action was
with a command over here.
If I finally know output this, then I get this field over here.

33 - Left Turn Policy
=====================
Let's now have some fun and apply this to an actual car problem.
The one I'll using is a bit simplified as always,
but it does relate to real world path planning as is done, for example, by Google Maps.
Suppose we have a car down here.
This car now has its state an x, a y, and an orientation, theta.
By orientation for simplicity is chosen from 4 possible directions--up, down, left, and right.
As I quiz you in the beginning, I'd like to get to the location over here, facing left.
Realize that now the state space is 3-dimensional, just like in our localization example.
I now would like to implement a dynamic programming planner
that gives me the optimal path for going from here to here
and that let's me play with cost functions.
There are three principle actions.
One is move in which the car just goes 1 grid cell forward in its present orientation.
It doesn't turn at all. That could be applied anywhere in the maze in any direction.
One is turn left and then move.
This car in this position in the cell over here could chose
the turn left and move, which makes it move over here.
The last one is turn right and move,
in which case it would, from this cell over here,
turn over here and head in this direction.
Here's our world again.
You can see there is a street over here that's navigable, one over here that's navigable.
You see the loop on the right side.
Remember that now this state space is 3-dimensional, not 2- dimensional.
Our goal is to move to cell [2, 0], which is the one over here.
Our initial state is up here,
and the initial state has not just a position of [4, 3] but also an orientation of 0.
It's a 3-dimensional state.
Here are my orientations--0, 1, 2, and 3.
The first one makes the robot go up, the second go left,
third one go down, and the fourth one go right.
Here are the names associated with it---up, left, down, and right.
This thing here is interesting.
As actions, we have 3 actions.
We can add to the index orientation -1, 0, or 1.
If we add -1 we jump 1 up in the cyclic array over here,
which is the same as doing a right turn.
For example, if you go from go left to go up, that the same as turning right.
If we add +1, that's the same as turning left.
If we leave the orientation unchanged,
then we go straight, which is indicated by this hash symbol over here.
These actions come with different costs.
Right now the left turn costs me 2, going straight costs me 1,
and going right costs me 1 as well, which, as we all know,
makes the left turn the preferred solution over here.
Indeed, as I run it, you can see how the car turns left over here to the goal location.
If I were to increase the cost for the left action to 20, then my solution changes.
You can see the car dashes straight ahead over here, turns right over here,
right over here, right over here, and then goes straight to the goal location.
That software I want you to implement. There is one more hint.
The value function itself is 3-dimensional, and here is the code that I've been using.
Not necessarily the most efficient, but it has inside 4 identical arrays
of the size of the grid concatenated into a megagrid
and initialized all by a very large value--999 in this case.
You need functions just like these, and it turns out this makes it more difficult to write the code.
This is our last quiz in this lecture.
Our last programming assignment, and you might spend some time.
It took me a while to program it myself to get an output just like this over here.

34 - Left Turn Policy Solution
==============================
Here is my solution, I have the value function initialized. It has lots of 999s.
The policy is a similar function in 3D.
Then I have a function called policy2d, which is the one I'm later going to print.
That's the same in 2D.
Scrolling down, my update function is exactly the same as before for dynamic programming
While change exists go through [x, y]'s and all orientations
of which there are 4, so it's now a deeper loop.
If you found the goal location, then update the value,
and if there's an actual update, set "change" to True
and also mark it as the goal location.
Otherwise, if our grid cell is navigable at all,
let's go through the 3 different actions and here's a tricky part
how to make the action work but it works beautifully.
We go through the 3 different actions.
When we tag the ith action,
we add the corresponding orientation change to our orientation modulo 4.
It's a cyclic buffer, so this might subtract 1.
Keeping it the same will add 1 to orientation.
Then we apply the corresponding new motion model to x and y to obtain x2 and y2.
Then over here is our model of a car that steers first and then moves.
Scrolling down further, if we arrived at a valid grid cell in that it's still inside the grid
and it's not an obstacle, then like before we add to the value
the value of this new grid cell plus the cost of the corresponding action.
This is non-uniform, depending on what action we pick now.
This improves over the existing value.
We set this value to be the new value, and we mark change as True.
We also memorize the action name as before.
This is all effectively the same code as we had before
when we did dynamic programming in a 2-dimensional world.
It gets us the value function, and it gets us the policy action.
However, I printed out a 2-dimensional table, not a 3-dimensional table.
To get to the 2-dimensional table, I now need to be sensitive of my initial state.
Otherwise, it actually turns out to be undefined.
Let me set the initial state to be x, y, and orientation.
All I do now is run the policy.
With the very first state, I copy over the policy form the 3-dimensional table
into the 2-dimensional one, which will be this hash mark over here.
While I haven't reached the goal state quite yet as indicated
by checking for the star in my policy table.
Now, my policy table has a hash mark R and L,
but otherwise is the same as before.
If it's a hash mark, we just keep our orientation the way it is.
If it's R, I turn to the right. L is turn to the left.
I apply my forward motion,
and I then update my new x and y coordinates
to be the corresponding after the motion,
and I update my orientation to be o2.
Finally, I copy the 3-dimensional symbol for my policy straight into the 2-dimensional array.
This is the array that I finally print.
The key insight here is to go from the 3-dimensional full policy
to a 2-dimensional array I had to run the policy.
That's something you would have done to get back this table over here.
That's somewhat nontrivial. I didn't tell you this, but I hope you figured it out.
But everything else is the same dynamic programming loop that you've seen before.

35 - Planning Conclusion
========================
A visualization of our Standford racing car, Junior,
in action, applying that exact same algorithm for actual driving.
You can see here that a right turn is being executed, followed by a lane shift.
These are discrete actions, and the car actually performs those
to reach a goal location at the orange circle.
But if we make a lane shift prohibitively expensive,
just as we made a left turn expensive before,
then the car chooses a different path.
It goes straight, then takes a left turn, which right now isn't that expensive.
It takes a left turn and a left turn again to find itself
in the lane where the goal location is located.
That is a result of modifying cost functions in our dynamic programming algorithm
in the same 3D regime we just studied and that you just programmed.
Your program could effectively drive this car, and by changing these cost function,
as you can see over here, the car would be able to attain its goal
in the optimal way, relative to the cost that you have given him.
Congratulations. You made it through my first motion class.
Today we assumed that the world is discrete,
and we looked at 2 planning algorithms--A-star, which uses a heuristic to find a path,
and dynamic programming, which finds an entire policy that has a plan for every location.
We implemented both of them.
In fact, in the policy case, even in 3D, which is quite an achievement.
I want to congratulate you to get here.
You really now understand two of the main paradigms
by which our robots make motion decisions,
and they are are also some very major paradigms for artificial intelligence in general.
In the next class we talk about how to turn this into actual robot motion.
We'll talk about continuous state spaces, and we'll talk about what's called "control,"
in which we make a robot move. I'll see you next week.

