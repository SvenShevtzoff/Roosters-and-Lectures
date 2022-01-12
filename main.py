'''Usage: main.py [algorithm]'''
import sys
from load import load
from algorithms import *
import pandas as pd
from IPython.display import display

def list_to_df(roomslots):
    df = pd.DataFrame(columns = ["day", "time", "room", "activity"])
    for slot in roomslots:
        if not slot.get_activity():
            df = df.append({"day" : slot.get_day(), "time" : slot.get_time(), "room" : slot.get_room(), "activity" : "No Activity"}, ignore_index = True)
        else:
            df = df.append({"day" : slot.get_day(), "time" : slot.get_time(), "room" : slot.get_room(), "activity" : slot.get_activity()}, ignore_index = True)
    return df

# checking if algorithm is specified
if len(sys.argv) < 2:
    sys.exit(f"Specify the algorithm to make schedule (random_schedule, random_schedule_two, random_schedule_three)")

# loading in data
activities, roomslots = load("data/rooms.csv", "data/courses.csv")

# checking which algorithm is selected and making a schedule accordingly
if sys.argv[1] == "random_schedule":
    schedule = random_schedule(roomslots, activities)
elif sys.argv[1] == "random_schedule_two":
    schedule = random_schedule_two(roomslots, activities)
elif sys.argv[1] == "random_schedule_three":
    schedule = random_schedule_three(roomslots, activities)
else:
    # when no matching algorithm is found exit
    sys.exit("This algorithm does not exist")

# # printing schedule
# for slot in schedule:
#     print(slot)
#     # if slot.get_activity():
#     #     print(f"Room capacity: {slot.get_room().get_capacity()} and maximum students: {slot.get_activity().get_max_stud()}")

df = list_to_df(schedule)

df.to_csv('schedule.csv', index=False)
