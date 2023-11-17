import logging
from pprint import pprint, pformat
from collections import namedtuple
import random
from copy import deepcopy, copy
import tqdm
from matplotlib import pyplot as plt
from dataclasses import dataclass
import numpy as np

Nimply = namedtuple("Nimply", "row, num_objects")

N_ROWS = 5
ELEMENT_PER_ROW = 2*N_ROWS - 1
POPULATION_SIZE = 30
OFFSPRING_SIZE = 20          # λ
MUTATION_STEP = 2             # σ


class Nim:
    def __init__(self, num_rows: int, k: int = None) -> None:
        self._rows = [i * 2 + 1 for i in range(num_rows)]
        self._k = k

    def __bool__(self):
        return sum(self._rows) > 0

    def __str__(self):
        return "<" + " ".join(str(_) for _ in self._rows) + ">"

    @property
    def rows(self) -> tuple:
        return tuple(self._rows)

    def nimming(self, ply: Nimply) -> None:
        row, num_objects = ply
        assert self._rows[row] >= num_objects
        assert self._k is None or num_objects <= self._k
        self._rows[row] -= num_objects


@dataclass
class Individual:
    genotype: [list[float], list[list[float]]]
    fitness: float


def evolve_Individual(ind: Individual):
    new_population = [deepcopy(ind) for _ in range(OFFSPRING_SIZE)]
    #print(ind)
    for offspring in new_population:
        mutation_gene_1 = np.abs(np.random.normal(loc=0, scale=2, size=N_ROWS))
        new_gene_1 = offspring.genotype[0] + mutation_gene_1
        tot = np.sum(new_gene_1)
        offspring.genotype[0] = np.array(new_gene_1/tot)
        # - - - - - - #
        mutation_gene_2 = np.abs(np.random.normal(loc=0, scale=2, size=(N_ROWS, ELEMENT_PER_ROW)))
        for r in range(1, N_ROWS+1):
            for i in range(ELEMENT_PER_ROW):
                if i >= 2*r-1:
                    mutation_gene_2[r-1, i] = 0
        new_gene_2 = mutation_gene_2 + ind.genotype[1]
        tot = np.reshape(np.sum(new_gene_2, axis=1), (N_ROWS, 1))
        offspring.genotype[1] = np.array(new_gene_2/tot)

    return new_population


def fitness1(state):
    return  # ...


def game(my_player, opponent):
    nim = Nim(5)
    logging.info(f"init : {nim}")
    player = 0
    while nim:
        ply = strategy[player](nim)
        logging.info(f"ply: player {player} plays {ply}")
        nim.nimming(ply)
        logging.info(f"status: {nim}")
        player = 1 - player
    logging.info(f"status: Player {player} won!")

if __name__ == "__main__":
    first_player = Individual(
        genotype=[
            np.array([1 / N_ROWS for _ in range(N_ROWS)]),
            np.array([[1 / (2 * r - 1) if i < 2 * r - 1 else 0 for i in range(ELEMENT_PER_ROW)] for r in
                      range(1, N_ROWS + 1)])
        ],
        fitness=None)

    history = list()
    best_so_far = deepcopy(first_player)
    history.append(first_player)

    for n in tqdm(range(1_000_000 // OFFSPRING_SIZE)):
        # offspring <- select λ random points mutating the current solution
        offsprings = evolve_Individual(first_player)
        # evaluate and select best
        evals = Evaluate(offsprings)
        solution = offspring[np.argmax(evals)]
        if rastrigin(best_so_far) < rastrigin(solution):
            best_so_far = np.copy(solution)
            history.append((n, rastrigin(solution)))

    logging.info(f"Best solution: {rastrigin(best_so_far)}")

    history = np.array(history)
    plt.figure(figsize=(14, 4))
    plt.plot(history[:, 0], history[:, 1], marker=".")


