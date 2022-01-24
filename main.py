# =============================================================================
# main.py:  Usage: main.py [algorithm]
# =============================================================================


import sys
from code.load import load
from code.algorithms.randomise import randomise
from code.classes.schedule import Schedule


if __name__ == "__main__":
    # checking if algorithm is specified
    if len(sys.argv) < 2:
        sys.exit("Specify the algorithm to make schedule (greedy, randomise, baseline)")

    
    #loading data
    activities, roomslots, students, courses, rooms = load(
        "data/rooms.csv",
        "data/courses.csv",
        "data/students_and_courses.csv")
    schedule = Schedule(roomslots, activities, students)
    schedule = randomise(schedule)
    malus_points = schedule.fitness()

    print(f"Pandapunten: {malus_points}")

    # schedule.visualize_by_room(rooms)
