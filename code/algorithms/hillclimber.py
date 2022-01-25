# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy
import copy
import random

def swap_activities(roomslot1, roomslot2):
    """Swaps the roomslots of two activities"""
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


def move_student(schedule, student_key, from_activity_key, to_activity_key):
    """Moves a student from one activity (tutorial or practicum) to another"""
    # obtain the Activities and Student objects
    from_activity = schedule.activities().single(from_activity_key)
    to_activity = schedule.activities().single(to_activity_key)
    student = schedule.students().single(student_key)

    # removing and adding
    from_activity.remove_student(student_key)
    student.remove_activity(from_activity_key)
    to_activity.add_student(student_key)
    student.add_activity(to_activity_key)


def merge(schedule, activity_to_merge):
    """Merges an activity with other activities, if any"""
    all_activities = schedule.activities()
    activities_to_merge = []

    # find all activities to merge
    for activity in all_activities.list():
        if activity.kind() == activity_to_merge.kind() and activity.course() == activity_to_merge.course():
            activities_to_merge.append(activity)

    # save the activity to keep and the current number of groups
    activity_to_keep = activities_to_merge[0]
    num_of_groups = len(activities_to_merge)

    # if there is more than 1 activity to merge, merge it
    if len(activities_to_merge) > 1:
        activities_to_remove = activities_to_merge[1:]

        # replace students from activities to remove and remove these activities
        for activity in activities_to_remove:
            for student_key in list(activity.students()):
                move_student(schedule, student_key, str(activity), str(activity_to_keep))
                activity.roomslot().remove_activity()
            all_activities.remove_activity(str(activity))

        return activity_to_keep, num_of_groups
    else:
        return activity_to_merge, 1


def mutate(schedule):
    """This function chooses a mutation and then executes it"""
    all_activities = schedule.activities()
    all_roomslots = schedule.roomslots()
    all_students = schedule.students()
    mutation = random.choice([1, 2, 3])

    if mutation == 1:
        # choose two random roomslots and swap their activities
        roomslot1 = random.choice(all_roomslots.list())
        roomslot2 = random.choice(all_roomslots.list())
        swap_activities(roomslot1, roomslot2)

    elif mutation == 2:
        # choose a random student from the schedule
        student = random.choice(all_students.list())
        # these are all activities a student is enrolled in
        activities_keys = student.activities()
        # choose a random activity to move the student from
        from_activity_key = random.choice(activities_keys)
        
        # if the activity is not a lecture, find activities of the same course and kind and swap student to a random one of these
        if all_activities.single(from_activity_key).kind() != "Lecture":
            activities_to_choose = []
            for activity_key in activities_keys:
                if all_activities.single(activity_key).course() == all_activities.single(from_activity_key).course():
                    if all_activities.single(activity_key).kind() == all_activities.single(from_activity_key).kind():
                        activities_to_choose.append(activity_key)
            to_activity_key = random.choice(activities_to_choose)

            if from_activity_key != to_activity_key:
                move_student(schedule, str(student), from_activity_key, to_activity_key)

    elif mutation == 3:
        activity_to_merge = random.choice(all_activities.list())
        if activity_to_merge.kind() != "Lecture":
            activity_to_split, num_of_groups = merge(schedule, activity_to_merge)
            more_or_less = random.choice([-1, 1])
            if num_of_groups != 1:
                new_activities = activity_to_split.split_into(num_of_groups + more_or_less, all_students)
                for activity in new_activities:
                    all_activities.add_activity(activity)
                    while not activity.roomslot():
                        slot = random.choice(all_roomslots.list())
                        if slot.activity():
                            continue
                        else:
                            activity.set_roomslot(slot)


def hill_climber_alg(schedule, mutations=5):
    """The hill climber algorithm"""
    no_change_count = 0
    best_schedule = None

    try:
        while True:
            # copy 'empty' schedule and fill it in by randomising a schedule
            copied_schedule = copy.deepcopy(schedule)
            current_schedule = randomise(copied_schedule)

            while no_change_count < 250:
                # copy the schedule
                new_schedule = copy.deepcopy(current_schedule)

                # make some mutations
                for _ in range(mutations):
                    mutate(new_schedule)

                # if the new schedule is better save it
                if new_schedule.fitness() < current_schedule.fitness():
                    print(new_schedule.fitness())
                    current_schedule = new_schedule
                    no_change_count = 0
                else:
                    # keep track of the amount of iterations without change
                    no_change_count += 1

            if best_schedule:
                if current_schedule.fitness() < best_schedule.fitness():
                    best_schedule = current_schedule
            else:
                best_schedule = current_schedule
            no_change_count = 0

    except KeyboardInterrupt:
        return best_schedule
