# LAB 09
## Problem description
The problem consisted in writing a local-search algorithm (eg. an EA) able to solve the *Problem* instances 1, 2, 5, and 10 on a 1000-loci genomes, using a minimum number of fitness calls.
In order to do so, we had to obtain an individual in our population with fitness = 1

## Our approach
We started thinking about how we could mantain some diversity among our population. 
We decided to implement an algorithm following the island idea.

In order to do so, we generated xxx different population of xxx individuals each and made them evolve (recombination using the crossover function and mutation) separately, exploiting *migration* every xxx "separated" generations.
After each era (= num of generations on separate islands), we selected the 2 best individuals of each island and put them in another island, randomly. After this operation, the separate evolution would take again place and so on.

## Initialization
We decided to initialize the population randomly and distributing the individuals on the different islands.


## Our results
Unfortunately, we didn't manage to achieve good results. We tried different combinations of NUM_ERAS, NUM_GENERATIONS_PER_ERA and population dimensions but our results were still saturate to a non-optimal fitness value.
We thought the islands approach was a good idea but, looking at our results, we probably got something working not properly.


Problem(1) -> fitness(best individual) = 1.0 with 65950 fitness function calls
Problem(2) -> fitness(best individual) = 0.884 with 150100 fitness function calls (stopped because reached 200 eras)
Problem(5) -> fitness(best individual) = 0.436 with 150100 fitness function calls (stopped because reached 200 eras) (stalled from 39º era)
Problem(10) -> fitness(best individual) = 0.33 with 150100 fitness function calls (stopped because reached 200 eras) (stalled from 69° era)


## Contributing
Made with the contribution of Gregorio Nicora s310820