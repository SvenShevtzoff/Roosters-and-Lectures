'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms.random_alg import *
from algorithms.greedy_alg import *
from classes.schedule import Schedule
from visualize import visualize_room, visualize_student, visualize_course
import matplotlib.pyplot as plt


# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule \
             (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students, greedy_schedule_one)")

# loading in data
activities, roomslots, students, courses = load("../data/rooms.csv", "../data/courses.csv", "../data/students_and_courses.csv")

schedule = Schedule(roomslots, activities, students)

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule_one(schedule)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(schedule)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(schedule)
elif sys.argv[1] == "greedy_schedule_one":
    schedule = greedy_schedule_one(schedule)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")



# print(schedule.course_schedule("Bioinformatica"))
# print(schedule.room_schedule("A1.08"))
# print(schedule.student_schedule("Yanick Abbing"))
# print(schedule.day_schedule("Mon"))
# print(schedule.time_schedule(13))
schedule.fitness()

# visualize_room(schedule.room_schedule("A1.08"))
# visualize_student(schedule, "Yanick Abbing")
# counter = 0
# for student in students.get_list():
#     visualize_student(schedule, student)
#     plt.savefig(f"../doc/testing_student/schedule_{student.get_name()}")
#     counter += 1
#     if counter == 10:
#         break
# for slot in roomslots.get_list():
#     if slot.get_time() == 17 and slot.get_activity():
#         visualize_course(schedule, slot.get_course())
#         plt.savefig(f"../doc/testing_course/schedule_{slot.get_course().get_name()}")
# visualize_course(schedule, "Bioinformatica")
