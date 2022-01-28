# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================
import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.algorithms.genetic import genetic as gen
from code.algorithms.genetic_2 import genetic
from code.algorithms.simulatedannealing import simulated_annealing as sa
from code.classes.schedule import Schedule
from code.visualize.visualize import visualize_student, visualize_course


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (randomise, greedy, hillclimber, simulatedannealing, genetic)")

    # loading data
    activities, roomslots, students, courses, rooms = load(
        "data/rooms.csv",
        "data/courses.csv",
        "data/students_and_courses.csv")
    schedule = Schedule(roomslots, activities, students, courses)

    schedule.divide_students()

    # checking which algorithm is selected and making a schedule accordingly
    if sys.argv[1] == "randomise":
        best_schedule = randomise(schedule)
    elif sys.argv[1] == "greedy":
        best_schedule = gr(schedule)
    elif sys.argv[1] == "hillclimber":
        if len(sys.argv) == 3:
            best_schedule = hc(schedule, int(sys.argv[2]))
        best_schedule = hc(schedule)
    elif sys.argv[1] == "simulatedannealing":
        if len(sys.argv) == 3:
            best_schedule = sa(schedule, int(sys.argv[2]))
        best_schedule = sa(schedule)
    elif sys.argv[1] == "genetic":
        best_schedule = genetic(schedule)
    else:
        # when no matching algorithm is found exit
        sys.exit('This algorithm does not exist, try: ["randomise", "greedy", "hillclimber", "simulatedannealing", "genetic"]')

    print(f"Pandapunten: {best_schedule.fitness()}")
    best_schedule.output()
    # best_schedule.visualize_by_room(rooms)
    # visualize_course(best_schedule, "Bioinformatica")
    # visualize_student(schedule, "52311353")
