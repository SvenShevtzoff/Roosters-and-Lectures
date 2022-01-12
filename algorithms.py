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

def random_schedule_three(roomslots, activities):
    """ Creates a random schedule, taking into account roomsizes and E(studenten) """
    activities = sorted(activities, key=lambda x: x.get_max_stud(), reverse=True)
    for ac in activities:
        print(ac)
    for activity in activities:
        # print("1")
        while not activity.get_roomslot():
            # print("2")
            slot = random.choice(roomslots)
            if slot.get_activity():
                # print("3")
                continue
            elif slot.get_room().get_capacity() < activity.get_max_stud():
                # print("4")
                continue
            else:
                # print("5")
                activity.set_roomslot(slot)

    return roomslots
