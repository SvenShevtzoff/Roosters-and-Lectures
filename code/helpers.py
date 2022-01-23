# =============================================================================
# helpers.py contains different helper functions
# =============================================================================

def swap_activities(activity1, activity2):
    """Swaps the roomslots of two activities"""
    helper = activity1.roomslot()
    activity1.set_roomslot(activity2.roomslot())
    activity2.set_roomslot(helper)

def move_students(student, from_activity, to_activity):
    """Moves a student from one activity to another"""
    from_activity.remove_student(student)
    student.remove_activity(from_activity)
    to_activity.add_student(student)
    student.add_activity(to_activity)

  








