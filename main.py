# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================
import sys
from code.load import load
from code.classes.schedule import Schedule
from code.algorithms.randomise import randomise
from code.algorithms.baseline import randomise_baseline
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.algorithms.genetic import genetic as gen
from code.visualize.visualize import visualize_student, visualize_course


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (randomise, greedy, hillclimber, simulatedannealing, genetic)")

    # loading data
    print()
    print("Loading data and making datastructure")
    
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
    print("Performing algorithm")
    if algorithm == "randomise":
        best_schedule = randomise(schedule)
    elif algorithm == "randomise_baseline":
        best_schedule = randomise_baseline(schedule)
    elif algorithm == "greedy":
        best_schedule = gr(schedule)
    elif algorithm == "hillclimber":
        best_schedule = hc(schedule, 1)
    elif algorithm == "genetic":
        best_schedule = gen(schedule)
    else:
        # when no matching algorithm is found exit
        sys.exit('This algorithm does not exist, try: ["randomise", "randomise_baseline", "greedy", "hillclimber", "genetic"]')

    print("Solution found, making output and visualizations")

    # fitness of best schedule
    print(f"Maluspoints: {best_schedule.fitness()}")

    # schedule of 'Bioinformatica' is visualized, change the name to get a different course
    visualize_course(best_schedule, "Bioinformatica")
    print("Course 'Bioinformatica' visualized, see .png in output folder")

    # schedule of '52311353' is visualized, change the student number to get a different student
    visualize_student(best_schedule, "52311353")
    print("Student '52311353' visualized, see .png in output folder")

    # the entire schedule is visualized by room
    best_schedule.visualize_by_room(rooms)
    print("The whole schedule is visualized by room, see .png's in output folder")

    # the best schedule is outputted to a csv
    best_schedule.output(algorithm)
    print("Solution outputted to csv, see .csv in output folder")
    print()
