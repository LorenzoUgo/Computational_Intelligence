from random import choices, randint, choice, random
from copy import copy
import lab9_lib
import numpy as np

# GLOBAL PARAMETER #
NUM_LOCI = 1000
POPULATION_SIZE = 10
NEW_OFFSPRING = 15
TOURNAMENT_SIZE = 5
NUM_ISLANDS = 10
NUM_GENERATIONS = 5
NUM_ERA = 200

MUTATION_PROBABILITY = .35
NUM_MUTATION = 10

# . . . # Problem Definition + first individual # . . . #

fitness = lab9_lib.make_problem(5)
starting_population = [choices([0, 1], k=NUM_LOCI) for _ in range(1000)]


def inizialization():
    dim = NUM_LOCI//NUM_ISLANDS
    starting_population = [
        [
            [0 for _ in range(i*dim)] + choices([0, 1], k=dim) + [0 for _ in range((NUM_ISLANDS-i-1)*dim)] for _ in range(POPULATION_SIZE)] for i in range(NUM_ISLANDS)]

    return starting_population


def distribute_individuals(populations):
    galapagos = []
    individual_tag = [i for i in range(POPULATION_SIZE*NUM_ISLANDS)]
    for _ in range(NUM_ISLANDS):
        island_population = []
        for _ in range(POPULATION_SIZE):
            tag = choice(individual_tag)
            island_population.append(populations[tag % NUM_ISLANDS][tag % POPULATION_SIZE])
            individual_tag.remove(tag)
        galapagos.append(island_population)

    return galapagos


def mutation_one(ind):  # 1 loci(gene) mutated
    offspring = copy(ind)
    pos = randint(0, NUM_LOCI - 1)
    offspring[pos] = 1 - offspring[pos]  # Se ho T/F-> offspring[pos] = not offspring[pos]

    assert len(offspring) == NUM_LOCI
    return offspring


def mutation_n_random(ind):  # 2 loci(gene) mutated
    offspring = copy(ind)
    n = randint(1, NUM_MUTATION+1)
    for _ in range(n):
        pos = randint(0, NUM_LOCI - 1)
        offspring[pos] = 1 - offspring[pos]  # Se ho T/F-> offspring[pos] = not offspring[pos]

    assert len(offspring) == NUM_LOCI
    return offspring


def mutation_n(ind):  # Reset randomly a random number of loci
    poss = (randint(0, NUM_LOCI - 1), randint(0, NUM_LOCI - 1))
    offspring = ind[:min(poss)] + [choice([0, 1]) for _ in range(max(poss) - min(poss))] + ind[max(poss):]

    assert len(offspring) == NUM_LOCI
    return offspring


def mutation_reverse_n(ind):  # Invert a random number of loci
    offspring = copy(ind)
    poss = (randint(0, NUM_LOCI - 1), randint(0, NUM_LOCI - 1))
    offspring = ind[:min(poss)] + [1 - offspring[pos] for pos in range(max(poss) - min(poss))] + ind[max(poss):]

    assert len(offspring) == NUM_LOCI
    return offspring


def one_cut_crossover(ind1, ind2):
    cut_point = randint(0, NUM_LOCI - 1)
    offspring = ind1[:cut_point] + ind2[cut_point:]

    assert len(offspring) == NUM_LOCI
    return offspring


def two_cut_crossover(ind1, ind2):
    cut_points = (randint(0, NUM_LOCI - 1), randint(0, NUM_LOCI - 1))
    offspring = ind1[:min(cut_points)] + ind2[min(cut_points): max(cut_points)] + ind1[max(cut_points):]

    assert len(offspring) == NUM_LOCI
    return offspring


def uniform_crossover(ind1, ind2):
    offspring = [ind1[i] if i % 2 else ind2[i] for i in range(NUM_LOCI)]

    assert len(offspring) == NUM_LOCI
    return offspring


def crossover(ind1, ind2):
    offspring = [ind1[i] if random() < .5 else ind2[i] for i in range(NUM_LOCI)]
    assert len(offspring) == NUM_LOCI
    return offspring


def uniform_crossover_double(ind1, ind2):
    o1, o2 = (
    [ind1[i] if i % 2 else ind2[i] for i in range(NUM_LOCI)], [ind2[i] if i % 2 else ind1[i] for i in range(NUM_LOCI)])

    assert len(o1) == NUM_LOCI and len(o2) == NUM_LOCI
    return o1, o2


def roulette_wheel(population):  # Roulette wheel with same probability
    return choice(population)[0]


def roulette_wheel_fitness_weight(population):  # Roulette wheel with fitness as weight
    w = [ind[1] for ind in population]
    return choices(population, weights=w, k=1)[0][0]


def static_tournament(population):
    pool = [choice(population) for _ in range(TOURNAMENT_SIZE)]
    champ = max(pool, key=lambda ind: ind[1])
    return champ[0]

def best_parent_ever(population):
    champ = max(population, key=lambda ind: ind[1])
    return champ[0]


def genotype_distance(population):  # Select the 2 element with most different genotype
    distance = np.array(
        [[sum(np.bitwise_xor(np.array(population[i][0]), np.array(population[j][0]))) for j in range(len(population))]
         for i in range(len(population))])
    max_position = np.unravel_index(np.argmax(distance, axis=None), distance.shape)

    return population[max_position[0]][0], population[max_position[1]][0]


# TO BE DEFINED...
def distance_ind(population):  # Select the 2 element with most different genotype
    distance = np.array([[sum(np.bitwise_xor(np.array(population[i][0]), np.array(population[j][0]))) for j in range(len(population))]
         for i in range(len(population))])
    avg_distance_ind = sorted([(np.sum(ind)/(len(ind) - 1), i) for i, ind in enumerate(distance)], reverse=True)

    copy_population = [population[avg_distance_ind[ind][1]] for ind in range(len(population))]    # ORDERING FROM BEST TO WORSE
    return copy_population[:POPULATION_SIZE]  # SURVIVAL SELECTION


def survival_selection(population):
    population.sort(key=lambda ind: ind[1], reverse=True)  # ORDERING FROM BEST TO WORSE
    return population[:POPULATION_SIZE]  # SURVIVAL SELECTION


def remove_twin(population):  # Remove TWIN from the population because I belive that they will have the same fitness
    twins = {j for i in range(len(population)) for j in range(i + 1, len(population)) if population[i] == population[j]}
    new_p = [ind for i, ind in enumerate(population) if i not in twins]
    return new_p


def survive_only_the_best(population):
    population.sort(key=lambda ind: ind[1], reverse=True)  # ORDERING FROM BEST TO WORSE
    return population[:1]  # SURVIVAL SELECTION


# STANDARD ISLAND MODEL #
recombination_strategy = (one_cut_crossover, two_cut_crossover, uniform_crossover)
parent_selection_strategy = (roulette_wheel, static_tournament, roulette_wheel_fitness_weight)
survival_selection_strategy = (remove_twin, survival_selection)
mutation_strategy = (mutation_one, mutation_n, mutation_n_random, mutation_reverse_n)


def island(population):  #
    offspring = list()
    for counter in range(NEW_OFFSPRING):
        p1 = static_tournament(population)
        p2 = static_tournament(population)
        o = one_cut_crossover(p1, p2)

        if random() < MUTATION_PROBABILITY:
            # MUTATION
            o = mutation_one(o)

        offspring.append((o, fitness(o)))

    population.extend(offspring)
    population = remove_twin(population)
    # population = distance_ind(population)
    population = survival_selection(population)

    return population


# MIGRATION STRATEGY #
def migration(galapagos):
    migrants = 2
    individual_tag = [i for i in range(migrants*NUM_ISLANDS)]
    galapagos_best = [population[0:migrants] for population in galapagos]

    for ni in range(NUM_ISLANDS):
        chosen = []
        for _ in range(2):
            tag = choice(individual_tag)
            chosen.append(galapagos_best[tag % NUM_ISLANDS][tag % migrants])
            individual_tag.remove(tag)

        galapagos[ni].extend(chosen)

    return galapagos


def check_early_end(ind):
    if ind[1] == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    # galapagos_population = inizialization()
    # galapagos_population = distribute_individuals(galapagos_population)
    galapagos_population = [choices(starting_population, k=POPULATION_SIZE) for _ in range(NUM_ISLANDS)]  # N island
    galapagos_population = [[(ind, fitness(ind)) for ind in population] for population in galapagos_population]

    best_ind = []

    for era in range(NUM_ERA):
        # print("New era !")
        if len(best_ind) != 0:
            if check_early_end(best_ind[0]):
                break

        for g in range(NUM_GENERATIONS):
            # print("New generation !")
            i = 0
            if len(best_ind) != 0:
                if check_early_end(best_ind[0]):
                    break

            for p in range(len(galapagos_population)):
                i += 1
                if len(best_ind) != 0:
                    if check_early_end(best_ind[0]):
                        break

                # print(f'Isola numero {i}, generazione {g+1}, era {era+1} !')
                galapagos_population[p] = island(galapagos_population[p])

            best_ind = [p[0] for p in galapagos_population]
            best_ind.sort(key=lambda ind: ind[1], reverse=True)

        galapagos_population = migration(galapagos_population)
        print(era, best_ind[0][1])

    print(fitness.calls, "\n", best_ind[0][1])
