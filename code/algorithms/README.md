# Algorithms

The following algorithms are present in this folder:

- baseline.py: generates a random/greedy schedule and improves it using a hillclimber algorithm until valid (iterative);
- genetic.py: makes a population and by changing the worst schedules, improves the population (iterative);
- greedy.py: makes a schedule with activities and roomslots sorted by max students (constructive);
- hillclimber.py: starts with a single random start state and continously improves on that (iterative);
- randomise.py: makes a random schedule not accounting for anything (can be invalid) (constructive);
- simulatedannealing.py: Like the hillclimber only now detoriations can be accepted (iterative);
