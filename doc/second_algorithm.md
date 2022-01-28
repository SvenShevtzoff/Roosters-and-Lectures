# First Algorithm

### Genetic Algorithm

For our second algorithm we decided to make a Genetic algorithm. This algorithm starts with a'random' start state containing N random schedules (the population) and tries to improve on this. When a random population is made, the algorithm enters a loop. In this loop the Genetic algorithm will start by taking the weakest two schedules (the mother and the father). When it has done this, it tries to make a better child (more on this later). The mother is removed from the population while the child takes her place in the population. By doing this the individuals in the population will get stronger every iterration.

### Constraint relaxation

Like the hillclimber this algorithm also uses constraint relexation, this is no problem because the weakest solutions are also the non-feasable solutions and the weakest solutions will get eliminatied the quickest.

### The Child

The algorithm makes a child by combining the roomslots of the father and the mother. Every iteration a roomslot of the father and a roomslot of the mother is chosen. By changce it is determent whitch roomslot will be given to the child. Near the end of an iteration almost all differen roomslots given to the child, the activitys of roomslots that are left over will be randomly given to the child in this way the child gets mutations.

### Technicalities

We run one iteration of the hillclimber algorithm until it does not improve for 1000 iterations. When this is reached, it will start over with a new random start state. The best solution overall will be recorded and returned at the end of the algorithm.

### Results

After a whole night of running the best solution found had 258 malus points. When comparing this with our baseline (mean of 1520) we see that this solution is significantly better. However, this algorithm still uses a form of the random algorithm used in the baseline, which results in the same biases mentioned there.