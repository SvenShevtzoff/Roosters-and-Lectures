# Second Algorithm

### Genetic Algorithm

For our second algorithm we decided to make a Genetic algorithm. This algorithm starts with a start state containing N random schedules (the population) and tries to improve on this. When a random population is made, the algorithm enters a loop and the best P schedules are chosen (where P < N). In this loop the Genetic algorithm will start by taking two schedules from the P schedules and then recombine these schedules into a new schedule. It does this N times and this will create a new (and hopefully better) population. The algorithm does this for X times and then takes the best schedule in the last pupulation

### Constraint relaxation

Like the hillclimber this algorithm also uses constraint relexation, this is no problem because the weakest solutions are also the non-feasable solutions and the weakest solutions will get eliminatied the quickest.

### The Child

A recombined schedule C is called a child of schedule M and F (or just child). By chance the child gets for every avalible roomslot an activity form M or F. When all activities are given a roomslot the child will mutate (and it will always mutate) where the number of mutations depents on the number of parents in the population P with the same fitness. 

### Results

The best result we had was a schedule with a fitness of 324 and it seems that how bigger you chose N the better result you get
