# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================
import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.algorithms.genetic import genetic as gen
from code.algorithms.simulatedannealing import simulated_annealing as sa
from code.algorithms.baseline import baseline
from code.classes.schedule import Schedule
from code.visualize.visualize import visualize_student, visualize_course


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (randomise, greedy, hillclimber, simulatedannealing, genetic)")

    # loading data
    print("Loading data and making datastructure")
    print()
    activities, roomslots, students, courses, rooms = load(
        "data/rooms.csv",
        "data/courses.csv",
        "data/students_and_courses.csv")

    # making 'empty' schedule object from data
    schedule = Schedule(roomslots, activities, students, courses)

    # dividing students over workinggroups
    schedule.divide_students()

    # checking which algorithm is selected and making a schedule accordingly
    algorithm = sys.argv[1]
    print(f"'{algorithm}' algorithm selected")
    print()
    if algorithm == "randomise":
        best_schedule = randomise(schedule)
    elif algorithm == "baseline":
        best_schedule = baseline(schedule)
    elif algorithm == "greedy":
        best_schedule = gr(schedule)
    elif algorithm == "hillclimber":
        if len(sys.argv) == 3:
            best_schedule = hc(schedule, int(sys.argv[2]))
        else:
            best_schedule = hc(schedule)
    elif algorithm == "simulatedannealing":
        if len(sys.argv) == 3:
            best_schedule = sa(schedule, int(sys.argv[2]))
        else:
            best_schedule = sa(schedule)
    elif algorithm == "genetic":
        best_schedule = gen(schedule)
    else:
        # when no matching algorithm is found exit
        sys.exit('This algorithm does not exist, try: ["randomise", "greedy", "hillclimber", "simulatedannealing", "genetic"]')

    print("Solution found, making output and visualizations")
    print()

    print(f"Maluspoints: {best_schedule.fitness()}")
    print()

    visualize_course(best_schedule, "Bioinformatica")
    print("Course 'Bioinformatica' visualized, see .png in main folder")
    print()

    visualize_student(best_schedule, "52311353")
    print("Student '52311353' visualized, see .png in main folder")
    print()

    best_schedule.output(algorithm)
    print("Solution outputted to csv, see .csv in main folder")
