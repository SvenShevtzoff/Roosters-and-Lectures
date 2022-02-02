# =============================================================================
# greedy.py with greedy algoritm functions
# =============================================================================

def greedy(schedule):
    schedule.divide_students()
    activities = schedule.activities()
    sorted_activities = sorted(activities.list(), key=lambda x: x.num_of_enrolled_students(), reverse=True)
    activities_set = 0
    for activity in sorted_activities:
        for slot in schedule.roomslots().list():
            if not slot.activity() and slot.room().capacity() >= activity.num_of_enrolled_students():
                activity.set_roomslot(slot)
                activities_set += 1
                break

    return schedule
