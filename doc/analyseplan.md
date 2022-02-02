# Analyseplan

### Randomise: Vera
- opnieuw met alleen feasible oplossingen
- even aanpassen wat betreft constraint relaxation doen
- 1000 keer runnen
- geen parameters

### Greedy: Vera
- opnieuw met feasible oplossingen
- aanpassen wat betreft constraint relaxation doen
- 1000 keer runnen
- geen parameters

### Hillclimber: Sven
- 1000 keer runnen per parameter
- parameters: mutations = [1, 3] max_change_count = [100, 250, 1000]

### Simulated annealing: Sven
- 1000 keer runnen per parameter
- parameters:  mutations = [1, 3] max_change_count = [100, 250, 1000], temperature interval = [1/1000, 1/10000]

### Genetic: Marc
- 1000 keer runnen per parameter
- parameters populatie_grootte[10, 20], best_children_amount[5, 10], aantal iteraties=[1000, stopconditie(s)]

---

## Output

File with dictionary with frequencies of fitness

Best schedule naar output