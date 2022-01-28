# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================

from collections import defaultdict, Counter

import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.algorithms.hillclimber import hill_climber_alg_1000 as hc1000
from code.algorithms.genetic import genetic as gen
from code.algorithms.genetic import genetic
from code.algorithms.simulatedannealing import simulated_annealing as sa
from code.classes.schedule import Schedule
from code.visualize.visualize import visualize_student, visualize_course


if __name__ == "__main__":
    # # checking if algorithm is specified
    # if len(sys.argv) < 2:
    #     sys.exit("Specify the algorithm to make schedule (randomise, greedy, hillclimber, simulatedannealing, genetic)")

    # loading data
    activities, roomslots, students, courses, rooms = load(
        "data/rooms.csv",
        "data/courses.csv",
<<<<<<< HEAD
        "data/students.csv")
    schedule = Schedule(roomslots, activities, students)
=======
        "data/students_and_courses.csv")
    schedule = Schedule(roomslots, activities, students, courses)
>>>>>>> 6d8f4783ce20332ea41a37d503a2e9997b4bad84

    schedule.divide_students()
    
    def checker(schedule):
        # ac_dict = Counter([[x, x.activity()][1] for x in schedule.roomslots().list()])
        rm_dict = Counter([[x, x.activity()][0] for x in schedule.roomslots().list()])
        for x in rm_dict:
            if rm_dict[x] > 1:
                return 1
            else:
                return 2
            

    i = 0 
    for x in range(1000):
        print(x)

        best_schedule = randomise(schedule)
        if checker(best_schedule) == 1:
            i += 1
    print(f"i: {i}")



    # visualize_student(schedule, "52311353")
    # checking which algorithm is selected and making a schedule accordingly
    if sys.argv[1] == "randomise":
        best_schedule = randomise(schedule)
    elif sys.argv[1] == "greedy":
        best_schedule = gr(schedule)
    elif sys.argv[1] == "hillclimber":
        best_schedule = hc(schedule)
    elif sys.argv[1] == "hillclimber1000":
        best_schedule = hc1000(schedule)
    elif sys.argv[1] == "simulatedannealing":
        best_schedule = sa(schedule)
    elif sys.argv[1] == "genetic":
        best_schedule = genetic(schedule)
    else:
        # when no matching algorithm is found exit
        sys.exit('This algorithm does not exist, try: ["randomise", "greedy", "hillclimber", "simulatedannealing", "genetic"]')

    # print(f"Pandapunten: {best_schedule.fitness()}")

    # best_schedule.visualize_by_room(rooms)
    # schedule.visualize_by_room(rooms)
    # visualize_course(best_schedule, "Bioinformatica")
    # visualize_student(schedule, "52311353")
    # visualize_course(schedule, "Bioinformatica")

    # best_schedule.visualize_by_room(rooms)
    # schedule.visualize_by_room(rooms)
    visualize_course(best_schedule, "Bioinformatica")
    # visualize_student(schedule, "52311353")
    # visualize_course(schedule, "Bioinformatica")

    # best_schedule.visualize_by_room(rooms)
    best_schedule.output()
