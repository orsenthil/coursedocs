Problem Set 4
=============

1 - Admissible Heuristic
========================
Welcome to homework assignment #4 in CS373.
To remind you, we covered A-star and dynamic programming in class.
Let's start with an A-star question.
We learned in class that we can use heuristics,
and a heuristic is a admissible if the heuristic value is no larger
than the actual cost it takes to get to the goal.
In a maze, we know that the number of steps in the maze is a good heuristic,
because obstacles will make the path only longer, not shorter.
Consider a maze of size 3 x 3 and say there's a single goal state,
and the cost of moving is 1.
Is the function shown here admissible or not?
Please check one of the two radio buttons.

2 - Admissible Heuristic Solution
=================================
The answer is "yes."
In this part of the state space, we are obviously entering values that are too small,
but the heuristic is admissible if h(x) is lower than the cost-to-goal.
It would have been inadmissible if the values over here were much larger
than the values we want them to be.

3 - Admissible Heuristic 2
==========================
Here's another heuristic function for a 3 x 3 maze.
Assume again the cost is 1, and it's our sole goal state in the corner over here.
Tell me is this admissible?
Please check one of the two buttons here.

4 - Admissible Heuristic 2 Solution
===================================
The answer is "no,"
because these numbers over here are too large.
Why is this bad?
You can see that in a maze like this you would expand node over here
before we touch any of the nodes over here.
If those are an optimal path, then we might miss them
and pick what might end up being a suboptimal path
even though in this specific case all the paths seem to be equally good.

5 - Bad Heuristic
=================
Let me ask a more general question now.
What may happen if h, the heuristic, is not admissible?
A-star finds the optimal path always.
A-star may find a suboptimal path in some cases.
A-star may fail to find a path even if one exists.
Or none of the above.
In answering this question, it is important to say this is a statement that always applies,
and these statements suggest they just apply sometimes
under certain circumstances.

6 - Bad Heuristic Solution
==========================
There was only one correct answer, which is this one over here.
The inadmissibility of the heuristic might lead down an exploration of the state space
that leads to the goal on a suboptimal path.
Let me demonstrate this to you.
Here is a world. Suppose our start step is here. Our goal is here.
The heuristic is super large for those states over here
and smaller around here.
The nodes will be expanded following the zeros around here and around here,
and the first time the goal is set occurs when we reach the point over here.
We never discover the shortcut straight from S to G
because of the inadmissible heuristic.
That renders point 2 correct, and as a result
A-star will not always find the optimal path as I have just proven.
Now, it turns out A-star will find the path if one exists.
It might find a suboptimal path, but eventually it expands
all the nodes that can be reached.
If the goal state is among them, it'll succeed to find a path.
Therefore this answer here was wrong.
Of course, none of the above is also a false answer.

7 - Diagonal Motion
===================
I now what to quiz you about dynamic programming.
Consider the following 3 x 3 world with a goal state in the corner over here.
Say the value of the goal state is defined to be zero.
The cost of motion is 1.
Quickly fill in the values for all the other cells over here,
assuming you can either move straight or diagonally.
In both cases the cost of motion is 1.

8 - Diagonal Motion Solution
============================
The answer is 1 over here, 2 here, 3 here, 4 here.
This one also is resolves to 2 and 3.

9 - Stochastic Motion
=====================
[Sebastian:] Let me talk about dynamic programming with stochastic actions.
At the end of this assignment, you'll be able to program this.
The motivation to study this is as follows:
suppose we have a robot, and we have an obstacle and a goal state.
Then this robot might be tempted to scratch the wall over here and head towards the goal.
In practice this is a bad idea, because robots that get really close to obstacles are frightening.
In fact, if their actions aren't quite perfect they might actually hit the obstacle, which is no good.
In practice, what we tend to do is we go more like this.
We maintain a certain clearance to obstacles.
Now we're going to modify our dynamic programming planner to do just that--
to find paths that are a little bit safer and lead a little bit away from obstacles.
The way we will do this is we will model actions as stochastic,
and we have not done this before, but you'll learn how to do it.
Take the action of going north from the from the cell over here.
In a deterministic action, it obviously succeeds, unless of course we run into a wall.
In the stochastic case, it succeeds with a certain probability--say 50%--
whereas with 25% chance, it might accidentally go left or right
even though we commanded it to go up.
This is a stochastic action, and it's exactly the type of action I want you to program later on.
If, for example, there was a wall over here and the robot decided to go up,
there'd be a 25% chance it would hit the wall, which is not good.
So staying away from the wall is a good idea in a stochastic situation.
I will now show you how the backup works without asking or quizzes.
Suppose we study the action of going up over here, and we have a 50% of success.
Suppose at the time we do the backup, the value over here is 10,
20 over here, and 40 on the right.
Then the value of the state for the action "go up" would be obtained as follows.
It's a 50% chance times 10, 25% times 20, and 25% chance times 40 plus 1,
which is our motion cost, which together gives me 5 plus 5 plus 10 plus 1 equals 21.
That is the backed up value over here for the action go up,
and you can do the same with go right, go left, go down.
The interesting case in your implementation is the one for an action
that either runs off the grid or into a wall.
Let's study the case of going north from this cell over here
where there is a 25% chance of falling off the grid.
Then the value for the cell and the action of going north
is 50% times 20, which is 10, 25% chance times 40, which is also 10,
and then we have this case where we fall off the wall.
Let's define the penalty for falling off the grid or for hitting an obstacle as 100.
So we add 25% chance times 100 plus 1, 1,
hence the new value is 10 plus 10 plus 25 plus, which is 46.
I want your update to produce for the cell over here 46 for this specific action of going up.
Of course, the value might be smaller because there might be a better action
like the action of going right.
But for this specific calculation you should receive 46.
Your programming assignment looks as follows. I will give you a grid.
In this case it's a grid that's entirely unoccupied.
As before, I give you a goal state and a set of actions.
I want you to program dynamic programming all the way to the end,
so when I run it, the values I get are 0 for the goal state,
37 for the 2 adjacent states, and 44, 16, and 63.
If I go right to the goal, there is a 50% chance of hitting the goal,
in which case my cost is just one, which is the cost of motion.
There is 25% chance of running into the wall,
which costs me 100 plus, of course, 1 for the robot motion,
and there's a 25% chance I find myself down here, which costs us 44.
If I put this into mathematics, we get 50% chance for reaching the goal,
25% for hitting a wall, which costs me 100,
25% for going south, and the value here is 44.77 plus the cost of motion is 1.
If you add this all up, you get exactly the 37.193 that this value over here constitutes.
After conversions for this grid, I want the value function to look just like this.
Here is the corresponding policy.
If I modify the grid to insert an obstacle over here,
then I get a value function like this. One thousand is my initial value for each cell.
It's unmodified for the obstacle cell, and these are the values I receive--
94, 86, 73, and 44.
You can check whether these values are correct.
Let me pick a slightly bigger grid
with a goal position in the top right corner and two obstacles down here--size 4 x 4.
Here is my output for the value function. I can read those values.
They happen to be 1000 for the two obstacles.
What's remarkable is the policy.
When I'm close to the wall, you can see that I'm being pulled away
from those wall elements to stay in free space.
I will eventually reach the goal, but I never am willing to drive in a way
that crashes me into a wall if it's not avoidable.
What you have to do with the code we provide is to modify
the dynamic programming routine that assumes a deterministic action
with the one for a stochastic action.
Specifically, what this routine should do is it should incorporate
the probability of successful action and the collision costs.
For example, if I modify the probability of success into a deterministic function,
then my value function will look as follows.
It's just a number of steps in the usual way--1, 2, 3--as before,
and the policy drives me straight to the goal as shown over here.
In your final submission, please exclude any printouts
so we can modify the grid and these values for success probabiilty and collision cost,
and we can see what your code generates.
In the initial value function, please initialize your value function with 1000.

10 - Stochastic Motion Solution
===============================
Here is my solution.
As I go through all different actions a, as before,
I now create a new inner loop of going through different action outcomes.
This lists is (-1, 0, 1),
and I set the actual outcome to the adjacent action in the action list.
You might remember the action list is a list of different outcomes.
By incrementing it by 1 or decrementing it by 1, I can pick a slightly different action in that list.
Of course, I have to do the modulo 4 on the right side.
Then the limitation is similar to before. I project the outcome into new coordinates--x2 and y2.
Now I need to assign the probability with this outcome
where if they modify a 0, we take the success probability.
If it's not 0, we take 1 minus that divided by 2, because there are 2 possible undesired outcomes.
Then the test proceeds by checking whether this is a legal grid cell,
it's inside the grid, and the grid value is 0.
Then like before, I add the value of the grid cell
by now multiplying by the probability of that specific action outcome.
Otherwise, I do the same for the collision cost.
Finally, I take my cumulative value of v2, which I initialized with the cost of motion.
You can't see this right here, but it's filled up.
I update my value function just like before.
You can see the quote over here.
This is what you should have programmed.
The key difference to our example in class is the inner loop over here
where I go over different possible action outcomes,
compute the actual action outcome,
and then do the probabilistic addition of these outcomes rather than just studying one outcome.
