from random import random
import numpy as np
from functools import *
from queue import *
from collections import *

PROBLEM_SIZE = 5
NUM_SETS = 10

SETS = tuple([np.array([random() < .3 for _ in range(PROBLEM_SIZE)]) for _ in range(NUM_SETS)])
State = namedtuple('State', ['taken', 'not_taken'])


def goal_check(state):
    return np.all(reduce(np.logical_or, [SETS[i] for i in state.taken], np.array([False for _ in range(PROBLEM_SIZE)])))


if __name__ == '__main__':

    #sets = tuple(np.array([random() < .2 for _ in range(PROBLEM_SIZE)]) for _ in range(NUM_SETS))
    assert goal_check(State(set(range(NUM_SETS)), set())), "problem not solvable"

    frontier = PriorityQueue()
    frontier.put(State(set(), set(range(NUM_SETS))))

    counter = 0
    current_state = frontier.get()

    while not goal_check(current_state):
        counter += 1
        for action in current_state[1]:
            new_state = State(current_state.taken ^ {action}, current_state.not_taken ^ {action})
            frontier.put(new_state)
        current_state = frontier.get()

    print(current_state)
    print(goal_check(current_state))

    print(f"Solved in {counter:} steps")

