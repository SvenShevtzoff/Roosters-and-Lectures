# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================


import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms import greedy as gr
from code.classes.schedule import Schedule
from collections import Counter
from copy import deepcopy
from code.helpers import swap_activities, move_students
import random


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (greedy, random_alg, baseline)")

#loading data
activities, roomslots, students, courses, rooms = load(
    "data/rooms.csv",
    "data/courses.csv",
    "data/students_and_courses.csv")
schedule = Schedule(roomslots, activities, students)
schedule = randomise(schedule)
roomslot1 = random.choice(roomslots.list())
print(roomslot1)
roomslot2 = random.choice(roomslots.list())
print(roomslot2)
swap_activities(roomslot1,roomslot2)
print(roomslot1)
print(roomslot2)

malus_points = schedule.fitness()
print(f"pandapunten: {malus_points}")

schedule.visualize_by_room(rooms)
