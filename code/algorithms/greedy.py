# =============================================================================
# greedy.py with greedy algorithm function
# =============================================================================
from code.algorithms.baseline import improve_once

def greedy(schedule):
    """This greedy algorithm sorts activities by number of enrolled students and roomslots by capacity"""
    schedule.divide_students()
    activities = schedule.activities()
    roomslots = schedule.roomslots()

    # sort activities and roomslots
    sorted_activities = sorted(activities.list(), key=lambda x: x.num_of_enrolled_students(), reverse=True)
    sorted_slots = sorted(roomslots.list(), key=lambda x: x.room().capacity(), reverse=True)

    # set roomslot to activity in greedy manner: largest activities and rooms first
    for activity in sorted_activities:
        for slot in sorted_slots:
            if not slot.activity() and slot.room().capacity() >= activity.num_of_enrolled_students():
                activity.set_roomslot(slot)
                break

    # keep improving by one step until there are no students with three gap hours, which makes the schedule valid
    while schedule.empty_roomslot_and_conflict_check()[0][3] > 0:
        fitness = schedule.fitness()
        improve_once(schedule, fitness)

    return schedule
