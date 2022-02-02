# =============================================================================
# random_alg.py with random algoritm functions
# =============================================================================

import random
        

def randomise(schedule):
    """Creates a random schedule, taking into account roomsizes and E(studenten)"""
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

    return schedule



