# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================


import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.classes.schedule import Schedule
from code.algorithms.hillclimber import hill_climber_alg

ITERATIONS = 100


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (randomise, greedy, hillclimber)")

    # loading data
    activities, roomslots, students, courses, rooms = load(
        "data/rooms.csv",
        "data/courses.csv",
        "data/students_and_courses.csv")
    schedule = Schedule(roomslots, activities, students)

<<<<<<< HEAD
    # checking which algorithm is selected and making a schedule accordingly
    if sys.argv[1] == "randomise":
        best_schedule = randomise(schedule)
    elif sys.argv[1] == "greedy":
        best_schedule = gr(schedule)
    elif sys.argv[1] == "hillclimber":
        best_schedule = hc(schedule, ITERATIONS)
    else:
        # when no matching algorithm is found exit
        sys.exit("This algorithm does not exist")

    print(f"Pandapunten: {best_schedule.fitness()}")
=======
    hill_climber_alg(schedule, 1)
    # schedule = randomise(schedule)
    # malus_points = schedule.fitness()
>>>>>>> 651ec1cd580e4029ee41c1d3dc5b83f95230565a

    # print(f"Pandapunten: {malus_points}")

    # # schedule.visualize_by_room(rooms)
