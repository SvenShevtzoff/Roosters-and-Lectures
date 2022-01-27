# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================


import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy as gr
from code.algorithms.hillclimber import hill_climber_alg as hc
from code.algorithms.hillclimber import hill_climber_alg_1000 as hc1000
from code.algorithms.genetic import genetic as gen
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
    schedule = Schedule(roomslots, activities, students)

    schedule.divide_students()

    # checking which algorithm is selected and making a schedule accordingl
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
        best_schedule = gen(schedule)
    else:
        # when no matching algorithm is found exit
        sys.exit('This algorithm does not exist, try: ["randomise", "greedy", "hillclimber", "simulatedannealing", "genetic"]')

    print(f"Pandapunten: {best_schedule.fitness()}")

<<<<<<< HEAD
    best_schedule.visualize_by_room(rooms)
    
=======
    visualize_student(schedule, "52311353")

    # best_schedule.visualize_by_room(rooms)
>>>>>>> 0ef141a0a452bb1b931cd570b6a2b0698288d86b
