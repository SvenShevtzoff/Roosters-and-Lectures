import random
from math import ceil


def random_schedule_one(schedule):
    """ Creates a random schedule, not taking into account roomsizes. """
    activities = schedule.get_activities()
    roomslots = schedule.get_roomslots()
    n = activities.length()
    random_slots = random.sample(roomslots.get_list(), n)
    for i in range(n):
        activities.get_list()[i].set_roomslot(random_slots[i])
    return schedule


def random_schedule_two(schedule):
    """ Creates a random schedule, taking into account roomsizes. """
    activities = schedule.get_activities()
    roomslots = schedule.get_roomslots()
    for activity in activities.get_list():
        while not activity.get_roomslot():
            slot = random.choice(roomslots.get_list())
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)

    return schedule


def random_schedule_three(schedule):
    """ Creates a random schedule, taking into account roomsizes and E(studenten) """
    activities = schedule.get_activities()
    roomslots = schedule.get_roomslots()
    activities = sorted(activities.get_list(), key=lambda x: x.get_num_of_enrolled_students(), reverse=True)
    for activity in activities:
        while not activity.get_roomslot():
            slot = random.choice(roomslots.get_list())
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)
    return schedule

def baseline(schedule):
    all_activities = schedule.get_activities()
    roomslots = schedule.get_roomslots()
    activities_to_add = []

    for activity in all_activities.get_list():
        if activity.get_kind() != "Lecture":
            amount = ceil(activity.get_num_of_enrolled_students() / activity.get_max_stud())
            if amount > 1:
                new_activities = activity.split_into(amount)

                for activity in new_activities:
                    activities_to_add.append(activity)
    
    for activity in activities_to_add:
        all_activities.add_activity(activity)

    schedule = random_schedule_three(schedule)

    return schedule
