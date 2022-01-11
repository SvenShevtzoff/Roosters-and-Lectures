import random


def random_schedule(roomslots, activities):
    """ Creates a random schedule, not taking into account class sizes. """
    n = len(activities)
    random_slots = random.sample(roomslots, n)
    for i in range(n):
        random_slots[i].set_activity(activities[i])
    return roomslots


def random_schedule_two(roomslots, activities):
    n = len(activities)
    for i in range(n):
        for j in range(n):
            if 

