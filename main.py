# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================


import sys
from code.load import load
from code.algorithms import randomise
from code.algorithms import greedy as gr
from code.classes.schedule import Schedule
from collections import Counter
from copy import deepcopy
from code.helpers import swap_activities, move_students


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (greedy, random_alg, baseline)")

    malus_points = -1
    while malus_points == -1:
        #loading data
        activities, roomslots, students, courses, rooms = load(
            "data/rooms.csv",
            "data/courses.csv",
            "data/students_and_courses.csv")
        schedule = Schedule(roomslots, activities, students)

    print(f"pandapunten: {malus_points}")










