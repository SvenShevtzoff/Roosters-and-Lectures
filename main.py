'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms import *

from fitness import *

import pandas as pd


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit(f"Specify the algorithm to make schedule (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students)")

# loading in data
courses, activities, roomslots, students = load("data/rooms.csv", "data/courses.csv", "data/students_and_courses.csv")

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule(roomslots, activities)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(roomslots, activities)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(roomslots, activities)
elif sys.argv[1] == "schedule_with_students":
    schedule = schedule_with_students(roomslots, activities, students, courses)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

print(schedule)