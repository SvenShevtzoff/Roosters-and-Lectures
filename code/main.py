'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import *
from algorithms.greedy_alg import *
from classes.schedule import Schedule
from visualize import visualize_non_student, visualize_student


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule \
             (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students)")

# loading in data
courses, activities, roomslots, students = load("../data/rooms.csv", "../data/courses.csv", "../data/students_and_courses.csv")


# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule(roomslots, activities)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(roomslots, activities)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(roomslots, activities)
elif sys.argv[1] == "schedule_with_students":
    schedule = schedule_with_students(roomslots, activities, courses)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

x = Schedule(roomslots, activities)

# print(x.course_schedule("Bioinformatica"))
# print(x.room_schedule("A1.08"))
# print(x.student_schedule("Yanick Abbing"))
# print(x.day_schedule("Mon"))
# print(x.time_schedule(13))
# print(x.fitness())
print(x.check_conflict("Yanick Abbing"))


visualize_non_student(x.room_schedule("A1.08"))
visualize_student(x.student_schedule("Yanick Abbing"))
