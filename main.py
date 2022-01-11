from classes import Room, Roomslot, Lecture, Tutorial, Practicum
from load import load
from algorithms import *

activities, roomslots = load("data/rooms.csv", "data/courses.csv")

random_schedule = random_schedule(roomslots, activities)
for slot in random_schedule:
    print(slot)


