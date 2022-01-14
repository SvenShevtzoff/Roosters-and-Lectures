import random
import pandas as pd


def random_schedule(roomslots, activities):
    """ Creates a random schedule, not taking into account roomsizes. """
    n = activities.length()
    random_slots = random.sample(roomslots.get_list(), n)
    for i in range(n):
        random_slots[i].set_activity(activities.get_list()[i])
    return roomslots


def random_schedule_two(roomslots, activities):
    """ Creates a random schedule, taking into account roomsizes. """
    for activity in activities.get_list():
        while not activity.get_roomslot():
            slot = random.choice(roomslots.get_list())
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)

    return roomslots


def random_schedule_three(roomslots, activities):
    """ Creates a random schedule, taking into account roomsizes and E(studenten) """
    activities = sorted(activities.get_list(), key=lambda x: x.get_max_stud(), reverse=True)
    for activity in activities:
        while not activity.get_roomslot():
            slot = random.choice(roomslots.get_list())
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)
    return roomslots


def schedule_with_students(roomslots, activities, courses):
    df_students_count = pd.DataFrame(columns=["Course name", "Student count"])
    for course in list(courses.values()):
        students_tutorial = course.get_students()
        students_practicum = course.get_students()
        # df_students_count = df_students_count.append({
        #     "Course name": course,
        #     "Student count": course.get_num_of_students()},
        #     ignore_index=True)
        for activity in course.get_activities():
            if activity.get_kind() == "Lecture":
                activity.set_students(course.get_students())
            if activity.get_kind() == "Tutorial" and not activity.get_students():
                maximum_students = activity.get_max_stud()
                if len(course.get_students()) <= maximum_students:
                    activity.set_students(course.get_student())
    # schedule students to activities


