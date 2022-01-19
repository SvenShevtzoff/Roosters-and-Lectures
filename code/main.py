'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import random_schedule_one, random_schedule_two, random_schedule_three
from algorithms.greedy_alg import greedy_schedule_one
from classes.schedule import Schedule


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule \
             (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students, greedy_schedule_one)")

# loading in data
activities, roomslots, students, courses, rooms = load(
    "../data/rooms.csv",
    "../data/courses.csv",
    "../data/students_and_courses.csv")

schedule = Schedule(roomslots, activities, students)

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule_one(schedule)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(schedule)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(schedule)
elif sys.argv[1] == "greedy_schedule_one":
    schedule = greedy_schedule_one(schedule)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

schedule.fitness()
schedule.visualize_by_room(rooms)
