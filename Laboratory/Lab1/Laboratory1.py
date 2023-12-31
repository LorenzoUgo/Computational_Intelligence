from random import random
from math import ceil
from functools import reduce
from collections import namedtuple, deque
from queue import PriorityQueue

import numpy
import numpy as np
from tqdm.auto import tqdm

State = namedtuple('State', ['taken', 'not_taken'])

PROBLEM_SIZE = 50
NUM_SETS = 1000
SETS = tuple(np.array([random() < .3 for _ in range(PROBLEM_SIZE)])for _ in range(NUM_SETS))


def goal_check(state):
    return np.all(covered(state))


def covered(state):
    return reduce(np.logical_or, [SETS[i] for i in state.taken], np.array([False for _ in range(PROBLEM_SIZE)]))


def f(state):
    g = g_func(state)
    h = h2_funct(state)
    return len(state.taken) + h


def g_func(state):
    c = covered(state)
    return PROBLEM_SIZE - sum(c)


def h_func(state):
    punti_presi = covered(state)
    sette = [np.logical_or(punti_presi, SETS[s]) for s in state.not_taken]
    free_tessere = min(PROBLEM_SIZE - sum(s) for s in sette)
    return free_tessere


def h2_funct(state):
    punti_presi = covered(state)
    taken = 0

    while PROBLEM_SIZE - sum(punti_presi) > 0:
        min_val = numpy.Inf
        for s in state.not_taken:
            val = PROBLEM_SIZE - sum(np.logical_or(punti_presi, SETS[s]))
            if val < min_val:
                min_val = PROBLEM_SIZE - sum(np.logical_or(punti_presi, SETS[s]))
                s_min = s
        punti_presi = np.logical_or(punti_presi, SETS[s_min])
        taken += 1

    return taken


if __name__ == "__main__":
    assert goal_check(State(set(range(NUM_SETS)), set())), "Problem not solvable"

    frontier = PriorityQueue()
    state = State(set(), set(range(NUM_SETS)))  # ({taken}, {not_taken})
    frontier.put((f(state), state))  # [ ( {f=g+h}, { {taken}, {not_taken} } ), ]

    counter = 0
    _, current_state = frontier.get()
    while not goal_check(current_state):
        counter += 1
        for tiles in current_state[1]:
            new_state = State(current_state.taken ^ {tiles}, current_state.not_taken ^ {tiles})  # "^" == XOR
            frontier.put((f(new_state), new_state))
        _, current_state = frontier.get()

    print(f"Solved in {counter:,} steps ({len(current_state.taken)} tiles)")