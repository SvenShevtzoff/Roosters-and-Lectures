'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms import *
from fitness import *

from schedule import Schedule

# from IPython.display import display
from classes import Student



# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit("Specify the algorithm to make schedule \
             (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students)")

# loading in data
courses, activities, roomslots, students = load("data/rooms.csv", "data/courses.csv", "data/students_and_courses.csv")


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

print(x.course_schedule("Technology for games"))
print(x.room_schedule("A1.08"))
print(x.student_schedule("Amos van den Oord"))
print(x.day_schedule("Mon"))
print(x.time_schedule(13))

print(x.fitness())




# display(fitness_function(schedule)[0])
# print(f"Malus points: {fitness_function(schedule)[1]}")

# schedule.to_csv("schedule.csv", index=False)

# maluspunten = fitness_function(schedule)
# print(maluspunten)



# dfSchedule = dict_to_df(schedule)
# # display(dfSchedule.explode('students').sort_values('students'))
# marc = Student("Marc", "Vlasblom", 12345678, [])
# key=lambda marc: marc.__str__()
# print(key)
# dfSchedule = dfSchedule.explode('students').sort_values(by='students', key=lambda student: student.__str__())
# # dfSchedule = dfSchedule.explode('students').groupby('students').agg(["day", "time", "room", "activity"])
# # dfSchedule.to_csv("schedule.csv", index=False)

# dict_to_df(schedule).to_csv('schedule.csv')
# x = Schedule(courses, activities, roomslots, students)
