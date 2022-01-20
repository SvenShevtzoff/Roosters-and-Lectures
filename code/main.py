'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import random_alg
from algorithms.greedy_alg import greedy
from classes.schedule import Schedule
import copy


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule (greedy, random_alg, baseline)")

# loading in data
activities, roomslots, students, courses, rooms = load(
    "../data/rooms.csv",
    "../data/courses.csv",
    "../data/students_and_courses.csv")
list = []
k = Schedule(roomslots, activities, students)
for x in range(0,4999):
    schedule = copy.deepcopy(k)
    schedule = baseline(schedule)
    schedule.fitness()
    schedule = None

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "greedy":
    schedule = greedy(schedule)
elif sys.argv[1] == "baseline":
    schedule = random_alg(schedule)
elif sys.argv[1] == "random_alg":
    schedule = random_alg(schedule)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")
