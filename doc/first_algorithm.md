# First Algorithm

### Hill Climber

For our first algorithm we decided to make a Hill Climber algorithm. This algorithm starts with a 'random' start state and tries to improve on this. When a random starting state is made, the algorithm enters a loop. In this loop the Hill Climber will start by making a mutation, more on that later. When it has done this, it checks to see if the state has improved. If that is the case the algorithm will simply continue with the mutated state. When it is the case that the algorithm has not improved, in other words the state has become worse, the mutation will be undone and the Hill Climber will start over and try to again make a mutation. This repeats itself and the state will become progressively better. 

### Constraint relaxation

Our randomise algorithm lost a significant amount of time by it generating non-feasible solutions ie. some student had 3 gapslots or the maximum amount of students in one tutorial was exceeded. In the randomise algorithm what would happen was that it just simply tried again untill a feasible solution was found. The downside of this is that it takes a lot of time. To make the Hill Climber faster we implemented constraint relaxation. This means, instead of rejecting the non-feasible solution, we gave a lot of malus points if the two rules mentioned before where broken. For every student that had 3 gapslots, 1000 malus points where counted and for every activity that had more students than allowed also 1000 malus points where added. This makes it so all solutions of a random state become in a way feasible. The strength of the Hill Climber is that is will quickly make mutations that get rid of those 1000 malus points added.

### Mutations

The algorithm had acces to two different mutations, one is swapping two activities' places. This could swap two activities or swap one activity with an empty roomslot. The second mutation is the moving of a student. This will move one student from one workgroup from an activity to another working group of the same activity.

### Technicalities

We run one iteration of the hillclimber algorithm untill it has not improved for 250 iterations. When this is reached, it will start over with a new random start state. The best solution overall will be recorded and returned at the end of the algorithm

### Results

After a whole night of running the best solution found was one with 258 malus points. When comparing this with our baseline (mean of 1520) we see that this solution is significantly better by a long waze. One thing to note, this algorithm still uses a form of the random algorithm used in the baseline, which results in the same biases mentioned there.