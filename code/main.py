'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import random_alg
from algorithms.greedy_alg import greedy
from classes.schedule import Schedule


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule (greedy, random_alg, baseline)")

# loading in data
activities, roomslots, students, courses, rooms = load(
    "../data/rooms.csv",
    "../data/courses.csv",
    "../data/students_and_courses.csv")

schedule = Schedule(roomslots, activities, students)

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

# schedule.fitness()
# schedule.visualize_by_room(rooms)

