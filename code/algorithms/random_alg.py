import random


def assign_random(schedule):
    """ Creates a random schedule, taking into account roomsizes and E(studenten) """
    activities = schedule.activities()
    roomslots = schedule.roomslots()
    activities = sorted(activities.list(), key=lambda x: x.num_of_enrolled_students(), reverse=True)
    for activity in activities:
        while not activity.roomslot():
            slot = random.choice(roomslots.list())
            if slot.activity():
                continue
            else:
                activity.set_roomslot(slot)


def random_alg(schedule):
    schedule.divide_students()
    assign_random(schedule)
    return schedule


