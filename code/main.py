# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================


import sys
from load import load
from algorithms.random_alg import random_alg
from algorithms.greedy_alg import greedy
from classes.schedule import Schedule
from collections import Counter
from copy import deepcopy
from helpers import swap_activities, move_students


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (greedy, random_alg, baseline)")

    malus_points = -1
    while malus_points == -1:
        #loading data
        activities, roomslots, students, courses, rooms = load(
            "../data/rooms.csv",
            "../data/courses.csv",
            "../data/students_and_courses.csv")
        schedule = Schedule(roomslots, activities, students)

        if sys.argv[1] == "greedy":
            schedule = greedy(schedule)
        elif sys.argv[1] == "baseline":
            schedule = random_alg(schedule)
        elif sys.argv[1] == "random_alg":
            schedule = random_alg(schedule)
        else:
            # when no matching algorithm is found exit
            sys.exit("This algorithm does not exist")

        malus_points = schedule.fitness()


    print(f"pandapunten: {malus_points}")










