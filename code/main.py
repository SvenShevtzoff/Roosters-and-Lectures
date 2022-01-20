'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import random_schedule_one, random_schedule_two, random_schedule_three, baseline
from algorithms.greedy_alg import greedy_schedule_one
from classes.schedule import Schedule
import copy


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule \
             (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students, greedy_schedule_one, baseline)")

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
# for x in range 

if sys.argv[1] == "random_schedule":
    schedule = random_schedule_one(schedule)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(schedule)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(schedule)
elif sys.argv[1] == "greedy_schedule_one":
    schedule = greedy_schedule_one(schedule)
elif sys.argv[1] == "baseline":
    schedule = baseline(schedule)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")
