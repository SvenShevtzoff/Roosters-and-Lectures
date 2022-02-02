import sched
import sys
from collections import Counter
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms.baseline import baseline
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.algorithms.genetic import genetic as gen
from code.algorithms.genetic import genetic
from code.algorithms.simulatedannealing import simulated_annealing as sa
from code.classes.schedule import Schedule
from code.visualize.visualize import visualize_student, visualize_course
import copy
import operator

activities, roomslots, students, courses, rooms = load(
        "data/rooms.csv",
        "data/courses.csv",
        "data/students_and_courses.csv")

schedule_head = Schedule(roomslots, activities, students, courses)


dictionary = []

if sys.argv[1] == "baseline":
    for x in range(1000):
        print(x)
        schedule = copy.deepcopy(schedule_head)
        schedule.divide_students()
        schedule = baseline(schedule)
        print(schedule.fitness())
        fitness = schedule.fitness()
        dictionary.append(fitness)
    dictionary = Counter(dictionary)
    with open('alg_data/baseline_data.txt', 'w') as f:
        print(dictionary, file=f)
#   best_schedule.output("randomise")

elif sys.argv[1] == "greedy":
    for x in range(10000):
        print(x)
        schedule = copy.deepcopy(schedule_head)
        schedule.divide_students()
        schedule = gr(schedule)
        dictionary.append(schedule.fitness())
    dictionary = Counter(dictionary)
    with open('alg_data/greedy_data.txt', 'w') as f:
        print(dictionary, file=f)
#    best_schedule.output("greedy")

elif sys.argv[1] == "hillclimber":
    schedules = dict()
    for x in range(10000):
        print(x)
        schedule = copy.deepcopy(schedule_head)
        schedule.divide_students()
        schedule = hc(schedule, 1, 10)
        dictionary.append(schedule.fitness())
        schedules[schedule] = schedule.fitness()
    dictionary = Counter(dictionary)
    with open('alg_data/hillclimber_data.txt', 'w') as f:
        print(dictionary, file=f)
    best_schedule = min(schedules.items(), key=operator.itemgetter(1))[0]
    best_schedule.output("hillclimber")

elif sys.argv[1] == "simulatedannealing":
    schedules = dict()
    for x in range(10000):
        print(x)
        schedule = copy.deepcopy(schedule_head)
        schedule.divide_students()
        schedule = sa(schedule, 1, 10)
        dictionary.append(schedule.fitness())
        schedules[schedule] = schedule.fitness()
    dictionary = Counter(dictionary)
    with open('alg_data/simulatedannealing_data.txt', 'w') as f:
        print(dictionary, file=f)
    best_schedule = min(schedules.items(), key=operator.itemgetter(1))[0]
    best_schedule.output("simulatedannealing")
 
elif sys.argv[1] == "genetic":
    schedules = dict()
    for x in range(10000):
        print(x)
        schedule = copy.deepcopy(schedule_head)
        schedule.divide_students()
        schedule = genetic(schedule)
        dictionary.append(schedule.fitness())
        schedules[schedule] = schedule.fitness()
    dictionary = Counter(dictionary)
    with open('alg_data/genetic_data.txt', 'w') as f:
        print(dictionary, file=f)
    best_schedule = min(schedules.items(), key=operator.itemgetter(1))[0]
    best_schedule.output("genetic")
else:
    # when no matching algorithm is found exit
    sys.exit('This algorithm does not exist, try: ["randomise", "greedy", "hillclimber", "simulatedannealing", "genetic"]')