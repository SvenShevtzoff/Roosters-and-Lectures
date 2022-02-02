# =============================================================================
# random_alg.py with random algoritm functions
# =============================================================================

import random
        

def randomise(schedule):
    """Creates a random schedule, taking into account roomsizes and E(studenten)"""
    activities = schedule.activities()
    roomslots = schedule.roomslots()

    # give every activity a random roomslot, if this roomslot does not have an activity yet
    for activity in activities:
        while not activity.roomslot():
            slot = random.choice(roomslots.list())
            if slot.activity():
                continue
            else:
                activity.set_roomslot(slot)

    return schedule



