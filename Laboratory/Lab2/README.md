 Nim Game Playing

This repository contains a Nim game implementation where the agent learns how to play the game using a genetic algorithm. The agent's strategy is defined by a genotype, and its performance is evaluated against a specified opponent.

## Nim Game

Nim is a two-player mathematical game where players take turns removing objects from distinct heaps or piles. The game ends when a player removes the last object, and the last player to make a move wins.

## Agent

The best agent is selected using an evolutionary strategy. The genotype of the agent defines its strategy, and the evolutionary strategy evolves a population of agents over multiple generations in order to improve their performance in playing Nim.

### Evolutionary strategy Components

- **Initialization:** A population of agents having as a genotype: first an array of probabilities to pick that specific row; second, a matrix representing for each row the probability of picking a certain number of element from that specific row.

- **Selection:** Agents are selected from the population based on their fitness: their success in playing against a specified opponent.

- **Evolution:** Some agents undergo mutation, where the genotype is modified summming random variable obtained by a gaussian mutation with a mutation step (σ=2), re-normalizing them each time to accomplish sum(all probability)=1.

- **Evaluation:** The fitness of each agent is evaluated by playing multiple games (100) of Nim against the opponent (pure_random).


# Agent Strategy

The agent strategy consists in taking the most probable number of element from the most probable row.
The behaviour for each agent is encoded in its genotype, which consists of two arrays: first an array of probabilities to pick that specific row; second, a matrix representing for each row the probability of picking a certain number of element from that specific row.

The strategy also includes considerations for edge cases. In fact when a row is empty the probabilities of the other rows are re-normalized. Instead, if some element are already missing from a row (not empty) the probabilities of taking a certain number of elements are re-normalized.

## Using a Different Evolution Strategy

We implemented (1+lambda), (1,lambda) and (mu+lambda) strategy. 
In the conclusion part, we are taking into consideration only the (mu+lambda) strategy.

Users can also tune our different strategies by adjusting population size (mu), offspring size (lamba), number of generations, mutation step (sigma) and number of row of the game.

## Conclusion 
The agent with genotype  has a winning rate on avarage of % against the optimal algorithm.
![Fitness of Agent vs Optimal over generation]()
![Win rates of 1000 matches divided in 100 games batches]()

## Contributing
Made with the contribution of Gregorio Nicore s310820