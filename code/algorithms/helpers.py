# =============================================================================
# helpers.py contains different helper functions
# =============================================================================

def swap_activities(roomslot1, roomslot2):
    activity1 = roomslot1.activity()
    activity2 = roomslot2.activity()

    if activity1 and activity2:
        helper = roomslot1
        activity1.set_roomslot(roomslot2)
        activity2.set_roomslot(helper)
    elif not activity1 and activity2:
        activity2.set_roomslot(roomslot1)
        roomslot2.remove_activity()
    elif activity1 and not activity2:
        activity1.set_roomslot(roomslot2)
        roomslot1.remove_activity()
    # else:
    #     pass


def move_student(student, from_activity, to_activity):
    """Moves a student from one activity to another"""
    from_activity.remove_student(student)
    student.remove_activity(from_activity)
    to_activity.add_student(student)
    student.add_activity(to_activity)

