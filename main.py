'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms import *
from fitness import *

# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit(f"Specify the algorithm to make schedule (random_schedule, random_schedule_two)")

# loading in data
activities, roomslots = load("data/rooms.csv", "data/courses.csv")

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule(roomslots, activities)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(roomslots, activities)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

# # printing schedule
# for slot in schedule:
#     print(slot)
#     # if slot.get_activity():
#     #     print(f"Room capacity: {slot.get_room().get_capacity()} and maximum students: {slot.get_activity().get_max_stud()}")

df = list_to_df(schedule)
print(df)