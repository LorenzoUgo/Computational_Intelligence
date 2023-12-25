# LAB 10
## Problem description
The problem consisted in writing an agent (**X player**) which is able to play tic-tac-toe exploiting 
reinforcement learning tecniques.

## Our approach
We adapted the initial solution of Professor Squillero to a solution we found on the internet.
The article can be found at [this link](https://towardsdatascience.com/reinforcement-learning-implement-tictactoe-189582bea542).
### State
We use as state *photograph* of each player's move at every time a player makes a move.
After ending each game we rate the list of moves that our agent has done with a positive rate
if it is a winning game.

### Action
The action is the actual choice of the move, which is done randomly and evaluated at the end 
of the game.

## Testing
We decided, in order to have some exploration also at test time, to have a certain
probability to make a random move instead of picking the highest rated in the dictionary 
built at training time. This is done by using the EXP_RATE variable.

It can be seen from the graph in the notebook that we're able to get 74% wins on average.

## Our results

We can see that, at the end, we can get decent results when playing against random player.

![Alt text](./results.jpg?raw=true "Title")

## Contributing
Made with the contribution of Gregorio Nicora s310820
