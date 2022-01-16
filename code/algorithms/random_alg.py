import random
from classes.schedule import Schedule
from classes.activities import Activities


def random_schedule(schedule):
    """ Creates a random schedule, not taking into account roomsizes. """
    activities = schedule.get_activities()
    roomslots = schedule.get_roomslots()
    n = activities.length()
    random_slots = random.sample(roomslots.get_list(), n)
    for i in range(n):
        random_slots[i].set_activity(activities.get_list()[i])
    return Schedule(roomslots, Activities(activities))


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

    return Schedule(roomslots, Activities(activities))


def random_schedule_three(schedule):
    """ Creates a random schedule, taking into account roomsizes and E(studenten) """
    activities = schedule.get_activities()
    roomslots = schedule.get_roomslots()
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
    return Schedule(roomslots, Activities(activities))
