
def greedy_schedule_one(schedule):
    activities = schedule.get_activities()
    sorted_activities = sorted(activities.get_list(), key=lambda x: x.get_num_of_enrolled_students(), reverse=True)
    activities_set = 0
    for activity in sorted_activities:
        for slot in schedule.get_roomslots().get_list():
            if not slot.get_activity() and slot.get_room().get_capacity() >= activity.get_num_of_enrolled_students():
                activity.set_roomslot(slot)
                activities_set += 1
                break

    return schedule

