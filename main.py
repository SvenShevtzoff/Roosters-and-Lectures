'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms import *
<<<<<<< HEAD
<<<<<<< HEAD
from fitness import *
=======
import pandas as pd
from IPython.display import display
from fitness import list_to_df
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053
=======
import pandas as pd
from IPython.display import display
from fitness import list_to_df
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053

# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit(f"Specify the algorithm to make schedule (random_schedule, random_schedule_two, random_schedule_three, schedule_with_students)")

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
    schedule = schedule_with_students(roomslots, activities, students, courses)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

# # printing schedule
# for slot in schedule:
#     print(slot)
#     # if slot.get_activity():
#     #     print(f"Room capacity: {slot.get_room().get_capacity()} and maximum students: {slot.get_activity().get_max_stud()}")
<<<<<<< HEAD
<<<<<<< HEAD

df = list_to_df(schedule)
print(df)
=======

# df = list_to_df(schedule)



# df.to_csv('schedule.csv', index=False)
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053
=======

# df = list_to_df(schedule)



# df.to_csv('schedule.csv', index=False)
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053
