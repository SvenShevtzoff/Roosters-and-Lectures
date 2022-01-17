'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import *
from algorithms.greedy_alg import *
from classes.schedule import Schedule
from visualize import visualize, visualize_student


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule \
             (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students)")

# loading in data
activities, roomslots, students = load("../data/rooms.csv", "../data/courses.csv", "../data/students_and_courses.csv")

schedule = Schedule(roomslots, activities, students)

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule(schedule)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(schedule)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(schedule)
# elif sys.argv[1] == "schedule_with_students":
#     schedule = schedule_with_students(roomslots, activities, courses)
elif sys.argv[1] == "algorithm_four":
    schedule = algorithm_four(schedule)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

# print(schedule.course_schedule("Bioinformatica"))
# print(schedule.room_schedule("A1.08"))
# print(schedule.student_schedule("Yanick Abbing"))
# print(schedule.day_schedule("Mon"))
# print(schedule.time_schedule(13))
print(schedule.fitness())

# y = schedule.get_conflicts_student("Yanick Abbing")
# schedule.get_conflicts_course("Bioinformatica")

# visualize(schedule.room_schedule("A1.08"))
visualize_student(schedule, "Yanick Abbing")
