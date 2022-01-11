from classes import Room, Roomslot, Activity
from load import load
from algorithms import *

activities, roomslots = load("data/rooms.csv", "data/courses.csv")

random_schedule = random_schedule_two(roomslots, activities)
for slot in random_schedule:
    print(slot)
    if slot.get_activity():
        print(f"Room capacity: {slot.get_room().get_capacity()} and maximum students: {slot.get_activity().get_max_stud()}")


