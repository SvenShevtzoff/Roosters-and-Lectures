import random
import pandas as pd
from load import load


def random_schedule(roomslots, activities):
    """ Creates a random schedule, not taking into account roomsizes. """
    n = len(activities)
    random_slots = random.sample(roomslots.keys(), n)
    for i in range(n):
        roomslots[random_slots[i]].set_activity(list(activities.values())[i])
    return roomslots


def random_schedule_two(roomslots, activities):
    """ Creates a random schedule, taking into account roomsizes. """
    for activity in list(activities.values()):
        while not activity.get_roomslot():
            slot = roomslots[random.choice(list(roomslots.keys()))]
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)

    return roomslots


def random_schedule_three(roomslots, activities):
    """ Creates a random schedule, taking into account roomsizes and E(studenten) """
    activities = sorted(list(activities.values()), key=lambda x: x.get_max_stud(), reverse=True)
    for activity in activities:
        while not activity.get_roomslot():
            slot = roomslots[random.choice(list(roomslots.keys()))]
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)
    return roomslots


def schedule_with_students(roomslots, activities, students, courses):
    df_students_count = pd.DataFrame(columns=["Course name", "Student count"])
    for course in list(courses.values()):
        df_students_count = df_students_count.append({
            "Course name": course,
            "Student count": courses[course].get_num_of_students()},
            ignore_index=True)




courses, activities, roomslots, students = load("data/rooms.csv", "data/courses.csv", "data/students_and_courses.csv")


schedule_with_students(roomslots, activities, students, courses)
