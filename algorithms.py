import random


def random_schedule(roomslots, activities):
    """ Creates a random schedule, not taking into account roomsizes. """
    n = len(activities)
    random_slots = random.sample(roomslots, n)
    for i in range(n):
        random_slots[i].set_activity(activities[i])
    return roomslots


def random_schedule_two(roomslots, activities):
    """ Creates a random schedule, taking into account roomsizes. """
    for activity in set(activities):
        while not activity.get_roomslot():
            slot = random.choice(roomslots)
            if slot.get_activity():
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                continue
            else:
                activity.set_roomslot(slot)

    return roomslots
