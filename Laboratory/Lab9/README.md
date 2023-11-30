Soluzione V0
    --> PARAMETRI GLOBALI:
            NUM_GENERATIONS = 50 - POPULATION_SIZE = 10 - NEW_OFFSPRING = 30 - TOURNAMENT_SIZE = 5 - NUM_ISLANDS = 3 - NUM_LOCI = 1000 - MUTATION_PROBABILITY = .15
    --> Generazione di individui fino a trovare l'individuo migliore (secondo <FITNESS>=1). No limiti sulle generazioni sviluppate
    --> Scelta probabilistica tra Mutazione (85%) e Ricombinazione(15%).
    --> Selezione del genitore con Roulette. Mutazione di 1 locus.
    --> Selezione dei genitori con tornei di dimensioni variabili e partecipanti random. Ricombinazione con crossover multiplo (casuale)
    --> Inizio la generazione generando 2 figli dagli individui più diversi (secondo <FITNESS>) che ho in popolazione
    --> Rimozione degli elementi con stesso <Genotipo>
    --> Classica selezione dei più forti. Scelta sia tra vecchia generazione, sia nuova generazione

Risultati:
    1)  Problema: 1 
        numero di chiamate alla FITNESS: 89130
        numero di generazioni necessarie: 2786
        tempo impiegato: 33 min
        individuo: [1, 1, ..., 1, 1] fitness=1.0

Soluzione V1
    --> PARAMETRI GLOBALI:
            ERA = 5 - NUM_GENERATIONS = 50 - POPULATION_SIZE = 10 - NEW_OFFSPRING = 30 - TOURNAMENT_SIZE = 5 - NUM_ISLANDS = 4 - NUM_LOCI = 1000 - MUTATION_PROBABILITY = .15
    --> 5 ERE di evoluzione delle isole di Recombination e Mutation + solo Mutation per l'isola Solitude
    --> 4 isole:
        - 1 Mutation: scelta della tecnica di mutation casuale. Esegue 50 generazioni.
        - 1 Recombination: scelta delle tecniche casuale ma bilanciata con pesi [0.5, 0,3, 0,1]. Esegue 50 generazioni.
        - 1 Champ: Solo recombination di tipo uniform_crossover. Genitore scelto con la roulette.
                   Pertita della popolazione orignale. Sull'isola restano solo i nuovi individui.
                   Dopo 50 generazioni, ciascunua isola mette qui il suo best individuo (secondo <FITNESS>). Esegue 1 generazione dopo le ERE delle isole M e R.
                   Mette il suo best individuo nell'isola S.
        - 1 Solitude: Strategie di Mutation e Recombination scelte in modo casuale. Genitore scelto con la roulette.
                      Alla fine sopravviverà solo l'individuo migliore (secondo <FITNESS>):
                        muta , ad ogni ERA, finchè è da solo;
                        ricombina quando, alla fine di tutte le ERE, qui viene aggiunto il best dall'isola CHAMP.

Risultati:
    1)  Problema: 1 
        numero di chiamate alla FITNESS: 120308
        numero di generazioni necessarie: 2000
        tempo impiegato: -- min
        individuo: [1, 1, ..., 1, 1] fitness=1.0
    
    2)  Problema: 1 
        numero di chiamate alla FITNESS: 120308
        numero di generazioni necessarie: 2000
        tempo impiegato: 44.1 sec
        individuo: [1, 1, ..., 1, 1] fitness=1.0



Soluzione V2
    --> PARAMETRI GLOBALI:
            NUM_GENERATIONS = 20 - POPULATION_SIZE = 10 - NEW_OFFSPRING = 30 - TOURNAMENT_SIZE = 5 - NUM_ISLANDS = 3 - NUM_LOCI = 1000 - MUTATION_PROBABILITY = .15
    --> 20 Generazioni di evoluzione delle isole di Recombination e Mutation + solo Mutation per l'isola Solitude
    --> 4 isole:
        - 1 Mutation: scelta della tecnica di mutation casuale. Esegue 1 generazioni.
        - 1 Recombination: scelta delle tecniche casuale ma bilanciata con pesi [0.5, 0,3, 0,1]. Esegue 1 generazioni.
        - 1 Champ: Solo recombination di tipo uniform_crossover. Genitore scelto con la roulette.
                   Pertita della popolazione orignale. Sull'isola restano solo i nuovi individui.
                   Dopo ciascuna generazione, ciascuna isola mette qui il suo best individuo (secondo <FITNESS>). Esegue 1 generazione dopo le 20 generazioni delle isole M e R.
                   Mette il suo best individuo nell'isola S.
        - 1 Solitude: Strategie di Mutation e Recombination scelte in modo casuale. Genitore scelto con la roulette.
                      Alla fine sopravviverà solo l'individuo migliore (secondo <FITNESS>):
                        muta, ad ogni generazione, finchè è da solo;
                        ricombina quando, alla fine di tutte le generazioni, qui viene aggiunto il best dall'isola CHAMP.
    
    --> Ciclo continuo fino a raggiungimento della fitness obiettivo

Risultati:
    1)  Problema: 1 
        numero di chiamate alla FITNESS: 111359
        numero di generazioni necessarie: 1869
        tempo impiegato: 37.7 sec
        individuo: [1, 1, ..., 1, 1] fitness=1.0

    2)  Problema: 1
        numero di chiamate alla FITNESS: 116363 
        numero di generazioni necessarie: 1953
        tempo impiegato: 45.5 sec
        individuo: [1, 1, ..., 1, 1] fitness=1.0


Soluzione V4
    --> PARAMETRI GLOBALI:
            NUM_GENERATIONS = 50 - POPULATION_SIZE = 10 - NEW_OFFSPRING = 30 - TOURNAMENT_SIZE = 5 - NUM_ISLANDS = 3 - NUM_LOCI = 1000 - MUTATION_PROBABILITY = .15
    --> Generazione di individui fino a trovare l'individuo migliore (secondo <FITNESS>=1). No limiti sulle generazioni sviluppate
    --> Scelta probabilistica tra Mutazione (85%) e Ricombinazione(15%).
    --> Selezione del genitore casuale. Scelta della tecnica di mutation casuale.
    --> Selezione del genitore casuale. Scelta della tecnica di Ricombinazione casuale
    --> Inizio la generazione generando 2 figli dagli individui più diversi (secondo <FITNESS>) che ho in popolazione
    --> Rimozione degli elementi con stesso <Genotipo>
    --> Classica selezione dei più forti. Scelta sia tra vecchia generazione, sia nuova generazione

Risultati:
    1)  Problema: 1 
        numero di chiamate alla FITNESS: 89130
        numero di generazioni necessarie: 2786
        tempo impiegato: 33 min
        individuo: [1, 1, ..., 1, 1] fitness=1.0

    2)  Problema: 1 
        numero di chiamate alla FITNESS: 92330
        numero di generazioni necessarie: 2885
        tempo impiegato: 29 min 10 sec
        individuo: [1, 1, ..., 1, 1] fitness=1.0